#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — QUEUE_OFFRES.PY (file d'attente des offres IA gratuites).
Chaque membre : valide ET suggère une amélioration (3 coups une pierre)."""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_QUEUE_OFFRES_2026-08-13"
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
AUDIT FAMILLE — QUEUE_OFFRES.PY (file d'attente des offres IA gratuites, ACE777)

CONTEXTE HUMAIN (Christophe) : « automatiser la flotille : les offres IA gratuites qui rentrent sont
mises en file d'attente ; la seule validation = comprendre si l'offre est RÉELLE et FONCTIONNE (test
d'appel API) ; la famille + le juge ne tranchent que les 4-6 meilleurs de la file ; réserve pour la
tempête ; vérifier les derniers qui rentrent d'abord. »

DESIGN VALIDÉ : [FLOTILLE] offres fraîches → [FILE QUEUE_OFFRES.json] → pré-filtre RÉEL (test
d'accès call_chat) sur toute la file, fraîcheur d'abord → [TOP 6 teste_ok] → A/B réel (candidat vs
actuel) + VRAI JUGE (hub, task signets.juge) → si MIEUX → intégration OBSERVATION dans
~/prise-ia/providers.json (free:True, enabled par défaut, note=observation) + réserve.

PROCESSUS : spec → codeur (5 itérations, le codeur a livré des versions avec régressions :
chemins faux, placeholders, hub_juge mal appelé, intégration jamais appelée) → SUPERVISEUR a
assemblé la v6 (base v4 correcte + corrections P1-P5 exactes) → tests réels PASSENT.

TESTS RÉELS (prouvés) :
- python3 queue_offres.py --scan → 49 entrées : 11 pistes (signets GARDER, mots-clés IA) + 38 offres
  veille (candidates_from_veille, champs model/base_url/api_key_env complets).
- --pretest → TEST RÉEL fonctionne et élimine les faux positifs : HTTP 429 (rate limit) et HTTP 404
  (endpoint inexistant) détectés sur les 6 premières offres. Cycle de vie : 3 essais → poubelle,
  attente_cle re-traîtée quand la clé devient dispo (chargement ~/prise-ia/.env), quota 4/jour.
- Aucun placeholder/TODO. Intégration ajouter_provider_observation définie ET appelée après verdict
  MIEUX (backup par COPIE jamais rename, structure hub exacte id/name/kind/base_url/model/
  api_key_env/order/timeout/free, doublon base_url+model vérifié).
- Non fatal, verrou PID anti-course, écriture atomique tmp+replace, kill switch STOP_HUB.

CONSTANTES : MAX_ESSAIS=3, MAX_INTEGRATIONS_JOUR=4, MAX_TESTS_PAR_PASSAGE=6.

TA MISSION (3 coups une pierre) :
1. Verdict GO / NO-GO (avec raison courte) sur ce script pour production (intégration launchd 8h15/14h/20h).
2. Un point de risque ou régression possible que tu vois (ex: le hub route-t-il un provider
   'observation' free:True non demandé ? la file grossit-elle indéfiniment ? le test réel consomme-t-il
   des quotas gratuits ?).
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
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[INJOIGNABLE] {str(e)[:120]}"


if __name__ == "__main__":
    print("=== AUDIT FAMILLE 6 — QUEUE_OFFRES ===", flush=True)
    for nom, task, system in MEMBRES:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] Avis écrits dans {OUT}")
