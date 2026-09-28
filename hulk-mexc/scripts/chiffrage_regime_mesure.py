#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_REGIME_MESURE.py — R17 : les seuils de RÉGIME sont-ils justes pour chaque paire ?

QUESTION (GO Christophe 22/09 : « mesurer QUIET_RANGE_PCT et SPIKE_15D_PCT dans l'unité de
chaque paire, même méthode que la sortie, et chiffrer AVANT de toucher ») :

  Le moteur classe le RÉGIME d'une paire — et le régime décide si on a le droit d'entrer —
  avec DEUX pourcentages UNIVERSELS :
      QUIET  si  range15 < QUIET_RANGE_PCT (8 %)  ET  move24 < 8 % × 0,6
      SPIKE  si  range15 ≥ SPIKE_15D_PCT (25 %)  OU  move24 ≥ impulse_pct(paire)
  Or une paire vit de 2,37 %/jour (RWA) à 49 %/jour : **21× d'écart**. Le MÊME 8 % ne dit pas
  la même chose sur les deux.

MÉTHODE (la même que pour la sortie — une seule grandeur MESURÉE, une seule échelle) :
  quiet_échelle  = range15 < (QUIET_RANGE_PCT / cadence_de_référence) × cadence_de_la_paire
  spike_échelle  = range15 ≥ (SPIKE_15D_PCT / cadence_de_référence) × cadence_de_la_paire
  → la règle reste la même ; on la lit dans l'unité de la paire au lieu d'un % universel.
  La référence est la MÉDIANE des cadences mesurées de l'univers (imprimée), comme pour la sortie.

CE QU'ON MESURE, barre par barre, sur 45 j de bougies 1 h RÉELLES :
  1. la fréquence de chaque régime sous la règle ACTUELLE vs sous la règle relue ;
  2. les barres où les deux règles DONNENT UN RÉGIME DIFFÉRENT (les « désaccords ») ;
  3. ce que le prix a fait APRÈS ces barres (MFE 24 h = occasion, MAE 24 h = risque) :
     - un désaccord qui BLOQUE (nouveau QUIET) doit avoir un avenir NÉGATIF pour être un gain ;
     - un désaccord qui OUVRE (nouveau COOLING/IMPULSE) doit avoir un avenir POSITIF.

LIMITES ÉCRITES (E8) : on isole l'effet du CHANGEMENT DE CLASSIFICATION — la chaîne d'entrée
complète (dip, murs, volume, fusible, fenêtre) n'est PAS rejouée → le $ est une BORNE HAUTE,
pas un PnL. 45 j = une composition de régimes. Les paires sans profil calibré prennent les
floors globaux (fail-open), comme le moteur.

