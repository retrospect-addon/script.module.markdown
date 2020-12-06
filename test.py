# SPDX-License-Identifier: GPL-3.0-or-later

import xbmcgui
from libs.kodimarkdown import converter

text = "# Main heading\n\n" \
       "## Second heading\n\n" \
       "### Third heading\n\n" \
       "#### Fourth heading\n\n" \
       "And this is more __bold__ text and _italic_ text\n\n" \
       "And this is more **bold** text and *italic* text"
xbmcgui.Dialog().textviewer("Test", text)
converted = converter.to_kodi(text)
xbmcgui.Dialog().textviewer("Test", converted)
