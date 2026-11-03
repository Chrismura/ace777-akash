#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""m_kelly_metre.py — le « mètre de m » maison (GO Christophe 02/11, signet @0bl4ze).

Question : pour chaque paire, m = taille réelle / taille juste (Kelly).
score = 2m - m² (m=1 optimal, m=2 rien, m>2 perd même en ayant raison).

Méthode ($ partout, lecture seule, 0 ordre) — FIX 02/11 boucle source :
- L'EDGE VIENT DU JOURNAL LUI-MÊME (colonne pnl_usdt, brut) : Σ = 43.36 $
  = brut PORTEFEUILLE (+43.45 $). L'avg-cost maison divergeait (+14 $) — le
  journal fait foi pour les closes, pas notre re-calcul.
- Coûts : brut journal - net PORTEFEUILLE par paire (coutCumule mission
  surestime : Σ 21.56 vs 15.44 validés). f* = p - (1-p)/b (Kelly) sur les
  nets. n >= 10 exigé, sinon non mesuré.
- RÉFÉRENCES DYNAMIQUES (audit 02/11 14h30) : le journal ET le MD vivent
  (journal appendu 13h04, MD régénéré 14h25) — les seuils 43.36/28.01 en dur
  sont interdits, on lit brut/coûts/net dans le header du MD.
- Quantités/cash : rejeu exact (notion±fee, pas d'avg). TEL/QAIT (hors
  mission, journal seul) inclus avec budget 30 historique, flaguées.
- Marks = dernier DIGEST TOUS MOIS (le glob 202610* ratait novembre !).
  pos$ = hold*mark (le bag piégé), latent$ = pos$ - coût_rejoué,
  couverture$ = cash / pos$.
