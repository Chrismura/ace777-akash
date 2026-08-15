#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cortana propose des ajustements de paramètres Hulk → écrit strategie/cortana_pilot.json.

Lecture seule (Cortana ne passe aucun ordre). Utilisation :
  python3 cortana_propose_params.py
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HULK = Path(__file__).resolve().parents[1]
WS = Path(os.path.expanduser("~/ace777-test-day1/Index_Maison"))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
PILOT = HULK / "strategie" / "cortana_pilot.json"
JUSTESSE = WS / "scripts" / "justesse_cockpit.json"
IDENT = WS / "identity" / "prompts" / "cortana.md"

sys.path.insert(0, str(HULK / "scripts"))
from cortana_contract import BOUNDS, validate_proposals  # noqa: E402


def latest_state() -> str:
    try:
        states = sorted((HULK / "runs").glob("PAPER_V1_*_state.json"),
                        key=lambda p: p.stat().st_mtime, reverse=True)
        if not states:
            return "aucun state"
        st = json.load(open(states[0]))
        return (f"PnL={st.get('pnl_total')} $ · positions={len(st.get('positions') or {})} "
                f"· bags={len(st.get('bags') or {})}")
    except Exception:
        return "state indisponible"


def main() -> int:
    score = 0.0
    try:
        score = float(json.load(open(JUSTESSE)).get("pct") or 0) / 100.0
    except Exception:
        pass
    ident = open(IDENT, encoding="utf-8").read() if IDENT.exists() else ""
    user = (
        "Tu es le pilote de paramètres de Hulk (paper MEXC spot, dip&rip + bags). "
        f"État Hulk : {latest_state()}. Ton score de justesse : {score:.0%}. Ta discipline F1 : "
        "si ton score est < 60%, tu es prudente (confiance faible/moyenne, JAMAIS 'haute').\n"
        f"Propose au plus 3 ajustements de paramètres DANS le contrat, uniquement parmi : "
        f"{list(BOUNDS.keys())} (bornes : {BOUNDS}). Format EXACT JSON, rien d'autre :\n"
        '{"proposals": [{"param": "DIP_FLOOR_MULT", "param_class": "threshold_multiplier", '
        '"value": 0.9, "confidence": "faible|moyenne|haute", "reason": "...", '
        '"expiry": "2026-08-17T00:00:00Z"}]}\n'
        "Règle : ne propose que si TU as une raison fondée (données Hulk, régimes, cadences) ; "
        "sinon proposals vides. Tu n'exécutes rien."
    )
    payload = {
        "task": "cortana.analyse",
        "messages": [{"role": "system", "content": ident}, {"role": "user", "content": user}],
        "temperature": 0.3,
        "max_tokens": 700,
    }
    req = urllib.request.Request(HUB, data=json.dumps(payload).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=None) as r:
        d = json.loads(r.read().decode())
    raw = d["choices"][0]["message"]["content"].strip()
    start, end = raw.find("{"), raw.rfind("}")
    if start == -1 or end == -1:
        print("cortana: pas de JSON exploitable", file=sys.stderr)
        return 1
    try:
        data = json.loads(raw[start:end + 1])
        data.setdefault("proposals", [])
    except Exception as e:
        print(f"cortana: JSON invalide : {e}", file=sys.stderr)
        return 1
    valid, rejects = validate_proposals(data, score=score, mode="ADVISORY")
    out = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "cortana",
        "session_id": datetime.now(timezone.utc).strftime("%Y%m%d%H%M"),
        "cortana_accuracy_score": round(score, 3),
        "enforced_mode": "ADVISORY",
        "proposals": valid,
    }
    PILOT.parent.mkdir(parents=True, exist_ok=True)
    tmp = PILOT.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(PILOT)
    print(f"cortana: {len(valid)} proposition(s) → {PILOT}")
    for r in rejects:
        print(f"cortana REJET: {r}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
