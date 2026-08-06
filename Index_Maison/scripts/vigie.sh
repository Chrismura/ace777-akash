#!/usr/bin/env bash
# ============================================================
# vigie.sh — LA VIGIE : sentinelle de sécurité ACE777
# Lecture seule SAUF chmod 600 des secrets trop ouverts (seul auto-fix).
# Usage : bash vigie.sh [--force]
# Launchd : com.ace777.vigie.plist (toutes les 30 min + au login)
# NB : vit hors de ~/Documents (TCC) pour être exécutable par launchd.
# NB : baseline et références créées le 06/08/2026 APRÈS un audit manuel complet
#      de la machine (vérifiée avant la première exécution de la Vigie).
# ============================================================
set -uo pipefail

HOME_DIR="$HOME"
VAULT="$HOME_DIR/Documents/Obsidian_ACE777"
STATE_DIR="$HOME_DIR/.vigie"
LOG="$HOME_DIR/Library/Logs/vigie.log"
NOTE="$STATE_DIR/SECURITE_VIGIE.md"
BASELINE="$STATE_DIR/baseline.txt"
PERSIST_REF="$STATE_DIR/persistence.txt"
STATE_FILE="$STATE_DIR/state.txt"

mkdir -p "$STATE_DIR"
FORCE=0; [ "${1:-}" = "--force" ] && FORCE=1

ALERTS=(); FIXED=()
now="$(date '+%Y-%m-%dT%H:%M:%S%z')"
log() { printf '%s %s\n' "$now" "$1" >> "$LOG"; }

# ---------- 1) Permissions des secrets (auto-chmod 600) ----------
fix_perm() {
  local f="$1" p
  [ -e "$f" ] || return
  # ne touche que les fichiers appartenant à l'utilisateur courant
  [ "$(stat -f %u "$f" 2>/dev/null)" = "$(id -u)" ] || return
  p=$(stat -f '%Lp' "$f" 2>/dev/null)
  if [ -n "$p" ] && [ "$p" != "600" ]; then
    chmod 600 "$f" 2>/dev/null && FIXED+=("chmod 600 : $f")
  fi
}
while IFS= read -r f; do fix_perm "$f"; done < <(find "$HOME_DIR" -maxdepth 4 \( -iname '*.env' -o -iname '*credential*' -o -iname '*secret*' -o -iname '*api_key*' -o -iname '*.pem' -o -iname 'id_rsa' -o -iname 'id_ed25519' \) -not -path '*/Library/*' -not -path '*/.git/*' 2>/dev/null)
for f in "$HOME_DIR/.config/manicode/credentials.json" "$HOME_DIR/.claude.json" "$HOME_DIR/.binance_testnet.env" "$HOME_DIR/prise-ia/.env" "$HOME_DIR/crypto-voice-assistant-core/.env"; do
  [ -e "$f" ] && fix_perm "$f"
done

# ---------- 2) Persistance nouvelle (1 seule alerte par item) ----------
persist_now="$STATE_DIR/persistence.now"
{
  ls -1 "$HOME_DIR/Library/LaunchAgents/" 2>/dev/null
  ls -1 /Library/LaunchAgents/ 2>/dev/null
  ls -1 /Library/LaunchDaemons/ 2>/dev/null
  crontab -l 2>/dev/null
} | sort -u > "$persist_now"
SEEN="$STATE_DIR/seen.txt"
[ -f "$SEEN" ] || : > "$SEEN"
if [ ! -f "$PERSIST_REF" ]; then
  cp "$persist_now" "$PERSIST_REF"
else
  while IFS= read -r item; do
    if ! grep -qxF "$item" "$PERSIST_REF" 2>/dev/null; then
      if ! grep -qxF "$item" "$SEEN" 2>/dev/null; then
        ALERTS+=("Nouvelle persistance : $item")
        echo "$item" >> "$SEEN"
      fi
    fi
  done < "$persist_now"
fi

# ---------- 3) Ports d'écoute hors localhost ----------
while IFS= read -r line; do
  addr=$(echo "$line" | awk '{print $9}')
  case "$addr" in
    *127.0.0.1:*|*\\[::1\\]*|*::1*) : ;;
    *:*) ALERTS+=("Port d'écoute non-loopback : $line");;
  esac
done < <(lsof -iTCP -sTCP:LISTEN -P -n 2>/dev/null | tail -n +2)

