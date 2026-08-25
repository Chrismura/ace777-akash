#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONSULTER_FAMILLE.py — consultation FAMILLE canonique ACE777 (18/08/2026).

PROTOCOLE (canon, NE PAS improviser) :
  1. GEMINI (gemini.analyse) + DEEPSEEK (deepseek.analyse) EN PARALLÈLE.
     Option --extra : ajoute ULTRA + INFERX + GROK en parallèle.
  2. JUGE (juge.tranche) SÉQUENTIEL : il reçoit les avis des autres et TRANCHE
     après les avoir lus (maker ≠ checker).
Chaque membre reçoit son prompt canon (identity/prompts/famille.json) + la
CLAUSE PERMANENTE de Christophe + le format de sortie obligatoire.
Avis seulement : rien n'est appliqué.

Usage :
  python3 consulter_famille.py --spec SPEC.md --sujet etape5 [--extra] [--out DIR]
  python3 consulter_famille.py --question "..." --sujet etape5 [--extra]

Sortie : OUT/AVIS_GEMINI.md, AVIS_DEEPSEEK.md, [AVIS_ULTRA/INFERX/GROK.md,]
         AVIS_JUGE.md, SYNTHESE.md
"""
import argparse
import json
import os
import sys
import time
import threading
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HUB = "http://127.0.0.1:11435/v1/chat/completions"
IDENTITE = Path(__file__).resolve().parent.parent / "identity" / "prompts" / "famille.json"

# Ordre du protocole : les "makers" (phase 1) puis le juge (phase 2)
MAKERS = ["GEMINI", "DEEPSEEK"]
EXTRA = ["ULTRA", "INFERX", "GROK"]


def charger_canon():
    data = json.loads(IDENTITE.read_text(encoding="utf-8"))
    membres = {m["nom"]: m for m in data["membres"]}
    return data["clause"], data["format"], membres


def ask(task, system, user, max_tokens=1600):
    payload = json.dumps({
        "task": task,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_tokens": max_tokens, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")


def extraire_verdict(texte):
    # Tolérant au format des membres (« VERDICT : », « **VERDICT** : »,
    # « ### VERDICT : ») — on cherche le mot VERDICT dans la ligne.
    for ln in texte.splitlines():
        u = ln.strip().upper()
        if "VERDICT" in u:
            # prend ce qui suit « : » après le mot VERDICT (dernier « : »)
            apres = ln.split(":", 1)[-1].strip() if ":" in ln else ln
            apres = apres.strip("*# -")
            if apres:
                return apres
    return "?"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", type=str, help="fichier SPEC à soumettre")
    ap.add_argument("--question", type=str, help="question brute")
    ap.add_argument("--sujet", type=str, default="consultation")
    ap.add_argument("--extra", action="store_true", help="ajouter ULTRA/INFERX/GROK")
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    if args.spec:
        brief = Path(args.spec).read_text(encoding="utf-8")
    elif args.question:
        brief = args.question
    else:
        print("Fournir --spec ou --question.")
        return 2

    clause, format_out, membres = charger_canon()
    out = Path(args.out) if args.out else Path(__file__).parent / f"CONSULTATION_FAMILLE_{args.sujet}"
    out.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

    system_user = f"{brief}\n\n---\nFORMAT DE SORTIE OBLIGATOIRE :\n{format_out}\n\nFactuel, concis, français. Info manquante -> « information insuffisante ». Vous DONNEZ UN AVIS, ne touchez à rien."

    # Phase 1 : makers en parallèle
    noms_phase1 = MAKERS + (EXTRA if args.extra else [])
    results = {}

    def run(nom):
        m = membres[nom]
        try:
            txt, prov = ask(m["task"], m["prompt"] + "\n\n" + clause, system_user)
            results[nom] = (txt, prov)
            (out / f"AVIS_{nom}.md").write_text(
                f"# AVIS {nom} (task {m['task']} · {prov} · {now})\n\n{txt}\n", encoding="utf-8")
            print(f"[OK] {nom} ({prov}) -> verdict={extraire_verdict(txt)}", flush=True)
        except Exception as e:
            results[nom] = (f"[INJOIGNABLE] {e}", "?")
            print(f"[ERREUR] {nom}: {e}", flush=True)

    ths = [threading.Thread(target=run, args=(n,)) for n in noms_phase1]
    for t in ths:
        t.start()
    for t in ths:
        t.join()

    # Phase 2 : le JUGE lit les avis des makers, puis tranche
    avis_texte = "\n\n".join(f"=== AVIS {n} ===\n{results[n][0]}" for n in MAKERS if n in results)
    m_juge = membres["JUGE"]
    try:
        txt, prov = ask(m_juge["task"], m_juge["prompt"] + "\n\n" + clause,
                        system_user + f"\n\n---\nAVIS DES AUTRES MEMBRES (à lire avant de trancher) :\n{avis_texte}")
        (out / "AVIS_JUGE.md").write_text(
            f"# AVIS JUGE (task {m_juge['task']} · {prov} · {now})\n\n{txt}\n", encoding="utf-8")
        print(f"[OK] JUGE ({prov}) -> verdict={extraire_verdict(txt)}", flush=True)
    except Exception as e:
        txt = f"[INJOIGNABLE] {e}"
        prov = "?"
        print(f"[ERREUR] JUGE: {e}", flush=True)
    results["JUGE"] = (txt, prov)

    # Synthèse
    lignes = ["# SYNTHÈSE FAMILLE — " + args.sujet + " — " + now, "",
              "| Membre | Verdict |", "|---|---|"]
    for n in noms_phase1 + ["JUGE"]:
        if n in results:
            lignes.append(f"| {n} | **{extraire_verdict(results[n][0])}** |")
    lignes.append("")
    (out / "SYNTHESE.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("\n" + "\n".join(lignes))
    print(f"\nArchive : {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
