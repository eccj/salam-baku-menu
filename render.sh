#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
IN="file://${ROOT}/src/index.html"
OUT="${ROOT}/output/pilot.pdf"

mkdir -p "${ROOT}/output"

"$CHROME" \
  --headless=new \
  --disable-gpu \
  --hide-scrollbars \
  --no-pdf-header-footer \
  --print-to-pdf="$OUT" \
  --no-margins \
  --virtual-time-budget=10000 \
  "$IN"

echo "→ $OUT"
ls -lh "$OUT"
