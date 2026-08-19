#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""recherche_famille.py — consultation famille en MODE RECHERCHE (19/08/2026).

Comme consulter_famille.py, mais pour une QUESTION OUVERTE (pas un verdict GO/NON) :
  GEMINI + DEEPSEEK en parallèle (prompts canon famille.json), puis le JUGE lit
  les deux et donne un TOP 3. Chaque réponse est archivée AVEC le provider réel
  qui a servi (pour exposer la diversité réelle de la famille).

Usage :
  python3 recherche_famille.py --spec SPEC.md --sujet prompt_memoire [--extra]
"""
import argparse, json, os, sys, threading, urllib.request
from datetime import datetime, timezone
from pathlib import Path

HUB = "http://127.0.0.1:11435/v1/chat/completions"
IDENTITE = Path(__file__).resolve().parent.parent / "identity" / "prompts" / "famille.json"
MAKERS = ["GEMINI", "DEEPSEEK"]
EXTRA = ["ULTRA", "INFERX", "GROK"]

FORMAT_RECHERCHE = (
    "FORMAT DE SORTIE (recherche) :\n"
    "Pour chacune des questions → 3-5 points concrets, chacun suivi d'une SOURCE "
    "(lien + date si connue). Si tu cites de mémoire sans être sûr, écris "
    "« de mémoire, à vérifier ». Pas de blabla, du factuel. Termine par un TOP 3 "
    "d'actions pour ACE777."
)


def charger_canon():
    data = json.loads(IDENTITE.read_text(encoding="utf-8"))
    membres = {m["nom"]: m for m in data["membres"]}
    return data["clause"], membres


# Provider forcé par membre (les tasks canoniques ne sont pas dans routing.json
# -> file universelle lente. On force pour que le test aboutisse, et on capture
# le provider RÉEL dans la réponse.)
MODEL_FORCE = {"GEMINI": "gemini", "DEEPSEEK": "nvidia", "JUGE": "nara"}


def ask(task, system, user, max_tokens=1500, model=None):
    payload = {"task": task,
               "messages": [
                   {"role": "system", "content": system},
                   {"role": "user", "content": user},
               ],
               "max_tokens": max_tokens, "temperature": 0.3}
    if model:
        payload["model"] = model
    body = json.dumps(payload).encode()
    req = urllib.request.Request(HUB, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=150) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", type=str, required=True)
    ap.add_argument("--sujet", type=str, default="recherche")
    ap.add_argument("--extra", action="store_true")
    args = ap.parse_args()

    brief = Path(args.spec).read_text(encoding="utf-8")
    clause, membres = charger_canon()
    out = Path(__file__).parent / f"RECHERCHE_FAMILLE_{args.sujet}_{datetime.now(timezone.utc).strftime('%Y%m%d')}"
    out.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

    user_msg = f"{brief}\n\n---\n{FORMAT_RECHERCHE}\n\nVous répondez avec vos connaissances. Ne touchez à rien."

    noms = MAKERS + (EXTRA if args.extra else [])
    results = {}

    def run(nom):
        m = membres[nom]
        try:
            txt, prov = ask(m["task"], m["prompt"] + "\n\n" + clause, user_msg, model=MODEL_FORCE.get(nom))
            results[nom] = (txt, prov)
            (out / f"AVIS_{nom}.md").write_text(
                f"# RECHERCHE {nom} (task {m['task']} · {prov} · {now})\n\n{txt}\n", encoding="utf-8")
            print(f"[OK] {nom} ({prov}) — {len(txt)} car.", flush=True)
        except Exception as e:
            results[nom] = (f"[INJOIGNABLE] {e}", "?")
            print(f"[ERREUR] {nom}: {e}", flush=True)

    ths = [threading.Thread(target=run, args=(n,)) for n in noms]
    for t in ths:
        t.start()
    for t in ths:
        t.join()

    avis_texte = "\n\n".join(f"=== {n} ===\n{results[n][0]}" for n in MAKERS if n in results)
    m_juge = membres["JUGE"]
    try:
        txt, prov = ask(m_juge["task"], m_juge["prompt"] + "\n\n" + clause,
                        user_msg + f"\n\n---\nAVIS DES AUTRES MEMBRES (à lire d'abord) :\n{avis_texte}",
                        model=MODEL_FORCE.get("JUGE"))
        (out / "AVIS_JUGE.md").write_text(
            f"# RECHERCHE JUGE (task {m_juge['task']} · {prov} · {now})\n\n{txt}\n", encoding="utf-8")
        print(f"[OK] JUGE ({prov}) — {len(txt)} car.", flush=True)
    except Exception as e:
        txt = f"[INJOIGNABLE] {e}"; prov = "?"
        print(f"[ERREUR] JUGE: {e}", flush=True)
    results["JUGE"] = (txt, prov)

    print(f"\nArchive : {out}")
    for n in noms + ["JUGE"]:
        if n in results:
            print(f"  {n}: {results[n][1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
