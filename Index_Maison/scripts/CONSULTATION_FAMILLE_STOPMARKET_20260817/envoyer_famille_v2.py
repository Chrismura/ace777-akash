#!/usr/bin/env python3
"""Validation famille V2 — PATCH STOP_MARKET (17/08/2026)
Règle d'économie : 2 membres + le juge (plus jamais 6)."""
import json
import os
import time
import urllib.request

D = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
PROMPT = open(os.path.join(D, "QUESTION_FAMILLE_V2.md"), encoding="utf-8").read()

MEMBRES = ["gemini", "groq"]  # 2 membres (les plus réactifs, vérifiés vivants)
JUGE = "signets.juge"         # le juge (nara) — tranche toujours

SYSTEM = (
    "Tu es un membre du conseil de la famille ACE777, consulté pour la validation finale d'un patch. "
    "Tu réponds en français, de façon structurée, honnête et critique. On te demande ton VRAI avis, "
    "pas une validation polie. Si la solution a un défaut, dis-le. Si tu vois mieux, propose-le. "
    "Termine par: VERDICT: GO / GO-AVEC-RÉSERVE / NO-GO + CONFIANCE: X%"
)

SYSTEM_JUGE = (
    "Tu es le JUGE du conseil de la famille ACE777. Deux membres ont déjà donné leur avis. "
    "Ton rôle : trancher. Tu lis le patch et tu rends la décision finale, en connaissance de cause. "
    "Tu peux confirmer, corriger, ou imposer une condition. Tu réponds en français, structuré et ferme. "
    "Termine par: VERDICT FINAL: GO / GO-AVEC-RÉSERVE / NO-GO + CONFIANCE: X% + conditions éventuelles"
)


def post(payload, timeout=300):
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def send(tag, model, system, out_md, out_json):
    payload = {
        "model": model,
        "task": "famille.stopmarket.v2",
        "temperature": 0.4,
        "max_tokens": 2200,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": PROMPT},
        ],
    }
    try:
        t0 = time.time()
        d = post(payload)
        prov = d.get("provider", "?")
        content = d["choices"][0]["message"]["content"]
        with open(out_md, "w", encoding="utf-8") as f:
            f.write("# AVIS %s (provider: %s, %.1fs)\n\n%s\n" % (tag, prov, time.time() - t0, content))
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        print("OK %s -> %s | %d car. (%.1fs)" % (tag, prov, len(content), time.time() - t0))
    except Exception as e:
        print("ERREUR %s: %s" % (tag, e))
        with open(out_json, "w", encoding="utf-8") as f:
            f.write("ERREUR: %s\n" % e)


if __name__ == "__main__":
    for m in MEMBRES:
        send(m, m, SYSTEM,
             os.path.join(D, "AVIS_FAMILLE_V2_%s.md" % m),
             os.path.join(D, "AVIS_FAMILLE_V2_%s.json" % m))
    send("JUGE", JUGE, SYSTEM_JUGE,
         os.path.join(D, "AVIS_FAMILLE_V2_JUGE.md"),
         os.path.join(D, "AVIS_FAMILLE_V2_JUGE.json"))
