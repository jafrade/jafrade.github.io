#!/bin/sh
# Make web-sized copies of the About photos for the mosaic and photo strip.
#
#     sh tools/resize-about-photos.sh
#
# Reads the full-size photos in images/about/originals (left untouched) and
# writes copies to images/about/web, at most 1200px on the long edge and
# JPEG quality 45. That's sharp on retina screens for the largest mosaic cell
# (about 430px wide). Uses sips, which comes with macOS.
set -e
cd "$(dirname "$0")/.."
mkdir -p images/about/web
for f in images/about/originals/*.jpg; do
  out="images/about/web/$(basename "$f")"
  sips -Z 1200 -s formatOptions 45 "$f" --out "$out" >/dev/null
  echo "$out  $(du -k "$out" | cut -f1)KB (was $(du -k "$f" | cut -f1)KB)"
done
