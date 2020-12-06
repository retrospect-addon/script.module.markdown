# SPDX-License-Identifier: GPL-3.0-or-later
# coding: utf-8

import unittest
from kodimarkdown import converter


class Lists(unittest.TestCase):
    def test_bullet_list(self):
        md_txt = "* This is a list item"
        kodi_text = "• This is a list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_plus_list(self):
        md_txt = "+ This is a list item"
        kodi_text = "• This is a list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_dash_list(self):
        md_txt = "- This is a list item"
        kodi_text = "• This is a list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bullet_list_multiple(self):
        md_txt = "* This is a list item\n" \
                 "* Second item"
        kodi_text = "• This is a list item\n" \
                    "• Second item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bullet_nested(self):
        md_txt = "* This is a list item\n" \
                 "  + Second item"
        kodi_text = "• This is a list item\n" \
                    "  - Second item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bullet_list_in_text(self):
        md_txt = "Just a list:\n" \
                 "* This is a list item\n" \
                 "* Second item\n" \
                 "  - Third item\n" \
                 "And more text"
        kodi_text = "Just a list:\n" \
                    "• This is a list item\n" \
                    "• Second item\n" \
                    "  - Third item\n" \
                    "And more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_list_with_emphasis(self):
        md_txt = "* This is a *italic* list item"
        kodi_text = "• This is a [I]italic[/I] list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
