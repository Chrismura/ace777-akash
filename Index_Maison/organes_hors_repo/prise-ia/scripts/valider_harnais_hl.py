#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valide le harnais hyperliquid-compare/hl_compare.py auprès du CODEUR (code.ia).
Écrit la réponse dans Index_Maison/REPONSE_CODEUR_HARNAIS_HL_2026-08-22.md"""
import json, os, sys, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
HARNAIS = os.path.expanduser("~/ace777-test-day1/hyperliquid-compare/hl_compare.py")
OUT = os.path.expanduser("~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_HARNAIS_HL_2026-08-22.md")

code = open(HARNAIS).read()

SYSTEM = "Tu es le codeur senior du projet ACE777. Code propre, stdlib, robuste, vérification rigoureuse."

PROMPT = f"""Tu dois VALIDER un harnais de comparaison Hyperliquid testnet.

=== CONTEXTE ===
- ACE777 (champion scellé 37fca367) tourne sur Binance Futures testnet en bash.
- On veut comparer frais/partial fills/PnL entre Binance et Hyperliquid testnet.
- Pour ça, on a écrit un harnais Python qui réplique la MÊME logique ACE :
  * momentum = prix p1 → sleep 1s → prix p2 → bps_change(p1,p2)
  * radar gates (RADAR_MIN_CONF 0.30, RADAR_MIN_MOM_BPS 0.01, RADAR_DIR_BPS 0.20, RADAR_MAX_SPREAD_BPS 8)
  * entrée TAKER (BUY_USDT 500, levier 5)
  * sortie : stop_loss 10 bps, take_profit 15 bps net, trailing arm 5/giveback 3, max_hold 150s
  * log CSV identique au format ACE (ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,feeUsdt,pnlNet,exitReason,holdSec,msg)
- SDK : hyperliquid-python-sdk (testnet https://api.hyperliquid-testnet.xyz), eth_account.

=== LE CODE DU HARNAIS ===
```python
{code}
```

=== TA MISSION ===
1. Vérifie que la logique décisionnelle réplique FIDÈLEMENT ACE (momentum p1→p2, radar, trailing).
2. Repère les bugs / risques / imprécisions (calcul PnL short, frais, slippage, boucle d'exit).
3. Vérifie la sécurité : jamais d'ordre hors testnet, clé privée jamais commitée, STOP file.
4. Réponds en 3 sections :
   a) VERDICT : harnais sain / à corriger (1 phrase).
   b) BUGS : chaque bug avec ligne + correctif exact (bloc python).
   c) AMÉLIORATIONS : max 5, priorisées, qui n'altèrent PAS la fidélité à ACE.
5. RÈGLES : stdlib/python3.9 (pas de dépendances lourdes), français, factuel, concis."""

payload = json.dumps({
    "model": "code.ia",
    "task": "code.ia",
    "messages": [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": PROMPT},
    ],
    "temperature": 0.2,
    "max_tokens": 6000,
}).encode()

req = urllib.request.Request(HUB, data=payload,
                             headers={"Content-Type": "application/json"}, method="POST")
print("[code.ia] Envoi du harnais pour validation...", flush=True)
t0 = time.time()
with urllib.request.urlopen(req, timeout=420) as resp:
    d = json.loads(resp.read().decode())
content = d["choices"][0]["message"]["content"]
dur = round(time.time() - t0, 1)
prov = d.get("provider", "?")

with open(OUT, "w", encoding="utf-8") as f:
    f.write(f"# Réponse CODEUR — validation harnais Hyperliquid ({prov}, {dur}s)\n\n{content}\n")
print(f"[OK] Répondu via {prov} ({dur}s) -> {OUT}", flush=True)
print("=" * 60)
print(content)
print("=" * 60)
