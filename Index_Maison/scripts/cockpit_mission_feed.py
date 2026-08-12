#!/usr/bin/env python3
"""
Cockpit mission feed — Alpha / Beta / Hulk (lecture seule).
Parse size, conf, tension, direction. Écrit mission.json + mission.js
"""
from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1")
RUNS = ROOT / "runs"
HULK = ROOT / "hulk-mexc" / "runs"
OUT = ROOT / "Index_Maison" / "cockpit"
THERMO = ROOT / "Index_Maison" / "thermo" / "live.json"


def fnum(x, d=4):
    try:
        return round(float(x), d)
    except Exception:
        return None


def freshest(glob_pat: str, root: Path):
    files = list(root.glob(glob_pat))
    if not files:
        return None
    return max(files, key=lambda p: p.stat().st_mtime)


def parse_hold(text: str | None) -> dict:
    t = text or ""
    out = {}
    for key in ("conf", "tension", "pct", "bid_drop", "ask_drop"):
        m = re.search(rf"{key}=([0-9.]+)", t)
        if m:
            out[key] = fnum(m.group(1), 6)
    m = re.search(r"size_note=([^\s]+)", t)
    if m:
        out["size_note"] = m.group(1)
    m = re.search(r"radar=(long|short|flat|none)", t, re.I)
    if m:
        out["radar_dir"] = m.group(1).lower()
    # leverage hint from size_note like hunter_revenge_1.5x
    m = re.search(r"([0-9]+(?:\.[0-9]+)?)x", t, re.I)
    if m:
        out["lev_hint"] = fnum(m.group(1), 2)
    return out


def parse_iso_ts(s: str | None):
    if not s:
        return None
    t = s.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(t)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def session_start_from_live(live: Path | None) -> datetime | None:
    """Début du boot courant = dernier STRICT CLONE + 1re heure HH:MM:SS (ou ISO).

    Les CSV NUAGE_* sont cumulatifs (plusieurs jours) — sans filtre le PnL cockpit ment.
    """
    if not live or not live.exists():
        return None
    try:
        # queue du fichier suffit (LIVE peut être énorme)
        raw = live.read_bytes()
        if len(raw) > 2_500_000:
            raw = raw[-2_500_000:]
        text = raw.decode("utf-8", errors="ignore")
    except Exception:
        return None
    lines = text.splitlines()
    banner_i = None
    for i in range(len(lines) - 1, -1, -1):
        if "STRICT CLONE" in lines[i]:
            banner_i = i
            break
    if banner_i is None:
        return None
    # date du LIVE (mtime UTC) — boot du matin = même jour que mtime en général
    day = datetime.fromtimestamp(live.stat().st_mtime, tz=timezone.utc).date()
    # ISO éventuel près du banner
    for j in range(banner_i, min(banner_i + 80, len(lines))):
        m = re.search(r"(20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})", lines[j])
        if m:
            return parse_iso_ts(m.group(1) + "Z")
    hhmm = None
    for j in range(banner_i, min(banner_i + 80, len(lines))):
        m = re.search(r"\b(\d{2}:\d{2}:\d{2})\b", lines[j])
        if m:
            hhmm = m.group(1)
            break
    if not hhmm:
        return datetime(day.year, day.month, day.day, tzinfo=timezone.utc)
    h, mi, s = map(int, hhmm.split(":"))
    return datetime(day.year, day.month, day.day, h, mi, s, tzinfo=timezone.utc)


def load_ace_side(path: Path | None, limit: int = 50, since: datetime | None = None):
    empty = {
        "file": None, "pnl": 0.0, "fills": 0, "skips": 0,
        "pnlLifetime": 0.0, "fillsLifetime": 0,
        "last": [], "fills_only": [], "spark": [], "cycle": None, "lastFill": None,
        "sessionSince": None,
    }
    if not path or not path.exists():
        return empty
    fills = skips = 0
    pnl = 0.0
    fills_life = 0
    pnl_life = 0.0
    rows = []
    fill_rows = []
    with path.open(newline="", encoding="utf-8", errors="ignore") as f:
        for row in csv.DictReader(f):
            st = (row.get("status") or "").upper()
            side = (row.get("side") or "").upper()
            p = fnum(row.get("pnl"), 6) or 0.0
            ts = row.get("ts")
            ts_dt = parse_iso_ts(ts)
            hold = parse_hold(row.get("holdSec") or row.get("msg") or "")
            item = {
                "ts": ts,
                "side": side or st,
                "status": st,
                "pnl": p,
                "qty": fnum(row.get("qty"), 6),
                "entry": fnum(row.get("entryPrice"), 2),
                "exit": fnum(row.get("exitPrice"), 2),
                "bps": fnum(row.get("bps"), 4),
                "reason": (row.get("exitReason") or "")[:70],
                "cycle": row.get("cycle"),
                **hold,
            }
            is_skip = st == "SKIPPED" or side == "SKIP"
            in_session = True
            if since is not None and ts_dt is not None:
                in_session = ts_dt >= since
            elif since is not None and ts_dt is None:
                # sans timestamp fiable : ignorer pour la session (évite faux +159$)
                in_session = False

            if is_skip:
                if in_session:
                    skips += 1
                    rows.append(item)
            else:
                fills_life += 1
                pnl_life += p
                if in_session:
                    fills += 1
                    pnl += p
                    fill_rows.append(item)
                    rows.append(item)
    last_cycle = rows[-1]["cycle"] if rows else None
    return {
        "file": path.name,
        "pnl": round(pnl, 4),
        "fills": fills,
        "skips": skips,
        "pnlLifetime": round(pnl_life, 4),
        "fillsLifetime": fills_life,
        "last": list(reversed(rows[-limit:])),
        "fills_only": list(reversed(fill_rows[-20:])),
        "spark": [r["pnl"] for r in fill_rows][-40:],
        "cycle": last_cycle,
        "lastFill": fill_rows[-1] if fill_rows else None,
        "sessionSince": since.strftime("%Y-%m-%dT%H:%MZ") if since else None,
        "mtime": datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
    }


