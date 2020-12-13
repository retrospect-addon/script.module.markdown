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
        (r"^# (.+?)( [#]+)? *$", r"[B][LIGHT][UPPERCASE]\1[/UPPERCASE][/LIGHT][/B]", False),  # Heading 1
        (r"^## (.+?)( [#]+)? *$", r"[B][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/B]", False),  # Heading 2
        (r"^### (.+?)( [#]+)? *$", r"[B][I][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/I][/B]", False),  # Heading 3
        (r"^[#]{4,} (.+?)( [#]+)? *$", r"[B][I][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/I][/B]", False),  # Heading 4

        (r"^[*+-] (.+?)$", r"• \1", False),  # Unordered List Level 1
        (r"^  [*+-] (.+?)$", r"  - \1", False),  # Unordered List Level 2
        (r"^(\d+)\. (.+?)$", r"\1. \2", False),  # Numbered List Level 2
        (r"^  (\d+)\. (.+?)$", r"  \1. \2", False),  # Numbered List Level 2

        (r"(?:__|\*\*)(.+?)(?:__|\*\*)", r"[B]\1[/B]", True),  # Bold
        (r"(?:_|\*)(.+?)(?:_|\*)", r"[I]\1[/I]", True),  # Italic

        (r"\!\[([^]]+)]\([^)]+\)", r"[COLOR yellow][\1][/COLOR]", False),  # Images
        (r"\[(.+)]\(([^)]+)\)", r"[COLOR blue]\1[/COLOR]", False),  # Links
    ]

    result = text
    for regex, replacement, multi_line in conversions:
        if multi_line:
            result = re.sub(regex, lambda m: replace_multi_line(m, replacement), result,
                            flags=re.MULTILINE + re.IGNORECASE + re.DOTALL)
        else:
            result = re.sub(regex, replacement, result,
                            flags=re.MULTILINE + re.IGNORECASE)

    return result


def replace_multi_line(m, replacement):
    match = m.group().replace("\n", " ")
    return m.re.sub(replacement, match)
