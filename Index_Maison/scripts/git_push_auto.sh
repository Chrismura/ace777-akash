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

# ── 0) SÉRIALISATION (ajout 20/09/2026) ──────────────────────────────────────
# Deux passages simultanés (plist 3 h + superviseur_auto qui l'appelle aussi) ont
# produit « cannot lock ref 'refs/heads/main': is at X but expected Y » = push perdu
# et bruit dans le journal. Un seul passage à la fois ; un verrou de plus de 30 min
# est considéré orphelin (passage tué en cours de route).
LOCK_DIR="$REPO_DIR/.git/.push_auto.lock"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    if [ -n "$(find "$LOCK_DIR" -maxdepth 0 -mmin +30 2>/dev/null)" ]; then
        echo "[$TS] GARDE-FOU : verrou de push orphelin (>30 min) retiré" >> "$LOG_FILE"
        rm -rf "$LOCK_DIR"
        mkdir "$LOCK_DIR" 2>/dev/null || { echo "[$TS] INFO : passage concurrent en cours — sauté"; exit 0; }
    else
        echo "[$TS] INFO : passage concurrent en cours — sauté"
        exit 0
    fi
fi
trap 'rmdir "$LOCK_DIR" 2>/dev/null' EXIT

cd "$REPO_DIR" || exit 1

# 1) Étendre l'OUTBOX depuis le système (pont machine → outbox)
if [ -f "$REPO_DIR/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh" ]; then
  bash "$REPO_DIR/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh" >> "$LOG_FILE" 2>&1
fi

# 1bis-bis) LE REPO EST L'INSTALLATION (20/09) — contrôle de conformité, LECTURE SEULE.
# Synchro inverse de sync_plists.sh : vérifie que chaque agent installé est bien un
# LIEN vers Index_Maison/plists/ (donc qu'aucune dérive installé/repo n'est possible).
# N'écrit jamais rien dans LaunchAgents (`--lier` est un acte délibéré, sur GO).
# Sortie 2 = un agent installé n'est pas conforme au repo : la dérive devient VISIBLE.
if [ -f "$REPO_DIR/Index_Maison/scripts/installer_depuis_repo.sh" ]; then
  bash "$REPO_DIR/Index_Maison/scripts/installer_depuis_repo.sh" --verifier >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : installation non conforme au repo (voir ci-dessus)" >> "$LOG_FILE"
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

# 1quinquies) VÉRIFICATEUR DES RÈGLES D'OR (19/09) — les règles d'or vivaient éparpillées
# dans 6 documents et personne ne vérifiait qu'elles étaient tenues. Lecture seule :
# rejoue les règles mesurables par la machine (RAM/cloud, scellés, 0 hors repo, 0 €, preuve
# datée) → thermo/REGLES_OR.md. Canon : Index_Maison/REGLE_D_OR.md.
if [ -f "$REPO_DIR/Index_Maison/scripts/verifier_regles_or.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/verifier_regles_or.py" >> "$LOG_FILE" 2>&1
fi

# 1sexies) REVUE DES ORGANES (20/09) — les 99 organes comparés à ce que le registre
# DÉCLARE : cadence déclarée vs déclencheur RÉEL du plist, produit déclaré que plus rien
# ne résout, produit frais dont le CONTENU n'avance plus. Le chien ne pouvait pas voir
# ces écarts STRUCTURELS : il mesure la fraîcheur, pas la cohérence des déclarations.
# Lecture seule sur la maison (n'écrit que thermo/revue_organes.json + REVUE_ORGANES.md).
# Un écart n'est pas une panne : c'est une déclaration à faire (strategie/revue_declares.json).
if [ -f "$REPO_DIR/Index_Maison/scripts/revue_organes.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/revue_organes.py" >> "$LOG_FILE" 2>&1
fi

# 1septies) VERDICTS DES PROTOCOLES EN TEST (20/09) — leurs critères sont PRÉ-ENREGISTRÉS
# (on fixe le critère AVANT de voir les données) donc les verdicts sont CALCULABLES.
# La page vol recopiait à la main un tableau du 14/09 : elle pouvait afficher un verdict
# périmé, et personne ne voyait qu'un protocole dont le verdict ne peut pas être rendu
# (0 cas à juger, matériel absent, seuil hors d'échelle) n'était pas une patience mais
# une panne de conception. Lecture seule (écrit thermo/PROTOCOLES_VERDICTS.json).
if [ -f "$REPO_DIR/Index_Maison/scripts/verdicts_protocoles.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/verdicts_protocoles.py" >> "$LOG_FILE" 2>&1
fi

# 1octies) GARDE-FOU DE MÉTHODE SUR LES SEUILS (23/09) — j'ai publié PENDANT TROIS JOURS
# un seuil RECALCULÉ de mémoire (« le repli exigé vaut max(dip 4,2 % ; 5 % ; 0,30×m6) »)
# alors que le moteur en appliquait 21,70 % : il manquait LE terme dominant
# `dip = max(dip_pct ; 0,50 × cadence)`. L'erreur n'était pas un chiffre, c'était une
# méthode. Ce contrôle CONFRONTE, chaque passage, le seuil recalculé aux chiffres que le
# moteur ÉCRIT lui-même (refus parlants + sa cadence colonne 9), nomme le terme qui décide
# (R15) et signale tout instrument qui recalcule un seuil sans la cadence.
# rc=0 conforme · rc=3 DÉSACCORD (à traiter, ne pas publier de chiffre) · rc=2 pas encore
# assez de refus chiffrés = EN ATTENTE (normal dans l'heure qui suit une relance).
if [ -f "$REPO_DIR/hulk-mexc/scripts/verif_seuil_moteur.py" ]; then
  python3 "$REPO_DIR/hulk-mexc/scripts/verif_seuil_moteur.py" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : garde-fou des seuils NON conforme (voir ci-dessus)" >> "$LOG_FILE"
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

# 3) Commit puis — TOUJOURS — pousser s'il reste des commits locaux.
# ⚠️ BUG CORRIGÉ le 19/09/2026 : avant, on ne poussait QUE si l'on venait de commiter →
# un unique push raté (réseau/auth) laissait la sauvegarde en arrière POUR DE BON.
# (même bug constaté côté vault : bloqué 22 h avec 1 commit non poussé.) On re-tente à chaque passage.
if ! git diff --cached --quiet 2>/dev/null; then
  git commit -m "auto-sync: pont OUTBOX + états [${TS}]" >> "$LOG_FILE" 2>&1 \
    || MSG="[$TS] ERREUR : commit échoué (voir $LOG_FILE)"
fi
EN_AVANCE=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
if [ "${EN_AVANCE:-0}" -gt 0 ] 2>/dev/null; then
  if git push origin main >> "$LOG_FILE" 2>&1; then
    MSG="[$TS] SUCCÈS : push effectué (ace777-akash) — ${EN_AVANCE} commit(s)"
  else
    MSG="[$TS] ERREUR : push échoué (réseau/auth ?) — ${EN_AVANCE} commit(s) EN ATTENTE"
  fi
fi
MSG="${MSG:-[$TS] INFO : aucun changement à pousser}"

echo "- $MSG" >> "$LOG_FILE"
echo "$MSG"
