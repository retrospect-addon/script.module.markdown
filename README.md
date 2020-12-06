# Markdown-to-Kodi formatted text
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/retrospect-addon/script.module.markdown)](https://github.com/retrospect-addon/script.module.markdown/releases)
[![License](https://img.shields.io/github/license/retrospect-addon/script.module.markdown)](https://github.com/retrospect-addon/script.module.markdown/blob/master/LICENSE.md)
[![Python](https://img.shields.io/badge/python-2.7%20%7C%203.6%2D-3.8-blue?logo=python)](https://kodi.tv/article/attention-addon-developers-migration-python-3)

This simple library for [Kodi](https://kodi.tv) converts basic [Markdown](https://daringfireball.net/projects/markdown) to valid Kodi formatted text (See [here](https://kodi.wiki/view/Label_Formatting)).

## Supported Markdown Syntax
The basic Markdown [syntax](https://daringfireball.net/projects/markdown/syntax) is supported. The aim is to eventually also support the majority of the [GitHub flavoured markdown](https://github.github.com/gfm/). A cheatsheet can be found at [GitHub](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf).

The following table has an overview of the supported syntax:

Description  | Markdown     | Kodi formatted text
------------ | ------------ | -------------
Heading 1    | `#`          | `[BOLD][LIGHT][UPPERCASE]`
Heading 2    | `##`         | `[BOLD][LIGHT][CAPITALIZE]`
Heading 3    | `###` `####` | `[LIGHT][CAPITALIZE]`

## Not Supported:
Description  | Remark
------------ | -------------
Tables       | _Will be removed completely_.
Images       | Replaced with the `alt` text: `[alt text](actual url)`
Links        | Will be replaced with the their corresponding text.