#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ORACLE INDÉPENDANT — classe E11 (GO 1, ordre Christophe 23/09/2026)
===================================================================
CE QU'IL FERME
--------------
E11 = « confondre COHÉRENCE et JUSTESSE » : mes gardiens précédents comparaient le moteur
À LUI-MÊME (seuil recalculé vs seuil écrit, journal vs journal). Si la RÈGLE du moteur est
fausse, mes instruments la valident et nous nous trompons ensemble.

Ici : la source est **externe et brute** — les bougies 1 minute de MEXC. Aucune ligne de code
du moteur n'est appelée, aucun de ses indicateurs n'est relu : l'oracle ne connaît que
(heure, prix, quantité) et le MARCHÉ. Il peut donc dire « le moteur a acheté malgré le marché »
et « le stop annoncé n'a pas été tenu », ce que mes autres contrôles ne pouvaient pas dire.

CE QU'IL MESURE PAR TRADE (tout depuis les bougies brutes)
----------------------------------------------------------
  A. ENTRÉE — la baisse annoncée existait-elle ? Recalcule la chute depuis le plus haut des
     6 et 15 minutes QUI PRÉCÈDENT l'achat, sur les HAUTS bruts.
     Verdict : entrée APRÈS une baisse (le motif est là) ou entrée SANS baisse (le moteur a
     « acheté en haut » — ce qui, sur une stratégie de creux, est une faute de motif).
  B. CHEMIN APRÈS L'ACHAT — meilleur et pire point (MFE/MAE) atteints avant la sortie, en %.
  C. LE STOP RÉEL A-T-IL TENU ? Le NOMINAL est **lu dans le motif de sortie du moteur**
     (« stop-39.23%_guard_partial_50 »), jamais deviné ni pris dans un fichier de config.
     Puis : première minute où le plus bas brut touche ce niveau → RETARD en minutes et
     COÛT en dollars (quantité réelle × (prix du niveau − prix de sortie réel)).
     ⚠ CORRECTION DU 23/09 (classe E17) : la version précédente de cet oracle testait des
     niveaux choisis par MOI (−4/−8 %) ; elle a produit un faux verdict (« le stop ne tient
     pas ») parce que RIZE n'a pas un stop à 8 % : son PLANCHER de config est 8 %, mais son
     stop RÉEL était 16,51 % puis 39,23 %, écrit dans ses propres sorties. Le plancher de
     config n'est pas le seuil de la machine — confondre les deux, c'est E10/E2.
  D. SORTIE — ce que le marché a fait dans les 60 minutes APRÈS la vente : plus bas (bien
     vendu) ou plus haut (vendu trop tôt, montant laissé).
  E. PnL indépendant : quantité réelle × (prix de sortie − prix d'entrée), puis net estimé
     (frais 5 bps/côté ESTIMÉS + spread déclaré dans le motif de vente s'il y en a un).

CE QU'IL NE FAIT PAS (déclaré, R8)
----------------------------------
- Il ne connaît pas la profondeur du carnet AU MOMENT du trade (elle n'est pas historisée) :
  le coût du retard est donc un coût sur le prix, pas une exécution simulée au carnet.
- Il ne rejuge pas la taille (elle dépend d'une profondeur passée non historisée).
- « Le motif est là » ne veut pas dire « le motif est rentable » : c'est un jugement de
  PROCESSUS, pas de résultat.
- Les frais sont ESTIMÉS (un paper ne paie rien).

Lecture seule : aucune écriture moteur, aucun ordre, 0 €. Klines mises en cache sur disque
(`runs/ORACLE_KL_*.json`) pour que le calcul soit rejouable à l'identique.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent          # hulk-mexc/
RUNS = RACINE / "runs"
FRAIS_BPS_COTE = 5.0          # ESTIMÉ (déclaré) : ce que paierait un ordre réel
# Plus de niveaux « choisis par l'agent » : le niveau testé est celui que la MACHINE écrit
# (voir nominal_du_moteur). Conservé vide pour que toute référence oubliée échoue visiblement.
NIVEAUX_STOP: list[float] = []
API = "https://api.mexc.com/api/v3/klines"


# ─────────────────────────────────────────────────────────────── utilitaires

def ts_ms(iso: str) -> int:
    return int(datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp() * 1000)


def iso(ms) -> str:
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def klines(pair: str, de_ms: int, a_ms: int, refresh: bool) -> list[list]:
    """Bougies 1 m brutes MEXC, en cache disque. Aucune donnée du moteur n'entre ici."""
    cache = RUNS / f"ORACLE_KL_{pair}_{de_ms // 1000}_{a_ms // 1000}.json"
    if cache.exists() and not refresh:
        try:
            return json.loads(cache.read_text(encoding="utf-8"))
        except Exception:
            pass
    out, curseur, essais = [], int(de_ms), 0
    while curseur < a_ms and essais < 40:
        url = f"{API}?symbol={pair}&interval=1m&startTime={curseur}&endTime={a_ms}&limit=1000"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hulk-oracle/1.0"})
            with urllib.request.urlopen(req, timeout=20) as r:
                lot = json.loads(r.read().decode())
        except Exception as e:                                    # noqa: BLE001
            print(f"   [!] {pair} klines: {str(e)[:80]} — pause 2 s", file=sys.stderr)
            time.sleep(2)
            essais += 1
            continue
        if not lot:
            break
        out.extend(lot)
        dernier = int(lot[-1][0])
        if dernier <= curseur:
            break
        curseur = dernier + 60_000
        time.sleep(0.25)                                          # courtoisie API
    out.sort(key=lambda k: int(k[0]))
    try:
        cache.write_text(json.dumps(out), encoding="utf-8")
    except Exception:
        pass
    return out


def lire_sequences(depuis: str) -> dict:
    """Reconstruit les séquences depuis le journal du moteur (le plus récent, qui contient
    l'historique recopié). Une séquence = un BUY puis ses sorties (qty remise à 0)."""
    p = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda x: x.stat().st_mtime)[-1]
    par_paire: dict[str, list] = {}
    for r in csv.reader(p.open(newline="", encoding="utf-8", errors="replace")):
        if len(r) < 11 or r[0] == "ts" or r[0] < depuis:
            continue
        if r[2] not in ("BUY", "SELL", "SELL_PARTIAL", "STOP"):
            continue
        par_paire.setdefault(r[1], []).append({
            "ts": r[0], "event": r[2], "price": float(r[4] or 0),
            "entry": float(r[5] or 0) if r[5] else None,
            "qty": float(r[6] or 0), "pnl": float(r[7] or 0),
            "pnl_total": float(r[8] or 0), "regime": r[3], "reason": r[10],
            "ts_prix": r[11] if len(r) > 11 else "",
        })
    seqs = {}
    for paire, evs in par_paire.items():
        cur = None
        for e in evs:
            if e["event"] == "BUY":
                if cur:
                    seqs.setdefault(paire, []).append(cur)
                cur = {"paire": paire, "buy": e, "sorties": []}
            elif cur is not None:
                cur["sorties"].append(e)
        if cur:
            seqs.setdefault(paire, []).append(cur)
    return {k: [s for s in v if s["sorties"]] for k, v in seqs.items()}


# ─────────────────────────────────────────────────────────────── jugements

def fenetre(kl: list[list], de_ms: int, a_ms: int) -> list[list]:
    return [k for k in kl if de_ms <= int(k[0]) < a_ms]


def juger_entree(kl, t_buy: int, prix: float) -> dict:
    """Chute depuis le plus haut des 6 / 15 minutes précédentes — sur les HAUTS bruts."""
    res = {}
    for mins in (6, 15):
        w = fenetre(kl, t_buy - mins * 60_000, t_buy)
        if not w:
            res[f"haut_{mins}m"] = None
            res[f"chute_{mins}m_pct"] = None
            continue
        haut = max(float(k[2]) for k in w)
        res[f"haut_{mins}m"] = haut
        res[f"chute_{mins}m_pct"] = round((haut - prix) / haut * 100, 3) if haut else None
    c15 = res.get("chute_15m_pct")
    if c15 is None:
        res["verdict_entree"] = "INDÉTERMINÉ (pas de bougies avant l'achat)"
    elif c15 >= 2.0:
        res["verdict_entree"] = f"APRÈS BAISSE ({c15:.2f}% sous le haut des 15 min) — motif présent"
    elif c15 >= 0.5:
        res["verdict_entree"] = f"baisse FAIBLE ({c15:.2f}%) — motif marginal"
    else:
        res["verdict_entree"] = f"SANS BAISSE ({c15:+.2f}%) — acheté au plus haut des 15 min"
    return res


def nominal_du_moteur(sorties: list[dict]) -> tuple[float | None, str]:
    """LE NIVEAU RÉEL DU STOP = celui que le MOTEUR ÉCRIT lui-même dans sa sortie
    (« stop-39.23%_guard_partial_50 »).

    ⚠ FAUTE CORRIGÉE ICI LE 23/09 (classe E17) : j'ai publié « stop annoncé 8 % pour RIZE »
    en lisant `universe_profils.json → RIZEUSDT.calib.stop_pct = 8.0` — un PLANCHER de config —
    alors que le moteur appliquait **16,51 %** (10/09) puis **39,23 %** (22/09), écrit noir sur
    blanc dans ses propres motifs de sortie. Publier un plancher comme le seuil réel de la
    machine, c'est E10/E2 une fois de plus : le chiffre existe, il est lisible à la source, et
    je ne l'ai pas lu. Le plancher n'est utilisé ici QUE si aucun motif ne porte de niveau, et
    dans ce cas c'est DÉCLARÉ.
    """
    for o in sorties:
        m = re.search(r"stop-([0-9.]+)%", o.get("reason", ""))
        if m:
            return float(m.group(1)), "lu dans le motif de sortie du moteur"
    m = re.search(r"stop[-_]([0-9.]+)%", " ".join(o.get("reason", "") for o in sorties))
    if m:
        return float(m.group(1)), "lu dans le motif (variante)"
    return None, "aucun niveau écrit par le moteur dans ce trade"


def juger_stop(kl, t_buy: int, t_sortie: int, prix_entree: float, qty: float,
               prix_sortie: float | None, nominal_pct: float | None, source_nominal: str) -> dict:
    """Le stop RÉEL du moteur a-t-il TENU ?
    On ne teste plus des niveaux choisis par moi (−4/−8 %) : on teste **le niveau que la
    machine a elle-même annoncé**, et on mesure le retard entre le moment où le MARCHÉ a touché
    ce niveau (plus-bas brut) et le moment où la machine est réellement sortie."""
    chemin = fenetre(kl, t_buy, t_sortie)
    out = {"minutes_tenues": round((t_sortie - t_buy) / 60_000, 1),
           "nominal_pct": nominal_pct, "source_nominal": source_nominal}
    if not chemin:
        out["note"] = "aucune bougie entre l'achat et la sortie (marché fermé/absence)"
        return out
    mfe = max(float(k[2]) for k in chemin)
    mae = min(float(k[3]) for k in chemin)
    out["mfe_pct"] = round((mfe - prix_entree) / prix_entree * 100, 2)
    out["mae_pct"] = round((mae - prix_entree) / prix_entree * 100, 2)
    if nominal_pct is None:
        out["verdict_stop"] = "INDÉTERMINÉ — le moteur n'a écrit aucun niveau de stop sur ce trade"
        return out
    seuil = prix_entree * (1 - nominal_pct / 100)
    touche = next((k for k in chemin if float(k[3]) <= seuil), None)
    if touche is None:
        out["touche"] = False
        out["verdict_stop"] = (f"NON DÉCLENCHÉ — le marché n'a jamais atteint −{nominal_pct:.2f} % "
                               f"(pire point : {out['mae_pct']:.2f} %)")
        return out
    t_touche = int(touche[0])
    retard = round((t_sortie - t_touche) / 60_000, 1)
    prix_trigger = seuil
    # COÛT DU RETARD = ce que la position a perdu EN PLUS entre le niveau touché par le marché et
    # la sortie réelle. On le mesure sur le PRIX DE SORTIE réel (pas sur la bougie de contact) :
    # c'est ce que le compte a payé. Prix de sortie manquant → coût NON CALCULÉ (jamais 0).
    cout = None
    if prix_sortie:
        cout = round(max(0.0, prix_trigger - prix_sortie) * qty, 4)
    out.update({
        "touche": True, "touche_a": iso(t_touche), "retard_min": retard,
        "prix_trigger": round(prix_trigger, 10), "cout_retard_usdt": cout,
        "cout_retard_pct_du_notional": (round((prix_trigger - prix_sortie)
                                             / (prix_entree * 100 / 100) * 100, 3)
                                        if prix_sortie else None),
    })
    out["verdict_stop"] = ("TENU (la machine sort dans la minute du contact)" if retard <= 2 else
                           f"EN RETARD de {retard:.1f} min après le contact du niveau"
                           + (f" · coût {cout:+.2f} $" if cout is not None else
                              " · coût NON CALCULÉ (prix de sortie absent)"))
    return out


def juger_sortie(kl, t_sortie: int, prix_sortie: float) -> dict:
    """Ce que le marché a fait dans les 60 minutes APRÈS la vente."""
    apres = fenetre(kl, t_sortie, t_sortie + 60 * 60_000)
    if not apres:
        return {"verdict_sortie": "INDÉTERMINÉ (pas de bougies après la vente)"}
    plus_bas = min(float(k[3]) for k in apres)
    plus_haut = max(float(k[2]) for k in apres)
    b = round((plus_bas - prix_sortie) / prix_sortie * 100, 2)
    h = round((plus_haut - prix_sortie) / prix_sortie * 100, 2)
    if b <= -1.0 and b <= h * -1:
        v = f"BIEN VENDU (le marché est descendu {b:.2f}% après)"
    elif h >= 1.0:
        v = f"VENDU TÔT (le marché est monté +{h:.2f}% après)"
    else:
        v = f"NEUTRE (marché plat : {b:+.2f}% / {h:+.2f}%)"
    return {"verdict_sortie": v, "apres_bas_pct": b, "apres_haut_pct": h}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=float, default=10.0, help="fenêtre en jours (défaut 10)")
    ap.add_argument("--refresh", action="store_true", help="recharger les klines depuis MEXC")
    ap.add_argument("--json", default=None)
    ap.add_argument("--txt", default=None)
    a = ap.parse_args()

    # Fenêtre arrondie à MINUIT UTC : autrement la clé du cache change à chaque minute et
    # l'oracle re-télécharge 16 000 bougies par paire pour rien (coût mesuré : ~6 min).
    # Un oracle qui n'est pas rejouable à l'identique ne peut pas être contesté (E10).
    _base = datetime.now(timezone.utc) - timedelta(days=a.jours)
    depuis = _base.replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
    seqs = lire_sequences(depuis)
    n_seq = sum(len(v) for v in seqs.values())
    print(f"ORACLE INDÉPENDANT — fenêtre {a.jours:g} j (depuis {depuis})")
    print(f"  séquences reconstruites depuis le journal : {n_seq} sur {len(seqs)} paires")
    print(f"  source de vérité : bougies 1 min MEXC (brutes). Aucun indicateur du moteur relu.\n")

    resultats, agregats = [], {"entrees": {}, "stops": {}, "sorties": {}, "pnl": {}}
    for paire in sorted(seqs):
        # fenêtre de klines : 60 min avant le 1er achat → 6 h après la dernière sortie
        ts = [ts_ms(s["buy"]["ts"]) for s in seqs[paire]] + \
             [ts_ms(o["ts"]) for s in seqs[paire] for o in s["sorties"]]
        de, fin = min(ts) - 60 * 60_000, max(ts) + 6 * 3600_000
        kl = klines(paire, de, fin, a.refresh)
        print(f"  {paire:12} {len(kl)} bougies 1m · {len(seqs[paire])} séquence(s)")
        for s in seqs[paire]:
            b, sorties = s["buy"], s["sorties"]
            t_buy, p_buy = ts_ms(b["ts"]), b["price"]
            qty_tot = sum(o["qty"] for o in sorties)
            # prix de sortie moyen pondéré par la quantité (les sorties peuvent être partielles)
            p_sortie = (sum(o["price"] * o["qty"] for o in sorties) / qty_tot) if qty_tot else None
            t_der = ts_ms(sorties[-1]["ts"])
            pnl_brut = sum(o["pnl"] for o in sorties)
            spread_bps = 0.0
            for o in sorties:
                for mot in o["reason"].split():
                    if mot.startswith("spread="):
                        try:
                            spread_bps = float(mot.split("=")[1].replace("bps", ""))
                        except Exception:
                            pass
            couts = (qty_tot * ((p_buy + (p_sortie or p_buy)) / 2)
                     * (2 * FRAIS_BPS_COTE + spread_bps) / 10000.0) if qty_tot else 0.0
            _nom = nominal_du_moteur(sorties)
            res = {
                "paire": paire, "achat": b["ts"], "prix_entree": p_buy, "qty": round(qty_tot, 6),
                "regime": b["regime"], "motif_achat": b["reason"][:80],
                "sortie": sorties[-1]["ts"], "prix_sortie": p_sortie,
                "motif_sortie": sorties[-1]["reason"][:80], "n_sorties": len(sorties),
                "pnl_brut_journal": round(pnl_brut, 4),
                "pnl_brut_oracle": round(qty_tot * ((p_sortie or p_buy) - p_buy), 4),
                "spread_declare_bps": spread_bps, "couts_estimes_usdt": round(couts, 4),
                "pnl_net_estime": round(pnl_brut - couts, 4),
                "entree": juger_entree(kl, t_buy, p_buy),
                "stop": juger_stop(kl, t_buy, t_der, p_buy, qty_tot, p_sortie,
                                   *_nom),
                "apres_sortie": juger_sortie(kl, t_der, p_sortie or p_buy),
            }
            resultats.append(res)

    # ── agrégats (ce que la famille va exiger)
    def cle(d, motif):
        for k in d:
            if k.startswith(motif):
                return k
        return None

    for r in resultats:
        ve = r["entree"].get("verdict_entree", "")
        cat = ("après baisse" if ve.startswith("APRÈS BAISSE") else
               "baisse faible" if ve.startswith("baisse FAIBLE") else
               "sans baisse" if ve.startswith("SANS BAISSE") else "indéterminé")
        agregats["entrees"][cat] = agregats["entrees"].get(cat, 0) + 1
        vs = r["apres_sortie"].get("verdict_sortie", "")
        cat_s = ("bien vendu" if vs.startswith("BIEN VENDU") else
                 "vendu tôt" if vs.startswith("VENDU TÔT") else "neutre/indéterminé")
        agregats["sorties"][cat_s] = agregats["sorties"].get(cat_s, 0) + 1
        # ── le stop RÉEL de la machine (niveau qu'elle écrit elle-même)
        st = r["stop"]
        nom = st.get("nominal_pct")
        cat_stop = ("indéterminé (aucun niveau écrit)" if nom is None else
                    "niveau jamais atteint par le marché" if not st.get("touche") else
                    "tenu (≤ 2 min)" if (st.get("retard_min") or 0) <= 2 else "EN RETARD")
        # NB : ne JAMAIS réutiliser `a` ici — c'est le namespace argparse (leçon payée :
        # « 'dict' object has no attribute 'jours' »).
        acc = agregats["stops"].setdefault(cat_stop, {"n": 0, "retard_max": 0.0,
                                                     "retard_med": [], "cout_total": 0.0})
        acc["n"] += 1
        if st.get("touche") and (st.get("retard_min") or 0) > 2:
            acc["retard_max"] = max(acc["retard_max"], st["retard_min"])
            acc["retard_med"].append(st["retard_min"])
        if st.get("cout_retard_usdt"):
            acc["cout_total"] = round(acc["cout_total"] + st["cout_retard_usdt"], 4)
        # niveau nominal par paire (ce que la machine se donne comme protection)
        if nom is not None:
            agregats["stops"].setdefault("_nominal_par_paire", {}).setdefault(r["paire"], []).append(nom)

    agg_pnl = {
        "n_sequences": len(resultats),
        "brut_journal": round(sum(r["pnl_brut_journal"] for r in resultats), 4),
        "brut_oracle": round(sum(r["pnl_brut_oracle"] for r in resultats), 4),
        "couts_estimes": round(sum(r["couts_estimes_usdt"] for r in resultats), 4),
        "net_estime": round(sum(r["pnl_net_estime"] for r in resultats), 4),
    }
    agregats["pnl"] = agg_pnl

    # ── affichage
    L = []
    L.append(f"ORACLE INDÉPENDANT — {a.jours:g} derniers jours · {len(resultats)} séquences "
             f"· {len(seqs)} paires · bougies 1 min MEXC (source externe, brute)")
    L.append("")
    L.append("=== A. LE MOTIF D'ENTRÉE EXISTAIT-IL DANS LE MARCHÉ ? (recalculé sur les hauts bruts)")
    tot_e = sum(agregats["entrees"].values()) or 1
    for k, v in sorted(agregats["entrees"].items(), key=lambda t: -t[1]):
        L.append(f"  {k:14} : {v:3} / {tot_e}  ({v / tot_e * 100:5.1f} %)")
    L.append("")
    L.append("=== B. LE STOP **RÉEL** DE LA MACHINE A-T-IL TENU ? "
             "(niveau LU dans ses propres motifs de sortie, jamais deviné)")
    nominal = agregats["stops"].get("_nominal_par_paire") or {}
    if nominal:
        L.append("  niveau que la machine se donne (médiane, lu dans ses sorties) :")
        for p in sorted(nominal, key=lambda x: -(sorted(nominal[x])[len(nominal[x]) // 2])):
            v = sorted(nominal[p])
            L.append(f"    {p:12} : {v[len(v) // 2]:6.2f} %")
    for k, v in agregats["stops"].items():
        if k.startswith("_"):
            continue
        med = (sorted(v["retard_med"])[len(v["retard_med"]) // 2] if v["retard_med"] else None)
        L.append(f"  {k:30} : {v['n']:3} trade(s)"
                 + (f" · retard médian {med:6.1f} min · max {v['retard_max']:6.1f} min"
                    if med is not None else "")
                 + (f" · COÛT du retard {v['cout_total']:+.2f} $" if v["cout_total"] else ""))
    L.append("")
    L.append("=== C. LES SORTIES (marché dans les 60 min après la vente)")
    tot_s = sum(agregats["sorties"].values()) or 1
    for k, v in sorted(agregats["sorties"].items(), key=lambda t: -t[1]):
        L.append(f"  {k:16} : {v:3} / {tot_s}  ({v / tot_s * 100:5.1f} %)")
    L.append("")
    L.append("=== D. LE PnL, RECALCULÉ PAR L'ORACLE (≠ ce que le moteur inscrit)")
    L.append(f"  brut inscrit par le moteur : {agg_pnl['brut_journal']:+8.2f} $")
    L.append(f"  brut recalculé (qty × écart) : {agg_pnl['brut_oracle']:+8.2f} $  "
             f"→ écart {agg_pnl['brut_oracle'] - agg_pnl['brut_journal']:+.4f} $")
    L.append(f"  coûts ESTIMÉS (frais 5 bps/côté + spread déclaré) : {agg_pnl['couts_estimes']:.2f} $")
    L.append(f"  NET estimé : {agg_pnl['net_estime']:+8.2f} $")
    L.append("")
    L.append("=== E. LES TRADES LES PLUS INSTRUCTIFS (5 pires entrées, 5 pires stops)")
    def pire_entree(r):
        return r["entree"].get("chute_15m_pct") if r["entree"].get("chute_15m_pct") is not None else 99
    for r in sorted(resultats, key=pire_entree)[:5]:
        L.append(f"  {r['paire']:12} {r['achat']}  entrée : {r['entree']['verdict_entree']}"
                 f"  · MFE/MAE {r['stop'].get('mfe_pct')}%/{r['stop'].get('mae_pct')}%"
                 f"  · pnl brut {r['pnl_brut_journal']:+.2f} $")
    for r in sorted(resultats, key=lambda x: (x["stop"].get("mae_pct") or 0))[:5]:
        st = r["stop"]
        det = (f"stop −{st.get('nominal_pct'):.2f} % (écrit par la machine) touché {st.get('touche_a')} "
               f"· sortie {r['sortie']} · {st.get('verdict_stop')}") if st.get("touche") else \
              f"stop −{st.get('nominal_pct')} % : {st.get('verdict_stop')}"
        L.append(f"  {r['paire']:12} MAE {st.get('mae_pct')}% · {det}")

    texte = "\n".join(L)
    print("\n" + texte)
    if a.txt:
        Path(a.txt).write_text(texte + "\n", encoding="utf-8")
    if a.json:
        Path(a.json).write_text(json.dumps({
            "instrument": "oracle_independant.py",
            "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "fenetre_jours": a.jours, "depuis": depuis, "source": "klines 1m MEXC (brutes)",
            "frais_bps_cote_estimes": FRAIS_BPS_COTE,
            "niveau_de_stop": "LU dans le motif de sortie du moteur (jamais deviné)",
            "n_sequences": len(resultats), "agregats": agregats, "sequences": resultats,
            "limites_declarees": [
                "Profondeur de carnet non historisée : le coût du retard est un coût de PRIX, "
                "pas une exécution simulée au carnet.",
                "Les frais sont ESTIMÉS (un paper ne paie rien) ; les spreads viennent du motif "
                "de vente quand il en déclare un, sinon 0.",
                "« motif présent » = jugement de PROCESSUS, pas de rentabilité.",
                "Aucun indicateur du moteur n'est relu : l'oracle ne peut pas dire si le moteur "
                "a bien calculé, seulement si le MARCHÉ lui donnait raison.",
            ],
            "lecture_seule": True, "ordres": 0,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
