import unittest

from kodimarkdown import converter


class Text(unittest.TestCase):
    def test_multiline(self):
        md_text = "This is a\n" \
                  "test line."
        kodi_text = "This is a test line."

        result = converter.to_kodi(md_text)
        self.assertEqual(kodi_text, result)
