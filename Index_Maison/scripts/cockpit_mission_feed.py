#!/usr/bin/env python3
"""
Cockpit mission feed — Alpha / Beta / Hulk (lecture seule).
Parse size, conf, tension, direction. Écrit mission.json + mission.js
"""
from __future__ import annotations

import csv
import json
import re
import time
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


def live_marks(pairs: list[str]) -> dict[str, float]:
    """Prix MEXC LIVE en 1 seul appel batch (fail-open).
    Le tableau DU DÉPART affichait scores[pair].price du state Hulk (sauvé
    toutes les ~60 s) → écart de plusieurs centaines de $ avec CoinMarketCap
    quand le marché bouge vite (observé 27/08 : BTC 80 283 → 79 942 en 5 min).
    Un seul GET /api/v3/ticker/price renvoie TOUS les symboles (~0.4 s,
    gratuit, zéro forfait). Si l'API ne répond pas → {} (on garde le state)."""
    import urllib.request
    if not pairs:
        return {}
    try:
        req = urllib.request.Request(
            "https://api.mexc.com/api/v3/ticker/price",
            headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        want = set(pairs)
        return {d.get("symbol"): float(d["price"]) for d in data
                if d.get("symbol") in want and d.get("price")}
    except Exception:
        return {}


def live_change24(pairs: list[str]) -> dict:
    """Vrai % 24h MEXC (priceChangePercent) en 1 appel, fail-open.
    C'est le % "maintenant vs il y a 24h" = ce que montre CoinMarketCap,
    distinct de move24_pct (amplitude haut-bas sur 24h, notre signal).
    On l'injecte dans chg24 des bulles SANS redémarrer le moteur Hulk.
    Si l'API ne répond pas → {} (le feed garde le fallback amplitude)."""
    import urllib.request
    if not pairs:
        return {}
    try:
        req = urllib.request.Request(
            "https://api.mexc.com/api/v3/ticker/24hr",
            headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        want = set(pairs)
        out = {}
        for d in data:
            sym = d.get("symbol")
            if sym not in want:
                continue
            v = d.get("priceChangePercent")
            if v is not None:
                try:
                    # MEXC renvoie une FRACTION (0.0832 = 8.32 %), pas un pourcentage.
                    out[sym] = round(float(v) * 100.0, 2)
                except Exception:
                    pass
        return out
    except Exception:
        return {}


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


def load_hulk_conseils() -> dict:
    """Conseils IA Hulk (lecture seule) : Cortana ADVISORY + Kelly ombre.
    ADA (gardienne) est déjà injecté à part dans le payload global."""
    out: dict = {}
    cp = ROOT / "hulk-mexc" / "strategie" / "cortana_pilot.json"
    if cp.exists():
        try:
            d = json.loads(cp.read_text(encoding="utf-8"))
            out["cortana"] = {
                "accuracy": d.get("cortana_accuracy_score"),
                "mode": d.get("enforced_mode"),
                "proposals": d.get("proposals") or [],
            }
        except Exception:
            pass
    kp = ROOT / "hulk-mexc" / "strategie" / "kelly_ombre.json"
    if kp.exists():
        try:
            d = json.loads(kp.read_text(encoding="utf-8"))
            out["kelly"] = {
                "win_rate": d.get("win_rate"),
                "n": d.get("n"),
                "mise": d.get("mise_recommandee"),
                "motif": d.get("motif"),
            }
        except Exception:
            pass
    return out


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
        "notional": None, "base": None, "cash": None, "equity": None, "engaged": None,
        "fees": None, "feeRate": 0.0005, "feeTrades": 0,
        "positions": [], "last": [], "bags": 0, "history": [], "skips": 0,
    }
    if state and state.exists():
        s = json.loads(state.read_text(encoding="utf-8"))
        out["stateFile"] = state.name
        out["pnl"] = round(float(s.get("pnl_total") or 0), 4)
        out["trades"] = int(s.get("trades") or 0)
        out["notional"] = fnum(s.get("notional_live"), 2)
        out["base"] = fnum(s.get("base_notional"), 2)
        # Wallet paper : cash libre récupéré (pair_cash) + équité = base + pnl
        pc = s.get("pair_cash") or {}
        cash_total = 0.0
        for v in pc.values():
            try:
                cash_total += float(v)
            except Exception:
                pass
        out["cash"] = round(cash_total, 2) if pc else 0.0
        if out["base"] is not None:
            out["equity"] = round(out["base"] + (out["pnl"] or 0.0), 2)
        pos = s.get("positions") or {}
        maison = s.get("bags") or {}  # bags maison (distinct des trades ouverts)
        scores = s.get("scores") or {}
        pair_cash = s.get("pair_cash") or {}
        universe = list(s.get("pairs") or [])
        if not universe:
            universe = sorted(set(list(pos.keys()) + list(maison.keys()) + list(scores.keys())))
        # Vrai % 24h marché (vs il y a 24h) récupéré en live MEXC, indépendant
        # du moteur (on n'a pas besoin de le redémarrer). move24 (amplitude) est
        # gardé tel quel = notre signal. chg24 = vrai % 24h.
        chg24_map = live_change24(universe)

        def _chg24(pair: str, sc: dict):
            if pair in chg24_map:
                return chg24_map[pair]
            return fnum(sc.get("change24_pct"), 2) if sc.get("change24_pct") is not None else fnum(sc.get("move24_pct"), 2)

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
            # BAG complet = position (qty × mark) + cash de la paire (pair_cash).
            # Quand Hulk vend PARTIEL, la qté baisse mais l'argent va dans le cash :
            # le bag total, lui, dit la vérité (mise 10 $ → bag 11,12 $ = +11 %).
            val_pos = (qty * mark) if (qty is not None and mark is not None) else None
            pair_c = float(pair_cash.get(pair, 0.0) or 0.0)
            bag_value = round(val_pos + pair_c, 4) if val_pos is not None else None
            stake = fnum(info.get("stake"), 2)
            bag_pct = None
            if bag_value is not None and stake:
                bag_pct = round((bag_value - stake) / stake * 100.0, 2)
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
                "bagValue": bag_value,
                "bagPct": bag_pct,
                "pairCash": round(pair_c, 2),
                "move24": fnum(sc.get("move24_pct"), 2),
                "chg24": _chg24(pair, sc),
                "opened": info.get("ts"),
                "seed": bool(info.get("seed")),
                "open": True,
            }

        # positions ouvertes (trades) — rétrocompat UI
        for pair, info in pos.items():
            out["positions"].append(_row_open(pair, info, "TRADE"))
        out["bags"] = len(out["positions"])
        out["positions"].sort(key=lambda p: (p.get("uPnl") is None, -(p.get("uPnl") or 0)))
        engaged = 0.0
        for p in out["positions"]:
            try:
                engaged += float(p.get("stake") or 0.0)
            except Exception:
                pass
        out["engaged"] = round(engaged, 2)

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
                    "move24": fnum(sc.get("move24_pct"), 2),
                    "chg24": _chg24(pair, sc),
                    "opened": None,
                    "seed": False,
                    "open": False,
                    # Fix 27/08 : les paires FERMÉES (stop) disparaissaient du
                    # tableau DU DÉPART et leur cash n'était pas compté dans le
                    # TOTAL. On porte explicitement pairCash + bagValue pour que
                    # le JS puisse les afficher et les sommer (vérité du wallet).
                    "pairCash": round(cash, 2),
                    "bagValue": round(cash, 2) if cash > 0 else None,
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
                price = fnum(row.get("price"), 6)
                entry = fnum(row.get("entry"), 6)
                pnl = fnum(row.get("pnl_usdt"), 4) or 0.0
                # sortie = vente / stop / bag (pnl réalisé) → % = (exit − entry) / entry
                is_exit = ev.startswith(("SELL", "STOP", "BAG_SELL", "BAG_CRASH"))
                pnl_pct = None
                if is_exit and price is not None and entry is not None and entry != 0:
                    pnl_pct = round((price - entry) / entry * 100.0, 2)
                rows.append(
                    {
                        "ts": row.get("ts"),
                        "pair": row.get("pair"),
                        "crypto": _crypto_from_pair(row.get("pair") or ""),
                        "event": row.get("event"),
                        "dir": "LONG" if ev == "BUY" else ("SELL" if is_exit else "?"),
                        "price": price,
                        "entry": entry,
                        "qty": fnum(row.get("qty"), 6),
                        "pnl": pnl,
                        "pnlPct": pnl_pct,
                        "total": fnum(row.get("pnl_total"), 4),
                        "reason": (row.get("reason") or "")[:60],
                    }
                )
        # Hulk CSV : on ne garde que les OPÉRATIONS RÉELLES (mouvement d'argent).
        # BUY / SELL / STOP / BAG_* / DCA = opérations. Les SKIP (radar, cooldown,
        # veille) sont des non-actions : exclues du journal pour ne pas noyer les
        # ventes/achats sous le bruit.
        real = [r for r in rows if (r.get("event") or "").strip()]
        trades = [
            r for r in real
            if (r.get("event") or "").upper().startswith(("BUY", "SELL", "STOP", "BAG", "DCA"))
        ]
        out["skips"] = len(real) - len(trades)
        # Détail des refus (27/08) : chaque SKIP a une raison (SENSE, MUR-SPOOF,
        # MUR-CASSE, VOL, SPREAD, CB…) — on les compte pour voir l'activité réelle
        # du moteur, pas seulement les trades exécutés. Sinon « il ne se passe rien »
        # alors que le moteur tente et refuse en continu.
        skip_reasons: dict[str, int] = {}
        for r in real:
            ev = (r.get("event") or "").upper()
            if ev != "SKIP":
                continue
            reason = (r.get("reason") or "SKIP").split(":", 1)[0][:24]
            skip_reasons[reason] = skip_reasons.get(reason, 0) + 1
        out["skipReasons"] = dict(sorted(skip_reasons.items(), key=lambda kv: -kv[1]))
        out["last"] = list(reversed(trades[-30:]))
        out["history"] = list(reversed(trades))  # TOUS les trades exécutés (Christophe : « je veux voir tout les trades exécutés »)
        out["tradesClosed"] = sum(
            1 for r in rows
            if (r.get("event") or "").upper().startswith(("SELL", "STOP", "BAG_SELL", "BAG_CRASH"))
        )
        # Frais plateforme estimés — MEXC spot : 0 % maker / 0,05 % taker.
        # Le moteur paper ne déduit PAS encore les frais : on estime ici ce que
        # coûterait le run en réel (taker, car ordres au marché).
        fee_total = 0.0
        fee_trades = 0
        for r in rows:
            px = r.get("price")
            qt = r.get("qty")
            if px is not None and qt is not None:
                try:
                    fee_total += float(px) * float(qt) * out["feeRate"]
                    fee_trades += 1
                except Exception:
                    pass
        out["fees"] = round(fee_total, 4)
        out["feeTrades"] = fee_trades

    # ——— WALLET : origine → réel vs statique (buy & hold) ———
    # Origine (point zéro Christophe 19/08) : 10 $ crypto + 20 $ cash = 30 $.
    out["walletOrigine"] = 30.0
    out["walletOrigineCrypto"] = 10.0
    out["walletOrigineCash"] = 20.0
    # Réel = valeur positions ouvertes (qty × mark) + cash libre (pair_cash).
    reel_pos = 0.0
    for p in out["positions"]:
        if p.get("qty") and p.get("mark"):
            try:
                reel_pos += float(p["qty"]) * float(p["mark"])
            except Exception:
                pass
    reel_cash = float(out.get("cash") or 0.0)
    out["walletReel"] = round(reel_pos + reel_cash, 2)
    out["walletReelPos"] = round(reel_pos, 2)
    out["walletReelCash"] = round(reel_cash, 2)
    # Statique = seeds tenus au cours actuel (buy & hold) + 20 $ cash initial.
    # Quantités de seed lues dans le CSV (BUY reason SEED_START).
    # 28/08 (Buffy) : on capture AUSSI seed_px (prix d'entrée du seed) et le
    # PnL RÉALISÉ cumulé par paire (SELL/SELL_PARTIAL/STOP/BAG_*) pour que le
    # tableau compare pomme avec pomme : "si rien fait" = move du prix depuis
    # le seed, "réel Hulk" = realized + uPnl (pas la valeur du bag réinvesti).
    seed_qty: dict[str, float] = {}
    seed_px: dict[str, float] = {}
    realized_pnl: dict[str, float] = {}
    if csv_p and csv_p.exists():
        with csv_p.open(newline="", encoding="utf-8", errors="ignore") as f:
            for row in csv.DictReader(f):
                _pair = row.get("pair") or ""
                _ev = (row.get("event") or "").upper()
                if _ev == "BUY" and (row.get("reason") or "").upper().startswith("SEED"):
                    try:
                        seed_qty[_pair] = float(row["qty"])
                        seed_px[_pair] = float(row["price"])
                    except Exception:
                        pass
                elif _ev.startswith(("SELL", "STOP", "BAG_SELL", "BAG_CRASH")):
                    try:
                        realized_pnl[_pair] = realized_pnl.get(_pair, 0.0) + float(row.get("pnl_usdt") or 0)
                    except Exception:
                        pass
    # Synthèse (24/08, fix resume) : après une reprise --resume, le CSV du run
    # n'a PAS de lignes SEED (positions restaurées en mémoire sans re-seed) →
    # seed_qty vide → « bags de départ » + statique vides à l'écran. On
    # reconstruit la quantité d'origine depuis l'état : qty_init (quantité de
    # départ AVANT ventes partielles), sinon stake/entry.
    _s_all = json.loads(state.read_text(encoding="utf-8")) if state and state.exists() else {}
    sc_all = _s_all.get("scores") or {}
    pos_all = _s_all.get("positions") or {}
    for pair, p in pos_all.items():
        if pair in seed_qty:
            continue
        qi = p.get("qty_init")
        if qi is not None:
            try:
                seed_qty[pair] = float(qi)
                continue
            except Exception:
                pass
        try:
            stake = float(p.get("stake") or 0.0)
            entry = float(p.get("entry") or 0.0)
            if stake > 0 and entry > 0:
                seed_qty[pair] = stake / entry
        except Exception:
            pass
    statique_pos = 0.0
    for pair, sq in seed_qty.items():
        mark = fnum((sc_all.get(pair) or {}).get("price"), 6)
        if mark is None:
            mark = (pos_all.get(pair) or {}).get("high")
        if mark:
            statique_pos += sq * float(mark)
    out["walletStatique"] = round(statique_pos + out["walletOrigineCash"], 2)
    out["walletStatiquePos"] = round(statique_pos, 2)
    out["walletEcart"] = round((out["walletReel"] or 0.0) - (out["walletStatique"] or 0.0), 2)
    # Tableau statique par crypto : qté seed (départ 10 $), valeur si rien fait, %.
    # Enrichir AUSSI out["portfolio"] : le JS du tableau DU DÉPART lit portfolio
    # en priorité — sans ça, seedQty/statiqueVal restaient vides à l'écran.
    def _statique_row(p):
        pair = p.get("pair") or ""
        sq = seed_qty.get(pair)
        px0 = seed_px.get(pair)
        if sq and p.get("mark"):
            p["seedQty"] = round(sq, 4)
            if px0:
                # 28/08 (Buffy) : seedPx = prix d'entrée du seed → le % "si rien
                # fait" devient le vrai move depuis le DÉPART (avant : entrée de la
                # position actuelle, ce qui faussait PYTH −0,33% au lieu de −4,7%).
                p["seedPx"] = round(px0, 6)
                p["seedVal"] = round(sq * px0, 2)
                p["statiquePct"] = round(
                    (float(p["mark"]) / px0 - 1.0) * 100.0, 2
                )
            else:
                p["statiquePct"] = round(
                    (float(p["mark"]) / float(p["entry"] or 1.0) - 1.0) * 100.0, 2
                ) if p.get("entry") else None
            p["statiqueVal"] = round(sq * float(p["mark"]), 2)
        p["realized"] = round(realized_pnl.get(pair, 0.0), 4)
    for p in out.get("portfolio") or []:
        _statique_row(p)
    for p in out["positions"]:
        _statique_row(p)

    # PRIX LIVE (27/08, Christophe : « le BTC affiche une différence de 300$
    # avec CoinMarketCap ») : le state Hulk est sauvé toutes les ~60 s, donc le
    # tableau affichait un prix périmé. 1 appel batch MEXC rafraîchit mark pour
    # TOUTES les paires suivies (ouvertes + FLAT) + recalcule les dérivés que le
    # JS affiche (cours, bagValue, statiqueVal, uPnl, pnlPct). Fail-open.
    pairs_folio = [p.get("pair") for p in (out.get("portfolio") or []) if p.get("pair")]
    lv = live_marks(pairs_folio)
    if lv:
        for p in out.get("portfolio") or []:
            px = lv.get(p.get("pair"))
            if px is None:
                continue
            p["mark"] = round(px, 6)
            qty = p.get("qty")
            if qty is not None:
                val = qty * px
                p["bagValue"] = round(val + float(p.get("pairCash") or 0.0), 4)
                entry = p.get("entry")
                if entry:
                    p["uPnl"] = round((px - entry) * qty, 4)
                    p["pnlPct"] = round((px - entry) / entry * 100.0, 3)
                stake = p.get("stake")
                if stake:
                    p["bagPct"] = round(
                        (float(p["bagValue"]) - float(stake)) / float(stake) * 100.0, 2)
            sq = p.get("seedQty")
            if sq is not None:
                p["statiqueVal"] = round(sq * px, 2)
                px0 = p.get("seedPx")  # 28/08 : vrai point de départ si connu
                if px0:
                    p["statiquePct"] = round((px / float(px0) - 1.0) * 100.0, 2)
                elif p.get("entry"):
                    p["statiquePct"] = round((px / float(p["entry"]) - 1.0) * 100.0, 2)
        # walletReel / walletStatique rafraîchis avec les prix live (vérité du moment)
        reel_pos = 0.0
        for p in out["positions"]:
            if p.get("qty") and p.get("mark"):
                try:
                    reel_pos += float(p["qty"]) * float(p["mark"])
                except Exception:
                    pass
        out["walletReel"] = round(reel_pos + float(out.get("cash") or 0.0), 2)
        out["walletReelPos"] = round(reel_pos, 2)
        st_pos = 0.0
        for p in out.get("portfolio") or []:
            if p.get("seedQty") and p.get("statiqueVal"):
                try:
                    st_pos += float(p["statiqueVal"])
                except Exception:
                    pass
        out["walletStatique"] = round(st_pos + float(out.get("walletOrigineCash") or 20.0), 2)
        out["walletStatiquePos"] = round(st_pos, 2)
        out["walletEcart"] = round(
            (out["walletReel"] or 0.0) - (out["walletStatique"] or 0.0), 2)

    # ——— SCORE « PORTEFEUILLE PAR CRYPTO » (28/08, Christophe : « +20$ c'était
    # pour CHAQUE crypto pour qu'il puisse opérer tranquillement, réfléchis à
    # une façon plus intelligente de tester le portefeuille ») ———
    # Le vrai design : chaque crypto a SON budget = seed + MARGE (20$) pour
    # opérer (DCA, ré-achats après stop…). On teste le portefeuille comme un
    # portefeuille de mini-comptes INDÉPENDANTS :
    #   1. budget par paire = coût du seed + MARGE_PAR_CRYPTO
    #   2. on REJOUE le CSV PAR PAIRE : BUY/DCA débite (qty×px + frais),
    #      SELL/STOP/BAG crédite (qty×px − frais) → cash réel de la paire
    #   3. valeur Hulk par paire = cash réel + position au mark live
    #   4. HOLD par paire = MÊME budget investi au prix du seed et tenu
    #      (comparaison équitable : même capital des deux côtés)
    #   5. écart par paire = Hulk − HOLD → somme = score du portefeuille
    # Garde-fou : si le net investi d'une paire dépasse son budget → alerte
    # (le moteur paper n'a pas de pool global : il pourrait dépenser plus que
    # le budget de la paire sans s'en rendre compte).
    MARGE_PAR_CRYPTO = 20.0
    # marks live (portfolio enrichi en amont par live_marks)
    mark_by_pair = {}
    for _p in out.get("portfolio") or []:
        if _p.get("pair") and _p.get("mark") is not None:
            mark_by_pair[_p["pair"]] = float(_p["mark"])
    # 30/08 (fix Christophe : « je n'ai pas les nouvelles entrées sur le tableau ») :
    # le tableau ne listait que les paires seedées/possessionnées → les paires
    # OBSERVE (QNT/FLUID/RWA/MNSRY, ni seed ni position par construction) étaient
    # INVISIBLES et QAIT (delisted 29/08) traînait encore en résidu du CSV.
    # On construit depuis l'UNIVERS actuel du state (16 tradées + 4 observe) :
    # les observe apparaissent en ligne neutre (budget = marge 20$, jamais
    # tradée, écart 0 → ne fausse pas le score) et QAIT disparaît (plus dans
    # l'univers → plus compté, cohérent avec son delisting).
    if state and state.exists():
        _all_pairs = set(universe)
    else:
        _all_pairs = set(seed_qty.keys()) | set(pos_all.keys())
    # Paires OBSERVE-ONLY (ni seed ni position) : le CSV peut contenir des
    # LIGNES RÉSIDUELLES (ex : FLUID a un BUY parasite du moteur v1 du 30/08
    # 09:54Z, annulé à 0 PnL ensuite). Rejouer ces lignes débiterait le cash
    # de la paire → écart faux (−19,55$). Pour une observe, le budget reste
    # intact : cash 20$ des deux côtés, écart 0. On les exclut donc du rejeu.
    _observe_pairs = _all_pairs - set(seed_qty.keys()) - set(pos_all.keys())
    # rejeu par paire : cash initial = budget (seed + marge)
    cash_par_paire: dict[str, float] = {}
    nadir_par_paire: dict[str, float] = {}
    net_investi: dict[str, float] = {}
    budget_par_paire: dict[str, float] = {}
    for _pair in _all_pairs:
        _sp = seed_px.get(_pair)
        if _sp is None:
            _sp = (pos_all.get(_pair) or {}).get("entry")
        _seed_val = float(seed_qty.get(_pair) or 0.0) * float(_sp or 0.0)
        budget_par_paire[_pair] = _seed_val + MARGE_PAR_CRYPTO
        cash_par_paire[_pair] = budget_par_paire[_pair]
        nadir_par_paire[_pair] = budget_par_paire[_pair]
        net_investi[_pair] = 0.0
    if csv_p and csv_p.exists():
        with csv_p.open(newline="", encoding="utf-8", errors="ignore") as f:
            for row in csv.DictReader(f):
                _pair = row.get("pair") or ""
                if _pair not in cash_par_paire or _pair in _observe_pairs:
                    continue
                _ev = (row.get("event") or "").upper()
                if _ev not in ("BUY", "DCA") and not _ev.startswith(("SELL", "STOP", "BAG")):
                    continue
                try:
                    _q = float(row.get("qty") or 0.0)
                    _p = float(row.get("price") or 0.0)
                except Exception:
                    continue
                if _q <= 0 or _p <= 0:
                    continue
                _notional = _q * _p
                _fee = _notional * float(out.get("feeRate") or 0.0)
                if _ev in ("BUY", "DCA"):
                    cash_par_paire[_pair] -= _notional + _fee
                    net_investi[_pair] += _notional
                else:
                    cash_par_paire[_pair] += _notional - _fee
                    net_investi[_pair] -= _notional
                if cash_par_paire[_pair] < nadir_par_paire[_pair]:
                    nadir_par_paire[_pair] = cash_par_paire[_pair]
    # valeur Hulk + HOLD par paire (même budget, tenu au seed_px)
    reel_par_paire: dict[str, float] = {}
    hold_par_paire: dict[str, float] = {}
    seed_par_paire: dict[str, float] = {}
    pos_par_paire: dict[str, float] = {}
    over_budget: list[str] = []
    for _pair in _all_pairs:
        _qty = float((pos_all.get(_pair) or {}).get("qty") or 0.0)
        _mark = mark_by_pair.get(_pair)
        _pos_val = _qty * _mark if (_qty and _mark) else 0.0
        _sp = seed_px.get(_pair)
        if _sp is None:
            _sp = (pos_all.get(_pair) or {}).get("entry")
        _seed_val = float(seed_qty.get(_pair) or 0.0) * float(_sp or 0.0)
        seed_par_paire[_pair] = _seed_val
        pos_par_paire[_pair] = _pos_val
        reel_par_paire[_pair] = cash_par_paire.get(_pair, 0.0) + _pos_val
        _budget = budget_par_paire.get(_pair, 0.0)
        # « Si rien fait » (29/08, Christophe) : les 20 $ de marge sont une
        # RÉSERVE de trading, pas un achat direct. Donc « rien fait » = le SEED
        # (10 $) tenu au cours actuel + la marge (20 $) qui reste en cash —
        # jamais investie. AVANT : on calculait (budget/seed_px)*mark, c-à-d les
        # 30 $ investis d'office (biaisé vs Hulk quand le prix monte).
        _seed_qty = float(seed_qty.get(_pair) or 0.0)
        if _mark and _seed_qty:
            hold_par_paire[_pair] = (_seed_qty * _mark) + MARGE_PAR_CRYPTO
        else:
            hold_par_paire[_pair] = _budget
        if net_investi.get(_pair, 0.0) > _budget + 0.01:
            over_budget.append(_pair)
    reel_w = sum(reel_par_paire.values())
    stat_w = sum(hold_par_paire.values())
    cash_reel = sum(cash_par_paire.values())
    cash_nadir = min(nadir_par_paire.values()) if nadir_par_paire else 0.0
    ecart_w = round(reel_w - stat_w, 2)
    base_pct = stat_w if stat_w != 0 else 1.0
    ecart_pct = round((reel_w - stat_w) / base_pct * 100.0, 2) if stat_w else None
    if ecart_w > 0:
        vs_verdict = "HULK > HOLD"
    elif ecart_w < 0:
        vs_verdict = "HULK < HOLD"
    else:
        vs_verdict = "ÉGAL"
    out["cashReel"] = round(cash_reel, 2)
    out["cashNadir"] = round(cash_nadir, 2)
    out["walletReelVrai"] = round(reel_w, 2)
    out["hulkVsHold"] = {
        "reel": round(reel_w, 2),
        "hold": round(stat_w, 2),
        "ecart_usd": ecart_w,
        "ecart_pct": ecart_pct,
        "verdict": vs_verdict,
        # Vrai compte PAR CRYPTO : chaque paire a son budget (seed + 20$ de
        # marge) et son cash rejoué. cash = somme des cash réels par paire
        # (ce qu'un vrai compte aurait en poche). cashPaper = ancien affichage.
        "cash": round(cash_reel, 2),
        "cashPaper": round(float(out.get("cash") or 0.0), 2),
        "cashNadir": round(cash_nadir, 2),
        "margeParCrypto": MARGE_PAR_CRYPTO,
        "nbPaires": len(_all_pairs),
        "budgetTotal": round(sum(budget_par_paire.values()), 2),
        "overBudget": over_budget,
        "pairs": sorted(
            [
                {
                    "pair": _p,
                    "seed": round(seed_par_paire.get(_p, 0.0), 2),
                    "seedQty": round(float(seed_qty.get(_p) or 0.0), 6),
                    "budget": round(budget_par_paire.get(_p, 0.0), 2),
                    "net": round(net_investi.get(_p, 0.0), 2),
                    "pos": round(pos_par_paire.get(_p, 0.0), 2),
                    "posQty": round(float((pos_all.get(_p) or {}).get("qty") or 0.0), 6),
                    "cash": round(cash_par_paire.get(_p, 0.0), 2),
                    "reel": round(reel_par_paire.get(_p, 0.0), 2),
                    "hold": round(hold_par_paire.get(_p, 0.0), 2),
                    "ecart": round(reel_par_paire.get(_p, 0.0) - hold_par_paire.get(_p, 0.0), 2),
                    "over": net_investi.get(_p, 0.0) > budget_par_paire.get(_p, 0.0) + 0.01,
                }
                for _p in _all_pairs
            ],
            key=lambda x: x["ecart"],
            reverse=True,
        ),
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    out["conseils"] = load_hulk_conseils()
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
    # Frais RÉELS Binance (income) + PnL net — le vrai compas (pas une estimation CSV).
    fees_actual = {}
    fees_path = ROOT / "Index_Maison" / "thermo" / "fees_platforme.json"
    if fees_path.exists():
        try:
            fees_actual = json.loads(fees_path.read_text(encoding="utf-8"))
        except Exception:
            fees_actual = {}
    combo_fees_today = fees_actual.get("today", {}).get("commission", 0.0) or 0.0
    combo_fees_24h = fees_actual.get("h24", {}).get("commission", 0.0) or 0.0
    combo_net = round(combo + combo_fees_today, 4)

    thermo = {}
    if THERMO.exists():
        try:
            thermo = json.loads(THERMO.read_text(encoding="utf-8"))
        except Exception:
            pass

    # ===== VÉRITÉ MOTEUR (27/08) : le run est-il VRAIMENT vivant ? =====
    # Avant : mission.json présentait le run le plus récent comme « live » même si
    # le moteur était éteint depuis des jours (CSV figés) → le cockpit mentait.
    # Même règle que le pont (/status) : LIVE_COLOR frais ≤45s = ON, ≤180s = STALE,
    # au-delà = OFF (moteur arrêté — on affiche le dernier run en HISTORIQUE).
    engine_state = "OFF"
    engine_age = None
    if live_path and live_path.exists():
        import time as _t
        engine_age = int(_t.time() - live_path.stat().st_mtime)
        if engine_age <= 45:
            engine_state = "ON"
        elif engine_age <= 180:
            engine_state = "STALE"
        else:
            engine_state = "OFF"
    engine_last = None
    if live_path:
        try:
            import time as _t2
            from datetime import datetime as _dt, timezone as _tz
            engine_last = _dt.fromtimestamp(live_path.stat().st_mtime, tz=_tz.utc).strftime("%Y-%m-%dT%H:%MZ")
        except Exception:
            engine_last = None

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
    if combo_net <= -20 or (hulk["pnl"] or 0) <= -5:
        alert = "red"
    elif combo_net < 0 or (hulk["pnl"] or 0) < 0:
        alert = "amber"

    run_label = None
    if a_path:
        run_label = a_path.name.split("_ALPHA_")[0] if "_ALPHA_" in a_path.name else a_path.stem

    payload = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "alert": alert,
        # VÉRITÉ MOTEUR (27/08) : ON/STALE/OFF + dernière trace du run + âge
        # → le cockpit peut afficher « moteur à l'arrêt depuis le 22/08 » au lieu
        # de présenter un run mort comme vivant.
        "engine": {"state": engine_state, "ageSec": engine_age, "last": engine_last},
        "run": run_label,
        "sessionSince": since.strftime("%Y-%m-%dT%H:%MZ") if since else None,
        "comboPnl": combo,
        "comboFeesToday": combo_fees_today,
        "comboFees24h": combo_fees_24h,
        "comboPnlNet": combo_net,
        "comboArrow": "up" if combo_net > 0 else ("down" if combo_net < 0 else "flat"),
        "swarmCycle": cyc,
        "thrust": thrust,
        "alpha": alpha,
        "beta": beta,
        "hulk": hulk,
        "portfolio": {
            "ace": combo_net,
            "aceArrow": "up" if combo_net > 0 else ("down" if combo_net < 0 else "flat"),
            "hulk": hulk["pnl"],
            "hulkArrow": "up" if (hulk["pnl"] or 0) > 0 else ("down" if (hulk["pnl"] or 0) < 0 else "flat"),
            "total": round(combo_net + (hulk["pnl"] or 0), 4),
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
            "onchain": thermo.get("onchain") or {},  # scan baleines RÉEL (mempool) + CPFP
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
    # === DISJONCTEUR UNIQUE (16/08) — lecture seule, jamais bloquante ===
    payload["disjoncteur"] = load_ada_block("disjoncteur_state.json") or {
        "declenche": False, "raison": "Normal", "ts": ""}

    (OUT / "mission.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "mission.js").write_text("window.__MISSION__ = " + json.dumps(payload, ensure_ascii=False) + ";\n", encoding="utf-8")
    # Cache-buster AUTO (27/08) : le ?v= des scripts était FIGÉ → un navigateur
    # qui cache mission.js par URL servait une copie périmée (symptôme Christophe :
    # journal rempli mais tableau départ + bulles vides). À chaque écriture du feed,
    # on tamponne ?v=<epoch> dans index.html → le prochain rechargement est frais.
    try:
        idx = OUT / "index.html"
        txt = idx.read_text(encoding="utf-8")
        now = int(time.time())
        new_txt = re.sub(r"(\?v=)\d+", r"\g<1>" + str(now), txt)
        new_txt = re.sub(r"(<meta name=\"version\" content=\")\d+(\")", r"\g<1>" + str(now) + r"\g<2>", new_txt)
        if new_txt != txt:
            idx.write_text(new_txt, encoding="utf-8")
    except Exception:
        pass
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
