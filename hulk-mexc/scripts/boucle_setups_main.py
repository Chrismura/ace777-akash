#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOUCLE DES SET-UPS — REFaite À LA MAIN (ordre Christophe 23/09/2026)
=====================================================================
« tu vas reprendre toute la boucle des set ups avec donnée à la main sur les 10 derniers jours
  et les soumettre à la famille pour qu'elle valide »

CE QUE « À LA MAIN » VEUT DIRE, PRÉCISÉMENT
-------------------------------------------
Le moteur affirme des choses (prix, pire point, stop, motifs). Ici je ne reprends AUCUNE de ses
conclusions : je reprends ses **faits horodatés** (heure, prix, quantité — la seule chose que je
ne peux pas inventer) et je **recalcule tout le reste moi-même** sur les bougies 1 minute MEXC :

  1. ENTRÉE      — le prix de l'achat existe-t-il dans la bougie de cette minute ?
                   le motif (chute avant l'achat) est-il là, dans le MARCHÉ ?
                   la paire EST-ELLE dans sa fenêtre d'entrée autorisée (heure lue dans le profil) ?
  2. MISE        — ce qui a été engagé, en $ et en % de la profondeur mesurée du carnet
                   (profondeur NON historisée → quand elle manque, c'est ÉCRIT « non mesuré »)
  3. BAGS        — combien de fois, quel montant (journal) — et si zéro, on l'écrit
  4. SORTIES     — chaque sortie relue : part de la position, motif, prix vérifié dans la minute,
                   et verdict de marché (le marché est-il monté/descendu après ?)
  5. STOP        — le niveau est LU dans le motif du moteur ; je cherche MOI-MÊME la minute où le
                   marché touche ce niveau, et je mesure le retard et le coût du retard.
  6. PnL à LA MAIN — quantité réelle × (prix sortie − prix entrée), MOINS frais (5 bps/côté
                   ESTIMÉS) et spread déclaré → net. Aucun chiffre repris du moteur.
  7. VERDICT par trade : entrée conforme ? sortie justifiée ? stop honoré ?
     → un tableau par paire, et un total sur 10 jours.

⚠ CE QUI RESTE HORS DE PORTÉE (déclaré, R8) : la profondeur du carnet minute par minute n'est pas
historisée (l'échantillonneur ne stocke pas 10 jours de carnet) : la mise ne peut donc PAS être
jugée « trop grosse pour le carnet » sur le passé — elle est comparée au profil FIGÉ, avec la
mention explicite. Et les frais sont ESTIMÉS : un paper ne paie rien.

Lecture seule · 0 ordre · 0 € · klines en cache partagé avec l'oracle (mêmes clés → même data).
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
RUNS = RACINE / "runs"
PROFILS = RACINE / "strategie" / "universe_profils.json"
# Fenêtres de creux par paire : LA MÊME source que le moteur (`fenetre_entree_ok`), lue à la
# source et pas devinée. Chaque paire porte des heures UTC en texte ("07", "08", "09"…).
CARTE_ENTREE = RACINE / "strategie" / "carte_fenetres_entree.json"
FRAIS_BPS_COTE = 5.0            # ESTIMÉ (déclaré) : ce que paierait un ordre réel


# ── utilitaires (mêmes clés de cache que oracle_independant.py → data identique)

def _oracle_klines(pair: str, de_ms: int, a_ms: int):
    """Réutilise EXACTEMENT la même fonction/cache que l'oracle : une seule vérité de marché."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("oracle", RACINE / "scripts" / "oracle_independant.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["oracle"] = mod
    spec.loader.exec_module(mod)
    return mod.klines(pair, de_ms, a_ms, False)


def ts_ms(iso: str) -> int:
    return int(datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp() * 1000)


def iso(ms) -> str:
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def profil(paire: str) -> dict:
    try:
        d = json.loads(PROFILS.read_text(encoding="utf-8"))
        return d.get(paire) or {}
    except Exception:
        return {}


def fenetres_paire(paire: str) -> tuple[list, str]:
    """Heures UTC de creux de CETTE paire, LUES dans la carte du moteur.

    ⚠ LIMITE DÉCLARÉE (E8) : la carte est celle d'AUJOURD'HUI ; les fenêtres sont refaites
    périodiquement (« finitions sur données fraîches »). L'appliquer à un trade d'il y a dix
    jours est INDICATIF, pas une preuve — le contrôle est donc étiqueté comme tel.
    """
    try:
        d = json.loads(CARTE_ENTREE.read_text(encoding="utf-8"))
        ent = (d.get("paires") or {}).get(paire) or {}
        fen = [str(x).split(":")[0].zfill(2) for x in (ent.get("fenetre_entree_utc") or [])]
        return fen, (d.get("ts") or "ts inconnu")
    except Exception:
        return [], "carte illisible"


def fentre(kl, de_ms, a_ms):
    return [k for k in kl if de_ms <= int(k[0]) < a_ms]


def dans_la_bougie(kl, t_ms: int, prix: float):
    """Le prix existe-t-il dans la bougie de cette minute ? (contrôle À LA MAIN du prix)"""
    w = fentre(kl, t_ms, t_ms + 60_000)
    if not w:
        return None
    k = w[0]
    bas, haut = float(k[3]), float(k[2])
    return bas <= prix <= haut


def _cfg() -> dict:
    """Lit config/defaults.env — la VALEUR EFFECTIVE, jamais le défaut du code (E18)."""
    out = {}
    p = RACINE / "config" / "defaults.env"
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            l = l.strip()
            if l and not l.startswith("#") and "=" in l:
                k, v = l.split("=", 1)
                out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def cadence_mediane_par_paire() -> dict:
    """Cadence de chaque paire, telle que le MOTEUR l'écrit dans son journal (colonne `cadence`).

    POURQUOI ELLE EST LÀ (classe E20, 23/09) : cet instrument comparait les entrées au
    **plancher du profil** (`calib.dip_pct`) — c'est le motif exact de la classe E17, et le
    gardien `verif_seuil_moteur.py` l'a signalé TOUT SEUL. Le seuil de repli que le moteur
    applique n'est pas le plancher : c'est
        dip = max( dip_pct_du_profil ; DIP_CADENCE_MULT × cadence_de_la_paire )
    et la porte finale `max(dip ; IMPULSE_PULLBACK_MIN_PCT ; IMPULSE_PULLBACK_FRAC × m6)`.
    Sans le terme cadence, RIZE (cadence ~55 %) était jugée sur 4,2 % au lieu de ~28 %.
    """
    import statistics as _st
    vals: dict[str, list] = {}
    p = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda x: x.stat().st_mtime)[-1]
    with p.open(newline="", encoding="utf-8", errors="replace") as f:
        for r in csv.reader(f):
            if len(r) < 10 or r[0] == "ts":
                continue
            v = (r[9] or "").strip()
            if not v:
                continue
            try:
                vals.setdefault(r[1], []).append(float(v))
            except Exception:
                continue
    return {k: round(_st.median(v), 2) for k, v in vals.items() if v}


def seuil_entree_effectif(calib: dict, cfg: dict, cadence: float | None, m6: float | None) -> dict:
    """LA formule du moteur, terme par terme (reproduite de `score_pair`, jamais devinée).

    Renvoie chaque terme SÉPARÉMENT pour qu'on puisse voir lequel décide (déterminance R15) :
    publier seulement le résultat final, c'est ce qui m'a fait prendre un plancher pour un seuil.
    """
    plancher = float(calib.get("dip_pct") if calib.get("dip_pct") is not None
                     else cfg.get("DIP_FLOOR_PCT", "2.5"))
    mult = float(cfg.get("DIP_CADENCE_MULT", "0.50"))
    t_cad = (cadence or 0.0) * mult
    dip = max(plancher, t_cad)
    # R20.2 / E23 — LE TERME PULLBACK DU PROFIL PAR PAIRE, pas le plancher global.
    # Le moteur lit `_cal.get("impulse_pullback_min_pct", cfg.get("IMPULSE_PULLBACK_MIN_PCT"))`
    # (paper_diprip.py:649). J'utilisais le global 5,0 partout : pour BTC (profil 1,5) je
    # surestimais le seuil exigé de 2,55 pt et je sous-comptais les entrées conformes.
    _pp = calib.get("impulse_pullback_min_pct")
    t_pull = float(_pp if _pp is not None else cfg.get("IMPULSE_PULLBACK_MIN_PCT", "5"))
    t_m6 = abs(m6 or 0.0) * float(cfg.get("IMPULSE_PULLBACK_FRAC", "0.30"))
    besoin = max(dip, t_pull, t_m6)
    termes = {"plancher_profil": plancher, "DIP_CADENCE_MULT × cadence": t_cad,
              ("pullback profil" if _pp is not None else "IMPULSE_PULLBACK_MIN_PCT"): t_pull,
              "IMPULSE_PULLBACK_FRAC × m6": t_m6}
    dominant = max(termes.items(), key=lambda kv: kv[1])[0]
    return {"plancher": round(plancher, 2), "terme_cadence": round(t_cad, 2),
            "dip": round(dip, 2), "besoin": round(besoin, 2), "terme_dominant": dominant,
            "mult": mult}


def lire_sequences(depuis: str) -> dict:
    p = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda x: x.stat().st_mtime)[-1]
    pp: dict[str, list] = {}
    for r in csv.reader(p.open(newline="", encoding="utf-8", errors="replace")):
        if len(r) < 11 or r[0] == "ts" or r[0] < depuis:
            continue
        if r[2] not in ("BUY", "SELL", "SELL_PARTIAL", "STOP", "BAG_ARM", "BAG_CRASH", "BAG_SELL"):
            continue
        # `ts_prix_utc` (colonne 11, ajoutée par GO 2) = L'HEURE À LAQUELLE LE PRIX A ÉTÉ LU.
        # C'est ELLE qu'il faut comparer à la bougie, PAS l'heure d'écriture de la ligne :
        # classe E25 (23/09) — j'ai jugé 57/141 prix « hors bougie » alors qu'ils étaient TOUS
        # à ±1-2 min du bon candle à cause du délai d'écriture (ex. ligne 14:14:23Z, prix lu
        # 14:13:44Z). 0 prix était vraiment hors marché : c'était MA mesure qui décalait.
        _tsp = str(r[11]) if len(r) > 11 and str(r[11])[:2] == "20" else None
        pp.setdefault(r[1], []).append({
            "ts": r[0], "event": r[2], "price": float(r[4] or 0),
            "ts_prix": _tsp,
            "entry": float(r[5] or 0) if r[5] else None, "qty": float(r[6] or 0),
            "pnl": float(r[7] or 0), "regime": r[3], "reason": r[10],
        })
    seqs = {}
    for paire, evs in pp.items():
        cur = None
        for e in evs:
            if e["event"] == "BUY":
                if cur and cur["sorties"]:
                    seqs.setdefault(paire, []).append(cur)
                cur = {"paire": paire, "buy": e, "sorties": [], "bags": []}
            elif cur is not None:
                if e["event"].startswith("BAG"):
                    cur["bags"].append(e)
                else:
                    cur["sorties"].append(e)
        if cur and cur["sorties"]:
            seqs.setdefault(paire, []).append(cur)
    return seqs


def lire_prix_observes(depuis: str) -> dict:
    """LES PRIX QUE LE MOTEUR A RÉELLEMENT VUS, paire par paire (classe E24, 23/09/2026).

    POURQUOI CETTE FONCTION EXISTE : `lire_sequences` ne garde que BUY/SELL/… — donc les
    lignes SKIP (le prix lu À CHAQUE CYCLE) étaient invisibles. Résultat : le contrôle des
    stops cherchait la MÈCHE d'une bougie 1 min sous le niveau, alors que LE MOTEUR ne
    déclenche que sur `chg <= -stop` évalué sur **le prix ponctuel du cycle**
    (`paper_diprip.py:2581`). Il a donc déclaré « 4 stops sur 15 non honorés » avec des retards
    de 88 min et 303 min pour un coût réel de 0,0055 $ — une FAUSSE ACCUSATION : le moteur
    avait vendu au niveau, la mèche n'a jamais été vue par personne.
    On mesure donc avec CE QUE LE MOTEUR A VU. La mesure « bougie » reste affichée À CÔTÉ.

    Renvoie {paire: [(ts_iso, ts_ms, prix), …]} pour TOUTES les lignes portant un prix > 0.
    """
    p = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda x: x.stat().st_mtime)[-1]
    obs: dict = {}
    for r in csv.reader(p.open(newline="", encoding="utf-8", errors="replace")):
        if len(r) < 11 or r[0] == "ts" or r[0] < depuis:
            continue
        try:
            prix = float(r[4] or 0)
        except Exception:
            continue
        if prix <= 0:
            continue
        try:
            obs.setdefault(r[1], []).append((r[0], ts_ms(r[0]), prix))
        except Exception:
            continue
    return obs


def dans_la_bougie_tol(kl, t_ms: int, prix: float, tol_min: int = 1):
    """Le prix tombe-t-il dans la bougie de SA minute, ou dans une VOISINE (± tol_min) ?

    JUSTIFICATION MESURÉE (classe E25, 23/09/2026) : le moteur écrit la ligne APRÈS avoir lu le
    prix (délai mesuré : ligne 14:14:23Z pour un prix lu à 14:13:44Z, soit 39 s). Juger sur
    l'heure d'ÉCRITURE fabriquait "57/141 prix hors bougie" alors que les 57 tombent TOUS dans
    un candle voisin (±1-2 min vérifié) — **0 prix vraiment hors marché**. On tolère donc la
    minute voisine, et le strict reste compté À CÔTÉ pour que l'écart reste visible.
    """
    for d in (0, -60_000, 60_000):
        if dans_la_bougie(kl, t_ms + d, prix) is True:
            return True
    return dans_la_bougie(kl, t_ms, prix)


def t_prix_effectif(e: dict) -> int:
    """L'heure de LECTURE du prix (colonne `ts_prix_utc`, GO 2), sinon l'heure de la ligne.

    Classe E25 : comparer l'heure d'ÉCRITURE à la bougie fabriquait 57 fausses « hors bougie ».
    """
    try:
        if e.get("ts_prix"):
            return ts_ms(e["ts_prix"])
    except Exception:
        pass
    return ts_ms(e["ts"])


def premier_prix_visible(observations: list, t_b: int, t_s: int, seuil: float):
    """Premier prix que le moteur a VU sous le seuil, entre l'achat et la sortie."""
    for ts_iso, t, prix in observations:
        if t_b <= t <= t_s and prix <= seuil:
            return t, ts_iso
    return None, None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=float, default=10.0)
    ap.add_argument("--json", default=None)
    ap.add_argument("--txt", default=None)
    a = ap.parse_args()

    _b = datetime.now(timezone.utc) - timedelta(days=a.jours)
    depuis = _b.replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
    seqs = lire_sequences(depuis)
    obs = lire_prix_observes(depuis)
    print(f"BOUCLE DES SET-UPS À LA MAIN — {a.jours:g} j (depuis {depuis}) · "
          f"{sum(len(v) for v in seqs.values())} séquences · {len(seqs)} paires")

    lignes, par_paire, totaux = [], {}, {"n": 0, "brut_moteur": 0.0, "brut_main": 0.0,
                                         "couts": 0.0, "net_main": 0.0,
                                         "entree_conforme": 0, "sortie_justifiee": 0,
                                         "stop_ok": 0, "stop_n": 0, "prix_verifies": 0, "prix_n": 0,
                                         "hors_fenetre": 0, "hors_fenetre_non_verifiable": 0}
    _C = _cfg()
    _CAD = cadence_mediane_par_paire()
    print(f"  (seuil d'entrée EFFECTIF = max(plancher ; DIP_CADENCE_MULT {_C.get('DIP_CADENCE_MULT')} × "
          f"cadence) puis porte pullback — le plancher du profil n'est PAS le seuil, E17/E20)")
    for paire in sorted(seqs):
        pr = profil(paire)
        calib = pr.get("calib") or {}
        dip_exige = float(calib.get("dip_pct") or 0.0)
        _se_pre = seuil_entree_effectif(calib, _C, _CAD.get(paire), None)
        fen, _ts_carte = fenetres_paire(paire)
        ts = [ts_ms(s["buy"]["ts"]) for s in seqs[paire]] + \
             [ts_ms(o["ts"]) for s in seqs[paire] for o in s["sorties"]]
        kl = _oracle_klines(paire, min(ts) - 3600_000, max(ts) + 6 * 3600_000)
        st = par_paire.setdefault(paire, {"n": 0, "brut": 0.0, "net": 0.0, "entree_ok": 0,
                                          "sortie_ok": 0, "stop_ok": 0, "stop_n": 0,
                                          "prix_ko": 0, "dip_exige": dip_exige,
                                          "dip_requis": _se_pre["besoin"],
                                          "dip_terme_dominant": _se_pre["terme_dominant"],
                                          "pnl_jours": {}})
        for s in seqs[paire]:
            b, sorties = s["buy"], s["sorties"]
            t_b, p_b = ts_ms(b["ts"]), b["price"]
            qty = sum(o["qty"] for o in sorties)
            if qty <= 0:
                continue
            p_s = sum(o["price"] * o["qty"] for o in sorties) / qty
            t_s = ts_ms(sorties[-1]["ts"])
            brut_moteur = sum(o["pnl"] for o in sorties)
            brut_main = qty * (p_s - p_b)
            spread = 0.0
            for o in sorties:
                m = re.search(r"spread=([0-9.]+)bps", o["reason"])
                if m:
                    spread = float(m.group(1))
            couts = qty * ((p_b + p_s) / 2) * (2 * FRAIS_BPS_COTE + spread) / 10000.0
            # ── 1. entrée : prix vérifié + motif de marché recalculé à la main
            # E25 : on juge sur l'heure de LECTURE du prix ; la comparaison sur l'heure
            # d'ÉCRITURE est conservée À CÔTÉ pour que l'écart entre les deux soit visible.
            prix_ok = dans_la_bougie_tol(kl, t_prix_effectif(b), p_b)
            prix_ok_strict = dans_la_bougie(kl, t_prix_effectif(b), p_b)
            w15 = fentre(kl, t_b - 15 * 60_000, t_b)
            chute_15 = ((max(float(k[2]) for k in w15) - p_b) / max(float(k[2]) for k in w15) * 100) if w15 else None
            # La famille `impulsion/pullback` annonce sa propre condition sur SIX minutes
            # (`dd6=…`) : on mesure les DEUX fenêtres, et la baisse retenue est la plus forte
            # des deux — sinon on compare le motif à une fenêtre qui n'est pas la sienne.
            w6 = fentre(kl, t_b - 6 * 60_000, t_b)
            chute_6 = ((max(float(k[2]) for k in w6) - p_b) / max(float(k[2]) for k in w6) * 100) if w6 else None
            chute_retenue = max([c for c in (chute_6, chute_15) if c is not None], default=None)
            # LE SEUIL CONTRE LEQUEL ON JUGE : celui du moteur, terme cadence INCLUS (E20).
            _se = seuil_entree_effectif(calib, _C, _CAD.get(paire), chute_6)
            motif_ok = (chute_retenue is not None) and (chute_retenue >= _se["besoin"])
            # FAMILLE DE MOTIF D'ENTRÉE, lue dans le motif que le moteur écrit lui-même.
            # ⚠ CONTRÔLE RETIRÉ LE 23/09 (et la raison écrite pour qu'il ne revienne pas) :
            # j'ai d'abord compté « 48/60 trades HORS fenêtre de creux » en comparant CHAQUE
            # achat aux heures de creux de la carte. FAUX : la porte d'heure ne gouverne qu'un
            # mode d'entrée ; les achats de type `impulse_pullback` (mesuré : TEL 18/09
            # 23:51Z, motif `impulse_pullback_dd6=5.1>=5.0`) ont leur PROPRE condition et ne
            # relèvent pas de la fenêtre. Publier 80 % d'infractions aurait été une accusation
            # non vérifiée de plus (E17). Le motif de la fenêtre n'est donc PAS jugé ici :
            # il est compté par FAMILLE, et la carte est citée pour information.
            _mo = b["reason"] or ""
            famille = ("impulsion/pullback" if _mo.startswith("impulse_pullback") else
                       "re-entrée après dump" if _mo.startswith("reentry_dump") else
                       "remploi de cash" if _mo.startswith("cash_redeploy") else
                       "seed d'inventaire" if _mo.startswith("SEED_START") else
                       "autre: " + _mo.split("(")[0][:24])
            heures_creux_carte, ts_carte = fenetres_paire(paire)
            heure_ok = None      # non jugé (voir ci-dessus) — déclaré, pas caché
            # ── 4. sorties : chaque prix vérifié dans sa minute, verdict de marché
            sorties_det, n_prix_ko = [], 0
            for o in sorties:
                to = ts_ms(o["ts"])
                ok = dans_la_bougie_tol(kl, t_prix_effectif(o), o["price"])
                ok_strict = dans_la_bougie(kl, t_prix_effectif(o), o["price"])
                if ok is False:
                    n_prix_ko += 1
                apres = fentre(kl, to, to + 3600_000)
                v = None
                if apres:
                    pb_ = min(float(k[3]) for k in apres)
                    ph_ = max(float(k[2]) for k in apres)
                    b_ = (pb_ - o["price"]) / o["price"] * 100
                    h_ = (ph_ - o["price"]) / o["price"] * 100
                    v = ("bien vendu" if (b_ <= -1 and b_ <= -h_) else
                         "vendu tôt" if h_ >= 1 else "neutre")
                sorties_det.append({"ts": o["ts"], "motif": o["reason"][:60],
                                    "part": round(o["qty"] / qty * 100, 1),
                                    "prix_dans_la_bougie": ok,
                                    "prix_dans_la_bougie_strict": ok_strict,
                                    "verdict_marche": v})
                # INC-C — LE MOTIF DE SORTIE, LU DANS CE QUE LE MOTEUR ÉCRIT (exigence du jury :
                # un `exit_reason` par sortie). Le moteur écrit TOUJOURS un motif ; ce qui est
                # mesuré ici, c'est LAQUELLE de ses sorties est « justifiée par le marché ».
                # Dire « 42 sorties inexpliquées » était MON mot imprécis : elles ont un motif.
                _mo = (o["reason"] or "").split("_")[0].split("-")[0].split("(")[0][:18] or "?"
                totaux.setdefault("motifs", {}).setdefault(_mo, {"n": 0, "pnl": 0.0,
                                                                 "justes": 0})
                totaux["motifs"][_mo]["n"] += 1
                totaux["motifs"][_mo]["pnl"] += float(o.get("pnl") or 0.0)
                if v == "bien vendu":
                    totaux["motifs"][_mo]["justes"] += 1
            sortie_ok = sum(1 for d in sorties_det if d["verdict_marche"] == "bien vendu")
            # ── 5. stop : niveau LU dans le motif, contact trouvé À LA MAIN
            nom = None
            for o in sorties:
                m = re.search(r"stop[_-]([0-9.]+)%", o["reason"])
                if m:
                    nom = float(m.group(1))
                    break
            stop = {"nominal_pct": nom}
            if nom:
                seuil = p_b * (1 - nom / 100)
                # ⚠️ E24 (23/09/2026) — LA MESURE A ÉTÉ CORRIGÉE APRÈS AVOIR ACCUSÉ LE MOTEUR À TORT.
                # AVANT : on cherchait la MÈCHE d'une bougie (`low <= seuil`) → « 4 stops/15 non
                # honorés », retards 88 min et 303 min… pour un coût réel de 0,0055 $ et 0,0082 $.
                # OR le moteur déclenche sur `chg <= -stop` avec LE PRIX PONCTUEL DU CYCLE
                # (paper_diprip.py:2581) : une mèche qu'aucun cycle n'a vue n'existe pas pour lui.
                # MAINTENANT : (a) le verdict est rendu sur LE PREMIER PRIX QUE LE MOTEUR A VU sous
                # le seuil (lignes du journal, prix observés à chaque cycle) ; (b) la mesure bougie
                # reste affichée À CÔTÉ, étiquetée, pour que l'écart entre les deux soit VISIBLE.
                chemin = fentre(kl, t_b, t_s)
                touche_b = next((k for k in chemin if float(k[3]) <= seuil), None)
                t_vis, ts_vis = premier_prix_visible(obs.get(paire, []), t_b, t_s, seuil)
                if t_vis is not None:
                    retard = round((t_s - t_vis) / 60_000, 1)
                    stop.update({"touche_a": ts_vis, "retard_min": retard,
                                 "criterion": "prix observé par le moteur (cycle)",
                                 "honore": retard <= 2,
                                 "cout_retard_usdt": round(max(0.0, seuil - p_s) * qty, 4)})
                    if touche_b:
                        stop["bougie_mouche_a"] = iso(int(touche_b[0]))
                        stop["bougie_retard_min"] = round((t_s - int(touche_b[0])) / 60_000, 1)
                        stop["ecart_bougie_visible_min"] = round(
                            (int(touche_b[0]) - t_vis) / 60_000, 1)
                    totaux["stop_n"] += 1
                    st["stop_n"] += 1
                    if retard <= 2:
                        totaux["stop_ok"] += 1
                        st["stop_ok"] += 1
                elif touche_b:
                    # le niveau a été touché en MÈCHE mais JAMAIS vu par un cycle → non imputable
                    stop.update({"touche_a": iso(int(touche_b[0])),
                                 "criterion": "mèche de bougie seulement",
                                 "honore": None,
                                 "note": "mèche non vue par un cycle — non imputable au moteur (E24)"})
                else:
                    stop["note"] = "niveau jamais atteint par le marché avant la sortie"
            # ── totaux
            totaux["n"] += 1
            totaux["brut_moteur"] += brut_moteur
            totaux["brut_main"] += brut_main
            totaux["couts"] += couts
            totaux["net_main"] += brut_main - couts
            totaux["entree_conforme"] += 1 if motif_ok else 0
            totaux["sortie_justifiee"] += 1 if sortie_ok else 0
            totaux["prix_n"] += 1 + len(sorties)
            totaux["prix_verifies"] += (1 if prix_ok else 0) + sum(1 for d in sorties_det if d["prix_dans_la_bougie"])
            totaux.setdefault("prix_verifies_strict", 0)
            totaux["prix_verifies_strict"] += ((1 if prix_ok_strict else 0)
                                               + sum(1 for d in sorties_det
                                                     if d.get("prix_dans_la_bougie_strict")))
            if heure_ok is False:
                totaux["hors_fenetre"] += 1
            elif heure_ok is None:
                totaux["hors_fenetre_non_verifiable"] += 1
            st["n"] += 1
            st["brut"] += brut_moteur
            st["net"] += brut_main - couts
            st["entree_ok"] += 1 if motif_ok else 0
            st["sortie_ok"] += 1 if sortie_ok else 0
            st["prix_ko"] += n_prix_ko
            j = b["ts"][:10]
            st["pnl_jours"][j] = round(st["pnl_jours"].get(j, 0.0) + brut_moteur, 4)
            # CONTRÔLE PAR FAMILLE (et pas global) : une condition de baisse ne s'applique QU'AUX
            # familles qui l'annoncent. Compté globalement, « 28 % d'entrées conformes » ferait
            # porter à `cash_redeploy` (remploi de cash — aucune condition de baisse annoncée) une
            # faute qu'il ne commet pas. Même piège que le faux « 80 % hors fenêtre » : on le
            # sépare AVANT de publier (E17).
            fam_stats = totaux.setdefault("familles", {}).setdefault(
                famille, {"n": 0, "avec_chute": 0, "chutes": [], "seuils": []})
            fam_stats["n"] += 1
            if chute_retenue is not None:
                fam_stats["chutes"].append(round(chute_retenue, 2))
                # LE SEUIL EST CELUI DE LA PAIRE, calculé (E20) — plus un « 2 % » plat.
                fam_stats["seuils"].append(_se["besoin"])
                if chute_retenue >= _se["besoin"]:
                    fam_stats["avec_chute"] += 1
            lignes.append({
                "paire": paire, "achat": b["ts"], "prix_entree": p_b, "mise_usdt": round(qty * p_b, 2),
                "regime": b["regime"], "motif_achat": b["reason"][:50],
                "famille_motif": famille, "heures_creux_carte": heures_creux_carte,
                "carte_ts": ts_carte,
                "qty": round(qty, 6), "n_sorties": len(sorties), "n_bags": len(s["bags"]),
                "sortie": sorties[-1]["ts"], "prix_sortie": round(p_s, 10),
                "duree_min": round((t_s - t_b) / 60_000, 1),
                "prix_entree_dans_la_bougie": prix_ok,
                "chute_6m_pct": (round(chute_6, 3) if chute_6 is not None else None),
                "chute_15m_pct": (round(chute_15, 3) if chute_15 is not None else None),
                "chute_retenue_pct": (round(chute_retenue, 3) if chute_retenue is not None else None),
                "dip_plancher_profil_pct": _se["plancher"],
                "dip_terme_cadence_pct": _se["terme_cadence"],
                "dip_effectif_pct": _se["dip"], "dip_requis_pct": _se["besoin"],
                "dip_terme_dominant": _se["terme_dominant"],
                "cadence_mediane_pct": _CAD.get(paire),
                "dip_exige_profil_pct": _se["plancher"],   # ANCIEN nom, gardé : c'était le PLANCHER
                "motif_entree_conforme": motif_ok,
                "heure_dans_fenetre": heure_ok,
                "brut_moteur": round(brut_moteur, 4), "brut_main": round(brut_main, 4),
                "spread_declare_bps": spread, "couts_estimes": round(couts, 4),
                "net_main": round(brut_main - couts, 4), "sorties": sorties_det, "stop": stop,
            })

    # ── restitution
    L = [f"BOUCLE DES SET-UPS, REFaite À LA MAIN — {a.jours:g} derniers jours "
         f"· {totaux['n']} trades · {len(par_paire)} paires",
         "Source : prix/heures/quantités du journal (faits horodatés) + bougies 1 min MEXC.",
         "Tout le reste est recalculé à la main (aucune conclusion du moteur reprise).", ""]
    L.append("=== 1. PAR PAIRE (10 jours) ===")
    L.append(f"{'paire':<12}{'n':>4}{'brut $':>9}{'net main $':>12}{'entrée conf.':>14}"
             f"{'sorties justes':>16}{'stop honoré':>13}{'prix hors bougie':>18}")
    for p in sorted(par_paire, key=lambda x: -par_paire[x]["brut"]):
        d = par_paire[p]
        L.append(f"{p:<12}{d['n']:>4}{d['brut']:>9.2f}{d['net']:>12.2f}"
                 f"{str(d['entree_ok']) + '/' + str(d['n']):>14}"
                 f"{str(d['sortie_ok']) + '/' + str(d['n']):>16}"
                 f"{(str(d['stop_ok']) + '/' + str(d['stop_n'])) if d['stop_n'] else '—':>13}"
                 f"{d['prix_ko']:>18}")
    L.append("")
    L.append("=== 2. TOTAUX 10 JOURS (à la main) ===")
    L.append(f"  trades                                    : {totaux['n']}")
    L.append(f"  entrées conformes au motif (marché)        : {totaux['entree_conforme']} "
             f"/ {totaux['n']}  ({totaux['entree_conforme'] / max(1, totaux['n']) * 100:.0f} %)")
    L.append("")
    L.append("=== 2bis. LE MOTIF D'ENTRÉE, PAR FAMILLE (une condition de baisse ne s'applique "
             "qu'aux familles qui l'annoncent) ===")
    L.append(f"{'famille':<34}{'n':>4}{'chute ≥ seuil EFFECTIF de la paire':>34}{'chute médiane':>16}"
             f"{'seuil médian':>14}")
    for k, d in sorted((totaux.get("familles") or {}).items(), key=lambda t: -t[1]["n"]):
        ch = sorted(d["chutes"])
        se = sorted(d.get("seuils") or [])
        med = ch[len(ch) // 2] if ch else None
        med_s = se[len(se) // 2] if se else None
        L.append(f"{k:<34}{d['n']:>4}"
                 f"{str(d['avec_chute']) + '/' + str(d['n']):>34}"
                 f"{(str(med) + ' %') if med is not None else '—':>16}"
                 f"{(str(med_s) + ' %') if med_s is not None else '—':>14}")
    L.append("  ⚠ PORTÉE DE LA COLONNE « chute ≥ seuil » : la chute est mesurée sur les bougies "
             "1 min (plus haut de la fenêtre → prix d'achat). Le moteur, lui, écrit SON PROPRE "
             "`dd6` dans le motif (ex. `impulse_pullback_dd6=5.1>=5.0`). Ce ne sont PAS la même "
             "grandeur : la ligne `impulsion/pullback` et `re-entrée` sont donc INDICATIVES, "
             "pas une preuve d'infraction — la preuve d'un franchissement, c'est le dd6 que le "
             "moteur écrit lui-même, et il faudra la lire là (travail NON fait, déclaré).")
    L.append("  ⚠ E20 (23/09) : la colonne de gauche compare la baisse de la paire au seuil d'entrée "
             "EFFECTIF du moteur, calculé (`max(plancher ; DIP_CADENCE_MULT × cadence)` puis porte "
             "pullback) — AVANT, elle comparait à un « 2 % » plat, et le compteur global à "
             "`plancher × 0,5` : deux chiffres faux (28 % d'entrées « conformes » au lieu de 5 %). "
             "Le compteur GLOBAL reste trompeur et est déclaré tel quel : `cash_redeploy` n'a AUCUNE "
             "condition de baisse annoncée, la ligne PAR FAMILLE est la seule lecture loyale.")
    L.append("  ⚠ le contrôle « hors fenêtre de creux » a été RETIRÉ : il comparait les achats "
             "à une porte qui ne les gouverne pas (motif impulsion/pullback) — 48/60 aurait été "
             "une accusation non vérifiée (E17).")
    L.append(f"  sorties justifiées par le marché (bien)     : {totaux['sortie_justifiee']} "
             f"/ {totaux['n']}  ({totaux['sortie_justifiee'] / max(1, totaux['n']) * 100:.0f} %)")
    # INC-C — TABLE DES MOTIFS DE SORTIE (exigence du jury : un exit_reason par sortie).
    # « 42 sorties inexpliquées » était MON mot : le moteur écrit TOUJOURS un motif. Ce qui
    # manquait, c'est la table qui les nomme un par un — la voici.
    L.append("")
    L.append("=== 3bis. INC-C — LE MOTIF DE CHAQUE SORTIE (lu dans le journal) ===")
    L.append(f"  {'motif':<22}{'n':>5}{'PnL brut $':>13}{'justes marché':>15}")
    _tot = 0
    for _m, _d in sorted((totaux.get("motifs") or {}).items(), key=lambda kv: -kv[1]["n"]):
        _tot += _d["n"]
        L.append(f"  {_m:<22}{_d['n']:>5}{_d['pnl']:>13.2f}"
                 f"{(str(_d['justes']) + '/' + str(_d['n'])):>15}")
    _sans = (totaux.get("motifs") or {}).get("?", {}).get("n", 0)
    L.append(f"  {'TOTAL':<22}{_tot:>5}   dont SANS motif lisible : {_sans}"
             + (" ✔ (le moteur écrit toujours son motif)" if _sans == 0 else
                " → à expliquer : une sortie sans motif"))
    L.append(f"  stops honorés (≤ 2 min après le 1er prix VU par le moteur) : "
             f"{totaux['stop_ok']} / {totaux['stop_n']}")
    L.append("  ⚠ E24 (23/09) : le critère AVANT cherchait la MÈCHE d'une bougie ; le moteur, lui,"
             " déclenche sur le PRIX PONCTUEL du cycle (paper_diprip.py:2581). Le critère est"
             " désormais le 1er prix que le moteur a VU sous le seuil ; la mesure bougie reste"
             " écrite à côté (`bougie_retard_min`, `ecart_bougie_visible_min`).")
    L.append(f"  prix vérifiés dans leur bougie (± 1 min, tolérance du délai d'écriture) : "
             f"{totaux['prix_verifies']} / {totaux['prix_n']}  "
             f"({totaux['prix_verifies'] / max(1, totaux['prix_n']) * 100:.1f} %)")
    L.append(f"  ⚠ E25 (23/09) — le MÊME contrôle en STRICT (minute exacte de l'heure d'écriture)"
             f" donnait {totaux.get('prix_verifies_strict', 0)} / {totaux['prix_n']} : ce n'était PAS"
             " de la donnée corrompue mais le DÉLAI D'ÉCRITURE (mesuré : ligne 14:14:23Z, prix lu"
             " 14:13:44Z). Les 57 prix jugés « hors bougie » tombent TOUS dans un candle voisin"
             " (±1-2 min vérifié) — 0 prix vraiment hors marché. INC-A était une FAUSSE ALARME.")
    L.append("")
    L.append("=== 3. LE PnL, RECALCULÉ À LA MAIN ===")
    L.append(f"  brut inscrit par le moteur : {totaux['brut_moteur']:+8.2f} $")
    L.append(f"  brut recalculé à la main   : {totaux['brut_main']:+8.2f} $ "
             f"(écart {totaux['brut_main'] - totaux['brut_moteur']:+.4f} $)")
    L.append(f"  coûts ESTIMÉS (frais 5 bps/côté + spread déclaré) : {totaux['couts']:.2f} $")
    L.append(f"  NET à la main              : {totaux['net_main']:+8.2f} $")
    L.append("")
    L.append("=== 4. LES 10 TRADES LES PLUS COÛTEUX (vus à la main) ===")
    for t in sorted(lignes, key=lambda x: x["brut_moteur"])[:10]:
        L.append(f"  {t['paire']:12} {t['achat']}  {t['mise_usdt']:>7.2f} $ · "
                 f"sortie {t['duree_min']:>7.0f} min · brut {t['brut_moteur']:+7.2f} $ · net main "
                 f"{t['net_main']:+7.2f} $ · chute avant achat "
                 f"{t['chute_retenue_pct'] if t['chute_retenue_pct'] is not None else '?'} % "
                 f"(exigé {t['dip_requis_pct']} % [plancher {t['dip_plancher_profil_pct']} · "
                 f"cadence {t['dip_terme_cadence_pct']} · dominant {t['dip_terme_dominant']}]) "
                 f"· entrée conforme={t['motif_entree_conforme']}"
                 f" · stop {t['stop'].get('verdict_stop') or ('honoré' if t['stop'].get('honore') else t['stop'].get('note', '—'))}")
    texte = "\n".join(L)
    print("\n" + texte)
    if a.txt:
        Path(a.txt).write_text(texte + "\n", encoding="utf-8")
    if a.json:
        Path(a.json).write_text(json.dumps({
            "instrument": "boucle_setups_main.py",
            "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "fenetre_jours": a.jours, "depuis": depuis, "frais_bps_cote_estimes": FRAIS_BPS_COTE,
            "totaux": {k: (round(v, 4) if isinstance(v, float) else v) for k, v in totaux.items()},
            "par_paire": par_paire, "trades": lignes,
            "limites_declarees": [
                "Profondeur de carnet non historisée : la mise n'est PAS jugée contre le carnet "
                "du moment, seulement mise en regard du profil.",
                "Frais ESTIMÉS (un paper ne paie rien) ; spread lu dans le motif de vente.",
                "« motif conforme » = chute de marché ≥ max(0,5 % ; moitié du dip du profil) avant "
                "l'achat — seuil de PROCESSUS, pas de rentabilité.",
                "La fenêtre d'entrée n'est vérifiée que si le profil en porte une lisible.",
            ],
            "lecture_seule": True, "ordres": 0,
        }, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
