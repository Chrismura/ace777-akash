#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoyer la consultation CHAÎNES à la famille (2 membres + juge).
Règle d'économie : 2 membres + le juge (plus jamais 6)."""
import json
import os
import sys
import time
import urllib.request

D = os.path.dirname(os.path.abspath(__file__))
QUESTION = os.path.join(D, "QUESTION_FAMILLE_CHAINES.md")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

MEMBRES = ["gemini", "groq"]  # 2 membres (les plus réactifs, vérifiés vivants)
JUGE = "signets.juge"         # le juge (nara) — tranche toujours

SYSTEM_MEMBRE = (
    "Tu es un membre du conseil de la famille ACE777. Christophe a demandé une "
    "vérification de la logique des chaînes automatiques et des modifications du jour. "
    "Réponds en français, 3 phrases max, tranche net : GO / GO-AVEC-RÉSERVE / NON. "
    "Si tu proposes une amélioration, dis-la en 1 phrase."
)

SYSTEM_JUGE = (
    "Tu es le JUGE du conseil de la famille ACE777. Deux membres ont déjà donné leur avis. "
    "Lis la question et les 2 avis, puis tranche définitivement : GO / GO-AVEC-RÉSERVE / NON, "
    "avec 3 phrases max et les conditions non négociables si GO-AVEC-RÉSERVE."
)


def lire_question():
    with open(QUESTION, encoding="utf-8") as f:
        return f.read()


def appeler(task, system, question, out_md, out_json):
    payload = {
        "task": task,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": question},
        ],
        "temperature": 0.3,
        "max_tokens": 500,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(HUB, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            txt = res.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        txt = "[ERREUR] %s" % e
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(txt)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({"task": task, "texte": txt}, f, ensure_ascii=False, indent=1)
    print("[OK] %s -> %s" % (task, os.path.basename(out_md)))
    time.sleep(2)


def main():
    question = lire_question()
    # Membres en parallèle (2 threads) puis juge
    import threading
    threads = []
    for m in MEMBRES:
        t = threading.Thread(target=appeler, args=(
            "famille.%s.chaines" % m, SYSTEM_MEMBRE, question,
            os.path.join(D, "AVIS_FAMILLE_CHAINES_%s.md" % m),
            os.path.join(D, "AVIS_FAMILLE_CHAINES_%s.json" % m),
        ))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    # Juge après les 2 avis
    avis = []
    for m in MEMBRES:
        p = os.path.join(D, "AVIS_FAMILLE_CHAINES_%s.md" % m)
        if os.path.exists(p):
            avis.append("## Avis %s\n%s" % (m, open(p, encoding="utf-8").read()))
    question_juge = question + "\n\n---\n\nAVIS DES MEMBRES :\n\n" + "\n\n".join(avis)
    appeler(JUGE, SYSTEM_JUGE, question_juge,
            os.path.join(D, "AVIS_FAMILLE_CHAINES_JUGE.md"),
            os.path.join(D, "AVIS_FAMILLE_CHAINES_JUGE.json"))
    print("=== CONSULTATION TERMINÉE (2 membres + juge) ===")


if __name__ == "__main__":
    main()