SORTIE : hulk-mexc/runs/CHIFFRAGE_REGIME_<ts>.json + imprimé. 0 €, aucun ordre, lecture seule.
"""
import glob
import json
import os
import statistics as st
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
CACHE = os.path.join(RUNS, "replay_cache")
PROFILS = os.path.join(BASE, "strategie", "universe_profils.json")
DEFAUTS = os.path.join(BASE, "config", "defaults.env")
NOTIONAL = 30.0          # mise de référence (dollar par trade) — pour exprimer en $
W15 = 360                # 15 jours de bougies 1 h
H_FWD = 24               # horizon de mesure après la barre


def lire_cfg():
    cfg = {}
    for l in open(DEFAUTS, encoding="utf-8", errors="ignore"):
        l = l.strip()
        if l and not l.startswith("#") and "=" in l:
            k, v = l.split("=", 1)
            cfg[k.strip()] = v.strip()
    return cfg


def lire_profils():
    try:
        d = json.load(open(PROFILS, encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for k, v in d.items():
        if k in ("version", "updated", "note"):
            continue
        if isinstance(v, dict):
            out[k.upper()] = (v.get("calib") or {})
    return out


def cadence_de(h, l):
    """Médiane des ranges journaliers (mêmes 24 h que le moteur) — la grandeur MESURÉE."""
    dr = []
    for i in range(0, len(h), 24):
        ch, cl = h[i:i + 24], l[i:i + 24]
        if ch and cl and min(cl) > 0:
            dr.append((max(ch) / min(cl) - 1.0) * 100.0)
    if not dr:
        return 0.0
    dr.sort()
    return dr[len(dr) // 2]


def regime_de(range15, move24, move6, dd15, dd6, impul_th, cooling_dd,
              quiet_min, spike_15, impulse_entry):
    """LA fonction de régime du moteur, à l'identique, paramétrée (aucune formule réécrite).

    Ordre EXACT de score_pair() : QUIET → IMPULSE → IMPULSE_WAIT → COOLING → WATCH.
    """
    had_spike = range15 >= spike_15 or move24 >= impul_th
    impulse_now = move6 >= impul_th or move24 >= impul_th * 1.2
    cooling = had_spike and dd15 >= cooling_dd and not (impulse_now and dd6 < 1.0)
    quiet = range15 < quiet_min and move24 < quiet_min * 0.6
    if quiet and not impulse_now:
        return "QUIET"
    if impulse_now and dd6 >= impulse_entry * 0.85:
        return "IMPULSE"
    if impulse_now:
        return "IMPULSE_WAIT"
    if cooling:
        return "COOLING"
    return "WATCH"


def main():
    cfg = lire_cfg()
    profils = lire_profils()
    q_ref = float(cfg.get("QUIET_RANGE_PCT", "8"))
    s_ref = float(cfg.get("SPIKE_15D_PCT", "25"))
    imp_ref = float(cfg.get("IMPULSE_PCT", "8"))
    cool_ref = float(cfg.get("COOLING_DD_MIN_PCT", "6"))

    fichiers = sorted(glob.glob(os.path.join(CACHE, "*_1h_45j.json")))
    if not fichiers:
        print("aucune bougie en cache — mesure impossible, on ne conclut pas")
        return 1

    # 1) cadence de chaque paire (dernière fenêtre 15 j) → pour la référence d'univers
    data = {}
    for f in fichiers:
        pair = os.path.basename(f).split("_")[0]
        try:
            bars = json.load(open(f))
        except Exception:
            continue
        if len(bars) < W15 + H_FWD + 24:
            continue
        data[pair] = bars
    if not data:
        print("historique trop court — mesure impossible")
        return 1
    cads = {}
    for pair, bars in data.items():
        h = [b["h"] for b in bars[-W15:]]
        l = [b["l"] for b in bars[-W15:]]
        cads[pair] = cadence_de(h, l)
    cad_ref = st.median([c for c in cads.values() if c > 0])
    k_q, k_s = q_ref / cad_ref, s_ref / cad_ref

    print("CHIFFRAGE RÉGIME MESURÉ (R17) — 45 j de bougies 1 h réelles")
    print(f"  seuils en place  : QUIET si range15 < {q_ref} %  ·  SPIKE si range15 ≥ {s_ref} %")
    print(f"  cadences mesurées: mini {min(cads.values()):.2f} · médiane {cad_ref:.2f} "
          f"· maxi {max(cads.values()):.2f} %/jour  (écart "
          f"{max(cads.values())/max(min(cads.values()),0.01):.0f}×)")
    print(f"  échelle mesurée  : QUIET si range15 < {k_q:.3f} × cadence · "
          f"SPIKE si range15 ≥ {k_s:.3f} × cadence\n")

    res = {}
    desac = []          # (pair, sens, regime_A, regime_B, mfe, mae)
    # Expectative par RÉGIME (règle ACTUELLE) : bloquer protège-t-il, ou coûte-t-il ?
    # QUIET/WATCH n'entrent pas → l'occasion (MFE) est un MANQUE À GAGNER, le MAE un risque ÉVITÉ.
    expect = {r: [] for r in ("QUIET", "WATCH", "COOLING", "IMPULSE", "IMPULSE_WAIT")}
    expect_quiet_par_paire = {}
    # Ce que ces DEUX seuils décident VRAIMENT (un seuil dominé par l'autre condition est INERTE :
    # règle #15 — brancher ou retirer ; R17 — on ne remplace pas un seuil mort par un seuil inventé).
    determinance = {"spike_seul": 0, "spike_avec_move24": 0,
                    "quiet_range_ok_mais_move24_bloque": 0, "quiet_les_deux": 0}
    for pair, bars in sorted(data.items()):
        cal = profils.get(pair) or {}
        imp = float(cal.get("impulse_pct", imp_ref))
        cool = float(cal.get("cooling_dd_pct", cool_ref))
        cad = cads[pair] or 0.0
        # dip/cooling/impulse par paire, comme score_pair (profil calibré, sinon floors)
        dip = max(float(cal.get("dip_pct", cfg.get("DIP_FLOOR_PCT", "2.5"))),
                  cad * float(cfg.get("DIP_CADENCE_MULT", "0.45")))
        cool_entry_frac = float(cal.get("cooling_pullback_frac",
                                        cfg.get("COOLING_PULLBACK_FRAC", "0.25")))
        imp_pb_min = float(cal.get("impulse_pullback_min_pct",
                                  cfg.get("IMPULSE_PULLBACK_MIN_PCT", "5")))
        imp_frac = float(cfg.get("IMPULSE_PULLBACK_FRAC", "0.30"))
        q_p, s_p = k_q * cad, k_s * cad
        cnt = {"A": {}, "B": {}}
        n = 0
        for i in range(W15, len(bars) - H_FWD):
            w = bars[i - W15 + 1:i + 1]
            h = [b["h"] for b in w]
            l = [b["l"] for b in w]
            c = [b["c"] for b in w]
            px = c[-1]
            peak15, trough15 = max(h), min(l)
            if trough15 <= 0:
                continue
            range15 = (peak15 / trough15 - 1.0) * 100.0
            dd15 = (1.0 - px / peak15) * 100.0 if peak15 > 0 else 0.0
            h24, l24 = h[-24:], l[-24:]
            p24, t24 = max(h24), min(l24)
            move24 = (p24 / t24 - 1.0) * 100.0 if t24 > 0 else 0.0
            dd6 = (1.0 - px / max(h[-6:])) * 100.0 if max(h[-6:]) > 0 else 0.0
            move6 = (max(h[-6:]) / min(l[-6:]) - 1.0) * 100.0 if min(l[-6:]) > 0 else 0.0
            imp_entry = max(dip, imp_pb_min, move6 * imp_frac)
            # --- les seuils sont-ils DÉTERMINANTS, ou l'autre condition décide-t-elle toujours ? ---
            if range15 >= s_ref:
                if move24 >= imp:
                    determinance["spike_avec_move24"] += 1
                else:
                    determinance["spike_seul"] += 1
            if range15 < q_ref:
                if move24 < q_ref * 0.6:
                    determinance["quiet_les_deux"] += 1
                else:
                    determinance["quiet_range_ok_mais_move24_bloque"] += 1
            rA = regime_de(range15, move24, move6, dd15, dd6, imp, cool, q_ref, s_ref, imp_entry)
            rB = regime_de(range15, move24, move6, dd15, dd6, imp, cool, q_p, s_p, imp_entry)
            cnt["A"][rA] = cnt["A"].get(rA, 0) + 1
            cnt["B"][rB] = cnt["B"].get(rB, 0) + 1
            n += 1
            fwd_all = bars[i + 1:i + 1 + H_FWD]
            if fwd_all:
                mf = (max(b["h"] for b in fwd_all) / px - 1) * 100.0
                ma = (min(b["l"] for b in fwd_all) / px - 1) * 100.0
                expect[rA].append((mf, ma))
                if rA in ("QUIET", "WATCH"):
                    expect_quiet_par_paire.setdefault(pair, []).append((mf, ma))
            if rA != rB:
                fwd = bars[i + 1:i + 1 + H_FWD]
                mfe = (max(b["h"] for b in fwd) / px - 1) * 100.0
                mae = (min(b["l"] for b in fwd) / px - 1) * 100.0
                ouvre = rA in ("QUIET", "WATCH") and rB in ("COOLING", "IMPULSE", "IMPULSE_WAIT")
                bloque = rA not in ("QUIET",) and rB == "QUIET"
                desac.append({"pair": pair, "sens": "OUVRE" if ouvre else ("BLOQUE" if bloque else "AUTRE"),
                              "A": rA, "B": rB, "mfe": mfe, "mae": mae})
        res[pair] = {"cadence": round(cad, 2), "n": n,
                     "A": cnt["A"], "B": cnt["B"],
                     "pct_quiet_A": round(100 * cnt["A"].get("QUIET", 0) / max(n, 1), 2),
                     "pct_quiet_B": round(100 * cnt["B"].get("QUIET", 0) / max(n, 1), 2),
                     "pct_cooling_imp_A": round(100 * (cnt["A"].get("COOLING", 0)
                                                       + cnt["A"].get("IMPULSE", 0)) / max(n, 1), 2),
                     "pct_cooling_imp_B": round(100 * (cnt["B"].get("COOLING", 0)
                                                       + cnt["B"].get("IMPULSE", 0)) / max(n, 1), 2)}

    print("  1b) QUE FAIT LE PRIX APRÈS CHAQUE RÉGIME (règle ACTUELLE, 24 h devant)\n"
          "      QUIET/WATCH n'entrent PAS : l'occasion est un MANQUE À GAGNER, le MAE un RISQUE ÉVITÉ.")
    print(f"      {'régime':13s} {'n':>6s} {'MFE moy':>9s} {'MFE méd':>9s} {'MAE moy':>9s} {'MAE méd':>9s}")
    for r, v in expect.items():
        if not v:
            print(f"      {r:13s} {0:6d}        —         —         —         —")
            continue
        mf = st.mean(x[0] for x in v)
        mm = st.median([x[0] for x in v])
        am = st.mean(x[1] for x in v)
        amm = st.median([x[1] for x in v])
        print(f"      {r:13s} {len(v):6d} {mf:+8.2f}% {mm:+8.2f}% {am:+8.2f}% {amm:+8.2f}%")
    if expect_quiet_par_paire:
        print("\n      Le blocage (QUIET/WATCH) ne concerne QUE ces paires :")
        for p, v in sorted(expect_quiet_par_paire.items(), key=lambda kv: -len(kv[1])):
            print(f"        {p:12s} n={len(v):4d} · MFE méd {st.median([x[0] for x in v]):+6.2f} % · "
                  f"MAE méd {st.median([x[1] for x in v]):+6.2f} %")

    tot_q_a = sum(v["A"].get("QUIET", 0) for v in res.values())
    tot_q_b = sum(v["B"].get("QUIET", 0) for v in res.values())
    tot_n = sum(v["n"] for v in res.values())
    tot_ci_a = sum(v["A"].get("COOLING", 0) + v["A"].get("IMPULSE", 0) for v in res.values())
    tot_ci_b = sum(v["B"].get("COOLING", 0) + v["B"].get("IMPULSE", 0) for v in res.values())

    print("  1) FRÉQUENCE DES RÉGIMES (barres 1 h, toutes paires)")
    print(f"     QUIET        actuel {tot_q_a:6d} barres ({100*tot_q_a/tot_n:.2f} %) "
          f"→ relu {tot_q_b:6d} ({100*tot_q_b/tot_n:.2f} %)")
    print(f"     COOLING+IMP. actuel {tot_ci_a:6d} ({100*tot_ci_a/tot_n:.2f} %) "
          f"→ relu {tot_ci_b:6d} ({100*tot_ci_b/tot_n:.2f} %)   "
          f"[les 2 régimes qui AUTORISENT l'entrée]")

    print("\n  1c) CES DEUX SEUILS DÉCIDENT-ILS VRAIMENT ? (R15 : brancher ou retirer)")
    d = determinance
    tot_s = d["spike_seul"] + d["spike_avec_move24"]
    print(f"      SPIKE_15D ≥ {s_ref} % est atteint {tot_s} fois · dont SEUL (move24 < impulse_pct) "
          f"{d['spike_seul']} fois ({100*d['spike_seul']/max(tot_s,1):.1f} %)"
          f" → {'le seuil DÉCIDE' if d['spike_seul'] else 'АUCUN cas propre → INERTE'}")
    tot_q2 = d["quiet_les_deux"] + d["quiet_range_ok_mais_move24_bloque"]
    print(f"      QUIET  : range15 < {q_ref} % est atteint {tot_q2} fois · dont la 2e condition "
          f"(move24 < {q_ref*0.6:.1f} %) manque {d['quiet_range_ok_mais_move24_bloque']} fois "
          f"({100*d['quiet_range_ok_mais_move24_bloque']/max(tot_q2,1):.1f} %)"
          f" → {'la 1re condition ne sert jamais seule' if not d['quiet_les_deux'] else 'les deux conditions servent'}")

    print(f"\n  2) DÉSACCORDS : {len(desac)} barres où les deux règles ne disent PAS la même chose")
    par_sens = {}
    for d in desac:
        par_sens.setdefault(d["sens"], []).append(d)
    for sens in ("OUVRE", "BLOQUE", "AUTRE"):
        v = par_sens.get(sens) or []
        if not v:
            print(f"     {sens:6s} : 0")
            continue
        mfe = sum(x["mfe"] for x in v) / len(v)
        mae = sum(x["mae"] for x in v) / len(v)
        print(f"     {sens:6s} : {len(v):5d} barres · occasion (MFE 24 h) {mfe:+6.2f} % · "
              f"risque (MAE 24 h) {mae:+6.2f} %  →  à {NOTIONAL:.0f} $/trade : "
              f"{NOTIONAL*mfe/100:+.2f} $ d'occasion, {NOTIONAL*mae/100:+.2f} $ de risque")

    print("\n  3) CARTE PAR PAIRE (QUIET % et entrée-autorisée % : actuel → relu)")
    print(f"     {'paire':12s} {'cad%j':>6s} {'n':>6s}  {'QUIET':>13s}  {'COOL+IMP':>13s}")
    for p, v in sorted(res.items(), key=lambda kv: -kv[1]["cadence"]):
        print(f"     {p:12s} {v['cadence']:6.2f} {v['n']:6d}  "
              f"{v['pct_quiet_A']:5.1f}% → {v['pct_quiet_B']:5.1f}% {v['pct_cooling_imp_A']:6.1f}%"
              f" → {v['pct_cooling_imp_B']:5.1f}%")

    # 4) VERDICT — écrit AVANT lecture, comme la méthode maison l'exige
    o = par_sens.get("OUVRE") or []
    b = par_sens.get("BLOQUE") or []
    mfe_o = sum(x["mfe"] for x in o) / len(o) if o else 0.0
    mfe_b = sum(x["mfe"] for x in b) / len(b) if b else 0.0
    # la moyenne peut mentir sur 33 barres : on regarde aussi la MÉDIANE et le pire cas
    med_o = st.median([x["mfe"] for x in o]) if o else 0.0
    med_b = st.median([x["mfe"] for x in b]) if b else 0.0
    print(f"     (détail des désaccords — la moyenne d'un petit lot peut mentir :  "
          f"OUVRE méd {med_o:+.2f} % · BLOQUE méd {med_b:+.2f} %)")
    print("\n  4) VERDICT")
    if not desac:
        verdict = "AUCUN CHANGEMENT : les deux seuils sont INERTES pour toutes les paires → rien à toucher."
    elif o and not b and mfe_o > 0:
        verdict = (f"RELIRE LA RÈGLE OUVRE {len(o)} barres dont l'avenir est POSITIF "
                   f"(+{mfe_o:.2f} % de MFE 24 h) → candidat soutenu par la mesure.")
    elif b and not o and mfe_b < 0:
        verdict = (f"RELIRE LA RÈGLE BLOQUE {len(b)} barres dont l'avenir est NÉGATIF "
                   f"({mfe_b:.2f} %) → la relecture PROTÈGE.")
    else:
        verdict = (f"MESURE NON CONCLUANTE : {len(o)} barres ouvertes (MFE {mfe_o:+.2f} %) et "
                   f"{len(b)} bloquées (MFE {mfe_b:+.2f} %) → on NE TOUCHE PAS.")
    print("     " + verdict)
    print("     (rappel : le $ ci-dessus est une BORNE HAUTE — la chaîne d'entrée n'est pas rejouée)")

    out = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "expectative_par_regime": {r: len(v) for r, v in expect.items()},
           "mediane_desaccords": {"OUVRE": med_o, "BLOQUE": med_b},
           "determinance": determinance,
           "expectative_par_regime_detail": {r: {"n": len(v),
                                               "mfe_med": (st.median([x[0] for x in v]) if v else None),
                                               "mae_med": (st.median([x[1] for x in v]) if v else None)}
                                           for r, v in expect.items()},
           "cadence_reference": cad_ref, "k_quiet": k_q, "k_spike": k_s,
           "quiet_pct": q_ref, "spike_pct": s_ref,
           "barres": tot_n, "quiet_A": tot_q_a, "quiet_B": tot_q_b,
           "cool_imp_A": tot_ci_a, "cool_imp_B": tot_ci_b,
           "desaccords": {k: len(v) for k, v in par_sens.items()},
           "par_paire": res, "verdict": verdict}
    fn = os.path.join(RUNS, f"CHIFFRAGE_REGIME_{datetime.now(timezone.utc):%Y%m%d_%H%M}.json")
    json.dump(out, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nsortie : {fn}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
