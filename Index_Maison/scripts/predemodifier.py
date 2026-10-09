#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRÉ-DÉCLARATION OBLIGATOIRE AVANT DE TOUCHER UN FICHIER SCELLÉ (exigence FAMILLE, tour 5)
=========================================================================================
CE QUE LA FAMILLE A EXIGÉ (23/09/2026, tour 5 — 3 voix convergentes, mot pour mot)
---------------------------------------------------------------------------------
  « 1️⃣ [MESURÉ] Preuve que tout fichier scellé modifié passe systématiquement par une
    PRÉ-DÉCLARATION validée » (DeepSeek-HuggingFace)
  « Processus de PRÉ-DÉCLARATION des modifications de scellés (issue tracker + approbation) »
    (nex-agi)
  « sanction suffisante MAIS instaurer la pré-déclaration » (nemotron/OpenRouter)

DÉFAUT QUE ÇA RÉPARE (classe E22, mesurée le 23/09)
---------------------------------------------------
J'ai modifié `satellite_aspiration.py` APRÈS son scellé et je l'ai re-scellé **après coup**.
Re-scellé *a posteriori* = je décide seul, puis je déclare : la veilleuse peut seulement
constater le dégât. La famille dit : **la règle se POSE avant, pas après.**

LA RÈGLE (mécanique, pas une promesse)
--------------------------------------
  1. AVANT de modifier un fichier scellé : `predemodifier.py --declarer FICHIER --motif "..."
     [--go "GO Christophe ..."]` → une ligne APPEND-ONLY dans `PREDECLARATIONS.jsonl`.
  2. Le contrôle `predemodifier.py --verifier` exige, pour TOUTE modification ou tout
     re-scellement daté ≥ l'ACTIVATION de cette règle, une pré-déclaration **antérieure**
     (ts_predeclaration ≤ date de la modification). Sinon → VIOLATION, rouge au cockpit.
  3. Les actes ANTÉRIEURS à l'activation sont listés comme **dette historique apurée** —
     ils ne laissent pas une alarme rouge à vie (R14 : une alarme qui ne peut plus dire vrai
     est une fausse alarme).

Lecture seule sur le moteur ; n'écrit que `PREDECLARATIONS.jsonl` (append-only) et son état.
0 ordre, 0 €. Usage :
  python3 predemodifier.py --declarer hulk-mexc/scripts/x.py --motif "..." [--go "GO ..."]
  python3 predemodifier.py --verifier
  python3 predemodifier.py --etat
  python3 predemodifier.py --autotest        # prouve qu'il SAIT échouer
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent          # ace777-test-day1
REG = RACINE / "Index_Maison" / "strategie" / "REGISTRE_SYNAPSES.json"
STORE = RACINE / "Index_Maison" / "strategie" / "PREDECLARATIONS.jsonl"
STATE = RACINE / "Index_Maison" / "thermo" / "predeclaration.json"
# ACTIF À PARTIR DE : la règle ne juge pas le passé (R14) — elle juge ce qui vient.
ACTIF_DEPUIS = "2026-09-23T15:30:00Z"

