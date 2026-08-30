#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ask_cortana_amplitude.py — demande à CORTANA une analyse profonde sur
l'amplitude (move24) des cryptos du portefeuille, avec les données réelles
archivées dans les *_state.json, puis transcrit sa réponse.

Usage:
  python3 ask_cortana_amplitude.py
"""
import json
import os
import sys
import urllib.request
from datetime import datetime

SCRIPTS = os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.expanduser("~/ace777-test-day1/hulk-mexc/runs")


def load_system_prompt():
    for p in (
        os.path.join(SCRIPTS, "prompts", "PROMPT_MASTER_ANALYSTE.md"),
        os.path.expanduser("~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md"),
    ):
        if os.path.exists(p):
            try:
                return open(p, encoding="utf-8").read()
            except Exception:
                pass
    return "Tu es Cortana, master analyste crypto du cockpit ACE777."


def build_facts():
    import glob
    series = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "*_state.json")), key=os.path.getmtime):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        ts = d.get("ts") or os.path.getmtime(f)
        try:
            t = datetime.fromisoformat(str(ts).replace("Z", "+00:00")).replace(tzinfo=None)
        except Exception:
            t = datetime.fromtimestamp(ts)
        for pair, v in (d.get("scores") or {}).items():
            m = (v or {}).get("move24_pct")
            if m is None:
                continue
            series.setdefault(pair, []).append((t.isoformat(), m))
    # résumé par paire
    per_pair = []
    for pair, pts in sorted(series.items()):
        vals = [p[1] for p in pts]
        if len(vals) < 10:
            continue
        avg = sum(vals) / len(vals)
        mx = max(vals)
        med = sorted(vals)[len(vals) // 2]
        below = round(100 * sum(1 for v in vals if v < avg) / len(vals))
        per_pair.append({
            "crypto": pair.replace("USDT", ""),
            "n_snapshots": len(vals),
            "amplitude_avg": round(avg, 1),
            "amplitude_med": round(med, 1),
            "amplitude_max": round(mx, 1),
            "ratio_max_avg": round(mx / avg, 2) if avg else 0,
            "pct_temps_sous_moyenne": below,
        })
    return per_pair


def call_cortana(facts):
    system = load_system_prompt()
    q = (
        "ANALYSE PROFONDE demandée par Christophe : nous étudions l'AMPLITUDE "
        "(move24 = range haut-bas sur 24h, en %) de chaque crypto du portefeuille "
        "paper HULK sur MEXC, archivée dans ~92 snapshots du 22/07 au 29/08/2026.\n\n"
        "Voici les données réelles (moyenne / médiane / max / ratio max/avg / "
        "% du temps sous la moyenne) par crypto :\n"
        + json.dumps(facts, ensure_ascii=False, indent=1)
        + "\n\nQuestion : 1) Vois-tu un PATRON exploitable pour le DCA / la "
        "gestion de portefeuille ? 2) Le ratio max/avg élevé (XRP 5.6, QAIT 4.2, "
        "HBAR 4.4) et le % de temps sous la moyenne (54-78%) suggèrent-ils un "
        "régime dormance->pic ? Comment l'exploiter ? 3) Quel serait le meilleur "
        "indicateur dérivé de l'amplitude pour déclencher accumulation (creux) "
        "vs protection (pic) ? Donne ta structure : FAITS, LECTURE PHYSIQUE, "
        "INTERPRÉTATION, MISE EN RELATION, PATTERN, OPINION."
    )
    payload = {
        "task": "cortana.analyse",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": q},
        ],
        "temperature": 0.4,
        "max_tokens": 1200,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.load(resp)
    content = data["choices"][0]["message"]["content"]
    return content, data.get("provider", "?")


def main():
    facts = build_facts()
    print("== Données envoyées à Cortana ==")
    for row in facts:
        print(f"  {row['crypto']:<7} n={row['n_snapshots']:>3} avg={row['amplitude_avg']:>5} "
              f"med={row['amplitude_med']:>5} max={row['amplitude_max']:>6} "
              f"max/avg={row['ratio_max_avg']:>4} sousMoy={row['pct_temps_sous_moyenne']}%")
    print("\n== Appel CORTANA (hub local)… ==")
    content, provider = call_cortana(facts)
    print(f"== Réponse CORTANA ({provider}) ==")
    print(content)


if __name__ == "__main__":
    main()
