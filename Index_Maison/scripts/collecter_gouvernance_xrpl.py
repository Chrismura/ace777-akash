#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""collecter_gouvernance_xrpl.py — RADAR GOUVERNANCE XRPL, collecteur PASSIF (P-XRPL-1).

═════════════════════════════════════════════════════════════════════════
SPÉCIFICATION FIGÉE AVANT LE PREMIER CYCLE (GO Christophe 13/09 « GO
collecteur passif gouvernance XRPL (7 jours, verdict J+8, 0 €) » + ajout
demandé le même jour : SUIVI DES FEATURES DÉSACTIVÉES APRÈS BUG).
Protocole identique au radar RWA : capter, ne rien alerter, verdict à J+8.
═════════════════════════════════════════════════════════════════════════
SOURCE (figée) : https://api.xrpscan.com/api/v1/amendments — 1 appel/h,
public, gratuit. Champs bruts conservés SANS interprétation (règle C3).

CE QUE LE COLLECTEUR FAIT (passif, zéro alerte) :
  1. SNAPSHOT horaire : la liste complète des amendements (110 aujourd'hui)
     écrite en JSONL append-only : data/xrpl_gouv_snapshots.jsonl
  2. MOUVEMENTS : delta de `count` par amendement vs snapshot précédent ;
     bascules enabled False→True (= ACTIVATION, l'événement majeur) ;
     approche du seuil (count − threshold).
  3. CIMETIÈRE (le suivi demandé le 13/09) : les features tuées après bug
     restent dans l'API avec des compteurs mourants, et leurs remplaçantes
     portent le suffixe V1_1. Le collecteur trace :
       - les paires (ancienne, remplaçante V1_1) connues : Batch→BatchV1_1,
         PermissionDelegation→PermissionDelegationV1_1,
         NonFungibleTokensV1→NonFungibleTokensV1_1,
         CryptoConditionsSuite→CryptoConditions
       - les NOUVELLES morts potentielles : un amendement watchlist dont
         `supported` passe à False, ou l'apparition d'un suffixe V1_1/V1_2
         pour un nom déjà connu (signal de remplacement post-incident).
  4. ÉTAT pour le chien : thermo/xrpl_gouv_etat.json (produit frais 1 h).

WATCHLIST institutionnelle (figée, 13) : LendingProtocol (XLS-66),
SingleAssetVault (XLS-65), BatchV1_1 (XLS-56), PermissionDelegationV1_1
(XLS-75), ConfidentialTransfer (XLS-96), DynamicMPT (XLS-94),
PermissionedDEX (XLS-81), PermissionedDomains (XLS-80), MPTokensV1
(XLS-33), Credentials (XLS-70), Sponsor (XLS-68), XChainBridge (XLS-38),
AMM (XLS-30).

CRITÈRE DE VERDICT J+8 — PRÉ-ENREGISTRÉ (écrit avant toute donnée) :
  SUCCÈS si, sur les 7 jours, AU MOINS UN de :
    a) ≥ 5 amendements de la watchlist gagnent ou perdent ≥ +2 validations
       (delta count cumulé sur la fenêtre) ;
    b) ≥ 1 bascule enabled (activation) dans la watchlist ;
    c) ≥ 1 événement cimetière nouveau (V1_1 qui apparaît, ou supported→False).
  ÉCHEC sinon = les votes sont figés → le radar n'a pas de signal à vendre,
  on arrête (même discipline que le radar RWA). Pas de deuxième essai.

ROBUSTESSE (leçons du 13/09, sniffer + V2) : 4 essais API avec backoff,
échec = cycle sauté HONNÊTEMENT (état marked api_ko), jamais de donnée
inventée. Zéro écriture hors data/ et thermo/. Zéro alerte. 0 €.

Usage : python3 collecter_gouvernance_xrpl.py           # 1 cycle
        python3 collecter_gouvernance_xrpl.py --status  # tableau de bord
