#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test comparatif codeurs du hub (14/08, demande Christophe : « y a-t-il un
meilleur codeur dans le hub / la file d'attente ? »).

Contexte : le task code.ia route vers puter-grok (grok-4.3) qui a HALLUCINE
2 livrables sur 3 (v1, v2 : variables/cles JSON inventees). Candidats en
reserve dans le hub : inferx-coder (Qwen3-Coder-Next, fallback officiel du
code.ia) et mistral (codestral-latest, specialiste code).

TACHE DE CONTROLE (le piege exact qui a fait echouer puter-grok) : recopier
EXACTEMENT des lignes bash donnees, sans rien inventer. On mesure la fidelite
litterale (0 = hallucination, 3 = parfait).
"""
import json
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"

TEST = """\
Tu es un codeur bash rigoureux. Recopie EXACTEMENT, sans rien modifier, sans
rien ajouter, sans commentaire, ces 3 lignes (une par ligne) :

  bid_px="$(as_num "$(json_get "$book_resp" "bidPrice")")"
  entry_price="$(as_num "$(json_get "$entry_resp" "avgPrice")")"
  px="$(as_num "$(json_get "$tick_resp" "price")")"
"""

CANDS = [
    ("inferx-coder (Qwen3-Coder-Next)", "inferx-coder"),
    ("mistral codestral-latest", "mistral"),
    ("puter-grok (actuel, temoin)", "puter-grok"),
    ("gemini-flash-lite (filet)", "gemini"),
]

EXPECTED = [
    'bid_px="$(as_num "$(json_get "$book_resp" "bidPrice")")"',
    'entry_price="$(as_num "$(json_get "$entry_resp" "avgPrice")")"',
    'px="$(as_num "$(json_get "$tick_resp" "price")")"',
]


def ask(provider, task="test.force.codeur"):
    # task NON routé volontairement : sinon la règle de tâche (puter-grok ->
    # inferx-coder -> gemini) écrase le champ model. Avec un task inconnu,
    # target_ids = [only_model] -> on force le provider exact.
    payload = {
        "task": task,
        "model": provider,
        "messages": [{"role": "user", "content": TEST}],
        "max_tokens": 300,
        "temperature": 0.0,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")
    except Exception as e:
        return f"[ERR] {str(e)[:150]}", "?"


def score(rep):
    if rep.startswith("[ERR]"):
        return -1, rep
    # normalise : on retire espaces/fences et on compte les lignes exactes
    lignes = [ln.strip() for ln in rep.splitlines() if ln.strip() and not ln.strip().startswith("```")]
    ok = sum(1 for e in EXPECTED if e in rep.replace("\r", ""))
    return ok, f"{ok}/3 lignes exactes (rep={len(lignes)} lignes)"


if __name__ == "__main__":
    print("=== TEST CODEURS ALTERNATIFS (tache de controle anti-hallucination) ===", flush=True)
    for nom, prov in CANDS:
        rep, routed = ask(prov)
        s, detail = score(rep)
        print(f"\n--- {nom} (routee vers: {routed}) : score {s} ---", flush=True)
        print(detail, flush=True)
        print(rep[:400], flush=True)
    print("\n[OK] fin du test", flush=True)
