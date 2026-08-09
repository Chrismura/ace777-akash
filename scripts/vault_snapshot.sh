#!/usr/bin/env bash
# vault_snapshot.sh — A3 (non destructif) : notes vault modifiees < 24h -> VAULT_SNAPSHOT.md (max 200 lignes)
# Donne au superviseur une vue recente du vault SANS copier les 1089 fichiers.
VAULT="$HOME/Documents/Obsidian_ACE777"
OUT="$HOME/ace777-test-day1/Index_Maison/VAULT_SNAPSHOT.md"
TMPF=$(mktemp)
trap 'rm -f "$TMPF"' EXIT

{
  echo "# VAULT SNAPSHOT — $(date -u +%Y-%m-%dT%H:%MZ)"
  echo
  echo "> Notes modifiees < 24h (extraits). Jamais un remplacement du vault — vue recente seulement."
  echo
  find "$VAULT" -name '*.md' -mtime -1 -not -path '*/.obsidian/*' -not -path '*/.git/*' -not -path '*/.trash/*' 2>/dev/null | head -15 | while read -r f; do
    echo "## $(basename "$f")"
    head -8 "$f"
    echo
  done
} > "$TMPF"
head -200 "$TMPF" > "$OUT"
echo "VAULT_SNAPSHOT -> $OUT ($(wc -l < "$OUT" | tr -d ' ') lignes)"
