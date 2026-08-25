#!/bin/bash
set -euo pipefail
VAULT="/Users/christophe/Documents/Obsidian_ACE777"
OB="/Users/christophe/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN"

echo "=== SYNC OUTBOX → VAULT ($(date)) ==="
count=0

# Racine
for f in "$OB"/*.md; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    cp "$f" "$VAULT/$base"
    count=$((count+1))
done

# Index_Maison/
mkdir -p "$VAULT/Index_Maison"
for f in "$OB/Index_Maison"/*.md; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    cp "$f" "$VAULT/Index_Maison/$base"
    count=$((count+1))
done

# Sous-dossiers A_Mon_Attention, Cahier, etc.
for dir in "$OB"/*/; do
    [ -d "$dir" ] || continue
    dirname=$(basename "$dir")
    [ "$dirname" = "Index_Maison" ] && continue  # déjà traité
    mkdir -p "$VAULT/$dirname"
    for f in "$dir"*.md; do
        [ -f "$f" ] || continue
        cp "$f" "$VAULT/$dirname/"
        count=$((count+1))
    done
done

echo "SYNC_DONE: $count fichiers → $VAULT"

# Auto-commit dans le vault
cd "$VAULT"
git add -A
git commit -m "auto-sync: OUTBOX → vault ($(date -u +'%Y-%m-%dT%H%MZ'))" --allow-empty 2>/dev/null || true
echo "GIT_COMMIT_DONE"
