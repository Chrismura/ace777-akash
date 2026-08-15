#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — VALIDATION FINALE DU PATCH v3 (anti-mort silencieuse).

Circuit : cible A tranchee 6/6 (AUDIT_CIBLE_CORRECTION) -> codeur -> SPEC v3
(diff EXACT, les 2 livrables precedents etaient de la fiction rejetee par le
superviseur) -> grille 1-3 passee -> FAMILLE valide le patch -> GO Christophe
-> application + re-scellement -> retest.

Chaque membre : (1) verdict GO / GO AVEC RESERVES / NON sur le patch v3,
(2) verifier le diff (pas d'invention, pas de regression nominale),
(3) la strategie safe_call est-elle la meilleure logique (clause Christophe),
(4) reserves eventuelles GO-sized AVANT application, (5) confirmation que le
re-scellement + indicateur retest (survie > 10 min / fill #50) suffisent.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
OUT = os.path.join(ROOT, "Index_Maison", "VALIDATION_PATCH_V3_2026-08-14")
os.makedirs(OUT, exist_ok=True)

with open(os.path.join(ROOT, "SPEC_correction_panne_alpha_v3.md"), encoding="utf-8") as f:
    SPEC = f.read()
with open(os.path.join(ROOT, "Index_Maison", "CODE_correction_panne_alpha_v3.md"), encoding="utf-8") as f:
    CODE = f.read()

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CONTEXTE = f"""\
VALIDATION FINALE DU PATCH — ALPHA meurt en rc=1 (mort silencieuse, reproduite
2x). Derniere porte avant GO Christophe : tu valides le patch v3 du codeur.

================
RAPPEL (faits verifies)
================
1. Panne : ALPHA rc=1 a 07:49:10Z (~8 min apres depart, apres fill #42),
   14/08. Pattern identique au 13/08. FATAL_RC1 VIDE (trap ERR ne se propage
   pas dans les substitutions sous set -e).
2. Mecanisme famille 6/6 (2 rounds) : helpers ruby (json_get/as_num) dans des
   substitutions $(...) qui sortent rc!=0 -> set -e guillotine le sous-shell.
   public_get/curl_with_retry sont deja proteges (retournent 0).
3. Cible tranchee 6/6 : Option A = ajout minimal dans genesis_manifest.txt
   (champion INTANGIBLE, mais re-scellable — precedent trap ligne 90 =
   af307996, valide 6/6). Option B (injection lanceur) rejetee.
4. Les 2 premiers livrables codeur (v1, v2) etaient de la FICTION : variables
   et cles JSON inventees ($book, calc_entry, "bid" au lieu de "bidPrice").
   Le superviseur a rejete et la SPEC v3 impose le diff EXACT (lignes lues).
5. Grille 1-3 passee par le superviseur : safe_call false -> rc 0 + warning
   logge ; safe_call json_get "" -> rc 0, pas de mort ; bash -n ok.

================
LE PATCH v3 A VALIDER
================
SPEC v3 :
{SPEC}

CODEUR v3 :
{CODE}

================
TA MISSION (5 reponses nettes)
================
1. VERDICT final : GO / GO AVEC RESERVES / NON sur l'application du patch v3.
2. Le diff est-il SANS invention et sans regression du comportement nominal
   (les 10 lignes old->new sont-elles exactes et minimales) ?
3. safe_call est-il la MEILLEURE logique (clause permanente Christophe) ?
4. RESERVES eventuelles AVANT application (GO-sized, minimales).
5. Le re-scellement du champion + l'indicateur retest (survie > 10 min /
   passage fill #50) suffisent-ils pour valider le retest ?
Reponds en francais, court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1500,
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
    import sys
    cible = sys.argv[1].upper() if len(sys.argv) > 1 else None
    membres = [(n, t, s) for n, t, s in MEMBRES if cible is None or n == cible]
    if not membres:
        print(f"[ERR] membre inconnu : {cible} (dispo: {[m[0] for m in MEMBRES]})")
        sys.exit(1)
    print(f"=== VALIDATION PATCH v3 ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
