#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verdicteur_micro.py — BOUCLE VERDICT 5s/60s (09/09/2026, GO Christophe prop.2).

Le vrai accélérateur d'apprentissage de Cortana : chaque alerte micro
(data/micro_alerts.jsonl) est confrontée au RÉEL par un juge indépendant
(prix MEXC public, jamais l'instrument qui a alerté) :

  - à ~5 s  : verdict_5s  — le prix a-t-il bougé dans le sens annoncé ?
  - à ~60 s : verdict_60s — CONFIRMÉE si |Δ| ≥ 2 bps dans le sens annoncé
    (règle du module : le retournement se confirme, il ne se prédit pas).

Score de justesse micro → data/cortana_micro_score.json
(< 60 % → CONFIANCE faible obligatoire + 1 alerte/h max, module cortana_microstructure).
Stdlib + price_source.py local · idempotent · fail-open · plist com.ace777.verdicteur.
"""
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from price_source import prix_btc

INDEX = os.path.expanduser("~/ace777-test-day1/Index_Maison")
DATA = os.path.join(INDEX, "data")
ALERTS = os.path.join(DATA, "micro_alerts.jsonl")
SCORE = os.path.join(DATA, "cortana_micro_score.json")
HIST = os.path.join(DATA, "verdicteur_historique.jsonl")

SEUIL_CONF_BPS = 2.0
GRACE_S = 2  # tolérance sur les échéances (pas de verdict en avance notable)


def _age_s(ts_iso):
    try:
        t = datetime.fromisoformat(ts_iso.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - t).total_seconds()
    except Exception:
        return None


def main():
    now = datetime.now(timezone.utc)
    px, src = prix_btc()
    if not px:
        print("[verdicteur] pas de prix — passage neutre")
        return 0

    alertes = []
    if os.path.exists(ALERTS):
        with open(ALERTS, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        alertes.append(json.loads(line))
                    except Exception:
                        continue

    changed = False
    for a in alertes:
        if a.get("verdict_60s"):
            continue
        age = _age_s(a.get("ts", ""))
        if age is None:
            continue
        side = (a.get("side") or "").upper()
        if side not in ("LONG", "SHORT") or not a.get("ref_price"):
            a["verdict_60s"] = {"ts": now.isoformat(), "confirmee": False,
                                "detail": "alerte mal formée (side/ref_price manquants)"}
            changed = True
            continue
        sens = 1.0 if side == "LONG" else -1.0
        d_bps = (px - float(a["ref_price"])) / float(a["ref_price"]) * 1e4 * sens
        if a.get("verdict_5s") is None and age >= 5 - GRACE_S:
            a["verdict_5s"] = {"ts": now.isoformat(), "d_bps": round(d_bps, 2),
                               "sens_ok": d_bps > 0}
            changed = True
        if age >= 60 - GRACE_S:
            a["verdict_60s"] = {"ts": now.isoformat(), "d_bps": round(d_bps, 2),
                                "confirmee": d_bps >= SEUIL_CONF_BPS,
                                "seuil_bps": SEUIL_CONF_BPS}
            changed = True

    if changed:
        with open(ALERTS, "w", encoding="utf-8") as f:
            for a in alertes:
                f.write(json.dumps(a, ensure_ascii=False) + "\n")
        with open(HIST, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": now.isoformat(), "prix": px, "source": src,
                                "n_maj": sum(1 for a in alertes if a.get("verdict_60s"))},
                               ensure_ascii=False) + "\n")

    # score de justesse micro
    v60 = [a for a in alertes if a.get("verdict_60s")]
    conf = sum(1 for a in v60 if a.get("verdict_60s", {}).get("confirmee"))
    score = {
        "ts": now.isoformat(),
        "n_alertes": len(alertes),
        "n_scorées_60s": len(v60),
        "n_confirmees": conf,
        "pct": round(100.0 * conf / len(v60), 1) if v60 else None,
        "regle": "<60% → CONFIANCE faible + 1 alerte/h max (module cortana_microstructure)",
    }
    with open(SCORE, "w", encoding="utf-8") as f:
        json.dump(score, f, ensure_ascii=False, indent=1)

    print(f"[verdicteur] prix {px} ({src}) | alertes {len(alertes)} | "
          f"scorées 60s {len(v60)} | confirmées {conf} "
          f"({score['pct'] if score['pct'] is not None else '—'} %)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
