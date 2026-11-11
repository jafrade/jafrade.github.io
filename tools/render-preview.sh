#!/bin/sh
# Render design/preview/og.html to og-image.jpg, the 1200 × 630 image that
# search results and link previews (LinkedIn, Slack, iMessage) show.
#
#     sh tools/render-preview.sh
#
# Needs Google Chrome.
set -e
cd "$(dirname "$0")/.."
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TMP="$(mktemp -d)"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1200,630 --virtual-time-budget=8000 \
  --user-data-dir="$TMP/profile" --screenshot="$TMP/og.png" "file://$PWD/design/preview/og.html" >/dev/null 2>&1
sips --resampleWidth 1200 -s format jpeg -s formatOptions 88 "$TMP/og.png" --out og-image.jpg >/dev/null
rm -rf "$TMP"
echo "og-image.jpg  $(du -k og-image.jpg | cut -f1)KB"
