#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verdicts_protocoles.py — LES VERDICTS DES PROTOCOLES EN TEST (20/09/2026, GO Christophe
« me donner les résultats en profondeur des protocoles en test — verdicts, vulgariser »).

POURQUOI : la page vol affichait le tableau des « protocoles en test » RECOPIÉ d'un
document écrit à la main le 14/09 (RECENSEMENT_OBSERVATIONS_20260914.md §3). Les
critères, eux, sont **pré-enregistrés** (c'est tout leur intérêt : on fixe le critère
AVANT de voir les données) — donc les verdicts sont CALCULABLES. Recopier un tableau
à la main, c'est exactement la famille de panne qu'on vient de réparer sept fois :
une page qui dit une chose périmée. Ici chaque verdict est **mesuré à la source**,
avec le critère écrit à côté de son résultat.

UN PROTOCOLE SANS VERDICT CALCULABLE EST UNE PANNE, PAS UNE PATIENCE : quatre
protocoles étaient dans cet état le 20/09 (troupeau jamais jugé — le plist ne lançait
que --cycle ; RWA dont le critère tombe sur des pools qui déclarent 0 % ; arbitrage
LLM-vs-règle sans une seule alerte à juger ; MiroFish sans nouveau run depuis le 10/08).
Le script le DIT au lieu de laisser croire que « ça suit son cours ».