"""
import argparse
import json
import time
import urllib.request
from typing import Optional
from datetime import datetime, timezone
from pathlib import Path

MAISON = Path.home() / "ace777-test-day1" / "Index_Maison"
DATA = MAISON / "data"
THERMO = MAISON / "thermo"
SNAP_JSONL = DATA / "xrpl_gouv_snapshots.jsonl"
ETAT = THERMO / "xrpl_gouv_etat.json"
API = "https://api.xrpscan.com/api/v1/amendments"

WATCHLIST = {
    "LendingProtocol": "XLS-66", "SingleAssetVault": "XLS-65",
    "BatchV1_1": "XLS-56", "PermissionDelegationV1_1": "XLS-75",
    "ConfidentialTransfer": "XLS-96", "DynamicMPT": "XLS-94",
    "PermissionedDEX": "XLS-81", "PermissionedDomains": "XLS-80",
    "MPTokensV1": "XLS-33", "Credentials": "XLS-70",
    "Sponsor": "XLS-68", "XChainBridge": "XLS-38", "AMM": "XLS-30",
}
# CIMETIÈRE connu au 13/09 (figé) : ancienne → remplaçante (motif post-bug)
CIMETIERE = {
    "Batch": "BatchV1_1",
    "PermissionDelegation": "PermissionDelegationV1_1",
    "NonFungibleTokensV1": "NonFungibleTokensV1_1",
    "CryptoConditionsSuite": "CryptoConditions",
}

def log(m): print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] {m}", flush=True)

def fetch_amendments() -> list:
    """4 essais avec backoff (leçon sniffer 13/09) — sinon exception honnête."""
    last = None
    for attempt in range(1, 5):
        try:
            req = urllib.request.Request(API, headers={"User-Agent": "ace777-radar-gouvernance/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except Exception as e:
            last = e
            log(f"  essai {attempt}/4 échoué : {e} — backoff {2**attempt}s")
            time.sleep(2 ** attempt)
    raise RuntimeError(f"API injoignable après 4 essais : {last}")

def charger_dernier_snapshot() -> Optional[dict]:
    if not SNAP_JSONL.exists():
        return None
    lignes = [l for l in SNAP_JSONL.read_text().splitlines() if l.strip()]
    return json.loads(lignes[-1]) if lignes else None

def cycle() -> None:
    DATA.mkdir(exist_ok=True)
    THERMO.mkdir(exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    rows = fetch_amendments()
    par_nom = {r.get("name"): r for r in rows}

    # 1) SNAPSHOT (bruts, append-only)
    snap = {"ts": ts, "n_amendements": len(rows), "validations": max((r.get("validations") or 0) for r in rows),
            "amendements": [{"name": r.get("name"), "xls": r.get("xls"), "enabled": r.get("enabled"),
                             "supported": r.get("supported"), "count": r.get("count"),
                             "threshold": r.get("threshold"), "majority": r.get("majority"),
                             "validations": r.get("validations")} for r in rows]}
    with SNAP_JSONL.open("a") as f:
        f.write(json.dumps(snap, ensure_ascii=False) + "\n")

    # 2) MOUVEMENTS vs précédent
    prec = charger_dernier_snapshot()
    # (le dernier snapshot est celui qu'on vient d'écrire → le précédent est l'avant-dernier)
    lignes = [l for l in SNAP_JSONL.read_text().splitlines() if l.strip()]
    if len(lignes) >= 2:
        prec = json.loads(lignes[-2])
    deltas, bascules = {}, []
    if prec:
        avant = {a["name"]: a for a in prec["amendements"]}
        for nom, w_xls in WATCHLIST.items():
            actuel = par_nom.get(nom)
            ancien = avant.get(nom)
            if not actuel:
                continue
            c_now, c_old = (actuel.get("count") or 0), ((ancien or {}).get("count") or 0)
            if c_now != c_old:
                deltas[nom] = {"de": c_old, "a": c_now, "delta": c_now - c_old}
            e_now, e_old = bool(actuel.get("enabled")), bool((ancien or {}).get("enabled"))
            if e_now and not e_old:
                bascules.append({"name": nom, "xls": w_xls, "ts": ts, "evenement": "ACTIVATION"})

    # 3) CIMETIÈRE — suivi des morts après bug (demandé 13/09)
    cimetiere_etat = {}
    for mort, remplaçante in CIMETIERE.items():
        m, r = par_nom.get(mort), par_nom.get(remplaçante)
        cimetiere_etat[mort] = {
            "compte_mort": (m or {}).get("count"), "enabled_mort": bool((m or {}).get("enabled")),
            "remplacante": remplaçante,
            "compte_remplacante": (r or {}).get("count"), "enabled_remplacante": bool((r or {}).get("enabled")),
        }
    # nouveaux remplacements possibles : suffixe V1_1/V1_2 sur un nom connu non tracké
    nouveaux_remp = [r.get("name") for r in rows
                     if r.get("name") and ("V1_1" in r["name"] or "V1_2" in r["name"])
                     and r["name"] not in CIMETIERE.values() and r["name"] not in WATCHLIST]

    # 4) ÉTAT chien + tableau de bord
    watch_rows = []
    for nom, xls in WATCHLIST.items():
        a = par_nom.get(nom)
        if not a:
            watch_rows.append({"name": nom, "xls": xls, "absent_api": True}); continue
        c, th, v = a.get("count") or 0, a.get("threshold") or 28, a.get("validations") or 35
        watch_rows.append({"name": nom, "xls": xls, "enabled": bool(a.get("enabled")),
                           "count": c, "threshold": th, "pct_validations": round(c / v * 100, 1),
                           "manquants_pour_passer": max(0, th - c)})
    etat = {"ts": ts, "organe": "xrpl-gouvernance",
            "role": "radar passif gouvernance XRPL — AUCUNE alerte (P-XRPL-1, GO 13/09)",
            "n_amendements": len(rows), "watchlist": watch_rows,
            "mouvements_dernier_cycle": deltas, "bascules": bascules,
            "cimetiere": cimetiere_etat, "nouveaux_remplacements_v1x": nouveaux_remp,
            "n_snapshots": len(lignes),
            "critere_j8": "succes si (a) >=5 watchlist |delta|>=2 OU (b) >=1 activation OU (c) >=1 mort nouvelle ; sinon echec"}
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1))
    actifs = [w["name"] for w in watch_rows if w.get("enabled")]
    log(f"snapshot #{len(lignes)} écrit · {len(rows)} amendements · watchlist {len(watch_rows)} · mouvements: {len(deltas)} · bascules: {len(bascules)}")
    log(f"activés en watchlist : {', '.join(actifs) if actifs else 'aucun'}")

def status() -> None:
    if not ETAT.exists():
        print("aucun état — jamais tourné"); return
    e = json.loads(ETAT.read_text())
    print(f"== RADAR GOUVERNANCE XRPL · snapshot #{e['n_snapshots']} · {e['ts'][:16]} ==")
    print(f"{'amendement':30s} {'xls':9s} {'statut':8s} {'count':>5}  {'%val':>5}  manquants")
    for w in e["watchlist"]:
        if w.get("absent_api"):
            print(f"{w['name']:30s} {w['xls']:9s} ABSENT"); continue
        st = "ACTIVÉ" if w["enabled"] else "en vote"
        print(f"{w['name']:30s} {w['xls']:9s} {st:8s} {w['count']:>5}  {w['pct_validations']:>4}%  {w['manquants_pour_passer']}")
    print("\n— cimetière (morts après bug, le suivi demandé) —")
    for mort, c in e["cimetiere"].items():
        print(f"  {mort:26s} (count {c['compte_mort']}) → {c['remplacante']:26s} (count {c['compte_remplacante']}, {'ACTIVÉE' if c['enabled_remplacante'] else 'en vote'})")
    if e["nouveaux_remplacements_v1x"]:
        print("\n— NOUVEAUX remplacements V1x détectés —")
        for n in e["nouveaux_remplacements_v1x"]: print("  ·", n)
    if e["mouvements_dernier_cycle"]:
        print("\n— mouvements du dernier cycle —")
        for nom, d in e["mouvements_dernier_cycle"].items():
            print(f"  {nom:30s} {d['de']} → {d['a']} ({d['delta']:+d})")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    status() if a.status else cycle()
