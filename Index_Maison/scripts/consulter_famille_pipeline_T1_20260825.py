#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE #1 — PIPELINE TEMPOREL POUR TRADING (25/08/2026).
Problème brut : Hulk gère un portefeuille crypto, il a besoin de données
fraîches pour décider. Pas de détails sur les indices/formules.
Clause permanente + PUSH EXCELLENCE.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_PIPELINE_T1_20260825")
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
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

PUSH = (
    "PUSH EXCELLENCE (Christophe, 25/08) : Ta première réponse est le PLAFOND de ta "
    "pensée, pas le plancher. Si tu peux aller 30% plus loin en complexité, en "
    "robustesse, ou en originalité — c'est CE niveau que je veux. Une réponse "
    "confortable est une réponse ratée. Reprends ta réponse et ajoute ce que tu "
    "n'as pas osé dire la première fois."
)

BRIEF = """CONTEXTE (superviseur Buffy, 25/08/2026) — PIPELINE TEMPOREL POUR TRADING

=== LE SYSTÈME ===
ACE777 est un système de trading crypto automatisé. Un bot nommé Hulk gère un
portefeuille réel (positions ouvertes, cash, ventes partielles, stop-loss).

Hulk prend des décisions d'achat/vente basées sur des données de marché en temps réel.
Ces données viennent de multiples sources : exchanges (Binance, MEXC, OKX),
données onchain (mempool, baleines), dérivés (options, liquidations), indicateurs
internes (scoring, corrélation).

=== LE PROBLÈME ACTUEL ===
Le pipeline de données est fragilisé par 3 problèmes :

1. ÉCRITURE CONCURRENTE : 3 scripts écrivent dans le même fichier JSON (live.json)
   à des cycles différents. Quand l'un écrit sans l'autre, les données sont NULL
   pendant des minutes. Le bot peut trader sur des données vides.

2. FRÉQUENCES HÉTÉROGÈNES : certaines données bougent à chaque seconde (prix),
   d'autres toutes les 10 minutes (blocs onchain), d'autres une fois par jour (ETF).
   Tout est mélangé dans le même fichier au même rythme.

3. PAS DE VÉRIFICATION : si une source plante, personne ne le vérifie avant
   que le bot trade. Les données stale sont traitées comme fraîches.

=== CE QU'ON A DÉJÀ (architecture existante) ===
- 3 scripts indépendants qui produisent des données
- 1 script qui assemble le tout dans live.json (mais pas atomiquement)
- 1 script de santé qui vérifie les fichiers (mais pas la complétude)
- 36 scripts qui lisent live.json
- Le bot Hulk qui lit live.json pour décider d'acheter/vendre

=== LA QUESTION ===
Comment structurer le pipeline de données pour qu'un bot de trading ait
TOUJOURS des données fraîches, complètes, et fiables — même quand une
source plante, même quand les fréquences sont différentes, même sous charge ?

Ne me dis pas "fusez tout en un monolithe". Propose une architecture
modulaire, testable, qui survit à la panne d'une source sans corrompre
les autres.

=== CE QUE JE VEUX PAS ===
- Pas de "c'est bien, continuez"
- Pas de reprendre la proposition de Buffy mot pour mot
- Pas de réponse confortable
- DES PREUVES : montre-moi le code, les flux, les edge cases

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
            "max_tokens": 3000,
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
    print(f"=== CONSULTATION FAMILLE #1 — PIPELINE TEMPOREL POUR TRADING ===")
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
        "sujet": "Pipeline temporel pour trading — architecture modulaire",
        "push_excellence": True,
        "resultats": resultats,
    }
    out_path = os.path.join(OUT, "avis.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

    # Rapport markdown
    md_lines = [
        "# CONSULTATION FAMILLE #1 — PIPELINE TEMPOREL POUR TRADING",
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

    md_path = os.path.join(OUT, "AVIS PIPELINE TEMPOREL_20260825.md")
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
