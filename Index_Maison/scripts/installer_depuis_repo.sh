#!/usr/bin/env bash
# installer_depuis_repo.sh — PILIER 1 : LE REPO EST L'INSTALLATION.
# ==============================================================================
# POURQUOI (20/09/2026, GO Christophe — suite du chantier « incassable/auto-réparant ») :
#   `sync_plists.sh` fait repo ← installé (il versionne, donc plus rien ne se perd).
#   Il manquait le sens inverse : installé ← repo. Résultat : deux endroits pour un
#   même agent (le repo et ~/Library/LaunchAgents) → une dérive est TOUJOURS possible,
#   et une machine neuve n'a AUCUN moyen simple de remettre les 99 agents en place.
#   Ici, on SUPPRIME la duplication : le fichier installé devient un LIEN vers le repo.
#   Une seule source, donc une dérive devient *impossible par construction*.
#
# RÈGLES (les mêmes que sync_plists.sh — un scellé/un choix ne s'écrase JAMAIS en silence) :
#   1. installé ABSENT                 → lien créé (pur gain)
#   2. installé IDENTIQUE au repo      → remplacé par un lien (contenu inchangé, zéro effet)
#   3. installé DIFFÉRENT du repo      → JAMAIS touché : signalé « à déclarer »
#   4. installé NON CONFORME mais repo absent → jamais touché : signalé
#
# MODES :
#   --verifier (défaut) : LECTURE SEULE. Écrit thermo/installation_repo.json et sort 2
#                         si un agent installé n'est pas conforme au repo (= dérive).
#                         Appelé par git_push_auto.sh (3 h) : la dérive devient visible.
#   --lier              : ACTE DÉLIBÉRÉ (GO). Remplace les fichiers conformes par des liens
#                         vers le repo. Sauvegarde chaque fichier écrasé dans
#                         plists/_ecrases_du_jour/ (preuve) avant de le faire.
#
# USAGE : bash installer_depuis_repo.sh [--verifier | --lier | --check]
set -uo pipefail

AGENTS="$HOME/Library/LaunchAgents"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/plists"
ARCHIVE="$REPO/_ecrases_du_jour"
ETAT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/thermo/installation_repo.json"
TS=$(date -u +%Y-%m-%dT%H:%MZ)

MODE="verifier"
case "${1:-}" in
    --lier) MODE="lier" ;;
    --verifier|--check|"") MODE="verifier" ;;
    *) echo "usage: installer_depuis_repo.sh [--verifier | --lier]"; exit 1 ;;
esac

mkdir -p "$ARCHIVE"

lies=0; a_lier=0; divergents=0; absents=0; liens_existants=0
liste_divergents=""

for src in "$REPO"/com.ace777.*.plist; do
    [ -f "$src" ] || continue
    nom=$(basename "$src")
    inst="$AGENTS/$nom"

    if [ -L "$inst" ]; then
        # Déjà un lien : conforme s'il pointe bien vers CE repo.
        cible=$(readlink "$inst")
        if [ "$cible" = "$src" ]; then liens_existants=$((liens_existants + 1))
        else divergents=$((divergents + 1)); liste_divergents="$liste_divergents $nom"; fi
        continue
    fi

    if [ ! -e "$inst" ]; then
        absents=$((absents + 1))
        if [ "$MODE" = "lier" ]; then
            ln -s "$src" "$inst" && echo "  + lien créé : $nom"
        fi
        continue
    fi

    if cmp -s "$src" "$inst"; then
        # Conforme : le contenu est déjà le bon → le lien ne change RIEN au comportement.
        if [ "$MODE" = "lier" ]; then
            cp -p "$inst" "$ARCHIVE/$nom.$TS.avant-lien"
            rm -f "$inst" && ln -s "$src" "$inst" && echo "  ~ lié (conforme) : $nom" && lies=$((lies + 1))
        else
            a_lier=$((a_lier + 1))
        fi
    else
        # DIVERGENT : c'est exactement ce que la maison ne fait jamais en silence.
        divergents=$((divergents + 1)); liste_divergents="$liste_divergents $nom"
    fi
done

total=$(ls -1 "$REPO"/com.ace777.*.plist 2>/dev/null | wc -l | tr -d ' ')

echo "[installer_depuis_repo] mode=$MODE | versionnés=$total | déjà liés=$liens_existants | liés ce passage=$lies | à lier=$a_lier | absents=$absents | DIVERGENTS=$divergents"
[ -n "$liste_divergents" ] && echo "[installer_depuis_repo] à déclarer (JAMAIS touchés) :$liste_divergents"

python3 - "$ETAT" "$MODE" "$total" "$liens_existants" "$lies" "$a_lier" "$absents" "$divergents" "$liste_divergents" "$TS" <<'PY'
import json, sys
chemin, mode, total, deja, lies, a_lier, absents, divergents, liste, ts = sys.argv[1:11]
json.dump({
    "ts": ts,
    "mode": mode,
    "versionnes": int(total),
    "deja_lies": int(deja),
    "lies_ce_passage": int(lies),
    "a_lier": int(a_lier),
    "absents": int(absents),
    "divergents": int(divergents),
    "liste_divergents": liste.split(),
    "principe": "Le repo EST l'installation : le fichier installé est un lien vers Index_Maison/plists/. "
                "Une dérive installé/repo devient impossible par construction.",
}, open(chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
PY

# Sort 2 uniquement sur une VRAIE dérive (un agent installé non conforme au repo).
if [ "$MODE" = "verifier" ] && [ "$divergents" -gt 0 ]; then exit 2; fi
exit 0
