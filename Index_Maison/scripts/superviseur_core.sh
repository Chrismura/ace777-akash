#!/usr/bin/env bash
# ============================================================
# superviseur_core.sh — COLONNE VERTEBRALE monitoring ACE777
# Absorbe 5 services launchd : heartbeat, pulse-sous-loeil,
# vigie, surveillance-quotas, rotation-logs.
# Cadences internes par fichiers timestamp (~/.superviseur_core/)
# Lancement : launchd toutes les 15 min (900 s)
#
# Partie cœur (heartbeat/pulse/vigie) : code produit par le HUB
# (task code.ia -> nvidia) le 10/08, complété par Ada pour
# quotas/rotation/orchestration (loi du brut : code identique aux
# scripts originaux, zéro réinvention).
# Règle d'or : LIT state.json, ne l'écrit JAMAIS.
# ============================================================
set -uo pipefail

# ---------- Configuration ----------
HOME_DIR="$HOME"
MAISON="$HOME_DIR/ace777-test-day1"
INDEX="$MAISON/Index_Maison"
OUTBOX="$INDEX/OUTBOX_OBSIDIAN"
PRISE_IA="$HOME_DIR/prise-ia"
REPORTS="$PRISE_IA/reports"
STATE_DIR="$HOME_DIR/.superviseur_core"
LOG_CORE="/tmp/superviseur-core.log"
FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

# ---------- Utilitaires ----------
mkdir -p "$STATE_DIR" "$REPORTS" "$OUTBOX/A_Mon_Attention" "$OUTBOX/Index_Maison"
# Réserve audit GEMINI-F1-3 : le dossier d'état doit être accessible en écriture,
# sinon on force les checks à chaque run (protection contre la surcharge CPU).
# (echo direct : core_log est défini plus bas)
if [ ! -w "$STATE_DIR" ]; then
    echo "$(date '+%Y-%m-%dT%H:%M:%S%z') ERREUR: $STATE_DIR non accessible en écriture — checks forcés" >> "$LOG_CORE"
    FORCE=1
fi

# Timestamp epoch portable (Python3)
epoch_now() {
    python3 -c 'import time; print(int(time.time()))'
}

# Vérifie si un check est dû (age >= intervalle secondes)
check_due() {
    local check="$1" interval="$2"
    [ "$FORCE" -eq 1 ] && return 0
    local last_file="$STATE_DIR/${check}.last"
    [ ! -f "$last_file" ] && return 0
    local last=$(cat "$last_file" 2>/dev/null || echo 0)
    local now=$(epoch_now)
    [ $((now - last)) -ge "$interval" ]
}

# Marque un check comme exécuté
mark_done() {
    local check="$1"
    epoch_now > "$STATE_DIR/${check}.last"
}

# Log core (append, borné 500 lignes)
core_log() {
    local msg="$1"
    echo "$(date '+%Y-%m-%dT%H:%M:%S%z') $msg" >> "$LOG_CORE"
    if [ -f "$LOG_CORE" ]; then
        local lines=$(wc -l < "$LOG_CORE" 2>/dev/null || echo 0)
        if [ "$lines" -gt 500 ]; then
            tail -n 500 "$LOG_CORE" > "$LOG_CORE.tmp" && mv "$LOG_CORE.tmp" "$LOG_CORE"
        fi
    fi
}

