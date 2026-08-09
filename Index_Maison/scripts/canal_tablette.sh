#!/bin/bash
# canal_tablette.sh — Chantier C4 : canal tablette pour les signets X (09/08/2026)
# iCloud Drive inactif sur ce Mac → dossier Tablette/ + serveur HTTP LAN.
# Si iCloud Drive s'active : copier $TAB vers CloudDocs pour l'offline.
set -uo pipefail
VAULT=~/Documents/Obsidian_ACE777/Signets_X
TAB=~/ace777-test-day1/Index_Maison/Tablette
PORT=8899
mkdir -p "$TAB"

# Signets datés (format 2026-MM-DD), plus récents d'abord — les Bookmark_Master_* (héritage) exclus
RECENTS=$(find "$VAULT" -name '*.md' -print0 | xargs -0 -I{} basename '{}' | grep -E '^20[0-9]{2}-[0-9]{2}-[0-9]{2}' | sort -r | head -80)

# 1) INDEX_SIGNETS.md
{
  echo "# 📱 SIGNETS — canal tablette"
  echo
  echo "> Généré $(date '+%Y-%m-%d %H:%M %Z') · coffre Signets_X · plus récents d'abord"
  echo
  printf '%s\n' "$RECENTS" | sed 's/^/- /'
  echo
  echo "## 📄 Derniers signets (contenu intégral ci-dessous)"
} > "$TAB/INDEX_SIGNETS.md"

# 2) Copier les 10 plus récents (contenu lisible)
printf '%s\n' "$RECENTS" | head -10 | while read -r f; do
  src=$(find "$VAULT" -name "$f" | head -1)
  [ -n "$src" ] && cp "$src" "$TAB/$(basename "$f")" && echo "copié: $f"
done

# 3) Serveur HTTP LAN (si pas déjà lancé)
if ! lsof -nP -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  nohup python3 -m http.server "$PORT" --bind 0.0.0.0 --directory "$TAB" >/tmp/canal_tablette_http.log 2>&1 &
  sleep 2
fi
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo '192.168.x.x')
echo "✅ CANAL TABLETTE PRÊT"
echo "   Dossier : $TAB"
echo "   Index tablette : http://$IP:$PORT/INDEX_SIGNETS.md"
