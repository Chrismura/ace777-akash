#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interroge CORTANA (task cortana.analyse) sur la comparaison de 2 setups ACE :
le setup GAGNANT (revenge qui encaisse, 13-15/08) vs le setup de la NUIT (revenge qui expire, 16-17/08).
Lui donne des morceaux de cycles RÉELS des 2 côtés et lui demande de trouver le pattern qui déconne.
"""
import json, os, time, urllib.request, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
IDENTITE = os.path.expanduser("~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md")

identite = open(IDENTITE).read() if os.path.exists(IDENTITE) else (
    "Tu es Cortana, analyste du cockpit ACE777. Tu parles écrit + voix (Vivienne). "
    "Tu réponds à toute question sur le marché et le cockpit.")

# Extraits réels (générés par extraction CSV — voir /tmp/extrait_vieux.txt et /tmp/extrait_nuit.txt)
EXTRAIT_VIEUX = open("/tmp/extrait_vieux.txt", encoding="utf-8").read() if os.path.exists("/tmp/extrait_vieux.txt") else "INDISPONIBLE"
EXTRAIT_NUIT = open("/tmp/extrait_nuit.txt", encoding="utf-8").read() if os.path.exists("/tmp/extrait_nuit.txt") else "INDISPONIBLE"

BRIEF = f"""TÂCHE (superviseur Buffy) — TROUVER LE PATTERN QUI DÉCONNE ENTRE 2 SETUPS ACE

CONTEXTE (moteur de trading testnet ACE777, duo SCOUT/BETA + HUNTER/ALPHA) :

Le HUNTER (ALPHA) encaisse en « revenge » : après une perte du SCOUT, il rentre avec une
taille 1.5× (size_note=hunter_revenge_1.5x) pour récupérer. C'est LUI qui faisait ~90% du PnL.

- SETUP GAGNANT (13-15/08) : revenge armé en permanence → 51-52 fills revenge par run,
  PnL ALPHA +8.61 à +28.26 USDT.
- SETUP DE LA NUIT (16/08 21:00 → 17/08 09:00, vient d'être arrêté) : un « fix » a été appliqué
  (FIX-LAST-LOSS : TTL revenge 120s + heartbeat). Résultat : 0 fill ALPHA, 0 revenge,
  46 « revenge_ttl_expired », PnL BETA −0.84, PnL ALPHA 0.

TA MISSION : comparer les 2 morceaux de cycles RÉELS ci-dessous et trouver le PATTERN précis
qui déconne dans le setup de la nuit. Pas de langue de bois : dis ce que tu vois.

───── MORCEAU 1 : SETUP GAGNANT (13-14/08) — revenge qui ENCAISSE ─────
{EXTRAIT_VIEUX}

───── MORCEAU 2 : SETUP DE LA NUIT (16-17/08) — revenge qui EXPIRE ─────
{EXTRAIT_NUIT}

QUESTIONS (réponds avec TON raisonnement, sans me faire plaisir) :
1. Quelle est la différence de COMPORTEMENT entre les 2 morceaux, ligne à ligne ?
2. Le « revenge_ttl_expired » de la nuit : à quel moment exact il apparaît ? Qu'est-ce qui
   bloque l'entrée juste avant (radar_block momentum_too_small / spread_too_wide / direction_unclear /
   tactic_mismatch / entry_error Margin insufficient) ? Est-ce le TTL qui expire ou le radar
   qui ne laisse jamais passer ?
3. Sur le setup gagnant, le revenge entre même quand le radar bloque des dizaines de cycles
   avant. Qu'est-ce qui a changé qui empêche ça maintenant ?
4. Ta recommandation concrète : quel setup reprendre (A : rollback complet revenge permanent,
   ou B : TTL 120s mais radar qui filtre) — et pourquoi ?

Sois précise, cite les lignes. Si tu ne sais pas, dis « je ne sais pas » — pas d'invention.
Format : 1) ton diagnostic, 2) les preuves dans les lignes, 3) ta reco."""


def ask():
    payload = json.dumps({
        "task": "cortana.analyse",
        "messages": [
            {"role": "system", "content": identite},
            {"role": "user", "content": BRIEF},
        ],
        "max_tokens": 2500, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    return content, d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    content, provider, dur = ask()
    out = os.path.join(ROOT, "CORTANA_COMPARAISON_SETUPS_REVENGE_20260817.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Réponse Cortana — comparaison setups revenge (provider {provider}, {dur}s)\n\n{content}\n")
    print(f"[OK] Réponse reçue ({provider}, {dur}s) — écrite {out}")
    print("=" * 60)
    print(content)
    print("=" * 60)


if __name__ == "__main__":
    main()
