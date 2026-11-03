#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""equity_reconcilie.py — LE GRAND LIVRE, PAR PÉRIMÈTRE (03/11/2026, GO Christophe).

CORRIGÉ 03/11 08:20 — ma première version comptait mal, et Christophe l'a dit :
WAXL / IOTA / LA sont en **OBSERVATION** (20 $ chacun, récolte de données pour
leur set sur mesure) et **QAIT / TEL ont été RADIÉS**. Donc :

  * le cash d'observation n'est PAS du « cash invisible » : c'est un budget
    réel, hors ratios de risque, mais dans la valeur du portefeuille ;
  * le cash résiduel des paires radiées est un FANTÔME : il traîne dans le
    journal et ne compte nulle part.

Trois livres séparés, jamais mélangés :
  TRADING      = le moteur (state : pair_cash + bags) vs le journal sur les
                 mêmes paires -> c'est LE vrai écart de comptabilité à corriger
  OBSERVATION  = 3 budgets de 20 $ (source : strategie/classification_paires.json)
  RADIÉS       = cash résiduel à sortir (doit tendre vers 0)

Portefeuille = trading + observation. Les ratios de risque (Kelly, réserve,
niveau hack, Mur) ne lisent QUE le trading — c'est le point que je m'étais
trompé : monter l'equity avec du cash d'observation gonflerait la réserve.

