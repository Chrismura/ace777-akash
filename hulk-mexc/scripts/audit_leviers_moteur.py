#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDIT_LEVIERS_MOTEUR.py — « comment savoir ce que je n'ai pas vu ».

Principe (règle d'or #8, appliquée à la plus-value) :
    un levier non mesuré est une bombe, pas un levier.
Donc on ne cherche pas les angles morts à l'intuition : on CROISE la config du
moteur avec l'appareil de mesure. 0 €, lecture seule, aucun ordre.

Deux définitions STRICTES (sinon l'audit ment) :
  - MESURÉ : le paramètre est cité dans un script qui CALCULE un P&L
    (le fichier contient « pnl » ou « net » ou « chiffr » et n'est pas le moteur).
    Un simple commentaire ne compte pas.
  - LEVIER MONÉTAIRE : le paramètre change la TAILLE, la SORTIE, l'ENTRÉE ou le
    COMPOUNDING — c'est-à-dire qu'il multiplie le résultat. Le reste (sondes,
    cadences, plomberie) ne multiplie pas l'argent : classé « hors périmètre ».

Sortie = LA CARTE DES TROUS : les leviers monétaires jamais chiffrés.
Chacun est une question sans réponse chiffrée = un candidat de plus-value.
"""
import os
import re
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # hulk-mexc/
RACINE = os.path.dirname(BASE)                                       # ace777-test-day1/
DEFAUTS = os.path.join(BASE, "config", "defaults.env")
MOTEUR = os.path.join(BASE, "scripts", "paper_diprip.py")

NOM_MESURE = re.compile(r"(chiffrage|replay|banc|audit|radiographie|carte|"
                        r"monte_carlo|scorecard)", re.I)
CONTENU_MESURE = re.compile(r"(pnl|net_s|net_|chiffr|profit|ecart)", re.I)

# leviers qui MULTIPLIENT le résultat (les seuls qui comptent pour la plus-value)
MONETAIRES = [
    ("TAILLE / SIZING", ("NOTIONAL", "TIER", "STAKE", "SEED_USDT", "SEED_MODE",
                         "SEED_MAX_PAIRS", "SEED_ON")),
    ("COMPOUNDING", ("COMPOUND",)),
    ("SORTIE", ("RIP_", "STOP_", "SELL_", "BAG_CRASH", "BAG_SLOW", "BAG_DCA",
                "BAG_POSITION", "BAG_NO_TECH", "DUST_SWEEP")),
    ("ENTRÉE", ("ENTREE", "DIP", "IMPULSE", "COOLING", "REENTRY", "PLANCHER",
                "VOL_SPIKE", "VOL_HOT", "VOL_OK", "VOL_DRY", "SPIKE_15D",
                "QUIET_RANGE", "BUY_SPREAD", "SENSE_STRICT")),
    ("LIQUIDITÉ / MURS", ("WALL_", "SLIP_", "FUSIBLE", "ASPIRATION_MIN")),
    ("CADENCE / RYTHME", ("CADENCE", "POLL_SEC", "SCORE_EVERY", "VOL_SMALL")),
]


def categorie(k: str):
    for nom, prefixes in MONETAIRES:
        for p in prefixes:
            if k.startswith(p):
                return nom
    return None


def lire_params() -> list:
    out = []
    with open(DEFAUTS, encoding="utf-8", errors="ignore") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#") or "=" not in ligne:
                continue
            k, v = ligne.split("=", 1)
            out.append((k.strip(), v.strip()))
    return out


def scripts_mesure() -> list:
    """Scripts qui CALCULENT un P&L (pas seulement un fichier au nom qui ressemble)."""
    out = []
    for racine, _, fichiers in os.walk(RACINE):
        if "/.git" in racine or "OUTBOX" in racine or "historique" in racine:
            continue
        for f in fichiers:
            if not f.endswith(".py") or not NOM_MESURE.search(f):
                continue
            p = os.path.join(racine, f)
            if os.path.abspath(p) == os.path.abspath(MOTEUR):
                continue
            try:
                t = open(p, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            if CONTENU_MESURE.search(t):
                out.append(p)
    return out


def main():
    params = lire_params()
    mesures = scripts_mesure()
    corpus = "\n".join(open(p, encoding="utf-8", errors="ignore").read()
                       for p in mesures)
    moteur = open(MOTEUR, encoding="utf-8", errors="ignore").read()

    print(f"AUDIT DES LEVIERS DU MOTEUR — {len(params)} paramètres dans defaults.env")
    print(f"scripts qui CALCULENT un P&L (appareil de mesure) : {len(mesures)}")
    for p in mesures:
        print(f"   · {os.path.relpath(p, RACINE)}")
    print()

    trous, chiffres, morts, hors = defaultdict(list), defaultdict(list), [], []
    for k, v in params:
        motif = r"\b" + re.escape(k) + r"\b"
        dans_moteur = re.search(motif, moteur) is not None
        dans_mesure = re.search(motif, corpus) is not None
        cat = categorie(k)
        if not dans_moteur:
            morts.append((k, v, cat))
        elif cat is None:
            hors.append((k, v))
        elif dans_mesure:
            chiffres[cat].append((k, v))
        else:
            trous[cat].append((k, v))

    n_trous = sum(len(x) for x in trous.values())
    n_ch = sum(len(x) for x in chiffres.values())
    print("=" * 74)
    print(f"LEVIERS MONÉTAIRES : {n_ch} chiffrés · {n_trous} AVEUGLES")
    print("=" * 74)
    for nom, _ in MONETAIRES:
        t, c = trous.get(nom, []), chiffres.get(nom, [])
        print(f"\n[{nom}]  {len(t)} aveugle(s) / {len(t) + len(c)} leviers")
        for k, v in t:
            print(f"   ✗ AVEUGLE  {k:32s} = {v}")
        for k, v in c:
            print(f"   ✓ chiffré  {k:32s} = {v}")

    if morts:
        print("\n" + "=" * 74)
        print("PARAMÈTRES JAMAIS LUS PAR LE MOTEUR (règle #15 : brancher ou retirer)")
        print("=" * 74)
        for k, v, cat in morts:
            print(f"   {k:34s} = {v:>14s}   [{cat or 'hors périmètre'}]")

    print("\n--- LECTURE (à ne pas sauter) ---")
    print("  LIMITES ÉCRITES : (a) « lu par le moteur » = scripts/paper_diprip.py")
    print("  uniquement — un satellite peut lire un paramètre sans que ça se voie ici ;")
    print("  (b) le critère de mesure est NOMINATIF : un levier mesuré par sa VALEUR")
    print("  (ex. le +2 % de sortie) n'apparaît pas comme chiffré.")
    print("  Un levier monétaire AVEUGLE = une décision prise sans mesure.")
    print("  Priorité : TAILLE et SORTIE (ils multiplient tout le reste).")
    print(f"  Hors périmètre plus-value (sondes, plomberie) : {len(hors)} paramètres —")
    print("  ils ne sont pas comptés comme trous, mais restent mesurés nulle part.")


if __name__ == "__main__":
    main()
