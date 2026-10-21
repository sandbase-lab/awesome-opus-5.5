#!/usr/bin/env python3
"""Generate README.md, README.zh-CN.md and docs/prompts.md (en + zh-CN) from data/videos.json."""
import html
import json
import pathlib

from config import CATEGORIES, CFG, COPY, utm

ROOT = pathlib.Path(__file__).resolve().parents[1]
VIDEOS = json.loads((ROOT / 'data/videos.json').read_text(encoding='utf-8'))
MODEL_ID = CFG['model_id']
UTM = utm('readme')
DOC_UTM = utm('docs')
BLOG_UTM = utm('readme', 'reading')
LAB = CFG['lab_collection']
VISIBLE = 6  # cards per category shown before "show all"
# SandBase blog posts are optional: a model that shipped days ago may have none yet, and the list
# must not invent links (see CFG['reading'] in config.py). Everything reading-related is skipped.
HAS_READING = bool(CFG['reading'])


def lab(path='', loc='en', content=None):
    q = ('lang=zh-CN&' if loc == 'zh-CN' else '') + UTM + (f'&utm_content={content}' if content else '')
    return f'{LAB}{path}?{q}'


def blog(slug, loc):
    base = 'https://blog.sandbase.ai/zh-CN/' if loc == 'zh-CN' else 'https://blog.sandbase.ai/'
    return f'{base}{slug}/?{BLOG_UTM}'


def reading(loc):
    zh = loc == 'zh-CN'
    return [f'- [{zt if zh else et}]({blog(slug, loc)})' for slug, et, zt in CFG['reading']]


def links(loc):
    lang = 'lang=zh-CN&' if loc == 'zh-CN' else ''
    return {
        'name': CFG['name'], 'short': CFG['short'], 'model_id': MODEL_ID, 'html_out': CFG['html_out'],
        'guide_patterns': CFG['guide_patterns'], 'repo_url': CFG['repo_url'],
        'not_affiliated': CFG['not_affiliated'][loc],
        'lab_stats': lab(loc=loc, content='stats'), 'lab_quickstart': lab(loc=loc, content='quickstart'),
        'lab_recreate': lab(loc=loc, content='recreate'), 'lab_section': lab(loc=loc, content='section'),
        'arena_quickstart': f'{CFG["arena"]}&{lang}{UTM}&utm_content=quickstart',
        'model_page': f'{CFG["model_page"]}?{UTM}', 'keys': f'{CFG["keys"]}?{UTM}', 'sandbox': f'{CFG["sandbox"]}?{UTM}',
        'evals': f'{CFG["evals"]}?{lang}{UTM}', 'pelican': f'{CFG["pelican"]}?{lang}{UTM}',
        'blog_update': blog(CFG['reading'][0][0], loc) if HAS_READING else '',
        'lab_home': f'{CFG["lab_home"]}?{lang}{UTM}', 'all_collections': f'{CFG["all_collections"]}?{lang}{UTM}',
    }


def localize(loc):
    """COPY[loc] with every {placeholder} filled; strings that need counts stay templates."""
    ctx = links(loc)
    fill = lambda s: s.format(**ctx)
    t = {}
    for k, v in COPY[loc].items():
        if k in ('stats', 'show_all', 'more', 'p_intro'):
            t[k] = (lambda tpl: lambda **n: tpl.format(**ctx, **n))(v)
        elif isinstance(v, list):
            t[k] = [tuple(fill(x) for x in item) if isinstance(item, tuple) else fill(item) for item in v]
        else:
            t[k] = fill(v)
    t['h1'] = f'Awesome {CFG["name"]}'
    return t


T = {loc: localize(loc) for loc in ('en', 'zh-CN')}

CURL = '''```bash
jq -n --rawfile prompt prompt.txt \\
  '{model: "%s", max_tokens: %d, messages: [{role: "user", content: $prompt}]}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \\
  -H "Authorization: Bearer $SANDBASE_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d @- | jq -r '.choices[0].message.content' | sed '/^```/d' > %s
```''' % (MODEL_ID, CFG['max_tokens'], CFG['html_out'])


def length(ms):
    if not ms:
        return None
    s = round(ms / 1000)
    return f'{s // 60}:{s % 60:02d}'


def card(v, loc):
    title = v['title_zh'] if loc == 'zh-CN' else v['title']
    page = lab(f'/{v["id"]}', loc, 'card')
    alt = html.escape(title, quote=True)
    # The animated preview opens the video file itself (served by Lab); the title opens the Lab page.
    picture = f'<a href="{v["mp4"]}"><img src="previews/{v["id"]}.webp" alt="{alt}" width="100%"></a><br>'
    meta = [f'<a href="{v["postUrl"]}">@{html.escape(v["author"]["handle"])}</a>']
    if length(v['durationMs']):
        meta.append(length(v['durationMs']))
    if v['promptShared']:
        meta.append(f'<a href="{page}">{T[loc]["prompt_tag"]}</a>')
    return (f'<td width="33%" valign="top">{picture}<a href="{page}"><b>{html.escape(title)}</b></a>'
            f'<br><sub>{" · ".join(meta)}</sub></td>')


def table(group, loc):
    rows = ['<table>']
    for i in range(0, len(group), 3):
        rows.append('<tr>' + ''.join(card(v, loc) for v in group[i:i + 3]) + '</tr>')
    return rows + ['</table>']


