#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — DOUBLE SUJET (14/08) :
   1. ANALYSE DES CYCLES du run test en cours (santé du setup ACE777).
      Hypothèse Christophe : « quand il y a toutes ces décimales, c'est pas bon
      signe de la santé du setup » (tension ~0.00000000 + tonnes de SKIP).
   2. CHAÎNE D'APPROBATION PAR PROMPTS (proposition Buffy) : graver des prompts
      canoniques dans le coffre (Obsidian + GitHub) — GO RUN TEST · AUDIT
      FAMILLE · RE-SCELLAGE C1 · CHAÎNE COMPLÈTE — pour rejouer un flux propre
      et traçable à chaque chantier.

Le run test tourne EN PARALLÈLE (testnet, aucun argent réel). Audit = lecture
seule via le hub. Le run n'est pas interrompu.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_CYCLES_PROMPTS_2026-08-14"
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CONTEXTE = """\
AUDIT FAMILLE — DOUBLE SUJET (14/08, pendant un run test testnet en cours).

CONTEXTE HUMAIN (Christophe) : « Fais analyser un morceau des cycles par la
famille. À mon expérience, quand il y a toutes ces décimales, c'est pas bon
signe de la santé du setup. Et propose ton amélioration des prompts à la
famille en même temps. »

=============================
SUJET 1 — ANALYSE DES CYCLES
=============================
Run : MASTER_VORTEX_V2_COLLAB_4H (testnet, GEMINI_TEST + crash dump, lancé
14/08 07:41Z, durée 1h). Échantillon réel des cycles ALPHA (x13) et BETA (x3),
extrait du log live — pas un récit :

ALPHA (extrait #13→#41, 30 cycles) :
  #13 tension=0.00003549 momentum_too_small conf=0.0001
  #14 tension=0.27027879 wall_not_collapsed
  #15 tension=0.00000000 momentum_too_small conf=0.3493
  #16 tension=0.74447588 wall_not_collapsed
  #17 tension=0.76076460 wall_not_collapsed
  #18 tension=0.97055595 wall_not_collapsed
  #19 tension=0.19226503 direction_unclear conf=0.0116
  #20 tension=0.00002718 momentum_too_small conf=0.0
  #21 tension=0.00000000 momentum_too_small conf=0.3208
  #22 tension=0.02667132 direction_unclear conf=0.0444
  #23 tension=0.00000000 momentum_too_small conf=0.3493
  #24 tension=0.74520963 wall_not_collapsed
  #25 tension=0.00000000 momentum_too_small conf=0.3494
  #26 tension=0.19353512 direction_unclear conf=0.02
  #27 tension=0.00008509 momentum_too_small conf=0.0001
  #28 tension=0.00000000 momentum_too_small conf=0.2722
  #29 tension=0.52501057 wall_not_collapsed
  #30 tension=0.00000000 momentum_too_small conf=0.3228
  #31 tension=0.00000677 momentum_too_small conf=0.0
  #32 tension=0.00001915 momentum_too_small conf=0.0
  #33 tension=0.24498692 low_confidence conf=0.2482
  #34 tension=0.00002589 momentum_too_small conf=0.0
  #35 tension=0.87751616 wall_not_collapsed
  #36 FILL BUY tension=12.27441221 conf=0.9508 pnl=+2.67516000 bps=1.71 total=2.62407
  #37 tension=0.00000000 momentum_too_small conf=0.3278
  #38 tension=0.00000000 momentum_too_small conf=0.2733
  #39 tension=0.00053868 momentum_too_small conf=0.0009
  #40 tension=0.00000000 momentum_too_small conf=0.3233
  #41 tension=0.00000000 momentum_too_small conf=0.3278

BETA (extrait #18→#36, 19 cycles) :
  #18 tension=0.22021653 low_confidence conf=0.3663
  #19 tension=0.40918450 wall_not_collapsed
  #20 tension=0.00000303 momentum_too_small conf=0.0
  #21 tension=0.00000000 momentum_too_small conf=0.3493
  #22 tension=0.00000000 momentum_too_small conf=0.3055
  #23 tension=0.22061930 low_confidence conf=0.3407
  #24 tension=0.00001589 momentum_too_small conf=0.0
  #25 tension=0.00013653 momentum_too_small conf=0.0002
  #26 tension=0.00002447 momentum_too_small conf=0.0
  #27 tension=0.00000000 momentum_too_small conf=0.2083
  #28 tension=0.00000000 momentum_too_small conf=0.1923
  #29 tension=0.00002199 momentum_too_small conf=0.0
  #30 tension=0.00002174 momentum_too_small conf=0.0
  #31 tension=0.26249164 low_confidence conf=0.4001
  #32 tension=0.00021038 momentum_too_small conf=0.0003
  #33 tension=0.00000000 momentum_too_small conf=0.3431
  #34 tension=0.53508012 wall_not_collapsed
  #35 tension=0.00001859 momentum_too_small conf=0.0
  #36 FILL SELL tension=1.12325103 conf=0.726 pnl=+0.02726000 bps=0.46 total=2.65133

LECTURE OBSERVÉE (à confirmer/contredire) :
- ~2/3 des cycles ALPHA et BETA sont à tension ≈ 0 (momentum_too_small,
  conf parfois non nulle ~0.3) → le radar ne capte presque rien la plupart
  du temps. Les fills n'arrivent QUE sur les pics de tension (12.27 / 1.12).
- Profil bimodal : soit tension ~0 (dort), soit tension 0.5–0.97 mais rejeté
  par wall_not_collapsed (le mur n'est pas effondré) → le filtre wall bloque
  une grosse part des candidats.
- PnL positif sur le run (+2.65 total après 2 fills) mais activité très
  sparse : 1 fill ALPHA / 1 fill BETA en ~7 min de cycles serrés.

QUESTIONS SUJET 1 (réponds net) :
S1-1. Verdict santé du setup : sain / fatigué / à surveiller + raison courte.
S1-2. L'hypothèse de Christophe (« trop de décimales ~0 = pas bon signe »)
      est-elle fondée ? Pourquoi oui / non / nuance ?
S1-3. Le filtre wall_not_collapsed rejette-t-il trop ? (0.5–0.97 bloqués) —
      piste de réglage ou comportement voulu ?
S1-4. UNE amélioration GO-sized pour la santé du setup (pas cosmétique).

=============================
SUJET 2 — CHAÎNE D'APPROBATION PAR PROMPTS (proposition Buffy)
=============================
CONTEXTE : aujourd'hui on a refait le même flux à la main (SPEC → JUGE →
codeur → grille → famille → GO). Buffy propose de GRAVER des prompts
canoniques dans le coffre (note Obsidian + version GitHub, les 2 mémoires
globales du projet), chacun avec : contexte vérifié (faits, pas récit) +
points de retour (backups) + contrat de sortie + circuit d'approbation.
Catalogue proposé :
  P1 GO RUN TEST     → toi → préflight vert → run → cockpit en direct
  P2 AUDIT FAMILLE   → Buffy rédige SPEC → famille+juge 6 → verdicts → toi
  P3 RE-SCELLAGE C1  → diff preuve → famille 6/6 → backups → re-scelle doc
  P4 CHAÎNE COMPLÈTE → SPEC → JUGE → codeur → grille → famille → GO
Règles de base : maker ≠ checker (celui qui produit ne valide pas son propre
travail) · automation propose, humain approuve · tout traçable dans les
2 mémoires (obsidian-vault + ace777-akash) · 1 GO = 1 vol.

QUESTIONS SUJET 2 (réponds net) :
S2-1. Verdict sur la proposition : GO / GO AVEC RÉSERVES / NON + raison.
S2-2. Que manque-t-il / que corriger dans le catalogue P1–P4 ?
S2-3. UNE amélioration concrète de la chaîne d'approbation (GO-sized).

TA MISSION GLOBALE :
1. Verdict global (GO / GO AVEC RÉSERVES / NON + raison courte).
2. Réponses S1-1→S1-4 (sujet 1).
3. Réponses S2-1→S2-3 (sujet 2).
Réponds en français, format court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1300,
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
    print(f"=== AUDIT FAMILLE — CYCLES + PROMPTS ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
