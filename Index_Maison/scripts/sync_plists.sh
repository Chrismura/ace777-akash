#!/usr/bin/env bash
# sync_plists.sh — versionne les agents launchd (com.ace777.*) SANS jamais écraser.
# ==============================================================================
# POURQUOI (leçon du 19/09/2026) :
#   97 agents étaient INSTALLÉS, 44 seulement VERSIONNÉS → une restauration de
#   machine perdait 53 organes EN SILENCE (cockpit-http, cockpit-pont,
#   cortana-analyzer, autopilote, superviseur…).
#
#   ⚠️ LEÇON DE LA MÊME JOURNÉE (erreur commise puis corrigée) : la v1 écrasait
#   les plists versionnés par les installés → elle a clobberé 4 fichiers SCELLÉS
#   (whales, pont-onchain, cpfp, veilleuse) et fait crier INTRUSION à la veilleuse.
#   Un fichier scellé ne s'écrase JAMAIS en silence : on DÉCLARE.
#
# RÈGLES (v2) :
#   1. plist installé ABSENT du repo        → copié      (pur gain, aucune perte)
#   2. plist installé DIFFÉRENT du repo     → JAMAIS écrasé : la version installée
#      est archivée dans plists/_derive/ (preuve de ce que launchd exécute) et
#      comptée « à déclarer ». Le repo garde l'état DÉCLARÉ (les scellés restent
#      valides). Déclarer = `--declarer <nom>` (copie _derive → repo) + md5 au
#      registre si scellé.
#
# APPELÉ PAR : git_push_auto.sh (toutes les 3 h) et lisible par le cockpit « vol ».
# USAGE : bash sync_plists.sh [--check | --declarer <nom.plist>]
set -uo pipefail

AGENTS="$HOME/Library/LaunchAgents"
REPO="/Users/christophe/ace777-test-day1/Index_Maison/plists"
DERIVE="$REPO/_derive"
ETAT="/Users/christophe/ace777-test-day1/Index_Maison/thermo/plists_versionnes.json"

mkdir -p "$REPO" "$DERIVE"

# ── Déclarer une dérive : _derive/<nom> → repo (acte explicite, tracé) ────────
if [[ "${1:-}" == "--declarer" ]]; then
    nom="${2:?usage: sync_plists.sh --declarer com.ace777.xxx.plist}"
    if [ ! -f "$DERIVE/$nom" ]; then
        echo "[sync_plists] rien à déclarer pour $nom (pas dans _derive/)"; exit 1
    fi
    cp -p "$DERIVE/$nom" "$REPO/$nom"
    echo "[sync_plists] DÉCLARÉ : $nom ← _derive/ (pense à re-scellé au registre si scellé)"
    exit 0
fi

CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

total=0; crees=0; a_declarer=0
liste_crees=""; liste_derive=""
for src in "$AGENTS"/com.ace777.*.plist; do
    [ -f "$src" ] || continue
    total=$((total + 1))
    nom=$(basename "$src")
    dst="$REPO/$nom"
    if [ ! -f "$dst" ]; then
        if [ $CHECK -eq 0 ]; then cp -p "$src" "$dst"; fi
        crees=$((crees + 1)); liste_crees="$liste_crees $nom"
        echo "  + $nom"
    elif ! cmp -s "$src" "$dst"; then
        # JAMAIS d'écrasement : on archive la version installée comme preuve.
        if [ $CHECK -eq 0 ]; then cp -p "$src" "$DERIVE/$nom"; fi
        a_declarer=$((a_declarer + 1)); liste_derive="$liste_derive $nom"
        echo "  ⚠ à déclarer : $nom (repo conservé)"
    fi
done

versionnes=0; orphelins=0
for f in "$REPO"/com.ace777.*.plist; do
    [ -f "$f" ] || continue
    versionnes=$((versionnes + 1))
    [ -f "$AGENTS/$(basename "$f")" ] || orphelins=$((orphelins + 1))
done

etat="OK"; [ $((crees + a_declarer)) -gt 0 ] && etat="DERIVE"
echo "[sync_plists] installés=$total | versionnés=$versionnes | nouveaux=$crees | À DÉCLARER=$a_declarer | orphelins=$orphelins | état=$etat"

# État lisible par le cockpit « vol » (panneau Gardiens).
python3 - "$ETAT" "$total" "$versionnes" "$crees" "$a_declarer" "$orphelins" "$liste_crees" "$liste_derive" <<'PY'
import json, sys, time
chemin = sys.argv[1]
installes, versionnes, hors_repo, a_decl, orphelins = (int(x) for x in sys.argv[2:7])
json.dump({
    "ts": time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime()),
    "installes": installes,        # agents dans ~/Library/LaunchAgents
    "versionnes": versionnes,      # fichiers dans Index_Maison/plists/
    "hors_repo": hors_repo,        # installés ABSENTS du repo (la dérive qui perd des organes)
    "a_declarer": a_decl,          # installés DIFFÉRENTS du repo (preuve dans _derive/)
    "orphelins": orphelins,        # versionnés mais plus installés
    "liste_hors_repo": sys.argv[7].split() if len(sys.argv) > 7 else [],
    "liste_a_declarer": sys.argv[8].split() if len(sys.argv) > 8 else [],
}, open(chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
PY

# --check : sortie 2 UNIQUEMENT si un agent installé est ABSENT du repo (= organe
# perdu à la restauration). Une divergence « à déclarer » ne sort pas en erreur :
# elle est visible et archivée, c'est un point de revue, pas une perte.
if [ $CHECK -eq 1 ] && [ "$crees" -gt 0 ]; then exit 2; fi
exit 0
