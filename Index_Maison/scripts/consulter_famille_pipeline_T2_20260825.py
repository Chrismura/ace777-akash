#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE #2 — PUSH DES MEILLEURES IDÉES T1 (25/08/2026).
On reprend les meilleures propositions de la T1 et on les pousse avec
les contraintes réelles : macOS, 36 consommateurs, 3 temporalités,
implémentation incrémentale.
Clause permanente + PUSH EXCELLENCE.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_PIPELINE_T2_20260825")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon pragmatique de la famille ACE777. Tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu."
)

PUSH = (
    "PUSH EXCELLENCE (Christophe, 25/08) : Ta première réponse est le PLAFOND de ta "
    "pensée, pas le plancher. Si tu peux aller 30% plus loin en complexité, en "
    "robustesse, ou en originalité — c'est CE niveau que je veux. Une réponse "
    "confortable est une réponse ratée. Reprends ta réponse et ajoute ce que tu "
    "n'as pas osé dire la première fois."
)

BRIEF = """CONTEXTE (superviseur Buffy, 25/08/2026) — PUSH T2 : IMPLÉMENTATION CONCRÈTE

=== RAPPEL DE LA T1 (6/6 membres ont répondu) ===
La famille a proposé des architectures avancées :
- SQLite WAL (DEEPSEEK, ULTRA) — pas de Redis, pas de daemon lourd
- LMDB (GROK) — memory-mapped, ACID, zéro daemon
- TTL-Gate / Gatekeeper (JUGE) — validation fraîcheur avant lecture
- Circuit Breaker + Degraded Mode (GEMINI) — pas de trade sur données stale
- Price Anomaly Detector Z-Score (GROK) — filtrage aberrances
- Event-Sourcing + Shared Memory (INFERX) — bus IPC ultra-rapide

=== CONTRAINTES RÉELLES (maintenant) ===
1. **OS** : macOS (pas Linux). `/dev/shm` n'existe pas. LMDB marche.
2. **36 scripts** lisent actuellement `live.json`. On ne peut PAS tout casser d'un coup.
3. **3 temporalités** pour Hulk :
   - Court terme (scalping 5s-5min) : prix, spread, liquidations en temps réel
   - Swing (1h-4h) : corrélations, funding, score interne
   - Position (1j-7j) : baleines, ETF, macro
4. **Zéro dépendance externe** dans un premier temps (pas Redis, pas Kafka)
5. **Implémentation incrémentale** : on ne réécrit pas tout en 1 jour

=== CE QUE JE VEUX MAINTENANT ===
La feuille de route IMPLÉMENTABLE en 3 étapes :

ÉTAPE 1 (ce soir) : Le minimum vital — éliminer la race condition
- Comment faire pour que les 3 scripts écrivent sans se marcher dessus
- Sur macOS, avec stdlib seule
- En gardant la rétrocompatibilité live.json pour les 36 scripts

ÉTAPE 2 (cette semaine) : Le TTL + Circuit Breaker
- Comment intégrer la validation fraîcheur dans le flux de lecture de Hulk
- Comment Hulk réagit quand une source est stale
- Le Circuit Breaker concret (quel code, quel trigger)

ÉTAPE 3 (semaine prochaine) : Le store temporel
- SQLite WAL ou LMDB pour le stockage
- Isolation par temporalité (Hot/Warm/Cold)
- Le Dead Man's Switch

Pour CHAQUE étape, donne-moi :
- Le code exact (pas du pseudo-code, du Python qui tourne)
- Les edge cases à tester
- Le temps d'implémentation estimé

""" + CLAUSE + "\n\n" + PUSH


def appel_membre(membre, brief, timeout=90):
    nom, model, system = membre
    try:
        data = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system + "\n\n" + CLAUSE + "\n\n" + PUSH},
                {"role": "user", "content": brief},
            ],
            "temperature": 0.4,
            "max_tokens": 4000,
        }).encode()
        req = urllib.request.Request(
            HUB,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        t0 = time.time()
        with urllib.request.urlopen(req, timeout=timeout) as r:
            resp = json.loads(r.read())
        duree = time.time() - t0
        texte = resp["choices"][0]["message"]["content"]
        return {"nom": nom, "ok": True, "texte": texte, "duree": round(duree, 1)}
    except Exception as e:
        return {"nom": nom, "ok": False, "texte": str(e), "duree": 0}


def main():
    print(f"=== CONSULTATION FAMILLE #2 — PUSH T2 IMPLÉMENTATION ===")
    print(f"Membres : {len(MEMBRES)}")
    print(f"Push excellence : ON")
    print()
    resultats = []
    for membre in MEMBRES:
        print(f"  → {membre[0]}...", end="", flush=True)
        r = appel_membre(membre, BRIEF)
        resultats.append(r)
        if r["ok"]:
            print(f" ✅ {r['duree']}s ({len(r['texte'])} car)")
        else:
            print(f" ❌ {r['texte'][:80]}")
        time.sleep(0.5)

    # Sauvegarde
    out_data = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sujet": "Push T2 — feuille de route implémentable en 3 étapes",
        "push_excellence": True,
        "resultats": resultats,
    }
    out_path = os.path.join(OUT, "avis.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

    # Rapport markdown
    md_lines = [
        "# CONSULTATION FAMILLE #2 — PUSH T2 IMPLÉMENTATION",
        f"> {out_data['ts']}",
        f"> Push excellence : ON",
        "",
    ]
    for r in resultats:
        md_lines.append(f"## {r['nom']} {'✅' if r['ok'] else '❌'}")
        md_lines.append("")
        if r["ok"]:
            md_lines.append(r["texte"])
        else:
            md_lines.append(f"Erreur : {r['texte']}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    md_path = os.path.join(OUT, "AVIS PUSH T2_20260825.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\n=== SAUVEGARDÉ ===")
    print(f"  {out_path}")
    print(f"  {md_path}")

    # Résumé rapide
    print(f"\n=== RÉSUMÉ ===")
    for r in resultats:
        if r["ok"]:
            premiere_ligne = r["texte"].split("\n")[0][:120]
            print(f"  {r['nom']}: {premiere_ligne}")


if __name__ == "__main__":
    main()
