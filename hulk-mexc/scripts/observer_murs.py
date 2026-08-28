#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
observer_murs.py — OBSERVATEUR DES MURS DE LIQUIDITÉ (24/08, GO Christophe)
===========================================================================
La sonde aspiration (paper_diprip.py) collecte les murs bid/ask depuis le
16/08 dans runs/ASPIRATION_CALIB_*.csv — mais PERSONNE ne les lit. Ce script
est l'observateur : il agrège toutes les mesures et produit un rapport clair :

  - par paire : mur bid moyen / mur ask moyen / mur max (en $) / n mesures
  - spoof : nb et taux de « mur fond puis reconstruit » (manipulation)
  - drop : les chutes brutales de mur (≥ 15 %/s) — le signal ACE
  - synthèse : quelles paires ont les vrais murs (liquidité réelle) vs les
    murs de façade (spoof)

Sorties :
  - hulk-mexc/runs/MURS_RAPPORT.md   (lisible, pour Christophe)
  - hulk-mexc/runs/murs_observations.json (structuré, pour le cockpit)
Stdlib uniquement. Plist : com.ace777.observer-murs (StartInterval, sans KeepAlive).
"""
import csv
import json
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # hulk-mexc
RUNS = ROOT / "runs"
RAPPORT_MD = RUNS / "MURS_RAPPORT.md"
RAPPORT_JSON = RUNS / "murs_observations.json"
OBSERVATION_LIST = ROOT / "strategie" / "observation_list.json"

SPOOF_DROP_PCT_S = 15.0  # seuil maison : mur qui fond ≥ 15%/s puis se reconstruit

# En-tête IDENTIQUE à ASPIRATION_CALIB (paper_diprip.py) → la même agrégation
# csv.DictReader fonctionne sur les deux, et le profil futur d'une paire
# observée aura déjà des mesures ("set de départ" pour le portefeuille).
OBS_HEADER = [
    "ts", "pair", "regime", "asp_side", "drop_bid_pct_per_s",
    "drop_ask_pct_per_s", "max_drop_pct_per_s", "spread_bps",
    "spread_delta_bps", "wall_bid_usdt", "wall_ask_usdt",
    "notional_ok", "spoof", "price_delta_pct", "btc_price",
    "btc_delta_pct", "delay_s", "price",
]


def http_json(url: str, timeout: float = 12.0) -> dict:
    """GET JSON minimal (sonde observation — découplée du moteur)."""
    req = urllib.request.Request(url, headers={"User-Agent": "hulk-observe/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def last_price(pair: str) -> float:
    try:
        j = http_json(f"https://api.mexc.com/api/v3/ticker/price?symbol={pair}")
        return float(j.get("price") or 0.0)
    except Exception:
        return 0.0


def charger_observation_list() -> list[str]:
    """Liste des paires à OBSERVER (murs) — jamais tradées, jamais scorées.
    strategie/observation_list.json : {"pairs": ["SOLUSDT", ...]}.
    Absent ou vide → pas de sonde (comportement historique inchangé)."""
    try:
        if not OBSERVATION_LIST.exists():
            return []
        data = json.loads(OBSERVATION_LIST.read_text(encoding="utf-8"))
        pairs = [str(p).strip().upper() for p in (data.get("pairs") or []) if str(p).strip()]
        return pairs[:50]  # garde-fou : jamais plus de 50
    except Exception:
        return []


def probe_observation() -> str:
    """Sonde MURS dédiée (27/08, GO Christophe) — DÉCOUPLÉE du moteur :
    tourne dans observer_murs.py (plist autonome, 0 lien avec paper_diprip) →
    JAMAIS de ralentissement des exécutions, garantie structurelle.

    Mesure les murs bid/ask (double lecture du carnet) des paires de la liste
    d'observation, et écrit OBSERVATION_MURS_<ts>.csv au même format que
    ASPIRATION_CALIB. Quand la paire entrera au portefeuille, son profil aura
    déjà l'historique des murs (n_mesures, spoof, drops) = set de départ.
    Fail-open : une paire en erreur n'arrête pas les autres."""
    pairs = charger_observation_list()
    if not pairs:
        return ""
    from ace_sense_mexc import aspiration_sense  # noqa: E402  (import local, plist stdlib)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    csv_path = RUNS / f"OBSERVATION_MURS_{ts}.csv"
    ok_n = 0
    try:
        # 1 ticker batch pour TOUS les prix (1 appel au lieu de N)
        prices: dict[str, float] = {}
        try:
            j = http_json("https://api.mexc.com/api/v3/ticker/price")
            prices = {d.get("symbol"): float(d["price"]) for d in j
                      if d.get("symbol") and d.get("price")}
        except Exception:
            pass
        btc_price = prices.get("BTCUSDT", last_price("BTCUSDT"))
        with csv_path.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(OBS_HEADER)
            for pair in pairs:
                try:
                    a = aspiration_sense(pair, http_json, delay_s=0.3,
                                         min_notional_usdt=500.0)
                    if not a.get("ok"):
                        continue
                    price = prices.get(pair, last_price(pair))
                    w.writerow([
                        datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                        pair, "OBS", a.get("aspiration_side"),
                        a.get("drop_bid_pct_per_s"), a.get("drop_ask_pct_per_s"),
                        a.get("max_drop_pct_per_s"), a.get("spread_bps"),
                        a.get("spread_delta_bps"), a.get("wall_bid_usdt"),
                        a.get("wall_ask_usdt"), a.get("notional_drop_ok"),
                        False, a.get("price_delta_pct"),
                        round(btc_price, 2), 0.0, a.get("delay_s"), price,
                    ])
                    ok_n += 1
                except Exception:
                    continue  # fail-open par paire
            f.flush()
    except Exception as e:
        print(f"OBSERVATION probe error: {e}")
        return ""
    print(f"OBSERVATION: {ok_n}/{len(pairs)} paires mesurées → {csv_path.name}")
    return csv_path.name


