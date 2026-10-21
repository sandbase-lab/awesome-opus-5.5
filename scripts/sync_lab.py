#!/usr/bin/env python3
"""Pull the model's collection from SandBase Lab into data/videos.json.

SandBase Lab (CFG['lab_collection']) is the source of truth: it discovers posts on X, reviews
them, and mirrors videos, posters and avatars to its own R2. This repository only mirrors that
public list and links every card back to the Lab page.

  python3 scripts/sync_lab.py            # refuse to shrink the catalog by more than half
  python3 scripts/sync_lab.py --force    # accept any non-empty result
"""
import argparse
import json
import pathlib
import urllib.request

from config import CFG, SITE

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SLUG = CFG['slug']
SOURCE = CFG['lab_data']


def get_json(url: str, timeout: int = 30):
    req = urllib.request.Request(url, headers={'User-Agent': CFG['user_agent'], 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def absolute(path):
    if not path:
        return None
    # Media links always use the public host, even when LAB_ORIGIN points the sync elsewhere.
    return path if path.startswith('http') else SITE + path


def write(path, text):
    path.write_text(text, encoding='utf-8', newline='\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()

    lab = get_json(SOURCE)
    posts = lab.get('posts') or []
    if not posts:
        raise SystemExit(f'Refusing to sync: {SOURCE} returned no posts.')
    DATA.mkdir(exist_ok=True)
    videos_path = DATA / 'videos.json'
    previous = json.loads(videos_path.read_text(encoding='utf-8')) if videos_path.exists() else []
    if previous and len(posts) < len(previous) / 2 and not args.force:
        raise SystemExit(f'Refusing to sync: Lab has {len(posts)} posts, catalog has {len(previous)}. Re-run with --force if intended.')

    featured = lab.get('featured') or []
    videos = []
    for p in posts:
        poster = absolute(p['video'].get('poster'))
        videos.append({
            'id': p['id'],
            'title': p.get('title') or p['text'].split('\n')[0][:80],
            'title_zh': p.get('title_zh') or p.get('title') or p['text'].split('\n')[0][:80],
            'category': p.get('category') or 'showcase',
            'author': {'handle': p['author']['handle'], 'name': p['author']['name']},
            'postUrl': p['url'],
            'createdAt': p['created_at'],
            'durationMs': p['video'].get('duration_ms'),
            'mp4': absolute(p['video']['mp4']),
            'promptShared': bool(p.get('prompt_shared')),
            # Lab shows the post text as the prompt when the creator put it in the post.
            **({'promptText': p['text']} if p.get('prompt_shared') else {}),
            'featured': featured.index(p['id']) if p['id'] in featured else None,
            'poster': poster,
            'labUrl': f'{CFG["lab_collection"]}/{p["id"]}',
        })
    # Like counts change every day; keep them out so an unchanged Lab list means an unchanged repo.
    videos.sort(key=lambda v: (v['createdAt'], v['id']))

    write(videos_path, json.dumps(videos, ensure_ascii=False, indent=1) + '\n')
    write(DATA / 'sync.json', json.dumps({
        'source': f'{SITE}/lab/data/ai-videos/{SLUG}.json',
        # Only Lab's own timestamp: an unchanged Lab list must produce an unchanged repo (no empty daily commits).
        'labSyncedAt': lab.get('synced_at'),
        'count': len(videos),
    }, indent=1) + '\n')
    added = len({v['id'] for v in videos} - {v['id'] for v in previous})
    removed = len({v['id'] for v in previous} - {v['id'] for v in videos})
    print(f'Synced {len(videos)} posts from Lab (lab synced_at {lab.get("synced_at")}): +{added} / -{removed}.')


if __name__ == '__main__':
    main()
