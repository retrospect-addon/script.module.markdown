# SPDX-License-Identifier: GPL-3.0-or-later

import re

__compiled_regex = {}


def to_kodi(text):
    """ Converts the input Markdown text to Kodi formatted text.

    :param str text: The Markdown text.

    :return: A converted Kodi formated text
    :rtype: str
    """

    conversions = [
        (r"^# (.+)$", r"[BOLD][LIGHT][UPPERCASE]\1[/UPPERCASE][/LIGHT][/BOLD]"),  # Heading 1
        (r"^## (.+)$", r"[BOLD][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/BOLD]"),  # Heading 2
        (r"^### (.+)$", r"[LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT]"),  # Heading 2
        (r"^#### (.+)$", r"[LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT]"),  # Heading 2
    ]

    result = text
    for regex, replacement in conversions:
        result = re.sub(regex, replacement, result, flags=re.MULTILINE + re.IGNORECASE)

    return result
