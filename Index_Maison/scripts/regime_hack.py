#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""regime_hack.py — LE CONSOMMATEUR (03/11/2026, GO Christophe « go sur toute la ligne »).

Hier (02/11) la maison a mesuré un régime HACK_ACTIF et… personne ne le lisait :
`thermo/hack_actif.json` avait zéro consommateur, donc zéro effet. Ce module est
le branchement : il rend le plafond de mise RÉEL, à appeler avant tout fill.

Plafond = min( maxS2 du m-mètre , cap_trade_usd du régime hack ), chacun lu
seulement s'il est frais (preuve de vie). Ce module ne fait que RÉDUIRE :
il ne peut jamais augmenter une mise, ni créer un ordre (C3).

Fail-open EXPLICITE : organe absent/stale/illisible -> mise inchangée + raison
"SANS_MESURE" (R11 : pas de coupe aveugle), et le rituel doit crier dessus.
"""
import json
import os
import sys
import time
from datetime import datetime, timezone

ROOT = os.path.expanduser("~/ace777-test-day1")
THERMO = os.path.join(ROOT, "Index_Maison", "thermo")
M_KELLY = os.path.join(THERMO, "m_kelly_live.json")
HACK = os.path.join(THERMO, "hack_actif.json")
M_KELLY_MAX_H = 30.0
HACK_MAX_H = 2.0


def _frais(path, max_h):
    try:
        age_h = (time.time() - os.path.getmtime(path)) / 3600.0
        return age_h <= max_h, age_h
    except Exception:
        return False, None


def _lire(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def etat():
    """Photographie des deux organes (fraîcheur + valeurs). Jamais d'exception."""
    out = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "m_kelly": {"present": False}, "hack": {"present": False}}
    ok, age = _frais(M_KELLY, M_KELLY_MAX_H)
    mk = _lire(M_KELLY) if ok else None
    if mk:
        out["m_kelly"] = {"present": True, "age_h": round(age or 0, 2),
                          "maxS2": mk.get("maxS2"), "m_global": mk.get("m_global")}
    ok, age = _frais(HACK, HACK_MAX_H)
    hk = _lire(HACK) if ok else None
    if hk:
        out["hack"] = {"present": True, "age_h": round(age or 0, 2),
                       "niveau": hk.get("niveau"), "label": hk.get("label"),
                       "cap_trade_usd": hk.get("cap_trade_usd"),
                       "taille_multiplier": hk.get("taille_multiplier"),
                       "cash_reel_usd": hk.get("cash_reel_usd"),
                       "cash_cible_usd": hk.get("cash_reserve_usd"),
                       "cash_ecart_usd": hk.get("cash_ecart_usd")}
    return out


def plafond(taille):
    """Retourne {'taille', 'bride', 'raison', 'sources'} — ne hausse jamais."""
    try:
        taille = float(taille)
    except Exception:
        return {"taille": taille, "bride": False, "raison": "taille illisible",
                "sources": {}}
    caps, sources = [], {}
    e = etat()
    mk = e["m_kelly"]
    if mk.get("present") and mk.get("maxS2"):
        caps.append(float(mk["maxS2"]))
        sources["maxS2"] = float(mk["maxS2"])
    hk = e["hack"]
    if hk.get("present") and hk.get("cap_trade_usd"):
        caps.append(float(hk["cap_trade_usd"]))
        sources["hack_cap"] = float(hk["cap_trade_usd"])
        sources["niveau"] = hk.get("niveau")
    if not caps:
        return {"taille": taille, "bride": False,
                "raison": "SANS_MESURE (m_kelly/hack absents ou stale) — mise inchangée",
                "sources": sources}
    cap = min(caps)
    if cap <= 0:
        return {"taille": 0.0, "bride": True,
                "raison": "CAP NUL (niveau FORTRESSE ou edge nul) — pas de nouvelle mise",
                "sources": sources}
    if taille > cap:
        return {"taille": cap, "bride": True,
                "raison": "plafond %.2f$ (min de %s)" % (
                    cap, ", ".join("%s=%.2f" % (k, v) for k, v in sources.items()
                                   if isinstance(v, float))),
                "sources": sources}
    return {"taille": taille, "bride": False, "raison": "OK (sous plafond %.2f$)" % cap,
            "sources": sources}


if __name__ == "__main__":
    t = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0
    print(json.dumps(etat(), ensure_ascii=False, indent=1))
    print(json.dumps(plafond(t), ensure_ascii=False, indent=1))
