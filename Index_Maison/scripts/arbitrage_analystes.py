#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""arbitrage_analystes.py — C7 (07/08) : arbitrage multi-modèle.

Compare le dernier avis du master analyste (Gemini) et celui de Qwen (btc)
dans analyses/*.jsonl. Si divergence totale (LONG vs SHORT) → DÉSACCORD :
la confiance globale du brief est rétrogradée + badge « ⚠️ Désaccord analystes ».
Si accord ou abstention → pas de rétrogradation.

Usage :
  python3 arbitrage_analystes.py            # verdict texte pour le brief
  python3 arbitrage_analystes.py --json     # verdict JSON (cockpit)

Lecture seule — ne passe jamais d'ordre.
"""
import argparse
import json
import os
import re
import sys

ANALYSES_DIR = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/thermo/analyses")


def load_entries():
    if not os.path.isdir(ANALYSES_DIR):
        return []
    out = []
    try:
        files = sorted(f for f in os.listdir(ANALYSES_DIR) if f.endswith(".jsonl"))
    except OSError:
        return []
    for fn in files:
        try:
            with open(os.path.join(ANALYSES_DIR, fn)) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        e = json.loads(line)
                    except Exception:
                        continue
                    out.append(e)
        except OSError:
            continue
    return out


def parse_avis(analyse):
    txt = analyse.get("analyse", "") or ""
    m_av = re.search(r"AVIS\s*STRICT\s*:\s*(\w+)", txt, re.IGNORECASE)
    m_cf = re.search(r"CONFIANCE\s*:\s*(\w+)", txt, re.IGNORECASE)
    return {
        "avis": m_av.group(1).upper() if m_av else None,
        "confiance": m_cf.group(1).lower() if m_cf else None,
    }


def last_by_family(entries):
    """Dernière entrée par FAMILLE (robuste au fallback) :
    - voix du chief  = indice != 'btc'  (analyses funding/radar/fearGreed, Gemini)
    - voix de Qwen   = indice == 'btc'  (l'analyse BTC, même si servie par Gemini
      en fallback — on compare le CONTENU btc, pas le provider physique)."""
    gemini = qwen = None
    for e in entries:
        ts = e.get("ts", "")
        if not e.get("avis_ok"):
            continue
        if e.get("indice") == "btc":
            if qwen is None or ts > qwen["ts"]:
                qwen = {"ts": ts, "indice": "btc", **parse_avis(e)}
        else:
            if gemini is None or ts > gemini["ts"]:
                gemini = {"ts": ts, "indice": e.get("indice"), **parse_avis(e)}
    return gemini, qwen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    entries = load_entries()
    gemini, qwen = last_by_family(entries)

    if not gemini and not qwen:
        print("⚠️ Arbitrage : aucune analyse notée — bientôt deux voix à comparer.")
        return 0

    verdict = {
        "gemini": gemini,
        "qwen": qwen,
        "desaccord": False,
        "retrograde": False,
        "badge": None,
        "detail": "",
    }

    if gemini and qwen:
        g, q = gemini.get("avis"), qwen.get("avis")
        if g and q:
            if (g == "LONG" and q == "SHORT") or (g == "SHORT" and q == "LONG"):
                verdict["desaccord"] = True
                verdict["retrograde"] = True
                verdict["badge"] = "⚠️ DÉSACCORD ANALYSTES"
                verdict["detail"] = (f"Chief {g} vs Qwen {q} — les deux voix se "
                                     "contredisent : CONFIANCE GLOBALE : BASSE.")
            elif g == "NEUTRE" or q == "NEUTRE":
                verdict["badge"] = "ℹ️ Accord partiel (abstention)"
                verdict["detail"] = f"Chief {g} · Qwen {q} — au moins un des deux est neutre."
            else:
                verdict["badge"] = "✅ Accord"
                verdict["detail"] = f"Chief {g} et Qwen {q} dans le même sens."
        else:
            verdict["badge"] = "⚠️ Avis illisible"
            verdict["detail"] = (f"Les deux analystes ont parlé mais un avis est illisible "
                                 f"(chief : {g or '-'} · Qwen : {q or '-'}).")
    else:
        if gemini:
            verdict["detail"] = f"Seul le chief a parlé (Gemini : {gemini['avis'] or 'sans avis'})."
        elif qwen:
            verdict["detail"] = f"Seul Qwen a parlé (Qwen : {qwen['avis'] or 'sans avis'})."

    if a.json:
        print(json.dumps(verdict, ensure_ascii=False, indent=2))
        return 0

    print(f"🤖 Arbitrage des analystes ({len(entries)} analyses)")
    if gemini:
        g = gemini["avis"] or "-"
        print(f"  • Chief (Gemini) : {g} (confiance {gemini['confiance'] or '?'}) "
              f"— {gemini['ts'][:16]}")
    if qwen:
        q = qwen["avis"] or "-"
        print(f"  • Qwen (btc)     : {q} (confiance {qwen['confiance'] or '?'}) "
              f"— {qwen['ts'][:16]}")
    print()
    print(verdict["badge"] or "—")
    print(verdict["detail"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