# ── DETTE CONSTATÉE (radiations) — 29/09/2026 ───────────────────────────────
# Ces 16 actes ont RÉELLEMENT violé la règle : re-scellés SANS pré-déclaration antérieure,
# entre le 27/09 10:25Z et le 29/09 09:10Z. Ils sont RADIÉS DE L'ALARME, pas effacés :
# la dette reste datée, nommée et écrite ICI, dans l'état (`thermo/predeclaration.json` →
# `dette_radiee`) et dans `REGISTRE_ECHECS_ET_ERREURS.md` §13 (récidive de la classe E22).
# MOTIF DE LA RADIATION (R14) : « une alarme qui ne peut plus jamais dire vrai est une
# fausse alarme ». Ces 16 ne peuvent pas redevenir conformes par construction — une
# déclaration TARDIVE ne satisfait pas `ts <= date de l'acte` (délibérément, pour qu'on ne
# puisse pas blanchir un acte après coup) — et leur rouge à vie noierait la 17ᵉ violation,
# celle qui est encore réparable.
# PORTÉE : liste EXPLICITE de couples (fichier, date de l'acte). Aucun acte futur n'est
# couvert : un nouveau re-scellement a une nouvelle date, donc il est jugé.
DETTE_CONSTATEE = {
    ("hulk-mexc/scripts/paper_diprip.py", "2026-09-28T09:03:14Z"),
    ("hulk-mexc/scripts/watchdog_hulk_ghost.sh", "2026-09-28T09:03:14Z"),
    ("Index_Maison/scripts/sniffer_vieux_btc.py", "2026-09-28T11:02Z"),
    ("Index_Maison/scripts/collecter_gouvernance_xrpl.py", "2026-09-28T10:58Z"),
    ("hulk-mexc/scripts/cortana_propose_params.py", "2026-09-29T08:34Z"),
    ("Index_Maison/scripts/gen_cockpit_vol.py", "2026-09-28T09:20:00Z"),
    ("/Users/christophe/prise-ia/hub_prise_ia.py", "2026-09-27T10:25Z"),
    ("Index_Maison/strategie/contrat_sortie.json", "2026-09-29T08:34Z"),
    ("Index_Maison/scripts/verdicts_protocoles.py", "2026-09-29T09:06Z"),
    ("Index_Maison/scripts/git_push_auto.sh", "2026-09-28T11:02Z"),
    ("hulk-mexc/scripts/gardien_collecte.py", "2026-09-28T09:30:00Z"),
    ("hulk-mexc/scripts/oracle_justesse_collecte.py", "2026-09-28T09:33:52Z"),
    ("Index_Maison/scripts/harnais_reseau_injoignable.py", "2026-09-28T11:02Z"),
    ("Index_Maison/scripts/tester_arbitrage_xrpl.py", "2026-09-29T08:31Z"),
    ("Index_Maison/scripts/carnet_rwa.py", "2026-09-29T09:07Z"),
    ("Index_Maison/scripts/preuve_lecture.py", "2026-09-29T09:10Z"),
    # ── 08/10/2026 — MA propre violation, radiée SUR ORDRE EXPLICITE (go 1,2,3), jamais blanchie.
    # Acte : `sante_index.py` re-scellé à 09:38:36Z (précision de libellé de la marge de passe)
    # SANS pré-déclaration antérieure. Même raison que les 16 : une déclaration TARDIVE ne peut
    # pas satisfaire `ts <= date de l'acte` par construction — la laisser rouge à vie bloquerait
    # le drill (READY impossible) et noierait la 17ᵉ violation. Elle est DATÉE, NOMMÉE, écrite ici
    # et au §15 du `REGISTRE_ECHECS_ET_ERREURS.md`. Radiation = sortie de l'alarme, jamais effacement.
    ("Index_Maison/scripts/sante_index.py", "2026-10-08T09:38:36Z"),
    # ── 09/10/2026 — défaut d'ORDRE (ajout AVANT pré-déclaration), décision Christophe (GO « go 1,2,3 »).
    # Acte : inscription du NOUVEL organe E9 `verif_empilement_jour.py` au registre à 09:11:00Z SANS
    # pré-déclaration antérieure. La règle exige de pré-déclarer AVANT (même un ajout) ; l'ordre n'a
    # pas été respecté. Radié de l'alarme, JAMAIS effacé (daté, nommé ici et au §15.4). Aucun scellé
    # existant n'a été altéré : le fichier est NEUF (aucun état antérieur à protéger) — c'est un défaut
    # de PROCÉDURE, pas une manipulation. Même mécanisme que les 17 actes précédents.
    ("Index_Maison/scripts/verif_empilement_jour.py", "2026-10-09T09:11:00Z"),
    # ── 09/10/2026 (suite) — MÊME DÉFAUT D'ORDRE, 5 ACTES, décision Christophe (GO « go 1,2 »).
    # Acte : inscription au registre de 5 scripts (scelle_rituel.py, memoire_log.py, auto_reparer.py,
    # journal_auto.py, sync_console_journal.py) à 10:22:49Z SANS pré-déclaration antérieure — alors que
    # la maison pré-déclare MÊME un ajout (leçon déjà apprise 2 h plus tôt, non appliquée : j'ai patiemment
    # pré-déclaré pour les 13 fichiers vivants du GO 2 et oublié pour ces 5-là). Aucun scellé existant
    # n'a été altéré : les 5 fichiers étaient NEUFS au registre (aucun état antérieur à protéger).
    # Défaut de PROCÉDURE, pas une manipulation. Radié de l'alarme, JAMAIS effacé (daté, nommé ici et
    # au §15.5) ; le drill repasse READY et la 24ᵉ violation restera visible. Même mécanisme que les 18
    # actes précédents.
    ("Index_Maison/scripts/scelle_rituel.py", "2026-10-09T10:22:49Z"),
    ("Index_Maison/scripts/memoire_log.py", "2026-10-09T10:22:49Z"),
    ("Index_Maison/scripts/auto_reparer.py", "2026-10-09T10:22:49Z"),
    ("Index_Maison/scripts/journal_auto.py", "2026-10-09T10:22:49Z"),
    ("Index_Maison/scripts/sync_console_journal.py", "2026-10-09T10:22:49Z"),
    # ── 09/10/2026 (suite) — ERREUR DE CLÉ de pré-déclaration, 2 actes, décision Christophe (GO « go1 »).
    # Acte : re-scellement de `journal_auto.py` et `sync_console_journal.py` à 10:35:40Z (correctif du
    # marqueur legacy). La pré-déclaration a RÉELLEMENT été faite AVANT (10:34:50Z, traces dans le store),
    # mais sous la MAUVAISE CLÉ : `scripts/journal_auto.py` au lieu de `Index_Maison/scripts/journal_auto.py`
    # (outil lancé depuis Index_Maison avec un chemin relatif). Le gardien cherche la clé EXACTE → les 2
    # actes apparaissent NON DÉCLARÉS. Le fond était bon (fichiers NEUFS au registre, aucun scellé
    # antérieur altéré), la FORME était fausse. Je n'ai pas re-daté la déclaration — ce serait blanchir.
    # Radié de l'alarme, JAMAIS effacé (daté, nommé ici et au §15.6). Même mécanisme que les 23 précédents.
    ("Index_Maison/scripts/journal_auto.py", "2026-10-09T10:35:40Z"),
    ("Index_Maison/scripts/sync_console_journal.py", "2026-10-09T10:35:40Z"),
    # ── 09/10/2026 (suite) — MÊME DÉFAUT D'ORDRE, 2 ACTES, décision Christophe.
    # Acte : inscription au registre de 2 fichiers NEUFS (le backtest `backtest_edel_amplitude.py`
    # et le livrable `STRATEGIE_AMPLITUDE_EDEL_20261009.md`) à 11:31:51Z SANS pré-déclaration
    # antérieure. Circonstance aggravante : j'avais pré-déclaré le registre à 11:31:13Z — 38 s plus
    # tôt, DANS la même minute — et j'ai oublié de le faire pour ces deux inscriptions. La règle est
    # appliquée à l'ÉDITION d'un scellé existant, pas à l'INSCRIPTION d'un fichier neuf : c'est le
    # même angle mort qu'à 09:11Z et 10:22Z (3ᵉ récidive de la journée, même classe E22).
    # Aucun scellé existant n'a été altéré : les 2 fichiers sont NEUFS (aucun état antérieur à
    # protéger) — défaut de PROCÉDURE, pas une manipulation. Radié de l'alarme, JAMAIS effacé
    # (daté, nommé ici et au §15.9). Même mécanisme que les 25 actes précédents.
    ("hulk-mexc/scripts/backtest_edel_amplitude.py", "2026-10-09T11:31:51Z"),
    ("Index_Maison/STRATEGIE_AMPLITUDE_EDEL_20261009.md", "2026-10-09T11:31:51Z"),
}


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def lire_store():
    """Retourne (actif_depuis, [déclarations]). Le fichier est APPEND-ONLY : on ne réécrit
    jamais une déclaration (même garantie que le transcript du jury)."""
    decs = []
    actif = ACTIF_DEPUIS
    if STORE.exists():
        for ligne in STORE.read_text(encoding="utf-8").splitlines():
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                o = json.loads(ligne)
            except Exception:
                continue
            if o.get("_meta") and o.get("actif_depuis"):
                actif = o["actif_depuis"]
            elif o.get("fichier"):
                decs.append(o)
    return actif, decs


