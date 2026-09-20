#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""collecter_rwa_yields.py — COLLECTEUR PASSIF RWA (prototype 7 jours).

GO Christophe 11/09 (dossier DOSSIER_FAMILLE_RADAR_RWA_VOTE_20260911.md).
Un seul rôle : noter les rendements des pools de crédit privé tokenisé
(DefiLlama) dans un historique JSONL. AUCUNE alerte, AUCUN moteur,
AUCUN cockpit en phase 1. Le verdict J+8 se prendra sur le critère
pré-enregistré : >= 3 pools du top 20 TVL bougent de >= 50 bps en 7 jours.

Correctifs validés intégrés :
  [C1] endpoint https://yields.llama.fi/pools (1 requête = snapshot complet)
  [C3] champs BRUTS conservés sans interprétation
  [C4] n'écrit JAMAIS dans alarme.json (circuit des sirènes interdit phase 1)
  [C5] produit ajouté à rotation_jsonl.py (leçon journal_radar.log 3,3 Go)
  [C6] anti-figage : hash du payload identique 3 cycles consécutifs = flag
       (pas de sirène : le flag vit dans l'état + le journal, règle [C4])

Sorties :
  Index_Maison/data/rwa_yields_hist.jsonl   (1 ligne par pool par cycle, brut)
  Index_Maison/data/rwa_yields_etat.json    (état : dernier ts, hash, figage)

Usage : python3 collecter_rwa_yields.py        (cette cadence : plist 6 h)
Stdlib uniquement, zéro clé API, zéro écriture hors data/.
"""
import json
import os
import hashlib
import urllib.request
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1/Index_Maison"
HISTO = os.path.join(ROOT, "data", "rwa_yields_hist.jsonl")
ETAT = os.path.join(ROOT, "data", "rwa_yields_etat.json")
URL = "https://yields.llama.fi/pools"
UA = {"User-Agent": "ACE777-rwa-prototype/1.0 (GO Christophe 2026-09-11)"}

# Filtre candidats crédit privé / RWA (à raffiner à l'analyse J+8, jamais maintenant)
MOTS_CLES = (
    "maple", "goldfinch", "centrifuge", "kamino", "truefi", "credix",
    "figure", "untangled", "homec", "tangible", "landshare", "parcl",
    "jigsaw", "credit", "rwa", "private", "pareto",
)

SEUIL_FIGAGE = 3  # [C6] hash identique 3 cycles consécutifs


def ecrire_atomique(chemin, texte):
    tmp = chemin + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(texte)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, chemin)


def charger_etat():
    try:
        with open(ETAT, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"fige_consecutifs": 0}


def main():
    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # [C1] une requête, timeout large, un seul retry doux (jamais de boucle)
    data = None
    for tentative in (1, 2):
        try:
            req = urllib.request.Request(URL, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.loads(r.read())
            break
        except Exception as e:
            print(f"[rwa_yields] tentative {tentative} échouée : {e}")
            if tentative == 2:
                raise SystemExit(1)

    pools = data.get("data", data) if isinstance(data, dict) else data

    # [C3] filtre candidats mais champs BRUTS stockés (aucune transformation)
    candidats = [
        p for p in pools
        if any(m in str(p.get("project", "")).lower()
               or m in str(p.get("symbol", "")).lower() for m in MOTS_CLES)
    ]

    # [C6] hash du payload figé sur (pool_id, apy, tvl) triés — contenu, pas métadonnées
    empreinte_src = json.dumps(
        sorted([str(p.get("pool")), p.get("apy"), p.get("tvlUsd")] for p in candidats),
        separators=(",", ":"),
    )
    md5_payload = hashlib.md5(empreinte_src.encode()).hexdigest()

    etat = charger_etat()
    if md5_payload == etat.get("md5_payload"):
        etat["fige_consecutifs"] = etat.get("fige_consecutifs", 0) + 1
    else:
        etat["fige_consecutifs"] = 0
    fige = etat["fige_consecutifs"] >= SEUIL_FIGAGE

    # [C5] append par pool : greppable, rotation gérée par rotation_jsonl.py
    with open(HISTO, "a", encoding="utf-8") as f:
        for p in candidats:
            f.write(json.dumps({
                "ts": maintenant,
                "payload_md5": md5_payload,
                "raw": p,
            }, separators=(",", ":"), ensure_ascii=False) + "\n")

    etat.update({
        "dernier_ts": maintenant,
        "nb_pools_total": len(pools),
        "nb_pools_candidats": len(candidats),
        "md5_payload": md5_payload,
        "alerte_figee": fige,  # [C6] flag lu à l'analyse J+8 ; pas de sirène [C4]
    })
    ecrire_atomique(ETAT, json.dumps(etat, ensure_ascii=False, indent=1))

    print(f"[rwa_yields] {maintenant} — {len(candidats)}/{len(pools)} pools notés "
          f"(md5 {md5_payload[:8]}…, fige {etat['fige_consecutifs']}/{SEUIL_FIGAGE}"
          f"{' ⚠️ SOURCE FIGÉE' if fige else ''})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
