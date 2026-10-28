#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cortana_fade_ombre.py — le point faible devient la piste (28/10/2026, §47).

Constat : analyste Cortana ~29 % de justesse (pilot 0.294, opérateur 135/463).
Discipline maison : on transforme en protocole MESURÉ, pas en avis.
- Si Cortana dit haussier et a tort 7 fois sur 10, le FADE (inverse) a raison
  7 fois sur 10 — À MESURER, jamais cru.
- 0 ORDRE, 0 effet live : on écrit runs/cortana_fade_ombre.jsonl uniquement.
- Chaque run : (1) lit cortana_analysis.json, extrait les appels DIRECTIONNELS
  (critique/dangereux = baissier, haussier = haussier, le reste = pas de matière) ;
  (2) note le prix BTC du moment ; (3) solde les appels vieux de 24 h+ en
  comparant au prix d'alors : fade gagnant si le marché a fait l'INVERSE.
Usage : python3 scripts/cortana_fade_ombre.py --once (launchd 1×/h si GO).
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
ANALYSIS = ROOT.parent / "Index_Maison" / "data" / "cortana_analysis.json"
SRC = RUNS / "croisement_contexte.jsonl"
JOURNAL = RUNS / "cortana_fade_ombre.jsonl"
HORIZON_H = 24.0

BEARISH = {"critique", "dangereux"}
BULLISH = {"haussier"}


def utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def prix_btc_now():
    try:
        best = None
        with open(SRC, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                if r.get("pair") != "BTCUSDT":
                    continue
                ts = r.get("ts") or 0
                if best is None or ts > best[0]:
                    best = (ts, float(r.get("price")))
        if best:
            return best[1]
    except Exception:
        pass
    try:
        live = json.loads((RUNS / "aspiration_live.json").read_text(encoding="utf-8"))
        p = float(live.get("btc_price") or 0)
        return p if p > 0 else None
    except Exception:
        return None


def appels_directionnels():
    """Retourne [(niveau, action)] directionnels, [] si pas de matière."""
    try:
        d = json.loads(ANALYSIS.read_text(encoding="utf-8"))
    except Exception:
        return []
    out = []
    for a in d.get("analyses", []) or []:
        niv = str((a.get("interpretation") or {}).get("niveau", "inconnu")).lower()
        if niv in BEARISH:
            out.append((niv, "baissier"))
        elif niv in BULLISH:
            out.append((niv, "haussier"))
    return out


def lire_journal():
    lignes = []
    if JOURNAL.exists():
        for line in JOURNAL.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                lignes.append(json.loads(line))
            except Exception:
                continue
    return lignes


def run_once() -> int:
    px = prix_btc_now()
    appels = appels_directionnels()
    now = time.time()
    log = lire_journal()
    # 1. solder les appels échus (24 h+, sans issue, avec prix maintenant)
    soldes = 0
    if px:
        for e in log:
            if e.get("type") == "appel" and e.get("issue") is None:
                try:
                    age_h = (now - float(e.get("epoch", now))) / 3600.0
                except Exception:
                    continue
                if age_h >= HORIZON_H:
                    sens = 1 if e.get("sens") == "haussier" else -1
                    move = (px - float(e.get("prix_btc", px))) / float(e.get("prix_btc", px)) * 100.0
                    # fade = inverse de l'appel : gagnant si marché contre l'appel
                    fade_gagnant = (move * sens) < 0
                    e["issue"] = {
                        "ts_solde": utc(),
                        "prix_btc_solde": px,
                        "move_24h_pct": round(move, 3),
                        "fade_gagnant": bool(fade_gagnant),
                    }
                    log.append({"type": "solde", "ts": utc(),
                                "sens": e.get("sens"), "niveau": e.get("niveau"),
                                "move_24h_pct": round(move, 3),
                                "fade_gagnant": bool(fade_gagnant)})
                    soldes += 1
    # 2. enregistrer les appels du moment
    nouveaux = 0
    if px and appels:
        for niv, sens in appels:
            log.append({"type": "appel", "ts": utc(), "epoch": now,
                        "niveau": niv, "sens": sens, "prix_btc": px,
                        "issue": None})
            nouveaux += 1
    JOURNAL.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in log) + "\n",
                       encoding="utf-8")
    # 3. bilan fade
    soldes_l = [e for e in log if e.get("type") == "solde"]
    win = sum(1 for e in soldes_l if e.get("fade_gagnant"))
    print(f"[FADE-OMBRE] prix_btc={px} appels_maintenant={len(appels)} "
          f"nouveaux={nouveaux} soldes_ce_run={soldes} "
          f"historique={len(soldes_l)} win_fade={win} "
          f"({'PAS DE MATIÈRE' if not soldes_l and not appels else 'en accumulation, 0 ordre'})")
    return 0


if __name__ == "__main__":
    sys.exit(run_once())