def _crypto_from_pair(pair: str) -> str:
    p = (pair or "").upper()
    for suf in ("USDT", "USDC", "USD"):
        if p.endswith(suf) and len(p) > len(suf):
            return p[: -len(suf)]
    return p or "?"


def load_hulk():
    state = freshest("*_state.json", HULK)
    # CSV apparié au state (même stem) — sinon freshest PAPER*
    csv_p = None
    if state and state.exists():
        stem = state.name.replace("_state.json", "")
        cand = HULK / f"{stem}.csv"
        if cand.exists():
            csv_p = cand
    if not csv_p:
        csv_p = freshest("PAPER*.csv", HULK)
    out = {
        "file": None, "stateFile": None, "pnl": 0.0, "trades": 0,
        "notional": None, "base": None, "positions": [], "last": [], "bags": 0,
        "history": [],
    }
    if state and state.exists():
        s = json.loads(state.read_text(encoding="utf-8"))
        out["stateFile"] = state.name
        out["pnl"] = round(float(s.get("pnl_total") or 0), 4)
        out["trades"] = int(s.get("trades") or 0)
        out["notional"] = fnum(s.get("notional_live"), 2)
        out["base"] = fnum(s.get("base_notional"), 2)
        pos = s.get("positions") or {}
        maison = s.get("bags") or {}  # bags maison (distinct des trades ouverts)
        scores = s.get("scores") or {}
        pair_cash = s.get("pair_cash") or {}
        universe = list(s.get("pairs") or [])
        if not universe:
            universe = sorted(set(list(pos.keys()) + list(maison.keys()) + list(scores.keys())))

        def _row_open(pair: str, info: dict, kind: str) -> dict:
            entry = fnum(info.get("entry"), 6)
            high = fnum(info.get("high"), 6)
            qty = fnum(info.get("qty"), 6)
            sc = scores.get(pair) or {}
            mark = fnum(sc.get("price"), 6)
            if mark is None:
                mark = high  # paper : dernier haut suivi ≈ mark soft
            u_pnl = None
            pnl_pct = None
            if entry and mark is not None and qty:
                u_pnl = round((mark - entry) * qty, 4)
            if entry and mark is not None and entry > 0:
                pnl_pct = round((mark - entry) / entry * 100.0, 3)
            return {
                "pair": pair,
                "crypto": _crypto_from_pair(pair),
                "status": kind,  # TRADE | BAG | FLAT | CASH
                "dir": "LONG" if kind in ("TRADE", "BAG") else "FLAT",
                "entry": entry,
                "qty": qty,
                "stake": fnum(info.get("stake"), 2),
                "mark": mark,
                "high": high,
                "regime": info.get("regime") or sc.get("regime"),
                "uPnl": u_pnl,
                "uPnlApprox": u_pnl,
                "pnlPct": pnl_pct,
                "opened": info.get("ts"),
                "seed": bool(info.get("seed")),
                "open": True,
            }

        # positions ouvertes (trades) — rétrocompat UI
        for pair, info in pos.items():
            out["positions"].append(_row_open(pair, info, "TRADE"))
        out["bags"] = len(out["positions"])
        out["positions"].sort(key=lambda p: (p.get("uPnl") is None, -(p.get("uPnl") or 0)))

        # PORTEFEUILLE COMPLET = toutes les cryptos suivies (vision d’ensemble)
        portfolio = []
        open_set = set(pos.keys())
        bag_set = set(maison.keys())
        for pair in universe:
            sc = scores.get(pair) or {}
            if pair in pos:
                row = _row_open(pair, pos[pair], "TRADE")
            elif pair in maison:
                row = _row_open(pair, maison[pair], "BAG")
            else:
                cash = fnum(pair_cash.get(pair), 2) or 0.0
                mark = fnum(sc.get("price"), 6)
                row = {
                    "pair": pair,
                    "crypto": _crypto_from_pair(pair),
                    "status": "CASH" if cash > 0 else "FLAT",
                    "dir": "FLAT",
                    "entry": None,
                    "qty": None,
                    "stake": cash if cash > 0 else None,
                    "mark": mark,
                    "high": None,
                    "regime": sc.get("regime"),
                    "uPnl": None,
                    "uPnlApprox": None,
                    "pnlPct": fnum(sc.get("move24_pct"), 2),
                    "opened": None,
                    "seed": False,
                    "open": False,
                }
            portfolio.append(row)
        # ouverts d’abord, puis par nom
        portfolio.sort(key=lambda p: (0 if p.get("open") else 1, p.get("crypto") or p.get("pair") or ""))
        out["portfolio"] = portfolio
        out["universe"] = len(universe)
        out["bagsMaison"] = len(bag_set)
        out["openTrades"] = len(open_set)
    if csv_p and csv_p.exists():
        out["file"] = csv_p.name
        rows = []
        with csv_p.open(newline="", encoding="utf-8", errors="ignore") as f:
            for row in csv.DictReader(f):
                ev = (row.get("event") or "").upper()
                rows.append(
                    {
                        "ts": row.get("ts"),
                        "pair": row.get("pair"),
                        "crypto": _crypto_from_pair(row.get("pair") or ""),
                        "event": row.get("event"),
                        "dir": "LONG" if ev == "BUY" else (
                            "FLAT" if ev in ("SELL", "SELL_OK", "SELL_KO") else "?"
                        ),
                        "price": fnum(row.get("price"), 6),
                        "entry": fnum(row.get("entry"), 6),
                        "qty": fnum(row.get("qty"), 6),
                        "pnl": fnum(row.get("pnl_usdt"), 4) or 0.0,
                        "total": fnum(row.get("pnl_total"), 4),
                        "reason": (row.get("reason") or "")[:60],
                    }
                )
        # SKIP = bruit (centaines) — historique utile = BUY/SELL seulement
        real = [r for r in rows if (r.get("event") or "").upper() in (
            "BUY", "SELL", "SELL_OK", "SELL_KO"
        )]
        out["last"] = list(reversed(real[-20:]))
        out["history"] = list(reversed(real[-40:]))
        out["tradesClosed"] = sum(
            1 for r in rows if (r.get("event") or "").upper().startswith("SELL")
        )
    return out


