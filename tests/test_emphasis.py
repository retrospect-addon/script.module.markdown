# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
from kodimarkdown import converter


class Emphasis(unittest.TestCase):
    def test_bold_stars(self):
        md_txt = "Some **bold** text"
        kodi_text = "Some [B]bold[/B] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bold_underscores(self):
        md_txt = "Some __bold__ text"
        kodi_text = "Some [B]bold[/B] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_italic_star(self):
        md_txt = "Some *italic* text"
        kodi_text = "Some [I]italic[/I] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_italic_underscore(self):
        md_txt = "Some _italic_ text"
        kodi_text = "Some [I]italic[/I] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def mixed_emphasis_b_i(self):
        md_txt = "Some **_italic_** text"
        kodi_text = "Some [B][I]italic[/I][/B] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def mixed_emphasis_b_i_all_stars(self):
        md_txt = "Some ***italic*** text"
        kodi_text = "Some [B][I]italic[/I][/B] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def mixed_emphasis_b_i_all_underscores(self):
        md_txt = "Some ___italic___ text"
        kodi_text = "Some [B][I]italic[/I][/B] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def mixed_emphasis_i_underscore_b_stars(self):
        md_txt = "Some _**italic**_ text"
        kodi_text = "Some [I][B]italic[/B][/I] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def mixed_emphasis_i_star_b_underscores(self):
        md_txt = "Some *__italic__* text"
        kodi_text = "Some [I][B]italic[/B][/I] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
