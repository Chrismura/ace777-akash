#!/bin/bash
# Force-copie A_Mon_Attention (INDEX à jour) → vault Obsidian
# À lancer dans Terminal (pas Cursor) à cause de macOS Documents.
set -euo pipefail
SRC="/Users/christophe/ace777-test-day1/Index_Maison/A_Mon_Attention"
VAULT="/Users/christophe/Documents/Obsidian_ACE777"
for dest in \
  "$VAULT/Index_Maison/A_Mon_Attention" \
  "$VAULT/A_Mon_Attention"
do
  mkdir -p "$dest"
  cp -f "$SRC/"*.md "$dest/"
  echo "OK → $dest/INDEX.md ($(wc -c < "$dest/INDEX.md") octets)"
done
echo
echo "Ouvre dans Obsidian :"
echo "  Index_Maison / A_Mon_Attention / INDEX"
open "obsidian://open?vault=Obsidian_ACE777&file=Index_Maison%2FA_Mon_Attention%2FINDEX"
echo DONE
