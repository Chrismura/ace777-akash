#!/usr/bin/env bash
# git_push_vault.sh — push automatique du vault Obsidian (obsidian-vault).
# Même philosophie que git_push_auto.sh (maison) : SÉCURISÉ, on ne commit que
# l'utile (fichiers déjà suivis + dossiers de travail), jamais Signets_X ni .obsidian (bruit).
# Cadence : toutes les 3h (plist com.ace777.gitpush-vault). Log : ~/prise-ia/reports/SYNC_LOG.md
#
# ⚠️ RÉPARATION DU 20/09/2026 (la sauvegarde du coffre était MORTE depuis 2 jours) :
#   Un `.git/index.lock` orphelin de 0 octet, daté du 18/09 18:55, bloquait TOUT `git add`.
#   Le script avalait l'erreur (`git add … 2>/dev/null`) puis annonçait « à jour » :
#   panne 100 % silencieuse. Le garde-fou qui rattrape ce cas existait depuis le 05/09
#   dans git_push_auto.sh — il n'avait JAMAIS été recopié ici. La boucle était coupée.
#   Ce qui est ajouté ici :
#     1. garde-fou index.lock orphelin (recopié de git_push_auto.sh, testé au 03/09) ;
#     2. sérialisation (deux passages simultanés → « cannot lock ref » = push perdu) ;
#     3. plus AUCUNE erreur avalée : si `git add` échoue, on le DIT ;
#     4. un battement de pouls écrit SEULEMENT quand le coffre est prouvé à jour
#        (rien à commiter ET rien en avance sur origin) → le chien de garde mesure
#        un fait VRAI (R14 : une alarme qui ne peut plus dire vrai est une fausse alarme).
set -uo pipefail

REPO_DIR="$HOME/Documents/Obsidian_ACE777"
LOG_DIR="$HOME/prise-ia/reports"
LOG_FILE="$LOG_DIR/SYNC_LOG.md"
POULS_FILE="$HOME/ace777-test-day1/Index_Maison/pouls/gitpush-vault.json"
LOCK_DIR="$REPO_DIR/.git/.push_vault.lock"
TS=$(date -u +%Y-%m-%dT%H:%MZ)

mkdir -p "$LOG_DIR"
mkdir -p "$(dirname "$POULS_FILE")"

# ── 0) SÉRIALISATION — un seul passage à la fois ─────────────────────────────
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    if [ -n "$(find "$LOCK_DIR" -maxdepth 0 -mmin +30 2>/dev/null)" ]; then
        echo "[$TS] GARDE-FOU vault : verrou orphelin (>30 min) retiré" >> "$LOG_FILE"
        rm -rf "$LOCK_DIR"
        mkdir "$LOCK_DIR" 2>/dev/null || { echo "[$TS] INFO vault : passage concurrent en cours — sauté"; exit 0; }
    else
        echo "[$TS] INFO vault : passage concurrent en cours — sauté"
        exit 0
    fi
fi
trap 'rmdir "$LOCK_DIR" 2>/dev/null' EXIT

cd "$REPO_DIR" || exit 1

# ── 0bis) GARDE-FOU index.lock ORPHELIN ─────────────────────────────────────
# Un verrou git qui ne correspond à aucun git vivant bloque toute la sauvegarde.
# On le met de côté (jamais supprimé : preuve conservée) au lieu d'avaler l'erreur.
if [ -f ".git/index.lock" ]; then
    if pgrep -f "git (add|commit|push|rebase|merge)" >/dev/null 2>&1; then
        echo "[$TS] INFO vault : git actif détecté — passage sans commit" >> "$LOG_FILE"
        exit 0
    fi
    mv ".git/index.lock" "/tmp/index.lock.vault.orphelin.$TS" 2>/dev/null \
        && echo "[$TS] GARDE-FOU vault : index.lock orphelin mis de côté → /tmp/index.lock.vault.orphelin.$TS" >> "$LOG_FILE"