def readme(loc):
    t = T[loc]
    zh = loc == 'zh-CN'
    creators = len({v['author']['handle'].lower() for v in VIDEOS})
    prompts = sum(v['promptShared'] for v in VIDEOS)
    cats = sorted({v['category'] for v in VIDEOS}, key=lambda c: (list(CATEGORIES).index(c) if c in CATEGORIES else 99, c))
    featured = sorted((v for v in VIDEOS if v['featured'] is not None), key=lambda v: v['featured'])
    name = lambda c: CATEGORIES.get(c, (c, c))[1 if zh else 0]
    actions = f'{CFG["repo_url"]}/actions/workflows/sync.yml'
    badges = ' '.join([
        '[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)',
        f'[![Videos](https://img.shields.io/badge/videos-{len(VIDEOS)}-blue)](#contents)',
        f'[![Prompts](https://img.shields.io/badge/prompts-{prompts}-green)]({"docs/zh-CN/prompts.md" if zh else "docs/prompts.md"})',
        f'[![Sync]({actions}/badge.svg)]({actions})',
        f'[![Run on SandBase](https://img.shields.io/badge/run%20on-SandBase-black)]({CFG["model_page"]}?{UTM})',
    ])
    lines = [f'# {t["h1"]}', '', t['switch'], '', badges, '',
             f'[![{t["alt"]}](assets/banner.png)]({lab(loc=loc, content="banner")})', '',
             t['tagline'], '', t['stats'](n=len(VIDEOS), a=creators, p=prompts), '',
             f'## {t["start"]}', '', f'| {t["goal"]} | {t["where"]} |', '|---|---|',
             *[f'| {a} | {b} |' for a, b in t['start_rows']], '',
             '<a id="contents"></a>', '', f'## {t["contents"]}', '']
    if featured:
        lines.append(f'- [{t["featured"]}](#featured) ({len(featured)})')
    lines += [f'- [{name(c)}](#{c}) ({sum(v["category"] == c for v in VIDEOS)})' for c in cats]
    lines += [f'- [{t["recreate"]}](#recreate)', f'- [{t["faq"]}](#faq)']
    if HAS_READING:
        lines.append(f'- [{t["reading"]}](#reading)')
    lines += [f'- [{t["contribute"]}](#contribute)', '', t['how'], '']
    if featured:
        lines += ['<a id="featured"></a>', '', f'## {t["featured"]}', '', *table(featured, loc), '']
    for c in cats:
        group = [v for v in VIDEOS if v['category'] == c]
        lines += [f'<a id="{c}"></a>', '', f'## {name(c)}', '', *table(group[:VISIBLE], loc), '']
        if len(group) > VISIBLE:
            lines += ['<details>', f'<summary><b>{t["show_all"](n=len(group))}</b></summary>', '', *table(group[VISIBLE:], loc), '', '</details>', '']
    lines += [t['more'](n=len(VIDEOS)), '',
              '<a id="recreate"></a>', '', f'## {t["recreate"]}', '', *t['recreate_body'], '', CURL, '', t['recreate_after'], '',
              '<a id="faq"></a>', '', f'## {t["faq"]}', '']
    for q, a in t['faq_items']:
        lines += [f'### {q}', '', a, '']
    if HAS_READING:
        lines += ['<a id="reading"></a>', '', f'## {t["reading"]}', '', t['reading_intro'], '', *reading(loc), '']
    lines += ['<a id="contribute"></a>', '', f'## {t["contribute"]}', '', t['contribute_body'], '', f'## {t["credits"]}', '']
    for p in t['credits_body']:
        lines += [p, '']
    lines += ['---', '', t['footer'], '']
    return '\n'.join(lines)


def fence(text):
    """A code fence longer than any backtick run inside the creator's text."""
    longest = run = 0
    for ch in text:
        run = run + 1 if ch == '`' else 0
        longest = max(longest, run)
    tick = '`' * max(3, longest + 1)
    return f'{tick}text\n{text}\n{tick}'


def prompt_index(loc):
    t = T[loc]
    zh = loc == 'zh-CN'
    rows = [v for v in VIDEOS if v['promptShared']]
    cats = sorted({v['category'] for v in rows}, key=lambda c: (list(CATEGORIES).index(c) if c in CATEGORIES else 99, c))
    cname = lambda c: CATEGORIES.get(c, (c, c))[1 if zh else 0]
    lines = [f'# {t["p_title"]}', '', t['p_switch'], '', t['p_intro'](n=len(rows)), '', t['p_note'], '']
    lines += [f'- [{cname(c)}](#{c}) ({sum(v["category"] == c for v in rows)})' for c in cats] + ['']
    for c in cats:
        lines += [f'<a id="{c}"></a>', '', f'## {cname(c)}', '']
        for v in (v for v in rows if v['category'] == c):
            title = v['title_zh'] if zh else v['title']
            page = lab('/' + v['id'], loc, 'prompt-index').replace(UTM, DOC_UTM)
            meta = [f'[@{v["author"]["handle"]}]({v["postUrl"]})']
            if length(v['durationMs']):
                meta.append(length(v['durationMs']))
            meta += [f'[{t["p_watch"]}]({v["mp4"]})', f'[{t["p_open"]}]({page})']
            lines += [f'### {title}', '', ' · '.join(meta), '', fence(v['promptText']), '']
    return '\n'.join(lines)


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')


def main():
    write('README.md', readme('en'))
    write('README.zh-CN.md', readme('zh-CN'))
    write('docs/prompts.md', prompt_index('en'))
    write('docs/zh-CN/prompts.md', prompt_index('zh-CN'))
    print(f'Built two READMEs with {len(VIDEOS)} cards each.')


if __name__ == '__main__':
    main()
