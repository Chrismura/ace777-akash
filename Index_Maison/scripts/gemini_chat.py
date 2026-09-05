#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEMINI_CHAT.py — dialogue multi-rounds avec GEMINI (hub local 11435),
historique persistant entre les rounds (fenêtre complète conservée).

Usage :
  python3 gemini_chat.py --session NOM --round "message"     # envoie et garde l'historique
  python3 gemini_chat.py --session NOM --show                # affiche l'historique

Historique : Index_Maison/scripts/GEMINI_SESSION_<NOM>.json
Transcript : Index_Maison/scripts/GEMINI_SESSION_<NOM>.md
"""
import argparse, json, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

HUB = "http://127.0.0.1:11435/v1/chat/completions"
TASK = "gemini.analyse"
HERE = Path(__file__).resolve().parent

# Canon famille (même identité que consulter_famille.py)
FAMILLE = HERE.parent / "identity" / "prompts" / "famille.json"
_d = json.loads(FAMILLE.read_text(encoding="utf-8"))
_m = {m["nom"]: m for m in _d["membres"]}
SYSTEM = _m["GEMINI"]["prompt"] + "\n\n" + _d["clause"]

def ask(history, user_msg):
    msgs = history + [{"role": "user", "content": user_msg}]
    payload = json.dumps({
        "task": TASK,
        "messages": [{"role": "system", "content": SYSTEM}] + msgs,
        "max_tokens": 4000, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--session", required=True)
    ap.add_argument("--round", dest="msg")
    ap.add_argument("--round-file", dest="msg_file", help="message lu depuis un fichier (evite les problemes d'echappement)")
    ap.add_argument("--show", action="store_true")
    args = ap.parse_args()
    if args.msg_file:
        args.msg = Path(args.msg_file).read_text(encoding="utf-8")

    hist_p = HERE / f"GEMINI_SESSION_{args.session}.json"
    md_p   = HERE / f"GEMINI_SESSION_{args.session}.md"
    history = json.loads(hist_p.read_text(encoding="utf-8")) if hist_p.exists() else []

    if args.show:
        for i, m in enumerate(history):
            who = "GEMINI" if m["role"] == "assistant" else f"ROUND {i//2+1}"
            print(f"\n===== {who} =====\n{m['content']}")
        return 0
    if not args.msg:
        print("Rien à envoyer (--round ou --show)."); return 2

    answer, prov = ask(history, args.msg)
    now = datetime.now(timezone.utc).strftime("%H:%MZ")
    history += [{"role": "user", "content": args.msg}, {"role": "assistant", "content": answer}]
    hist_p.write_text(json.dumps(history, ensure_ascii=False, indent=1), encoding="utf-8")

    with open(md_p, "a", encoding="utf-8") as f:
        r = len(history)//2
        f.write(f"\n\n---\n## ROUND {r} — {now} ({prov})\n\n### MOI\n{args.msg}\n\n### GEMINI\n{answer}\n")
    print(f"===== GEMINI (round {r}, {prov}) =====\n{answer}")

if __name__ == "__main__":
    sys.exit(main())