# ---------- Check 1 : HEARTBEAT (1 h) — code hub ----------
check_heartbeat() {
    local fail=0
    core_log "HEARTBEAT: début"

    local hub_ok="false"
    if curl -s --max-time 6 http://127.0.0.1:11435/health >/dev/null 2>&1; then
        hub_ok="true"
    fi

    local ram_free=0
    eval "$(python3 - <<'PY'
import subprocess
try:
    ps = int(subprocess.check_output(["pagesize"], stderr=subprocess.DEVNULL).decode().strip())
except Exception:
    ps = 16384
out = subprocess.check_output(["vm_stat"], stderr=subprocess.DEVNULL).decode()
d = {}
for line in out.splitlines()[1:]:
    if ":" not in line: continue
    k, v = line.split(":", 1)
    try: d[k.strip()] = int(v.strip().rstrip("."))
    except Exception: pass
free = (d.get("Pages free", 0) + d.get("Pages speculative", 0)) * ps / 1024 / 1024
print(f"RAM_FREE={free:.0f}")
PY
)"

    local git_status="clean"
    if [ -d "$MAISON/.git" ]; then
        git -C "$MAISON" status --porcelain >/dev/null 2>&1 && git_status="dirty" || git_status="clean"
    fi

    python3 - "$hub_ok" "$ram_free" "$git_status" <<'PY'
import json, sys, os
from datetime import datetime, timezone
hub_ok = sys.argv[1] == "true"
ram_free = int(sys.argv[2])
git_status = sys.argv[3]
data = {
    "horodatage": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "hub_ok": hub_ok,
    "ram_free_mb": ram_free,
    "git_status": git_status,
    "source": "superviseur_core"
}
path = os.path.expanduser("~/prise-ia/heartbeat.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w") as f:
    json.dump(data, f, indent=2)
PY

    if [ "$hub_ok" = "false" ]; then
        fail=1
        local alert_file="$OUTBOX/A_Mon_Attention/HEARTBEAT_ALERT.md"
        local pause_file="$MAISON/Index_Maison/PAUSE_ORCHESTRATRICE"
        local alert_age=999999
        if [ -f "$alert_file" ]; then
            alert_age=$(stat -f %m "$alert_file" 2>/dev/null || echo 0)
            case "$alert_age" in *[!0-9]*) alert_age=0;; esac
        fi
        if [ ! -f "$alert_file" ] || [ $(( $(epoch_now) - alert_age )) -gt 3600 ]; then
            cat > "$alert_file" <<EOF
# 🚨 HEARTBEAT ALERT

**Date** : $(date '+%Y-%m-%dT%H:%M:%S%z')
**Statut** : HUB INJOIGNABLE

Le hub local (127.0.0.1:11435) ne répond pas.
Cela peut indiquer un problème majeur.

**Actions** :
- Vérifier le processus hub
- Redémarrer si nécessaire
EOF
            touch "$pause_file"
            core_log "HEARTBEAT: ALERTE hub KO + PAUSE créée"
        fi
    fi

    mark_done "heartbeat"
    core_log "HEARTBEAT: fin (hub_ok=$hub_ok)"
    [ "$fail" -eq 0 ] && echo "OK" || echo "NOK"
}

