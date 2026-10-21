#!/usr/bin/env python3
"""Make a short animated WebP preview for every post that does not have one yet.

Source: the MP4 that SandBase Lab mirrors in its own R2 (never X directly).
Output: previews/<post id>.webp, ~3 s, 8 fps, 400 px wide, looping. Existing files are kept,
so a daily run only encodes new posts; previews of posts Lab dropped are deleted.

Needs ffmpeg with libwebp (`brew install ffmpeg` / `apt-get install ffmpeg`). Animated output
comes from the `libwebp_anim` encoder (ffmpeg 4.0+, the one on CI); older builds only ship the
still-image `libwebp` encoder, which still writes ANIM/ANMF frames when given a video stream, so
it is used as a fallback. Both produce the same file format.
"""
import concurrent.futures as cf
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'previews'
VIDEOS = json.loads((ROOT / 'data/videos.json').read_text(encoding='utf-8'))
CLIP_S, FPS, WIDTH, QUALITY = 3, 8, 400, 60
# Preferred first; the fallback only matters on ffmpeg builds predating the animated encoder.
CODECS = ('libwebp_anim', 'libwebp')


def start_at(duration_ms):
    """Skip intros: start 20% in, but always leave room for a full clip."""
    if not duration_ms:
        return 1.0
    total = duration_ms / 1000
    return max(0.0, min(total * 0.2, total - CLIP_S))


def command(v, codec, tmp):
    return ['ffmpeg', '-v', 'error', '-y', '-ss', f'{start_at(v["durationMs"]):.2f}', '-t', str(CLIP_S),
            '-i', v['mp4'], '-an',
            '-vf', f'fps={FPS},scale={WIDTH}:-2:flags=lanczos',
            '-loop', '0', '-c:v', codec, '-quality', str(QUALITY), '-compression_level', '6', str(tmp)]


def encode(v):
    target = OUT / f'{v["id"]}.webp'
    if target.exists():
        return v['id'], 'kept'
    tmp = target.with_suffix('.tmp.webp')
    for codec in CODECS:
        for _ in range(2):
            r = subprocess.run(command(v, codec, tmp), capture_output=True, text=True, timeout=180)
            if r.returncode == 0 and tmp.exists() and tmp.stat().st_size > 1000:
                tmp.replace(target)
                return v['id'], 'made'
            if 'Unknown encoder' in (r.stderr or ''):
                break  # Try the next codec instead of retrying the same unavailable one.
        else:
            tmp.unlink(missing_ok=True)
            return v['id'], f'failed: {r.stderr.strip()[:200]}'
        tmp.unlink(missing_ok=True)
    return v['id'], f'failed: {r.stderr.strip()[:200]}'


def main():
    OUT.mkdir(exist_ok=True)
    wanted = {v['id'] for v in VIDEOS}
    for stale in OUT.glob('*.webp'):
        if stale.stem not in wanted:
            stale.unlink()
    with cf.ThreadPoolExecutor(6) as pool:
        results = list(pool.map(encode, VIDEOS))
    failed = [(i, s) for i, s in results if s.startswith('failed')]
    made = sum(s == 'made' for _, s in results)
    size = sum(p.stat().st_size for p in OUT.glob('*.webp'))
    print(f'Previews: {made} made, {len(results) - made - len(failed)} kept, {len(failed)} failed; total {size / 1e6:.1f} MB.')
    for i, s in failed:
        print(f'  {i}: {s}', file=sys.stderr)
    # Everything failed (e.g. no usable encoder): fail loudly instead of letting
    # validate.py be the first to notice a run that produced nothing.
    if failed and made == 0:
        raise SystemExit(f'All {len(failed)} preview encodes failed')


if __name__ == '__main__':
    main()
