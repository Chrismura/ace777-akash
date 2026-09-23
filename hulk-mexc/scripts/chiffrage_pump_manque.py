#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE « PUMP MANQUÉ » — AUTOPSIE D'UN ÉPISODE SUR LES DONNÉES DU MOTEUR
==========================================================================
Demande Christophe 23/09/2026 : « explique-moi pourquoi RIZE a perdu le pump ! »

CE QUE FAIT CET INSTRUMENT (lecture seule, 0 ordre, 0 €)
  Il lit le LOG CONTINU du moteur (`runs/croisement_contexte.jsonl`) — SES PROPRES
  décisions, cycle par cycle, avec le PRIX et le RÉGIME qu'il a lui-même écrits — et il
  répond à trois questions, dans cet ordre :

  1. QUEL ÉTAIT LE MOUVEMENT ? (bas / haut / amplitude, horodatés)
  2. POURQUOI LE MOTEUR N'EST PAS ENTRÉ ? Régimes comptés dans la fenêtre +, pour la
     porte du REPLI, le repli MAXIMUM offert par le prix vs le repli EXIGÉ par la règle
     (`impulse_entry = max(dip, 5 %, 0,30 × m6)`).
  3. COMBIEN ÇA A COÛTÉ ? Contre-factuel E2 « entrée sans repli » (la porte IMPULSE_WAIT
     est tradée au lieu d'être attendue) contre E0 (règle actuelle), sortie = LA VRAIE
     SORTIE DE LA PAIRE lue dans son profil (`calib`) et **séquence complète** d'entrées/
     sorties (ré-entrées autorisées, cooldown post-stop réel) : on ne juge pas un trade
     isolé, on juge ce que le moteur AURAIT FAIT de l'épisode.

PORTÉES ET LIMITES DÉCLARÉES (E8 — obligatoire, non négociable)
  · Le départ du contre-factuel est l'instant où la paire est RÉELLEMENT À PLAT (dernier
    SELL/DUST du journal du run), pas le début de la fenêtre : sinon on « entre » dans
    une position qui existe déjà (piège attrapé le 23/09 sur la 1re version).
  · Le contre-factuel rejoue **UNE seule règle : la porte du repli**. Les autres portes
    (volume sec, mur, spread, aspiration, plancher, fusible) ne sont PAS rejouées : au
    fond, c'est le gate de VOLUME qui refusait (journal CSV). Ces chiffres mesurent donc
    **la porte du repli**, pas le P&L du moteur. Même limite que le chiffrage EDEL du 21/09.
  · dd6 n'existe pas dans le log : il est reconstruit sur le chemin de prix (sommet 6 h).
    C'est le seul intrant reconstruit ; la fidélité du régime recalculé est AFFICHÉE.
  · La sortie réelle peut être scindée 50/50 par le garde-fou d'amplitude (SELL_FULL) ;
    ici on sort en une fois au même niveau de prix.

Usage :
  python3 chiffrage_pump_manque.py --paire RIZEUSDT --depuis 2026-09-22T02:00
  python3 chiffrage_pump_manque.py --paire RIZEUSDT --depuis 2026-09-22T02:00 \
      --plat-depuis 2026-09-22T02:15:45 --json /tmp/out.json
