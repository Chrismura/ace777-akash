#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle : Détecteur de CHOC MACRO (mode "macro tempête").
Contexte ACE777 : le 19-20/08/2026, BTC +8 % en 24 h (volume ×3) sur décision
Trésor/Fed/Bessent. BETA (scout, FORCE_ENTRY_SIDE=SELL) a fait 255 fills SELL
à contre-courant de la hausse → -48,66 USDT sur le run. Ce détecteur écrit un
flag que radar_gate.rb lit à chaque cycle : en choc haussier, les SELL sont
bloqués ; en choc baissier, les BUY sont bloqués.

Doctrine : stdlib uniquement, écriture atomique, kill-switch, idempotent,
100 % gratuit (lit thermo/live.json déjà produit). Lancé par launchd (--once).
"""
import os
import sys
import time
import json
import tempfile
from datetime import datetime, timezone

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
INDEX_MAISON = os.path.join(BASE_DIR, "Index_Maison")
STRATEGIE_DIR = os.path.join(INDEX_MAISON, "strategie")
RUNS_DIR = os.path.join(BASE_DIR, "runs")

LIVE_JSON = os.path.join(INDEX_MAISON, "thermo", "live.json")
OUTPUT_JSON = os.path.join(RUNS_DIR, "macro_tempete.json")
HIST_VOL_FILE = os.path.join(INDEX_MAISON, "data", "macro_vol_hist.jsonl")

STOP_FILE = os.path.join(STRATEGIE_DIR, "STOP")
STOP_ALL_FILE = os.path.join(INDEX_MAISON, "STOP_ALL")

# Molettes (env, défauts maison)
CHG24_PCT = float(os.environ.get("MACRO_TEMPETE_CHG24_PCT", "3.0"))     # |chg24| ≥ 3 % = choc
VOL_RATIO = float(os.environ.get("MACRO_TEMPETE_VOL_RATIO", "3.0"))     # volume ≥ ×3 médiane 7j = confirmé
VOL_HIST_DAYS = int(os.environ.get("MACRO_TEMPETE_VOL_HIST_DAYS", "7"))
VOL_HIST_MAX = int(os.environ.get("MACRO_TEMPETE_VOL_HIST_MAX", "5000"))  # purge sécurité


def check_kill_switch():
    for s in (STOP_FILE, STOP_ALL_FILE):
        if os.path.exists(s):
            print(f"[KILL-SWITCH] Arrêt d'urgence : {s}", file=sys.stderr)
            sys.exit(0)


def atomic_write_json(filepath, data):
    check_kill_switch()
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(filepath), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp, filepath)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


def median(vals):
    if not vals:
        return None
    s = sorted(vals)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2.0


def load_vol_history():
    """Retourne [(ts, volQuote)] sur la fenêtre, et purge les vieux."""
    check_kill_switch()
    now = int(time.time())
    cutoff = now - VOL_HIST_DAYS * 86400
    rows = []
    if os.path.exists(HIST_VOL_FILE):
        try:
            with open(HIST_VOL_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        o = json.loads(line)
                        if o.get("ts", 0) >= cutoff:
                            rows.append((o["ts"], float(o.get("vol", 0.0))))
                    except (json.JSONDecodeError, KeyError, ValueError):
                        continue
        except OSError:
            pass
    # Purge atomique si trop gros
    if len(rows) > VOL_HIST_MAX:
        rows = rows[-VOL_HIST_MAX:]
        _rewrite_history(rows)
    return rows


def _rewrite_history(rows):
    check_kill_switch()
    os.makedirs(os.path.dirname(HIST_VOL_FILE), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(HIST_VOL_FILE), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            for ts, vol in rows:
                f.write(json.dumps({"ts": ts, "vol": vol}) + "\n")
        os.replace(tmp, HIST_VOL_FILE)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)


def append_vol(ts, vol):
    check_kill_switch()
    try:
        os.makedirs(os.path.dirname(HIST_VOL_FILE), exist_ok=True)
        with open(HIST_VOL_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": ts, "vol": vol}) + "\n")
    except OSError as e:
        print(f"[ERREUR] append hist volume: {e}", file=sys.stderr)


def main():
    check_kill_switch()
    if not os.path.exists(LIVE_JSON):
        print("[ERREUR] thermo/live.json absent — flag inchangé (fail-open).", file=sys.stderr)
        sys.exit(1)

    try:
        with open(LIVE_JSON, "r", encoding="utf-8") as f:
            live = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"[ERREUR] lecture live.json: {e} — flag inchangé.", file=sys.stderr)
        sys.exit(1)

    chg24 = float(live.get("chg24") or 0.0)
    vol = float(live.get("volQuote") or 0.0)
    now = int(time.time())

    # Historique volume → ratio × médiane (baseline locale, 7 jours)
    hist = load_vol_history()
    vols = [v for _, v in hist if v > 0]
    med_vol = median(vols)
    vol_ratio = (vol / med_vol) if (med_vol and med_vol > 0 and vol > 0) else None
    append_vol(now, vol)

    # Décision
    abs_chg = abs(chg24)
    choc_haussier = chg24 >= CHG24_PCT
    choc_baissier = chg24 <= -CHG24_PCT
    choc = choc_haussier or choc_baissier
    confirme_volume = vol_ratio is not None and vol_ratio >= VOL_RATIO

    # Raison : chg seul suffit à déclencher ; volume confirme (info)
    if choc_haussier:
        direction = "long"
        raisons = [f"chg24={chg24:+.2f}% >= {CHG24_PCT}%"]
    elif choc_baissier:
        direction = "short"
        raisons = [f"chg24={chg24:+.2f}% <= -{CHG24_PCT}%"]
    else:
        direction = "none"
        raisons = [f"chg24={chg24:+.2f}% < {CHG24_PCT}%"]
    if confirme_volume:
        raisons.append(f"vol x{vol_ratio:.1f} >= x{VOL_RATIO}")
    elif vol_ratio is not None:
        raisons.append(f"vol x{vol_ratio:.1f}")
    else:
        raisons.append("vol baseline insuffisante (calibration)")

    out = {
        "ts": now,
        "utc": datetime.now(timezone.utc).isoformat(),
        "active": bool(choc),
        "direction": direction,          # "long" = choc haussier → bloquer SELL ; "short" = choc baissier → bloquer BUY
        "chg24": round(chg24, 4),
        "vol": round(vol, 2),
        "vol_ratio": round(vol_ratio, 2) if vol_ratio is not None else None,
        "seuil_chg24_pct": CHG24_PCT,
        "seuil_vol_ratio": VOL_RATIO,
        "confirme_volume": confirme_volume,
        "raison": " ; ".join(raisons),
    }
    atomic_write_json(OUTPUT_JSON, out)
    status = "ACTIF" if choc else "calme"
    print(f"[MACRO-TEMPÊTE] {status} dir={direction} chg24={chg24:+.2f}% vol_ratio={out['vol_ratio']} → {OUTPUT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
