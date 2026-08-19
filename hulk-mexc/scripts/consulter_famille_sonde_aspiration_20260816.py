#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — HULK : SONDE ASPIRATION (double lecture carnet) — 16/08/2026.

Protocole maison : 6 personnages famille (prompts system officiels) routés via le hub
par task, + avis du codeur (task code.ia) déjà recueillis en entrée. Ne touche à rien.
"""
import json
import os
import sys
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_SONDE_ASPIRATION_20260816")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

# CLAUSE PERMANENTE (gravée 16/08 par Christophe — applicable à TOUS les prompts).
CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

CONTEXTE = """\
SONDE ASPIRATION HULK — consultation famille (16/08/2026 soir)

================
LA DEMANDE (Christophe)
================
« Je veux qu'il sonde comme ACE : voir les murs de liquidité, l'aspiration,
l'historique qui fait parti pris — l'intelligence si c'est possible. »
HULK (paper dip&rip MEXC small caps) lit déjà le carnet une fois par cycle
(scripts/ace_sense_mexc.py : spread, profondeur, imbalance, murs, tension).
Ce qui manque vs ACE : la DOUBLE lecture du carnet à ~0.5-1s d'écart pour
voir les MURS QUI FONDENT (wall_drop_bid/ask_pct) et en déduire
aspiration_side (BUY si le mur ask fond = prix aspiré vers le haut ;
SELL si le mur bid fond). C'est « l'aspiration ».

================
VERDICTS DU CODEUR (task code.ia, 4 avis recueillis ce soir)
================
4/4 : GO-AVEC-RÉSERVE (confiance 72-78%).
- Délai 2e lecture : 0.5s (DeepSeek/Codestral) vs 1s (Gemini/NVIDIA) — à trancher.
- Seuil « percussion » : 12% (NVIDIA), 15% (DeepSeek), 20% (Gemini), 10-15% (Codestral).
- Fail-open validé par tous : 2e lecture qui échoue → lecture simple, jamais de blocage.
- Réserve commune : implémenter en MODE OBSERVATION 48h (log drop_bid/drop_ask/side,
  SANS agir sur les entrées), calibrer le seuil sur données réelles, activer ensuite
  seulement si signal juste (>60%).
- Limiter aux paires actives (régime COOLING/IMPULSE) pour ne pas exploser le rate-limit MEXC.
- Entrée d'abord ; sortie anticipée (aspiration SELL sur position ouverte) en V2.
- Bonus DeepSeek : triple lecture 0.3s + médiane pour filtrer le bruit.

================
CE QUE JE PROPOSE (superviseur Buffy)
================
A. Implémenter aspiration_sense() dans ace_sense_mexc.py : double lecture fail-open,
   drop_bid_pct/drop_ask_pct/side/max_drop_pct, config ASPIRATION_ON/DELAY_S/WALL_DROP_PCT.
B. Mode OBSERVATION : log + radar (drop_bid/drop_ask/side par paire) + fichier de
   calibration. AUCUN effet sur entry_gate pendant 48h.
C. Après 48h : analyser la justesse (aspiration BUY → prix monte ?), puis décider
   d'activer l'effet sur les entrées (ou pas) avec la famille.

================
TA MISSION (3 coups une pierre)
================
1. VERDICT sur le plan A+B+C : GO / GO AVEC RESERVES / NON + raison courte et nette
   (le JUGE tranche formellement).
2. Le(s) point(s) qui MANQUE(nt) ou est/sont mal borné(s) dans ce plan (angle mort).
3. UNE amélioration concrète GO-sized (pas cosmétique) pour fiabiliser la sonde.
Réponds en français, format court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system + "\n\n" + CLAUSE},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1400,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")
    except Exception as e:
        return f"[INJOIGNABLE] {str(e)[:120]}", "?"


if __name__ == "__main__":
    import time
    cible = sys.argv[1].upper() if len(sys.argv) > 1 else None
    membres = [(n, t, s) for n, t, s in MEMBRES if cible is None or n == cible]
    if not membres:
        print(f"[ERR] membre inconnu : {cible} (dispo: {[m[0] for m in MEMBRES]})")
        sys.exit(1)
    for nom, task, system in membres:
        try:
            content, provider = ask((nom, task), system)
        except Exception as e:
            content, provider = f"[ERREUR] {e}", "?"
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as fh:
            fh.write(f"# AVIS {nom} (provider {provider})\n\n{content}\n")
        print(f"[OK] {nom} ({provider})")
        time.sleep(2)
