# coding: utf-8
# SPDX-License-Identifier: GPL-3.0-or-later

import requests

import xbmcgui
from libs.kodimarkdown import converter
markdown = requests.get("https://raw.githubusercontent.com/wiki/retrospect-addon/plugin.video.retrospect/Home.md", verify=False).text
xbmcgui.Dialog().textviewer("Test", markdown)
converted = converter.to_kodi(markdown)
xbmcgui.Dialog().textviewer("Test", converted)
