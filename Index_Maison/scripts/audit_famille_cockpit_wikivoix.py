#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — COCKPIT WIKI+VOIX (GLOSSARY etfEthM/etfXrpM).
Chaque membre : valide ET suggère une amélioration (3 coups une pierre).
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_COCKPIT_WIKIVOIX_2026-08-13"
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, membre de la famille ACE777. Audit de code."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, membre de la famille ACE777. Audit de code."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Audit de code."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Audit de code."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, membre de la famille ACE777. Audit de code."),
]

CONTEXTE = """
AUDIT FAMILLE — COCKPIT ACE777 (WIKI + VOIX)

Plaintes utilisateur : « les petites boutons wiki des bulles d'indice ne marchent plus et même la voix aussi ».

DIAGNOSTIC SUPERVISEUR (prouvé par tests réels Chromium headless + pywebview/WebKit = moteur du user) :
1. BUG RÉEL GLOSSARY : les bulles ETF ETH (etfEthM) et ETF XRP (etfXrpM) étaient référencées par data-wiki/DELTA_PEDA mais ABSENTES du dictionnaire GLOSSARY du panneau pédagogique. Clic sur 📖 → fillPeda() false → le panneau gardait l'ancien contenu (ex: « ETF BTC FLUX ») → impression de bouton mort. Les 22 autres boutons marchaient déjà.
2. La VOIX est saine : clic VOIX → pont :17777 /speak → brief Gemini (cortana_brief.py) → TTS edge_tts → afplay joue le mp3 (vérifié : process afplay actif ~55s, fichier mp3 généré, volume 75%, mute=false).
3. Cause probable de l'impression « boutons morts » chez l'utilisateur : il voyait une VIEILLE version en cache (fenêtre pywebview ouverte avant le fix « badge avis IA » du 21:15) où la fonction avBadgeHtml était HORS du bloc <script> → le bloc JS entier plantait → handlers wiki ET voix jamais attachés. La version servie (md5 identique au disque) est corrigée.

CORRECTION INTÉGRÉE (flux codeur + superviseur) :
- Ajout de 2 entrées GLOSSARY : etfEthM {t:'ETF ETH FLUX', ...} et etfXrpM {t:'ETF XRP FLUX', ...}, même structure t/d/s que les autres, insérées après etfBtcM.

TESTS RÉELS (après correction) :
- Chromium headless : clic 📖 sur etfBtcM → « ETF BTC FLUX », etfEthM → « ETF ETH FLUX », etfXrpM → « ETF XRP FLUX », fearGreed → « FEAR & GREED ». Aucune clé wiki manquante restante. node --check OK sur les 2 blocs.
- WebKit (pywebview) : clic wiki OK, VOIX → bouton « ■ STOP » + bubble « brief en cours… ».

TA MISSION (3 coups une pierre) :
1. Verdict GO / NO-GO (avec raison courte) sur cette correction.
2. Un point de risque ou régression possible que tu vois (ex: panneau pédagogique figé sur contenu périmé quand une clé est absente).
3. UNE suggestion d'amélioration concrète de logique/perf/stabilité (pas cosmétique).
Réponds en français, format court et net.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 700,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        r = json.loads(urllib.request.urlopen(req, timeout=None).read().decode())
        return r["choices"][0]["message"]["content"]
    except Exception as e:
        return f"ERREUR: {e}"


def main():
    for nom, task, system in MEMBRES:
        rep = ask((nom, task), system)
        p = os.path.join(OUT, f"VERDICT_{nom}.md")
        with open(p, "w", encoding="utf-8") as f:
            f.write(f"# VERDICT {nom}\n\n{rep}\n")
        print(f"[{nom}] → {p}")
        print(rep[:300].replace("\n", " "))
        print("---")


if __name__ == "__main__":
    main()