def charger_mesures():
    """Toutes les mesures de tous les CSVs ASPIRATION_CALIB + OBSERVATION_MURS."""
    mesures = []
    for glob_pat in ("ASPIRATION_CALIB_*.csv", "OBSERVATION_MURS_*.csv"):
        for csv_path in sorted(RUNS.glob(glob_pat)):
            try:
                with csv_path.open(newline="", encoding="utf-8", errors="ignore") as f:
                    for row in csv.DictReader(f):
                        mesures.append((csv_path.stem, row))
            except Exception:
                continue
    return mesures


def fnum(v, d=2):
    try:
        return round(float(v), d)
    except Exception:
        return None


def main() -> int:
    # Sonde observation (27/08) : mesure les murs des paires de la liste
    # d'observation AVANT l'agrégation — découplée du moteur, fail-open.
    obs_csv = probe_observation()
    mesures = charger_mesures()
    if not mesures:
        print("aucune mesure (pas de CSV ASPIRATION_CALIB)")
        return 1

    # agrégation par paire
    par_pair = defaultdict(lambda: {
        "n": 0, "bid_sum": 0.0, "ask_sum": 0.0, "bid_max": 0.0, "ask_max": 0.0,
        "spoof_n": 0, "drop_n": 0, "spread_sum": 0.0, "spread_n": 0,
    })
    total_spoof = 0
    total_drop = 0
    for src, r in mesures:
        pair = (r.get("pair") or "?").upper()
        a = par_pair[pair]
        a["n"] += 1
        wb = fnum(r.get("wall_bid_usdt")); wa = fnum(r.get("wall_ask_usdt"))
        if wb is not None:
            a["bid_sum"] += wb
            a["bid_max"] = max(a["bid_max"], wb)
        if wa is not None:
            a["ask_sum"] += wa
            a["ask_max"] = max(a["ask_max"], wa)
        if str(r.get("spoof") or "").strip().lower() in ("true", "1", "oui", "yes"):
            a["spoof_n"] += 1
            total_spoof += 1
        drop = fnum(r.get("drop_bid_pct_per_s")) or 0.0
        if drop >= SPOOF_DROP_PCT_S:
            a["drop_n"] += 1
            total_drop += 1
        sp = fnum(r.get("spread_bps"))
        if sp is not None:
            a["spread_sum"] += sp
            a["spread_n"] += 1

    # tri par mur bid moyen décroissant (les vrais murs)
    lignes = []
    for pair, a in sorted(par_pair.items(), key=lambda kv: -(kv[1]["bid_sum"] / max(1, kv[1]["n"]))):
        n = a["n"]
        bid_avg = a["bid_sum"] / max(1, n)
        ask_avg = a["ask_sum"] / max(1, n)
        spoof_pct = (a["spoof_n"] / max(1, n)) * 100
        spread_avg = (a["spread_sum"] / max(1, a["spread_n"])) if a["spread_n"] else None
        lignes.append({
            "pair": pair, "n": n,
            "bid_avg_usd": fnum(bid_avg), "bid_max_usd": fnum(a["bid_max"]),
            "ask_avg_usd": fnum(ask_avg), "ask_max_usd": fnum(a["ask_max"]),
            "spoof_n": a["spoof_n"], "spoof_pct": fnum(spoof_pct),
            "drop_n": a["drop_n"], "spread_avg_bps": fnum(spread_avg),
        })

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    total_mesures = len(mesures)

    # --- Rapport markdown lisible ---
    md = [
        "# OBSERVATOIRE DES MURS DE LIQUIDITÉ",
        f"> {ts} — {total_mesures} mesures sur {len(par_pair)} paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS" + (f" · sonde observation {obs_csv}" if obs_csv else ""),
        "",
        "## Les VRAIS murs (top 12 par mur bid moyen)",
        "",
        "| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |",
        "|---|---|---|---|---|---|---|",
    ]
    for l in lignes[:12]:
        md.append(
            f"| {l['pair']} | {l['n']} | {l['bid_avg_usd']} | {l['bid_max_usd']} | "
            f"{l['ask_avg_usd']} | {l['spoof_n']} ({l['spoof_pct']}%) | {l['drop_n']} |"
        )
    md += [
        "",
        f"## Synthèse",
        f"- **Total mesures** : {total_mesures} (16-24/08, sonde aspiration)",
        f"- **Spoofs détectés** : {total_spoof} ({total_spoof/max(1,total_mesures)*100:.1f}% des mesures) — murs de façade (fond puis se reconstruit)",
        f"- **Chutes brutales de mur** (≥ {SPOOF_DROP_PCT_S:.0f}%/s) : {total_drop} — le signal ACE « le mur s'effondre »",
        "",
        "## Lecture",
        "- Un mur BID épais = support réel (des acheteurs tiennent le prix)",
        "- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)",
        "- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)",
        "- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)",
        "",
    ]
    RAPPORT_MD.write_text("\n".join(md), encoding="utf-8")

    # --- JSON structuré pour le cockpit ---
    out = {
        "ts": ts,
        "n_mesures": total_mesures,
        "n_paires": len(par_pair),
        "total_spoof": total_spoof,
        "total_drop": total_drop,
        "top_murs": lignes,  # toutes les paires (pas juste top 12 — Hulk a besoin de TOUT)
        "lecture": (
            "Les murs BID épais = supports réels · les murs ASK épais = résistances. "
            "Spoof élevé = murs de façade (manipulation). Drop ≥ 15%/s = le mur "
            "s'effondre (le signal ACE)."
        ),
    }
    RAPPORT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"OK {ts} — {total_mesures} mesures, {len(par_pair)} paires, "
          f"{total_spoof} spoofs, {total_drop} drops")
    for l in lignes[:5]:
        print(f"  {l['pair']:12} bid_avg={l['bid_avg_usd']:>10} $  spoof={l['spoof_pct']}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
