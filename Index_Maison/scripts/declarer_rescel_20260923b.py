#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DÉCLARER + RE-SCELLER — 2e VAGUE DU 23/09/2026 (règle d'or #5 : un scellé ne s'écrase
JAMAIS en silence ; leçon E22 : j'ai touché un fichier scellé SANS le déclarer le jour même).

CE QUI S'EST PASSÉ (mesuré, pas supposé)
----------------------------------------
La veilleuse a crié, à raison : « INTRUSION — Modification non déclarée :
hulk-mexc/scripts/satellite_aspiration.py ». Le drill est passé en **TROU** (R5 + R13
violées). Deux fichiers scellés divergent du registre, et UN instrument neuf n'y est pas :

  1. hulk-mexc/scripts/satellite_aspiration.py     — ECART (sonde WS en ombre, GO 1)
  2. hulk-mexc/scripts/verif_seuil_moteur.py       — ECART (correctif E23)
  3. hulk-mexc/scripts/ws_book.py                  — HORS REGISTRE (instrument neuf)

Cet outil fait l'acte prévu par la maison : BACKUP du registre, mise à jour du md5,
AJOUT du nouveau, et — surtout — une déclaration `_rescel_20260923b` qui dit CE QUI a
changé et POURQUOI. Lecture seule sur le moteur ; n'écrit que le registre (avec backup).
"""
import hashlib
import json
import os
import shutil
import time
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent          # ace777-test-day1
REG = RACINE / "Index_Maison" / "strategie" / "REGISTRE_SYNAPSES.json"

DECLARATIONS = {
    "hulk-mexc/scripts/satellite_aspiration.py": (
        "GO 1 (23/09/2026, ordre Christophe « pourquoi pas les deux ? ») : le satellite "
        "SONDE désormais le flux WebSocket public MEXC EN OMBRE pour les 20 paires et écrit "
        "des champs `ws_*` À CÔTÉ des valeurs REST (ws_prix, ws_age_ms, ws_spread_bps, "
        "ws_chute_pct_s, ws_ombre). LE MOTEUR N'EST PAS TOUCHÉ : il lit toujours le REST ; "
        "le mode ombre MESURE l'écart REST vs flux avant toute bascule. MESURÉ : ws_ombre "
        "20/20 paires · écart médian REST vs flux 0,1456 % (≈ 15 bps, soit un spread de "
        "retard) · âge du flux 0,35 s. FAUTE RÉVÉLÉE ET CORRIGÉE PAR CETTE MODIF (classe "
        "E22) : `aspiration_live.json` était écrit AVANT le bloc → la mesure était faite "
        "puis JETÉE (le champ n'apparaissait jamais) ; corrigé par une réécriture atomique "
        "APRÈS le bloc. LECTURE SEULE sur le moteur : aucune décision, aucun seuil, aucune "
        "porte, aucun ordre modifié. Réversible en retirant le bloc `ws_*`. "
        "-- DÉFAUT DE PROCESSUS DÉCLARÉ (E22) : cette modification a été faite APRÈS le "
        "scellé et N'A PAS ÉTÉ DÉCLARÉE le jour même → veilleuse INTRUSION + drill TROU "
        "(R5 + R13 violées). C'est la faute que ce re-scellement répare et que le registre "
        "E22 consigne."
    ),
    "hulk-mexc/scripts/verif_seuil_moteur.py": (
        "CORRECTIF E23 (23/09/2026) — CE GARDIEN ACCUSAIT LE MOTEUR À TORT. Il recalculait "
        "le seuil d'entrée SANS le terme `impulse_pullback_min_pct` DU PROFIL PAR PAIRE "
        "(paper_diprip.score_pair l.649 : `_cal.get(\"impulse_pullback_min_pct\", "
        "cfg.get(\"IMPULSE_PULLBACK_MIN_PCT\", \"5\"))`) — il n'utilisait que le plancher "
        "GLOBAL (5,0). CONSÉQUENCE MESURÉE : sur BTCUSDT (profil dip_pct 2,0 · "
        "impulse_pullback_min_pct 1,5) il annonçait « écrit 1.70 % · recalculé 4.25 % — "
        "DÉSACCORD », alors que LE MOTEUR AVAIT RAISON (seuil réel = max(2,0 ; 1,5 ; "
        "0,30×m6) × 0,85 = 1,70 %, exactement ce que le moteur avait écrit). Un gardien qui "
        "accuse à tort le moteur est une FAUSSE ALARME (R14), pire qu'aucun gardien. "
        "CORRECTIF : lecture du terme PROFIL + autotest enrichi d'un point « BTC réel » ; "
        "l'autotest savait aussi injecter un profil SYNTHÉTIQUE (champ `cal`), sinon il ne "
        "pouvait PAS prouver la détection. RÉSULTAT MESURÉ APRÈS CORRECTIF : invariant "
        "24/24 conformes (avant 23/24) · autotest 12/12 erreurs discriminantes détectées "
        "(avant 8/12 — le gardien se déclarait CASSÉ). Aucune décision moteur touchée : "
        "outil de contrôle, lecture seule."
    ),
}

NOUVEAUX = {
    "hulk-mexc/scripts/ws_book.py": {
        "role": "Décodeur du flux WebSocket public MEXC (protobuf bookTicker) : prix FRAIS "
                "et CHUTE mesurée sur la frise des trames, sans attendre 0,5 s.",
        "origine": "GO 1+2 (23/09/2026, ordre Christophe). Mesure : 14 ms de latence médiane "
                   "contre 1058 ms en REST. Lecture seule, aucun ordre.",
    },
}

# Auto-scellement : cet outil se déclare LUI-MÊME au registre, sinon il serait « hors
# registre » dès sa création (règle d'or #6 : 0 hors repo).
SELF = "Index_Maison/scripts/declarer_rescel_20260923b.py"


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def main():
    reg = json.load(open(REG, encoding="utf-8"))
    backup = REG.with_name(REG.name + ".bak_declare_b_%s" % time.strftime("%H%M%S"))
    shutil.copy2(REG, backup)
    print(f"backup : {backup.name}")
    faits = 0
    for nom, declaration in DECLARATIONS.items():
        cible = RACINE / nom
        if not cible.exists():
            print(f"  [SKIP] absent : {nom}")
            continue
        actuel = md5(cible)
        for it in reg["fichier"]:
            if str(it.get("nom")) == nom:
                avant = it.get("md5")
                if avant == actuel:
                    print(f"  [=] {nom} déjà conforme")
                    break
                it["md5"] = actuel
                it["date"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
                it["_rescel_20260923b"] = declaration
                print(f"  [OK] {nom}\n       {avant} → {actuel}")
                faits += 1
                break
        else:
            print(f"  [ABSENT DU REGISTRE] {nom}")
    # 2) AJOUT des nouveaux instruments
    noms = {str(i.get("nom")) for i in reg["fichier"]}
    for nom, meta in list(NOUVEAUX.items()) + [(SELF, {
            "role": "Acte de déclaration + re-scellement (2e vague 23/09) — outil de "
                    "maintenance, il DÉCLARE au lieu d'écraser.",
            "origine": "Règle d'or #5. Déclare satellite_aspiration.py, verif_seuil_moteur.py "
                       "et ajoute ws_book.py."})]:
        cible = RACINE / nom
        if nom in noms:
            print(f"  [=] déjà au registre : {nom}")
            continue
        if not cible.exists():
            print(f"  [SKIP] absent : {nom}")
            continue
        reg["fichier"].append({"nom": nom, "role": meta["role"], "origine": meta["origine"],
                               "verif": "md5", "auto_modifiable": False,
                               "md5": md5(cible),
                               "date": time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime()),
                               "_ajout_20260923b": "Instrument créé le 23/09/2026 (GO "
                                                   "Christophe) — ajouté au registre le jour "
                                                   "même pour qu'il soit VU (veilleuse, drill)."})
        print(f"  [+] AJOUTÉ : {nom}")
    reg["updated"] = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    tmp = REG.with_suffix(".json.tmp")
    json.dump(reg, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    os.replace(tmp, REG)
    print(f"\n{faits} scellé(s) re-déclaré(s) · registre réécrit ({len(reg['fichier'])} entrées)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