Lecture seule, 0 ordre, 0 mutation d'état. Sortie : thermo/equity_reconcilie.json
Exit 0 = mesure écrite (même si l'écart est mauvais) ; 2 = source illisible.
"""
import csv
import glob
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.expanduser("~/ace777-test-day1")
RUNS = os.path.join(ROOT, "hulk-mexc", "runs")
THERMO = os.path.join(ROOT, "Index_Maison", "thermo")
MISSION = os.path.join(ROOT, "Index_Maison", "cockpit", "mission.json")
CLASSIF = os.path.join(ROOT, "Index_Maison", "strategie", "classification_paires.json")
OUT = os.path.join(THERMO, "equity_reconcilie.json")
ANCRE = os.path.join(RUNS, "LIVRE_ANCRE.json")
LEDGER = os.path.join(RUNS, "CASH_LEDGER.csv")
SEUIL_ECART_USD = 5.0
SEUIL_CAISSE_USD = 1.0
FEE = 0.0005


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def lire_state():
    ptr = os.path.join(RUNS, ".hulk_resume_pointer")
    nom = open(ptr, encoding="utf-8").read().strip()
    return json.load(open(os.path.join(RUNS, nom), encoding="utf-8")), nom


def lire_journal():
    cands = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")), key=os.path.getmtime)
    if not cands:
        raise FileNotFoundError("aucun journal PAPER_V1_*.csv")
    return cands[-1]


def lire_marks():
    fs = sorted(glob.glob(os.path.join(RUNS, "DIGEST_*.json")), key=os.path.getmtime)
    if not fs:
        raise FileNotFoundError("aucun DIGEST")
    d = json.load(open(fs[-1], encoding="utf-8"))
    marks = {}
    for e in (d.get("pairs") or []):
        try:
            if e.get("pair") and float(e.get("last") or 0) > 0:
                marks[e["pair"]] = float(e["last"])
        except Exception:
            continue
    return marks, os.path.basename(fs[-1]), d.get("ts")


def lire_journal_meta(journal, ts_ancre):
    """Compte ce que le journal CONTIENT — au lieu de raconter pourquoi il manque des choses.

    POURQUOI (03/11/2026, 3ᵉ passe). Le drift de 24,96 $ portait une cause écrite à la main
    (« cash bougé sans ligne ») que RIEN ne mesurait : une cause inventée est une erreur de
    plus, et c'est exactement la classe que Christophe dénonce. Ici on ne raconte pas, on
    compte :
      · `n_seed` = événements de financement initial (SEED/INIT/DEPOT/FUND). Mesuré = 0 sur
        tout le journal → le rejeu ne PEUT PAS reconstruire le cash de départ, il doit
        inventer un budget (mission.json). L'écart mélange donc deux POINTS DE DÉPART : ce
        n'est ni une perte, ni du cash manquant.
      · `n_cash_post_ancre` = événements qui bougent du cash APRÈS l'ancre. S'il en existe
        et qu'aucun mouvement n'est écrit dans CASH_LEDGER.csv, la réconciliation est VIDE :
        publier 0,00 $ serait un faux vert (le défaut du 03/11, trouvé par Christophe).
    """
    types, n_seed, n_cash_post, n_lignes = {}, 0, 0, 0
    cash_ev = ("BUY", "SELL", "STOP", "DCA", "GBAG", "BAG", "CORE")
    with open(journal, newline="", encoding="utf-8-sig", errors="replace") as f:
        for r in csv.DictReader(f):
            n_lignes += 1
            ev = (r.get("event") or "").upper()
            types[ev] = types.get(ev, 0) + 1
            if ev.startswith(("SEED", "INIT", "DEPOT", "FUND")):
                n_seed += 1
            elif ts_ancre and ev.startswith(cash_ev) and str(r.get("ts") or "") > ts_ancre:
                n_cash_post += 1
    return {"n_lignes": n_lignes, "types": len(types), "n_seed": n_seed,
            "n_cash_post_ancre": n_cash_post}


def qty_de(ent):
    if not isinstance(ent, dict):
        return 0.0
    for k in ("qty", "quantite", "quantity", "amount"):
        if ent.get(k) is not None:
            try:
                return float(ent[k])
            except Exception:
                pass
    return 0.0


def main():
    try:
        st, nom_state = lire_state()
        journal = lire_journal()
        try:
            _a0 = json.load(open(ANCRE, encoding="utf-8"))
        except Exception:
            _a0 = {}
        meta_journal = lire_journal_meta(journal, _a0.get("ts"))
        meta_journal["ledger_present"] = os.path.exists(LEDGER)
        marks, nom_digest, ts_digest = lire_marks()
        # FIX 03/11 (boucle source) : une paire absente du dernier DIGEST était
        # valorisée 0 -> QNT/FLUID/RWA ont fait disparaître 103 $ du livre au run
        # de 08:25Z (moteur 691,95 $ au lieu de 795 $). Un prix manquant n'est pas
        # un prix nul : on reprend le dernier mark CONNU et on le DÉCLARE.
        marks_secours = {}
        try:
            for f in sorted(glob.glob(os.path.join(RUNS, "DIGEST_*.json")),
                            key=os.path.getmtime, reverse=True):
                d = json.load(open(f, encoding="utf-8"))
                for e in (d.get("pairs") or []):
                    p0 = e.get("pair")
                    if not p0 or p0 in marks or p0 in marks_secours:
                        continue
                    try:
                        v = float(e.get("last") or 0)
                    except Exception:
                        continue
                    if v > 0:
                        marks_secours[p0] = (v, d.get("ts"))
                if len(marks) + len(marks_secours) >= 30:
                    break
        except Exception:
            pass
        marks_stale = {p0: ts0 for p0, (_, ts0) in marks_secours.items()}
        for p0, (v0, _) in marks_secours.items():
            marks[p0] = v0
        mission = json.load(open(MISSION, encoding="utf-8"))
        cls = json.load(open(CLASSIF, encoding="utf-8"))
    except Exception as e:
        print("[equity] source illisible : %s" % e, file=sys.stderr)
        return 2
    if not cls.get("paires"):
        print("[equity] classification_paires.json vide — aucune conclusion (R26)",
              file=sys.stderr)
        return 2
    statut = {p: (v.get("statut") or "?") for p, v in cls["paires"].items()}

    budgets = {p["pair"]: float(p.get("budget") or 0.0)
               for p in mission["hulk"]["hulkVsHold"]["pairs"]}
    for p, v in cls["paires"].items():
        budgets.setdefault(p, float(v.get("budget") or 0.0))

    # --- journal (rejeu), toutes paires déclarées ---
    rp = {p: {"cash": budgets.get(p, 0.0), "qty": 0.0, "cost": 0.0}
          for p in budgets}
    n_ev = 0
    with open(journal, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            p = r.get("pair") or ""
            if p not in rp:
                continue
            ev = (r.get("event") or "").upper()
            if ev == "BAG_ARM":
                continue
            try:
                q = float(r.get("qty") or 0.0)
                px = float(r.get("price") or 0.0)
            except Exception:
                continue
            if q <= 0 or px <= 0:
                continue
            s = rp[p]
            notion, fee = q * px, q * px * FEE
            if ev in ("BUY", "DCA", "GBAG_SOUCHE", "GBAG_PYRAMIDE", "BAG_DCA"):
                s["cash"] -= max(0.0, s["cash"]) if ev == "GBAG_SOUCHE" else notion + fee
                s["qty"] += q
                s["cost"] += notion + fee
            elif ev.startswith(("SELL", "STOP", "BAG")):
                avg = (s["cost"] / s["qty"]) if s["qty"] > 1e-12 else 0.0
                s["cash"] += notion - fee
                s["qty"] = max(0.0, s["qty"] - q)
                s["cost"] = max(0.0, s["cost"] - avg * q)
            n_ev += 1

    def livre_caisse(cash_moteur, meta):
        """ÉCART POST-ANCRE — la seule mesure qui ne peut pas mentir.

        POURQUOI CE CHANGEMENT (03/11/2026). L'ancien calcul rejouait tout le
        journal depuis les budgets déclarés. Mesuré : 25,15 $ d'écart dont
        WUSDT 29,88 $ — or le moteur est la seule autorité sur son cash. La
        cause n'était pas une erreur du moteur mais un TROU DU JOURNAL : du cash
        crédité/débité sans ligne (WUSDT, QNTUSDT, MNSRYUSDT). Aucun replay ne
        peut retrouver une information qui n'a jamais été écrite.

        Depuis le livre de caisse, le moteur écrit CHAQUE mouvement
        (add/take_pair_cash) et une ancre de départ. Donc :
            cash_ancre + Σ deltas post-ancre  ==  cash moteur
        par construction. Si ça diverge, un chemin a touché le cash sans le
        déclarer : c'est un défaut RÉEL, nommé à la paire près.
        Le drift antérieur (25,15 $) n'est ni caché ni requalifié : il est
        publié tel quel dans `drift_historique_usd`, avec sa cause.
        """
        try:
            a = json.load(open(ANCRE, encoding="utf-8"))
        except Exception:
            return {"disponible": False,
                    "raison": "ancre absente (moteur pas encore relancé avec le livre de caisse)"}
        cash = {p: float(v or 0.0) for p, v in (a.get("cash") or {}).items()}
        n0 = int(a.get("n_ledger_0") or 0)
        n_mvt = 0
        if os.path.exists(LEDGER):
            with open(LEDGER, newline="", encoding="utf-8") as f:
                lignes = list(csv.DictReader(f))
            for r in lignes[n0:]:
                p = r.get("pair") or ""
                if not p:
                    continue
                try:
                    d = float(r.get("delta_usdt") or 0.0)
                except ValueError:
                    continue
                cash[p] = cash.get(p, 0.0) + d
                n_mvt += 1
        ecarts = {}
        for p in sorted(set(cash) | set(cash_moteur)):
            e = round(float(cash_moteur.get(p, 0.0)) - cash.get(p, 0.0), 2)
            if abs(e) >= 0.01:
                ecarts[p] = e
        total = round(sum(ecarts.values()), 2)
        # PREUVE VIDE — le défaut mesuré le 03/11 : CASH_LEDGER.csv était ABSENT, donc
        # ancre + 0 delta == pair_cash par construction, et le rapport publiait
        # « écart 0,00 $ · ok true ». Un vert qui ne mesure rien. Trois états, désormais :
        #   probant   → au moins un mouvement écrit dans le livre ................ ok = |d| ≤ seuil
        #   non probant + des événements de cash depuis l'ancre (sans ligne) ..... ok = False (SANS_MESURE)
        #   non probant + aucun événement de cash ............................... ok = None (rien à réconcilier)
        probant = bool(os.path.exists(LEDGER)) and n_mvt > 0
        base = {"disponible": True, "ancre_ts": a.get("ts"),
                "ancre_journal": a.get("journal"), "n_mouvements": n_mvt,
                "ecart_post_ancre_usd": total, "ecart_par_paire": ecarts,
                "probant": probant, "seuil_usd": SEUIL_CAISSE_USD,
                "n_evenements_cash_post_ancre": meta.get("n_cash_post_ancre", 0),
                "ledger_present": bool(os.path.exists(LEDGER))}
        if not probant and meta.get("n_cash_post_ancre", 0) > 0:
            base.update({
                "ok": False,
                "raison": ("SANS_MESURE : %d événement(s) de cash depuis l'ancre et %s — "
                           "la réconciliation n'est PAS prouvée" % (
                               meta["n_cash_post_ancre"],
                               "CASH_LEDGER.csv absent" if not os.path.exists(LEDGER)
                               else "aucun mouvement écrit dans CASH_LEDGER.csv"))})
            return base
        if not probant:
            base.update({
                "ok": None,
                "raison": ("aucun événement de cash depuis l'ancre — identité vraie par "
                           "construction, NON PROBANTE (à ne pas lire comme une preuve)")})
            return base
        base["ok"] = abs(total) <= SEUIL_CAISSE_USD
        return base

    def agg(perimetre):
        cash = sum(rp[p]["cash"] for p in perimetre if p in rp)
        val = sum(rp[p]["qty"] * marks.get(p, 0.0) for p in perimetre if p in rp)
        return cash, val

    trading = [p for p, s in statut.items() if s == "trading"]
    observation = [p for p, s in statut.items() if s == "observation"]
    radies = [p for p, s in statut.items() if s == "radie"]

    # --- moteur : ce qu'il porte RÉELLEMENT ---
    cash_m = {p: float(v or 0) for p, v in (st.get("pair_cash") or {}).items()}
    qty_m = {}
    for d in (st.get("positions") or {}, st.get("bags") or {}):
        for p, e in d.items():
            qty_m[p] = qty_m.get(p, 0.0) + qty_de(e)
    val_m = sum(q * marks.get(p, 0.0) for p, q in qty_m.items())
    book_moteur = sum(cash_m.get(p, 0.0) for p in trading) + val_m

    cash_t, val_t = agg(trading)
    book_journal = cash_t + val_t
    cash_o, val_o = agg(observation)
    cash_r, val_r = agg(radies)
    # RADIÉS (03/11, 2ᵉ passe — mesuré AVANT de conclure) : le replay semait le
    # budget DÉCLARÉ (30 $/paire) de paires que le moteur n'a jamais financées.
    # Preuve : QAIT net journal −0,85 $ / moteur 0 ; TEL net journal +1,47 $ /
    # moteur 0. Les 60,28 $ n'étaient donc PAS du cash : c'était un artefact de
    # budget. Le bon critère n'est pas « le replay tombe à zéro » (impossible par
    # construction) mais « LE MOTEUR NE DÉTIENT RIEN » — vérifiable à la source.
    radies_detenu = {p: round(float(cash_m.get(p, 0.0)) + qty_m.get(p, 0.0) * marks.get(p, 0.0), 2)
                     for p in radies}
    radies_detenu_total = round(sum(radies_detenu.values()), 2)

    ecart = round(book_moteur - book_journal, 2)
    portefeuille = round(book_moteur + cash_o + val_o, 2)
    caisse = livre_caisse(cash_m, meta_journal)
    # ok = l'écart RÉEL du livre de caisse (post-ancre) + le résidu des radiés.
    # L'ancien écart de replay est CONSERVÉ et publié (drift historique), jamais
    # utilisé pour blanchir : il mesure une information absente du journal.
    # ok_caisse : False seulement si la mesure CONTREDIT (écart réel ou SANS_MESURE).
    # None (rien à réconcilier) n'est pas une preuve mais n'est pas une contradiction.
    ok_caisse = (caisse.get("ok") is not False) if caisse.get("disponible") else False
    ok_radies = abs(radies_detenu_total) <= 0.01
    ok_global = bool(ok_caisse and ok_radies)

    # détail des écarts, paires trading seulement (le vrai chantier)
    detail = {}
    for p in sorted(trading):
        if p not in rp:
            continue
        cm = cash_m.get(p)
        cr = rp[p]["cash"]
        qm = qty_m.get(p, 0.0)
        qr = rp[p]["qty"]
        ec = (cm - cr) if cm is not None else None
        dq = (qm - qr) * marks.get(p, 0.0)
        if (ec is None or abs(ec) < 0.005) and abs(dq) < 0.005:
            continue
        detail[p] = {"cash_moteur": (round(cm, 2) if cm is not None else None),
                     "cash_journal": round(cr, 2),
                     "ecart_cash": (round(ec, 2) if ec is not None else None),
                     "ecart_qty_usd": round(dq, 2)}

    res = {
        "ts": utc(), "state": nom_state, "journal": os.path.basename(journal),
        "digest": nom_digest, "ts_digest": ts_digest,
        "perimetres": {"trading": len(trading), "observation": len(observation),
                       "radie": len(radies)},
        "book_trading_moteur": round(book_moteur, 2),
        "book_trading_journal": round(book_journal, 2),
        "ecart_trading_moteur_journal": ecart,
        "cash_trading_moteur": round(sum(cash_m.get(p, 0.0) for p in trading), 2),
        "cash_trading_journal": round(cash_t, 2),
        "observation_cash": round(cash_o, 2),
        "observation_valeur": round(val_o, 2),
        "radies_residuel": radies_detenu_total,
        "radies_detenu_moteur_usd": radies_detenu_total,
        "radies_budget_artefact_usd": round(cash_r + val_r, 2),
        "radies_budget_cause": ("budget déclaré semé dans le replay pour des paires "
                                "jamais financées par le moteur (artefact, pas du cash) — "
                                "critère retenu : détention moteur = 0"),
        "equity_portefeuille": portefeuille,
        "equity_trading_moteur": round(book_moteur, 2),
        "ok": ok_global,
        "ok_caisse": ok_caisse,
        "ok_radies": ok_radies,
        "livre_caisse": caisse,
        "drift_historique_usd": ecart,
        "drift_historique_attribue": False,
        "drift_historique_cause": (
            "NON ATTRIBUÉ à un mouvement précis. Mesuré, pas raconté : le journal ne contient "
            "AUCUN événement de financement initial (%d SEED/INIT sur %d lignes, %d types) — "
            "un rejeu ne peut donc pas reconstruire le cash de départ et doit inventer un "
            "budget (mission.json). L'écart mesure donc DEUX CHOSES MÊLÉES : deux points de "
            "départ différents + les mouvements que le journal n'a pas écrits. Ce n'est ni "
            "une perte ni du cash manquant : la poche moteur (pair_cash) fait foi. "
            "L'attribution exacte exige de journaliser les seeds (à faire, calendrier)."
            % (meta_journal["n_seed"], meta_journal["n_lignes"], meta_journal["types"])),
        "drift_historique_preuve": dict(meta_journal),
        "seuil_alerte_usd": SEUIL_CAISSE_USD,
        "detail_trading": detail,
        "observation": {p: round(rp[p]["cash"], 2) for p in observation},
        "radies": radies_detenu,
        "radies_detail": {p: {"budget_declare": round(budgets.get(p, 0.0), 2),
                              "cash_journal_replay": round(rp[p]["cash"], 2),
                              "detenu_moteur": radies_detenu.get(p, 0.0)} for p in radies},
        "note": ("portefeuille = trading (moteur) + observation. Les ratios de risque "
                 "ne lisent QUE le trading ; le résidu des radiés doit être purgé."),
        "marks_sans_prix_frais": marks_stale,
        "n_evenements_rejoues": n_ev,
    }
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    os.replace(tmp, OUT)

    print("[equity] trading moteur=%.2f$ journal(replay)=%.2f$ drift=%+.2f$ | observation=%.2f$ "
          "| radies=%.2f$ | portefeuille=%.2f$ | ok=%s"
          % (book_moteur, book_journal, ecart, cash_o + val_o, cash_r + val_r,
             portefeuille, res["ok"]))
    if caisse.get("disponible"):
        _etat = {True: "OK (probant)", False: "KO " + str(caisse.get("ecart_par_paire")),
                 None: "NON PROBANT — " + str(caisse.get("raison"))}[caisse.get("ok")]
        print("[equity] LIVRE DE CAISSE (post-ancre) : ecart=%+.2f$ sur %d mouvements "
              "(ancre %s) -> %s"
              % (caisse["ecart_post_ancre_usd"], caisse["n_mouvements"],
                 caisse.get("ancre_ts"), _etat))
    else:
        print("[equity] LIVRE DE CAISSE : %s" % caisse.get("raison"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