# ---------- 4) Intégrité des fichiers clés ----------
key_files=(
  "$HOME_DIR/ace777-test-day1/Index_Maison/scripts/vigie.sh"
  "$HOME_DIR/ace777-test-day1/Index_Maison/scripts/ace777_aliases.sh"
  "$HOME_DIR/Documents/Obsidian_ACE777/scripts/ada.command"
  "$HOME_DIR/Documents/Obsidian_ACE777/scripts/buffy_reveil.py"
  "$HOME_DIR/.zshrc"
  "$HOME_DIR/prise-ia/hub_prise_ia.py"
  "$HOME_DIR/prise-ia/providers.json"
  "$HOME_DIR/.config/manicode/freebuff"
)
[ -f "$BASELINE" ] || : > "$BASELINE"
for f in "${key_files[@]}"; do
  [ -f "$f" ] || continue
  # > 5 Mo : contrôle taille+date (ex. binaire freebuff 87 Mo qui s'auto-met à jour) — compromis assumé
  if [ "$(stat -f %z "$f" 2>/dev/null || echo 0)" -gt 5242880 ]; then
    h="STAT:$(stat -f '%z:%m' "$f" 2>/dev/null)"
  else
    h=$(shasum -a 256 "$f" 2>/dev/null | awk '{print $1}')
  fi
  [ -n "$h" ] || continue   # fichier illisible (TCC/launchd) : on saute, pas de fausse alerte
  old=$(grep -F "|$f|" "$BASELINE" 2>/dev/null | head -1 | cut -d'|' -f1)
  if [ -z "$old" ]; then
    echo "$h|$f|" >> "$BASELINE"
  elif [ "$old" != "$h" ]; then
    ALERTS+=("Fichier modifié : $f")
    grep -v "^${old}|$f|" "$BASELINE" > "$BASELINE.tmp" 2>/dev/null && mv "$BASELINE.tmp" "$BASELINE"
    echo "$h|$f|" >> "$BASELINE"
  fi
done

# ---------- 5) Secrets suivis par git ----------
for repo in "$VAULT" "$HOME_DIR/ace777-test-day1"; do
  if git -C "$repo" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    leaks=$(git -C "$repo" ls-files 2>/dev/null | grep -E '\.env$|id_rsa|id_ed25519|credential' | head -3 | tr -d '`$')
    [ -n "$leaks" ] && ALERTS+=("Secret suivi par git ($repo) : $leaks")
  fi
done

# ---------- 6) État système : FileVault / pare-feu / womp ----------
fv=$(fdesetup status 2>/dev/null | head -1)
case "$fv" in *[Oo]n*) : ;; *) ALERTS+=("FileVault désactivé : $fv");; esac
fw=$(/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate 2>/dev/null)
case "$fw" in *[Ee]nabled*|*on*) : ;; *) ALERTS+=("Pare-feu désactivé");; esac
womp=$(pmset -g custom 2>/dev/null | grep -c 'womp[[:space:]]*1')
[ "$womp" -gt 0 ] && ALERTS+=("Réveil réseau actif (womp) — à désactiver : sudo pmset -a womp 0")

# ---------- 7) Hub Prise IA localhost uniquement ----------
hub_line=$(lsof -iTCP:11435 -sTCP:LISTEN -P -n 2>/dev/null | tail -n +2 | head -1)
case "$hub_line" in
  *127.0.0.1:11435*) : ;;
  *) [ -n "$hub_line" ] && ALERTS+=("Hub 11435 exposé : $hub_line");;
esac

# ---------- Sortie ----------
n_alert=${#ALERTS[@]}; n_fix=${#FIXED[@]}
prev=$(cat "$STATE_FILE" 2>/dev/null || echo OK)
if [ "$n_alert" -gt 0 ]; then
  status="ALERTE($n_alert)"; log "ALERTE $n_alert alerte(s) · $n_fix correction(s)"
  for a in "${ALERTS[@]}"; do log "  ! $a"; done
else
  status="OK"; log "OK · $n_fix correction(s)"
fi

if [ "$status" != "$prev" ] || [ "$FORCE" = 1 ]; then
  {
    echo "---"; echo "genere: $now"; echo "statut: $status"; echo "---"
    echo "# 🛡️ SECURITE_VIGIE — rapport de La Vigie"
    echo ""
    echo "**Statut :** $status — $(date '+%d/%m/%Y %H:%M')"
    echo ""
    if [ "$n_alert" -gt 0 ]; then
      echo "## 🚨 Alertes"
      for a in "${ALERTS[@]}"; do echo "- $a"; done
    else
      echo "## ✅ Tout est sous contrôle"
      echo ""
      echo "- FileVault : $(echo "$fv" | head -c 60)"
      echo "- Pare-feu : $fw"
    fi
    if [ "$n_fix" -gt 0 ]; then
      echo ""
      echo "## 🔧 Corrections automatiques"
      for fx in "${FIXED[@]}"; do echo "- $fx"; done
    fi
    echo ""
    echo "> Ada copie ce rapport dans le vault à chaque réveil (ada.command). Relance : \`bash $HOME_DIR/ace777-test-day1/Index_Maison/scripts/vigie.sh\`"
  } > "$NOTE"
  echo "$status" > "$STATE_FILE"
fi
# Sortie : 0 = RAS · 2 = alertes actives (état constaté, pas une erreur) · 1 = erreur fatale
if [ "$n_alert" -gt 0 ]; then exit 2; else exit 0; fi
