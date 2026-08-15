#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test comparatif codeurs gratuits — LE VRAI DIFF SPEC v3 (14/08).

Christophe : « cherche un autre model coder mieux que mistral toujours gratuit ».
Benchmarks web (juin 2026) : gpt-oss-120b:free et north-mini-code:free = top
free coding sur OpenRouter. Le hub a deja gpt-oss-20b:free et north-mini-code.
On teste sur la VRAIE tache : transformer les 10 lignes old->new de la SPEC v3
(le piege qui a fait halluciner puter-grok 2x). Score = lignes exactes produites.

Format : on donne 3 lignes AVANT (les plus representatives : 1600, 1734, 2142)
et on demande la transformation EXACTE. Mesure la fidelite litterale.
"""
import json
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"

TEST = """\
Tu es un codeur bash rigoureux. Transforme EXACTEMENT ces 3 lignes en
encapsulant CHAQUE helper ruby (as_num, json_get) dans safe_call, SANS rien
renommer (garde $book_resp, "bidPrice", "avgPrice", "price" tels quels).

LIGNE 1 (avant) :  bid_px="$(as_num "$(json_get "$book_resp" "bidPrice")")"
LIGNE 2 (avant) :  entry_price="$(as_num "$(json_get "$entry_resp" "avgPrice")")"
LIGNE 3 (avant) :  px="$(as_num "$(json_get "$tick_resp" "price")")"

Le helper safe_call est : safe_call() { local rc=0; "$@" 2>/dev/null || rc=$?; return 0; }
Transforme en : $("$(safe_call as_num "$(safe_call json_get ...)")" ...)

Reponds UNIQUEMENT avec les 3 lignes transformees, rien d'autre :
"""

EXPECTED = [
    'bid_px="$(safe_call as_num "$(safe_call json_get "$book_resp" "bidPrice")")"',
    'entry_price="$(safe_call as_num "$(safe_call json_get "$entry_resp" "avgPrice")")"',
    'px="$(safe_call as_num "$(safe_call json_get "$tick_resp" "price")")"',
]

# (nom, provider_id a forcer via model=)
CANDS = [
    ("codestral-latest (ref actuelle)", "mistral"),
    ("gpt-oss-20b:free (openrouter)", "openrouter-free"),
    ("north-mini-code:free (cohere)", "obs-1786688184"),
    ("puter-grok (temoin hallucinant)", "puter-grok"),
    ("gemini-flash-lite (filet)", "gemini"),
]


def ask(provider):
    payload = {
        "task": "test.force.codeur2",
        "model": provider,
        "messages": [{"role": "user", "content": TEST}],
        "max_tokens": 600,
        "temperature": 0.0,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=150) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")
    except Exception as e:
        return f"[ERR] {str(e)[:120]}", "?"


def score(rep):
    if rep.startswith("[ERR]"):
        return -1, rep[:100]
    # chaque ligne attendue doit apparaitre (avec ses espaces de tete normalises)
    ok = 0
    for e in EXPECTED:
        if e in rep.replace("\r", ""):
            ok += 1
    return ok, f"{ok}/3 transformees exactement"


if __name__ == "__main__":
    print("=== TEST CODEURS GRATUITS — VRAI DIFF SPEC v3 (safe_call) ===", flush=True)
    for nom, prov in CANDS:
        rep, routed = ask(prov)
        s, detail = score(rep)
        print(f"\n--- {nom} (routée vers: {routed}) : {s} ---", flush=True)
        print(detail, flush=True)
        print(rep[:500], flush=True)
    print("\n[OK] fin du test", flush=True)
