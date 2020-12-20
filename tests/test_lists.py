# SPDX-License-Identifier: GPL-3.0-or-later
# coding: utf-8

import unittest
from kodimarkdown import converter


class Lists(unittest.TestCase):
    def test_bullet_list(self):
        md_txt = "* This is a list item"
        kodi_text = " • This is a list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_plus_list(self):
        md_txt = "+ This is a list item"
        kodi_text = " • This is a list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_dash_list(self):
        md_txt = "- This is a list item"
        kodi_text = " • This is a list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bullet_list_multiple(self):
        md_txt = "* This is a list item\n" \
                 "* Second item"
        kodi_text = " • This is a list item\n" \
                    " • Second item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bullet_list_multiple_multiline(self):
        md_txt = "* This is a list\n" \
                 "item\n" \
                 "* Second item"
        kodi_text = " • This is a list item\n" \
                    " • Second item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bullet_nested(self):
        md_txt = "* This is a list item\n" \
                 "  + Second item\n" \
                 "    + Second item"
        kodi_text = " • This is a list item\n" \
                    "   - Second item\n" \
                    "     - Second item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_bullet_list_in_text(self):
        md_txt = "Just a list:\n" \
                 "* This is a list item\n" \
                 "* Second item\n" \
                 "  - Third item\n" \
                 "\n" \
                 "And more text"
        kodi_text = "Just a list:\n" \
                    " • This is a list item\n" \
                    " • Second item\n" \
                    "   - Third item\n" \
                    "\n" \
                    "And more text"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_list_with_emphasis(self):
        md_txt = "* This is a *italic* list item"
        kodi_text = " • This is a [I]italic[/I] list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_numbered_list(self):
        md_txt = "1. This is a numbered list item"
        kodi_text = " 1. This is a numbered list item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_numbered_list_nested(self):
        md_txt = "1. This is a numbered list item\n" \
                 "  1. This is a nested numbered item\n" \
                 "    1. This is a nested numbered item"
        kodi_text = " 1. This is a numbered list item\n" \
                    "   1. This is a nested numbered item\n" \
                    "     1. This is a nested numbered item"
        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_numbered_list_nested_multiline(self):
        md_txt = "1. This is a numbered\n" \
                 "list\n" \
                 "item\n" \
                 "  1. This is a nested numbered item"
        kodi_text = " 1. This is a numbered list item\n" \
                    "   1. This is a nested numbered item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_numbered_list_nested_multiline_level2(self):
        md_txt = "1. This is a numbered list item\n" \
                 "  1. This is a nested\n" \
                 "numbered\n" \
                 "item"
        kodi_text = " 1. This is a numbered list item\n" \
                    "   1. This is a nested numbered item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)

    def test_combined_list(self):
        md_txt = "1. This is a numbered list item\n" \
                 "  + This is a nested unordered item"
        kodi_text = " 1. This is a numbered list item\n" \
                    "   - This is a nested unordered item"

        result = converter.to_kodi(md_txt)
        self.assertEqual(kodi_text, result)
