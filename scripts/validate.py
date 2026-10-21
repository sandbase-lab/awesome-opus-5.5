#!/usr/bin/env python3
"""Offline checks on the Lab snapshot, the generated READMEs and the docs."""
import json
import re
from pathlib import Path

from config import CFG

ROOT = Path(__file__).resolve().parents[1]
videos = json.loads((ROOT / 'data/videos.json').read_text(encoding='utf-8'))
errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


check(videos, 'catalog is empty')
check(len({v['id'] for v in videos}) == len(videos), 'duplicate post ids')
for v in videos:
    vid = v['id']
    check(re.fullmatch(r'\d+', vid), f'{vid}: bad id')
    check(v['postUrl'].startswith('https://x.com/') and vid in v['postUrl'], f'{vid}: postUrl must be the original X post')
    check(v['labUrl'] == f'{CFG["lab_collection"]}/{vid}', f'{vid}: bad labUrl')
    check(v['title'] and v['title_zh'], f'{vid}: missing title')
    check((ROOT / 'previews' / f'{vid}.webp').exists(), f'{vid}: missing animated preview')
    check(v['mp4'].startswith(CFG['media_prefix']), f'{vid}: video must be served by Lab')
    check('likes' not in v and 'views' not in v, f'{vid}: volatile counters must not be stored')
    if v['poster']:
        check(v['poster'].startswith(CFG['media_prefix']), f'{vid}: poster must come from Lab R2')

featured = sum(v['featured'] is not None for v in videos)
check({p.stem for p in (ROOT / 'previews').glob('*.webp')} == {v['id'] for v in videos}, 'stale previews')
for name, lang in (('README.md', ''), ('README.zh-CN.md', 'lang=zh-CN&')):
    text = (ROOT / name).read_text(encoding='utf-8')
    check(text.count('<td width="33%"') == len(videos) + featured, f'{name}: card count mismatch')
    check(text.count('<details>') == text.count('</details>'), f'{name}: unbalanced <details>')
    for v in videos:
        check(f'{v["labUrl"]}?{lang}utm_source=github' in text, f'{name}: {v["id"]} does not link to its Lab page')

check((ROOT / 'assets/banner.png').exists(), 'missing assets/banner.png')
for doc in ('prompts', 'prompt-guide', 'tutorial', 'model-comparison'):
    for loc in ('', 'zh-CN/'):
        check((ROOT / 'docs' / f'{loc}{doc}.md').exists(), f'missing docs/{loc}{doc}.md')
        check(f'docs/{loc}{doc}.md' in (ROOT / ('README.zh-CN.md' if loc else 'README.md')).read_text(encoding='utf-8'), f'README does not link docs/{loc}{doc}.md')

# Leak guard: no local paths or key-like strings, and nothing carried over from the sibling list
# this repository was modelled on. Patterns are split so this file does not match itself.
forbidden = re.compile('|'.join([
    r'/Users/', r'/Volumes/', r'\b[A-Za-z]:\\',
    r'sk-sb-[A-Za-z0-9]{8,}', r'\bsk-[a-f0-9]{32,}', 'cfut' + '_',
    re.escape('utm_campaign=awesome-' + 'minimax-m3-1-flash'),
    re.escape('/lab/ai-videos/' + 'minimax-m3-1-flash/'),
]))
scanned = [ROOT / 'README.md', ROOT / 'README.zh-CN.md', ROOT / 'CONTRIBUTING.md', ROOT / 'MEDIA-RIGHTS.md',
           *(ROOT / 'docs').rglob('*.md'), *(ROOT / 'scripts').glob('*.*'), *(ROOT / '.github').rglob('*.yml')]
for path in scanned:
    if path.name == 'validate.py' or path.suffix == '.pyc':
        continue
    hit = forbidden.search(path.read_text(encoding='utf-8'))
    check(not hit, f'{path.relative_to(ROOT).as_posix()}: contains a local path, a key or a sibling-list link ({hit.group(0) if hit else ""})')

if errors:
    print('\n'.join(f'FAIL: {e}' for e in errors[:50]))
    raise SystemExit(f'{len(errors)} problem(s)')
print(f'PASS: {len(videos)} posts ({featured} featured), every card links to SandBase Lab in both READMEs.')
