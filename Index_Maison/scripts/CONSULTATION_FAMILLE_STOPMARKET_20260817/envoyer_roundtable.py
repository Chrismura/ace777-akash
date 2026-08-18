#!/usr/bin/env python3
"""Round table famille — STOP_MARKET Binance (17/08/2026)
Envoie le même prompt à toute la famille via le hub, sauvegarde chaque avis."""
import json
import os
import sys
import time
import urllib.request

D = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
PROMPT = open(os.path.join(D, "QUESTION.md"), encoding="utf-8").read()
MEMBRES = ["gemini", "nara", "groq", "nvidia", "mistral", "huggingface"]

SYSTEM = (
    "Tu es un membre du conseil de la famille ACE777. Tu es consulté pour un round table. "
    "Tu réponds en français, de façon structurée, honnête et critique. On te demande ton VRAI avis, "
    "pas une validation polie. Si la solution proposée a un défaut, dis-le. Si tu vois mieux, propose-le. "
    "Termine par: VERDICT: GO / GO-AVEC-RÉSERVE / NO-GO + CONFIANCE: X%"
)

def post(payload, timeout=240):
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    for m in MEMBRES:
        f_json = os.path.join(D, "AVIS_%s.json" % m)
        f_md = os.path.join(D, "AVIS_%s.md" % m)
        try:
            payload = {
                "model": m,
                "task": "famille.stopmarket",
                "temperature": 0.5,
                "max_tokens": 2000,
                "messages": [
                    {"role": "system", "content": SYSTEM},
                    {"role": "user", "content": PROMPT},
                ],
            }
            t0 = time.time()
            d = post(payload)
            prov = d.get("provider", "?")
            content = d["choices"][0]["message"]["content"]
            with open(f_md, "w", encoding="utf-8") as f:
                f.write("# AVIS %s (provider: %s, %.1fs)\n\n%s\n" % (m, prov, time.time() - t0, content))
            with open(f_json, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=1)
            print("OK %s -> %s | %d car. (%.1fs)" % (m, prov, len(content), time.time() - t0))
        except Exception as e:
            print("ERREUR %s: %s" % (m, e))
            try:
                with open(f_json, "w", encoding="utf-8") as f:
                    f.write("ERREUR: %s\n" % e)
            except Exception:
                pass

if __name__ == "__main__":
    main()