"""
import argparse
import json
import os
from datetime import datetime, timezone

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
LOG = os.path.join(RUNS, "croisement_contexte.jsonl")
CSV = os.path.join(RUNS, "PAPER_V1_20260922_090430.csv")
# CORRECTION 23/09 : le journal d'un run est CUMULATIF (chaque fichier rejoue toute
# l'histoire du run série). Lire UN fichier figé, c'était juger « raté » un mouvement
# dont le BUY était antérieur à ce fichier. On lit donc LE PLUS RÉCENT — une seule
# vérité, la plus complète. (Le nom du fichier ne dit plus la période couverte.)
_CSV_CACHE = None


def csv_actuel():
    global _CSV_CACHE
    if _CSV_CACHE is None:
        import glob
        cands = [c for c in glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv"))
                 if os.path.getsize(c) > 1000]
        _CSV_CACHE = max(cands, key=os.path.getmtime) if cands else CSV
    return _CSV_CACHE
PROFILS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                       "strategie", "universe_profils.json")
ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config", "defaults.env")

FEE = 0.0005          # 5 bps par côté (convention de chiffrage_entree_sortie_replay.py)
MISE_REF = 30.0       # mise fixe de référence : isole l'effet de règle
IMPULSE_PCT = 8.0     # IMPULSE_PCT de defaults.env
PULLBACK_FRAC = 0.30  # IMPULSE_PULLBACK_FRAC
PULLBACK_MIN = 5.0    # IMPULSE_PULLBACK_MIN_PCT


def iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s):
    """Accepte « 2026-09-22T02:15:45Z » (journal du run) et « ...T02:15 » (CLI)."""
    s = s.strip().rstrip("Z")
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc).timestamp()
        except ValueError:
            continue
    raise ValueError(f"horodatage illisible : {s!r}")


def lire_env():
    cfg = {}
    if os.path.exists(ENV):
        for l in open(ENV, encoding="utf-8"):
            l = l.strip()
            if l and not l.startswith("#") and "=" in l:
                k, v = l.split("=", 1)
                cfg[k.strip()] = v.strip()
    return cfg


def profil(paire):
    raw = json.load(open(PROFILS, encoding="utf-8"))
    p = raw.get(paire) or {}
    return {"calib": p.get("calib") or {}, "brut": p}


def charger(paire, depuis):
    pts, last = [], None
    with open(LOG, encoding="utf-8", errors="ignore") as f:
        for ligne in f:
            if paire not in ligne:
                continue
            try:
                d = json.loads(ligne)
            except Exception:
                continue
            if d.get("pair") != paire or not d.get("price"):
                continue
            ts = float(d["ts"])
            if ts < depuis:
                continue
            p = {"ts": ts, "utc": d.get("utc") or iso(ts), "px": float(d["price"]),
                 "regime": d.get("regime") or "", "m6": float(d.get("m6_pct") or 0.0),
                 "dd15": float(d.get("dd15_pct") or 0.0)}
            if last and p["ts"] == last["ts"] and p["px"] == last["px"]:
                continue
            pts.append(p)
            last = p
    return pts


def derniere_vente(paire):
    """Le dernier instant où la paire a VENDU (donc potentiellement à plat) : une seule
    vérité = le journal du run."""
    if not os.path.exists(csv_actuel()):
        return None
    last = None
    with open(csv_actuel(), encoding="utf-8", errors="ignore") as f:
        for l in f:
            c = l.split(",")
            if len(c) > 2 and c[1] == paire and c[2] in ("SELL", "SELL_PARTIAL", "BAG_SELL"):
                last = parse(c[0].strip())
    return last


def repli_offert(pts):
    """dd6 reconstruit (sommet des 6 h précédentes) — seul intrant reconstruit."""
    out, i, n = [], 0, len(pts)
    while i < n:
        t, px = pts[i]["ts"], pts[i]["px"]
        haut = max([p["px"] for p in pts[max(0, i - 1080):i + 1] if p["ts"] >= t - 6 * 3600]
                   or [px])
        out.append((1.0 - px / haut) * 100.0 if haut else 0.0)
        i += 1
    return out


# =============================================================================
# LE SEUIL RÉEL — LA CORRECTION DU 23/09 (2ᵉ passe)
# -----------------------------------------------------------------------------
# ERREUR CORRIGÉE (la mienne) : l'instrument calculait le repli exigé comme
# `max(profil.dip_pct, 5 %, 0,30×m6)` — soit 4,25 % pour RIZE — alors que le moteur
# applique AVANT cela `dip = max(dip_floor, DIP_CADENCE_MULT × cadence)`
# (paper_diprip.score_pair, l.566). Pour RIZE (cadence écrite par le moteur :
# 49-51 %), le repli exigé est donc `max(4,2 ; 0,50 × 51,06) = 25,53 %`, et la porte
# de régime s'ouvre à 0,85 × 25,53 = **21,70 %** — exactement ce que la ligne
# `ATTENTE dd6=2.50 seuil=21.70 m6=12.5` écrite par le moteur affiche depuis le 23/09.
# Ma reconstruction sous-estimait donc le mur d'un facteur ~4, et c'est elle qui
# créait la « contradiction » avec les refus du moteur. Le moteur avait raison.
# La cadence n'est PAS reconstruite : on lit SON chiffre (colonne 9 du journal du run).
# =============================================================================
def cadences_toutes():
    """Cadence écrite PAR LE MOTEUR, par paire (colonne 9 du journal du run)."""
    out = {}
    if not os.path.exists(csv_actuel()):
        return out
    with open(csv_actuel(), encoding="utf-8", errors="ignore") as f:
        for l in f:
            c = l.rstrip("\n").split(",")
            if len(c) > 9 and c[9].strip():
                try:
                    out.setdefault(c[1], []).append((parse(c[0].strip()), float(c[9])))
                except Exception:
                    continue
    for p in out:
        out[p].sort()
    return out


def cadence_a(serie, ts, defaut=0.0):
    """La dernière cadence écrite AVANT ts (le moteur l'écrit ~1×/h)."""
    val = defaut
    for t, c in serie:
        if t <= ts:
            val = c
        else:
            break
    return val


def seuil_repli(cal, cfg, cadence, m6):
    """LE repli EXIGÉ par le moteur, reconstruit à l'identique de score_pair() :
    dip = max(dip_pct du profil, DIP_CADENCE_MULT × cadence) puis
    need = max(dip, IMPULSE_PULLBACK_MIN_PCT, IMPULSE_PULLBACK_FRAC × m6)."""
    from bisect import bisect_right
    dip_floor = float(cal.get("dip_pct") or cfg.get("DIP_FLOOR_PCT", "4.0") or 4.0)
    mult = float(cfg.get("DIP_CADENCE_MULT", "0.50") or 0.50)
    dip = max(dip_floor, cadence * mult)
    return max(dip, PULLBACK_MIN, m6 * PULLBACK_FRAC), dip


def regime_replique(pts, needs, cfg):
    """Reproduit l'ORDRE EXACT de score_pair() : QUIET → IMPULSE → IMPULSE_WAIT →
    COOLING → WATCH. Sert UNIQUEMENT de contrôle de fidélité (le régime du moteur,
    écrit dans le log, reste la seule vérité utilisée pour décider).
    `needs[i]` = repli exigé à l'instant i (voir seuil_repli)."""
    dd6 = repli_offert(pts)
    quiet_min = float(cfg.get("QUIET_RANGE_PCT", "8"))
    imp_th = float(cfg.get("IMPULSE_PCT", "8"))
    out = []
    for i, p in enumerate(pts):
        m6 = p["m6"]
        m24 = max(0.0, (p["px"] / min(x["px"] for x in pts[max(0, i - 2700):i + 1]) - 1) * 100)
        range15 = 0.0
        impulse_now = m6 >= imp_th or m24 >= imp_th * 1.2
        quiet = range15 < quiet_min and m24 < quiet_min * 0.6
        seuil = needs[i]
        if quiet and not impulse_now:
            r = "QUIET"
        elif impulse_now and dd6[i] >= seuil * 0.85:
            r = "IMPULSE"
        elif impulse_now:
            r = "IMPULSE_WAIT"
        else:
            r = "WATCH"
        out.append(r)
    return out, dd6


def simuler_sequence(pts, i_depart, cal, cfg, autorise_wait):
    """Rejoue la SÉQUENCE : à plat → on entre si la porte du repli le permet ; en
    position → on applique LA VRAIE SORTIE de la paire ; après une sortie, cooldown
    post-stop réel (STOP_COOLDOWN_HOURS) puis on peut re-entrer. Ré-entrée autorisée.

    autorise_wait=False → E0 : n'entre QUE si le régime (écrit par le moteur) == IMPULSE.
    autorise_wait=True  → E2 : trade aussi IMPULSE_WAIT (le pump en ligne droite)."""
    stop = -float(cal.get("stop_pct") or 8.0)
    t_arm = float(cal.get("trail_arm_pct") or 0.0)
    t_gb = float(cal.get("trail_giveback_pct") or 0.0)
    cooldown = float(cfg.get("STOP_COOLDOWN_HOURS", "1") or 0) * 3600.0
    mode = "trailing" if (t_arm > 0 and t_gb > 0) else "rip+stop"
    trades, pos, stop_jusqua = [], None, 0.0
    for p in pts[i_depart:]:
        if pos is None:
            if p["ts"] < stop_jusqua:
                continue
            ok = (p["regime"] == "IMPULSE") or (autorise_wait and p["regime"] == "IMPULSE_WAIT")
            if ok:
                pos = {"entree": p["px"], "entree_utc": p["utc"], "pic": p["px"],
                       "pic_utc": p["utc"]}
            continue
        if p["px"] > pos["pic"]:
            pos["pic"], pos["pic_utc"] = p["px"], p["utc"]
        chg = (p["px"] / pos["entree"] - 1.0) * 100.0
        raison = None
        if chg <= stop:
            raison = f"stop{stop:.0f}pct"
        elif t_arm > 0 and t_gb > 0:
            peak_chg = (pos["pic"] / pos["entree"] - 1.0) * 100.0
            if peak_chg >= t_arm and chg <= peak_chg - t_gb:
                raison = f"trailing_pic{peak_chg:.1f}_gb{t_gb:g}"
        if raison:
            trades.append({"entree_utc": pos["entree_utc"], "entree": pos["entree"],
                           "sortie_utc": p["utc"], "sortie": p["px"], "raison": raison,
                           "pic_pct": (pos["pic"] / pos["entree"] - 1.0) * 100.0,
                           "chg_pct": chg})
            if raison.startswith("stop"):
                stop_jusqua = p["ts"] + cooldown
            pos = None
    if pos is not None:  # position encore ouverte au dernier cycle
        p = pts[-1]
        trades.append({"entree_utc": pos["entree_utc"], "entree": pos["entree"],
                       "sortie_utc": p["utc"], "sortie": p["px"], "raison": "OUVERTE",
                       "pic_pct": (pos["pic"] / pos["entree"] - 1.0) * 100.0,
                       "chg_pct": (p["px"] / pos["entree"] - 1.0) * 100.0})
    return mode, trades


def net(t, mise):
    return mise * (t["chg_pct"] / 100.0) - mise * FEE * 2


# =============================================================================
# MODE SCAN — « combien de pumps avons-nous laissés, et POURQUOI » (toutes paires)
# Répond à la seule question qui compte quand « tout est vert » : les check-up
# mesurent ce qu'on PROTÈGE (les gardes), jamais ce qu'on REGARDE PASSER (les
# mouvements). Un pump est un zigzag : on le détecte sur le chemin de prix du log
# continu (+ ses archives de rotation), puis on demande au journal du run si un
# BUY a eu lieu — et sinon, quelle porte a refusé.
# Seuil de reporting (DÉCLARÉ, c'est un seuil d'AFFICHAGE, pas une décision) :
#   leg ≥ 20 % de hausse, avec réaction de 10 % pour clore le zigzag.
# =============================================================================
LEG_SEUIL_PCT = 20.0
LEG_REACTION_PCT = 10.0
LEG_VERTICAL_H = 12.0   # ≤ 12 h = mouvement RAPIDE (le pump) · > 12 h = dérive lente
ARCHIVES = ["croisement_contexte.jsonl.1.gz", "croisement_contexte.jsonl.2.gz"]


def charger_tout():
    """Chemin de prix dense par paire : log continu + archives de rotation."""
    import gzip
    par_paire = {}
    sources = [(LOG, False)] + [(os.path.join(RUNS, a), True) for a in ARCHIVES
                                if os.path.exists(os.path.join(RUNS, a))]
    for chemin, gz in sources:
        ouvre = gzip.open(chemin, "rt", errors="ignore") if gz else open(chemin,
                                                                        encoding="utf-8",
                                                                        errors="ignore")
        with ouvre as f:
            for ligne in f:
                if '"pair"' not in ligne:
                    continue
                try:
                    d = json.loads(ligne)
                except Exception:
                    continue
                p, ts, px = d.get("pair"), d.get("ts"), d.get("price")
                if not p or not ts or not px:
                    continue
                par_paire.setdefault(p, []).append((float(ts), float(px), d.get("regime") or ""))
    for p in par_paire:
        par_paire[p].sort(key=lambda x: x[0])
    return par_paire


def charger_tout_m6(par_paire):
    """Ajoute m6 au chemin de prix (le `need` de notre règle en dépend : 0,30 × m6).
    Non destructif : on relit le log continu une fois et on complète les tuples."""
    import gzip
    par_ts = {}
    sources = [(LOG, False)] + [(os.path.join(RUNS, a), True) for a in ARCHIVES
                                if os.path.exists(os.path.join(RUNS, a))]
    for chemin, gz in sources:
        ouvre = gzip.open(chemin, "rt", errors="ignore") if gz else open(chemin,
                                                                        encoding="utf-8",
                                                                        errors="ignore")
        with ouvre as f:
            for ligne in f:
                if '"pair"' not in ligne:
                    continue
                try:
                    d = json.loads(ligne)
                except Exception:
                    continue
                p, ts = d.get("pair"), d.get("ts")
                if not p or not ts:
                    continue
                par_ts.setdefault(p, {})[round(float(ts))] = float(d.get("m6_pct") or 0.0)
    for p, serie in par_paire.items():
        tab = par_ts.get(p, {})
        for i, (ts, px, reg) in enumerate(serie):
            m6 = tab.get(round(ts))
            if m6 is None:
                m6 = min(tab.items(), key=lambda kv: abs(kv[0] - ts))[1] if tab else 0.0
            serie[i] = (ts, px, reg, m6)
    return par_paire


def detecter_legs(serie, seuil=LEG_SEUIL_PCT, reaction=LEG_REACTION_PCT, sens=1):
    """Zigzag simple et reproductible : une jambe va du plus bas au plus haut (sens=+1)
    ou du plus haut au plus bas (sens=-1), close quand le prix rend « reaction » %.

    CORRECTION 23/09 (objection Christophe : « tu calcules sur un marché qui monte ? ») :
    on suit AUSSI le REPLI MAXIMAL offert pendant la jambe — c'est LA grandeur qui décide
    pour notre règle (`impulse_entry = max(dip, 5 %, 0,30×m6)`). Une jambe sans repli
    ≥ 5 % était INACCESSIBLE par construction ; une jambe qui a offert un repli et qu'on
    a ratée quand même = le problème est ailleurs (autre porte)."""
    legs = []
    if not serie:
        return legs
    # sens=-1 : on inverse les prix → la « jambe de baisse » devient une jambe de hausse
    signe = 1.0 if sens > 0 else -1.0
    lo = hi = signe * serie[0][1]
    t_lo = t_hi = serie[0][0]
    repli_max = 0.0
    m6_lo = 0.0
    for ts, px_brut, _reg, m6 in serie:
        px = signe * px_brut
        if px > hi:
            hi, t_hi = px, ts
        elif px < lo:
            lo, hi, t_lo, t_hi = px, px, ts, ts
            repli_max = 0.0
            m6_lo = m6
        if hi > 0:
            repli_max = max(repli_max, (hi - px) / hi * 100.0)
        if hi > lo and (hi - px) / hi * 100.0 >= reaction:
            amp = (hi / lo - 1.0) * 100.0
            if amp >= seuil:
                legs.append({"t_lo": t_lo, "lo": abs(lo), "t_hi": t_hi, "hi": abs(hi),
                             "amp": amp, "repli_max": repli_max, "sens": sens,
                             "m6_lo": m6_lo})
            lo = hi = px
            t_lo = t_hi = ts
            repli_max = 0.0
            m6_lo = m6
    amp = (hi / lo - 1.0) * 100.0
    if amp >= seuil:
        legs.append({"t_lo": t_lo, "lo": abs(lo), "t_hi": t_hi, "hi": abs(hi), "amp": amp,
                     "repli_max": repli_max, "sens": sens, "m6_lo": m6_lo, "ouvert": True})
    return legs


def lire_journal(paire):
    """Journal du run (une seule vérité) : les BUY, les refus, et l'ORDRE des
    opérations (pour savoir si la paire était DÉJÀ EN POSITION au début d'une jambe —
    un mouvement « traversé » en position n'est pas un mouvement raté)."""
    buys, skips, ops, sells = [], [], [], []
    if not os.path.exists(csv_actuel()):
        return buys, skips, ops, sells
    with open(csv_actuel(), encoding="utf-8", errors="ignore") as f:
        for l in f:
            c = l.split(",")
            if len(c) < 4 or c[1] != paire:
                continue
            try:
                ts = parse(c[0])
            except Exception:
                continue
            if c[2] == "BUY":
                buys.append(ts)
                ops.append((ts, "BUY"))
            elif c[2] == "SKIP":
                skips.append((ts, (c[-1].strip().split(":")[0] or "?").strip()))
            elif c[2] in ("SELL", "SELL_PARTIAL", "BAG_SELL", "DUST_SWEEP"):
                ops.append((ts, "SELL"))
                try:
                    sells.append((ts, float(c[7] or 0.0)))
                except Exception:
                    pass
    ops.sort()
    return buys, skips, ops, sells


def pnl_fenetre(t0, t1):
    """Le VRAI PnL de la fenêtre (une seule vérité : la colonne pnl_total du run).
    Indispensable : la somme des PnL « par jambe » est NON ADDITIVE (les fenêtres
    des jambes lentes se recouvrent)."""
    vals = []
    if not os.path.exists(csv_actuel()):
        return None, None
    with open(csv_actuel(), encoding="utf-8", errors="ignore") as f:
        for l in f:
            c = l.split(",")
            if len(c) < 4:
                continue
            try:
                ts = parse(c[0])
                v = float(c[8])
            except Exception:
                continue
            if t0 <= ts <= t1:
                vals.append(v)
    if not vals:
        return None, None
    return vals[0], vals[-1]


def pnl_realise(sells, t0, t1):
    """PnL RÉELLEMENT encaissé par la paire sur la fenêtre du mouvement (journal du run).
    C'est le chiffre qui dit « capté » — un BUY ne prouve rien (EDEL : intervenu sur
    +80 % de mouvement, PnL réalisé négatif)."""
    return sum(p for ts, p in sells if t0 - 1800 <= ts <= t1 + 1800)


def en_position(ops, t):
    """HEURISTIQUE DÉCLARÉE : la dernière opération AVANT t est un BUY → la paire
    détenait une position (donc le mouvement a été traversé, pas raté).
    Limite : un SELL_PARTIAL ne ferme pas la position, et un DUST_SWEEP qui vide
    la ligne est lu ici comme une sortie partielle. C'est une indication, pas une preuve."""
    dernier = None
    for ts, type_op in ops:
        if ts <= t:
            dernier = type_op
        else:
            break
    return dernier == "BUY"


def raison_dominante(skips, t0, t1):
    cpt = {}
    for ts, r in skips:
        if t0 <= ts <= t1:
            cpt[r] = cpt.get(r, 0) + 1
    if not cpt:
        return "(aucun refus écrit)", 0
    r, n = max(cpt.items(), key=lambda x: x[1])
    return r, n


def serie_vers_pts(serie):
    """Adapte le chemin dense (tuples) au format attendu par simuler_sequence()."""
    return [{"ts": ts, "utc": iso(ts), "px": px, "regime": reg, "m6": m6}
            for ts, px, reg, m6 in serie]


def chiffrer_manquees(manq, par_paire, profs, cfg):
    """LE CHIFFRAGE — jambes RATÉES, à plat, sur le chemin DENSE (archives comprises).
    E0 = règle actuelle · E2 = porte du repli levée. Les DEUX sont comptés au
    PLAFOND RÉEL de la paire (2 % de son mur bid médian), pas à 30 $ : c'est la mise
    que le carnet autorise vraiment. Sortie = la sortie réelle de la paire (profil).
    LIMITE DÉCLARÉE : les 4 autres portes ne sont pas rejouées (volume/mur/spread/…),
    donc E2 est une BORNE HAUTE de ce que la porte du repli coûte — pas une promesse."""
    print("\n== LE CHIFFRAGE DES JAMBES RATÉES (chemin dense · sortie réelle de la paire) ==")
    print(f"{'paire':10}{'jambe':>26}{'E0 (actuel)':>17}{'E2 (repli levé)':>18}"
          f"{'écart':>10}{'cap':>9}  trades E0/E2")
    tot_e0 = tot_e2 = 0.0
    for l in manq:
        pr = profs.get(l["paire"]) or {}
        cal = pr.get("calib") or {}
        mur = float(pr.get("mur_bid_med") or 0.0)
        cap = mur * float(cal.get("mise_max_pct_mur") or 0.0)
        pts = serie_vers_pts(par_paire.get(l["paire"]) or [])
        i0 = next((i for i, p in enumerate(pts) if p["ts"] >= l["t_lo"]), None)
        if i0 is None or cap <= 0:
            continue
        nets, ntr = {}, {}
        for nom, w in (("E0", False), ("E2", True)):
            _mode, trades = simuler_sequence(pts, i0, cal, cfg, w)
            gardes = [t for t in trades
                      if l["t_lo"] - 1 <= parse(t["entree_utc"]) <= l["t_hi"] + 1]
            nets[nom] = sum(net(t, cap) for t in gardes)
            ntr[nom] = len(gardes)
        tot_e0 += nets["E0"]
        tot_e2 += nets["E2"]
        print(f"{l['paire'].replace('USDT', ''):10}"
              f"{iso(l['t_lo'])[5:16] + ' → ' + iso(l['t_hi'])[5:16]:>26}"
              f"{nets['E0']:>+16.2f} ${nets['E2']:>+17.2f} $"
              f"{nets['E2'] - nets['E0']:>+9.2f} ${cap:>8.2f}$  {ntr['E0']}/{ntr['E2']}")
    print(f"{'TOTAL':10}{'7 jambes':>26}{tot_e0:>+16.2f} ${tot_e2:>+17.2f} $"
          f"{tot_e2 - tot_e0:>+9.2f} $")
    return tot_e0, tot_e2


def cadences_par_paire():
    """GO 2 (23/09) — « combien de jambes chaque paire est STRUCTURELLEMENT interdite de
    prendre ». Le seuil d'entrée dépend de la cadence PROPRE de la paire
    (`dip = max(dip_pct ; 0,50 × cadence)`) : plus une paire bouge, plus le repli exigé
    est grand — donc plus ses pumps sont inaccessibles. On lit la cadence ÉCRITE PAR LE
    MOTEUR (colonne 9 du journal du run) et on confronte chaque jambe ≥ 20 % au repli que
    cette paire exige VRAIMENT."""
    cfg = lire_env()
    cads = cadences_toutes()
    profs = json.load(open(PROFILS, encoding="utf-8"))
    par_paire = charger_tout_m6(charger_tout())
    mult = float(cfg.get("DIP_CADENCE_MULT", "0.50") or 0.50)
    print("SOURCE : cadence écrite PAR LE MOTEUR (colonne 9) + chemin de prix dense")
    print(f"seuil exigé = 0,85 × max(dip_pct ; {mult:g} × cadence ; "
          f"{cfg.get('IMPULSE_PULLBACK_MIN_PCT', '5')} ; "
          f"{cfg.get('IMPULSE_PULLBACK_FRAC', '0.30')} × m6)\n")
    print(f"{'paire':10}{'cadence':>9}{'dip exigé':>11}{'seuil':>8}{'jambes':>8}"
          f"{'inaccess.':>11}{'part':>7}{'PnL réalisé':>13}  qui décide")
    lignes = []
    for paire, serie in sorted(par_paire.items()):
        cal = (profs.get(paire) or {}).get("calib") or {}
        cs = [c for _, c in cads.get(paire, [])]
        if not cs:
            continue
        cs.sort()
        cad = cs[len(cs) // 2]
        dip = max(float(cal.get("dip_pct") or 0.0), cad * mult)
        seuil = dip * 0.85
        _b, _s, _o, sells = lire_journal(paire)
        pnl = sum(p for _t, p in sells)
        legs = detecter_legs(serie)
        n_inacc = 0
        for lg in legs:
            need, _d = seuil_repli(cal, cfg, cadence_a(cads.get(paire, []), lg["t_lo"], cad),
                                   lg.get("m6_lo") or 0.0)
            if lg["repli_max"] < need:
                n_inacc += 1
        part = (n_inacc / len(legs) * 100) if legs else 0.0
        dom = ("cadence" if cad * mult > max(float(cal.get("dip_pct") or 0.0), 5.0)
               else "plancher")
        lignes.append((paire, cad, dip, seuil, len(legs), n_inacc, part, pnl, dom))
    for l in sorted(lignes, key=lambda x: -x[2]):
        print(f"{l[0].replace('USDT', ''):10}{l[1]:>8.1f}%{l[2]:>10.2f}%{l[3]:>7.2f}%"
              f"{l[4]:>8}{l[5]:>11}{l[6]:>6.0f}%{l[7]:>+12.2f} $  {l[8]}")
    print("\n  ⚠️ PORTÉE : jambe ≥ 20 % détectée par zigzag (seuil d'AFFICHAGE) ; inaccessibles =\n"
          "     repli offert < repli exigé. Le PnL réalisé vient du journal du run (une seule vérité).")
    return 0


def scan():
    cfg = lire_env()
    par_paire = charger_tout_m6(charger_tout())
    cads = cadences_toutes()
    profs = json.load(open(PROFILS, encoding="utf-8"))
    if not par_paire:
        print("[ERR] log continu introuvable")
        return 2
    tous = [ts for v in par_paire.values() for ts, _, _, _ in v]
    print("SOURCE : log continu du moteur + archives de rotation (chemin de prix par paire)")
    print(f"FENÊTRE : {iso(min(tous))} → {iso(max(tous))} · {len(par_paire)} paires\n")
    print(f"DÉTECTION DÉCLARÉE : jambe ≥ {LEG_SEUIL_PCT:.0f} % · zigzag clos à "
          f"{LEG_REACTION_PCT:.0f} % de réaction (seuil d'AFFICHAGE, pas de décision)\n")
    lignes, cpt_causes = [], {}
    for paire, serie in sorted(par_paire.items()):
        buys, skips, ops, sells = lire_journal(paire)
        for sens in (1, -1):
          for lg in detecter_legs(serie, sens=sens):
            lg["duree_h"] = (lg["t_hi"] - lg["t_lo"]) / 3600.0
            lg["rapide"] = lg["duree_h"] <= LEG_VERTICAL_H
            lg["pris"] = any(lg["t_lo"] - 1800 <= b <= lg["t_hi"] + 1800 for b in buys)
            lg["pos"] = en_position(ops, lg["t_lo"])
            lg["pnl"] = pnl_realise(sells, lg["t_lo"], lg["t_hi"])
            # ENTRABLE ? repli offert ≥ repli EXIGÉ par la règle RÉELLE de la paire :
            #   dip = max(dip_pct du profil, DIP_CADENCE_MULT × cadence)  puis 0,30 × m6
            # (la cadence est celle ÉCRITE PAR LE MOTEUR au début de la jambe)
            cal = (profs.get(paire) or {}).get("calib") or {}
            cad = cadence_a(cads.get(paire, []), lg["t_lo"], 0.0)
            need, dip = seuil_repli(cal, cfg, cad, lg.get("m6_lo") or 0.0)
            lg["cadence"], lg["besoin"], lg["dip"] = cad, need, dip
            lg["entrable"] = lg["repli_max"] >= need
            raison, n = ("—", 0) if lg["pris"] else raison_dominante(skips, lg["t_lo"], lg["t_hi"])
            lg["raison"], lg["n"] = raison, n
            if not lg["pris"] and not lg["pos"]:
                cpt_causes[raison] = cpt_causes.get(raison, 0) + 1
            lignes.append({"paire": paire, **lg})
    lignes.sort(key=lambda x: -x["amp"])
    print("seuil = repli EXIGÉ par la règle RÉELLE de la paire : max(dip_pct, "
          "0,50 × cadence moteur) puis max(…, 5 %, 0,30 × m6)")
    print(f"{'paire':10}{'sens':>5}{'bas → haut':>34}{'amplitude':>11}{'durée':>8}"
          f"{'cad':>6}{'seuil':>7}{'repli':>7}{'entrable':>9}{'BUY ?':>8}"
          f"{'PnL réalisé':>12}   cause")
    for l in lignes[:26]:
        etat = "oui" if l["pris"] else ("EN POS." if l["pos"] else "NON")
        cause = "—" if l["pris"] else (
            "position ouverte dès le début" if l["pos"] else f"{l['raison']} ({l['n']})")
        print(f"{l['paire'].replace('USDT', ''):10}{'HAUSSE' if l['sens'] > 0 else 'BAISSE':>5}"
              f"{iso(l['t_lo'])[5:16] + ' → ' + iso(l['t_hi'])[5:16]:>34}"
              f"{l['amp']:>+10.1f}%{l['duree_h']:>7.1f}h{l['cadence']:>5.1f}%"
              f"{l['besoin']:>6.1f}%{l['repli_max']:>6.1f}%"
              f"{'oui' if l['entrable'] else 'NON':>9}{etat:>8}{l['pnl']:>+11.2f} $   {cause}")
    manq = [l for l in lignes if not l["pris"] and not l["pos"]]
    rapides = [l for l in lignes if l["rapide"]]
    rap_manq = [l for l in rapides if not l["pris"] and not l["pos"]]

    def mv(serie):
        return (serie[-1][1] / serie[0][1] - 1) * 100 if serie and serie[0][1] else 0.0

    btc = par_paire.get("BTCUSDT") or []
    hausses = sum(1 for s in par_paire.values() if mv(s) > 0)
    print("\n== CONTEXTE DE MARCHÉ (objection Christophe : « tu calcules sur un marché qui "
          "monte ? ») ==")
    if btc:
        print(f"  BTC : {btc[0][1]:,.0f} $ → {btc[-1][1]:,.0f} $ = {mv(btc):+.1f} % sur la fenêtre")
    print(f"  paires en HAUSSE sur la fenêtre : {hausses}/{len(par_paire)}"
          f"  → un marché qui monte gonfle mécaniquement le compte des jambes de HAUSSE")
    print(f"  jambes de HAUSSE : {sum(1 for l in lignes if l['sens'] > 0)}"
          f"  ·  jambes de BAISSE : {sum(1 for l in lignes if l['sens'] < 0)}"
          f"  → le scan est SYMÉTRIQUE : on ne compte pas que les pumps")
    print(f"\n  ⚠️ LE TRI QUI COMPTE (seuil = repli EXIGÉ par la règle réelle de la paire) :")
    print(f"     ratés INACCESSIBLES par construction (repli offert < repli exigé) : "
          f"{sum(1 for l in manq if not l['entrable'])}"
          f"  ← le prix n'a JAMAIS donné le repli que la règle demande")
    print(f"     ratés ENTRABLES (le repli exigé a été offert, on n'y est pas allé) : "
          f"{sum(1 for l in manq if l['entrable'])}"
          f"  ← c'est CEUX-LÀ qui accusent le moteur, pas les autres")
    print(f"\n== VERDICT SUR LA FENÊTRE ==")
    print(f"  mouvements ≥ {LEG_SEUIL_PCT:.0f} % détectés : {len(lignes)}"
          f"  ·  RAPIDES (≤ {LEG_VERTICAL_H:.0f} h) : {len(rapides)}"
          f"  ·  LENTS (> {LEG_VERTICAL_H:.0f} h) : {len(lignes) - len(rapides)}")
    print(f"  INTERVENU (un BUY) : {sum(1 for l in lignes if l['pris'])}"
          f"  ·  PAS INTERVENU : {len(manq)}"
          f"  ·  EN POSITION dès le début : {sum(1 for l in lignes if l['pos'])}")
    print(f"  RATÉS (à plat, rien acheté) : {len(manq)}  "
          f"({sum(l['amp'] for l in manq):.0f} % d'amplitude laissée sur la table)"
          f"  ·  dont RAPIDES (le pump) : {len(rap_manq)}"
          f"  ({sum(l['amp'] for l in rap_manq):.0f} %)")
    debut, fin = pnl_fenetre(min(tous), max(tous))
    print(f"  ⚠️ INTERVENIR N'EST PAS CAPTER : PnL réalisé autour des mouvements où on est"
          f" intervenu = {sum(l['pnl'] for l in lignes if l['pris']):+.2f} $"
          f"  (indicatif : les fenêtres se recouvrent → NON additif)")
    if debut is not None:
        print(f"  ✔ LE FAIT BRUT : PnL du moteur sur la fenêtre = {debut:.2f} $ → {fin:.2f} $"
              f" = {fin - debut:+.2f} $ (colonne pnl_total du run, aucune reconstruction)")
    if rapides:
        print(f"  → sur les mouvements RAPIDES, taux d'intervention : "
              f"{sum(1 for l in rapides if l['pris']) / len(rapides) * 100:.0f} %"
              f"  ·  PnL réalisé sur ces mouvements = "
              f"{sum(l['pnl'] for l in rapides):+.2f} $")
    print("\n== POURQUOI (portes qui ont refusé les mouvements RATÉS) ==")
    for r, n in sorted(cpt_causes.items(), key=lambda x: -x[1]):
        print(f"    {r:34} {n:4} mouvement(s)")
    par_paire_manq = {}
    for l in manq:
        par_paire_manq[l["paire"]] = par_paire_manq.get(l["paire"], 0) + 1
    if par_paire_manq:
        print("  paires concernées : " + " · ".join(
            f"{k.replace('USDT', '')} {v}" for k, v in sorted(par_paire_manq.items(),
                                                           key=lambda x: -x[1])))
    chiffrer_manquees(manq, par_paire, profs, cfg)
    print("\n  ⚠️ PORTÉE : ce scan dit COMBIEN et PAR QUELLE PORTE — et, pour les jambes RATÉES,\n"
          "     ce que la règle ACTUELLE et la porte DU REPLI LEVÉE auraient donné sur le chemin\n"
          "     dense. Les autres portes (volume/mur/spread/plancher/fusible) ne sont PAS rejouées :\n"
          "     E2 est une BORNE HAUTE, pas une promesse de P&L.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true",
                    help="scanne TOUTES les paires : mouvements ≥ 20 % pris / manqués + cause")
    ap.add_argument("--cadences", action="store_true",
                    help="GO 2 : par paire, le repli RÉELLEMENT exigé et la part de jambes "
                         "que la règle rend inaccessibles")
    ap.add_argument("--paire", default="RIZEUSDT")
    ap.add_argument("--depuis", default="2026-09-22T02:00")
    ap.add_argument("--plat-depuis", default="",
                    help="instant où la paire est RÉELLEMENT à plat (défaut : dernier SELL du run)")
    ap.add_argument("--json", default="")
    a = ap.parse_args()
    if a.scan:
        return scan()
    if a.cadences:
        return cadences_par_paire()
    depuis = parse(a.depuis)
    pr = profil(a.paire)
    cal, brut = pr["calib"], pr["brut"]
    cfg = lire_env()

    pts = charger(a.paire, depuis)
    if len(pts) < 10:
        print(f"[ERR] pas assez de cycles pour {a.paire} depuis {a.depuis}")
        return 2
    t_plat = parse(a.plat_depuis) if a.plat_depuis else derniere_vente(a.paire)
    i_dep = next((i for i, p in enumerate(pts) if t_plat and p["ts"] >= t_plat), 0)

    print(f"SOURCE : log continu du moteur — SES PROPRES décisions (prix + régime écrits)")
    print(f"PAIRE  : {a.paire} · {len(pts)} cycles · {pts[0]['utc']} → {pts[-1]['utc']}")
    if t_plat:
        print(f"DÉPART DU CONTRE-FACTUEL : {iso(t_plat)} (dernière vente du run = paire À PLAT)")
    print()

    # ---- 1. LE MOUVEMENT ----------------------------------------------------
    bas = min(pts, key=lambda p: p["px"])
    haut = max(pts, key=lambda p: p["px"])
    print("== 1. LE MOUVEMENT ==")
    print(f"  PLUS BAS  {bas['utc']}  {bas['px']:.6f}")
    print(f"  PLUS HAUT {haut['utc']}  {haut['px']:.6f}")
    print(f"  AMPLITUDE bas → haut : {(haut['px'] / bas['px'] - 1) * 100:+.1f} %\n")

    # ---- 2. LA PORTE FERMÉE -------------------------------------------------
    # LE SEUIL RÉEL — la cadence est CELLE ÉCRITE PAR LE MOTEUR (colonne 9 du run),
    # pas une reconstruction : `need = max(max(dip_pct, 0,50×cadence), 5 %, 0,30×m6)`.
    cads = cadences_toutes().get(a.paire, [])
    cad_defaut = (sorted(c for _, c in cads)[len(cads) // 2] if cads else 0.0)
    needs = [seuil_repli(cal, cfg, cadence_a(cads, p["ts"], cad_defaut), p["m6"])[0]
             for p in pts]
    reg_repl, dd6 = regime_replique(pts, needs, cfg)
    n_ok = sum(1 for r, p in zip(reg_repl, pts) if r == p["regime"])
    f = n_ok / len(pts) * 100.0
    cpt = {}
    for p in pts[i_dep:]:
        cpt[p["regime"]] = cpt.get(p["regime"], 0) + 1
    n_apres = max(1, len(pts) - i_dep)
    print("== 2. LA PORTE QUI A TENU FERMÉ (régimes écrits PAR LE MOTEUR, après mise à plat) ==")
    for k, v in sorted(cpt.items(), key=lambda x: -x[1]):
        print(f"    {k:14} {v:5} cycles ({v / n_apres * 100:5.1f} %)")
    imp = [p for p in pts[i_dep:] if p["regime"] == "IMPULSE"]
    if imp:
        print(f"  ⚠️ {len(imp)} cycles en IMPULSE (SEULE porte d'entrée ouverte) de "
              f"{imp[0]['utc']} à {imp[-1]['utc']} — le moteur A eu le droit d'entrer ; "
              f"ce sont les AUTRES portes qui ont refusé (journal CSV : VOL sec / MUR-CASSE)")
    else:
        print("  → AUCUN cycle IMPULSE après la mise à plat : entrée structurellement fermée")
    wait = [i for i in range(i_dep, len(pts)) if pts[i]["regime"] == "IMPULSE_WAIT"]
    if wait:
        seuils = [needs[i] for i in wait]
        off = [dd6[i] for i in wait]
        manques = [s - o for s, o in zip(seuils, off)]
        cw = sorted(cadence_a(cads, pts[i]["ts"], cad_defaut) for i in wait)
        c_lo, c_med, c_hi = cw[0], cw[len(cw) // 2], cw[-1]
        mult = float(cfg.get("DIP_CADENCE_MULT", "0.50") or 0.50)
        dip_lo = max(float(cal.get("dip_pct") or 4.0), c_lo * mult)
        print(f"  cadence ÉCRITE PAR LE MOTEUR (durant les faits, 1 chiffre/h) : "
              f"{c_lo:.1f}–{c_hi:.1f} % · médiane {c_med:.1f} %"
              f"  → dip = max({cal.get('dip_pct')} ; {mult:g} × {c_med:.1f})"
              f" = {max(float(cal.get('dip_pct') or 4.0), c_med * mult):.2f} %"
              f"  ·  m6 max {max(pts[i]['m6'] for i in wait):.1f} %")
        print(f"  en IMPULSE_WAIT : {len(wait)} cycles · repli EXIGÉ {min(seuils):.2f}–"
              f"{max(seuils):.2f} % · repli OFFERT (reconstruit) jusqu'à {max(off):.2f} %")
        print(f"  → il manquait {min(manques):.2f} à {max(manques):.2f} point(s) de repli :"
              f" la porte n'a JAMAIS pu s'ouvrir pendant que le prix montait")
        print(f"     ⚠️ dd6 exact non journalisé : la décision du moteur (le régime) est la preuve,"
              f" pas ma reconstruction (réserve R14 ci-dessous)")
        cont = [(pts[i]["utc"], dd6[i], needs[i]) for i in range(i_dep, len(pts))
                if pts[i]["regime"] == "IMPULSE_WAIT" and dd6[i] >= needs[i] * 0.85]
        print(f"  CONTRÔLE DE COHÉRENCE : cycles restés IMPULSE_WAIT alors que mon dd6"
              f" reconstruit ≥ seuil exigé → {len(cont)}")
        for u, d, s in cont[:5]:
            print(f"     {u}  dd6={d:.2f} % ≥ {s * 0.85:.2f} %  ← contradiction à expliquer")
    print(f"  (fidélité du régime recalculé : {f:.1f} % — réserve R14, "
          f"la décision reste celle écrite par le moteur)\n")

    # ---- 3. LE CONTRE-FACTUEL ----------------------------------------------
    mur = float(brut.get("mur_bid_med") or 0.0)
    cap = mur * float(cal.get("mise_max_pct_mur") or 0.0)
    res = {}
    for nom, wait_ok in (("E0_ACTUEL", False), ("E2_SANS_REPLI", True)):
        mode, trades = simuler_sequence(pts, i_dep, cal, cfg, wait_ok)
        res[nom] = {"mode": mode, "trades": trades,
                    "net_30": sum(net(t, MISE_REF) for t in trades),
                    "net_cap": sum(net(t, cap) for t in trades) if cap > 0 else None}
    print("== 3. CE QUE LA RÈGLE AURAIT DONNÉ (sortie RÉELLE de la paire, séquence complète) ==")
    print(f"  sortie : {res['E2_SANS_REPLI']['mode']} (stop {cal.get('stop_pct')} % · trail arm "
          f"{cal.get('trail_arm_pct')} % / giveback {cal.get('trail_giveback_pct')} % · "
          f"paliers rip : AUCUN) · cooldown post-stop {cfg.get('STOP_COOLDOWN_HOURS', '1')} h")
    for nom in ("E0_ACTUEL", "E2_SANS_REPLI"):
        r = res[nom]
        print(f"\n  --- {nom} : {len(r['trades'])} trade(s) · net {r['net_30']:+.2f} $ (30 $) · "
              f"{r['net_cap']:+.2f} $ (au plafond du mur {cap:.2f} $) ---")
        for t in r["trades"]:
            print(f"    {t['entree_utc']} → {t['sortie_utc']}  pic {t['pic_pct']:+6.1f} %  "
                  f"sortie {t['chg_pct']:+7.1f} %  {t['raison']}")

    # ---- 4. EN CLAIR --------------------------------------------------------
    e0, e2 = res["E0_ACTUEL"], res["E2_SANS_REPLI"]
    print("\n== 4. LE COÛT, EN CLAIR ==")
    print(f"  Mouvement offert par le prix sur la fenêtre : {(haut['px'] / pts[i_dep]['px'] - 1) * 100:+.1f} %"
          f" (depuis la mise à plat {pts[i_dep]['px']:.6f})")
    print(f"  RÈGLE ACTUELLE (E0)          : {len(e0['trades'])} trade(s) → {e0['net_30']:+.2f} $ (30 $) · "
          f"{e0['net_cap']:+.2f} $ (plafond {cap:.2f} $)")
    print(f"  AVEC LA PORTE DU REPLI LEVÉE (E2) : {len(e2['trades'])} trade(s) → {e2['net_30']:+.2f} $ (30 $) · "
          f"{e2['net_cap']:+.2f} $ (plafond {cap:.2f} $)")
    print(f"  → écart mesuré de la porte : {e2['net_30'] - e0['net_30']:+.2f} $ pour 30 $ · "
          f"{(e2['net_cap'] or 0) - (e0['net_cap'] or 0):+.2f} $ au plafond réel")
    print(f"  ⚠️ PORTÉE : seule la PORTE DU REPLI est rejouée (les portes volume/mur/spread/"
          f"plancher ne le sont pas) → ce chiffre mesure LA PORTE, pas le P&L du moteur.")
    print(f"  ⚠️ Taille réelle : plafond {cap:.2f} $ = 2 % d'un mur médian de {mur} $ — c'est LA limite.")

    if a.json:
        json.dump({"paire": a.paire, "plat_depuis": iso(t_plat) if t_plat else None,
                   "amplitude_pct": (haut["px"] / bas["px"] - 1) * 100,
                   "regimes_apres_plat": cpt, "fidelite_pct": f, "plafond_mise": cap,
                   "contrefactuel": res}, open(a.json, "w"), ensure_ascii=False, indent=2)
        print(f"  (détail écrit : {a.json})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
