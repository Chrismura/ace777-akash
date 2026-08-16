#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — PRÉ-VOL SANTÉ DES INDEX (17/08/2026).
Avis seulement, rien n'est appliqué. Clause permanente gravée (16/08)."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_SANTE_INDEX_20260817")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

BRIEF = """CONTEXTE (superviseur Buffy, 17/08/2026) — PRÉ-VOL « SANTÉ DES INDEX » ACE777

=== LE PROBLÈME (Christophe, source directe) ===
« Comment avoir des index et savoir qu'ils sont branchés et fonctionnent en un coup d'œil ? »
Motivation : le chantier baleines est resté DÉBRANCHÉ alors qu'il devait l'être — le scan
tournait (fichier frais), mais le pont n'était lancé par AUCUNE plist → Ada/Cortana ne
recevaient rien, et RIEN ne le montrait. La veilleuse synapses vérifie l'intégrité (md5)
et la fraîcheur des fichiers UN PAR UN — pas que la donnée TRAVERSE la chaîne.

=== CE QUI A ÉTÉ LIVRÉ (17/08, vérifié) ===
1. sante_index.py (plist toutes les 5 min) : vérifie 6 chaînes MAILLON PAR MAILLON —
   process vivant + fichier frais + donnée présente chez le consommateur :
   BALEINES (scan→pont→live.json.onchain→Ada+Cortana) · HULK (sonde→CSV aspiration) ·
   LIVE (thermo→mission→cockpit) · CPFP (observation 7j) · SÉCURITÉ (veilleuse) ·
   SAISON (6 indices). Écrit thermo/sante_index.json + cockpit/sante_live.js.
2. Cockpit : carte 🩺 SANTÉ DES INDEX (🟢/🔴 par chaîne, détail des maillons cassés en rouge).
3. Déclaré au registre veilleuse (md5) — veilleuse STABLE.

=== CE QUI EST DEMANDÉ AU CODEUR (en cours, en parallèle) ===
Alerte vocale sur chaîne rouge + historique append-only des transitions + panneau dépliable.

=== VOTRE MISSION (avis, rien n'est appliqué) ===
1. VERDICT : GO / GO AVEC RÉSERVES / NON sur le pré-vol SANTÉ DES INDEX tel que conçu
   (chaînes maillon par maillon, cockpit, plist 5 min).
2. LES 6 CHAÎNES : manque-t-il une chaîne critique ? (ex. hub LLM, git push auto, discipline quotidienne,
   scan baleines seul ?) Une chaîne est-elle mal définie ou trop laxiste (seuil d'âge trop grand) ?
3. FAUX POSITIFS / FAUX NÉGATIFS : que risque-t-on de rater ou de crier à tort ?
   (ex. fichier append-only vide sur marché calme, process label différent, seuils.)
4. ALERTE VOCALE sur chaîne rouge : pertinente ? Risque de sur-alerte (crier pour un maillon
   transitoire) ? Quelle escalade proposer (log → carte rouge → voix) ?
5. AMÉLIORATION PROPOSÉE (clause permanente) : UNE idée concrète qui a du sens — si elle est
   prouvée, elle sera retenue.

Puis donnez :
  VERDICT : GO | GO-AVEC-RÉSERVES | NON
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) qui ferai(en)t basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)
SYNTHÈSE (5 lignes max).

Factuel, concis, français. Info manquante → « information insuffisante ». Vous DONNEZ UN
AVIS, ne touchez à rien."""


def ask(membre, system):
    payload = json.dumps({
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system + "\n\n" + CLAUSE},
            {"role": "user", "content": BRIEF},
        ],
        "max_tokens": 1600, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for membre in MEMBRES:
        nom = membre[0]
        out_file = os.path.join(OUT, f"AVIS_{nom}.md")
        if os.path.exists(out_file):
            print(f"[SKIP] {nom} déjà répondu")
            continue
        try:
            content, provider, dur = ask(membre, membre[2])
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(f"# AVIS {nom} (task {membre[1]}, provider {provider}, {dur}s)\n\n{content}\n")
            print(f"[OK] {nom} ({dur}s, provider {provider})")
        except Exception as e:
            print(f"[ERREUR] {nom}: {e}")


if __name__ == "__main__":
    main()
