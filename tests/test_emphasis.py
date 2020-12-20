# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
from kodimarkdown import converter


class Emphasis(unittest.TestCase):
    def test_bold_stars(self):
        md_txt = "Some **bold** text"
        kodi_text = "Some [B]bold[/B] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bold_stars_multiline(self):
        md_txt = "Just start text\n" \
                 "\n" \
                 "Some **bo\n" \
                 "ld** text"
        kodi_text = "Just start text\n" \
                    "\n" \
                    "Some [B]bo ld[/B] text"

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

    def test_italic_double(self):
        md_txt = "Some *italic* text and some more *italic* text"
        kodi_text = "Some [I]italic[/I] text and some more [I]italic[/I] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_italic_multiline(self):
        md_txt = "Just start text\n" \
                 "\n" \
                 "Some _bo\n" \
                 "ld_ text"
        kodi_text = "Just start text\n" \
                    "\n" \
                    "Some [I]bo ld[/I] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_mixed_emphasis_b_i(self):
        md_txt = "Some **_italic_** text"
        kodi_text = "Some [B][I]italic[/I][/B] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_mixed_emphasis_i_underscore_b_stars(self):
        md_txt = "Some _**italic**_ text"
        kodi_text = "Some [I][B]italic[/B][/I] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_mixed_emphasis_i_star_b_underscores(self):
        md_txt = "Some *__italic__* text"
        kodi_text = "Some [I][B]italic[/B][/I] text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_adjecent_emphasis(self):
        md_txt = "Some *italic**text*"
        kodi_text = "Some [I]italic[/I][I]text[/I]"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_just_a_star(self):
        md_txt = "1. From that recovery image, you will need the Widevine files located in /opt/google/chrome/libwidevinecdm*.so.\n" \
                 "1. These files need to be copied to the `<kodi-profile>/cdm` folder.\n\n_"
        kodi_text = " 1. From that recovery image, you will need the Widevine files located in /opt/google/chrome/libwidevinecdm*.so.\n" \
                    " 1. These files need to be copied to the `<kodi-profile>/cdm` folder.\n\n_"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
