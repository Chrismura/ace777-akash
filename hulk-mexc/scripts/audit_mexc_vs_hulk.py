#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_mexc_vs_hulk.py — GO 1 : MEXC live vs données Hulk, PAIRE PAR PAIRE
========================================================================

DEMANDE CHRISTOPHE (23/09/2026) : « tu vas prendre les données de MEXC, tu vas les
comparer une par une avec les données paires de Hulk […] vérifier les données qu'on
mémorise, si il en manque, si elles sont correctement enregistrées. »

CE QU'ON COMPARE (et avec QUELLE définition — c'est le cœur du sujet)
--------------------------------------------------------------------
  Source Hulk (lue dans le CODE, pas dans un document) :
    * prix          ← `scripts/paper_diprip.py::fetch_all_prices`     → api.mexc.com /ticker/price
    * spread + mur  ← `scripts/ace_sense_mexc.py::book_sense`         → api.mexc.com /depth?limit=20
        · spread_bps  = (best_ask − best_bid) / mid × 10 000
        · wall_bid_usdt = **MAX du notionnel (prix × qté) des 20 premiers bids**
          ⚠ ce n'est PAS la profondeur cumulée : c'est UN ordre. Confondre les deux est
          l'erreur qui a produit « RIZE = 801 k$ de mur » face à un carnet réel de ~600 $.
        · alimenté par `scripts/satellite_aspiration.py` dans `runs/aspiration_live.json`
          (MAX_PAIRS = 5 par passe + paires FORCE_PROBE → tout le monde n'a PAS de vue live)
    * profils       ← `strategie/universe_profils.json` (mur_bid_med, spread_bps_med, prix…)

  Source MEXC (rejouée ici, mêmes endpoints, mêmes formules, même instant).

CE QUE L'INSTRUMENT MESURE, PAIRE PAR PAIRE
-------------------------------------------
  1. COUVERTURE  : la paire a-t-elle une vue live dans aspiration_live.json, et de quand date-t-elle ?
  2. PRIX        : Hulk vs MEXC (Δ bps) + l'ÂGE de la vue Hulk (une comparaison sans âge ne prouve rien)
  3. SPREAD      : Hulk vs MEXC (Δ bps) — mesuré, jamais supposé
  4. MUR         : Hulk (max niveau) vs MEXC (max niveau, même définition) **et** la
                   profondeur cumulée sous −0,5 / −1 / −2 % (l'autre grandeur, à ne pas confondre)
  5. PROFIL      : le `prix` et le `mur_bid_med` du profil sont-ils encore vrais ? (dérive, n_mesures)

LECTURE SEULE : aucune écriture moteur, 0 ordre, 0 €. Sorties : runs/AUDIT_MEXC_VS_HULK_*.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]          # hulk-mexc/
RUNS = RACINE / "runs"
STATE_GLOB = "PAPER_V1_*_state.json"
ASPIRATION = RUNS / "aspiration_live.json"
PROFILS = RACINE / "strategie" / "universe_profils.json"
TAG = datetime.now(timezone.utc).strftime("%Y%m%d")
SORTIE_JSON = RUNS / f"AUDIT_MEXC_VS_HULK_{TAG}.json"
SORTIE_TXT = RUNS / f"AUDIT_MEXC_VS_HULK_{TAG}.txt"

UA = {"User-Agent": "hulk-audit/1.0"}
PAUSE = 0.12          # politesse rate-limit MEXC


def http_json(url: str, timeout: float = 15.0, retries: int = 3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:                       # noqa: BLE001 — on veut TOUT capturer
            last = e
            time.sleep(0.6 * (i + 1))
    raise RuntimeError(f"HTTP KO {url} : {last}")


def derniers_state() -> dict:
    f = sorted(RUNS.glob(STATE_GLOB))[-1]
    return json.loads(f.read_text(encoding="utf-8"))


def profils() -> dict[str, dict]:
    d = json.loads(PROFILS.read_text(encoding="utf-8"))
    meta = {"version", "updated", "note", "_note", "commentaire"}
    return {k: v for k, v in d.items() if k not in meta and isinstance(v, dict)}


def _f(x, d=0.0) -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def book_mesure(pair: str, limit: int = 20) -> dict:
    """Rejoue EXACTEMENT les formules de ace_sense_mexc.book_sense + la profondeur cumulée.

    ⚠ Les deux grandeurs sont nommées séparément À DESSEIN : `mur_max_niveau_usdt`
    (ce que le moteur appelle « mur ») et `profondeur_cumul_usdt` (ce qu'un desk
    appellerait la profondeur). Les confondre invalide toute conclusion de taille.
    """
    q = urllib.parse.urlencode({"symbol": pair, "limit": limit})
    j = http_json(f"https://api.mexc.com/api/v3/depth?{q}")
    bids = [(_f(p), _f(v)) for p, v in (j.get("bids") or [])]
    asks = [(_f(p), _f(v)) for p, v in (j.get("asks") or [])]
    out = {"quote_ts_ms": j.get("timestamp"), "n_bids": len(bids), "n_asks": len(asks)}
    if not bids or not asks:
        return {**out, "ok": False, "raison": "carnet vide (paire absente du spot MEXC ?)"}
    best_bid, best_ask = bids[0][0], asks[0][0]
    mid = (best_bid + best_ask) / 2.0
    out.update({
        "ok": True, "best_bid": best_bid, "best_ask": best_ask, "mid": mid,
        "spread_bps": round((best_ask - best_bid) / mid * 10000.0, 2) if mid > 0 else 9999.0,
        # définition MOTEUR : plus gros niveau unitaire des 20 premiers
        "mur_max_niveau_bid_usdt": round(max((p * v for p, v in bids), default=0.0), 2),
        "mur_max_niveau_ask_usdt": round(max((p * v for p, v in asks), default=0.0), 2),
        "mur_max_niveau_bid_prix": round(max(bids, key=lambda x: x[0] * x[1])[0], 10),
    })
    # profondeur cumulée sous −0,5 / −1 / −2 % du mid (l'autre grandeur, mesurée)
    for pct in (0.5, 1.0, 2.0):
        seuil = mid * (1 - pct / 100.0)
        cum = sum(p * v for p, v in bids if p >= seuil)
        out[f"profondeur_cumul_sous_{pct}pct_usdt"] = round(cum, 2)
    return out


def main() -> int:
    st = derniers_state()
    paires = list(st.get("pairs") or [])
    positions = st.get("positions") or {}
    prof = profils()
    asp = json.loads(ASPIRATION.read_text(encoding="utf-8")) if ASPIRATION.exists() else {}
    asp_p = asp.get("paires") or {}
    asp_ts = asp.get("ts_utc")
    age_asp = None
    if asp.get("ts"):
        age_asp = round(time.time() - _f(asp.get("ts")), 1)

    print("=== AUDIT MEXC vs HULK — PAIRE PAR PAIRE ===")
    print(f"paires moteur : {len(paires)} · avec profil : {len(prof)} · vue live aspiration : {len(asp_p)}"
          f" · âge de la vue d'ensemble : {age_asp} s ({asp_ts})")
    print()

    # 1) prix MEXC pour tout le monde en un appel (comme le moteur)
    tous_prix = {}
    try:
        for r in http_json("https://api.mexc.com/api/v3/ticker/price"):
            tous_prix[r["symbol"]] = _f(r.get("price"))
        print(f"prix MEXC récupérés : {len(tous_prix)} symboles")
    except Exception as e:                           # noqa: BLE001
        print(f"⚠ /ticker/price KO : {e}")
    print()

    lignes, anomalies, trous = [], [], []
    for pair in paires:
        a = asp_p.get(pair) or {}
        p = prof.get(pair) or {}
        pos = positions.get(pair) or {}
        row = {
            "pair": pair,
            "vue_live": (a.get("regime") or "AUCUNE") if a else "AUCUNE",
            "vue_live_age_s": age_asp if a else None,
            "hulk_prix_feed": _f(a.get("prix")) or None,
            "hulk_spread_bps": a.get("spread_bps") if a else None,
            "hulk_mur_bid_usdt": a.get("wall_bid_usdt") if a else None,
            "profil_prix": _f(p.get("prix")) or None,
            "profil_mur_bid_med": _f(p.get("mur_bid_med")) or None,
            "profil_spread_bps_med": _f(p.get("spread_bps_med")) or None,
            "profil_n_mesures": p.get("n_mesures"),
            "en_position": bool(pos),
            "position_entree": _f(pos.get("entry")) or None,
        }
        # --- MEXC live (mêmes formules que le moteur) ---
        try:
            row["mexc_prix"] = tous_prix.get(pair)
            time.sleep(PAUSE)
            b = book_mesure(pair)
            row["mexc_carnet"] = b
            if b.get("ok"):
                row["ecart_prix_feed_vs_mexc_bps"] = (
                    round((row["hulk_prix_feed"] - b["mid"]) / b["mid"] * 10000.0, 1)
                    if row.get("hulk_prix_feed") else None)
                row["ecart_spread_bps"] = (
                    round(_f(row["hulk_spread_bps"]) - b["spread_bps"], 2)
                    if row.get("hulk_spread_bps") is not None else None)
                row["ecart_mur_pct"] = (
                    round((_f(row["hulk_mur_bid_usdt"]) - b["mur_max_niveau_bid_usdt"])
                          / b["mur_max_niveau_bid_usdt"] * 100.0, 1)
                    if row.get("hulk_mur_bid_usdt") and b["mur_max_niveau_bid_usdt"] > 0 else None)
                row["ecart_profil_prix_pct"] = (
                    round((row["profil_prix"] - b["mid"]) / b["mid"] * 100.0, 2)
                    if row.get("profil_prix") else None)
                # le rapport qui a fait dire « mur de 801 k$ » : max niveau vs profondeur cumulée
                prof05 = b.get("profondeur_cumul_sous_0.5pct_usdt") or 0.0
                row["mur_sur_profondeur_0.5pct"] = (
                    round(row["mexc_carnet"]["mur_max_niveau_bid_usdt"] / prof05, 2) if prof05 > 0 else None)
        except Exception as e:                       # noqa: BLE001
            row["mexc_carnet"] = {"ok": False, "raison": str(e)[:120]}
            anomalies.append(f"{pair} : carnet illisible ({str(e)[:60]})")
        # --- trous de mémoire déclarés ---
        if pair not in prof:
            trous.append(f"{pair} : AUCUN profil (mur/spread/dip/stop = valeurs de repli du code)")
        if not a:
            trous.append(f"{pair} : AUCUNE vue live (pas dans les {len(asp_p)} sondées) — mur = profil figé")
        lignes.append(row)
        # --- anomalies mesurées ---
        if row.get("ecart_prix_feed_vs_mexc_bps") is not None and abs(row["ecart_prix_feed_vs_mexc_bps"]) > 50 and a:
            anomalies.append(f"{pair} : prix Hulk vs MEXC = {row['ecart_prix_feed_vs_mexc_bps']} bps "
                             f"(âge vue {row['vue_live_age_s']} s)")
        if row.get("ecart_spread_bps") is not None and abs(row["ecart_spread_bps"]) > 20:
            anomalies.append(f"{pair} : spread Hulk vs MEXC = {row['ecart_spread_bps']} bps")
        if row.get("ecart_mur_pct") is not None and abs(row["ecart_mur_pct"]) > 60:
            anomalies.append(f"{pair} : mur Hulk vs MEXC = {row['ecart_mur_pct']} % (mur = 1 ordre, "
                             f"très volatil — écart attendu, à lire avec la profondeur)")

    # ---------- tableau ----------
    def fnum(x, w=10, d=2):
        return f"{x:>{w}.{d}f}" if isinstance(x, (int, float)) else f"{'—':>{w}}"

    print(f"{'paire':<11}{'vue':<7}{'âge s':>7}{'Hulk px':>12}{'MEXC mid':>12}{'Δ bps':>8}"
          f"{'spread H':>9}{'spread M':>9}{'Δ':>8}{'mur H $':>12}{'mur M $':>12}{'Δ %':>9}"
          f"{'prof<0.5% $':>12}{'mur/prof':>9}")
    for r in sorted(lignes, key=lambda x: x["pair"]):
        b = r.get("mexc_carnet") or {}
        print(f"{r['pair']:<11}{str(r['vue_live'])[:6]:<7}"
              f"{fnum(r['vue_live_age_s'], 7, 0)}{fnum(r['hulk_prix_feed'], 12, 6)}"
              f"{fnum(b.get('mid'), 12, 6)}{fnum(r.get('ecart_prix_feed_vs_mexc_bps'), 8, 1)}"
              f"{fnum(r.get('hulk_spread_bps'), 9, 2)}{fnum(b.get('spread_bps'), 9, 2)}"
              f"{fnum(r.get('ecart_spread_bps'), 8, 2)}{fnum(r.get('hulk_mur_bid_usdt'), 12, 2)}"
              f"{fnum(b.get('mur_max_niveau_bid_usdt'), 12, 2)}{fnum(r.get('ecart_mur_pct'), 9, 1)}"
              f"{fnum(b.get('profondeur_cumul_sous_0.5pct_usdt'), 12, 2)}"
              f"{fnum(r.get('mur_sur_profondeur_0.5pct'), 9, 1)}")

    print()
    print(f"TROUS DE MÉMOIRE ({len(trous)}) :")
    for t in trous:
        print("  -", t)
    print()
    print(f"ANOMALIES MESURÉES ({len(anomalies)}) :")
    for a in anomalies:
        print("  -", a)
    if not anomalies:
        print("  (aucune au-delà des seuils de lecture 50 bps / 20 bps / 60 %)")

    rapport = {
        "instrument": "audit_mexc_vs_hulk.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sources_hulk": {
            "prix": "paper_diprip.fetch_all_prices → api.mexc.com/api/v3/ticker/price",
            "spread_mur": "ace_sense_mexc.book_sense → api.mexc.com/api/v3/depth?limit=20 "
                          "(mur = MAX niveau unitaire, PAS la profondeur cumulée)",
            "feed": "runs/aspiration_live.json (satellite_aspiration.py, MAX_PAIRS=5 par passe)",
            "profils": "strategie/universe_profils.json",
        },
        "vue_aspiration_ts_utc": asp_ts, "vue_aspiration_age_s": age_asp,
        "n_paires": len(paires), "n_profils": len(prof), "n_vues_live": len(asp_p),
        "trous": trous, "anomalies": anomalies, "paires": lignes,
        "lecture_seule": True, "ordres": 0,
    }
    SORTIE_JSON.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")
    SORTIE_TXT.write_text(
        "\n".join([f"AUDIT MEXC vs HULK — {rapport['ts_utc']}",
                   f"vue live : {asp_ts} (âge {age_asp} s) · paires {len(paires)} · profils {len(prof)}",
                   "", f"TROUS ({len(trous)}) :"] + [f"  - {t}" for t in trous] +
                  [f"", f"ANOMALIES ({len(anomalies)}) :"] + [f"  - {a}" for a in anomalies]),
        encoding="utf-8")
    print()
    print(f"écrit : {SORTIE_JSON.name} + {SORTIE_TXT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