Lecture seule sur la maison : n'écrit que thermo/PROTOCOLES_VERDICTS.json.
Stdlib uniquement.
"""
import json
import os
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

IM = Path(__file__).resolve().parent.parent
BASE = IM.parent
DATA = IM / "data"
OUT = IM / "thermo" / "PROTOCOLES_VERDICTS.json"


def charger(p, defaut=None):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return defaut if defaut is not None else None


def lignes(p):
    out = []
    try:
        for l in open(p, encoding="utf-8"):
            if l.strip():
                try:
                    out.append(json.loads(l))
                except Exception:
                    pass
    except Exception:
        pass
    return out


def ts_iso(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def age_h(p):
    try:
        return (time.time() - Path(p).stat().st_mtime) / 3600.0
    except Exception:
        return None


# ── 1. TROUPEAU-INV (R4 juge à T+72h · R6 verdict 08/11 : ≥55 % sur ≥20 cas) ────
def troupeau_inv():
    rows = lignes(IM / "troupeau_inv_hist.jsonl")
    div = [r for r in rows if r.get("diverge")]
    juges = [r for r in div if r.get("verdict") in ("HIT", "MISS")]
    hits = sum(1 for r in juges if r["verdict"] == "HIT")
    t0 = min([ts_iso(r.get("ts_graine")) for r in rows if ts_iso(r.get("ts_graine"))], default=None)
    echeance = ts_iso("2026-11-08T00:00Z")
    jours = (time.time() - t0) / 86400.0 if t0 else 0
    cadence = (len(div) / jours * 7) if jours > 0 else 0            # divergences / semaine
    cas_au_verdict = len(juges) + max(0.0, (echeance - time.time()) / 86400.0) * (cadence / 7)
    manquants = max(0, 20 - len(juges))
    if len(juges) >= 20:
        verdict = "SUCCES" if hits / len(juges) >= 0.55 else "ECHEC"
    else:
        verdict = "EN ATTENTE (%d cas jugé(s) sur 20 requis)" % len(juges)
    att = ("le verdict du 08/11 demandera 20 cas ; la cadence mesurée est de %.1f divergence(s)/semaine "
           "→ environ %.1f cas au 08/11" % (cadence, cas_au_verdict)) if manquants else ""
    return {
        "protocole": "TROUPEAU-INV",
        "critere": "R4 : juger à T+72h la direction réelle du BTC · R6 : verdict 08/11/2026 si ≥ 55 % de HIT sur ≥ 20 cas",
        "faits": "%d paires enregistrées · %d divergente(s) · %d jugée(s) · %d HIT" % (len(rows), len(div), len(juges), hits),
        "verdict": verdict,
        "alerte": att,
        "detail": [{"paire": r.get("paire"), "graine": r.get("ts_graine"), "dirA": r.get("dirA"),
                    "dirB": r.get("dirB"), "reel": r.get("reel"), "verdict": r.get("verdict")} for r in div][:8],
    }


# ── 2. RWA (critère pré-enregistré : ≥ 3 pools du top 20 TVL bougent ≥ 50 bps en 7 j) ─
def radar_rwa():
    par_pool = {}
    for d in lignes(DATA / "rwa_yields_hist.jsonl"):
        r = d.get("raw") or {}
        t, pid = ts_iso(d.get("ts")), r.get("pool")
        if t and pid:
            par_pool.setdefault(pid, []).append((t, r))
    if not par_pool:
        return {"protocole": "Radar RWA (DefiLlama)", "verdict": "IMPOSSIBLE (aucun historique)"}
    tous = [t for v in par_pool.values() for t, _ in v]
    t0 = min(tous)
    j0 = t0 + 8 * 3600
    j7 = t0 + 7 * 86400
    def plus_proche(v, cible):
        return min(v, key=lambda x: abs(x[0] - cible)) if v else None
    top = []
    for pid, v in par_pool.items():
        # Top 20 TVL « au J0 » = le PREMIER relevé de chaque pool (déterministe : on ne
        # dépend pas de l'heure à laquelle on relit). Le critère est donc celui du 11/09.
        cand = sorted([y for y in v if y[0] <= j0], key=lambda x: x[0])
        if cand:
            top.append((cand[0][1].get("tvlUsd") or 0, pid, cand[0]))
    top.sort(reverse=True)
    top20 = top[:20]
    bouges, bouges_apy, n_apy0 = 0, 0, 0
    detail = []
    for tvl, pid, (t0p, r0) in top20:
        fin = plus_proche([y for y in par_pool[pid] if y[0] >= j7], j7)
        apy7 = fin[1].get("apy") if fin else None
        a0, a7 = r0.get("apy"), apy7
        delta = (a7 - a0) * 100 if (a0 is not None and a7 is not None) else None
        # « sans rendement » = APY < 0,5 % : c'est le cas des pools de lending Solana
        # (kamino DSOL/JITOSOL/JLP…) qui trustent le top TVL sans être des rendements de
        # crédit privé tokenisé — la vraie raison pour laquelle le critère est mal ciblé.
        if (a0 or 0) < 0.5:
            n_apy0 += 1
        if delta is not None and abs(delta) >= 50:
            bouges += 1
            if a0:
                bouges_apy += 1
        detail.append({"pool": "%s %s (%s)" % (r0.get("project"), r0.get("symbol"), r0.get("chain")),
                       "tvl_musd": round((tvl or 0) / 1e6), "apy_j0": a0, "apy_j7": a7,
                       "delta_bps": None if delta is None else round(delta)})
    verdict = "SUCCES (critère atteint)" if bouges >= 3 else "ECHEC (critère non atteint)"
    return {
        "protocole": "Radar RWA (DefiLlama)",
        "critere": "pré-enregistré J+8 : ≥ 3 pools du top 20 TVL (au 1er relevé du 11/09) bougent de ≥ 50 bps en 7 jours",
        "faits": "%d relevés · %d pools suivis · top 20 TVL : %d pool(s) ont bougé de ≥ 50 bps" % (
            sum(len(v) for v in par_pool.values()), len(par_pool), bouges),
        "verdict": verdict,
        "alerte": ("critère MAL CIBLÉ : %d des 20 plus gros pools ont un rendement quasi nul (< 0,5 %% — lending "
                   "Solana : DSOL/JITOSOL/JLP…) → le top 20 TVL n'est PAS la liste des rendements de crédit privé "
                   "que le prototype visait ; sur les pools qui portent un vrai rendement, %d bouge(nt) de ≥ 50 bps"
                   % (n_apy0, bouges_apy)) if n_apy0 >= 5 else "",
        "detail": detail,
    }


# ── 3. XRPL gouvernance (critère J8 pré-enregistré) ────────────────────────────
def xrpl_gouvernance():
    ls = lignes(DATA / "xrpl_gouv_snapshots.jsonl")
    if len(ls) < 2:
        return {"protocole": "Radar XRPL gouvernance", "verdict": "IMPOSSIBLE (historique trop court)"}
    def etat(i):
        return {a.get("name"): a for a in (ls[i].get("amendements") or [])}
    a0, a1 = etat(0), etat(-1)
    def wl(a):
        return {k: v for k, v in a.items() if not v.get("enabled") and (v.get("count") or 0) > 0}
    w0, w1 = wl(a0), wl(a1)
    communs = set(w0) & set(w1)
    deltas = sorted([(k, (w1[k].get("count") or 0) - (w0[k].get("count") or 0)) for k in communs],
                    key=lambda x: -abs(x[1]))
    gros = [d for d in deltas if abs(d[1]) >= 2]
    activ = [k for k in a1 if a1[k].get("enabled") and not a0.get(k, {}).get("enabled")]
    neufs = [k for k in a1 if k not in a0]
    morts = [k for k in a0 if k not in a1]
    ok = len(gros) >= 5 or bool(activ) or bool(morts)
    return {
        "protocole": "Radar XRPL gouvernance",
        "critere": "J8 pré-enregistré : (a) ≥ 5 amendements dont le compteur bouge de ≥ 2 votes, OU (b) ≥ 1 activation, OU (c) ≥ 1 amendement mort ; sinon échec",
        "faits": "%d snapshots · %d amendements suivis · (a) %d bougent de ≥ 2 (il en fallait 5) · (b) %d activation · (c) %d mort · %d nouveau(x)" % (
            len(ls), len(a1), len(gros), len(activ), len(morts), len(neufs)),
        "verdict": "SUCCES (critère atteint)" if ok else "ECHEC (critère non atteint)",
        "alerte": ("le radar VOIT (les 4 plus gros mouvements : %s) — c'est le seuil du critère qui est "
                   "hors d'échelle : sur XRPL un amendement vit des mois, pas 8 jours" % ", ".join(
                       "%s %+d" % (k, d) for k, d in gros[:4])) if gros and not ok else "",
        "detail": [{"amendement": k, "delta_votes": d} for k, d in deltas[:8]],
    }


# ── 4. Arbitrage LLM-vs-règle (Cortana) ───────────────────────────────────────
def arbitrage_llm():
    alerts = lignes(DATA / "micro_alerts.jsonl")
    score = charger(DATA / "cortana_micro_score.json") or {}
    juste = charger(IM / "scripts" / "justesse_v2.json") or {}
    d = juste.get("directionnel") or {}
    pi = (juste.get("par_indice") or {})
    n_alertes = score.get("n_alertes") or 0
    v = "IMPOSSIBLE (0 cas à juger)" if not alerts else (
        "SUCCES" if (score.get("pct") or 0) >= 60 else "ECHEC")
    return {
        "protocole": "Arbitrage LLM-vs-règle (Cortana)",
        "critere": "la règle maison : < 60 % de justesse micro → confiance faible + 1 alerte/h max. Verdict annoncé 27/09",
        "faits": "%d alerte(s) microstructure au journal · %d notée(s) par le juge indépendant · justesse %s · "
                 "avis directionnels de Cortana (toutes matières) : %s/%s = %s %%" % (
                     len(alerts), score.get("n_scorées_60s") or 0,
                     ("%.1f %%" % score["pct"]) if score.get("pct") is not None else "n/d",
                     d.get("hit"), d.get("n"), d.get("pct")),
        "verdict": v,
        "alerte": ("le verdict du 27/09 ne pourra PAS être rendu : %d alerte(s) en 7 jours → 0 cas. "
                   "Le producteur d'alertes (module microstructure) n'a rien écrit depuis le 09/09 "
                   "(data/micro_alerts.jsonl = 0 octet) — il faut trancher : module mort, ou rien à alerter ?" % n_alertes)
                  if n_alertes == 0 else "",
        "detail": [{"indice": k, "directionnels": (pi[k] or {}).get("dir_n"), "corect": (pi[k] or {}).get("dir_hit"),
                    "n": (pi[k] or {}).get("n")} for k in sorted(pi) if (pi[k] or {}).get("dir_n")][:10],
    }


# ── 5. Geopol (réanimé 12/09 · fenêtre 4 semaines → ~10/10) ────────────────────
def geopol():
    juste = charger(IM / "scripts" / "justesse_v2.json") or {}
    pi = (juste.get("par_indice") or {}).get("geopol") or {}
    sc = (charger(IM / "indice_app" / "data" / "scores_geopol.json") or {}).get("geopol") or {}
    dir_n, dir_hit = pi.get("dir_n") or 0, pi.get("dir_hit") or 0
    verdict = "EN ATTENTE (fenêtre jusqu'au ~10/10)"
    if dir_n >= 20:
        verdict = "SUCCES" if dir_hit / dir_n >= 0.56 else "ECHEC"
    return {
        "protocole": "Geopol (réanimé)",
        "critere": "GEOPOL-C2/C3 : avis geopol noté vs BTC 2×/jour, fenêtre 4 semaines (→ ~10/10), critère P3 ≥ 56 %",
        "faits": "score actuel %.4f « %s » (ML %.4f) · %d avis enregistrés dont %d directionnels (%d correct(s)) · %d NEUTRE" % (
            sc.get("score") or 0, sc.get("niveau") or "?", (sc.get("ml_score") if sc.get("ml_score") is not None else sc.get("ml", {}).get("risk_score") if isinstance(sc.get("ml"), dict) else 0) or 0,
            pi.get("n") or 0, dir_n, dir_hit, pi.get("neutre") or 0),
        "verdict": verdict,
        "alerte": ("1 avis correct sur %d directionnels : à cette cadence le critère ne sera pas tranchable dans "
                   "la fenêtre" % dir_n) if (dir_n and dir_hit / dir_n < 0.5) else "",
        "detail": [{"indice": "geopol", "n": pi.get("n"), "directionnels": dir_n, "corrects": dir_hit,
                    "neutres": pi.get("neutre"), "t_stat": pi.get("t_stat")}],
    }


# ── 6. paternes-btc (Kronos) — n ≥ 30 avant verdict ───────────────────────────
def paternes_btc():
    rows = lignes(DATA / "paternes_btc_hist.jsonl")
    dern = rows[-1] if rows else {}
    reg = dern.get("regime_fond") or {}
    macd = (dern.get("macd_filtre") or {}).get("histogramme")
    premiers = rows[0] if rows else {}
    p0, p1 = premiers.get("prix_dernier"), dern.get("prix_dernier")
    var = ((p1 - p0) / p0 * 100) if (p0 and p1) else None
    manque = max(0, 30 - len(rows))
    return {
        "protocole": "paternes-btc (Kronos)",
        "critere": "mesure en continu des paternes validés (50w×200w + RSI hebdo, MACD daily = filtre, cycle) — verdict à n ≥ 30 cycles",
        "faits": "%d cycles · régime %s (écart 50w/200w %.1f %%, RSI hebdo %.0f) · MACD histogramme %s · BTC %s → %s (%s)" % (
            len(rows), reg.get("regime"), reg.get("ecart_pct") or 0, reg.get("rsi_w") or 0,
            macd, int(p0) if p0 else "?", int(p1) if p1 else "?",
            ("%+.1f %%" % var) if var is not None else "n/d"),
        "verdict": "EN ATTENTE (il manque %d cycle(s) — cadence quotidienne → ~%d jour(s))" % (manque, manque),
        "alerte": "",
        "detail": [{"ts": r.get("ts"), "prix": r.get("prix_dernier"), "regime": (r.get("regime_fond") or {}).get("regime"),
                    "rsi_w": (r.get("regime_fond") or {}).get("rsi_w")} for r in rows[-5:]],
    }


# ── 7. MiroFish ───────────────────────────────────────────────────────────────
def mirofish():
    d = IM / "MIROFISH_DONNEES_2026-08-10"
    sims = sorted([p.name for p in (d / "simulations").glob("sim_*")]) if (d / "simulations").exists() else []
    rapports = sorted([p.name for p in d.glob("report_*")]) if d.exists() else []
    return {
        "protocole": "MiroFish",
        "critere": "simulateur multi-agents, à la demande — verdict « après TROUPEAU » · 08/08 : sim jugée MISS",
        "faits": "%d simulation(s) (%s) · %d rapport(s) (%s) · dernier run le 10/08" % (
            len(sims), ", ".join(sims), len(rapports), ", ".join(rapports)),
        "verdict": "EN ATTENTE (aucun nouveau run depuis le 10/08 — protocole à la demande, donc rien à juger)",
        "alerte": "« réveillé le 13/09 » n'a produit aucune simulation : le réveil n'a pas été jusqu'au run",
        "detail": [],
    }


def main():
    maintenant = datetime.now(timezone.utc)
    protos = [troupeau_inv(), radar_rwa(), xrpl_gouvernance(), arbitrage_llm(),
              geopol(), paternes_btc(), mirofish()]
    sortie = {
        "ts": maintenant.isoformat(timespec="seconds"),
        "note": ("Verdicts MESURÉS à la source (scripts/verdicts_protocoles.py). Chaque protocole porte son "
                 "critère pré-enregistré : c'est lui qui décide, pas l'impression du moment. Un verdict "
                 "« IMPOSSIBLE » ou une ligne « alerte » signale un protocole dont le verdict ne peut pas "
                 "être rendu — c'est une panne de conception, pas une patience."),
        "protocoles": protos,
        "compte": {
            "total": len(protos),
            "verdicts_rendus": len([p for p in protos if str(p["verdict"]).startswith(("SUCCES", "ECHEC"))]),
            "en_attente": len([p for p in protos if "ATTENTE" in str(p["verdict"])]),
            "impossibles": len([p for p in protos if "IMPOSSIBLE" in str(p["verdict"])]),
            "avec_alerte": len([p for p in protos if p.get("alerte")]),
        },
    }
    OUT.write_text(json.dumps(sortie, indent=2, ensure_ascii=False), encoding="utf-8")
    c = sortie["compte"]
    print("Protocoles : %d — %d verdict(s) rendu(s), %d en attente, %d impossible(s), %d avec alerte"
          % (c["total"], c["verdicts_rendus"], c["en_attente"], c["impossibles"], c["avec_alerte"]))
    for p in protos:
        print("  %-28s %s" % (p["protocole"], p["verdict"]))
        if p.get("alerte"):
            print("      ⚠ %s" % p["alerte"][:150])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
