#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulter la FAMILLE sur le diagnostic MOTEUR (revenge + shock_stop + tension stale) — 15/08/2026.

Protocole §C : #9 Multi-Perspective + #5 Confidence-Weighted (verdict + confiance 0-100 %
+ hypothèses + ce qui changerait l'avis) + AMÉLIORATIONS (stacking functions).
Lecture seule : la famille DONNE UN AVIS, ne touche à rien.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_MOTEUR_REVENGE_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — DIAGNOSTIC MOTEUR ACE777 (analyse seule, zéro code)

=== LE SYSTÈME ===
ACE777 = duo scalper sur Binance testnet : BETA (scout, ouvre) + ALPHA (hunter, amplifie).
Le « revenge » est un mécanisme du genesis : quand BETA ferme une PERTE (stop_loss /
shock_inversion_stop / shock_exit_10bps / fluid_exit_* / beta_sentinel_cut), ALPHA ré-entre
immédiatement en mode « revenge » à ~1.5x pour récupérer la perte. (code : revenge = role==SCOUT
&& closed_loss && revenge_reasons.include?(reason) → out_mult=revenge_mult).
Contrainte : champion genesis intouchable · jamais de LLM dans la boucle d'ordre · GO humain
obligatoire avant tout changement · 8 Go · vérité = CSV/fichiers.

=== CHIFFRES RÉELS (extraits des CSV scellés, ALPHA uniquement) ===
| jour | fills | revenge | %revenge | %shock_stop | PnL revenge (n) | PnL normal (n) |
| 08-12 | 28 | 20 | 71.4% | 67.9% | -1.30 (20) | -0.49 (8) |
| 08-13 | 62 | 36 | 58.1% | 72.6% | -3.60 (36) | +4.62 (26) |
| 08-14 | 151 | 103 | 68.2% | 84.1% | +51.14 (103) | +7.40 (48) |
| 08-15 | 81 | 72 | 88.9% | 79.0% | +0.93 (72) | -0.84 (9) |
Constat : le %revenge MONTE (58→89%) ; ~68-84% des exits = shock_inversion_stop ;
le PnL revenge est TRÈS volatil (+51 le 14, -3.6 le 13, +0.9 le 15).

=== AUTRE SIGNAL (run du 15/08 12:45-14:47) ===
- E-STALE : 0 (tous les jours précédents) → 1032 aujourd'hui = `tension_stale age>800ms (NUAGE)`
  = le feed de tension lag de 8-12s (latence réseau/alpage, gate 800ms) → le bot SKIP.
- E-PROC : 4 → 75 (morts de process).
- Marché férié (15/08) → tension moyenne la plus basse des 4 jours (0.13/0.23 vs 0.19-0.45).

=== VOTRE MISSION (format EXACT exigé) ===
Analysez sous 3 angles :
  • Technique : le couple « shock_inversion_stop (~80%) → revenge 1.5x » forme-t-il une boucle
    (scout stoppé → hunter revanche → stoppé → revanche) = churn/frais sans edge, ou est-ce
    une vraie stratégie ? Le revenge est-il net positif ou net négatif (chiffres mitigés) ?
  • Risque/Impact : que faudrait-il mesurer en plus pour trancher (ex. PnL par séquence
    scout+hunter, frais cumulés, hold moyen revenge vs normal) ?
  • Priorité : E-STALE 1032 + E-PROC 75 (infra/feed) sont-ils à corriger AVANT le revenge ?

Puis donnez :
  VERDICT : (sur « faut-il ouvrir un chantier correctif moteur, et lequel en premier »)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3 hypothèses sous-jacentes
  CE QUI CHANGERAIT L'AVIS : le(s) fait(s) qui ferait/faisaient basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)

SYNTHÈSE (5 lignes max) : diagnostic le plus probable + ordre des actions recommandé.

Factuel, concis, en français. Si une info manque, dites « information insuffisante ».
Vous DONNEZ UN AVIS : ne touchez à rien, n'écrivez aucun code."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


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
        try:
            content, provider, secs = ask(m)
            with open(os.path.join(OUT, f"AVIS_{m}.md"), "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
            print(f"[OK] {m} ({secs}s)")
        except Exception as e:
            print(f"[ERR] {m}: {e}")
        time.sleep(2)


if __name__ == "__main__":
    main()
