# Markdown-to-Kodi formatted text
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/retrospect-addon/script.module.markdown)](https://github.com/retrospect-addon/script.module.markdown/releases)
[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/retrospect-addon/script.module.markdown/unit-tests/master)](https://github.com/retrospect-addon/script.module.markdown/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=retrospect-addon_script.module.markdown&metric=alert_status)](https://sonarcloud.io/dashboard?id=retrospect-addon_script.module.markdown)
[![License](https://img.shields.io/github/license/retrospect-addon/script.module.markdown)](https://github.com/retrospect-addon/script.module.markdown/blob/master/LICENSE.md)
[![Python](https://img.shields.io/badge/python-2.7%20%7C%203.6%2D-3.8-blue?logo=python)](https://kodi.tv/article/attention-addon-developers-migration-python-3)

This simple library for [Kodi](https://kodi.tv) converts basic [Markdown](https://daringfireball.net/projects/markdown) to valid Kodi formatted text (See [here](https://kodi.wiki/view/Label_Formatting)).

## Supported Markdown Syntax
The basic Markdown [syntax](https://daringfireball.net/projects/markdown/syntax) is supported. The aim is to eventually also support the majority of the [GitHub flavoured markdown](https://github.github.com/gfm/). A cheatsheet can be found at [GitHub](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf).


### Basic Markdown Syntax
The following table has an overview of the supported syntax:

Description  | Markdown     | Kodi formatted text
------------ | ------------ | -------------
Heading 1    | `#`          | `[B][LIGHT][UPPERCASE]`
Heading 2    | `##`         | `[B][LIGHT][CAPITALIZE]`
Heading 3    | `###`        | `[LIGHT][CAPITALIZE]`
Heading 4    | `####`       | `[LIGHT][CAPITALIZE]`
Bold         | `**bold**` or `__bold__` | `[B]bold[/B]`
Italic       | `*bold*` or `_bold_` | `[I]bold[/I]`
Link         | `[text](url)` | `[COLOR blue]text[/COLOR]`
Image        | `![text](url)` | `[COLOR yellow][text][/COLOR]`

### Lists
Ordered and unordered lists are supported. However, ordered lists need to have proper numbering. Output for numbered lists is:

    1. Ordered List Level 1         |    1. Ordered List Level 1
    2. Ordered List Level 1         |    2. Ordered List Level 1
      1. Ordered List Level 2       |      1. Ordered List Level 2
      2. Ordered List Level 2       |      2. Ordered List Level 2

For unordered lists, the chars `*`, `+` and `-` can be used. The Kodi formatted output will be:

    - Unordered Level 1             |    • Ordered List Level 1
    + Unordered  Level 1            |    • Ordered List Level 1
    * Unordered Level 1             |    • Ordered List Level 1
      + Unordered Level 2           |      - Ordered List Level 2
      - Unordered List Level 2      |      - Ordered List Level 2
      * Unordered List Level 2      |      - Ordered List Level 2

List styles can be combined:

    - Unordered Level 1             |    • Ordered List Level 1
    - Unordered Level 1             |    • Ordered List Level 1
      1. Ordered List Level 2       |      1. Ordered List Level 2
      2. Ordered List Level 2       |      2. Ordered List Level 2

## Not Supported:
Description  | Remark
------------ | -------------
Tables       | _Will be removed completely_.
Images       | Replaced with the `alt` text: `[alt text](actual url)`
Links        | Will be replaced with the their corresponding text.
