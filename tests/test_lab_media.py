"""Regression coverage for shared R2 objects and public URL boundaries."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from lab_media import is_lab_media


class LabMediaTests(unittest.TestCase):
    def test_shared_objects_remain_valid_for_every_collection(self):
        for key, kind in (
            ('x/gemini-4-hydrogen/2121030005899825504/video.mp4', 'video'),
            ('x/gemini-4-hydrogen/2121030005899825504/poster.jpg', 'poster'),
            ('x/gemini-4-carbon/123/video.webm', 'video'),
            ('static/downloads/example/v2/clip.mp4', 'video'),
            ('static/downloads/example/v2/poster.webp', 'poster'),
        ):
            with self.subTest(key=key):
                self.assertTrue(is_lab_media('https://www.sandbase.ai/lab/media/' + key, kind))

    def test_external_and_non_media_urls_are_rejected(self):
        good = 'https://www.sandbase.ai/lab/media/x/example/123/video.mp4'
        for url in (
            None, '', good.replace('https:', 'http:'),
            good.replace('www.sandbase.ai', 'www.sandbase.ai.evil.example'),
            good.replace('www.sandbase.ai', 'user@www.sandbase.ai'),
            good.replace('www.sandbase.ai', 'www.sandbase.ai:443'),
            good.replace('/media/x/', '/media/private/'),
            good.replace('/media/x/', '/media/'),
            good.replace('/example/', '/example/../'),
            good.replace('/example/', '/example/%2e%2e/'),
            good.replace('/example/', '/example//'),
            good.replace('/example/', '/example\\'),
            good + '?download=1', good + '#preview', good + '\n',
            good.replace('www.', 'www.\t'),
            good.replace('video.mp4', 'video.html'),
        ):
            with self.subTest(url=url):
                self.assertFalse(is_lab_media(url, 'video'))

    def test_media_type_is_preserved(self):
        self.assertFalse(is_lab_media(
            'https://www.sandbase.ai/lab/media/x/example/123/poster.jpg', 'video'))
        self.assertFalse(is_lab_media(
            'https://www.sandbase.ai/lab/media/x/example/123/video.mp4', 'poster'))


if __name__ == '__main__':
    unittest.main()
