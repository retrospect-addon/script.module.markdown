# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
from kodimarkdown import converter


class HeadingTest(unittest.TestCase):
    def test_heading_1_line(self):
        md_txt = "# This is a heading 1"
        kodi_text = "[B][LIGHT][UPPERCASE]This is a heading 1[/UPPERCASE][/LIGHT][/B]"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_1_multiline(self):
        md_txt = "# This is a heading 1\n\n" \
                 "And this is more text"
        kodi_text = "[B][LIGHT][UPPERCASE]This is a heading 1[/UPPERCASE][/LIGHT][/B]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_1_multiline_middle(self):
        md_txt = "Pre-text\n\n" \
                 "# This is a heading 1\n\n" \
                 "And this is more text"
        kodi_text = "Pre-text\n\n" \
                    "[B][LIGHT][UPPERCASE]This is a heading 1[/UPPERCASE][/LIGHT][/B]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_2_line(self):
        md_txt = "## This is a heading 2"
        kodi_text = "[B][LIGHT][CAPITALIZE]This is a heading 2[/CAPITALIZE][/LIGHT][/B]"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_2_multiline(self):
        md_txt = "## This is a heading 2\n\n" \
                 "And this is more text"
        kodi_text = "[B][LIGHT][CAPITALIZE]This is a heading 2[/CAPITALIZE][/LIGHT][/B]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_2_multiline_middle(self):
        md_txt = "Pre-text\n\n" \
                 "## This is a heading 2\n\n" \
                 "And this is more text"
        kodi_text = "Pre-text\n\n" \
                    "[B][LIGHT][CAPITALIZE]This is a heading 2[/CAPITALIZE][/LIGHT][/B]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_3_line(self):
        md_txt = "### This is a heading 3"
        kodi_text = "[LIGHT][CAPITALIZE]This is a heading 3[/CAPITALIZE][/LIGHT]"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_3_multiline(self):
        md_txt = "### This is a heading 3\n\n" \
                 "And this is more text"
        kodi_text = "[LIGHT][CAPITALIZE]This is a heading 3[/CAPITALIZE][/LIGHT]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_3_multiline_middle(self):
        md_txt = "Pre-text\n\n" \
                 "### This is a heading 3\n\n" \
                 "And this is more text"
        kodi_text = "Pre-text\n\n" \
                    "[LIGHT][CAPITALIZE]This is a heading 3[/CAPITALIZE][/LIGHT]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_4_line(self):
        md_txt = "#### This is a heading 4"
        kodi_text = "[LIGHT][CAPITALIZE]This is a heading 4[/CAPITALIZE][/LIGHT]"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_4_multiline(self):
        md_txt = "#### This is a heading 4\n\n" \
                 "And this is more text"
        kodi_text = "[LIGHT][CAPITALIZE]This is a heading 4[/CAPITALIZE][/LIGHT]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_4_multiline_middle(self):
        md_txt = "Pre-text\n\n" \
                 "#### This is a heading 4\n\n" \
                 "And this is more text"
        kodi_text = "Pre-text\n\n" \
                    "[LIGHT][CAPITALIZE]This is a heading 4[/CAPITALIZE][/LIGHT]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_heading_1_2_3_mixed(self):
        md_txt = "# Main heading\n\n" \
                 "## Second heading\n\n" \
                 "### Third heading\n\n" \
                 "And this is more text"
        kodi_text = "[B][LIGHT][UPPERCASE]Main heading[/UPPERCASE][/LIGHT][/B]\n\n" \
                    "[B][LIGHT][CAPITALIZE]Second heading[/CAPITALIZE][/LIGHT][/B]\n\n" \
                    "[LIGHT][CAPITALIZE]Third heading[/CAPITALIZE][/LIGHT]\n\n" \
                    "And this is more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
