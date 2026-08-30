#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — DÉTECTION BALEINES DISCRÈTES (25/08/2026).
On pose le problème SANS révéler nos méthodes existantes.
Clause permanente + PUSH EXCELLENCE.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_WHALES_20260825")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches : GO / GO AVEC RESERVES / NON."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Robustesse à l'échelle."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Logique interne, pièges."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon pragmatique de la famille ACE777."),
]

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger. "
    "Propose AUTRE CHOSE ou une AMÉLIORATION. Corriger n'est pas suffisant."
)

PUSH = (
    "PUSH EXCELLENCE : Ta première réponse est le PLAFOND, pas le plancher. "
    "Va 30% plus loin. Une réponse confortable est ratée."
)

BRIEF = """CONTEXTE (superviseur Buffy, 25/08/2026) — DÉTECTION BALEINES DISCRÈTES

=== LE PROBLÈME ===
On surveille les mouvements de baleines Bitcoin pour anticiper les mouvements de marché.
Notre approche actuelle : détecter les gros blocs (>1000 BTC) sur les adresses surveillées.

Le problème : les baleines savent qu'elles sont traquées par des sociétés spécialisées.
Elles bougent en douce :
- Micro-transactions sous les seuils de détection
- Fragmentation en 50-100 petits wallets
- Timing aux heures creuses
- OTC (hors chaîne, invisible)

Conséquence : nos signaux de mouvement de baleines sont souvent des CONSOLIDATIONS INTERNES
(ex: hot wallet exchange qui déplace du BTC vers cold wallet) et pas des vrais
mouvements de marché.

=== CE QU'ON A OBSERVÉ ===
Quand il n'y a AUCUN mouvement de baleines visible sur les adresses surveillées,
mais que les FRAIS de transaction montent anormalement (z-score élevé) et que
le nombre de micro-transactions augmente → c'est souvent le signe d'une activité
CACHÉE. Le marché ne bouge pas, mais la mempool parle.

=== LA QUESTION ===
Comment améliorer la sensibilité de détection des mouvements de baleines
quand elles agissent en douce ? Quels signaux INDIRECTS pourraient trahir
leur activité même quand elles ne bougent pas de gros blocs ?

Ne me dis pas "augmentez le seuil" ou "ajoutez plus d'adresses".
Propose des approches NOUVELLES qui exploitent les traces laissées
par l'activité même quand elle est discrète.

=== CE QUE JE VEUX PAS ===
- Pas de "c'est bien, continuez"
- Pas de reprendre notre approche
- Des preuves concrètes (exemples historiques, mécanismes)
- Une hiérarchie des signaux par fiabilité
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
            HUB, data=data,
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
    print("=== CONSULTATION FAMILLE — BALEINES DISCRÈTES ===")
    print(f"Membres: {len(MEMBRES)}")
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

    out_data = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "sujet": "Détection baleines discrètes — signaux indirects",
        "resultats": resultats,
    }
    out_path = os.path.join(OUT, "avis.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

    md_lines = [
        "# CONSULTATION — BALEINES DISCRÈTES",
        f"> {out_data['ts']}",
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

    md_path = os.path.join(OUT, "AVIS BALEINES DISCRÈTES_20260825.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\n=== SAUVEGARDÉ ===")
    print(f"  {md_path}")


if __name__ == "__main__":
    main()
