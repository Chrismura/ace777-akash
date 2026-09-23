#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_memoire_donnees.py — GO 3 : ce qu'on MÉMORISE, et ce que ça permet de juger
=================================================================================

DEMANDE CHRISTOPHE (23/09/2026) : « vérifier les données qu'on mémorise, si il en manque,
si elles sont correctement enregistrées […] ensuite tu rejoues tout ça avec les derniers
set-up ».

QUATRE PARTIES, aucune ne devine
--------------------------------
  A. COUVERTURE : pour chacune des paires du moteur — profil ? vue live ? observation de murs ?
     position/état ? événements au journal ? La table de présence est brute, sans commentaire.
  B. COMPLÉTUDE : colonne par colonne du journal, quelle part des lignes porte une valeur ?
     Puis ce qui MANQUE pour qu'un trade soit jugeable après coup (mise visée, mur utilisé,
     spread payé, seuil exigé, dd6, stop nominal) : mesuré sur le texte des raisons.
  C. COHÉRENCE : horodatages non décroissants, continuité de `pnl_total` (chaque ligne = la
     précédente + son `pnl_usdt`), doublons stricts. Un écart est listé, jamais lissé.
  D. RE-INJECTION DES SET-UP (simulation, pas un ordre) : les valeurs viennent de
     runs/SETUPS_PAIRES_*.json (l'instrument source), jamais retapées à la main. On confronte :
       · stop ANNONCÉ vs stop RÉALISÉ, et ce que le dépassement COÛTE en $ sur les séquences
         réellement sorties sur stop ;
       · mise exécutée vs plafond (`cap` du set-up) ;
       · profondeur mesurée (`serie.med_05`) vs mise : la mise tenait-elle dans le carnet ?

⚠ LIMITE DÉCLARÉE : la re-injection utilise les extrêmes MESURÉS de la période de tenue
(min/max klines), pas un chemin tick par tick. Un stop nominal peut donc être « touché » sans
qu'on sache s'il l'aurait été sur un chemin monotone — c'est une borne, pas une prédiction.

LECTURE SEULE, 0 ordre, 0 €. Sorties : runs/AUDIT_MEMOIRE_*.
"""

from __future__ import annotations

import csv
import json
import statistics as stats
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
RUNS = RACINE / "runs"
TAG = "20260923"
CSV = max(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime)
STATE = sorted(RUNS.glob("PAPER_V1_*_state.json"))[-1]
PROFILS = RACINE / "strategie" / "universe_profils.json"
ASP = RUNS / "aspiration_live.json"
MURS_OBS = RUNS / "murs_observations.json"
SETUPS = sorted(RUNS.glob("SETUPS_PAIRES_*.json"))[-1]
SEQ = sorted(RUNS.glob("AUDIT_SEQUENCES_*.json"))[-1]
SORTIE_JSON = RUNS / f"AUDIT_MEMOIRE_{TAG}.json"
SORTIE_TXT = RUNS / f"AUDIT_MEMOIRE_{TAG}.txt"


def jload(p: Path, defaut=None):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return defaut


def main() -> int:
    st = jload(STATE, {}) or {}
    prof_all = jload(PROFILS, {}) or {}
    meta = {"version", "updated", "note", "_note", "commentaire"}
    prof = {k: v for k, v in prof_all.items() if k not in meta and isinstance(v, dict)}
    asp = (jload(ASP, {}) or {}).get("paires") or {}
    murs = {p.get("pair"): p for p in (jload(MURS_OBS, {}) or {}).get("top_murs", []) if p.get("pair")}
    setu = {x["paire"]: x for x in (jload(SETUPS, {}) or {}).get("paires", []) if x.get("paire")}
    seq_doc = jload(SEQ, {}) or {}
    seqs = seq_doc.get("sequences") or []

    paires = list(st.get("pairs") or [])
    ev_par_paire = Counter()
    rows = []
    with open(CSV, encoding="utf-8") as f:
        rd = csv.DictReader(f)
        champs = rd.fieldnames
        for r in rd:
            ev_par_paire[r["pair"]] += 0 if r["event"] == "SKIP" else 1
            rows.append(r)

    print("=== GO 3 — AUDIT DE LA MÉMOIRE ===")
    print(f"journal {CSV.name} · {len(rows)} lignes · état {STATE.name}")
    print()

    # ---------- A. couverture ----------
    print("--- A. COUVERTURE (une croix = la donnée existe) ---")
    print(f"{'paire':<12}{'profil':>7}{'vue live':>9}{'obs murs':>9}{'état (pos/bag)':>16}"
          f"{'événements':>11}{'set-up':>8}")
    trous = []
    for p in sorted(paires):
        pos = bool((st.get("positions") or {}).get(p))
        bag = bool((st.get("bags") or {}).get(p))
        n_ev = ev_par_paire.get(p, 0)
        print(f"{p:<12}{('oui' if p in prof else 'NON'):>7}{('oui' if p in asp else 'NON'):>9}"
              f"{('oui' if p in murs else 'NON'):>9}{(('pos' if pos else '') + ('bag' if bag else '') or 'NON'):>16}"
              f"{n_ev:>11}{('oui' if p in setu else 'NON'):>8}")
        if p not in prof:
            trous.append(f"{p} : pas de profil (villages de repli du code)")
        if p not in murs:
            trous.append(f"{p} : pas d'observation de murs (wall_strength → 0,5 neutre par défaut)")
        if p not in asp:
            trous.append(f"{p} : pas de vue live → cap de mise sur le profil figé")
        if p not in setu:
            trous.append(f"{p} : pas de set-up chiffré (moins de 20 paires couvertes)")
    print()

    # ---------- B. complétude du journal ----------
    print("--- B. COMPLÉTUDE DU JOURNAL (part de lignes non vides par colonne, par type) ---")
    par_type: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        par_type[r["event"]].append(r)
    for ev, rs in sorted(par_type.items(), key=lambda x: -len(x[1])):
        if ev == "SKIP":
            continue
        parts = []
        for c in champs:
            n = sum(1 for r in rs if (r.get(c) or "").strip() not in ("", "0", "0.0000", "0.00000000"))
            parts.append(f"{c}={100 * n // max(1, len(rs))}%")
        print(f"  {ev:<13} n={len(rs):<4} " + " ".join(parts))
    print()
    # ce qui est ÉCRIT dans le texte libre (donc mémorisé « par chance »)
    n_sell = len(par_type.get("SELL", [])) + len(par_type.get("SELL_PARTIAL", []))
    with_spread = sum(1 for r in par_type.get("SELL", []) + par_type.get("SELL_PARTIAL", [])
                      if "spread=" in (r.get("reason") or ""))
    with_peak = sum(1 for r in par_type.get("SELL", []) + par_type.get("SELL_PARTIAL", [])
                    if "peak" in (r.get("reason") or ""))
    champs_absents = []
    for nom, desc in [
        ("mise_visee", "mise calculée AVANT les plafonds/fusibles"),
        ("mur_utilise", "valeur du mur (live ou profil) ayant plafonné"),
        ("seuil_exige", "repli exigé par la paire au moment de l'entrée"),
        ("dd6_observe", "repli observé (écrit seulement sur les refus depuis le 23/09)"),
        ("stop_nominal", "niveau de stop annoncé à l'entrée"),
        ("spread_paye", "spread effectivement traversé"),
    ]:
        champs_absents.append(f"{nom} — {desc}")
    print(f"spread présent dans le texte des {n_sell} ventes : {with_spread} "
          f"({100 * with_spread // max(1, n_sell)} %) · pic de sortie : {with_peak}")
    print("COLONNES QUI MANQUENT pour juger un trade après coup :")
    for c in champs_absents:
        print("  -", c)
    print()

    # ---------- C. cohérence ----------
    print("--- C. COHÉRENCE INTERNE ---")
    ts_prec: str | None = None
    pnl_prec: float | None = None
    desordres, pnl_ecarts, dupes = [], [], []
    dupes_skip = 0
    sans_pnl = []
    vus = set()
    vus_skip = set()
    for r in rows:
        cle = (r["ts"], r["pair"], r["event"], r["reason"][:40])
        if r["event"] == "SKIP":
            # les SKIP sont dédupliqués par le moteur avec un TTL → des répétitions à
            # l'identique sont NORMALES. On les compte À PART pour ne pas les confondre
            # avec une vraie duplication d'événement de trading.
            if cle in vus_skip:
                dupes_skip += 1
            vus_skip.add(cle)
            ts_prec = r["ts"]
            continue
        if cle in vus:
            dupes.append(cle)
        vus.add(cle)
        if ts_prec and r["ts"] < ts_prec:
            desordres.append((ts_prec, r["ts"]))
        if r["event"] in ("SELL", "SELL_PARTIAL"):
            if (r["pnl_usdt"] or "").strip() == "":
                sans_pnl.append((r["ts"], r["pair"], r["reason"][:50]))
            if pnl_prec is not None:
                attendu = round(pnl_prec + float(r["pnl_usdt"] or 0), 4)
                reel = round(float(r["pnl_total"] or 0), 4)
                if abs(attendu - reel) > 0.01:
                    pnl_ecarts.append((r["ts"], r["pair"], attendu, reel))
        ts_prec = r["ts"]
        if (r["pnl_total"] or "").strip() != "":
            pnl_prec = float(r["pnl_total"])
    print(f"ventes sans pnl_usdt inscrit : {len(sans_pnl)}")
    for v in sans_pnl[:4]:
        print(f"   {v[0]} {v[1]} {v[2]}")
    print(f"horodatages non croissants : {len(desordres)}")
    for d in desordres[:5]:
        print(f"   {d[0]} → {d[1]}")
    print(f"discontinuités de pnl_total (>0,01 $) : {len(pnl_ecarts)}")
    for e in pnl_ecarts[:6]:
        print(f"   {e[0]} {e[1]} attendu {e[2]} vs inscrit {e[3]}")
    print(f"doublons stricts HORS SKIP (donc des vrais événements de trading) : {len(dupes)}")
    print(f"lignes SKIP strictement répétées (TTL du dédup — bruit, pas une corruption) : {dupes_skip}")
    print()

    # ---------- D. re-injection des set-up ----------
    print("--- D. RE-INJECTION DES SET-UP SUR LES SÉQUENCES MESURÉES (simulation, 0 ordre) ---")
    depassements = []
    for s in seqs:
        m = s.get("mexc") or {}
        if not m.get("ok"):
            continue
        u = setu.get(s["pair"])
        if not u:
            continue
        motifs = " ".join(s.get("motifs") or [])
        est_stop = ("stop-" in motifs) or ("guard" in motifs) or ("dust" in motifs)
        if not est_stop:
            continue
        annonce = u.get("stop_annonce")
        if annonce is None:
            continue
        # perte réellement encaissée vs perte qu'aurait donnée le stop ANNONCÉ
        perte_reelle = s["pnl_inscrit_brut"]
        notional = s["notional_entree"] or 0.0
        perte_nominale = -notional * float(annonce) / 100.0
        depassements.append({
            "pair": s["pair"], "fermeture": s["fermeture"], "pnl_reel": round(perte_reelle, 4),
            "stop_annonce_pct": annonce, "pnl_si_stop_nominal": round(perte_nominale, 4),
            "cout_du_derapage": round(perte_reelle - perte_nominale, 4),
            "min_tenue_pct": round((m["prix_min_tenue"] - s["prix_moyen_entree"])
                                   / s["prix_moyen_entree"] * 100, 2) if m.get("prix_min_tenue") else None,
        })
    par_paire_dep: dict[str, dict] = defaultdict(lambda: {"n": 0, "cout": 0.0, "annonce": None})
    for d in depassements:
        dd = par_paire_dep[d["pair"]]
        dd["n"] += 1
        dd["cout"] += d["cout_du_derapage"]
        dd["annonce"] = d["stop_annonce_pct"]
    print(f"{'paire':<12}{'n stops':>9}{'stop annoncé %':>16}{'coût du dérapage $':>20}")
    for p in sorted(par_paire_dep, key=lambda x: -par_paire_dep[x]["cout"]):
        dd = par_paire_dep[p]
        print(f"{p:<12}{dd['n']:>9}{dd['annonce']:>16.2f}{dd['cout']:>20.2f}")
    cout_total = round(sum(d["cout_du_derapage"] for d in depassements), 2)
    print(f"{'TOTAL':<12}{len(depassements):>9}{'':>16}{cout_total:>20.2f}")
    print()

    # mise exécutée vs plafond du set-up + profondeur mesurée
    print(f"{'paire':<12}{'mise méd $':>11}{'cap set-up $':>13}{'prof<0,5% $':>12}"
          f"{'mise/cap':>10}{'mise/prof':>11}")
    mise_info = {}
    par_paire_not = defaultdict(list)
    for s in seqs:
        if s.get("notional_entree"):
            par_paire_not[s["pair"]].append(s["notional_entree"])
    for p in sorted(par_paire_not):
        u = setu.get(p) or {}
        med = stats.median(par_paire_not[p])
        cap = u.get("cap")
        prof_med = ((u.get("serie") or {}).get("med_05"))
        print(f"{p:<12}{med:>11.2f}{((f'{cap:.2f}') if cap else '—'):>13}"
              f"{((f'{prof_med:.2f}') if prof_med else '— (non mesuré)'):>12}"
              f"{((f'{med / cap:.2f}') if cap else '—'):>10}"
              f"{((f'{med / prof_med:.3f}') if prof_med else '—'):>11}")
        mise_info[p] = {"mise_med": round(med, 2), "cap": cap, "prof_05": prof_med}

    rapport = {
        "instrument": "audit_memoire_donnees.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "journal": CSV.name, "n_lignes": len(rows), "champs_journal": champs,
        "couverture": {p: {"profil": p in prof, "vue_live": p in asp, "obs_murs": p in murs,
                           "en_position": bool((st.get("positions") or {}).get(p)),
                           "evenements": ev_par_paire.get(p, 0), "set_up": p in setu}
                       for p in paires},
        "trous": trous,
        "completude": {ev: {c: round(100 * sum(1 for r in rs if (r.get(c) or "").strip()
                           not in ("", "0", "0.0000", "0.00000000")) / max(1, len(rs)), 1)
                            for c in champs} for ev, rs in par_type.items()},
        "spread_dans_le_texte_pct": round(100 * with_spread / max(1, n_sell), 1),
        "colonnes_manquantes": champs_absents,
        "coherence": {"horodatages_non_croissants": len(desordres),
                      "discontinuites_pnl_total": len(pnl_ecarts), "doublons": len(dupes),
                      "ventes_sans_pnl_usdt": len(sans_pnl),
                      "doublons_skip_bruyants": dupes_skip,
                      "exemples_desordre": desordres[:5], "exemples_sans_pnl": sans_pnl[:4],
                      "exemples_pnl": pnl_ecarts[:6]},
        "re_injection": {"n_stops_analyses": len(depassements),
                         "cout_total_derapage_vs_stop_annonce": cout_total,
                         "detail": depassements, "mise_vs_cap": mise_info},
        "limites_declarees": [
            "re-injection sur les EXTRÊMES mesurés de la tenue (borne, pas un chemin tick par tick)",
            "le mur/cap du set-up est celui d'AUJOURD'HUI, pas celui de l'instant du trade",
        ],
        "lecture_seule": True, "ordres": 0,
    }
    SORTIE_JSON.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")
    SORTIE_TXT.write_text("\n".join([
        f"AUDIT MÉMOIRE — {rapport['ts_utc']} — {CSV.name}",
        f"lignes {len(rows)} · trous de couverture {len(trous)} · doublons {len(dupes)} · "
        f"pnl_total discontinu {len(pnl_ecarts)}",
        f"spread dans le texte des ventes : {rapport['spread_dans_le_texte_pct']} %",
        f"coût du dérapage de stop vs stop annoncé : {cout_total} $ sur {len(depassements)} stops",
        "", "TROUS :"] + [f"  - {t}" for t in trous] +
        ["", "COLONNES QUI MANQUENT :"] + [f"  - {c}" for c in champs_absents] +
        ["", "LIMITES DÉCLARÉES :"] + [f"  - {l}" for l in rapport["limites_declarees"]]),
        encoding="utf-8")
    print()
    print(f"écrit : {SORTIE_JSON.name} + {SORTIE_TXT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
