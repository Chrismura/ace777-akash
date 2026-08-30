#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consulter_famille_hulk_verification_20260824.py — Vérif codeur avant passage Hulk (24/08, Buffy).

Question posée au codeur (via le hub, 1 appel) : Christophe veut passer Hulk
du paper au réel APRÈS 3 jours d'observation. Avant ça, on a fait 4 chantiers
le 24/08 — on demande au codeur de les VÉRIFIER (bugs, pièges, améliorations)
et de valider le plan des 3 jours d'observation.

Chantiers à vérifier :
  1. Tableau cockpit HULK : colonnes BAG LIVE + CASH + TOTAUX (départ vs live vs cash)
  2. Persistance coupures : paper_diprip.py --resume (reprend le dernier state)
  3. Cas RWA expliqué : vente seed 25% au rip 7% = stratégie, pas bug
  4. Observateur des murs : observer_murs.py (35 012 mesures, murs/spoofs/drops)

Usage : python3 consulter_famille_hulk_verification_20260824.py
Stdlib uniquement · 1 appel hub · écriture dans
  scripts/CONSULTATION_FAMILLE_HULK_VERIFICATION_20260824/
"""
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1/Index_Maison")
HULK = Path("/Users/christophe/ace777-test-day1/hulk-mexc")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT_DIR = Path(__file__).resolve().parent / "CONSULTATION_FAMILLE_HULK_VERIFICATION_20260824"

SYSTEM = (
    "Tu es le CODEUR SENIOR de la maison ACE777 (expert Python, trading paper MEXC, "
    "machines de trading). Christophe veut passer Hulk du PAPER au RÉEL après 3 jours "
    "d'observation. On a fait 4 chantiers le 24/08 avant ce passage — tu dois les "
    "VÉRIFIER comme un codeur qui relit avant mise en prod : bugs, pièges, cas limites, "
    "risques, et ce qui manque. Ton rôle est critique et honnête : tu signales ce qui "
    "peut casser, jamais de complaisance. Réponds en français, format structuré, factuel, "
    "concis (pas de storytelling)."
)

USER = """CONTEXTE RÉEL (24/08) :

ÉTAT HULK ACTUEL (paper MEXC, portefeuille séparé ACE) :
{mission}

MURS DE LIQUIDITÉ (observateur, 24/08) :
{murs}

LES 4 CHANTIERS FAITS AUJOURD'HUI (à vérifier) :

1. TABLEAU COCKPIT HULK — colonnes ajoutées au tableau « DU DÉPART » :
   CRYPTO · BAG AU DÉBUT (seedQty) · BAG LIVE (qty actuel + diff) · SI RIEN FAIT
   · RÉEL ($) · CASH + ligne TOTAL (sommes départ vs live + cash dispo walletReelCash).
   Question : y a-t-il un piège sur la sémantique seedQty vs qty (partial sells) ?

2. PERSISTANCE COUPURES — paper_diprip.py --resume :
   À chaque boot, le script re-seedait (nouveau state_path + seed_inventory/seed_bags)
   → perte des positions ouvertes. Ajouté : --resume + resume_state() qui recharge le
   dernier PAPER_V1_*_state.json (positions/bags/bag_dca/pair_cash/reentry/scores/pnl/
   trades), CSV + state_path restent NEUFS pour traçabilité. Watchdog relance avec
   --resume. Testé : reprise 14 positions + 14,46$ cash + pnl −0,54$ + 3 trades.
   Question : pièges du resume (paires qui ne sont plus dans la config ? seeds vs
   trades reprises ? cohérence scores au boot ? double-run si 2 instances ?)

3. CAS RWA (position seed 10$) : Hulk a vendu 25% au rip 7% (SELL_PARTIAL 23/08,
   1327/5310 qté) — c'est la stratégie rip scale-out programmée, PAS un bug.
   Christophe veut « vendre haut, racheter plus bas, gonfler le bag, sans jamais
   perdre les bags accumulés ». Question : est-ce que le rip scale-out actuel
   (palier 1 = 25%) est compatible avec « ne jamais perdre le bag accumulé » ?
   Risque si le prix ne re-descend pas (vente définitive) ?

4. OBSERVATEUR MURS — observer_murs.py : la sonde aspiration collecte wall_bid/ask
   depuis le 16/08 mais personne ne lisait les CSV. L'observateur agrège tout
   (35 012 mesures, 15 paires, 763 spoofs, 1 507 drops ≥15%/s) →
   runs/MURS_RAPPORT.md + runs/murs_observations.json. Top : XRP 82 777$ moy (606k
   max) · RWA 1 347$ (fins, 68 spoofs).
   Question : le rapport est-il exploitable pour décider ? Quoi ajouter ?

TA MISSION — RÉPONDS EN 4 PARTIES :
A. VERDICT PAR CHANTIER (1-4) : OK / À CORRIGER (quoi exactement) / RISQUE
B. LES 3 PIÈGES les plus dangereux pour le passage au RÉEL (classés par gravité)
C. CE QUI MANQUE avant le passage réel (checklist courte)
D. PLAN 3 JOURS : que valider chaque jour pendant l'observation ?

RÈGLES :
- Factuel, pas de complaisance. Cite les risques précis (fichiers, cas limites).
- Si un chantier est risqué, dis-le franchement.
- Format : listes nettes, actionnables."""


def lire(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception:
        return "(absent)"


def main() -> int:
    mission = lire(ROOT / "cockpit" / "mission.json")
    murs = lire(HULK / "runs" / "MURS_RAPPORT.md")
    # mission.json brut est lourd : on allège (mêmes clés utiles que le cockpit)
    try:
        m_obj = json.loads(mission)
        m_trim = {k: m_obj.get(k) for k in (
            "ts", "run", "comboPnl", "sessionSince", "thermo", "hulk") if k in m_obj}
        mission = json.dumps(m_trim, ensure_ascii=False)[:2500]
    except Exception:
        mission = mission[:2500]
    user = USER.format(mission=mission, murs=(murs or "(rapport absent)")[:1500])

    payload = json.dumps({
        "task": "analyse.profonde",
        "model": "nvidia",
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        "max_tokens": 3000,
        "temperature": 0.2,
    }).encode()

    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    print("[consultation] soumission au codeur (analyse.profonde)…", flush=True)
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    secs = round(time.time() - t0, 1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    rep = OUT_DIR / "REPONSE.md"
    rep.write_text(
        f"# VÉRIF CODEUR — PASSAGE HULK AU RÉEL — {now}\n"
        f"> provider : {provider} · {secs}s\n\n{content}\n",
        encoding="utf-8")
    (OUT_DIR / "contexte.json").write_text(
        json.dumps({"mission": mission, "murs": murs, "prompt_user": user},
                   ensure_ascii=False, indent=1),
        encoding="utf-8")
    print(f"[OK] provider={provider} ({secs}s) → {rep}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
