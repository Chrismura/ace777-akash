#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation CODEUR — HULK : SONDE ASPIRATION (double lecture carnet) — 16/08/2026.

Protocole maison : code EXACT injecté, avis factuel, ne touche à rien.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_CODEUR_SONDE_ASPIRATION_20260816")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CLAUSE PERMANENTE (Christophe, 16/08 — applicable à TOUS les prompts) :
Ne te contente PAS de corriger ou de valider. Si tu proposes AUTRE CHOSE (approche différente,
autre architecture, autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement.
Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait que « c'est bon »
ou « corrige X » est incomplète.

CONTEXTE (superviseur Buffy, 16/08/2026) — CONSULTATION CODEUR : sonde aspiration HULK

=== LE SYSTÈME ===
HULK = paper trading dip&rip sur MEXC spot (~15 paires small caps, watchlist CMC « The Hulk
Portfolio Picks »). Mise 20$/trade, stop ~6%, RIP scale-out 2 paliers (XRP/HBAR 2%/6%, small caps
6%/8%, 25% par palier), cible 2× → bag maison, kill-switch veille, contrat Cortana ADVISORY.
Le moteur importe déjà scripts/ace_sense_mexc.py : book_sense() (1 lecture du carnet : spread,
profondeur, imbalance, murs wall_bid_usdt/wall_ask_usdt, best_bid/ask) + tension_score() +
entry_gate() (refuse si spread large / carnet mince / mur ask écrasant / tension faible).
Config : SENSE_ON=1, SENSE_MAX_SPREAD_BPS=80, SENSE_MIN_DEPTH_USDT=80, SENSE_MIN_TENSION=1.2,
SENSE_MAX_ASK_WALL_RATIO=8.

=== LA DEMANDE (Christophe, 16/08) ===
« Je veux qu'il sonde comme ACE : voir les murs de liquidité, l'aspiration, l'historique qui fait
parti pris — l'intelligence si c'est possible. »
ACE (genesis) fait une DOUBLE lecture du carnet à quelques instants d'écart, calcule la chute de
chaque mur (wall_drop_bid_pct / wall_drop_ask_pct), et en déduit aspiration_side (BUY si le mur
ask fond → prix aspiré vers le haut ; SELL si le mur bid fond), + percussion (si la chute dépasse
un seuil → signal fort) + tension boostée. HULK ne fait aujourd'hui QU'UNE SEULE lecture → il voit
les murs mais PAS leur mouvement.

=== LA SPEC PROPOSÉE (à évaluer, code EXACT) ===
1. Nouvelle fonction dans ace_sense_mexc.py (fail-open) :
     def aspiration_sense(pair, http_json, delay_s=1.0):
         # lecture 1 (book_sense existant) ; si KO → return sens1 seul, aspiration=None
         sens1 = book_sense(pair, http_json)
         if not sens1.get("ok"):
             return sens1, None
         time.sleep(delay_s)
         try:
             sens2 = book_sense(pair, http_json)
         except Exception:
             return sens1, None          # fail-open : pas de 2e lecture → pas d'aspiration
         if not sens2.get("ok"):
             return sens1, None
         # chute de mur entre les 2 lectures (ACE : depth_wall_masses + wall_drop_pct)
         def wall_drop(m1, m2):
             if m1 <= 0: return 0.0
             return (m1 - m2) / m1 * 100.0
         drop_bid = wall_drop(sens1["wall_bid_usdt"], sens2["wall_bid_usdt"])
         drop_ask = wall_drop(sens1["wall_ask_usdt"], sens2["wall_ask_usdt"])
         side = "SELL" if drop_bid >= drop_ask else "BUY"
         return sens2, {"drop_bid_pct": round(drop_bid,2), "drop_ask_pct": round(drop_ask,2),
                        "side": side, "max_drop_pct": round(max(drop_bid, drop_ask),2)}
   Config : ASPIRATION_ON=1, ASPIRATION_DELAY_S=1.0, ASPIRATION_WALL_DROP_PCT=15.0 (seuil
   « percussion » : si max_drop_pct >= seuil → aspiration forte).
2. Intégration dans sense_ok() du moteur (appelé à chaque buy potentiel) : si ASPIRATION_ON,
   faire aspiration_sense() à la place de book_sense(), stocker le dict dans sc["aspiration"].
   Dans entry_gate() : si aspiration forte (max_drop_pct >= seuil) → tension = max(tension,
   tension + bonus) ; si side=BUY (aspiration haussière) → favorise l'entrée ; si side=SELL et
   tension faible → refuse (« mur bid fond = vent dominant »).
3. Sortie (bonus, non bloquant) : le radar affiche drop_bid/drop_ask/side par paire.

=== VOS 5 QUESTIONS ===
1. La double lecture à ~1 s est-elle fiable/pertinente sur small caps MEXC (carnet qui bouge vite,
   timeouts fréquents) ? Délai optimal (0.5s/1s/2s) ?
2. ASPIRATION_WALL_DROP_PCT=15 % comme seuil de « percussion » : raisonnable ? (ACE utilise
   IMPULSE_RESONANCE_WALL_DROP_PCT — contexte différent, futures BTC.)
3. Fail-open si la 2e lecture échoue (on garde la lecture simple) : bon choix, ou fail-closed ?
4. L'aspiration doit-elle servir à l'ENTRÉE seulement, ou aussi à la SORTIE (sortie anticipée si le
   mur bid fond sur une position ouverte) ? (Le moteur ne gère pas ça aujourd'hui.)
5. Coût API : +1 lecture carnet par paire par cycle (15 paires × 20s). Acceptable, ou limiter
   l'aspiration aux paires en régime COOLING/IMPULSE (prêtes à trader) ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur « implémenter la spec ci-dessus », réserve précisée)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3 hypothèses
  CE QUI CHANGERAIT L'AVIS : le(s) fait(s) qui ferait/faisaient basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)

SYNTHÈSE (5 lignes max) : diagnostic le plus probable + ordre des actions.

Factuel, concis, français. Si une info manque : « information insuffisante ». Vous DONNEZ UN AVIS :
ne touchez à rien, n'écrivez aucun code."""

MODELS = ["gemini", "nvidia", "deepseek-ai/deepseek-v4-flash-0731", "codestral-latest"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2400, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for m in MODELS:
        for attempt in (1, 2):
            try:
                content, provider, secs = ask(m)
                name = m.split("/")[-1].split(":")[0]
                with open(os.path.join(OUT, f"AVIS_{name}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
                print(f"[OK] {m} ({secs}s)")
                break
            except Exception as e:
                print(f"[ERR] {m} (tentative {attempt}): {e}")
                time.sleep(3)
        time.sleep(2)


if __name__ == "__main__":
    main()
