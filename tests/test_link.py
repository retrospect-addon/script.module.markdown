# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
from kodimarkdown import converter


class Links(unittest.TestCase):
    def test_simple_link(self):
        md_txt = "[link title](https://url/to/page)"
        kodi_text = "[COLOR blue]link title[/COLOR]"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_link_in_text(self):
        md_txt = "A simple link to a [site](https://url/to/page) with info"
        kodi_text = "A simple link to a [COLOR blue]site[/COLOR] with info"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
