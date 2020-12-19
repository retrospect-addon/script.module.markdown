# SPDX-License-Identifier: GPL-3.0-or-later
# coding: utf-8

import re

__compiled_regex = {}
__replace_count = 0


def to_kodi(text):
    """ Converts the input Markdown text to Kodi formatted text.

    :param str text: The Markdown text.

    :return: A converted Kodi formated text
    :rtype: str
    """

    conversions = [
        (r"\!\[([^]]+?)]\([^)]+?\)", r"[COLOR yellow][\1][/COLOR]", False),  # Images
        (r"\[(.+?)]\(([^)]+?)\)", r"[COLOR blue]\1[/COLOR]", False),  # Links

        (r"^# (.+?)( [#]+)? *$", r"[B][LIGHT][UPPERCASE]\1[/UPPERCASE][/LIGHT][/B]", False),  # Heading 1
        (r"^## (.+?)( [#]+)? *$", r"[B][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/B]", False),  # Heading 2
        (r"^### (.+?)( [#]+)? *$", r"[B][I][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/I][/B]", False),  # Heading 3
        (r"^[#]{4,} (.+?)( [#]+)? *$", r"[B][I][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/I][/B]", False),  # Heading 4

        (r"^[*+-] ((?:.|.\n)+?)(?=(\s*[*+-])|\n{2}|\Z)", r"• \1", True),  # Unordered List Level 1
        (r"^  [*+-] ((?:.|.\n)+?)(?=(\s*[*+-])|\n{2}|\Z)", r"  - \1", True),  # Unordered List Level 2
        # (r"^(\d   +)\. (.+?)(?=[\n]\s*((\d+)\.||[*+-]) |[\n]{2}$|\Z)", r"\1. \2", True),  # Numbered List Level 2
        # (r"^  (\d+)\. (.+?)(?=[\n]\s*((\d+)\.||[*+-]) |[\n]{2}$|\Z)", r"  \1. \2", True),  # Numbered List Level 2

        (r"(__|\*\*)((?!\1)(?:.|.\n)+?)(__|\*\*)", r"[B]\2[/B]", True),  # Italic
        (r"(_|\*)((?!\1)(?:.|.\n)+?)(_|\*)", r"[I]\2[/I]", True),  # Bold
    ]

    result = text
    # Regex Debugging
    # debug_count = 0
    for regex, replacement, multi_line in conversions:
        # Regex Debugging
        # debug_count += 1
        # replacement = "{0}>{1}<{0}".format(debug_count, replacement)
        if multi_line:
            result = re.sub(regex, lambda m: replace_multi_line(m, replacement), result,
                            flags=re.MULTILINE + re.IGNORECASE)
        else:
            result = re.sub(regex, replacement, result,
                            flags=re.MULTILINE + re.IGNORECASE)

    return result


def replace_multi_line(m, replacement):
    match = m.group().replace("\n", " ")
    return m.re.sub(replacement, match)
