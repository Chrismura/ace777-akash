#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulter le CODEUR (code.ia) : spec graphique BTC + points entrees/sorties.
Prototype hors-cockpit deja fonctionnel (scripts/graph_trades_btc.py -> /tmp/*.html).
On demande au codeur : revue de la spec, meilleure logique, et plan d'integration cockpit."""
import json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_CODEUR_GRAPHIQUE_20260814")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 14/08/2026, run 4h testnet en cours, moteur corrige) :

OBJECTIF : voir les points d'entree et de sortie des trades du moteur ACE777 sur un
graphique du prix BTC. Le superviseur a deja fait un PROTOTYPE HORS-COCKPIT fonctionnel :
  - scripts/graph_trades_btc.py : lit le CSV des trades FILLED (ts, side BUY/SELL,
    entryPrice, exitPrice, qty, pnl, exitReason, msg), recupere les klines 1m du
    testnet (https://testnet.binancefuture.com/fapi/v1/klines), et genere un HTML
    100% autonome (canvas pur, zero dependance, stdlib uniquement).
  - Points verts = entree BUY (long), points rouges = entree SELL (short),
    croix jaunes = sortie, infobulle au survol (heure, direction, qty, entrees/sorties,
    pnl colorie, raison, message radar).
  - Generation : python3 scripts/graph_trades_btc.py --csv runs/<TAG>_ALPHA_X13_BURST13.csv
    --since 2026-08-14T16:24:00 --out /tmp/btc_trades_alpha.html
  - Teste et valide (JSON parse OK, 167 bougies / 24 trades ALPHA, 111 trades BETA).

DECISION HUMAINE : on n'integre au cockpit (http://127.0.0.1:17800/cockpit/index.html,
canvas deja presents : radar, synapses) QUE si le prototype s'avere vraiment utile.
Le cockpit est un fichier index.html de 4362 lignes + serveur HTTP local (17800)
+ pont cortana (17777). Le moteur tourne : NE RIEN casser, NE PAS toucher au run.

DEMANDE AU CODEUR :
1) Revuez le prototype (scripts/graph_trades_btc.py) : y a-t-il une meilleure logique
   ou une amelioration evidente (lisibilite, perfs, gestion CSV append-only enorme,
   erreurs API) ?
2) Pour l'integration cockpit si elle se fait : proposez le plan le plus propre et le
   MOINS intrusif (ex: un fichier cockpit/graph_trades.js + <canvas> ajoute dans un
   panneau existant, data servie par le pont ou generee par un petit script cote serveur)
   — sans rien modifier maintenant.
3) Repondez : AMELIORATIONS_PROTOTYPE (liste courte) + PLAN_INTEGRATION (etapes) +
   RISQUES (ce qui peut casser le cockpit ou le moteur) + votre recommandation :
   integrer maintenant / attendre validation humaine du prototype / ne pas integrer.
Contrainte : stdlib uniquement (pas de pandas/plotly), le moteur tourne, on ameliore
on ne degrade pas — prouvez la meilleure logique si vous en voyez une."""

MODELS = ["inferx-coder", "gemini", "oss20"]

def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 1600, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)

def main():
    results = {}
    for m in MODELS:
        try:
            content, provider, secs = ask(m)
            results[m] = content
            f = os.path.join(OUT, f"AVIS_{m}.md")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
            print(f"[OK] {m} -> {f} ({secs}s)")
        except Exception as e:
            print(f"[ERR] {m}: {e}")
        time.sleep(2)
    print("\n=== SYNTHESE ===")
    print(f"Consultation terminee : {len(results)}/{len(MODELS)} avis dans {OUT}")

if __name__ == "__main__":
    main()
