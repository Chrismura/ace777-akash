#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sandbox_replay.py — GO 24/10 @igus_ai (copie réaliste de prod, 0 ordre).
Copie les caches 45j vers thermo/sandbox_<ts>/ (copie, jamais le live),
rejoue en lecture seule : fraîcheur, trous, amplitude.
Sortie : thermo/sandbox_replay_<ts>.json (hors git, runtime).
IA=Buffy (Muse Spark 1.3, Freebuff). 0 ordre, 0 €, moteur intouchable.
"""
import json, shutil, sys
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CACHE = Path("/Users/christophe/ace777-test-day1/hulk-mexc/runs/replay_cache")
THERMO = RACINE / "thermo"

def analyser(p):
    try:
        kl = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        return {"ok": False, "erreur": str(e)}
    if not isinstance(kl, list) or not kl:
        return {"ok": False, "erreur": "vide"}
    closes = [float(b.get("c", 0)) for b in kl if b.get("c")]
    if not closes or min(closes) <= 0:
        return {"ok": False, "erreur": "closes invalides"}
    amp = (max(closes) - min(closes)) / min(closes) * 100.0
    # trous : sauts de timestamp > 2h
    ts = [int(b.get("t", 0)) for b in kl if b.get("t")]
    trous = sum(1 for a, b in zip(ts, ts[1:]) if b - a > 2 * 3600 * 1000)
    age_h = (datetime.now(timezone.utc).timestamp() * 1000 - ts[-1]) / 3600000.0 if ts else -1
    return {"ok": True, "n": len(kl), "amp_pct": round(amp, 2),
            "trous_2h": trous, "age_derniere_h": round(age_h, 1)}

def main():
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    dest = THERMO / f"sandbox_{ts}"
    dest.mkdir(parents=True, exist_ok=True)
    paires = sorted(CACHE.glob("*_1h_45j.json"))
    resume, details = [], {}
    for p in paires:
        try:
            shutil.copy2(p, dest / p.name)
        except Exception as e:
            details[p.stem] = {"ok": False, "erreur": f"copie: {e}"}
            continue
        r = analyser(dest / p.name)
        details[p.stem] = r
        resume.append((p.stem, r))
    ok = sum(1 for _, r in resume if r.get("ok"))
    out = {"ts": datetime.now(timezone.utc).isoformat(), "bac": str(dest),
           "n_caches": len(paires), "n_ok": ok,
           "copie": "replay_cache -> sandbox (live jamais touché)",
           "paires": details,
           "lecture": f"Bac réaliste prêt : {ok}/{len(paires)} caches rejouables, 0 ordre."}
    f = THERMO / f"sandbox_replay_{ts}.json"
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"-> {f} ({ok}/{len(paires)} OK, bac {dest.name})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