def find_ace_pair():
    """Préfère le préfixe du LIVE le plus récent, sinon freshest ALPHA/BETA.
    Retourne (alpha_csv, beta_csv, live_path)."""
    lives = sorted(RUNS.glob("*_LIVE_COLOR.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    for live in lives[:8]:
        prefix = live.name.replace("_LIVE_COLOR.log", "")
        alphas = list(RUNS.glob(prefix + "*ALPHA*.csv"))
        betas = list(RUNS.glob(prefix + "*BETA*.csv"))
        if alphas and betas:
            return (
                max(alphas, key=lambda p: p.stat().st_mtime),
                max(betas, key=lambda p: p.stat().st_mtime),
                live,
            )
        if alphas:
            a = max(alphas, key=lambda p: p.stat().st_mtime)
            cand = RUNS / a.name.replace("ALPHA_X13_BURST13", "BETA_X5")
            if cand.exists():
                return a, cand, live

    alphas = sorted(RUNS.glob("*ALPHA*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    for a in alphas[:25]:
        name = a.name
        if "_ALPHA_" not in name:
            continue
        prefix = name.split("_ALPHA_")[0]
        betas = list(RUNS.glob(prefix + "*BETA*.csv"))
        if not betas:
            cand = RUNS / name.replace("ALPHA_X13_BURST13", "BETA_X5")
            if cand.exists():
                betas = [cand]
        if betas:
            live = RUNS / f"{prefix}_LIVE_COLOR.log"
            return a, max(betas, key=lambda p: p.stat().st_mtime), live if live.exists() else None
    return None, None, None


def load_ada_block(name: str) -> dict:
    """Lit un bloc ADA (intention, saison...) s'il existe — jamais bloquant."""
    p = ROOT / "Index_Maison" / "strategie" / name
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    # ADA saison + gardienne détectées AVANT le payload pour être à jour dans le même cycle
    try:
        import ada_saison
        ada_saison.scan()
    except Exception:
        pass
    try:
        import ada_gardienne
        ada_gardienne.scan()
    except Exception:
        pass

    a_path, b_path, live_path = find_ace_pair()
    since = session_start_from_live(live_path)
    alpha = load_ace_side(a_path, since=since)
    beta = load_ace_side(b_path, since=since)
    hulk = load_hulk()
    combo = round((alpha["pnl"] or 0) + (beta["pnl"] or 0), 4)

    thermo = {}
    if THERMO.exists():
        try:
            thermo = json.loads(THERMO.read_text(encoding="utf-8"))
        except Exception:
            pass

    # swarm pulse = max cycle
    try:
        cyc = max(int(alpha.get("cycle") or 0), int(beta.get("cycle") or 0))
    except Exception:
        cyc = 0

    thrust = {
        "alpha": min(100, max(8, 48 + (alpha["pnl"] or 0) * 10)),
        "beta": min(100, max(8, 48 + (beta["pnl"] or 0) * 10)),
        "hulk": min(100, max(8, 48 + (hulk["pnl"] or 0) * 6)),
    }
    alert = "nominal"
    if combo <= -20 or (hulk["pnl"] or 0) <= -5:
        alert = "red"
    elif combo < 0 or (hulk["pnl"] or 0) < 0:
        alert = "amber"

    run_label = None
    if a_path:
        run_label = a_path.name.split("_ALPHA_")[0] if "_ALPHA_" in a_path.name else a_path.stem

    payload = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "alert": alert,
        "run": run_label,
        "sessionSince": since.strftime("%Y-%m-%dT%H:%MZ") if since else None,
        "comboPnl": combo,
        "comboArrow": "up" if combo > 0 else ("down" if combo < 0 else "flat"),
        "swarmCycle": cyc,
        "thrust": thrust,
        "alpha": alpha,
        "beta": beta,
        "hulk": hulk,
        "portfolio": {
            "ace": combo,
            "aceArrow": "up" if combo > 0 else ("down" if combo < 0 else "flat"),
            "hulk": hulk["pnl"],
            "hulkArrow": "up" if (hulk["pnl"] or 0) > 0 else ("down" if (hulk["pnl"] or 0) < 0 else "flat"),
            "total": round(combo + (hulk["pnl"] or 0), 4),
        },
        "thermo": {
            "climate": thermo.get("climate"),
            "score": thermo.get("score"),
            "funding": thermo.get("funding"),
            "whaleN": thermo.get("whaleN"),
            "deltas": thermo.get("deltas") or {},
            "fearGreed": thermo.get("fearGreed"),
            "fearGreedLabel": thermo.get("fearGreedLabel"),
            "marketCapUsd": thermo.get("marketCapUsd"),
            "altSeason": thermo.get("altSeason"),
            "altSeasonScore": thermo.get("altSeasonScore"),
            "liq24Usd": thermo.get("liq24Usd"),
            "etf": thermo.get("etf") or {},
            "btcDominance": thermo.get("btcDominance"),
            "indicators": {
                k: thermo.get("indicators", {}).get(k)
                for k in ("D26", "D27", "D28", "D29", "D30", "D31", "D32")
                if thermo.get("indicators", {}).get(k)
            },
        },
    }

    # === BRIGUES ADA — lecture seule, jamais bloquantes ===
    payload["intention"] = load_ada_block("journal_intention_live.json")
    payload["saison"] = load_ada_block("ada_saison_live.json")
    _g = load_ada_block("ada_gardienne_live.json") or {}
    payload["gardienne"] = _g.get("gardienne") or {}
    payload["coup_doeil"] = _g.get("coup_doeil") or {}

    (OUT / "mission.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "mission.js").write_text("window.__MISSION__ = " + json.dumps(payload, ensure_ascii=False) + ";\n", encoding="utf-8")
    ob = ROOT / "Index_Maison" / "OUTBOX_OBSIDIAN" / "cockpit"
    ob.mkdir(parents=True, exist_ok=True)
    for name in ("mission.json", "mission.js"):
        (ob / name).write_text((OUT / name).read_text(encoding="utf-8"), encoding="utf-8")

    # Rafraîchit les briques ADA avec la session fraîche (jamais bloquant)
    try:
        import journal_intention
        journal_intention.scan()
    except Exception:
        pass

    print(f"MISSION_OK combo={combo} cycle={cyc} alert={alert} since={payload.get('sessionSince')}")
    print(
        f"  ALPHA fills={alpha['fills']} pnl={alpha['pnl']}"
        f" (life fills={alpha.get('fillsLifetime')} pnl={alpha.get('pnlLifetime')})"
    )
    print(
        f"  BETA  fills={beta['fills']} pnl={beta['pnl']}"
        f" (life fills={beta.get('fillsLifetime')} pnl={beta.get('pnlLifetime')})"
    )
    print(f"  HULK  bags={hulk['bags']} pnl={hulk['pnl']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
