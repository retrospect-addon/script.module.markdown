# SPDX-License-Identifier: GPL-3.0-or-later
# coding: utf-8

import re

__compiled_regex = {}


def to_kodi(text):
    """ Converts the input Markdown text to Kodi formatted text.

    :param str text: The Markdown text.

    :return: A converted Kodi formated text
    :rtype: str
    """

    conversions = [
        (r"^# (.+)$", r"[B][LIGHT][UPPERCASE]\1[/UPPERCASE][/LIGHT][/B]"),  # Heading 1
        (r"^## (.+)$", r"[B][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/B]"),  # Heading 2
        (r"^### (.+)$", r"[B][I][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/I][/B]"),  # Heading 3
        (r"^#### (.+)$", r"[B][I][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/I][/B]"),  # Heading 4

        (r"(?:__|\*\*)(.+?)(?:__|\*\*)", r"[B]\1[/B]"),  # Bold
        (r"(?:_|\*)(.+?)(?:_|\*)", r"[I]\1[/I]"),  # Italic
        (r"^[*+-] (.+?)$", r"• \1"),  # List Level 1
        (r"^  [*+-] (.+?)$", r"  - \1"),  # List Level 2
    ]

    result = text
    for regex, replacement in conversions:
        result = re.sub(regex, replacement, result, flags=re.MULTILINE + re.IGNORECASE)

    return result