# ---------- Check 2 : PULSE SOUS L'OEIL (15 min) — code hub ----------
check_pulse() {
    local fail=0 warn=0
    core_log "PULSE: début"

    local ace_on=0 hulk_on=0 ollama_on=0
    pgrep -lf 'GO_USINE_NUAGE|ace777_launch_v85|launch_vide_froid|launch_vortex' >/dev/null 2>&1 && ace_on=1
    [ "$ace_on" -eq 0 ] && pgrep -lf 'launch_test_master_base_v8_6_fortress' >/dev/null 2>&1 && ace_on=1
    pgrep -lf 'paper_diprip' >/dev/null 2>&1 && hulk_on=1
    pgrep -lf 'ollama serve' >/dev/null 2>&1 && ollama_on=1

    local mode="FROID"
    { [ "$ace_on" -eq 1 ] || [ "$hulk_on" -eq 1 ]; } && mode="VOL"

    local ram_label="OK" ram_free=0
    eval "$(python3 - <<'PY'
import subprocess
try:
    ps = int(subprocess.check_output(["pagesize"], stderr=subprocess.DEVNULL).decode().strip())
except Exception:
    ps = 16384
out = subprocess.check_output(["vm_stat"], stderr=subprocess.DEVNULL).decode()
d = {}
for line in out.splitlines()[1:]:
    if ":" not in line: continue
    k, v = line.split(":", 1)
    try: d[k.strip()] = int(v.strip().rstrip("."))
    except Exception: pass
free = (d.get("Pages free", 0) + d.get("Pages speculative", 0)) * ps / 1024 / 1024
print(f"FREE_MB={free:.0f}")
if free >= 400: print("RAM_LABEL=OK")
elif free >= 200: print("RAM_LABEL=TIGHT")
else: print("RAM_LABEL=CRITIQUE")
PY
)"

    local champ="FAIL"
    local gen_md5=$(md5 -q "$MAISON/genesis_manifest.txt" 2>/dev/null || echo "MISSING")
    [[ "$gen_md5" == 8bce77b1* ]] && champ="OK"   # 16/08 re-scellé FIX-LAST-LOSS (autorisation Christophe)

    local hb_age="—" live_age="—"
    if [ -f "$PRISE_IA/heartbeat.json" ]; then
        hb_age=$(python3 -c "import os,time; print(f'{int(time.time()-os.path.getmtime(os.path.expanduser(\"~/prise-ia/heartbeat.json\")))}s')" 2>/dev/null || echo "—")
    fi

    local verdict="OK"
    [ "$champ" = "FAIL" ] && { warn=$((warn+1)); verdict="WARN"; }
    [ "$ram_label" = "CRITIQUE" ] && { fail=$((fail+1)); verdict="NOK"; }
    [ "$ram_label" = "TIGHT" ] && { warn=$((warn+1)); [ "$verdict" = "OK" ] && verdict="WARN"; }

    local report="$INDEX/SOUS_L_OEIL.md"
    cat > "$report" <<EOF
# 👁️ SOUS L'ŒIL — Pulse machine

**Date** : $(date '+%Y-%m-%dT%H:%M:%S%z')
**Mode** : $mode
**Verdict** : $verdict

## Processus
- ACE (lanceur) : $([ "$ace_on" -eq 1 ] && echo "✅ actif" || echo "❌ inactif")
- HULK (paper_diprip) : $([ "$hulk_on" -eq 1 ] && echo "✅ actif" || echo "❌ inactif")
- OLLAMA (serve) : $([ "$ollama_on" -eq 1 ] && echo "✅ actif" || echo "❌ inactif")

## Ressources
- RAM libre : ${ram_free} Mo ($ram_label)
- Champion (genesis_manifest) : $champ

## Fraîcheur
- Heartbeat : $hb_age
- LIVE : $live_age

---
*Généré par superviseur_core.sh — lecture seule, jamais de GO*
EOF
    cp "$report" "$OUTBOX/SOUS_L_OEIL.md"
    cp "$report" "$OUTBOX/Index_Maison/SOUS_L_OEIL.md"

    mark_done "pulse"
    core_log "PULSE: fin (verdict=$verdict)"
    echo "$verdict"
}

