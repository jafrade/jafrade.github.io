#!/bin/sh
# Render the redrawn diagrams in design/diagrams/<project>/ to JPEGs.
#
#     sh tools/render-diagrams.sh
#
# Each HTML page is one 1600 × 1100 board. Chrome screenshots it at 2x and
# sips saves it as design/diagrams/<project>/rendered/<name>.jpg. They aren't
# on the site now; to use one, copy it into images/<project>/ with a name
# starting "diagram-", so the build frames it as a board. Needs Google Chrome.
set -e
cd "$(dirname "$0")/.."
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TMP="$(mktemp -d)"
for f in design/diagrams/*/*.html; do
  project="$(basename "$(dirname "$f")")"
  name="$(basename "$f" .html)"
  mkdir -p "design/diagrams/$project/rendered"
  out="design/diagrams/$project/rendered/$name.jpg"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size=1600,1100 --virtual-time-budget=8000 \
    --user-data-dir="$TMP/profile" --screenshot="$TMP/$name.png" "file://$PWD/$f" >/dev/null 2>&1
  sips -s format jpeg -s formatOptions 88 "$TMP/$name.png" --out "$out" >/dev/null
  echo "$out  $(du -k "$out" | cut -f1)KB"
done
rm -rf "$TMP"