- juste$ = max(0, f*) * budget. m = pos$ / juste$ (juste=0 et pos>0 -> INF).
- Shorts : trades des *_state.json, bankroll 100 $, notionnel médian.
DOUBLE VALIDATION : Σ brut == 43.36 ± 0.5 ET Σ net == +28.01 ± 2, sinon STOP.
"""
import argparse
import csv
import glob
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from couts_communs import journal_actif  # §41 : UNE définition du journal vivant

ROOT = "/Users/christophe/ace777-test-day1"
RUNS = ROOT + "/hulk-mexc/runs"
MISSION = ROOT + "/Index_Maison/cockpit/mission.json"
JOURNAL = None   # résolu à l'exécution : le journal VIVANT, jamais un nom figé


def _journal():
    """Journal vivant — délégué à couts_communs (§41 : une seule définition)."""
    global JOURNAL
    if JOURNAL is None:
        JOURNAL = str(journal_actif(Path(RUNS)))
    return JOURNAL
PF_MD = RUNS + "/PORTEFEUILLE_LATEST.md"
FEE = 0.0005
N_MIN = 10  # en dessous : edge non mesuré, pas de f*


def lire_refs_pf():
    """Références vivantes du header : brut, coûts, net (le MD est régénéré
    en continu — aucune constante en dur)."""
    import re
    try:
        txt = open(PF_MD, encoding="utf-8").read()
    except Exception:
        return {}
    m = re.search(r"brut\s*([+-]?[0-9.]+).*coûts est\.\s*([+-]?[0-9.]+).*NET\s*([+-]?[0-9.]+)", txt)
    if not m:
        return {}
    return {"brut": float(m.group(1)), "couts": float(m.group(2)), "net": float(m.group(3))}


def lire_couts_pf():
    """Coûts par paire = brut journal - net PORTEFEUILLE (les deux font foi).
    FIX boucle source : coutCumule mission (Σ 21.56) surestime vs coûts
    validés du portefeuille (15.44) ; ici Σ coûts == 15.35 ≈ 15.44."""
    import re
    net = {}
    try:
        txt = open(PF_MD, encoding="utf-8").read()
    except Exception:
        return net
    for m in re.finditer(r"\|\s*(\w+USDT)\s*\|\s*([+-]?[0-9.]+)\s*\|", txt):
        if "paire" in m.group(1).lower():
            continue
        try:
            net[m.group(1)] = float(m.group(2))
        except Exception:
            continue
    return net


def parse_ts(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None


def digest_marks():
    idx = {}
    for f in sorted(glob.glob(RUNS + "/DIGEST_*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        t = parse_ts(d.get("ts"))
        if t is None:
            continue
        px = {}
        for e in (d.get("pairs") or []):
            try:
                if e.get("pair") and float(e.get("last") or 0) > 0:
                    px[e["pair"]] = float(e["last"])
            except Exception:
                continue
        if px:
            idx[t] = px
    if not idx:
        return {}, None
    tmax = max(idx)
    return idx[tmax], tmax


def lire_cash_moteur():
    """Cash par paire depuis le state live (vérité moteur).
    Retour : (dict, nom_du_state). Dict vide si state illisible (repli rejeu)."""
    import os as _os
    try:
        ptr = _os.path.join(RUNS, ".hulk_resume_pointer")
        nom = open(ptr, encoding="utf-8").read().strip() if _os.path.exists(ptr) else ""
        chemin = _os.path.join(RUNS, nom) if nom else ""
        if not chemin or not _os.path.exists(chemin):
            cands = sorted(glob.glob(RUNS + "/PAPER_V1_*_state.json"),
                           key=lambda f: _os.path.getmtime(f), reverse=True)
            if not cands:
                return {}, "?"
            chemin = cands[0]
        d = json.load(open(chemin, encoding="utf-8"))
        out = {}
        for p, v in (d.get("pair_cash") or {}).items():
            try:
                out[p] = float(v or 0.0)
            except Exception:
                continue
        return out, _os.path.basename(chemin)
    except Exception:
        return {}, "?"


def replay():
    mission = json.load(open(MISSION, encoding="utf-8"))
    consts = {p["pair"]: p for p in mission["hulk"]["hulkVsHold"]["pairs"]}
    rows = list(csv.DictReader(open(_journal(), newline="", encoding="utf-8-sig")))
    st = {}
    for p, c in consts.items():
        st[p] = {"budget": float(c.get("budget") or 0.0), "cash": float(c.get("budget") or 0.0),
                 "qty": 0.0, "cost": 0.0, "pnls": [], "real": 0.0, "nbuy": 0.0,
                 "cout": float(c.get("coutCumule") or 0.0), "mission": True}
    for jp in ("TELUSDT", "QAITUSDT"):  # hors mission mais dans le journal
        if jp not in st:
            st[jp] = {"budget": 30.0, "cash": 30.0, "qty": 0.0, "cost": 0.0,
                      "pnls": [], "bruts": [], "real": 0.0, "nbuy": 0.0,
                      "cout": 0.0, "mission": False}
    for _s in st.values():
        _s.setdefault("bruts", [])
    for r in rows:
        p = r.get("pair") or ""
        if p not in st:
            continue
        ev = (r.get("event") or "").upper()
        if ev == "BAG_ARM":
            continue
        is_buy = ev in ("BUY", "DCA", "GBAG_SOUCHE", "GBAG_PYRAMIDE", "BAG_DCA")
        is_sell = ev.startswith(("SELL", "STOP", "BAG")) and not is_buy
        # §23/§24 — UN BOOKING = |pnl_usdt| > 0, TOUT événement confondu.
        # DÉFAUT FERMÉ LE 03/11/2026 (mesuré) : le mètre re-filtrait par NOM
        # d'événement et perdait CORE_FILET (−4,55 $, 1 booking) → Σ brut 43,13 $
        # au lieu de 38,58 $, coûts 20,43 $ au lieu de 15,89 $, donc f*/juste/m
        # faux pour la paire concernée, et publication bloquée. Le brut vient du
        # JOURNAL, jamais d'une liste de noms à tenir à jour.
        try:
            pnl_j = float(r.get("pnl_usdt") or 0.0)
        except Exception:
            pnl_j = 0.0
        if not is_buy and not is_sell:
            # hors familles rejouables : ça COMPTE dans le brut, ça ne déplace
            # ni cash ni quantité (aucune quantité inventée dans le rejeu).
            if abs(pnl_j) > 1e-9:
                st[p]["bruts"].append(pnl_j)
            continue
        try:
            q = float(r.get("qty") or 0.0)
            px = float(r.get("price") or 0.0)
        except Exception:
            continue
        if q <= 0 or px <= 0:
            continue
        s = st[p]
        notion = q * px
        fee = notion * FEE
        if is_buy:
            if ev == "GBAG_SOUCHE":
                s["cash"] -= max(0.0, s["cash"])
            else:
                s["cash"] -= notion + fee
            s["qty"] += q
            s["cost"] += notion + fee
            s["nbuy"] += notion
        else:
            avg = (s["cost"] / s["qty"]) if s["qty"] > 1e-12 else 0.0
            pnl = notion - fee - avg * q
            s["pnls"].append(pnl)
            try:
                s["bruts"].append(pnl_j)
            except Exception:
                s["bruts"].append(0.0)
            s["real"] += pnl
            s["cash"] += notion - fee
            s["qty"] = max(0.0, s["qty"] - q)
            s["cost"] = max(0.0, s["cost"] - avg * q)
    return st


def kelly(pnls):
    n = len(pnls)
    if n < N_MIN:
        return {"n": n, "mesure": False}
    wins = [x for x in pnls if x > 0]
    loss = [-x for x in pnls if x < 0]
    p = len(wins) / n
    W = sum(wins) / len(wins) if wins else 0.0
    L = sum(loss) / len(loss) if loss else 0.0
    if W <= 0 or L <= 0:
        return {"n": n, "mesure": True, "p": round(p, 3), "W": round(W, 4),
                "L": round(L, 4), "b": None, "f": 0.0 if p == 0 else None,
                "e": round(sum(pnls) / n, 4)}
    b = W / L
    f = p - (1 - p) / b
    return {"n": n, "mesure": True, "p": round(p, 3), "W": round(W, 4),
            "L": round(L, 4), "b": round(b, 3), "f": round(f, 4),
            "e": round(sum(pnls) / n, 4)}


def flag(m, mesure, f):
    if not mesure:
        return "🟡 EDGE NON MESURÉ"
    if f is not None and f <= 0:
        return "🔴 EDGE ≤ 0"
    if m != m:  # NaN
        return "🟡"
    if m == float("inf"):
        return "🔴 m=INF (expo sans edge)"
    if m > 2:
        return "🔴 m>2 PERDANT"
    if m > 1.5:
        return "🟡 m>1,5"
    if m > 1.0:
        return "🟡 m>1"
    return "🟢"


def scenarios(lignes):
    """Scénarios de dégraissage SUR MESURE (GO Christophe 02/11, lecture seule).
    Règle : on n'allège JAMAIS en dessous de la cible, on n'ajoute JAMAIS
    (R11 fail-safe, R18 épargne). α_régime = 1 neutre (thermo score 66 le
    02/11 14h00, ni euphorie ni crash — branchable plus tard sur le score).
    - S1 JUSTE (m->1) : cible = juste (l'optimum du post @0bl4ze).
    - S2 PRO (demi-Kelly) : cible = 0,5 × juste (standard des desks).
    - S3 BAG (sur mesure) : cible = juste × (1+lat%) — la profondeur du bag
      de CHAQUE paire règle sa propre dureté (1+lat% >= 0 garanti car
      latent >= -pos). Sans edge (f*<=0) : cible 0 = sortie au fil de l'eau.
      Edge non mesuré : on TIENT (pas d'action sans mesure, R17)."""
    print()
    print("--- SCÉNARIOS (α_régime=1 neutre, thermo 66 — lecture seule, 0 ordre) ---")
    print(f"{'paire':12s} {'pos$':>8s} {'juste$':>7s} {'lat%':>6s} "
          f"{'S1 allég':>9s} {'S2 allég':>9s} {'S3 allég':>9s}  note")
    tot = {"pos": 0.0, "s1": 0.0, "s2": 0.0, "s3": 0.0, "cash": 0.0}
    for L in lignes:
        pos, cash, juste = L["pos"], L["cash"], L["juste"]
        if pos <= 0.01:
            continue
        tot["pos"] += pos
        tot["cash"] += cash
        latf = max(0.0, 1.0 + L["latpc"] / 100.0)
        if L["cas"] == "sain":
            c1, c2, c3 = juste, 0.5 * juste, juste * latf
            note = ""
        elif L["cas"] == "sans_edge":
            c1 = c2 = c3 = 0.0
            note = "sortie fil de l'eau"
        else:
            c1 = c2 = c3 = pos
            note = "AVEUGLE: tenir, mesurer"
        a1, a2, a3 = max(0.0, pos - c1), max(0.0, pos - c2), max(0.0, pos - c3)
        tot["s1"] += a1
        tot["s2"] += a2
        tot["s3"] += a3
        j = "NA" if juste != juste else f"{juste:.2f}"
        print(f"{L['p']:12s} {pos:8.2f} {j:>7s} {L['latpc']:5.1f}% "
              f"{a1:9.2f} {a2:9.2f} {a3:9.2f}  {note}")
    print()
    for sid, nom in (("s1", "JUSTE (m->1)"), ("s2", "PRO (demi-Kelly)"),
                      ("s3", "BAG (sur mesure)")):
        expo_ap = tot["pos"] - tot[sid]
        couv_ap = (tot["cash"] + tot[sid]) / expo_ap if expo_ap > 0.01 else float("inf")
        print(f"{nom}: allégé={tot[sid]:.2f} $ · expo {tot['pos']:.2f} -> {expo_ap:.2f} $ · "
              f"coussin récupéré={tot[sid]:.2f} $ · couv globale {couv_ap:.2f}")
    print("La règle n'ajoute JAMAIS, ne vend jamais en panique : les cibles sont des "
          "plafonds atteints au fil de l'eau (rebonds, DCA inverse) — mécanique à décider.")


def main(opts=None):
    global PF_NET, JOURNAL
    if getattr(opts, "csv", None):
        JOURNAL = opts.csv
    print(f"journal mesuré : {os.path.basename(_journal())}")
    PF_NET = lire_couts_pf()
    marks, tmarks = digest_marks()
    st = replay()
    # §74 anti-aveugle : le cash REJOUÉ diverge du moteur (négatifs fictifs :
    # QNT -6,10 $ au rejeu vs +11,95 $ moteur — écart total 82 $ localisé).
    # La couverture se lit sur le cash MOTEUR (state, vérité live), pas rejoué.
    moteur_cash, moteur_src = lire_cash_moteur()
    for _p, _s in st.items():
        if _p in moteur_cash:
            _s["cash"] = moteur_cash[_p]
            _s["cash_src"] = "moteur"
        else:
            _s["cash_src"] = "rejeu"
    lignes = []
    print(f"marks: {tmarks.isoformat() if tmarks else '?'} ({len(marks)} paires)")
    print(f"{'paire':12s} {'bdg':>5s} {'pos$':>8s} {'cash$':>8s} {'couv':>6s} "
          f"{'lat$':>8s} {'lat%':>6s} {'n':>4s} {'p':>5s} {'b':>6s} {'f*':>7s} "
          f"{'juste$':>7s} {'m':>6s} {'score':>6s}  drapeau")
    tot_pos = tot_juste = tot_brut = tot_cout = tot_lat = tot_expo = expo_sans_edge = 0.0
    for p in sorted(st):
        s = st[p]
        mk = marks.get(p, 0.0)
        pos = s["qty"] * mk
        avg = (s["cost"] / s["qty"]) if s["qty"] > 1e-12 else 0.0
        latent = s["qty"] * (mk - avg) if s["qty"] > 1e-12 else 0.0
        latpc = (100 * latent / pos) if pos > 1e-9 else 0.0
        tot_lat += latent
        if pos > 0.01:
            tot_expo += pos
        couv = (s["cash"] / pos) if pos > 0.01 else float("inf")
        bruts = s.get("bruts") or []
        tot_brut += sum(bruts)
        if p in PF_NET:
            cout = sum(bruts) - PF_NET[p]  # brut journal - net validé
        else:
            cout = s["cout"]  # repli mission si paire absente du PF
        tot_cout += cout
        share = (cout / len(bruts)) if bruts else 0.0
        nets = [b - share for b in bruts]  # edge NET de coûts (spread+fees)
        k = kelly(nets)
        if k.get("mesure") and k.get("f") is not None and k["f"] > 0:
            juste = k["f"] * s["budget"]
            m = pos / juste if juste > 1e-9 else (float("inf") if pos > 1e-9 else 0.0)
            tot_pos += pos
            tot_juste += juste
        elif k.get("mesure"):
            if pos > 0.01:
                expo_sans_edge += pos  # exposé SANS edge : le cas le plus grave
            juste, m = 0.0, (float("inf") if pos > 1e-9 else 0.0)
        else:
            juste, m = float("nan"), float("nan")
        score = 2 * m - m * m if m == m and m != float("inf") else float("-inf")
        if k.get("mesure") and k.get("f") is not None and k["f"] > 0:
            _cas = "sain"
        elif k.get("mesure"):
            _cas = "sans_edge"
        else:
            _cas = "aveugle"
        lignes.append({"p": p, "pos": pos, "cash": s["cash"],
                       "juste": juste, "latpc": latpc, "cas": _cas})
        couv_s = "INF" if couv == float("inf") else f"{couv:.2f}"
        m_s = "INF" if m == float("inf") else ("NA" if m != m else f"{m:.2f}")
        sc_s = "-INF" if score == float("-inf") else f"{score:.2f}"
        b_s = "NA" if k.get("b") is None else f"{k['b']:.2f}"
        f_s = "NA" if k.get("f") is None else f"{k['f']:.3f}"
        p_s = "NA" if k.get("p") is None else f"{k['p']:.2f}"
        print(f"{p:12s} {s['budget']:5.0f} {pos:8.2f} {s['cash']:8.2f} {couv_s:>6s} "
              f"{latent:8.2f} {latpc:5.1f}% {k['n']:4d} {p_s:>5s} {b_s:>6s} {f_s:>7s} "
              f"{(f'{juste:.2f}' if juste == juste else 'NA'):>7s} {m_s:>6s} {sc_s:>6s}  "
              f"{flag(m, k.get('mesure'), k.get('f'))}")
    m_glob = tot_pos / tot_juste if tot_juste > 1e-9 else float("nan")
    s_glob = 2 * m_glob - m_glob ** 2 if m_glob == m_glob else float("nan")
    print()
    print(f"PORTEFEUILLE (edge mesuré) : pos={tot_pos:.2f} $ juste={tot_juste:.2f} $ "
          f"-> m_global={m_glob:.3f} score={s_glob:.3f}")
    print(f"EXPOSITION TOTALE : {tot_expo:.2f} $ dont SANS edge (f*<=0 ou non mesuré) : "
          f"{expo_sans_edge + (tot_expo - tot_pos - expo_sans_edge):.2f} $ "
          f"— la part sans edge est à m=INF par construction")
    net = tot_brut - tot_cout
    refs = lire_refs_pf()
    rb, rc, rn = refs.get("brut"), refs.get("couts"), refs.get("net")
    if rb is None:
        print("⚠️ header PORTEFEUILLE illisible — validation impossible, STOP.")
        return 2
    print(f"VALIDATION (réfs vivantes du MD) : Σ brut = {tot_brut:.2f} $ (réf {rb:.2f}) · "
          f"Σ coûts = {tot_cout:.2f} $ (réf {rc:.2f}) · net = {net:.2f} $ (réf {rn:.2f}) · "
          f"Σ latent = {tot_lat:.2f} $ (marks {tmarks.isoformat() if tmarks else '?'})")
    if abs(tot_brut - rb) > 0.5 or abs(net - rn) > 2.0 or abs(tot_cout - rc) > 2.0:
        print("⚠️ ÉCART — méthode à revoir, chiffres NON publiés.")
        return 2
    # Preuve de vie par conception (R26 anti-aveugle) : le rituel, le
    # disjoncteur (cap per-trade) et la garde aveugles lisent CE fichier.
    try:
        paires = {}
        for L in lignes:
            if L["cas"] == "sain":
                c2 = 0.5 * L["juste"]
            elif L["cas"] == "sans_edge":
                c2 = 0.0
            else:
                c2 = None  # aveugle : pas de cible, TENIR
            paires[L["p"]] = {"pos": round(L["pos"], 2),
                               "juste": (round(L["juste"], 2)
                                          if L["juste"] == L["juste"] else None),
                               "cible_S2": (round(c2, 2) if c2 is not None else None),
                               "cas": L["cas"]}
        sains = [v["cible_S2"] for v in paires.values()
                 if v["cas"] == "sain" and v["cible_S2"]]
        aveugles = sorted(p for p, v in paires.items()
                          if v["cas"] == "aveugle" and paires[p]["pos"] > 0.01)
        live = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "m_global": round(m_glob, 3) if m_glob == m_glob else None,
                "expo_totale": round(tot_expo, 2),
                "maxS2": round(max(sains), 2) if sains else None,
                "aveugles_pos": aveugles,
                "paires": paires}
        with open(ROOT + "/Index_Maison/thermo/m_kelly_live.json", "w",
                  encoding="utf-8") as f:
            json.dump(live, f, ensure_ascii=False, indent=1)
    except Exception as e:
        print(f"⚠️ preuve de vie non écrite : {e}")
        return 2
    if opts and opts.scenarios:
        scenarios(lignes)
    # --- SHORTS ---
    print()
    print("--- SHORTS (bankroll 100 $) ---")
    for sym in ["btc", "eth", "xrp"]:
        try:
            d = json.load(open(f"{RUNS}/short_{sym}_live.json", encoding="utf-8"))
            s = json.load(open(f"{RUNS}/short_{sym}_state.json", encoding="utf-8"))
        except Exception as e:
            print(f"{sym}: illisible ({e})")
            continue
        trs = s.get("trades") or []
        # AUDIT 02/11 : pnl_usd short = BRUT (short_btc.py:535, aucune fee).
        # Kelly NET : on déduit 2×0.05%×notionnel par trade (estimation
        # documentée — le capital affiché par le moteur est lui aussi brut).
        pnls = [float(t.get("pnl_usd") or 0.0) - 2 * 0.0005 * float(t.get("notional") or 0.0)
                for t in trs]
        nots = [float(t.get("notional") or 0.0) for t in trs if float(t.get("notional") or 0.0) > 0]
        k = kelly(pnls)
        nmed = sorted(nots)[len(nots) // 2] if nots else 0.0
        if k.get("mesure") and k.get("f") is not None and k["f"] > 0:
            juste = k["f"] * 100.0
            m = nmed / juste if juste > 1e-9 else 0.0
        else:
            juste, m = float("nan"), float("nan")
        pos_now = d.get("position")
        print(f"{sym.upper()}: pos_now={pos_now} n={k['n']} p={k.get('p')} b={k.get('b')} "
              f"f*={k.get('f')} notion_med={nmed:.2f} $ juste={juste if juste==juste else 'NA'} $ "
              f"m={m if m==m else 'NA'} cap={d.get('capital')} pnl={d.get('pnl_total')}")
    return 0


if __name__ == "__main__":
    _ap = argparse.ArgumentParser()
    _ap.add_argument("--scenarios", action="store_true",
                     help="scénarios de dégraissage S1/S2/S3 (lecture seule)")
    raise SystemExit(main(_ap.parse_args()))
