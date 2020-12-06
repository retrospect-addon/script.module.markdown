# SPDX-License-Identifier: GPL-3.0-or-later

import xbmcgui
from libs.kodimarkdown import converter

text = "# Main heading\n\n" \
       "## Second heading\n\n" \
       "### Third heading\n\n" \
       "And this is more text"
xbmcgui.Dialog().textviewer("Test", text)
converted = converter.to_kodi(text)
xbmcgui.Dialog().textviewer("Test", converted)
