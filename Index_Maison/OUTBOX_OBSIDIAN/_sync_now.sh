#!/bin/bash
# _sync_now.sh — SYNC DES FICHIERS VIVANTS OUTBOX → VAULT (réécrit 05/09, audit graph view)
# ==============================================================================
# RÔLE (unique) : re-copier dans le vault les fichiers VIVANTS (stems protégés,
# régénérés en continu par pulse_sous_loeil.sh, thermo_*, superviseur_*).
# Ces fichiers ne sont JAMAIS archivés par obsidian_writer (PROTECTED_STEMS) :
# leur seul chemin vers le vault passe ici.
#
# CE QU'IL NE FAIT PLUS (corrigé 05/09 — c'était la source de la pollution) :
#   - NE copie PLUS _traites/ (1596 archives reflétées → points fantômes du graph)
#   - NE copie PLUS les dossiers de notes typées (Crypto_Projet, Hulk, Cahier,
#     A_Mon_Attention…) : obsidian_writer s'en charge via la CLI et les archive.
#   - NE crée PLUS de doublons Index_Maison/ à la racine du vault.
#
# Le push git du vault est fait par son propre agent : com.ace777.gitpush-vault
# (git_push_vault.sh). Ici on ne fait que copier + marquer les changements.
set -uo pipefail

VAULT="/Users/christophe/Documents/Obsidian_ACE777"
OB="/Users/christophe/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN"

# Stems VIVANTS — DOIT rester aligné sur PROTECTED_STEMS de obsidian_writer.py
LIVE_STEMS="THERMO_DERNIER SOUS_L_OEIL SUPERVISEUR_LOG CHECKUP_DERNIER ETAT_SYSTEME CHECKUP_20260730T1511Z HEARTBEAT JOURNAL_COCKPIT POINT_REPRISE_DERNIER"

echo "=== SYNC VIVANTS OUTBOX → VAULT ($(date -u +%H:%M:%SZ)) ==="
count=0
for stem in $LIVE_STEMS; do
    src="$OB/$stem.md"
    [ -f "$src" ] || continue
    cp "$src" "$VAULT/$stem.md"
    count=$((count+1))
done
echo "SYNC_LIVE: $count fichiers vivants → $VAULT (racine, jamais _traites)"

# Marquer dans le git du vault (commit+push = agent com.ace777.gitpush-vault)
cd "$VAULT" 2>/dev/null || exit 0
git add -u 2>/dev/null || true
git commit -m "auto-sync: fichiers vivants ($(date -u +'%Y-%m-%dT%H%MZ'))" --allow-empty 2>/dev/null || true
echo "GIT_MARK_DONE (push = gitpush-vault)"
