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

    def test_heading_then_link(self):
        md_txt = "# Markdown-to-Kodi formatted text\n[![text (text)](https://url)](url)\ntest"
        kodi_text = "[B][LIGHT][UPPERCASE]Markdown-to-Kodi formatted text[/UPPERCASE][/LIGHT][/B]\n" \
                    "[COLOR blue][COLOR yellow][text (text)][/COLOR][/COLOR]\ntest"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_and_links(self):
        md_txt = """tracker at GitHub.

# Installing Retrospect #
There are two ways to install Retrospect, depending on what version of Kodi you are using.

### Kodi Leia and later
Starting from Kodi Leia (v18), you can easily install Retrospect from the official Kodi add-on repository. Simply use the search function in the add-ons section to find `Retrospect` and install it. More detailed information can be found in the [Retrospect Wiki](https://github.com/retrospect-addon/plugin.video.retrospect/wiki/Installation)."""
        kodi_text = """tracker at GitHub.

[B][LIGHT][UPPERCASE]Installing Retrospect[/UPPERCASE][/LIGHT][/B]
There are two ways to install Retrospect, depending on what version of Kodi you are using.

[B][I][LIGHT][CAPITALIZE]Kodi Leia and later[/CAPITALIZE][/LIGHT][/I][/B]
Starting from Kodi Leia (v18), you can easily install Retrospect from the official Kodi add-on repository. Simply use the search function in the add-ons section to find `Retrospect` and install it. More detailed information can be found in the [COLOR blue]Retrospect Wiki[/COLOR]."""
        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