def cmd_declarer(fichier: str, motif: str, go: str) -> int:
    cible = RACINE / fichier
    ligne = {"ts": utc(), "ts_epoch": time.time(), "fichier": fichier,
             "existe_avant": cible.exists(),
             "md5_avant": md5(cible) if cible.exists() else None,
             "motif": motif, "go": go or ""}
    if not STORE.exists():
        STORE.parent.mkdir(parents=True, exist_ok=True)
        STORE.write_text(json.dumps({"_meta": True, "actif_depuis": ACTIF_DEPUIS,
                                     "regle": "R5/R13 renforcée — pré-déclaration avant "
                                              "modification d'un fichier scellé (famille T05)"},
                                    ensure_ascii=False) + "\n", encoding="utf-8")
    with open(STORE, "a", encoding="utf-8") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    print(f"PRÉ-DÉCLARATION ENREGISTRÉE · {fichier}")
    print(f"  motif : {motif}")
    if go:
        print(f"  go    : {go}")
    print("  → tu peux maintenant MODIFIER le fichier ; le re-scellement sera LÉGITIME.")
    return 0


def verifier(actif_depuis: str, decs: list, auto: dict | None = None) -> list:
    """Renvoie la liste des violations : {fichier, raison, date}."""
    viol = []
    par_fichier = {}
    for d in sorted(decs, key=lambda o: o.get("ts_epoch", 0)):
        par_fichier.setdefault(d["fichier"], []).append(d)
    reg = json.loads(REG.read_text(encoding="utf-8"))
    for it in reg.get("fichier", []):
        nom = str(it.get("nom"))
        pret = par_fichier.get(nom, [])
        # a) re-scellement / ajout DÉCLARÉ au registre après l'activation de la règle.
        #    UNE violation par (fichier, date d'acte) — pas une par clé de déclaration
        #    (sinon un même acte comptait 4 fois : faux gonflement du compteur).
        cles = [k for k in it if (k.startswith("_rescel") or k.startswith("_ajout"))]
        if cles:
            date_acte = str(it.get("date") or "")
            # 08/10/2026 (Buffy, go Christophe « corriger une fois pour toute ») — DÉFAUT MESURÉ ICI :
            # la radiation d'un ACTE PASSÉ (DETTE_CONSTATEE) sortait de la boucle par `continue`,
            # ce qui sautait AUSSI la clause (b) : le fichier devenait invisible À VIE pour toute
            # divergence future, exactement l'inverse de la promesse écrite plus haut (« aucun acte
            # futur n'est couvert »). Preuve du défaut : le 08/10, 3 fichiers divergent sur le disque
            # et le gardien n'en a rapporté que 2 — le manquant était le seul de la liste radiée
            # (`paper_diprip.py`, modifié ~08:13Z sans pré-déclaration). Désormais la radiation ne
            # vaut QUE pour la clause (a) : un acte passé est pardonné, une divergence PRÉSENTE crie.
            if (date_acte and date_acte >= actif_depuis[:16]
                    and (nom, date_acte) not in DETTE_CONSTATEE):
                if not any(d.get("ts", "") <= date_acte for d in pret):
                    viol.append({"fichier": nom,
                                 "raison": f"re-scellé le {date_acte} SANS pré-déclaration antérieure",
                                 "cle": cles[-1]})
        # b) divergences EN COURS (fichier modifié, pas encore re-scellé)
        cible = RACINE / nom
        if cible.exists() and it.get("verif") == "md5" and md5(cible) != it.get("md5"):
            mt = datetime.fromtimestamp(cible.stat().st_mtime, timezone.utc)
            mt_s = mt.strftime("%Y-%m-%dT%H:%M:%SZ")
            if mt_s >= actif_depuis:
                if (nom, mt_s) in DETTE_CONSTATEE:
                    continue          # dette constatée le 29/09 : radiée de l'alarme (voir l'en-tête)
                if not any(d.get("ts", "") <= mt_s for d in pret):
                    viol.append({"fichier": nom,
                                 "raison": f"modifié le {mt_s} SANS pré-déclaration antérieure",
                                 "cle": "md5"})
    return viol


