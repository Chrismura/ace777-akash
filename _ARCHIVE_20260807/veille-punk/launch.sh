#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
osascript <<APPLESCRIPT
tell application "Terminal"
  activate
  set punkCmd to "clear; export VEILLE_ROOT='$ROOT'; export VEILLE_BANNER_SHOWN=; cd '$ROOT'; source '$ROOT/zshrc.punk'; exec zsh -i"
  do script punkCmd
  delay 0.3
  set w to front window
  try
    set current settings of w to settings set "Pro"
  end try
  set background color of w to {2048, 0, 6144}
  set normal text color of w to {0, 60000, 65535}
  set bold text color of w to {65535, 12000, 42000}
  set cursor color of w to {65535, 20000, 50000}
  set custom title of w to "◆ VEILLE PUNK"
  set title displays custom title of w to true
  set title displays device name of w to false
  set title displays shell path of w to false
  set title displays window size of w to false
end tell
APPLESCRIPT
echo "OK → Terminal « ◆ VEILLE PUNK » (fond violet / texte cyan)"
echo "  $ROOT"
