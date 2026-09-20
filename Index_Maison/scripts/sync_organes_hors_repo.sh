#!/usr/bin/env bash
# sync_organes_hors_repo.sh — MIROIR DE SAUVEGARDE des organes qui vivent HORS du repo git.
# ==============================================================================
# POURQUOI (leçon du 19/09/2026) :
#   Le drill de restauration a montré que `~/prise-ia` (le HUB des providers — l'organe
#   qui fait tourner TOUTE l'IA de la maison) n'était versionné NULLE PART :
#   une machine neuve ne le ramenait pas. `~/mirofis` a lui son git amont + son image
#   Docker, donc il est déjà restaurable — mais personne ne le DISAIT (trou silencieux).
#
# DOCTRINE (anti-doublon) :
#   - Le VIVANT reste là où il est (`~/prise-ia`). Ce dossier est un MIROIR DE SAUVEGARDE,
#     pas une 2e source de vérité. On ne le modifie JAMAIS à la main ; on le régénère.
#   - Seules les SOURCES sont copiées (code/config/docs). Jamais : .env (clés), logs,
#     historiques .jsonl, sauvegardes .bak, états runtime, dossiers de rapports.
#   - `rsync --delete` dans le miroir : il reflète l'état actuel, aucune vieille copie.
#
# APPELÉ PAR : git_push_auto.sh (toutes les 3 h) → la copie part sur GitHub (ace777-akash).
# RÉSULTAT : le drill de restauration lit thermo/organes_hors_repo.json et, si le miroir
#   est frais, il ne compte PLUS ces organes comme « perdus ».
# USAGE : bash sync_organes_hors_repo.sh [--check]
set -uo pipefail

RACINE="$HOME/ace777-test-day1"
MIROIR="$RACINE/Index_Maison/organes_hors_repo"
ETAT="$RACINE/Index_Maison/thermo/organes_hors_repo.json"
CHECK=0; [[ "${1:-}" == "--check" ]] && CHECK=1

mkdir -p "$MIROIR"

# Organes hors git du prototype. mode = miroir-source (on copie) | git-amont (déjà versionné ailleurs).
# Format : nom|chemin_vivant|mode|remote_ou_vide
ORGANES=(
  "prise-ia|$HOME/prise-ia|miroir-source|"
  "mirofis|$HOME/mirofis|git-amont|$(git -C "$HOME/mirofis" remote get-url origin 2>/dev/null || echo '')"
)

EXCLUS=(
  "--exclude=.env*" "--exclude=*.log" "--exclude=*.err" "--exclude=*.out"
  "--exclude=*.jsonl*" "--exclude=*.bak*" "--exclude=*.pid"
  "--exclude=hub.db*" "--exclude=__pycache__/" "--exclude=.DS_Store"
  "--exclude=reports/" "--exclude=backups_routing/" "--exclude=.dockerignore"
  # états runtime (reconstruits tout seuls) — pas des sources
  "--exclude=heartbeat.json" "--exclude=observatoire.json"
  "--exclude=node_modules/" "--exclude=.git/"
)

ITEMS=()
for ligne in "${ORGANES[@]}"; do
  IFS='|' read -r nom src mode remote <<< "$ligne"
  if [ ! -d "$src" ]; then
    echo "  ⚠ $nom : $src introuvable (organe absent ?)"
    continue
  fi
  if [[ "$mode" == "git-amont" ]]; then
    echo "  ✓ $nom : déjà versionné en amont ($remote) — rien à copier"
    ITEMS+=("$nom|git-amont|$src||$remote")
    continue
  fi
  if [ $CHECK -eq 1 ]; then
    echo "  · $nom : miroir présent ? $([ -d "$MIROIR/$nom" ] && echo oui || echo NON)"
    continue
  fi
  rsync -a --delete "${EXCLUS[@]}" "$src/" "$MIROIR/$nom/"
  echo "  + $nom : sources mirées → organes_hors_repo/$nom/ ($(find "$MIROIR/$nom" -type f | wc -l | tr -d ' ') fichiers)"
  ITEMS+=("$nom|miroir-source|$src|$MIROIR/$nom|")
done

[ $CHECK -eq 1 ] && exit 0

# Manifeste lisible par le drill + par un humain qui restaure.
#   champ « chemin_vivant »  = où l'organe tourne (jamais modifié ici)
#   champ « chemin_miroir »  = la copie de sauvegarde qui part sur GitHub
python3 - "$ETAT" "${ITEMS[@]}" <<'PY'
import json, sys, time, pathlib
etat = sys.argv[1]
organes = []
for item in sys.argv[2:]:
    nom, mode, vivant, miroir, remote = (item.split("|") + ["", "", "", "", ""])[:5]
    o = {"nom": nom, "mode": mode, "chemin_vivant": vivant}
    if remote:
        o["remote"] = remote
    if miroir:
        d = pathlib.Path(miroir)
        o["chemin_miroir"] = miroir
        o["fichiers"] = sum(1 for f in d.rglob("*") if f.is_file())
        o["octets"] = sum(f.stat().st_size for f in d.rglob("*") if f.is_file())
    organes.append(o)
json.dump({"ts": time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime()), "organes": organes},
          open(etat, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"[organes_hors_repo] {len(organes)} organe(s) → {etat}")
PY
exit 0
