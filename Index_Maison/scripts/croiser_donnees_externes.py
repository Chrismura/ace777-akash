#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
croiser_donnees_externes.py — PROTOCOLE DE CROISEMENT EXTERNE (29/08, GO Christophe)
=====================================================================================
Christophe : « beaucoup de décisions se prennent sur nos données, mais on a vu
plusieurs fois qu'elles n'étaient pas correctes. Quand c'est important, il faut
les croiser avec des données extérieures pour être sûr qu'elles sont bonnes. »

RÈGLE DES 2 SOURCES (validée Christophe, 29/08 17:45Z) :
  1. Avant toute décision importante, vérifier le chiffre clé sur au moins
     1 source externe (MEXC, Binance, CoinGecko, blockstream, mempool).
  2. Écart > 5 % entre notre donnée et l'externe → data_quality_fail :
     on ne décide PAS, on récupère d'abord.
  3. Registre : chaque croisement (source externe + écart + verdict) est loggé
     dans Index_Maison/data/croisement_externe.jsonl pour audit.

CE QUE CE SCRIPT CROISE (v1 — les 2 données les plus critiques pour Hulk) :
  A. PRIX : nos prix (runs/croisement_contexte.jsonl, dernier par paire) vs
     ticker live MEXC + Binance (quand dispo).
  B. MURS : nos murs (runs/murs_observations.json, top_murs) vs order book
     live MEXC (bid/ask depth best).

Sorties :
  - Index_Maison/data/croisement_externe.jsonl   (registre, append)
  - Index_Maison/data/croisement_externe_etat.json (état récent pour le cockpit)
  - Index_Maison/data/alertes/ALERTE_data_quality.json (si ≥ 1 fail, sinon supprimé)

Stdlib uniquement. Plist : com.ace777.croisement-externe (StartInterval 1800).
Fail-open : une API en panne (ex. mempool) ne casse pas les autres.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent          # Index_Maison
HULK = INDEX.parent / "hulk-mexc"                        # hulk-mexc
RUNS = HULK / "runs"

CROISEMENT_CONTEXTE = RUNS / "croisement_contexte.jsonl"
MURS_OBSERVATIONS = RUNS / "murs_observations.json"

REGISTRE = INDEX / "data" / "croisement_externe.jsonl"
ETAT = INDEX / "data" / "croisement_externe_etat.json"
ALERTE_PATH = INDEX / "data" / "alertes" / "ALERTE_data_quality.json"

SEUIL_ECART_PCT = 5.0        # règle des 2 sources : > 5 % = fail
AGE_MAX_PRIX_MIN = 60        # un prix stocké de plus de 60 min = trop vieux (fail doux)

# Paires à croiser en priorité (celles qu'on trade / observe vraiment)
PAIRES_PRIORITAIRES = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "SOLUSDT", "ADAUSDT",
                       "CHIPUSDT", "QAITUSDT", "REDUSDT", "PYTHUSDT", "ZBCNUSDT",
                       "HBARUSDT", "XLMUSDT"]

MEXC_PRICE = "https://api.mexc.com/api/v3/ticker/price"
BINANCE_PRICE = "https://api.binance.com/api/v3/ticker/price"


