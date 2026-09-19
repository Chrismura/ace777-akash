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

# 4) Commit puis — TOUJOURS — pousser s'il reste des commits locaux.
# ⚠️ BUG CORRIGÉ le 19/09/2026 : avant, on ne poussait QUE si l'on venait de commiter.
# Un unique push raté (réseau/auth) laissait donc la sauvegarde en arrière POUR DE BON.
# Constaté en direct : vault bloqué 22 h avec 1 commit non poussé + 36 fichiers modifiés,
# alors que le script disait « aucun changement à pousser ». On RE-TENTE désormais à
# chaque passage tant qu'il reste des commits en avance sur origin/main.
if ! git diff --cached --quiet 2>/dev/null; then
  git commit -m "auto-sync vault: états [${TS}]" >> "$LOG_FILE" 2>&1 \
    || MSG="[$TS] ERREUR vault : commit échoué (voir $LOG_FILE)"
fi
EN_AVANCE=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
if [ "${EN_AVANCE:-0}" -gt 0 ] 2>/dev/null; then
  if git push origin main >> "$LOG_FILE" 2>&1; then
    MSG="[$TS] SUCCÈS vault : push effectué (obsidian-vault) — ${EN_AVANCE} commit(s)"
  else
    MSG="[$TS] ERREUR vault : push échoué (réseau/auth ?) — ${EN_AVANCE} commit(s) EN ATTENTE"
  fi
fi
: "${MSG:=[$TS] INFO vault : à jour}"
echo "- $MSG" >> "$LOG_FILE"
echo "$MSG"
