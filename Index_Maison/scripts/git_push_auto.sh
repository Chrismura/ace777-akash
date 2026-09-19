#!/usr/bin/env bash
# git_push_auto.sh — push automatique du repo système (conception Gemini, intégré Ada).
# Cadence : toutes les 3h (plist com.ace777.gitpush).
# SÉCURISÉ : ne commit QUE les fichiers déjà suivis (+ les canoniques de l'OUTBOX),
# jamais les 1600+ fichiers non suivis (bruit). Log dans ~/prise-ia/reports/SYNC_LOG.md.
set -uo pipefail

REPO_DIR="$HOME/ace777-test-day1"
LOG_DIR="$HOME/prise-ia/reports"
LOG_FILE="$LOG_DIR/SYNC_LOG.md"
TS=$(date -u +%Y-%m-%dT%H:%MZ)

mkdir -p "$LOG_DIR"
cd "$REPO_DIR" || exit 1

# 1) Étendre l'OUTBOX depuis le système (pont machine → outbox)
if [ -f "$REPO_DIR/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh" ]; then
  bash "$REPO_DIR/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh" >> "$LOG_FILE" 2>&1
fi

# 1bis) Versionner les agents launchd (anti-dérive, 19/09). Au 19/09 : 97 agents
# installés pour 44 versionnés → une restauration perdait 53 organes en silence.
# Ce passage les recopie dans Index_Maison/plists/ à chaque push (toutes les 3 h).
if [ -f "$REPO_DIR/Index_Maison/scripts/sync_plists.sh" ]; then
  bash "$REPO_DIR/Index_Maison/scripts/sync_plists.sh" >> "$LOG_FILE" 2>&1
fi

# 1ter) DRILL DE RESTAURATION (19/09) — « si le Mac mourrait ce soir, ACE777
# reviendrait-il ? ». Lecture seule : rebâtit les agents dans un dossier neuf en
# /tmp, valide chaque plist, vérifie que chaque organe invoqué existe, compare les
# scellés. Écrit thermo/DRILL_RESTAURATION.md (verdict lu par la page « vol »).
# Une sauvegarde jamais testée n'est pas une sauvegarde : c'est une hypothèse.
if [ -f "$REPO_DIR/Index_Maison/scripts/drill_restauration.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/drill_restauration.py" >> "$LOG_FILE" 2>&1
fi

# 1quater) ORGANES HORS REPO (19/09) — ~/prise-ia (le HUB) n'était versionné NULLE PART.
# Miroir des SOURCES (jamais .env ni logs) → Index_Maison/organes_hors_repo/ → part sur GitHub.
# ~/mirofis, lui, est déjà versionné sur son git amont : on se contente de le déclarer.
if [ -f "$REPO_DIR/Index_Maison/scripts/sync_organes_hors_repo.sh" ]; then
  bash "$REPO_DIR/Index_Maison/scripts/sync_organes_hors_repo.sh" >> "$LOG_FILE" 2>&1
fi

# 2) Ne committer que les fichiers DÉJÀ SUIVIS (modifiés/supprimés) + les canoniques
# Garde-fou 05/09 (incident index.lock orphelin du 03/09 : 2,5 jours de push mort
# en silence, le 2>/dev/null avalait le rc=128 et le script disait « aucun changement ») :
# si un index.lock traîne, on vérifie qu'aucun git ne tourne, puis on le retire.
if [ -f "$REPO_DIR/.git/index.lock" ]; then
  if ! pgrep -f "git (add|commit|push|rebase|merge)" >/dev/null 2>&1; then
    rm -f "$REPO_DIR/.git/index.lock"
    echo "[$TS] GARDE-FOU : index.lock orphelin retiré" >> "$LOG_FILE"
  else
    echo "[$TS] INFO : git actif détecté, passage sans commit" >> "$LOG_FILE"
    exit 0
  fi
fi
git add -u 2>/dev/null || { echo "[$TS] ERREUR : git add a échoué (rc=$?)" >> "$LOG_FILE"; }
# agents launchd versionnés (nouveaux fichiers → git add -u ne les prend pas)
[ -d "$REPO_DIR/Index_Maison/plists" ] && git add Index_Maison/plists 2>/dev/null
# organes hors repo mirés (nouveaux fichiers → git add -u ne les prend pas)
[ -d "$REPO_DIR/Index_Maison/organes_hors_repo" ] && git add Index_Maison/organes_hors_repo 2>/dev/null
# canoniques OUTBOX (s'ils existent, suivis ou non)
for f in \
  Index_Maison/OUTBOX_OBSIDIAN/MEMOIRE_COLLAB.md \
  Index_Maison/OUTBOX_OBSIDIAN/CONSOLE_GENERALE.md \
  Index_Maison/OUTBOX_OBSIDIAN/THERMO_DERNIER.md \
  Index_Maison/OUTBOX_OBSIDIAN/SOUS_L_OEIL.md \
  Index_Maison/OUTBOX_OBSIDIAN/PLAN_DE_VOL.md \
  Index_Maison/OUTBOX_OBSIDIAN/AUTO_PROCESSUS.md ; do
  [ -f "$REPO_DIR/$f" ] && git add "$f" 2>/dev/null
done

# 3) Commit + push
if git diff --cached --quiet 2>/dev/null; then
  MSG="${MSG:-[$TS] INFO : aucun changement à pousser}"
else
  if git commit -m "auto-sync: pont OUTBOX + états [${TS}]" >> "$LOG_FILE" 2>&1; then
    if git push origin main >> "$LOG_FILE" 2>&1; then
      MSG="[$TS] SUCCÈS : push effectué (ace777-akash)"
    else
      MSG="[$TS] ERREUR : push échoué (réseau/auth ?) — commit local conservé"
    fi
  else
    MSG="[$TS] ERREUR : commit échoué (voir $LOG_FILE)"
  fi
fi

echo "- $MSG" >> "$LOG_FILE"
echo "$MSG"
