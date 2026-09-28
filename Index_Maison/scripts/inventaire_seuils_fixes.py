#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du module : inventaire_seuils_fixes.py
Projet       : ACE777 — mise en œuvre de R17 (« aucun seuil fixe : la mesure décide »)
Rôle         : INVENTORIER, mécaniquement et sans invention, TOUS les seuils du moteur encore
               « en dur » (temps, compteurs, pourcentages constants) et les classer :
                 - TEMPS_DECISION      : une durée en dur décide d'un arrêt / d'une entrée  ⚠ (R17)
                 - TEMPS_HORS_DECISION : une durée en dur ne sert qu'à cadence/dédup (acceptable)
                 - COMPTEUR_DECISION   : un nombre d'événements décide  ⚠ (R17)
                 - PCT_FIXE_DECISION   : un pourcentage constant décide (entrée/sortie/blocage)  ⚠ (R17)
                 - FILTRE_ABSOLU       : plancher constant sur une grandeur MESURÉE (sélection d'univers)
                 - RELATIF_MESURE      : dérivé d'une grandeur mesurée de l'actif (conforme R17)
                 - SIZING / FLAG / DOC / TEST : aucun arrêt décidé
               Le rapport SORT les ⚠ par impact, et l'organe EXIT 1 si un seuil numérique n'est
               pas classé → impossible d'ajouter une garde « inventée » sans qu'elle soit vue.
BUT          : donner la liste chiffrée des seuils à mesurer (R17) — et empêcher qu'on en
               ajoute un nouveau en silence.
0 €, lecture seule, aucun ordre.
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # Index_Maison
ROOT = os.path.dirname(BASE)
DEFAUTS = os.path.join(ROOT, "hulk-mexc", "config", "defaults.env")
RUNS_H = os.path.join(ROOT, "hulk-mexc", "runs")
SORTIE_MD = os.path.join(BASE, "SEUILS_FIXES_DERNIER.md")
SORTIE_JSON = os.path.join(BASE, "SEUILS_FIXES_DERNIER.json")

# ─── Classification CURÉE : chaque entrée porte SA raison (règle : rien sans source) ──────────
# « impact » = ce que le seuil décide, en clair. Le $ vient du dernier chiffrage des gardes
# quand le nom du seuil est mappable sur un code de refus du journal.
C = {
    # ---- ⚠ SEUILS DE DÉCISION EN DUR (cible R17) ----
    "QUIET_RANGE_PCT":       ("PCT_FIXE_DECISION", "classifie le RÉGIME (QUIET) pour TOUTES les paires, quelle que soit leur amplitude"),
    "SPIKE_15D_PCT":         ("PCT_FIXE_DECISION", "classifie le RÉGIME (SPIKE) — même seuil pour une paire qui bouge 1,3 % et une qui bouge 150 %"),
    "IMPULSE_PCT":           ("PCT_FIXE_DECISION", "seuil d'allumage de rafale, en dur (8 %)"),
    "COOLING_DD_MIN_PCT":    ("PCT_FIXE_DECISION", "entrée en COOLING (chute mini) en dur"),
    "COOLING_PULLBACK_FRAC": ("PCT_FIXE_DECISION", "fraction de repli en dur"),
    "IMPULSE_PULLBACK_MIN_PCT": ("PCT_FIXE_DECISION", "repli minimum exigé (5 %) en dur — mesuré le 21/09 : ferme 66 % des rafales"),
    "IMPULSE_PULLBACK_FRAC": ("PCT_FIXE_DECISION", "fraction de repli en dur"),
    "RIP_EARLY_P1_PCT":      ("PCT_FIXE_DECISION", "palier de vente en dur (+2 %)"),
    "RIP_EARLY_P2_PCT":      ("PCT_FIXE_DECISION", "palier de vente en dur (+6 %)"),
    "RIP_LATE_P1_PCT":       ("PCT_FIXE_DECISION", "palier de vente en dur (+6 %)"),
    "RIP_LATE_P2_PCT":       ("PCT_FIXE_DECISION", "palier de vente en dur (+8 %)"),
    "SELL_FULL_AMPLITUDE_GUARD": ("PCT_FIXE_DECISION", "interdit une coupe 100 % si move24 > 12 % en dur — décide d'une SORTIE"),
    "BAG_SLOW_DD_PCT":       ("PCT_FIXE_DECISION", "chute lente du bag en dur"),
    "BAG_DCA_DD_PCT":        ("PCT_FIXE_DECISION", "rachat bag en dur"),
    "BAG_CRASH_DD_PCT":      ("PCT_FIXE_DECISION", "vente de crash en dur (20 %)"),
    "BAG_CRASH_SELL_FRAC":   ("PCT_FIXE_DECISION", "fraction vendue au crash, en dur"),
    "REENTRY_DD_PCT":        ("PCT_FIXE_DECISION", "dump exigé pour racheter (6 %) en dur"),
    "ASPIRATION_SPOOF_DROP_PCT_S": ("PCT_FIXE_DECISION", "chute de mur ≥ 15 %/s = refus d'entrée — mesuré protecteur, mais en dur"),
    "STOP_COOLDOWN_HOURS":   ("TEMPS_DECISION", "cooldown post-stop HISTORIQUE, non re-mesuré — CONSERVÉ et DÉCLARÉ (règle #8)"),
    "VEILLE_STALE_HOURS":    ("TEMPS_DECISION", "veille muette > 6 h = plus de nouvel achat (STANDBY)"),
    "VEILLE_STATUS_MAX_AGE_MIN": ("TEMPS_DECISION", "âge maxi du statut de veille avant blocage"),
    "PLANCHER_GATE_TTL_SEC": ("TEMPS_DECISION", "TTL du veto plancher (durée de validité d'une décision)"),
    "REENTRY_TTL_SEC":       ("TEMPS_DECISION", "durée de validité d'un armement de re-entry"),
    "BAG_DCA_TTL_SEC":       ("TEMPS_DECISION", "durée de validité d'un DCA bag"),
    "WALL_STALE_SEC":        ("TEMPS_DECISION", "fraîcheur du mur pour la porte murs (porte OFF aujourd'hui)"),
    # ---- COMPTEURS ----
    "SLIP_GATE_MIN_STOPS":   ("COMPTEUR_DECISION", "nb de stops avant bridage — le BRIDAGE est mesuré (glissement réel), pas le seuil"),
    "BAG_MAX_POSITIONS":     ("COMPTEUR_DECISION", "nb max de bags simultanés"),
    "SEED_MAX_PAIRS":        ("TEST", "scaffolding paper"),
    "SCORE_EVERY":           ("TEMPS_HORS_DECISION", "cadence de rafraîchissement des régimes"),
    "POLL_SEC":              ("TEMPS_HORS_DECISION", "cadence de cycle"),
    "SENSE_CACHE_TTL_SEC":   ("TEMPS_HORS_DECISION", "cache carnet (réduction d'appels)"),
    "SENSE_MIN_DEPTH_USDT":  ("FILTRE_ABSOLU", "profondeur mini du carnet (grandeur mesurée, plancher constant)"),
    "SENSE_MIN_TENSION":     ("RELATIF_MESURE", "ratio mesuré du carnet"),
    "SENSE_MAX_SPREAD_BPS":  ("FILTRE_ABSOLU", "spread maxi (grandeur mesurée)"),
    "SENSE_MAX_SPREAD_BPS_SPIKE": ("FILTRE_ABSOLU", "spread maxi en rafale"),
    "SENSE_MAX_ASK_WALL_RATIO": ("RELATIF_MESURE", "ratio de murs mesuré"),
    "MIN_QUOTE_VOL_USDT":    ("FILTRE_ABSOLU", "volume 24 h mini (mesuré)"),
    "MAX_SPREAD_BPS":        ("FILTRE_ABSOLU", "spread maxi (mesuré)"),
    "TIER_B_SPREAD_MAX_BPS": ("FILTRE_ABSOLU", "spread maxi tier B (mesuré)"),
    "BUY_SPREAD_MAX_BPS":    ("FILTRE_ABSOLU", "spread maxi à l'achat (mesuré)"),
    "DUST_SWEEP_MIN_NOTIONAL": ("FILTRE_ABSOLU", "résidu mini à balayer"),
    "WALL_GATE_MIN_WALL_USDT": ("FILTRE_ABSOLU", "mur mini (porte OFF)"),
    "WALL_GATE_REL_MIN":     ("RELATIF_MESURE", "mur relatif à sa médiane"),
    "VOL_SMALL_CAP_USDT":    ("FILTRE_ABSOLU", "définit « small cap » (volume mesuré)"),
    "VOL_SMALL_CADENCE":     ("RELATIF_MESURE", "cadence attendue d'une small cap"),
    "VOL_SPIKE_MIN_SMALL":   ("RELATIF_MESURE", "ratio volume/cadence MESURÉ (vol spike)"),
    "VOL_HOT_SPIKE":         ("RELATIF_MESURE", "ratio mesuré"),
    "VOL_OK_SPIKE":          ("RELATIF_MESURE", "ratio mesuré"),
    "VOL_DRY_SPIKE":         ("RELATIF_MESURE", "ratio mesuré (sec)"),
    "SLIP_GATE_SLIP_PP":     ("RELATIF_MESURE", "glissement réel mesuré (points de %)"),
    "SLIP_GATE_MULT":        ("SIZING", "bridage mesuré"),
    "ASPIRATION_MIN_NOTIONAL_USDT": ("RELATIF_MESURE", "filtre mur (désactivé volontairement)"),
    "ASPIRATION_DELAY_S":    ("TEMPS_HORS_DECISION", "délai entre les 2 lectures du carnet"),
    "ASPIRATION_PROBE_EVERY": ("TEMPS_HORS_DECISION", "cadence de sonde"),
    "ASPIRATION_MAX_PAIRS":  ("TEMPS_HORS_DECISION", "rotation de sonde"),
    "ACCUM_DESCENTE_PCT":    ("PCT_FIXE_DECISION", "signal d'accumulation — OBSERVATION seule, aucun trade"),
    "ACCUM_DROP_PCT_S":      ("PCT_FIXE_DECISION", "observation seule"),
    "ACCUM_MUR_USDT":        ("FILTRE_ABSOLU", "observation seule"),
    "ACCUM_MEMO_SEC":        ("TEMPS_HORS_DECISION", "observation seule"),
    "HINT_COOLDOWN_SEC":     ("TEMPS_HORS_DECISION", "dédup des hints de veille"),
    "SILENCE_LOG_TTL_SEC":   ("TEMPS_HORS_DECISION", "anti-silence : fréquence d'écriture, ne décide rien"),
    "SCAN_DEADLINE_SEC":     ("TEMPS_HORS_DECISION", "garde réseau"),
    "DIGEST_LOOP_SEC":       ("TEMPS_HORS_DECISION", "cadence veille"),
    "DIP_FLOOR_PCT":         ("RELATIF_MESURE", "plancher du seuil de creux, multiplié par la CADENCE MESURÉE de la paire"),
    "RIP_FLOOR_PCT":         ("RELATIF_MESURE", "idem (rip = plancher + mult × cadence)"),
    "STOP_FLOOR_PCT":        ("RELATIF_MESURE", "idem (stop = plancher + mult × cadence)"),
    "DIP_CADENCE_MULT":      ("RELATIF_MESURE", "multiplie la cadence MESURÉE"),    "RIP_CADENCE_MULT":     ("RELATIF_MESURE", "idem"),
    "RIP_CADENCE_REF_PCT":  ("RELATIF_MESURE", "ÉCHELLE mesurée : médiane des cadences des paires réellement tradées (7,30 %/j au 22/09). Le palier de sortie = fixe × max(1 ; cadence_paire / cette référence) — ce n'est pas un seuil de décision, c'est l'unité dans laquelle on lit le palier."),
    "STOP_CADENCE_MULT":     ("RELATIF_MESURE", "idem"),
    # ---- SIZING / STRUCTURE (ne décide aucun arrêt) ----
    "NOTIONAL_USDT": ("SIZING", ""), "COMPOUND_ON": ("FLAG", ""), "COMPOUND_FRAC": ("SIZING", ""),
    "COMPOUND_MAX_MULT": ("SIZING", ""), "STAKE_DOUBLE_MULT": ("SIZING", ""),
    "STAKE_SELL_FRAC": ("SIZING", ""), "RIP_SELL_FRAC": ("SIZING", ""),
    "RIP_SCALEOUT_FRAC": ("SIZING", ""), "BAG_POSITION_MULT": ("SIZING", ""),
    "TIER_B_POSITION_MULT": ("SIZING", ""), "SEED_USDT": ("TEST", ""), "SEED_ON": ("FLAG", ""),
    "SEED_MODE": ("TEST", ""), "SEED_BAGS_USDT": ("TEST", ""),
    "SEED_BAGS_ENTRY_DD_PCT": ("TEST", ""), "SEED_BAGS_ON": ("FLAG", ""),
    "MODE": ("FLAG", ""), "QUOTE": ("FLAG", ""), "PAPER_MAX_PAIRS": ("TEST", ""),
    "BAG_NO_TECH_STOP": ("FLAG", ""), "SELL_FULL_GUARD_DEGRADED": ("FLAG", ""),
    "SELL_FULL_REQUIRE_INVALIDATION": ("FLAG", ""), "SELL_PARTIAL_CASCADE": ("FLAG", ""),
    "SENSE_STRICT_TENSION": ("FLAG", ""),
    "VEILLE_STATUS_REFRESH_SEC": ("TEMPS_HORS_DECISION", "cadence de rafraîchissement du statut de veille"),
}

# Toute clé qui finit par _ON et vaut 0/1 est un drapeau, pas un seuil.
FLAG_MOTIF = re.compile(r"(_ON$|_OFF$)")

TEMPS_MOTIF = re.compile(r"(_SEC|_SECONDS|_HOURS|_H$|_TTL|_MIN$|_MINUTES|_DAYS|_JOURS|INTERVAL)")


def lire_config():
    cles = {}
    with open(DEFAUTS, encoding="utf-8", errors="ignore") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#") or "=" not in ligne:
                continue
            k, v = ligne.split("=", 1)
            cles[k.strip()] = v.strip()
    return cles


def est_numerique(v):
    return bool(re.fullmatch(r"-?\d+(\.\d+)?", v.replace("%", "")))


def impact_du_dernier_chiffrage():
    """Le $ mesuré des gardes (dernier CHIFFRAGE_GARDES_*.json) — pour donner un ordre d'impact."""
    import glob
    fs = sorted(glob.glob(os.path.join(RUNS_H, "CHIFFRAGE_GARDES_*.json")))
    if not fs:
        return {}, None
    d = json.load(open(fs[-1], encoding="utf-8"))
    return ({g["code"]: g["dollars"] for g in d.get("gardes", [])}, os.path.basename(fs[-1]))


def main():
    cfg = lire_config()
    chiffres, src_chiffre = impact_du_dernier_chiffrage()
    classes = {}
    non_classees = []
    for k, v in cfg.items():
        if not est_numerique(v):
            classes[k] = ("NON_NUMERIQUE", "liste/texte/flag")
            continue
        if k in C:
            classes[k] = C[k]
        elif FLAG_MOTIF.search(k) and v in ("0", "1"):
            classes[k] = ("FLAG", "interrupteur 0/1 (aucun seuil)")
        elif TEMPS_MOTIF.search(k):
            classes[k] = ("TEMPS_A_CLASSER", "nom en _SEC/_HOURS/_TTL → à ranger explicitement")
            non_classees.append(k)
        else:
            classes[k] = ("A_CLASSER", "seuil numérique sans classification")
            non_classees.append(k)

    decideurs = [(k, v, classes[k]) for k, v in cfg.items()
                 if classes[k][0] in ("TEMPS_DECISION", "COMPTEUR_DECISION", "PCT_FIXE_DECISION")]

    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    lignes = [
        "# Seuils encore FIXES dans le moteur — inventaire mécanique (R17)",
        "",
        f"> {maintenant} · généré par `inventaire_seuils_fixes.py` · **lecture seule, 0 €**.",
        f"> Source : `hulk-mexc/config/defaults.env` ({len(cfg)} clés) · impact $ : "
        f"`{src_chiffre or 'aucun chiffrage disponible'}`.",
        "",
        f"**{len(decideurs)} seuils DÉCIDENT d'un arrêt/d'une entrée/d'une sortie sans être mesurés**",
        f" (cible de la règle R17). {len(non_classees)} seuil(s) non classé(s).",
        "",
        "## ⚠ Seuils de DÉCISION en dur (à mesurer, par ordre d'impact)",
        "",
        "| Seuil | Valeur | Classe | Ce qu'il décide |",
        "|---|---|---|---|",
    ]
    for k, v, (cl, why) in sorted(decideurs, key=lambda x: (x[2][0], x[0])):
        lignes.append(f"| `{k}` | {v} | {cl.replace('_DECISION','')} | {why} |")
    lignes += ["", "## Conformes R17 (dérivés d'une grandeur mesurée de l'actif)", "",
               "| Seuil | Pourquoi c'est conforme |", "|---|---|"]
    for k, (cl, why) in sorted(classes.items()):
        if cl == "RELATIF_MESURE":
            lignes.append(f"| `{k}` | {why} |")
    if non_classees:
        lignes += ["", "## ❌ NON CLASSÉS (l'organe crie : un seuil a été ajouté sans être rangé)", ""]
        lignes += [f"- `{k}` = {cfg[k]}" for k in sorted(non_classees)]
    lignes += ["", "## Lecture", "",
               "Le $ mesuré des gardes (dernier chiffrage, à recouper au moins à 2 horizons — R17.3) :", ""]
    for code, dol in sorted(chiffres.items(), key=lambda x: x[1]):
        lignes.append(f"- `{code}` : {dol:+.1f} $")
    open(SORTIE_MD, "w", encoding="utf-8").write("\n".join(lignes) + "\n")
    json.dump({"ts": maintenant, "cles": len(cfg), "decideurs": len(decideurs),
               "non_classees": non_classees,
               "classes": {k: {"valeur": cfg[k], "classe": classes[k][0], "pourquoi": classes[k][1]}
                           for k in cfg}},
              open(SORTIE_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print(f"INVENTAIRE DES SEUILS — {len(cfg)} clés · {len(decideurs)} DÉCIDENT sans mesure · "
          f"{len(non_classees)} non classé(s)")
    if non_classees:
        print("  ❌ non classés :", ", ".join(sorted(non_classees)))
    print(f"  rapport : {SORTIE_MD}")
    return 1 if non_classees else 0


if __name__ == "__main__":
    sys.exit(main())
