"""Validate public Lab media references independently of collection ownership."""
import re
from urllib.parse import urlsplit


def is_lab_media(url, kind):
    """Accept public R2 objects; collection page links are checked separately."""
    if not isinstance(url, str) or kind not in ('video', 'poster'):
        return False
    # Reject characters URL parsers normalize, credentials, queries and fragments.
    if re.search(r'[\s\\?#%]', url):
        return False
    try:
        parsed = urlsplit(url)
    except ValueError:
        return False
    if parsed.scheme != 'https' or parsed.netloc != 'www.sandbase.ai':
        return False
    prefix = '/lab/media/'
    if not parsed.path.startswith(prefix):
        return False
    key = parsed.path[len(prefix):]
    if not key.startswith(('x/', 'static/downloads/')):
        return False
    if not all(re.fullmatch(r'[a-zA-Z0-9_][a-zA-Z0-9._-]*', part)
               for part in key.split('/')):
        return False
    extensions = r'\.(mp4|webm)' if kind == 'video' else r'\.(jpg|jpeg|png|webp|avif)'
    return bool(re.search(extensions + r'$', key, re.IGNORECASE))
