# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
from kodimarkdown import converter


class Images(unittest.TestCase):
    def test_simple_image(self):
        md_txt = "![link title](https://url/to/image)"
        kodi_text = "[COLOR yellow][link title][/COLOR]"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_inline_image(self):
        md_txt = "An inline ![image](https://url/to/image) for tests"
        kodi_text = "An inline [COLOR yellow][image][/COLOR] for tests"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_image_link(self):
        md_txt = "An inline [![image](https://url/to/image)](https://url/to/page) for tests"
        kodi_text = "An inline [COLOR blue][COLOR yellow][image][/COLOR][/COLOR] for tests"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
