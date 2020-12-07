# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
from kodimarkdown import converter


class Images(unittest.TestCase):
    def test_simple_image(self):
        md_txt = "![link title](https://url/to/page)"
        kodi_text = "[COLOR yellow][link title][/COLOR]"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_inline_image(self):
        md_txt = "An inline ![image](https://url/to/page) for tests"
        kodi_text = "An inline [COLOR yellow][image][/COLOR] for tests"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