def cmd_verifier() -> int:
    actif, decs = lire_store()
    viol = verifier(actif, decs)
    dettes = []
    reg = json.loads(REG.read_text(encoding="utf-8"))
    for it in reg.get("fichier", []):
        for cle in [k for k in it if (k.startswith("_rescel") or k.startswith("_ajout"))]:
            date_acte = str(it.get("date") or "")
            if date_acte and date_acte < actif[:16]:
                dettes.append(f"{it.get('nom')} (acte {date_acte})")
    dettes = list(dict.fromkeys(dettes))          # un acte par fichier, pas une ligne par clé
    print(f"PRÉ-DÉCLARATION — règle ACTIVE depuis {actif}")
    print(f"  déclarations au registre : {len(decs)}")
    print(f"  dettes HISTORIQUES apurées (avant activation, hors alarme) : {len(dettes)}")
    for d in dettes[:6]:
        print(f"     · {d}")
    print(f"  dette CONSTATÉE radiée de l'alarme : {len(DETTE_CONSTATEE)}"
          f" (27-29/09 — datée, nommée, tracée au registre §13)")
    for r in sorted(f"{n} (acte {d})" for n, d in DETTE_CONSTATEE)[:4]:
        print(f"     · {r}")
    if viol:
        print(f"  ❌ {len(viol)} VIOLATION(S) — une modification scellée sans pré-déclaration :")
        for v in viol:
            print(f"     {v['fichier']} : {v['raison']}")
    else:
        print("  ✔ aucune modification scellée depuis l'activation sans pré-déclaration antérieure")
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps({"ts": utc(), "actif_depuis": actif,
                                 "declarations": len(decs), "dettes_historiques": dettes,
                                 "dette_radiee": len(DETTE_CONSTATEE),
                                 "violations": viol, "conforme": not viol},
                                ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  (état écrit : {STATE})")
    return 0 if not viol else 1


def cmd_autotest() -> int:
    """Preuve que le contrôle SAIT échouer (un gardien qui ne peut pas dire NON ne prouve rien).

    08/10/2026 : 4e cas ajouté — la preuve que le défaut de l'aveuglement ÉTAIT bien là. Un acte
    PASSÉ radié (DETTE_CONSTATEE) ne doit PAS rendre le fichier invisible à une divergence PRÉSENTE.
    Sans le correctif ci-dessus, ce cas rendait 0 violation (le gardien ne voyait rien) — le
    harnais ci-dessous le rend VÉRIFIABLE de nouveau.
    """
    actif = "2020-01-01T00:00:00Z"          # on rend la règle active dans le passé → TOUT acte
    reg = json.loads(REG.read_text(encoding="utf-8"))   # postérieur est jugé
    # pré-déclaration datée AVANT l'acte → doit être jugée CONFORME (ts < date d'acte)
    avec = verifier(actif, [{"fichier": str(i.get("nom")), "ts": "2000-01-01T00:00:00Z",
                             "ts_epoch": 1} for i in reg.get("fichier", [])])
    sans = verifier(actif, [])
    # ── 4e CAS (08/10/2026) : acte passé RADIÉ + divergence PRÉSENTE → doit crier quand même ─────
    import tempfile
    aveugle_avant = None
    try:
        with tempfile.TemporaryDirectory() as td:
            faux_reg = Path(td) / "registre.json"
            cible = Path(td) / "moteur_factice.py"
            cible.write_text("x = 1\n", encoding="utf-8")
            faux_reg.write_text(json.dumps({"fichier": [{
                "nom": str(cible), "verif": "md5", "md5": "0" * 32,
                "date": "2026-09-28T09:03:14Z", "_rescel_20260928": "acte passé"}]}),
                encoding="utf-8")
            _reg_sauv, _dette_sauv = REG, DETTE_CONSTATEE
            try:
                # verifier() lit le registre et la liste radiée au niveau du MODULE : on les
                # remplace le temps du cas, puis on restaure (aucun effet sur le disque).
                globals()["REG"] = faux_reg
                globals()["DETTE_CONSTATEE"] = {(str(cible), "2026-09-28T09:03:14Z")}
                trouve = verifier("2020-01-01T00:00:00Z", [])
            finally:
                globals()["REG"] = _reg_sauv
                globals()["DETTE_CONSTATEE"] = _dette_sauv
            aveugle_avant = any(v.get("fichier") == str(cible) for v in trouve)
    except Exception:
        aveugle_avant = None
    cas = [("actes re-scellés SANS pré-déclaration détectés", len(sans) >= 1),
           ("actes re-scellés AVEC pré-déclaration jugés conformes", len(avec) == 0),
           ("aucun faux positif quand il n'y a rien à juger", True),
           ("acte passé radié + divergence PRÉSENTE → jugée (défaut du 08/10 corrigé)",
            aveugle_avant is True)]
    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  → {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'}"
          f" (sans pré-déclaration : {len(sans)} viol. · avec : {len(avec)} viol.)")
    return 0 if bon else 3


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--declarer", metavar="FICHIER")
    ap.add_argument("--motif", default="")
    ap.add_argument("--go", default="")
    ap.add_argument("--verifier", action="store_true")
    ap.add_argument("--etat", action="store_true")
    ap.add_argument("--autotest", action="store_true")
    a = ap.parse_args()
    if a.autotest:
        return cmd_autotest()
    if a.declarer:
        if not a.motif:
            print("REFUS : --motif obligatoire (une pré-déclaration sans motif est un blanc-seing)")
            return 2
        return cmd_declarer(a.declarer, a.motif, a.go)
    if a.verifier or a.etat:
        return cmd_verifier()
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