fi

# ── 1) Indexation ───────────────────────────────────────────────────────────
# Plus de `2>/dev/null` : une indexation qui échoue DOIT être visible.
ERREUR_ADD=""
git add -u || ERREUR_ADD="git add -u"
PATHS=()
for d in Evaluations AUTO_EVOL A_Mon_Attention Index_Maison; do
    [ -d "$d" ] && PATHS+=("$d")
done
for f in PROTOCOLE_DELEGATION.md REVEIL_BUFFY.md MEMOIRE_COLLAB.md CHANTIERS.md INVENTAIRE_COMPLET.md; do
    [ -f "$f" ] && PATHS+=("$f")
done
if [ ${#PATHS[@]} -gt 0 ]; then
    git add "${PATHS[@]}" || ERREUR_ADD="${ERREUR_ADD:+$ERREUR_ADD + }git add ${PATHS[*]}"
fi

# ── 2) Commit puis — TOUJOURS — pousser s'il reste des commits locaux ────────
# ⚠️ BUG CORRIGÉ le 19/09/2026 : avant, on ne poussait QUE si l'on venait de commiter.
# Un unique push raté (réseau/auth) laissait donc la sauvegarde en arrière POUR DE BON.
# Constaté en direct : vault bloqué 22 h avec 1 commit non poussé + 36 fichiers modifiés,
# alors que le script disait « aucun changement à pousser ». On RE-TENTE désormais à
# chaque passage tant qu'il reste des commits en avance sur origin/main.
COMMIT_OK=1
if ! git diff --cached --quiet 2>/dev/null; then
    git commit -m "auto-sync vault: états [${TS}]" >> "$LOG_FILE" 2>&1 || COMMIT_OK=0
fi

PUSH_FAIT=0
EN_AVANCE=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
if [ "${EN_AVANCE:-0}" -gt 0 ] 2>/dev/null; then
    if git push origin main >> "$LOG_FILE" 2>&1; then
        PUSH_FAIT=1
        MSG="[$TS] SUCCÈS vault : push effectué (obsidian-vault) — ${EN_AVANCE} commit(s)"
    else
        MSG="[$TS] ERREUR vault : push échoué (réseau/auth ?) — ${EN_AVANCE} commit(s) EN ATTENTE"
    fi
fi

# ── 3) Le coffre est-il PROUVÉ à jour ? (battement de pouls = fait mesuré) ───
# Vrai si : l'indexation n'a pas échoué, le commit n'a pas échoué, et il ne reste
# RIEN en attente vers origin. Dans tous les autres cas, AUCUN battement n'est écrit :
# le chien de garde crie — et cette fois il a raison.
RESTE_COMMITS=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 1)
EN_SYNC=1
[ -n "$ERREUR_ADD" ] && EN_SYNC=0
[ "$COMMIT_OK" -eq 0 ] && EN_SYNC=0
[ "${RESTE_COMMITS:-1}" -gt 0 ] 2>/dev/null && EN_SYNC=0
if [ "$EN_SYNC" -eq 1 ]; then
    TMP_POULS="${POULS_FILE}.tmp.$$"
    printf '{\n  "organe": "gitpush-vault",\n  "dernier_battement": "%s",\n  "en_sync": true,\n  "push": %s\n}\n' \
        "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$PUSH_FAIT" > "$TMP_POULS" \
        && mv "$TMP_POULS" "$POULS_FILE"
else
    MSG="${MSG:-[$TS] ERREUR vault : coffre NON prouvé à jour — aucune écriture de pouls}"
fi

[ -n "$ERREUR_ADD" ] && MSG="[$TS] ERREUR vault : indexation échouée ($ERREUR_ADD) — sauvegarde BLOQUÉE"

MSG="${MSG:-[$TS] INFO vault : à jour}"
echo "- $MSG" >> "$LOG_FILE"
echo "$MSG"
