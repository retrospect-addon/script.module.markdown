# SPDX-License-Identifier: GPL-3.0-or-later

import re

__compiled_regex = {}


def to_kodi(text):
    conversions = [
        (r"^# (.+)$", r"[BOLD][LIGHT][UPPERCASE]\1[/UPPERCASE][/LIGHT][/BOLD]"),  # Heading 1
        (r"^## (.+)$", r"[BOLD][LIGHT][CAPITALIZE]\1[/CAPITALIZE][/LIGHT][/BOLD]"),  # Heading 2
    ]

    result = text
    for regex, replacement in conversions:
        compiled = __get_compiled_regex(regex)
        result = compiled.sub(replacement, result)

    return result


def __get_compiled_regex(regex):
    compiled_regex = __compiled_regex.get(regex)
    if compiled_regex:
        return compiled_regex

    compiled_regex = re.compile(regex, re.MULTILINE + re.IGNORECASE)
    __compiled_regex[regex] = compiled_regex
    return compiled_regex
