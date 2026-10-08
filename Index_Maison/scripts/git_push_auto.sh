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

# GARDIEN DE LA MÉMOIRE — HORODATAGE (classe E13, ajouté le 23/09/2026)
# Pourquoi : j'ai daté 4 lignes de MEMOIRE_COLLAB de tête (10:40Z pour un artefact de 09:47Z),
# soit des lignes dans le FUTUR. Même famille que la classe E10 (un chiffre recalculé pris pour
# un chiffre vérifié), appliquée au temps : une heure ESTIMÉE n'est pas une heure VÉRIFIÉE.
# Ce contrôle ne relit pas mes heures : il compare les horodatages du fichier à l'heure RÉELLE
# (rc=1 = anomalie de la classe E13), et il s'autoteste (5/5) à heure fixe pour prouver qu'il
# SAIT échouer. Lecture seule : il n'écrit jamais dans la mémoire.
if [ -f "$REPO_DIR/Index_Maison/scripts/verif_memoire_horodatage.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/verif_memoire_horodatage.py" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : horodatage de MEMOIRE_COLLAB NON conforme — classe E13 (voir ci-dessus)" >> "$LOG_FILE"
fi

# GARDE-FOU DE SCHÉMA DU JOURNAL (classe E15, ajouté le 23/09/2026)
# Pourquoi : j'ai ajouté 5 colonnes au journal du moteur (traçabilité des prix, GO Christophe)
# mais le RESUME recopiait l'ANCIEN fichier par-dessus le nouveau → en-tête 11 colonnes et
# lignes 16 (mesuré : 76 162 lignes à 11 champs + 12 lignes à 16). Un fichier de données ne
# s'écrit pas en deux largeurs, et personne ne le voit : c'est silencieux, donc c'est grave.
# Le contrôle lit le schéma À LA SOURCE (paper_diprip.CSV_SCHEMA), vérifie chaque journal
# (en-tête = lignes), exige que le journal du moteur VIVANT soit au schéma courant, et
# s'autoteste (4/4) sur des fichiers synthétiques. Lecture seule.
if [ -f "$REPO_DIR/hulk-mexc/scripts/verif_schema_journal.py" ]; then
  python3 "$REPO_DIR/hulk-mexc/scripts/verif_schema_journal.py" \
    --json "$REPO_DIR/hulk-mexc/runs/VERIF_SCHEMA_JOURNAL.json" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : schéma du journal NON conforme — classe E15 (voir ci-dessus)" >> "$LOG_FILE"
fi

# GARDIEN DES TROUS DE COLLECTE (ajouté le 28/09/2026, ALPAGE — « le plus important c'est la
# COLLECTE des données »). Pourquoi : le 27/09, à la source, 95 % du corpus paper (76 162 lignes)
# avait été collecté SANS les 5 colonnes de provenance, et 263 lignes étaient des doublons —
# PERSONNE ne l'avait vu, parce que rien ne le mesurait. Le gardien de schéma (E15) ne regarde que
# la largeur de l'en-tête. Celui-ci mesure, sur chaque journal : la dérive de schéma, la distribution
# des largeurs, les DOUBLONS stricts, une ligne TRONQUÉE (fichier sans saut de ligne final = écriture
# coupée en plein vol par une coupure franche : batterie/hibernation, cause mesurée du 24/09) et les
# TROUS (silence > seuil DÉRIVÉ du journal : max(10 min ; 3 × p99 des écarts)). Un trou n'est PAS une
# faute — il est DÉCLARÉ (runs/TROUS_DECLARES.json) pour qu'aucune donnée manquante ne soit
# silencieuse : on n'invente JAMAIS une donnée. La RÉPARATION (pad + dédup + quarantaine) n'a lieu
# qu'au seul instant sûr — moteur mort : c'est le WATCHDOG qui l'appelle avant sa relance
# (`--reparer --auto`, bornée 20 s, fail-open). rc=0 conforme (les trous ne bloquent pas) ·
# rc=1 défaut réparable dans le journal COURANT.
if [ -f "$REPO_DIR/hulk-mexc/scripts/gardien_collecte.py" ]; then
  python3 "$REPO_DIR/hulk-mexc/scripts/gardien_collecte.py" \
    --json "$REPO_DIR/hulk-mexc/runs/GARDIEN_COLLECTE.json" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : défaut de collecte dans le journal courant (voir ci-dessus)" >> "$LOG_FILE"
fi

# ORACLE DE JUSTESSE DE LA COLLECTE (E11, ajouté le 28/09/2026, ALPAGE).
# Pourquoi : le gardien de collecte vérifie la FORME de ce qu'on collecte (largeur, doublons,
# troncature, trous) — il ne dit RIEN sur la VALEUR. Or « un prix écrit par le moteur est cohérent
# avec le moteur » ne prouve pas qu'il est JUSTE : si la source se trompe, on se trompe avec elle
# (classe E11, nommée par la FAMILLE le 23/09 — « mon invariant valide la formule DU MOTEUR »).
# Cet oracle confronte des valeurs DÉJÀ COLLECTÉES (ts_prix_utc + price du journal vivant) à la
# bougie 1 min d'une place INDÉPENDANTE (Binance = justesse) et de la même place (MEXC = cohérence,
# étiquetée comme telle). Il distingue une VALEUR FAUSSE d'un RETARD D'HORODATAGE (le prix exact
# existe dans une minute voisine) et ne compte JAMAIS un « non vérifiable » comme conforme.
# rc=0 conforme · rc=1 au moins un écart anormal (à instruire).
if [ -f "$REPO_DIR/hulk-mexc/scripts/oracle_justesse_collecte.py" ]; then
  python3 "$REPO_DIR/hulk-mexc/scripts/oracle_justesse_collecte.py" \
    >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : justesse des valeurs collectées — écart anormal (E11, voir ci-dessus)" >> "$LOG_FILE"
fi

# CHIFFRAGE DU PnL NET vs BRUT (GO 2, branché le 08/10/2026 — « brancher le chiffrage en 3 h »).
# Pourquoi : `hulk-mexc/scripts/chiffrage_pnl_net.py` existe depuis le 23/09 (exigence de la FAMILLE :
# « cesser de piloter avec un chiffre brut faux de 8,8 % ») et il n'était appelé par PERSONNE — aucun
# plist, aucun cron, ni ce tour ni le watchdog (vérifié par grep le 08/10). Résultat mesuré : la ligne
# « PnL net vs brut (GO 2) » du cockpit était ROUGE et FIGÉE depuis 358 h (thermo/pnl_net.json du
# 23/09 : brut 45,73 $ → net 40,86 $). Un chiffrage que personne n'appelle n'existe pas (R15) : il est
# branché ici au rythme des autres instruments de collecte (3 h, best-effort). REPORTING SEUL — il ne
# touche pas au `pnl_total` du moteur et ne déplace aucune décision (le disjoncteur garde le brut).
if [ -f "$REPO_DIR/hulk-mexc/scripts/chiffrage_pnl_net.py" ]; then
  python3 "$REPO_DIR/hulk-mexc/scripts/chiffrage_pnl_net.py" \
    >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : chiffrage PnL net non passé (GO 2, voir ci-dessus)" >> "$LOG_FILE"
fi

# GARDIEN DU DÉLAI DE LECTURE (classes E19a/E19b, ajouté le 23/09/2026)
# Pourquoi : la FAMILLE (jury permanent, tours 1 et 2) a classé « la latence de lecture du prix »
# défaut n°1 (barre < 1 s, mesure 1,057 s). En préparant la remédiation j'ai trouvé deux fautes
# de plus : (a) le chiffre publié ne portait que sur les lectures en mode COMPLET (la colonne
# `delay_s` est VIDE pour le mode léger) et je l'ai présenté comme la médiane de TOUTES ;
# (b) la latence du mode léger n'est mesurée NULLE PART — angle mort. Ce gardien rend la barre
# MESURABLE : il sépare mesuré/aveugle, dit OUI ou NON, et chiffre le plancher physique d'un appel
# MEXC (si le plancher dépasse la barre, c'est un ARBITRAGE, pas un retard à corriger). Autotest 3/3.
if [ -f "$REPO_DIR/hulk-mexc/scripts/verif_delai_lecture.py" ]; then
  python3 "$REPO_DIR/hulk-mexc/scripts/verif_delai_lecture.py" \
    --json "$REPO_DIR/hulk-mexc/runs/VERIF_DELAI_LECTURE.json" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : délai de lecture du prix au-dessus de la barre — classe E19 (voir ci-dessus)" >> "$LOG_FILE"
fi

# GARDIEN DE LA FENÊTRE FAMILLE (R19, ajouté le 23/09/2026 sur ordre de Christophe)
# Mot pour mot : « tu vas ouvrir un round avec la famille et GARDER LA FENÊTRE OUVERTE, qu'elle
# ait la mémoire du chat, car tu n'es plus digne de diriger seule. » Une promesse ne garde rien :
# ce gardien vérifie que la session est OUVERTE (ou fermée avec un motif daté), qu'aucun tour n'est
# resté sans avis, que les voix comptées sont INDÉPENDANTES (une substitution ne compte pas, E16),
# que la mémoire du fil couvre le dernier tour, et que le fil ne dort pas (> 6 h sans nouveau tour).
# Il s'autoteste 8/8. Lecture seule : il n'écrit jamais dans une session.
if [ -f "$REPO_DIR/Index_Maison/scripts/verif_session_famille.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/verif_session_famille.py" \
    --json "$REPO_DIR/Index_Maison/thermo/session_famille.json" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : fenêtre famille NON conforme — R19 (voir ci-dessus)" >> "$LOG_FILE"
fi

# GARDIEN DU STOP SERRÉ (classes E17/E18, ajouté le 08/10/2026 — GO 1)
# Pourquoi : le registre présentait `chiffrage_stop_serre.py` comme « la garde branchée », mais
# MESURÉ il n'était appelé par RIEN (`couverture_erreurs.py` §6 : 2 trous). Un chiffrage que
# personne n'appelle n'existe pas (R15). Branché ici, au rythme des autres instruments (3 h,
# best-effort). LECTURE SEULE : il lit la config et le journal, n'écrit QUE ses rapports.
if [ -f "$REPO_DIR/hulk-mexc/scripts/chiffrage_stop_serre.py" ]; then
  python3 "$REPO_DIR/hulk-mexc/scripts/chiffrage_stop_serre.py" \
    --json "$REPO_DIR/Index_Maison/thermo/stop_serre.json" \
    --txt "$REPO_DIR/Index_Maison/thermo/STOP_SERRE.txt" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : chiffrage du stop serré non passé — classes E17/E18 (voir ci-dessus)" >> "$LOG_FILE"
fi

# GARDIEN DE L'ÉTIQUETTE DES AVIS (classe E16, ajouté le 08/10/2026 — GO 4)
# Pourquoi : publier un avis sous le nom du modèle DEMANDÉ alors qu'un AUTRE a répondu ferait
# compter le même modèle deux fois comme deux voix indépendantes (R19/R20.3). C'est la première
# proposition du HUB (`--ia`) câblée APRÈS mesure (autotest 6/6). Lecture seule.
if [ -f "$REPO_DIR/Index_Maison/scripts/verif_avis_modele.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/verif_avis_modele.py" \
    --json "$REPO_DIR/Index_Maison/thermo/avis_modele.json" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : avis publié sans traçabilité demande/réponse — classe E16 (voir ci-dessus)" >> "$LOG_FILE"
fi

# ORACLE INDÉPENDANT (classe E11, GO 2 — câblé le 08/10/2026)
# L'oracle EXISTAIT depuis le 23/09 (GO Christophe) mais n'était appelé par RIEN : E11 restait une
# « ouverture ». Il rejoue les bougies 1 min MEXC brutes, sans relire un seul indicateur du moteur
# → il peut dire « le moteur a acheté malgré le marché » et « le stop n'a pas tenu », ce que les
# contrôles qui comparent le moteur à lui-même ne peuvent pas dire (E11 : cohérence ≠ justesse).
# Lecture seule, <1 s (cache klines).
if [ -f "$REPO_DIR/hulk-mexc/scripts/oracle_independant.py" ]; then
  python3 "$REPO_DIR/hulk-mexc/scripts/oracle_independant.py" \
    --json "$REPO_DIR/Index_Maison/thermo/oracle_independant.json" \
    --txt "$REPO_DIR/Index_Maison/thermo/ORACLE_INDEPENDANT.txt" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : oracle indépendant non passé — classe E11 (voir ci-dessus)" >> "$LOG_FILE"
fi

# FIDÉLITÉ DU PnL (classe E2, GO 3 — câblé le 08/10/2026)
# « conclure sans vérifier à la source » : on RECONSTRUIT le PnL depuis le journal (FIFO, outil
# existant) et on le compare à l'état ÉCRIT. Mesuré le 08/10 : 42,12 $ vs 42,12 $ (écart 0,0004).
if [ -f "$REPO_DIR/Index_Maison/scripts/verif_fidelite_pnl.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/verif_fidelite_pnl.py" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : PnL reconstruit ≠ état — classe E2 (voir ci-dessus)" >> "$LOG_FILE"
fi

# SOURCES DES INSTRUMENTS (classe E3, GO 3 — câblé le 08/10/2026)
# Un instrument qui pointe un journal ÉCRIT EN DUR devient aveugle en silence (cas mesuré 21/09).
# Fatal seulement si l'instrument est INVOQUÉ par la boucle ; sinon dette déclarée (R14).
if [ -f "$REPO_DIR/Index_Maison/scripts/verif_sources_instruments.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/verif_sources_instruments.py" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : un instrument invoqué pointe un journal mort — classe E3 (voir ci-dessus)" >> "$LOG_FILE"
fi

# ARRÊT INSTRUIT (classe E26, GO 3 — câblé le 08/10/2026)
# Aucune interruption sans instruction EXPLICITE tracée (leçon 30/09 : j'ai lu une question comme
# un ordre). Un drapeau d'arrêt sans `strategie/ORDRE_ARRET.json` antérieur crie.
if [ -f "$REPO_DIR/Index_Maison/scripts/verif_arret_instruit.py" ]; then
  python3 "$REPO_DIR/Index_Maison/scripts/verif_arret_instruit.py" >> "$LOG_FILE" 2>&1 || \
    echo "[$(date -u +%Y-%m-%dT%H:%MZ)] ALERTE : drapeau d'arrêt sans instruction explicite — classe E26 (voir ci-dessus)" >> "$LOG_FILE"
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
# INSTRUMENTS DE LA BOUCLE (28/09/2026, ALPAGE — « stopper les bidouilles ») :
# `git add -u` ne prend QUE les fichiers DÉJÀ suivis → un instrument NOUVEAU (gardien,
# oracle, sonde, garde-fou) restait HORS GIT jusqu'à ce qu'un humain pense à le stager.
# C'est exactement le trou mesuré par le drill de restauration le 28/09 :
# « gardien_collecte.py, oracle_justesse_collecte.py — 2 instrument(s) que la boucle
# EXÉCUTE et qui ne sont PAS dans git → perdus à la restauration ». Le commit reste
# l'acte de l'auto-sync ; ici on ne fait que rendre VISIBLE ce que la boucle exécute.
# On ne stage QUE du CODE (.py/.sh) à la racine des dossiers d'instruments :
# jamais de données, jamais de .json (le bruit des 1 600+ fichiers non suivis est exclu).
for d in Index_Maison/scripts hulk-mexc/scripts; do
  [ -d "$REPO_DIR/$d" ] || continue
  find "$REPO_DIR/$d" -maxdepth 1 -type f \( -name '*.py' -o -name '*.sh' \) -print0 2>/dev/null \
    | xargs -0 -r git add -- 2>/dev/null
done
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
