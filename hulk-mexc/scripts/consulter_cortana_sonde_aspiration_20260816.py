#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation CORTANA — HULK : sonde inspiration ACE (bassine / verre d'eau / vortex) — 16/08/2026.

Task officiel cortana.analyse via le hub (gemini principal + nemotron-ultra + nvidia).
ADVISORY : Cortana propose, ne touche à rien.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_CORTANA_SONDE_ASPIRATION_20260816")
os.makedirs(OUT, exist_ok=True)

SYSTEM = (
    "Tu es CORTANA, l'analyste-maîtresse de la famille ACE777 (contrat : ADVISORY — "
    "tu PROPOSES, tu n'appliques JAMAIS rien ; mode appliqué seulement si justesse ≥60%). "
    "Tu connais l'inspiration ACE (pattern V8 : bassine, verre d'eau, vortex) et le moteur "
    "HULK (paper dip&rip MEXC small caps). Avis franc, chiffré, GO-sized."
)

# CLAUSE PERMANENTE (gravée 16/08 par Christophe — applicable à TOUS les prompts).
CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

CONTEXTE = """\
SONDE HULK INSPIRÉE ACE — avis de Cortana (16/08/2026 soir)

================
L'INSPIRATION ACE (les métaphores de Christophe)
================
- LA BASSINE : le bassin de liquidité du carnet (les murs bid/ask). Un bassin profond =
  le marché peut exécuter. Un bassin qui se vide = danger ou opportunité.
- LE VERRE D'EAU : le vide attire le liquide. Un mur qui fond (vide créé) attire le prix
  vers lui : aspiration BUY si le mur ask fond (le prix est aspiré vers le haut), SELL si
  le mur bid fond. C'est LA métaphore de l'aspiration.
- LE VORTEX : le régime / la rotation du marché (chop vs trend), la tension qui s'accumule
  puis se libère. ACE le pilote via vortex_supervisor (radar chop 0.85 / trend 0.618).

Pattern V8 d'ACE : RADAR → FENÊTRE → MUR → ASPIRATION/SKIP.
- radar : régime (confiance, direction)
- fenêtre : le moment (dt_ms=128, double lecture)
- mur : wall_drop_bid/ask_pct entre 2 lectures
- aspiration : direction (BUY/SELL) + mass mult 1.618 si angle fort
- void_lock / shock_exit : garde-fous de sortie

================
HULK AUJOURD'HUI
================
HULK (paper MEXC) lit le carnet 1× par cycle (ace_sense_mexc.py : spread, profondeur,
imbalance, murs wall_bid/ask, tension). Il VOIT les murs mais PAS leur mouvement.
Codeur (4 avis) + famille (6 avis) : GO-AVEC-RÉSERVES pour ajouter la double lecture
(aspiration : drop_bid/drop_ask/side), en MODE OBSERVATION 48h d'abord (aucun effet sur
les entrées), fail-open, limité aux paires actives, avec 3 corrections :
1. drop normalisé par le temps réel (drop_pct/sec — insensible au jitter réseau)
2. volume absolu minimum (mur > 500$ notional — sinon c'est un ordre qui se retire)
3. croiser avec le spread (mur fond + spread resserré = vraie aspiration ; spread élargi =
   retrait = ignorer) — logger spread_delta
Puis calibration du seuil sur données réelles, activation seulement si justesse >60%.

================
TA MISSION (3 coups une pierre)
================
1. VERDICT sur le plan (double lecture inspiration ACE, mode observation 48h, 3 corrections) :
   GO / GO AVEC RESERVES / NON + raison courte et nette.
2. Est-ce que la métaphore « verre d'eau » (vide attire le liquide) se transpose bien à
   l'aspiration sur small caps MEXC ? Ou y a-t-il une limite (ex. carnets trop minces,
   spoofing) qui invalide la métaphore à cette échelle ?
3. UNE amélioration concrète GO-sized pour la sonde Hulk (pas cosmétique).
Réponds en français, court et net, sans blabla. Tu es ADVISORY : tu ne modifies rien.
"""


def main():
    payload = {
        "task": "cortana.analyse",
        "messages": [
            {"role": "system", "content": SYSTEM + "\n\n" + CLAUSE},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1500,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    content = d["choices"][0]["message"]["content"].strip()
    provider = d.get("provider", "?")
    with open(os.path.join(OUT, "AVIS_CORTANA.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# AVIS CORTANA (provider {provider})\n\n{content}\n")
    print(f"[OK] CORTANA ({provider})")


if __name__ == "__main__":
    main()
