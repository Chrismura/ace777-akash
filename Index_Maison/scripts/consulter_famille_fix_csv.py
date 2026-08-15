#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulter la FAMILLE sur le correctif CSV (durée de détention manquante).

Changement proposé au genesis scellé (8d9ee8d6) → validation famille/juge avant
toute implémentation (le code partira au codeur, pas au superviseur)."""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_FIX_CSV_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — VALIDER UN CORRECTIF DE TRACAGE

=== LE SYSTÈME ===
ACE777 est un moteur de trading BTC (testnet) en duo SCOUT(BETA x5)/HUNTER(ALPHA x13).
Le genesis (genesis_manifest.txt, scellé md5 8d9ee8d6) écrit un CSV de trades qui
EST le fichier de vérité (scellé sha256+md5, chmod 444, analysé en post-mortem).

=== LE BUG TROUVÉ (preuve code) ===
- En-tête CSV (ligne 393) : ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg  → 12 colonnes
- Ligne FILLED (ligne 2507) : echo "...FILLED,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,radar=... conf=... size_note=... soft=... pct=... tension=... bid_drop=... ask_drop=..." → 11 champs seulement
- Conséquence : la colonne 11 (holdSec, censée contenir la DURÉE de détention en secondes)
  contient en réalité le message de diagnostic ; la colonne 12 (msg) n'est JAMAIS écrite ;
  la durée $hold_done (calculée ligne 2490, affichée au terminal ligne 2516 "hold=7s sec=7")
  n'est PAS dans le CSV scellé. Le fichier de vérité est donc aveugle à la durée.
- Les autres lignes (SKIP, OBSERVE, ENTRY_ERROR) écrivent aussi 11 champs avec un message en 11e
  (mais elles n'ont pas de durée : ce sont des non-trades).

=== LE CORRECTIF PROPOSÉ (1 ligne, logging-only) ===
Ligne 2507, AVANT :
  echo "...FILLED,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,radar=... size_note=... ..." >> "$LOG_FILE"
Ligne 2507, APRÈS (insérer $hold_done en 11e, déplacer le message en 12e) :
  echo "...FILLED,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,$hold_done,radar=... size_note=... ..." >> "$LOG_FILE"

Résultat : la ligne FILLED passe à 12 colonnes (durée dans holdSec, message dans msg),
conforme à l'en-tête. Aucun impact sur la logique de trading (c'est l'écriture CSV).

=== CONTRAINTES ===
- Le genesis est scellé : toute modification impose re-scellement (nouveau md5) + test.
- Consommateurs du CSV existants : scripts/verifier_test.sh (compte lignes + pnl_total),
  cockpit, scripts d'analyse (qui coupent les colonnes par position).

=== QUESTIONS ===
1) Le correctif est-il un changement de traçage pur (aucun impact sur le chemin de trading) ?
2) Risque-t-il de casser un consommateur du CSV (sceller, cockpit, analyse) qui attendrait
   11 champs sur les lignes FILLED ? Si oui, lesquels et comment les protéger ?
3) Faut-il corriger AUSSI les autres types de lignes (SKIP/OBSERVE/ENTRY_ERROR) pour qu'elles
   passent à 12 colonnes (message dans msg, holdSec vide), ou ne corriger QUE les lignes FILLED ?
4) Un correctif logging-only justifie-t-il un run de validation testnet court, ou un simple
   smoke (quelques cycles + vérif du CSV) suffit-il avant re-scellement ?

Répondez factuellement et concis (pas de roman)."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 1200, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for m in MODELS:
        try:
            content, provider, secs = ask(m)
            f = os.path.join(OUT, f"AVIS_{m}.md")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
            print(f"[OK] {m} ({secs}s)")
        except Exception as e:
            print(f"[ERR] {m}: {e}")
        time.sleep(2)


if __name__ == "__main__":
    main()
