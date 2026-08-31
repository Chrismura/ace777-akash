#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""satellite_aspiration.py — SATELLITE carnet/aspiration (Phase 3, 31/08, GO Christophe).

POURQUOI
--------
Phase 3 « moteur léger et costaud » : sortir la LECTURE du carnet de profondeur
(aspiration_sense) du cœur de trading pour alléger la boucle de décision et
isoler les pannes réseau. Ce satellite est un démon autonome qui fait le travail
d'OBSERVATION (radar aspiration par paire active) et écrit un fichier JSON unique,
écrit ATOMIQUEMENT (fichier .tmp + os.replace) : runs/aspiration_live.json.

ZÉRO RISQUE :
- Le moteur Hulk continue de tourner INLINE tant que la bascule config
  (ASPIRATION_SRC=fichier) n'est PAS activée. Ce satellite observe et écrit.
- Une fois validé sur plusieurs jours, on bascule le cœur sur ce fichier via
  ESP/ASPIRATION_SRC → la lecture carnet sort du cœur. Rien n'est forcé.

CONTENU DE aspiration_live.json (écrit en continu, ~1×/LOOP_SEC) :
  { ts, frais, btc_price, gex:{callWall,putWall,ok},
    paires: { SYM: {régime, side, drop_bid_pct_per_s, drop_ask_pct_per_s,
                    max_drop_pct_per_s, spread_bps, spread_delta_bps,
                    wall_bid_usdt, wall_ask_usdt, notional_drop_ok,
                    spoof, price_delta_pct, price, delay_s} } }

USAGE : python3 scripts/satellite_aspiration.py   (boucle continue)
Planifié par launchd com.ace777.satellite-aspiration (StartInterval ~20s via --once
ou boucle interne ; on utilise --once + StartInterval pour la résilience launchd).

Lecture des paires actives : depuis le DERNIER state du moteur (PAPER_V1_*_state.json)
pour connaître le régime de chaque paire (COOLING/IMPULSE = actives). Fail-open :
si pas de state, on ne fait rien.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
LIVE = RUNS / "aspiration_live.json"
LOOP_SEC = 20.0          # cadence d'écriture (le moteur a une boucle 20s aussi)
MAX_PAIRS = 5            # max paires sondées par passe (rate-limit MEXC)
STALE_STATE_MAX = 120.0  # un state moteur + vieux que ça = on abandonne la passe
HTTP_TIMEOUT = 12.0

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ace_sense_mexc import aspiration_sense  # noqa: E402


def http_json(url, timeout=HTTP_TIMEOUT, retries=1):
    import signal
    import urllib.request

    last_err = None
    for attempt in range(max(1, retries)):
        try:
            prev = signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError("alarm")))
            signal.alarm(int(timeout) + 2)
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "hulk-satellite/1.0"})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return json.loads(r.read().decode())
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, prev)
        except Exception as e:
            last_err = e
            time.sleep(0.3 * (attempt + 1))
    raise last_err


def derniere_paires():
    """Lit le dernier state du moteur → {pair: regime}. Fail-open."""

    def to_state(st):
        return st.get("ts"), st.get("scores") or {}

    best = None
    for f in RUNS.glob("PAPER_V1_*_state.json"):
        try:
            ts = f.stat().st_mtime
            if best is None or ts > best[0]:
                best = (ts, f)
        except Exception:
            continue
    if not best:
        return {}
    if time.time() - best[0] > STALE_STATE_MAX:
        return {}
    try:
        st = json.loads(best[1].read_text(encoding="utf-8"))
    except Exception:
        return {}
    scores = st.get("scores") or {}
    pairs_cfg = set(p.strip().upper() for p in (st.get("pairs") or []))
    return {p: ((scores.get(p) or {}).get("regime") or "?") for p in pairs_cfg}


def gex_local():
    """Lit la GEX wall depuis thermo/live.json (fichier local, pas réseau)."""
    try:
        live = json.loads((ROOT / "Index_Maison" / "thermo" / "live.json").read_text())
        gex = live.get("gex") or {}
        return {"ok": bool(gex.get("ok")),
                "callWall": float(gex.get("callWall") or 0),
                "putWall": float(gex.get("putWall") or 0)}
    except Exception:
        return {"ok": False, "callWall": 0, "putWall": 0}


def atomic_write(path: Path, data: dict):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def saisir_prix(pairs):
    """1 appel batch → {pair: prix} (même technique que le cœur Phase 1)."""
    out = {}
    try:
        data = http_json("https://api.mexc.com/api/v3/ticker/price")
    except Exception:
        return out
    if isinstance(data, list):
        want = set(pairs)
        for it in data:
            if isinstance(it, dict) and it.get("symbol") in want:
                try:
                    out[it["symbol"]] = float(it["price"])
                except Exception:
                    continue
    return out


def run_once() -> int:
    paires = derniere_paires()
    if not paires:
        # pas de state frais → ne rien écrire (on ne cache pas l'absente)
        return 0
    actives = [p for p, r in paires.items() if r in ("COOLING", "IMPULSE")][: MAX_PAIRS]
    prix = saisir_prix(list(paires.keys()))
    btc = prix.get("BTCUSDT", 0.0)
    radar = {}

    for pair in actives + []:
        pass
    for pair in actives:
        radar[pair] = {"regime": paires.get(pair, "?"), "prix": prix.get(pair, 0.0)}
        try:
            a = aspiration_sense(pair, http_json, delay_s=0.5,
                                 min_notional_usdt=500)
        except Exception as e:
            radar[pair]["ok"] = False
            radar[pair]["reason"] = f"probe_err:{e}"
            continue
        radar[pair]["ok"] = bool(a.get("ok"))
        for k in ("aspiration_side", "drop_bid_pct_per_s", "drop_ask_pct_per_s",
                  "max_drop_pct_per_s", "spread_bps", "spread_delta_bps",
                  "wall_bid_usdt", "wall_ask_usdt", "notional_drop_ok",
                  "price_delta_pct", "delay_s"):
            radar[pair][k] = a.get(k)

    LIVE_DATA = {
        "ts": int(time.time()),
        "ts_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "frais": True,
        "btc_price": btc,
        "gex": gex_local(),
        "n_actives": len(actives),
        "paires": radar,
        "source": "satellite_aspiration",
        "sat_ok": True,
    }
    try:
        atomic_write(LIVE, LIVE_DATA)
        print(f"[sat-asp] ts={LIVE_DATA['ts']} actives={len(actives)} "
              f"écrites->{LIVE.name} btc={btc:.0f}")
    except Exception as e:
        print(f"[sat-asp] WRITE_ERR {e}")
        return 1
    return 0


def main() -> int:
    if "--once" in sys.argv:
        return run_once()
    while True:
        try:
            run_once()
        except Exception as e:
            print(f"[sat-asp] ERR {e}")
        time.sleep(LOOP_SEC)
    return 0


if __name__ == "__main__":
    sys.exit(main())