# ---------- Check 3 : VIGIE (30 min) — code hub ----------
check_vigie() {
    local fail=0
    core_log "VIGIE: début"

    local vigie_dir="$HOME_DIR/.vigie"
    mkdir -p "$vigie_dir"
    local alerts=() fixed=()
    local now="$(date '+%Y-%m-%dT%H:%M:%S%z')"

    fix_perm() {
        local f="$1" p
        [ -e "$f" ] || return
        [ "$(stat -f %u "$f" 2>/dev/null)" = "$(id -u)" ] || return
        p=$(stat -f '%Lp' "$f" 2>/dev/null)
        if [ -n "$p" ] && [ "$p" != "600" ]; then
            chmod 600 "$f" 2>/dev/null && fixed+=("chmod 600 : $f")
        fi
    }
    while IFS= read -r f; do fix_perm "$f"; done < <(find "$HOME_DIR" -maxdepth 4 \( -iname '*.env' -o -iname '*credential*' -o -iname '*secret*' -o -iname '*api_key*' -o -iname '*.pem' -o -iname 'id_rsa' -o -iname 'id_ed25519' \) -not -path '*/Library/*' -not -path '*/.git/*' 2>/dev/null)
    for f in "$HOME_DIR/.config/manicode/credentials.json" "$HOME_DIR/.claude.json" "$HOME_DIR/.binance_testnet.env" "$HOME_DIR/prise-ia/.env" "$HOME_DIR/crypto-voice-assistant-core/.env"; do
        [ -e "$f" ] && fix_perm "$f"
    done

    local persist_now="$vigie_dir/persistence.now"
    {
        ls -1 "$HOME_DIR/Library/LaunchAgents/" 2>/dev/null
        ls -1 /Library/LaunchAgents/ 2>/dev/null
        ls -1 /Library/LaunchDaemons/ 2>/dev/null
        crontab -l 2>/dev/null
    } | sort -u > "$persist_now"
    local seen="$vigie_dir/seen.txt"
    [ -f "$seen" ] || : > "$seen"
    if [ ! -f "$vigie_dir/persistence.txt" ]; then
        cp "$persist_now" "$vigie_dir/persistence.txt"
    else
        while IFS= read -r item; do
            if ! grep -qxF "$item" "$vigie_dir/persistence.txt" 2>/dev/null; then
                if ! grep -qxF "$item" "$seen" 2>/dev/null; then
                    alerts+=("NOUVELLE PERSISTANCE: $item")
                    echo "$item" >> "$seen"
                fi
            fi
        done < "$persist_now"
    fi

    local ports=$(lsof -iTCP -sTCP:LISTEN -P -n 2>/dev/null | grep -v "127.0.0.1" | grep -v "::1" | grep -v "COMMAND" | head -5)
    [ -n "$ports" ] && alerts+=("PORTS NON-LOOPBACK: $ports")

    if [ -f "$vigie_dir/baseline.txt" ]; then
        while IFS= read -r line; do
            [ -z "$line" ] && continue
            local hash=$(echo "$line" | awk '{print $1}')
            local file=$(echo "$line" | awk '{print $2}')
            if [ -f "$file" ]; then
                local current=$(shasum -a 256 "$file" | awk '{print $1}')
                [ "$current" != "$hash" ] && alerts+=("INTEGRITE: $file modifié")
            fi
        done < "$vigie_dir/baseline.txt"
    fi

    if [ -d "$MAISON/.git" ]; then
        local git_secrets=$(git -C "$MAISON" ls-files 2>/dev/null | grep -E '\.env$|credential|secret|api_key' | head -3)
        [ -n "$git_secrets" ] && alerts+=("SECRETS DANS GIT: $git_secrets")
    fi

    local fv=$(fdesetup status 2>/dev/null | grep -c "On")
    fv=${fv:-0}
    case "$fv" in *[!0-9]*) fv=0;; esac
    [ "$fv" -eq 0 ] && alerts+=("FILEVAULT DESACTIVE")
    local pf=$(/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate 2>/dev/null | grep -c "enabled")
    pf=${pf:-0}
    case "$pf" in *[!0-9]*) pf=0;; esac
    [ "$pf" -eq 0 ] && alerts+=("PARE-FEU DESACTIVE")
    local womp=$(pmset -g custom 2>/dev/null | grep -c "womp.*1")
    womp=${womp:-0}
    case "$womp" in *[!0-9]*) womp=0;; esac
    [ "$womp" -gt 0 ] && alerts+=("WOMP ACTIF (reveil réseau)")

    local hub_exposed=$(lsof -iTCP:11435 -sTCP:LISTEN -P -n 2>/dev/null | grep -v "127.0.0.1" | grep -v "::1" | grep -v "COMMAND" | head -1)
    [ -n "$hub_exposed" ] && alerts+=("HUB EXPOSE: $hub_exposed")

    local state_file="$vigie_dir/state.txt"
    local prev_state=""
    [ -f "$state_file" ] && prev_state=$(cat "$state_file")
    local new_state="OK"
    [ ${#alerts[@]} -gt 0 ] && new_state="ALERTES: ${#alerts[@]}"

    # Chaînes sûres (évite unbound variable avec set -u + tableau vide en bash 3.2)
    local alerts_str="" fixes_str=""
    [ ${#alerts[@]} -gt 0 ] && alerts_str=$(printf -- '- %s\n' "${alerts[@]}")
    [ ${#fixed[@]} -gt 0 ] && fixes_str=$(printf -- '- %s\n' "${fixed[@]}")

    if [ "$new_state" != "$prev_state" ]; then
        cat > "$vigie_dir/SECURITE_VIGIE.md" <<EOF
# 🛡️ SECURITE VIGIE

**Date** : $now
**État** : $new_state

## Alertes (${#alerts[@]})
${alerts_str:-aucune}

## Corrections auto (${#fixed[@]})
${fixes_str:-aucune}

---
*Généré par superviseur_core.sh — sentinelle sécurité*
EOF
        echo "$new_state" > "$state_file"
        core_log "VIGIE: changement d'état -> $new_state"
    fi

    mark_done "vigie"
    core_log "VIGIE: fin (alertes=${#alerts[@]})"
    if [ ${#alerts[@]} -gt 0 ]; then
        echo "WARN"
    else
        echo "OK"
    fi
}

# ---------- Check 4 : SURVEILLANCE QUOTAS (30 min) — code original surveillé ----------
check_quotas() {
    local fail=0
    core_log "QUOTAS: début"

    # Code intégré depuis surveillance_quotas.py (loi du brut : identique à l'original)
    python3 <<'PY'
import os, json, sys
from datetime import datetime, timezone
from collections import defaultdict

HOME = os.path.expanduser("~")
BASE_DIR = os.path.join(HOME, "prise-ia")
USAGE_FILE = os.path.join(BASE_DIR, "usage.jsonl")
PROVIDERS_FILE = os.path.join(BASE_DIR, "providers.json")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
LOG_FILE = os.path.join(REPORT_DIR, "SURVEILLANCE_QUOTAS.log")
OUT_LOG_FILE = os.path.join(REPORT_DIR, "SURVEILLANCE_QUOTAS.out.log")

os.makedirs(REPORT_DIR, exist_ok=True)


def read_json_file(path, description):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERREUR: {description} introuvable: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERREUR: {description} invalide: {path} - {e}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"ERREUR: impossible de lire {description}: {path} - {e}", file=sys.stderr)
        sys.exit(1)


def read_usage_file():
    entries = []
    if not os.path.exists(USAGE_FILE):
        return entries
    with open(USAGE_FILE, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"ERREUR: ligne {line_num} invalide dans usage.jsonl: {e}", file=sys.stderr)
    return entries


def main():
    providers_data = read_json_file(PROVIDERS_FILE, "providers.json")
    providers_list = providers_data.get("providers", [])
    if not isinstance(providers_list, list):
        print("ERREUR: providers.json doit contenir une liste 'providers'", file=sys.stderr)
        sys.exit(1)

    active_providers = {}
    for p in providers_list:
        if not isinstance(p, dict):
            continue
        pid = p.get("id") or p.get("name")
        if pid and p.get("enabled", True):
            active_providers[str(pid)] = True

    entries = read_usage_file()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    today_entries = []
    for e in entries:
        ts = e.get("ts", "")
        if isinstance(ts, str) and ts.startswith(today):
            today_entries.append(e)

    provider_stats = defaultdict(lambda: {"appels": 0, "echecs": 0, "recent_errors": []})
    for e in today_entries:
        provider = e.get("provider")
        if not provider:
            continue
        provider = str(provider)
        if provider not in active_providers:
            continue
        stats = provider_stats[provider]
        stats["appels"] += 1
        status = e.get("status", "ok")
        error = e.get("error")
        if status != "ok" or error:
            stats["echecs"] += 1
            stats["recent_errors"].append(e)

    alerts = []
    for provider, stats in provider_stats.items():
        appels = stats["appels"]
        echecs = stats["echecs"]
        recent_errors = stats["recent_errors"]
        recent_count = len(recent_errors)
        last_10 = [e for e in today_entries if str(e.get("provider")) == provider][-10:]
        last_10_errors = sum(1 for e in last_10 if e.get("status", "ok") != "ok" or e.get("error"))
        rate = last_10_errors / len(last_10) if last_10 else 0

        if recent_count >= 2 or (len(last_10) >= 2 and rate > 0.5):
            alerts.append((provider, appels, echecs))

    if alerts:
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                for provider, appels, echecs in alerts:
                    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    f.write(f"[{ts}] ALERTE provider={provider} appels={appels} echecs={echecs}\n")
        except OSError as e:
            print(f"ERREUR: impossible d'écrire le log: {e}", file=sys.stderr)
            sys.exit(1)

    out_lines = [f"SURVEILLANCE QUOTAS - {today}"]
    if not active_providers:
        out_lines.append("Aucun provider actif configuré")
    else:
        for provider in active_providers:
            stats = provider_stats.get(provider, {"appels": 0, "echecs": 0})
            appels = stats["appels"]
            echecs = stats["echecs"]
            if echecs >= 3 or (appels > 0 and echecs / appels > 0.5):
                etat = "MORT"
            elif echecs >= 1:
                etat = "FAIBLE"
            else:
                etat = "OK"
            out_lines.append(f"{provider}: {appels} appels, {echecs} echecs, {etat}")
    try:
        with open(OUT_LOG_FILE, "a", encoding="utf-8") as f:
            f.write("\n".join(out_lines) + "\n")
    except OSError:
        pass
    # NOTE : pas de print sur stdout (le contrat de sortie du core est sur stdout)


main()
PY
    local rc=$?
    mark_done "quotas"
    core_log "QUOTAS: fin (rc=$rc)"
    [ "$rc" -eq 0 ] && echo "OK" || echo "NOK"
}

# ---------- Check 5 : ROTATION LOGS (6 h) — code original ----------
check_rotation() {
    local fail=0
    core_log "ROTATION: début"

    # Code intégré depuis rotation_logs.py (loi du brut : identique à l'original)
    python3 <<'PY'
import os
import shutil
from datetime import datetime, timezone

SEUIL_OCTETS = 500000
BACKUP_COUNT = 3
BASE_DIR = "/Users/christophe/prise-ia"
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
ROTATION_LOG = os.path.join(REPORTS_DIR, "ROTATION.log")


def get_files():
    files = [
        os.path.join(REPORTS_DIR, "SYNC_LOG.md"),
        os.path.join(BASE_DIR, "usage.jsonl"),
        os.path.join(BASE_DIR, "hub_events.jsonl"),
        os.path.join(REPORTS_DIR, "SUPERVISEUR.log"),
    ]
    try:
        for entry in os.listdir(REPORTS_DIR):
            full = os.path.join(REPORTS_DIR, entry)
            if os.path.isfile(full) and (entry.endswith(".log") or entry.endswith(".out.log") or entry.endswith(".err.log")):
                files.append(full)
    except OSError:
        pass
    return files


def rotate_file(filepath):
    try:
        size = os.path.getsize(filepath)
    except OSError:
        return None
    if size <= SEUIL_OCTETS:
        return None

    try:
        for i in range(BACKUP_COUNT, 0, -1):
            src = f"{filepath}.{i-1}" if i > 1 else filepath
            dst = f"{filepath}.{i}"
            if i == 1:
                shutil.copy2(filepath, dst)
            else:
                if os.path.exists(src):
                    if os.path.exists(dst):
                        os.remove(dst)
                    os.rename(src, dst)
        with open(filepath, "w", encoding="utf-8") as f:
            f.truncate(0)
        extra = f"{filepath}.{BACKUP_COUNT+1}"
        if os.path.exists(extra):
            os.remove(extra)
        return size
    except Exception:
        return None


def main():
    now = datetime.now(timezone.utc).isoformat()
    rotated = []
    for f in get_files():
        size = rotate_file(f)
        if size is not None:
            rotated.append((f, size))
            try:
                with open(ROTATION_LOG, "a", encoding="utf-8") as log:
                    log.write(f"[{now}] rotation: {f} ({size} octets -> archive .1, backups: {BACKUP_COUNT})\n")
            except OSError:
                pass
    # NOTE : pas de print sur stdout (le contrat de sortie du core est sur stdout)


main()
PY
    local rc=$?
    mark_done "rotation"
    core_log "ROTATION: fin (rc=$rc)"
    [ "$rc" -eq 0 ] && echo "OK" || echo "NOK"
}

# ============================================================
# ORCHESTRATION (bash 3.2 macOS : pas de tableaux associatifs)
# BOUCLE INTERNE (spec V2 [C2] + corrections famille 10/08) :
# le processus reste VIVANT (KeepAlive:true) — jamais une seule execution.
# ============================================================

# C2 (famille/DEEPSEEK) : arrêt propre sur signal
# (sinon un `launchctl kickstart -k` tuerait la boucle sans contrat de sortie)
trap 'echo "CORE=STOP"; exit 0' INT TERM

while true; do
    R_HEARTBEAT="SKIP"; R_PULSE="SKIP"; R_VIGIE="SKIP"; R_QUOTAS="SKIP"; R_ROTATION="SKIP"

    # Correction famille BLOQUANTE (4/4 : GEMINI/DEEPSEEK/JUGE/ULTRA) :
    # gestion de FORCE par cycle — un `--force` relance un cycle complet immediat
    # (timestamps remis a 0) puis la boucle continue normalement.
    if [ "$FORCE" = "1" ]; then
        : > "$STATE_DIR/heartbeat.last"
        : > "$STATE_DIR/pulse.last"
        : > "$STATE_DIR/vigie.last"
        : > "$STATE_DIR/quotas.last"
        : > "$STATE_DIR/rotation.last"
        FORCE=0
        core_log "BOUCLE: cycle force (--force) — timestamps reinitialises"
    fi

    # heartbeats : 1 h = 3600 s ; vigie/quotas : 30 min = 1800 s ; rotation : 6 h = 21600 s
    # Réserve audit GEMINI-F1-2 : chaque check encapsulé avec fallback NOK (jamais de
    # variable vide qui fausserait le contrat de sortie CORE=OK|WARN|NOK).
    if check_due "heartbeat" 3600; then R_HEARTBEAT=$(check_heartbeat || echo "NOK"); fi
    if check_due "pulse" 900; then R_PULSE=$(check_pulse || echo "NOK"); fi
    if check_due "vigie" 1800; then R_VIGIE=$(check_vigie || echo "NOK"); fi
    if check_due "quotas" 1800; then R_QUOTAS=$(check_quotas || echo "NOK"); fi
    if check_due "rotation" 21600; then R_ROTATION=$(check_rotation || echo "NOK"); fi

    # Contrat de sortie (identique a l'existant, ecrit a CHAQUE cycle)
    NOK_COUNT=0
    ALL="$R_HEARTBEAT $R_PULSE $R_VIGIE $R_QUOTAS $R_ROTATION"
    for r in $ALL; do
        [ "$r" = "NOK" ] && NOK_COUNT=$((NOK_COUNT+1))
    done

    if [ "$NOK_COUNT" -gt 0 ]; then
        CORE="NOK"
    elif [[ "$ALL" == *WARN* ]]; then
        CORE="WARN"
    else
        CORE="OK"
    fi

    echo "CORE=$CORE checks=heartbeat:$R_HEARTBEAT,pulse:$R_PULSE,vigie:$R_VIGIE,quotas:$R_QUOTAS,rotation:$R_ROTATION"

    # Pause entre cycles (60 s) — le processus reste vivant. Protégée :
    # un signal pendant le sleep ne casse pas la boucle (correction DEEPSEEK).
    sleep 60 || true
done
