#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — COCKPIT STABILITÉ v1 (corrections C1/C2/C3).
Chaque membre : valide ET suggère une amélioration (3 coups une pierre).
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_COCKPIT_STABILITE_2026-08-13"
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
AUDIT FAMILLE — COCKPIT ACE777 (STABILITÉ v1)

Problèmes utilisateur (tous REPRODUITS par tests réels : vision Gemini + Chromium headless + pywebview/WebKit) :
1. Le graph cosmos "saute" et les providers restent tassés au centre. Cause : pollHubLive() rappelait buildNodes() toutes les 10s, qui remettait tous les providers à x:0,y:0 (physique de convergence lente ~6s).
2. Cartes ALPHA/BETA : SIZE et lignes de trades affichaient des size_note bruts en anglais (strong_conf_full+entry_25_75_full).
3. Feed cosmos hub.json régénéré toutes les 120s → cockpit pas synchronisé en live.

CORRECTIONS INTÉGRÉES (C1, C2, C3) :
- C1a: buildNodes() initialise désormais les providers DIRECTEMENT sur leur orbite (x=tx, y=ty calculés avant le push).
- C1b: pollHubLive() ne rappelle plus buildNodes() : mise à jour douce des couleurs/tailles des nodes existants (buildNodes complet seulement si le nombre de providers change).
- C2: fonction traduireSizeNote() (FR) appliquée à SIZE et aux lignes de trades des cartes ALPHA/BETA. Insérée dans le bloc 1 (renderEngine) car le bloc 2 est une IIFE.
- C3: launchd com.ace777.hub-cockpit-feed StartInterval 120s → 30s (vérifié : feed âge 13-27s).

TESTS RÉELS (après correction) :
- Chromium : positions stables T0=141 / T+12s=137 (avant : 89 → 138 = saut permanent). Cartes traduites. 0 erreur JS.
- WebKit (pywebview, moteur réel) : cartes traduites, synMeta "ACE ON · PONT ON · NET SLOW", feed 27s, 0 erreur.

TA MISSION (3 coups une pierre) :
1. Verdict GO / NO-GO (avec raison courte) sur ces corrections.
2. Un point de risque ou régression possible que tu vois.
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
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"]

for nom, task, system in MEMBRES:
    try:
        print(f"[i] {nom} ...")
        rep = ask((nom, task), system)
        with open(os.path.join(OUT, nom + ".md"), "w", encoding="utf-8") as f:
            f.write(rep)
        print(f"  → {nom} répondu ({len(rep)} chars)")
    except Exception as e:
        print(f"[X] {nom} échec : {e}")
