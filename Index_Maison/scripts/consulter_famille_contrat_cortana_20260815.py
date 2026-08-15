#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — contrat JSON Cortana↔moteur Hulk (pilote de paramètres)."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_CONTRAT_CORTANA_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — CONTRAT JSON CORTANA ↔ MOTEUR HULK

=== LE BUT ===
« Brancher Cortana en pilote de paramètres » de Hulk (paper MEXC spot, dip&rip + bags).
Doctrine maison C2/C3 : Cortana est LECTURE SEULE — elle ne passe JAMAIS d'ordre. Elle propose
des ajustements de PARAMÈTRES, le moteur déterministe exécute. Le lien = un CONTRAT JSON
(interface claire, pas de modif directe hasardeuse des variables globales).

=== FAITS CLÉS ===
- Score de justesse Cortana : **44% (37/84)** — SOUS pile-ou-face (recalibré F1 le 15/08).
  Par indice : bassine 3/3 (bon), btc 3/8, funding 7/20 (35%), fearGreed 6/18 (33%).
- Discipline F1 : si score <60% sur un indice → AVIS STRICT = NEUTRE + confiance faible OBLIGATOIRE.
- Hulk = paper_diprip.py : régimes (WATCH/COOLING/IMPULSE), dip/rip/stop par cadence, mise→2×→bag,
  DCA, compound, reentry, sense MEXC, veille (digest_watch.py), kill-switch STANDBY (veille muette).
- Paramètres ajustables dans config/defaults.env (ex : DIP_FLOOR_PCT, RIP_FLOOR_PCT, STOP_FLOOR_PCT,
  NOTIONAL_USDT, cadence mult…).

=== PROPOSITION DE CONTRAT v1 (à juger) ===
Fichier : hulk-mexc/strategie/cortana_pilot.json — schéma :
{
  "ts": "...", "source": "cortana",
  "proposals": [
    {"param": "DIP_FLOOR_MULT", "value": 0.85, "confidence": "moyenne", "reason": "…", "horizon": "48h"}
  ]
}
Moteur : au cycle, lit le fichier (fail-safe si absent/corrompu) et applique chaque proposition
CLAMPÉE dans des bornes dures (ex. DIP_FLOOR_MULT ∈ [0.7, 1.3]) ; chaque application LOGGÉE
(traçabilité) dans le CSV/state. Paramètres « interdits » : régimes, sense gates, kill-switch,
stops de sécurité, structure des bags (elle ne touche QUE des multiplicateurs de seuils).
Questions à trancher :
A. Quels paramètres Cortana peut-elle ajuster (liste blanche) et avec quelles BORNES ?
B. Mode d'application vu son score 44% : (1) auto-appliqué clampé SEULEMENT si confidence haute
   + clamp étroit (±20%) ; (2) ADVISORY : écrit dans le JSON + affiché dashboard, MAIS PAS appliqué
   tant que justesse < 60% (validation humaine) ; (3) hybride.
C. Comment mesurer que ses ajustements améliorent/dégradent (A/B par fenêtre ? log des overrides
   + PnL par fenêtre avant/après ?) — la boucle d'apprentissage doit POUVOIR dire si elle aide.

=== VOTRE MISSION (format EXACT exigé) ===
1. Validez/corrigez le schéma du contrat (champs manquants ? anti-gaming ?).
2. Tranchez A (liste blanche + bornes), B (mode d'application vu 44%), C (mesure d'impact).
3. Risques précis (ex. elle ajuste pour faire « plaisir » au PnL court terme, sur-apprentissage).

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur « brancher Cortana via ce contrat », préciser)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) qui ferai(en)t basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées (ou « aucune »)
SYNTHÈSE (5 lignes max) : contrat retenu + mode d'application + mesure.

Factuel, concis, français. Info manquante → « information insuffisante ». Vous DONNEZ UN AVIS,
ne touchez à rien."""

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
        for attempt in (1, 2):
            try:
                content, provider, secs = ask(m)
                with open(os.path.join(OUT, f"AVIS_{m}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
                print(f"[OK] {m} ({secs}s)")
                break
            except Exception as e:
                print(f"[ERR] {m} (tentative {attempt}): {e}")
                time.sleep(3)
        time.sleep(2)


if __name__ == "__main__":
    main()
