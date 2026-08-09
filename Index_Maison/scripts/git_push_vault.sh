#!/usr/bin/env bash
# git_push_vault.sh — push automatique du vault Obsidian (obsidian-vault).
# Même philosophie que git_push_auto.sh (maison) : SÉCURISÉ, on ne commit que
# l'utile (fichiers déjà suivis + dossiers de travail), jamais Signets_X ni .obsidian (bruit).
# Cadence : toutes les 3h (plist com.ace777.gitpush-vault). Log : ~/prise-ia/reports/SYNC_LOG.md
set -uo pipefail

REPO_DIR="$HOME/Documents/Obsidian_ACE777"
LOG_DIR="$HOME/prise-ia/reports"
LOG_FILE="$LOG_DIR/SYNC_LOG.md"
TS=$(date -u +%Y-%m-%dT%H:%MZ)

mkdir -p "$LOG_DIR"
cd "$REPO_DIR" || exit 1

# 1) Modifications des fichiers DÉJÀ SUIVIS (mémoire, protocole, reveil, etc.)
git add -u 2>/dev/null

# 2) Dossiers de travail canoniques (nouveaux fichiers légitimes, pas le bruit)
git add Evaluations AUTO_EVOL A_Mon_Attention Index_Maison 2>/dev/null

# 3) Fichiers racine clés (s'ils existent)
for f in PROTOCOLE_DELEGATION.md REVEIL_BUFFY.md MEMOIRE_COLLAB.md CHANTIERS.md INVENTAIRE_COMPLET.md; do
  [ -f "$REPO_DIR/$f" ] && git add "$f" 2>/dev/null
done

# 4) Commit + push
if git diff --cached --quiet 2>/dev/null; then
  MSG="[$TS] INFO vault : aucun changement à pousser"
else
  git commit -m "auto-sync vault: états [${TS}]" >> "$LOG_FILE" 2>&1
  if git push origin main >> "$LOG_FILE" 2>&1; then
    MSG="[$TS] SUCCÈS vault : push effectué (obsidian-vault)"
  else
    MSG="[$TS] ERREUR vault : push échoué (réseau/auth ?)"
  fi
fi
echo "- $MSG" >> "$LOG_FILE"
echo "$MSG"