def http_json(url: str, timeout: float = 10.0):
    req = urllib.request.Request(url, headers={"User-Agent": "ace777-croisement/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def prix_externes_mexc() -> dict:
    """Tous les prix MEXC en 1 appel (batch)."""
    try:
        j = http_json(MEXC_PRICE)
        return {d.get("symbol"): float(d["price"]) for d in j
                if d.get("symbol") and d.get("price")}
    except Exception:
        return {}


def prix_externe_binance(pair: str):
    try:
        j = http_json(f"{BINANCE_PRICE}?symbol={pair}")
        return float(j.get("price") or 0.0)
    except Exception:
        return None


def nos_prix() -> dict:
    """Dernier prix par paire depuis croisement_contexte.jsonl."""
    last: dict = {}
    try:
        with CROISEMENT_CONTEXTE.open(encoding="utf-8") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                p = d.get("pair")
                if p and d.get("price") is not None:
                    last[p] = {"price": float(d["price"]), "utc": d.get("utc", "")}
    except OSError:
        pass
    return last


def murs_externes_mexc(pair: str):
    """Profondeur totale USDT sur 5 niveaux MEXC (bid + ask).

    Le best price seul est trompeur (souvent minuscule) ; un mur se compare
    à la profondeur TOTALE locale — c'est l'ordre de grandeur qui compte.
    """
    try:
        j = http_json(f"https://api.mexc.com/api/v3/depth?symbol={pair}&limit=5")
        bids = j.get("bids") or []
        asks = j.get("asks") or []
        bid_tot = sum(float(b[1]) * float(b[0]) for b in bids)
        ask_tot = sum(float(a[1]) * float(a[0]) for a in asks)
        return bid_tot, ask_tot
    except Exception:
        return None, None


# Tolérance murs : contrôle d'ORDRE DE GRANDEUR (x0.05 à x20) — nos moyennes
# historiques (depuis le 16/08) vs un snapshot instantané varient naturellement
# d'un facteur 2-11 sur les paires (BTC 10x, CHIP 11x, HBAR 7x selon l'état du
# carnet au moment du scan). On ne fail que si c'est ABSURDE (x>20 ou x<0.05),
# c'est-à-dire une donnée visiblement fausse (type QAIT 66M BTC impossibles).
# Le contrôle FIN (écart > 5 %) reste réservé aux PRIX — la donnée critique
# des décisions d'exécution.
MURS_TOL_MIN = 0.05
MURS_TOL_MAX = 20.0


def nos_murs() -> dict:
    """Murs agrégés par paire depuis murs_observations.json (top_murs)."""
    try:
        d = json.loads(MURS_OBSERVATIONS.read_text(encoding="utf-8"))
        top = d.get("top_murs") or []
        return {str(m["pair"]).upper(): m for m in top if isinstance(m, dict) and m.get("pair")}
    except Exception:
        return {}


def ecart_pct(a: float, b: float) -> float:
    if not b:
        return 0.0
    return abs(a - b) / b * 100.0


def age_min(utc_str: str):
    """Âge en minutes d'un timestamp UTC stocké (None si illisible)."""
    try:
        t = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - t).total_seconds() / 60.0
    except Exception:
        return None


def main() -> int:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    registre: list = []
    fails: list = []
    warns: list = []

    prix_nos = nos_prix()
    prix_mexc = prix_externes_mexc()

    # ---------- A. CROISEMENT PRIX ----------
    paires_a_croiser = [p for p in PAIRES_PRIORITAIRES if p in prix_nos]
    if not paires_a_croiser:
        paires_a_croiser = list(prix_nos.keys())[:10]

    for pair in paires_a_croiser:
        notre = prix_nos[pair]
        p_me = prix_mexc.get(pair)
        p_bi = prix_externe_binance(pair) if pair in ("BTCUSDT", "ETHUSDT") else None

        refs = []
        if p_me is not None:
            refs.append(("mexc", p_me, ecart_pct(notre["price"], p_me)))
        if p_bi is not None:
            refs.append(("binance", p_bi, ecart_pct(notre["price"], p_bi)))

        if not refs:
            registre.append({"ts": ts, "type": "prix", "pair": pair,
                             "verdict": "no_source", "detail": "aucune API externe dispo"})
            continue

        # Le verdict se base sur la source avec le plus petit écart (le plus fiable)
        refs.sort(key=lambda r: r[2])
        src, prix_ref, ecart = refs[0]

        age = age_min(notre["utc"])
        stale = age is not None and age > AGE_MAX_PRIX_MIN

        fail = ecart > SEUIL_ECART_PCT
        if stale and ecart > 1.0:
            fail = True  # prix vieux ET écart = donnée douteuse

        verdict = "fail" if fail else "ok"
        if fail:
            fails.append({"type": "prix", "pair": pair, "ecart_pct": round(ecart, 2),
                          "notre": notre["price"], "externe": prix_ref, "source": src,
                          "age_min": round(age, 1) if age is not None else None})

        registre.append({
            "ts": ts, "type": "prix", "pair": pair,
            "notre_prix": notre["price"], "notre_utc": notre["utc"],
            "source": src, "prix_externe": prix_ref,
            "autres_sources": [{"source": s, "prix": p, "ecart_pct": round(e, 2)}
                               for s, p, e in refs[1:]],
            "ecart_pct": round(ecart, 2), "age_min": round(age, 1) if age is not None else None,
            "seuil_pct": SEUIL_ECART_PCT, "verdict": verdict,
        })

    # ---------- B. CROISEMENT MURS ----------
    # Les murs sont un WARNING informatif, PAS un fail bloquant : notre mur
    # moyen est une moyenne historique (depuis le 16/08) et la profondeur
    # externe est un snapshot instantané — le ratio varie naturellement de
    # 0.1x à 200x quand le carnet se déséquilibre (ex. BTC bid vide à
    # l'instant T). Ce n'est pas une donnée corrompue, c'est le marché.
    # Seul le PRIX (donnée critique d'exécution) déclenche le fail qui bloque.
    nos_m = nos_murs()

    def dans_tolerance(a: float, b: float) -> bool:
        """Contrôle d'ordre de grandeur (x0.05 à x20)."""
        if a <= 0 or b <= 0:
            return True
        r = a / b
        return MURS_TOL_MIN <= r <= MURS_TOL_MAX

    for pair, mi in nos_m.items():
        if pair not in PAIRES_PRIORITAIRES:
            continue
        bid_ext, ask_ext = murs_externes_mexc(pair)
        if bid_ext is None:
            continue
        bid_n = mi.get("bid_avg_usd") or 0.0
        ask_n = mi.get("ask_avg_usd") or 0.0

        ok_bid = dans_tolerance(bid_n, bid_ext)
        ok_ask = dans_tolerance(ask_n, ask_ext)
        if not (ok_bid and ok_ask):
            warns.append({"type": "murs", "pair": pair,
                          "notre_bid_avg": round(bid_n, 2), "ext_bid_5niv": round(bid_ext, 2),
                          "notre_ask_avg": round(ask_n, 2), "ext_ask_5niv": round(ask_ext, 2),
                          "note": f"ratio hors [{MURS_TOL_MIN}x-{MURS_TOL_MAX}x] — carnet déséquilibré ou donnée à surveiller"})

        registre.append({
            "ts": ts, "type": "murs", "pair": pair,
            "notre_bid_avg": round(bid_n, 2), "ext_bid_depth_5niv": round(bid_ext, 2),
            "notre_ask_avg": round(ask_n, 2), "ext_ask_depth_5niv": round(ask_ext, 2),
            "note": f"ordre de grandeur (x{MURS_TOL_MIN}-x{MURS_TOL_MAX}) moyenne historique vs profondeur 5 niveaux — warning informatif",
            "verdict": "ok" if (ok_bid and ok_ask) else "warn",
        })

    # ---------- ÉCRITURE ----------
    try:
        REGISTRE.parent.mkdir(parents=True, exist_ok=True)
        with REGISTRE.open("a", encoding="utf-8") as f:
            for ligne in registre:
                f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except OSError as e:
        print(f"[croisement] ERREUR registre: {e}", file=sys.stderr)

    etat = {
        "ts": ts,
        "n_verifications": len(registre),
        "n_fails": len(fails),
        "n_warns": len(warns),
        "fails": fails,
        "warns": warns[:8],
        "regle": f"écart > {SEUIL_ECART_PCT}% entre notre prix et une source externe = data_quality_fail (on ne décide pas) · murs = warning informatif",
        "lecture": (f"⛔ {len(fails)} prix douteux — vérifier avant décision"
                    if fails else (f"⚠️ {len(warns)} warning(s) murs (carnet déséquilibré) — prix OK"
                                   if warns else "✅ toutes les données croisées sont cohérentes")),
    }
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")

    # Alerte data_quality : écrite si ≥ 1 fail PRIX (bloquant), supprimée sinon.
    # Les warns murs ne déclenchent PAS d'alerte (pas de fausse alerte).
    ALERTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if fails:
        ALERTE_PATH.write_text(json.dumps({
            "id": "data_quality",
            "message": f"{len(fails)} prix en écart > {SEUIL_ECART_PCT}% avec une source externe — ne pas décider sans récupération",
            "ts": ts, "status": "actif",
            "fails": fails,
            "source": "Index_Maison/scripts/croiser_donnees_externes.py",
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    elif ALERTE_PATH.exists():
        ALERTE_PATH.unlink()

    # ---------- CONSOLE ----------
    print(f"[croisement] {ts} — {len(registre)} vérifications, {len(fails)} fail(s) prix, {len(warns)} warning(s) murs")
    for f_ in fails[:10]:
        print(f"  FAIL {f_['type']:5} {f_['pair']:<12} écart={f_['ecart_pct']}% (notre={f_['notre']}, externe={f_['externe']})")
    for w_ in warns[:5]:
        print(f"  WARN murs  {w_['pair']:<12} bid ratio hors tolérance (à surveiller)")
    print(f"[croisement] état -> {ETAT}")
    if fails:
        print(f"[croisement] ALERTE data_quality écrite -> {ALERTE_PATH}")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
