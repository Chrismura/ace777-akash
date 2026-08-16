#!/usr/bin/env python3
"""
Hulk MEXC — paper v1.5 (aucune clé).

Mise pleine (ex. 20$) → à 2× (40$) vend la moitié (récupère la mise) → reste = bag.
Bag : DCA lent / vend 90% si crash / redeploie le cash si remonte.
Volume sniffer small-caps + sense MEXC.
v1.5 : anti-reentry post-stop (cooldown) + skip RED veille (soft).
Genesis / GO_USINE NUAGE : non touchés.
"""
from __future__ import annotations

import csv
import json
import os
import signal
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# capteurs F1-like (module local Hulk — pas ACE genesis)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ace_sense_mexc import aspiration_sense, book_sense, entry_gate, tension_score  # noqa: E402
from veille_gates import entry_gate_check, record_stop, veille_stale  # noqa: E402
from cortana_contract import process_pilot  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "defaults.env"
INV = ROOT / "data" / "universe_mexc_inventory.csv"
RUNS = ROOT / "runs"
STOP_FILE = ROOT / "STOP_PAPER"

# Couleurs terminal (désactiver: NO_COLOR=1)
_USE_COLOR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")


class C:
    R = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    # cycle
    BUY = "\033[1;32m"  # vert — entrée
    SELL_OK = "\033[1;36m"  # cyan — sortie +
    SELL_KO = "\033[1;31m"  # rouge — sortie − / stop
    BAG = "\033[1;35m"  # magenta — bag manuel
    RUNNER = "\033[1;33m"  # jaune — runner
    REENTRY = "\033[1;34m"  # bleu — re-achat armé
    HEART = "\033[90m"  # gris — heartbeat
    SCORE = "\033[37m"
    WARN = "\033[33m"
    ERR = "\033[31m"
    HDR = "\033[1;37m"
    # régimes
    IMPULSE = "\033[1;33m"
    COOLING = "\033[1;36m"
    WATCH = "\033[90m"
    QUIET = "\033[2;37m"


def paint(color: str, text: str) -> str:
    if not _USE_COLOR:
        return text
    return f"{color}{text}{C.R}"


def say(kind: str, msg: str) -> None:
    """Log coloré par type d'événement du cycle."""
    colors = {
        "buy": C.BUY,
        "sell_ok": C.SELL_OK,
        "sell_ko": C.SELL_KO,
        "bag": C.BAG,
        "runner": C.RUNNER,
        "reentry": C.REENTRY,
        "heart": C.HEART,
        "score": C.SCORE,
        "warn": C.WARN,
        "err": C.ERR,
        "hdr": C.HDR,
    }
    print(paint(colors.get(kind, C.SCORE), msg))


def legend() -> None:
    say("hdr", "Légende — logique mise → 2× → bag :")
    say("buy", "  ■ BUY             = tu mises 100% (ex. 20$)")
    say("sell_ok", "  ■ STAKE_OUT       = ticket à 40$ → vend 50% (récupère la mise)")
    say("bag", "  ■ BAG             = l'autre moitié = plus-value (maison)")
    say("bag", "  ■ BAG DCA / CRASH = lent → DCA ; crash → vend 90%")
    say("sell_ko", "  ■ STOP trade      = coupe la mise si stop avant 2×")
    say("reentry", "  ■ CASH redeploy   = cash récupéré → rachat 100% si dip")
    say("heart", "  ■ heartbeat       = cycle vivant")
    say("score", "  ■ radar           = régime + pos/bag/cash + vol")
    print()
    say(
        "hdr",
        "Seuil 2× (simple) : mise 20$ → quand la position vaut 40$, tu vends la moitié.",
    )
    print()


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_env(path: Path) -> dict:
    d = {}
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            d[k.strip()] = v.strip()
    return d


def http_json(url: str, timeout: float = 40.0, retries: int = 4):
    """GET JSON avec retries (timeouts MEXC fréquents)."""
    last_err: Optional[Exception] = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hulk-paper/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
            last_err = e
            time.sleep(1.2 * (attempt + 1))
    assert last_err is not None
    raise last_err


def load_inventory() -> dict[str, dict]:
    out: dict[str, dict] = {}
    if not INV.exists():
        return out
    for r in csv.DictReader(INV.open()):
        p = (r.get("pair") or "").strip().upper()
        if p:
            out[p] = r
    return out


def pick_pairs(cfg: dict, inv: dict[str, dict]) -> list[str]:
    raw = cfg.get("PAPER_PAIRS", "").strip()
    if raw:
        # famille 16/08 : PAPER_PAIRS ne contourne plus le filtre tier — tier B exclu
        # sauf s'il est explicitement en watch (PAPER_EXTRA_PAIRS)
        extra = {
            p.strip().upper()
            for p in (cfg.get("PAPER_EXTRA_PAIRS") or "").split(",")
            if p.strip()
        }
        out = []
        for p in raw.split(","):
            p = p.strip().upper()
            if not p:
                continue
            t = (inv.get(p) or {}).get("tier", "A")
            if t == "B" and p not in extra:
                print(f"[TIER] exclue {p} (tier B illiquide — watch via PAPER_EXTRA_PAIRS si voulu)")
                continue
            out.append(p)
        return out
    n = int(float(cfg.get("PAPER_MAX_PAIRS", "10")))
    rows = list(inv.values())
    a = [r for r in rows if r.get("tier") == "A" and r.get("pair")]
    a.sort(key=lambda r: -float(r.get("quote_vol_usdt") or 0))
    pairs = [r["pair"].upper() for r in a[:n]]
    # spike candidates B utiles (ex. QAIT) si slot
    extra = cfg.get("PAPER_EXTRA_PAIRS", "QAITUSDT").strip()
    for p in [x.strip().upper() for x in extra.split(",") if x.strip()]:
        if p not in pairs:
            pairs.append(p)
    return pairs


def last_price(pair: str) -> float:
    q = urllib.parse.urlencode({"symbol": pair})
    j = http_json(f"https://api.mexc.com/api/v3/ticker/price?{q}")
    return float(j["price"])


def ticker_24h(pair: str) -> dict:
    q = urllib.parse.urlencode({"symbol": pair})
    j = http_json(f"https://api.mexc.com/api/v3/ticker/24hr?{q}")
    return {
        "price": float(j.get("lastPrice") or j.get("price") or 0),
        "quote_vol": float(j.get("quoteVolume") or 0),
        "change_pct": float(j.get("priceChangePercent") or 0),
    }


def klines(pair: str, interval: str, limit: int) -> list:
    q = urllib.parse.urlencode(
        {"symbol": pair, "interval": interval, "limit": max(5, min(1000, limit))}
    )
    return http_json(f"https://api.mexc.com/api/v3/klines?{q}")


def _ohlc(kl: list) -> tuple[list[float], list[float], list[float], list[float]]:
    o = [float(c[1]) for c in kl]
    h = [float(c[2]) for c in kl]
    l = [float(c[3]) for c in kl]
    c_ = [float(c[4]) for c in kl]
    return o, h, l, c_


def _quote_vols(kl: list) -> list[float]:
    """Quote volume USDT par bougie (MEXC kline[7]), fallback base*close."""
    out: list[float] = []
    for c in kl:
        if len(c) > 7 and c[7] not in (None, ""):
            out.append(float(c[7]))
        else:
            out.append(float(c[5]) * float(c[4]))
    return out


def sniff_volume(kl15: list, cfg: dict) -> dict:
    """
    Sniff volume tôt (même fetch klines) — prioritaire small-caps.
    vx = vol 6h récent / médiane des fenêtres 6h sur ~15j.
    """
    qv = _quote_vols(kl15)
    if len(qv) < 12:
        return {
            "vol6_usdt": 0.0,
            "vol_med6_usdt": 0.0,
            "vol_spike": 0.0,
            "vol_flag": "NA",
        }
    windows = []
    for i in range(0, len(qv) - 5):
        windows.append(sum(qv[i : i + 6]))
    windows.sort()
    med = windows[len(windows) // 2] if windows else 1.0
    vol6 = sum(qv[-6:])
    vx = vol6 / med if med > 0 else 0.0
    hot = float(cfg.get("VOL_HOT_SPIKE", "2.0"))
    ok = float(cfg.get("VOL_OK_SPIKE", "1.3"))
    dry = float(cfg.get("VOL_DRY_SPIKE", "0.8"))
    if vx >= hot:
        flag = "HOT"
    elif vx >= ok:
        flag = "OK"
    elif vx >= dry:
        flag = "DRY"
    else:
        flag = "DEAD"
    return {
        "vol6_usdt": round(vol6, 0),
        "vol_med6_usdt": round(med, 0),
        "vol_spike": round(vx, 2),
        "vol_flag": flag,
    }


def score_pair(pair: str, cfg: dict) -> dict:
    """Régime + cadence + sniff volume (15j 1h)."""
    quiet_min = float(cfg.get("QUIET_RANGE_PCT", "8"))
    spike_15 = float(cfg.get("SPIKE_15D_PCT", "25"))
    impulse_th = float(cfg.get("IMPULSE_PCT", "8"))
    cooling_dd = float(cfg.get("COOLING_DD_MIN_PCT", "6"))

    # Un seul fetch 60m × 15j (évite double timeout MEXC)
    kl15 = klines(pair, "60m", 24 * 15)
    _, h15, l15, c15 = _ohlc(kl15)
    price = c15[-1] if c15 else 0.0
    peak15 = max(h15) if h15 else 0.0
    trough15 = min(l15) if l15 else 0.0
    range15 = ((peak15 / trough15) - 1.0) * 100.0 if trough15 > 0 else 0.0
    dd15 = ((1.0 - price / peak15) * 100.0) if peak15 > 0 else 0.0

    # volume sniffer (priorité small-cap) — avant régimes d'entrée
    vol = sniff_volume(kl15, cfg)
    vol24 = 0.0
    try:
        t24 = ticker_24h(pair)
        vol24 = float(t24.get("quote_vol") or 0)
        if t24.get("price"):
            price = float(t24["price"])
            dd15 = ((1.0 - price / peak15) * 100.0) if peak15 > 0 else dd15
    except Exception:
        pass

    # cadence = médiane des ranges journaliers approx (24h blocs)
    day_ranges = []
    for i in range(0, len(h15), 24):
        chunk_h = h15[i : i + 24]
        chunk_l = l15[i : i + 24]
        if chunk_h and chunk_l and min(chunk_l) > 0:
            day_ranges.append((max(chunk_h) / min(chunk_l) - 1.0) * 100.0)
    day_ranges.sort()
    cadence = day_ranges[len(day_ranges) // 2] if day_ranges else max(range15 / 5.0, 3.0)

    # impulse 6h / 24h = slice du même historique
    h1 = h15[-24:] if len(h15) >= 24 else h15
    l1 = l15[-24:] if len(l15) >= 24 else l15
    peak24 = max(h1) if h1 else peak15
    trough24 = min(l1) if l1 else trough15
    move24 = ((peak24 / trough24) - 1.0) * 100.0 if trough24 > 0 else 0.0
    dd24 = ((1.0 - price / peak24) * 100.0) if peak24 > 0 else 0.0

    h6, l6 = (h1[-6:] if len(h1) >= 6 else h1), (l1[-6:] if len(l1) >= 6 else l1)
    peak6 = max(h6) if h6 else price
    trough6 = min(l6) if l6 else price
    move6 = ((peak6 / trough6) - 1.0) * 100.0 if trough6 > 0 else 0.0
    dd6 = ((1.0 - price / peak6) * 100.0) if peak6 > 0 else 0.0

    # seuils adaptés à la cadence
    dip = max(float(cfg.get("DIP_FLOOR_PCT", "2.5")), cadence * float(cfg.get("DIP_CADENCE_MULT", "0.45")))
    rip = max(float(cfg.get("RIP_FLOOR_PCT", "1.5")), cadence * float(cfg.get("RIP_CADENCE_MULT", "0.35")))
    stop = max(float(cfg.get("STOP_FLOOR_PCT", "4.0")), cadence * float(cfg.get("STOP_CADENCE_MULT", "0.70")))

    had_spike = range15 >= spike_15 or move24 >= impulse_th
    impulse_now = move6 >= impulse_th or move24 >= impulse_th * 1.2
    # COOLING strict : vrai spike 15j + drawdown significatif (pas un micro -2%)
    cooling = had_spike and dd15 >= cooling_dd and not (impulse_now and dd6 < 1.0)
    quiet = range15 < quiet_min and move24 < quiet_min * 0.6

    # pullback min pour entrer (fraction du range 15j, floor cooling_dd)
    cool_entry = max(
        cooling_dd,
        dip,
        range15 * float(cfg.get("COOLING_PULLBACK_FRAC", "0.25")),
    )
    impulse_entry = max(
        dip,
        float(cfg.get("IMPULSE_PULLBACK_MIN_PCT", "5")),
        move6 * float(cfg.get("IMPULSE_PULLBACK_FRAC", "0.30")),
    )

    small_cap_th = float(cfg.get("VOL_SMALL_CAP_USDT", "400000"))
    is_small = vol24 < small_cap_th or cadence >= float(cfg.get("VOL_SMALL_CADENCE", "12"))
    vol["vol24_usdt"] = round(vol24, 0)
    vol["is_small_cap"] = is_small

    if quiet and not impulse_now:
        regime = "QUIET"
    elif impulse_now and dd6 >= impulse_entry * 0.85:
        regime = "IMPULSE"
    elif impulse_now:
        regime = "IMPULSE_WAIT"
    elif cooling:
        regime = "COOLING"
    else:
        regime = "WATCH"

    return {
        "pair": pair,
        "price": price,
        "regime": regime,
        "cadence_pct": round(cadence, 2),
        "range15_pct": round(range15, 2),
        "dd15_pct": round(dd15, 2),
        "dd24_pct": round(dd24, 2),
        "dd6_pct": round(dd6, 2),
        "move6_pct": round(move6, 2),
        "move24_pct": round(move24, 2),
        "peak15": peak15,
        "peak24": peak24,
        "peak6": peak6,
        "dip_pct": round(dip, 2),
        "rip_pct": round(rip, 2),
        "stop_pct": round(stop, 2),
        "cool_entry_pct": round(cool_entry, 2),
        "impulse_entry_pct": round(impulse_entry, 2),
        **vol,
    }


class PaperBot:
    def __init__(self, cfg: dict, pairs: list[str], inv: dict[str, dict]):
        self.cfg = cfg
        self.pairs = pairs
        self.inv = inv
        self.poll = int(float(cfg.get("POLL_SEC", "20")))
        self.score_every = int(float(cfg.get("SCORE_EVERY", "3")))
        # v1.4 : plus de bag 15% — pleine mise, puis 2× → moitié bag
        self.double_mult = float(cfg.get("STAKE_DOUBLE_MULT", "2.0"))
        self.stake_sell_frac = float(cfg.get("STAKE_SELL_FRAC", "0.50"))
        self.bag_crash_dd = float(cfg.get("BAG_CRASH_DD_PCT", "20"))
        self.bag_crash_sell_frac = float(cfg.get("BAG_CRASH_SELL_FRAC", "0.90"))
        self.bag_dca_on = cfg.get("BAG_DCA_ON", "1").strip() not in ("0", "false", "False")
        self.bag_slow_dd = float(cfg.get("BAG_SLOW_DD_PCT", "8"))
        self.bag_dca_dd = float(cfg.get("BAG_DCA_DD_PCT", "6"))
        self.bag_dca_ttl = float(cfg.get("BAG_DCA_TTL_SEC", "86400"))
        self.cash_redeploy_on = cfg.get("CASH_REDEPLOY_ON", "1").strip() not in (
            "0",
            "false",
            "False",
        )
        self.base_notional = float(cfg.get("NOTIONAL_USDT", "20"))
        self.notional = self.base_notional
        self.compound_on = cfg.get("COMPOUND_ON", "1").strip() not in ("0", "false", "False")
        self.compound_frac = float(cfg.get("COMPOUND_FRAC", "0.50"))
        self.compound_max_mult = float(cfg.get("COMPOUND_MAX_MULT", "3.0"))
        self.reentry_on = cfg.get("REENTRY_ON", "1").strip() not in ("0", "false", "False")
        self.reentry_dd = float(cfg.get("REENTRY_DD_PCT", "6"))
        self.reentry_ttl = float(cfg.get("REENTRY_TTL_SEC", "7200"))
        # v1.5 gates
        self.stop_cooldown_h = float(cfg.get("STOP_COOLDOWN_HOURS", "2"))
        self.veille_skip_red = cfg.get("VEILLE_SKIP_RED_ON", "1").strip() not in (
            "0",
            "false",
            "False",
        )
        self.veille_window_min = int(float(cfg.get("VEILLE_STATUS_MAX_AGE_MIN", "30")))
        self.veille_refresh_sec = float(cfg.get("VEILLE_STATUS_REFRESH_SEC", "60"))
        self.veille_stale_h = float(cfg.get("VEILLE_STALE_HOURS", "6"))
        # === 2 classes de paires (famille 15/08) ===
        self.bag_pairs = {
            p.strip().upper() for p in (cfg.get("BAG_PAIRS") or "").split(",") if p.strip()
        }
        self.bag_max_positions = max(1, int(float(cfg.get("BAG_MAX_POSITIONS", "5"))))
        self.bag_position_mult = float(cfg.get("BAG_POSITION_MULT", "0.5"))
        self.bag_no_tech_stop = cfg.get("BAG_NO_TECH_STOP", "1").strip() not in ("0", "false", "False")
        # === tier/rip (famille 16/08) : tier B = taille microscopique, rip partiel, re-entry borné ===
        self.tier_b_position_mult = float(cfg.get("TIER_B_POSITION_MULT", "0.25"))
        self.tier_b_spread_max = float(cfg.get("TIER_B_SPREAD_MAX_BPS", "100"))
        self.buy_spread_max = float(cfg.get("BUY_SPREAD_MAX_BPS", "100"))
        self.rip_sell_frac = float(cfg.get("RIP_SELL_FRAC", "0.50"))
        # 16/08 soir (Christophe) : RIP scale-out 2 paliers — XRP/HBAR tôt (2%/6%), reste small caps (6%/8%)
        self.rip_early_pairs = {
            p.strip().upper()
            for p in (cfg.get("RIP_EARLY_PAIRS") or "XRPUSDT,HBARUSDT").split(",")
            if p.strip()
        }
        self.rip_early_p1 = float(cfg.get("RIP_EARLY_P1_PCT", "2.0"))
        self.rip_early_p2 = float(cfg.get("RIP_EARLY_P2_PCT", "6.0"))
        self.rip_late_p1 = float(cfg.get("RIP_LATE_P1_PCT", "6.0"))
        self.rip_late_p2 = float(cfg.get("RIP_LATE_P2_PCT", "8.0"))
        self.rip_scaleout_frac = float(cfg.get("RIP_SCALEOUT_FRAC", "0.25"))
        self.reentry_max = max(1, int(float(cfg.get("REENTRY_MAX", "1"))))
        self.reentry_count: dict[str, int] = {}
        # Bag de départ (test boucle bag dès le 1er jour) — 15/08 Christophe
        self.seed_bags_on = cfg.get("SEED_BAGS_ON", "1").strip() not in ("0", "false", "False")
        self.seed_bags_usdt = float(cfg.get("SEED_BAGS_USDT", "10"))
        self.seed_bags_dd = float(cfg.get("SEED_BAGS_ENTRY_DD_PCT", "8"))
        self.seed_bags_pairs = {
            p.strip().upper() for p in (cfg.get("SEED_BAGS_PAIRS") or "CCUSDT").split(",") if p.strip()
        }
        self.cortana_mode = (cfg.get("CORTANA_MODE", "ADVISORY") or "ADVISORY").strip().upper()
        self.cortana_pilot = ROOT / (cfg.get("CORTANA_PILOT_FILE") or "strategie/cortana_pilot.json")
        self.cortana_pending: list = []
        self.cortana_applied: dict = {}
        self.sense_on = cfg.get("SENSE_ON", "1").strip() not in ("0", "false", "False")
        self.vol_spike_min_small = float(cfg.get("VOL_SPIKE_MIN_SMALL", "1.5"))
        # === Sonde aspiration (16/08, mode OBSERVATION 48h — zéro effet sur les entrées) ===
        # Consensus codeur 4/4 + famille 6/6 + Cortana : double lecture du carnet (pattern V8 ACE),
        # log + radar + calibration CSV, SANS agir sur le moteur. Fail-open sur timeout MEXC.
        self.aspiration_on = cfg.get("ASPIRATION_ON", "1").strip() not in ("0", "false", "False")
        self.aspiration_delay_s = float(cfg.get("ASPIRATION_DELAY_S", "0.5"))
        self.aspiration_min_notional = float(cfg.get("ASPIRATION_MIN_NOTIONAL_USDT", "500"))
        # Probe toutes les N cycles (rate-limit MEXC ~200 req/min) + max paires actives par probe
        self.aspiration_probe_every = max(1, int(float(cfg.get("ASPIRATION_PROBE_EVERY", "1"))))
        self.aspiration_max_pairs = max(1, int(float(cfg.get("ASPIRATION_MAX_PAIRS", "5"))))
        # Seuil spoof (%/s) — 15% est une valeur de départ, à CALIBRER sur les données 48h
        self.aspiration_spoof_drop = float(cfg.get("ASPIRATION_SPOOF_DROP_PCT_S", "15"))
        # Corrélation BTC (16/08 Christophe) : BTCUSDT lu 1× par probe, stocké à côté de
        # chaque mesure → dans 48h, séparer « vrai signal » de « bruit entraîné par BTC »
        self.btc_price: float = 0.0
        self.btc_prev: float = 0.0
        self.aspiration: dict[str, dict] = {}  # dernière mesure par paire (radar + calibration)
        self.aspiration_prev: dict[str, dict] = {}  # lecture précédente (détection spoof « rétractable »)
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        self.aspiration_csv = RUNS / f"ASPIRATION_CALIB_{ts}.csv"
        if self.aspiration_on:
            with self.aspiration_csv.open("w", newline="") as f:
                csv.writer(f).writerow(
                    [
                        "ts", "pair", "regime", "asp_side", "drop_bid_pct_per_s",
                        "drop_ask_pct_per_s", "max_drop_pct_per_s", "spread_bps",
                        "spread_delta_bps", "wall_bid_usdt", "wall_ask_usdt",
                        "notional_ok", "spoof", "price_delta_pct", "btc_price",
                        "btc_delta_pct", "delay_s", "price",
                    ]
                )
        # Seed inventaire au boot (réalisme vente / marché baissier)
        self.seed_on = cfg.get("SEED_ON", "0").strip() not in ("0", "false", "False")
        self.seed_usdt = float(cfg.get("SEED_USDT", "20"))
        self.seed_mode = (cfg.get("SEED_MODE", "split") or "split").strip().lower()
        self.seed_max_pairs = max(1, int(float(cfg.get("SEED_MAX_PAIRS", "2"))))
        self.alive = True
        self.scores: dict[str, dict] = {}
        self.pos: dict[str, dict] = {}  # trade tant que < 2×
        self.bags: dict[str, dict] = {}  # plus-value après stake-out
        self.bag_dca: dict[str, dict] = {}  # attente rachat plus bas
        self.pair_cash: dict[str, float] = {}  # USDT libre par paire (mise récupérée)
        self.tier_logged: set[str] = set()  # log une fois des exclusions tier B (boot)
        self.reentry: dict[str, dict] = {}
        self.pnl_total = 0.0
        self.trades = 0
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        self.csv_path = RUNS / f"PAPER_V1_{ts}.csv"
        self.state_path = RUNS / f"PAPER_V1_{ts}_state.json"
        RUNS.mkdir(parents=True, exist_ok=True)
        with self.csv_path.open("w", newline="") as f:
            csv.writer(f).writerow(
                [
                    "ts",
                    "pair",
                    "event",
                    "regime",
                    "price",
                    "entry",
                    "qty",
                    "pnl_usdt",
                    "pnl_total",
                    "cadence",
                    "reason",
                ]
            )
        signal.signal(signal.SIGINT, self._stop)
        signal.signal(signal.SIGTERM, self._stop)

    def current_notional(self) -> float:
        """Taille trade : base + fraction du PnL réalisé (compound), plafonnée."""
        if not self.compound_on:
            self.notional = self.base_notional
            return self.notional
        grown = self.base_notional + max(0.0, self.pnl_total) * self.compound_frac
        if self.pnl_total < 0:
            grown = max(self.base_notional * 0.5, self.base_notional + self.pnl_total * 0.25)
        cap = self.base_notional * self.compound_max_mult
        self.notional = min(max(grown, self.base_notional * 0.5), cap)
        return self.notional

    def add_pair_cash(self, pair: str, usdt: float):
        if usdt <= 0:
            return
        self.pair_cash[pair] = float(self.pair_cash.get(pair, 0.0)) + usdt

    def take_pair_cash(self, pair: str, usdt: Optional[float] = None) -> float:
        have = float(self.pair_cash.get(pair, 0.0))
        if have <= 0:
            return 0.0
        take = have if usdt is None else min(have, usdt)
        left = have - take
        if left <= 0.01:
            self.pair_cash.pop(pair, None)
        else:
            self.pair_cash[pair] = left
        return take

    def _stop(self, *_):
        self.alive = False
        say("warn", f"\n[{utc_now()}] STOP demandé — fin propre")

    def tier(self, pair: str) -> str:
        return (self.inv.get(pair) or {}).get("tier", "A")

    def is_bag(self, pair: str) -> bool:
        """Classe B (small caps bag) : règles d'exception."""
        return pair in self.bag_pairs

    def sense_ok(self, pair: str, sc: dict, regime: str) -> tuple[bool, str]:
        if not self.sense_on:
            return True, "sense_off"
        try:
            sense = book_sense(pair, http_json)
        except Exception as e:
            return False, f"sense_err:{e}"
        tens = tension_score(
            sc.get("move6_pct", 0),
            sc.get("cadence_pct", 3),
            sc.get("dd6_pct", 0),
        )
        sc["tension"] = tens
        sc["sense"] = sense
        tier = self.tier(pair)
        allow_wide = tier == "B" or "IMPULSE" in regime or self.is_bag(pair)
        # deep cooling : tension mini assouplie
        cfg = dict(self.cfg)
        if regime == "COOLING" and sc.get("dd15_pct", 0) >= sc.get("cool_entry_pct", 8):
            cfg["SENSE_STRICT_TENSION"] = "0"
        ok, why = entry_gate(sense, tens, cfg, tier=tier, allow_wide_spike=allow_wide)
        return ok, why

    def probe_aspiration(self, n_cycle: int):
        """
        Sonde aspiration — MODE OBSERVATION (décision famille/codeur/Cortana 16/08).

        Double lecture du carnet (pattern V8 ACE : RADAR → FENÊTRE → MUR → ASPIRATION) sur
        les paires ACTIVES (régime COOLING/IMPULSE) seulement, max ASPIRATION_MAX_PAIRS par
        probe, toutes les ASPIRATION_PROBE_EVERY cycles (rate-limit MEXC).

        ZÉRO effet sur le moteur : on log + on remplit self.aspiration (radar) + CSV de
        calibration. Le spoof est « rétractable à maintenant » (décision Christophe 16/08) :
        mur fond puis reconstruit → spoof pour CETTE lecture, réévalué à chaque échantillon
        (debounce, pas de ban — pas de timer 15 min).
        """
        if not self.aspiration_on or n_cycle % self.aspiration_probe_every != 0:
            return
        # paires actives : COOLING / IMPULSE (prêtes à trader) — pas les WATCH/QUIET
        active = [
            p
            for p in self.pairs
            if (self.scores.get(p) or {}).get("regime") in ("COOLING", "IMPULSE")
        ]
        if not active:
            return
        # BTC 1× par probe (pas par paire) — corrélation avec les signaux
        try:
            self.btc_prev = self.btc_price
            self.btc_price = last_price("BTCUSDT")
        except Exception:
            pass
        btc_delta_pct = 0.0
        if self.btc_prev > 0 and self.btc_price > 0:
            btc_delta_pct = (self.btc_price - self.btc_prev) / self.btc_prev * 100.0
        active = active[: self.aspiration_max_pairs]
        for pair in active:
            try:
                price = last_price(pair)
            except Exception:
                price = 0.0
            try:
                a = aspiration_sense(
                    pair,
                    http_json,
                    delay_s=self.aspiration_delay_s,
                    min_notional_usdt=self.aspiration_min_notional,
                )
            except Exception as e:
                # fail-open : jamais de blocage, on garde la lecture précédente
                a = {"ok": False, "reason": f"probe_err:{e}", "partial": True}
            if not a.get("ok"):
                continue

            # === spoof « rétractable à maintenant » (Christophe) ===
            # mur fond (drop ≥ 15%/s) puis reconstruit à l'identique à la lecture suivante → spoof.
            # Pas de timer : l'état est réévalué à CHAQUE échantillon ; dès que le mur reste
            # fondu (ou change de niveau), le signal redevient valide au tick suivant.
            spoof = False
            prev = self.aspiration_prev.get(pair)
            drop_now = max(
                abs(float(a.get("drop_bid_pct_per_s") or 0)),
                abs(float(a.get("drop_ask_pct_per_s") or 0)),
            )
            if prev and drop_now >= self.aspiration_spoof_drop:
                side = a.get("aspiration_side")
                if side == "BUY":
                    w_prev, w_now = prev.get("wall_ask_usdt", 0), float(a.get("wall_ask_usdt") or 0)
                elif side == "SELL":
                    w_prev, w_now = prev.get("wall_bid_usdt", 0), float(a.get("wall_bid_usdt") or 0)
                else:
                    w_prev, w_now = 0.0, 0.0
                # mur reconstruit à l'identique (±10%) alors qu'il venait de fondre → spoof
                if w_prev > 0 and abs(w_now - w_prev) / w_prev <= 0.10:
                    spoof = True
            self.aspiration_prev[pair] = {
                "wall_bid_usdt": float(a.get("wall_bid_usdt") or 0),
                "wall_ask_usdt": float(a.get("wall_ask_usdt") or 0),
                "ts": time.time(),
            }

            a["spoof"] = spoof
            a["price"] = price
            a["regime"] = (self.scores.get(pair) or {}).get("regime", "?")
            self.aspiration[pair] = a
            # calibration CSV — try/except + flush (check-up : ne pas mourir en silence
            # si le fichier est verrouillé, et ne pas perdre les dernières lignes au crash)
            try:
                with self.aspiration_csv.open("a", newline="") as f:
                    w = csv.writer(f)
                    w.writerow(
                        [
                            utc_now(), pair, a["regime"], a.get("aspiration_side"),
                            a.get("drop_bid_pct_per_s"), a.get("drop_ask_pct_per_s"),
                            a.get("max_drop_pct_per_s"), a.get("spread_bps"),
                            a.get("spread_delta_bps"), a.get("wall_bid_usdt"),
                            a.get("wall_ask_usdt"), a.get("notional_drop_ok"),
                            spoof, a.get("price_delta_pct"),
                            round(self.btc_price, 2), round(btc_delta_pct, 4),
                            a.get("delay_s"), price,
                        ]
                    )
                    f.flush()
            except Exception as e:
                say("err", f"[asp] CSV_WRITE_ERR {pair}: {e}")
            if not a.get("partial"):
                say(
                    "score",
                    f"[asp] {pair:12} side={a.get('aspiration_side'):4} "
                    f"drop={a.get('max_drop_pct_per_s'):6.2f}%/s "
                    f"Δspread={a.get('spread_delta_bps'):+5.1f}bps "
                    f"notional={a.get('notional_drop_ok')} spoof={spoof}",
                )

    def arm_reentry(self, pair: str, price: float, high: float):
        if not self.reentry_on:
            return
        peak = max(price, float(high or price))
        self.reentry[pair] = {
            "peak": peak,
            "exit": price,
            "ts": time.time(),
            "armed": utc_now(),
        }
        print(
            paint(
                C.REENTRY,
                f"[{utc_now()}] REENTRY  armé {pair}  peak={peak:.6f}  "
                f"besoin dump≥{self.reentry_dd}%  ttl={int(self.reentry_ttl)}s",
            )
        )

    def maybe_reentry(self, pair: str, price: float, sc: dict) -> bool:
        """Racheter plus bas après un dump post-exit. True si buy fait."""
        if not self.reentry_on or pair not in self.reentry or pair in self.pos:
            return False
        info = self.reentry[pair]
        if time.time() - float(info["ts"]) > self.reentry_ttl:
            del self.reentry[pair]
            return False
        peak = float(info["peak"])
        if peak <= 0:
            return False
        dd = (1.0 - price / peak) * 100.0
        if dd < self.reentry_dd:
            return False
        ok, why = self.sense_ok(pair, sc, "IMPULSE")
        if not ok:
            print(paint(C.WARN, f"[{utc_now()}] REENTRY skip {pair} sense={why}"))
            return False
        vok, vwhy = self.vol_ok_for_entry(sc, "IMPULSE")
        if not vok:
            print(paint(C.WARN, f"[{utc_now()}] REENTRY skip {pair} {vwhy}"))
            return False
        self.buy(
            pair,
            price,
            sc,
            f"reentry_dump_dd={dd:.1f}>={self.reentry_dd} from={peak:.6f}",
        )
        self.reentry.pop(pair, None)
        return True

    def log(self, pair, event, regime, price, entry, qty, pnl, cadence, reason):
        with self.csv_path.open("a", newline="") as f:
            csv.writer(f).writerow(
                [
                    utc_now(),
                    pair,
                    event,
                    regime,
                    f"{price:.8f}",
                    f"{entry:.8f}" if entry else "",
                    f"{qty:.8f}" if qty else "",
                    f"{pnl:.4f}",
                    f"{self.pnl_total:.4f}",
                    f"{cadence:.2f}" if cadence is not None else "",
                    reason,
                ]
            )

    def save_state(self):
        self.state_path.write_text(
            json.dumps(
                {
                    "ts": utc_now(),
                    "pnl_total": self.pnl_total,
                    "notional_live": self.current_notional(),
                    "base_notional": self.base_notional,
                    "trades": self.trades,
                    "positions": self.pos,
                    "bags": self.bags,
                    "bag_dca": self.bag_dca,
                    "pair_cash": self.pair_cash,
                    "reentry": self.reentry,
                    "scores": self.scores,
                    "pairs": self.pairs,
                },
                indent=2,
            )
        )

    def _fmt_vol(self, usdt: float) -> str:
        if usdt >= 1_000_000:
            return f"{usdt/1e6:.1f}M$"
        if usdt >= 1000:
            return f"{usdt/1e3:.0f}k$"
        return f"{usdt:.0f}$"

    def format_radar_lines(self, pair: str, s: dict) -> list[str]:
        """Radar : régime + trade/bag/cash + volume."""
        reg = s.get("regime", "?")
        vx = float(s.get("vol_spike") or 0)
        vflag = s.get("vol_flag", "?")
        small = "SMALL" if s.get("is_small_cap") else "liq"
        line1 = (
            f"  {pair:12} {reg:12} cad={s['cadence_pct']:5.1f}% "
            f"r15={s['range15_pct']:6.1f}% dd15={s['dd15_pct']:5.1f}% "
            f"m6={s['move6_pct']:5.1f}% dip={s['dip_pct']} rip={s['rip_pct']}"
        )
        cash = float(self.pair_cash.get(pair, 0.0))
        line_vol = (
            f"               vol24={self._fmt_vol(float(s.get('vol24_usdt') or 0))} "
            f"vx={vx:.2f}x [{vflag}/{small}] "
            f"next_mise={self.current_notional():.2f}$"
            + (f"  cash={cash:.2f}$" if cash > 0 else "")
        )
        lines_out = [line1, line_vol]
        # Sonde aspiration (mode observation) : dernière lecture par paire
        if self.aspiration_on and pair in self.aspiration:
            a = self.aspiration[pair]
            side = a.get("aspiration_side", "NONE")
            drop = float(a.get("max_drop_pct_per_s") or 0)
            dsp = float(a.get("spread_delta_bps") or 0)
            spoof = " SPOOF" if a.get("spoof") else ""
            nok = "" if a.get("notional_drop_ok") else " <500$"
            lines_out.append(
                f"               asp={side:4} drop={drop:6.2f}%/s "
                f"Δspread={dsp:+5.1f}bps{nok}{spoof}"
            )
        price = float(s.get("price") or 0)

        if pair in self.pos and price > 0:
            p = self.pos[pair]
            entry = float(p["entry"])
            qty = float(p["qty"])
            stake = float(p.get("stake") or entry * qty)
            value = price * qty
            target = stake * self.double_mult
            upnl = (price - entry) * qty
            pct = (price / entry - 1.0) * 100.0
            lines_out.append(
                f"               pos=TRADE mise={stake:.2f}$ now={value:.2f}$ "
                f"cible_2x={target:.2f}$ uPnL={upnl:+.4f}$ ({pct:+.1f}%) "
                f"| vend 50% à {self.double_mult:.0f}×"
            )
        elif pair in self.reentry:
            info = self.reentry[pair]
            lines_out.append(
                f"               pos=REENTRY_WAIT peak={float(info['peak']):.6f} "
                f"need_dump≥{self.reentry_dd:.0f}%"
            )
        else:
            lines_out.append("               pos=FLAT")

        if pair in self.bags and price > 0:
            b = self.bags[pair]
            be = float(b["entry"])
            bq = float(b["qty"])
            value = price * bq
            bupnl = (price - be) * bq
            bpct = (price / be - 1.0) * 100.0
            lines_out.append(
                f"               bag=HOUSE value={value:.2f}$ entry={be:.6f} "
                f"uPnL={bupnl:+.4f}$ ({bpct:+.1f}%) "
                f"| lent−{self.bag_slow_dd:.0f}% DCA / crash−{self.bag_crash_dd:.0f}% vend "
                f"{self.bag_crash_sell_frac*100:.0f}%"
            )
        elif pair in self.bag_dca:
            d = self.bag_dca[pair]
            sp = float(d["sell_px"])
            need = sp * (1.0 - self.bag_dca_dd / 100.0)
            lines_out.append(
                f"               bag=DCA_WAIT sell@{sp:.6f} rebuy≤{need:.6f} "
                f"notion={float(d['notional']):.2f}$"
            )
        else:
            lines_out.append("               bag=—")

        return lines_out

    def refresh_scores(self):
        say("score", f"[{utc_now()}] score régimes…")
        for pair in self.pairs:
            try:
                self.scores[pair] = score_pair(pair, self.cfg)
                s = self.scores[pair]
                reg = s["regime"]
                rc = {
                    "IMPULSE": C.IMPULSE,
                    "IMPULSE_WAIT": C.IMPULSE,
                    "COOLING": C.COOLING,
                    "WATCH": C.WATCH,
                    "QUIET": C.QUIET,
                }.get(reg, C.SCORE)
                for line in self.format_radar_lines(pair, s):
                    print(paint(rc, line))
            except Exception as e:
                say("err", f"  {pair} SCORE_ERR (retry next): {e}")
            time.sleep(0.35)
        self.save_state()

    def buy(self, pair: str, price: float, sc: dict, reason: str, notion: Optional[float] = None):
        """Pleine mise (100%). Pas de bag 15% à l'entrée."""
        if pair in self.pos or pair in self.bags:
            return
        regime = sc.get("regime", "")
        # Kill-switch global : veille muette → pas de nouvel achat (l'existant est géré)
        stale, sreason = veille_stale(RUNS, max_age_hours=self.veille_stale_h)
        if stale:
            say("warn", f"[{utc_now()}] STANDBY | {pair} | {sreason} (pas de nouvel achat)")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"STANDBY:{sreason}",
            )
            return
        # v1.5 : cooldown post-stop + skip RED veille (soft, fail-open)
        allowed, code, detail = entry_gate_check(
            RUNS,
            pair,
            cooldown_hours=self.stop_cooldown_h,
            skip_red=self.veille_skip_red,
            window_min=self.veille_window_min,
            refresh_sec=self.veille_refresh_sec,
        )
        if not allowed:
            say("warn", f"[{utc_now()}] {code} | {pair} | {detail}")
            self.log(
                pair,
                "SKIP",
                regime,
                price,
                price,
                0.0,
                0.0,
                sc.get("cadence_pct"),
                f"{code}:{detail}",
            )
            return
        ok, why = self.sense_ok(pair, sc, regime)
        if not ok:
            say("warn", f"[{utc_now()}] BUY skip {pair} sense={why}")
            return
        if self.is_bag(pair):
            bag_open = sum(1 for p in self.pos if self.is_bag(p))
            if bag_open >= self.bag_max_positions:
                say("warn", f"[{utc_now()}] BAG MAX {pair} ({bag_open}/{self.bag_max_positions})")
                self.log(
                    pair, "SKIP", regime, price, price, 0.0, 0.0,
                    sc.get("cadence_pct"), f"BAG_MAX:{bag_open}",
                )
                return
        trade_n = float(notion) if notion is not None else self.current_notional()
        if self.is_bag(pair):
            trade_n = trade_n * self.bag_position_mult
        if self.tier(pair) == "B":
            trade_n = trade_n * self.tier_b_position_mult  # famille 16/08 : tier B = taille microscopique
        if trade_n < 1.0:
            return
        # famille 16/08 : garde spread au buy (même tier A) — paires mal classées (ex. QAIT 327 bps)
        inv_spread = float((self.inv.get(pair) or {}).get("spread_bps") or 0.0)
        if inv_spread > self.buy_spread_max:
            say("warn", f"[{utc_now()}] BUY skip {pair} spread={inv_spread:.0f}bps > {self.buy_spread_max:.0f}")
            return
        # famille 16/08 : re-entry borné — max REENTRY_MAX par paire après un stop
        if self.reentry_count.get(pair, 0) >= self.reentry_max:
            say("warn", f"[{utc_now()}] REENTRY_MAX {pair} ({self.reentry_count.get(pair, 0)}/{self.reentry_max})")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"REENTRY_MAX:{self.reentry_count.get(pair, 0)}",
            )
            return
        trade_qty = trade_n / price
        self.pos[pair] = {
            "entry": price,
            "qty": trade_qty,
            "qty_init": trade_qty,
            "stake": trade_n,
            "ts": utc_now(),
            "regime": regime,
            "rip": sc["rip_pct"],
            "stop": sc["stop_pct"],
            "cadence": sc["cadence_pct"],
            "notional": trade_n,
            "high": price,
            "tension": sc.get("tension"),
            "sense_spread": (sc.get("sense") or {}).get("spread_bps"),
        }
        self.log(
            pair, "BUY", regime, price, price, trade_qty, 0.0, sc["cadence_pct"], reason
        )
        cible = trade_n * self.double_mult
        say(
            "buy",
            f"[{utc_now()}] BUY   MISE {pair}  px={price:.6f}  "
            f"mise={trade_n:.2f}$  → vend 50% quand valeur≥{cible:.2f}$  "
            f"regime={regime}  ({reason})",
        )

    def sell_trade(self, pair: str, price: float, reason: str, qty: Optional[float] = None):
        """Vend qty du TRADE (pas du bag). Retourne proceeds USDT."""
        if pair not in self.pos:
            return 0.0
        p = self.pos[pair]
        entry = p["entry"]
        full_qty = p["qty"]
        sell_qty = full_qty if qty is None else min(qty, full_qty)
        if sell_qty <= 0:
            return 0.0
        proceeds = price * sell_qty
        pnl = (price - entry) * sell_qty
        self.pnl_total += pnl
        self.trades += 1
        event = "SELL" if sell_qty >= full_qty * 0.999 else "SELL_PARTIAL"
        inv_spread = float((self.inv.get(pair) or {}).get("spread_bps") or 0.0)
        self.log(
            pair,
            event,
            p.get("regime", ""),
            price,
            entry,
            sell_qty,
            pnl,
            p.get("cadence"),
            f"{reason} tier={self.tier(pair)} spread={inv_spread:.1f}bps",
        )
        kind = "sell_ok" if pnl >= 0 else "sell_ko"
        tag = "EXIT" if event == "SELL" else "EXIT_PART"
        say(
            kind,
            f"[{utc_now()}] {tag:10} {pair}  px={price:.6f}  "
            f"pnl={pnl:+.4f}$  cash≈{proceeds:.2f}$  total={self.pnl_total:+.4f}$  ({reason})",
        )
        # famille 16/08 : compteur re-entry — incrémenté à chaque fermeture, reset si gain
        if event == "SELL":
            if pnl >= 0:
                self.reentry_count[pair] = 0
            else:
                self.reentry_count[pair] = self.reentry_count.get(pair, 0) + 1
        # v1.5 : cache stop uniquement (pas stake_out / partial)
        if event == "SELL" and str(reason).lower().startswith("stop"):
            record_stop(RUNS, pair, utc_now())
            say(
                "warn",
                f"[{utc_now()}] STOP_CACHE | {pair} | cooldown={self.stop_cooldown_h:.0f}h",
            )
        left = full_qty - sell_qty
        high = float(p.get("high") or price)
        if left <= full_qty * 0.001:
            self.pos.pop(pair, None)
            self.arm_reentry(pair, price, high)
        else:
            p["qty"] = left
        return proceeds

    def stake_out_half(self, pair: str, price: float):
        """Valeur ≥ 2× mise → vend 50%. Cash = mise récupérée ; reste = BAG maison."""
        p = self.pos[pair]
        entry = float(p["entry"])
        qty = float(p["qty"])
        stake = float(p.get("stake") or entry * qty)
        sell_qty = qty * self.stake_sell_frac
        keep_qty = qty - sell_qty
        regime = p.get("regime", "")
        cad = p.get("cadence")
        proceeds = self.sell_trade(
            pair,
            price,
            f"stake_out_{self.double_mult:.0f}x_sell_{self.stake_sell_frac*100:.0f}pct",
            qty=sell_qty,
        )
        self.add_pair_cash(pair, proceeds)
        if keep_qty > 0:
            self.bags[pair] = {
                "entry": price,
                "qty": keep_qty,
                "ts": utc_now(),
                "note": "house_after_stake_out",
                "stake_ref": stake,
                "high": price,
            }
            self.pos.pop(pair, None)
            self.log(
                pair,
                "BAG_ARM",
                regime,
                price,
                price,
                keep_qty,
                0.0,
                cad,
                f"house_half_after_{self.double_mult:.0f}x",
            )
            say(
                "bag",
                f"[{utc_now()}] BAG   ARM   {pair}  px={price:.6f}  "
                f"house≈{price*keep_qty:.2f}$  cash_récupéré≈{proceeds:.2f}$  "
                f"(mise {stake:.2f}$ sortie)",
            )

    def manage_bag(self, pair: str, price: float, sc: dict):
        """Bag maison : crash→90% ; lent→DCA."""
        regime = (sc or {}).get("regime", "")

        if pair in self.bags:
            b = self.bags[pair]
            entry = float(b["entry"])
            if entry <= 0:
                return
            b["high"] = max(float(b.get("high") or entry), price)
            dd = (1.0 - price / entry) * 100.0
            qty = float(b["qty"])

            if dd >= self.bag_crash_dd:
                sell_qty = qty * self.bag_crash_sell_frac
                keep_qty = qty - sell_qty
                pnl = (price - entry) * sell_qty
                proceeds = price * sell_qty
                self.pnl_total += pnl
                self.trades += 1
                self.add_pair_cash(pair, proceeds)
                self.log(
                    pair,
                    "BAG_CRASH",
                    regime,
                    price,
                    entry,
                    sell_qty,
                    pnl,
                    (sc or {}).get("cadence_pct"),
                    f"crash_dd={dd:.1f}>={self.bag_crash_dd:.0f}_sell_{self.bag_crash_sell_frac*100:.0f}pct",
                )
                say(
                    "sell_ko",
                    f"[{utc_now()}] BAG   CRASH {pair}  dd={dd:.1f}%  "
                    f"vend {self.bag_crash_sell_frac*100:.0f}%  pnl={pnl:+.4f}$  "
                    f"cash+{proceeds:.2f}$  keep={keep_qty:.6f}",
                )
                if keep_qty * price < 0.5:
                    del self.bags[pair]
                else:
                    b["qty"] = keep_qty
                    b["entry"] = price
                return

            if self.bag_dca_on and dd >= self.bag_slow_dd:
                pnl = (price - entry) * qty
                proceeds = price * qty
                self.pnl_total += pnl
                self.trades += 1
                self.log(
                    pair,
                    "BAG_SELL",
                    regime,
                    price,
                    entry,
                    qty,
                    pnl,
                    (sc or {}).get("cadence_pct"),
                    f"slow_dd={dd:.1f}>={self.bag_slow_dd:.0f}_arm_dca",
                )
                say(
                    "bag",
                    f"[{utc_now()}] BAG   SELL  {pair}  dd={dd:.1f}% (lent)  "
                    f"pnl={pnl:+.4f}$  → DCA −{self.bag_dca_dd:.0f}%",
                )
                self.bag_dca[pair] = {
                    "sell_px": price,
                    "notional": proceeds,
                    "ts": time.time(),
                }
                del self.bags[pair]
            return

        if pair not in self.bag_dca:
            return
        info = self.bag_dca[pair]
        if time.time() - float(info["ts"]) > self.bag_dca_ttl:
            self.add_pair_cash(pair, float(info["notional"]))
            say("warn", f"[{utc_now()}] BAG DCA TTL {pair} → cash={info['notional']:.2f}$")
            del self.bag_dca[pair]
            return
        sell_px = float(info["sell_px"])
        dd = (1.0 - price / sell_px) * 100.0
        if dd < self.bag_dca_dd:
            return
        notion = float(info["notional"])
        qty = notion / price
        self.bags[pair] = {
            "entry": price,
            "qty": qty,
            "ts": utc_now(),
            "note": "dca_rebuy",
            "high": price,
        }
        self.log(
            pair,
            "BAG_DCA",
            regime,
            price,
            price,
            qty,
            0.0,
            (sc or {}).get("cadence_pct"),
            f"dca_dd={dd:.1f}>={self.bag_dca_dd:.0f}",
        )
        say(
            "bag",
            f"[{utc_now()}] BAG   DCA   {pair}  px={price:.6f}  "
            f"cost={notion:.2f}$  (encore −{dd:.1f}% sous sell)",
        )
        del self.bag_dca[pair]

    def manage_open(self, pair: str, price: float):
        """Trade : 2× → stake-out ; sinon stop."""
        p = self.pos[pair]
        entry = float(p["entry"])
        qty = float(p["qty"])
        stake = float(p.get("stake") or entry * qty)
        p["high"] = max(float(p.get("high") or entry), price)
        value = price * qty
        chg = (price / entry - 1.0) * 100.0

        if value >= stake * self.double_mult:
            self.stake_out_half(pair, price)
            return

        if not (self.is_bag(pair) and self.bag_no_tech_stop):
            if chg <= -float(p.get("stop") or 6):
                proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_avant_2x")
                self.add_pair_cash(pair, proceeds)
                return

            # 16/08 soir (Christophe) : RIP scale-out 2 paliers — « une pierre trois coups »
            # XRP/HBAR (liquides) : P1=+2%, P2=+6% · reste (small caps) : P1=+6%, P2=+8%
            # Chaque palier vend 25% de la quantité INITIALE → runner garde 50% pour le gros mouvement.
            early = pair in self.rip_early_pairs
            palier1 = self.rip_early_p1 if early else self.rip_late_p1
            palier2 = self.rip_early_p2 if early else self.rip_late_p2
            rip_step = int(p.get("rip_step") or 0)  # 0 = rien vendu, 1 = palier 1 vendu
            rip_next = palier1 if rip_step == 0 else (palier2 if rip_step == 1 else None)
            if rip_next is not None and chg >= rip_next:
                rip_ok = True
                if self.tier(pair) == "B":
                    inv_spread = float((self.inv.get(pair) or {}).get("spread_bps") or 0.0)
                    rip_ok = inv_spread <= self.tier_b_spread_max  # tier B illiquide : pas de rip si spread énorme
                if rip_ok:
                    p["rip_step"] = rip_step + 1
                    qty_init = float(p.get("qty_init") or qty)
                    sell_qty = qty_init * self.rip_scaleout_frac  # 25% de la quantité INITIALE par palier
                    if sell_qty >= qty * 0.001:
                        proceeds = self.sell_trade(
                            pair,
                            price,
                            f"rip_{chg:.1f}pct_palier{rip_step+1}_sell_{self.rip_scaleout_frac*100:.0f}pct",
                            qty=sell_qty,
                        )
                        self.add_pair_cash(pair, proceeds)

    def maybe_redeploy_cash(self, pair: str, price: float, sc: dict) -> bool:
        """Cash paire + dip → remets 100% du cash."""
        if not self.cash_redeploy_on:
            return False
        if pair in self.pos or pair in self.bags or pair in self.bag_dca:
            return False
        cash = float(self.pair_cash.get(pair, 0.0))
        if cash < 2.0:
            return False
        regime = sc.get("regime", "")
        if regime not in ("COOLING", "IMPULSE"):
            return False
        vok, _ = self.vol_ok_for_entry(sc, regime)
        if not vok:
            return False
        if regime == "COOLING":
            need = sc.get("cool_entry_pct", sc["dip_pct"])
            if sc["dd15_pct"] < need:
                return False
        elif regime == "IMPULSE":
            need = sc.get("impulse_entry_pct", max(sc["dip_pct"], 5.0))
            if sc["dd6_pct"] < need:
                return False
        taken = self.take_pair_cash(pair)
        if taken < 2.0:
            return False
        say(
            "reentry",
            f"[{utc_now()}] CASH  REDEPLOY {pair}  {taken:.2f}$ (100% cash paire)",
        )
        self.buy(pair, price, sc, f"cash_redeploy_{taken:.2f}", notion=taken)
        return pair in self.pos

    def vol_ok_for_entry(self, sc: dict, regime: str) -> tuple[bool, str]:
        if sc.get("pair") and self.is_bag(str(sc.get("pair"))):
            return True, "vol_ok_bag"  # Classe B : pas de filtre volume (accumulation sur périodes sèches)
        if not sc.get("is_small_cap"):
            return True, "vol_ok_liq"
        vx = float(sc.get("vol_spike") or 0)
        flag = sc.get("vol_flag", "?")
        need = self.vol_spike_min_small
        if regime == "COOLING":
            need = max(1.0, need * 0.85)
        if vx < need:
            return False, f"vol_dry_vx={vx:.2f}<{need:.2f}_{flag}"
        if flag in ("DEAD", "DRY") and "IMPULSE" in (regime or ""):
            return False, f"vol_{flag}_impulse_block"
        return True, f"vol_ok_vx={vx:.2f}_{flag}"

    def maybe_enter(self, pair: str, price: float, sc: dict):
        if self.maybe_redeploy_cash(pair, price, sc):
            return
        regime = sc["regime"]
        if regime in ("QUIET", "WATCH", "IMPULSE_WAIT"):
            return
        if pair in self.pos or pair in self.bags:
            return
        vok, vwhy = self.vol_ok_for_entry(sc, regime)
        if not vok:
            say("warn", f"[{utc_now()}] BUY skip {pair} {vwhy}")
            return
        if regime == "COOLING":
            need = sc.get("cool_entry_pct", sc["dip_pct"])
            dd = sc["dd15_pct"]
            if dd >= need:
                self.buy(pair, price, sc, f"cooling_dd15={dd:.1f}>={need:.1f}")
            return
        if regime == "IMPULSE":
            need = sc.get("impulse_entry_pct", max(sc["dip_pct"], 5.0))
            if sc["dd6_pct"] >= need and sc["move6_pct"] >= float(
                self.cfg.get("IMPULSE_PCT", "8")
            ):
                self.buy(
                    pair,
                    price,
                    sc,
                    f"impulse_pullback_dd6={sc['dd6_pct']:.1f}>={need:.1f} m6={sc['move6_pct']:.1f}",
                )
            return

    def tick_pair(self, pair: str):
        price = last_price(pair)
        sc = self.scores.get(pair)
        if not sc:
            return
        sc["price"] = price
        if sc.get("peak6"):
            sc["dd6_pct"] = round((1.0 - price / sc["peak6"]) * 100.0, 2)
        if sc.get("peak24"):
            sc["dd24_pct"] = round((1.0 - price / sc["peak24"]) * 100.0, 2)
        if sc.get("peak15"):
            sc["dd15_pct"] = round((1.0 - price / sc["peak15"]) * 100.0, 2)

        try:
            self.manage_bag(pair, price, sc)
        except Exception as e:
            say("err", f"[{utc_now()}] BAG_ERR {pair}: {e}")

        if pair in self.pos:
            self.manage_open(pair, price)
            return

        if self.maybe_reentry(pair, price, sc):
            return

        self.maybe_enter(pair, price, sc)

    def seed_inventory(self) -> None:
        """Place ~SEED_USDT en tokens paper dès le boot — pour tester les ventes baissières."""
        if not self.seed_on or self.seed_usdt < 1.0:
            return
        budget = float(self.seed_usdt)
        targets: list[str] = []
        for pair in self.pairs:
            if pair in self.pos:
                continue
            try:
                px = last_price(pair)
            except Exception:
                continue
            if px and px > 0:
                targets.append(pair)
            if self.seed_mode == "single":
                break
            if len(targets) >= self.seed_max_pairs:
                break
        if not targets:
            say("warn", f"[{utc_now()}] SEED skip — aucune paire avec prix")
            return
        per = budget / len(targets)
        say(
            "hdr",
            f"SEED inventaire {budget:.2f}$ → {len(targets)} paire(s) "
            f"({per:.2f}$ chacune) — réalisme vente baissière",
        )
        for pair in targets:
            try:
                price = last_price(pair)
            except Exception as e:
                say("err", f"SEED fail {pair}: {e}")
                continue
            if not price or price <= 0:
                continue
            # score minimal pour rip/stop (sinon manage_open plante)
            sc = self.scores.get(pair) or {}
            if not sc:
                try:
                    self.refresh_scores()
                    sc = self.scores.get(pair) or {}
                except Exception:
                    sc = {}
            trade_n = per
            trade_qty = trade_n / price
            regime = sc.get("regime") or "SEED"
            self.pos[pair] = {
                "entry": price,
                "qty": trade_qty,
                "qty_init": trade_qty,
                "stake": trade_n,
                "ts": utc_now(),
                "regime": regime,
                "rip": float(sc.get("rip_pct") or self.cfg.get("RIP_FLOOR_PCT", "2")),
                "stop": float(sc.get("stop_pct") or self.cfg.get("STOP_FLOOR_PCT", "6")),
                "cadence": float(sc.get("cadence_pct") or 0),
                "notional": trade_n,
                "high": price,
                "tension": sc.get("tension"),
                "sense_spread": None,
                "seed": True,
            }
            self.log(
                pair,
                "BUY",
                regime,
                price,
                price,
                trade_qty,
                0.0,
                sc.get("cadence_pct"),
                "SEED_START",
            )
            say(
                "buy",
                f"[{utc_now()}] SEED  {pair}  px={price:.6f}  "
                f"mise={trade_n:.2f}$  qty={trade_qty:.6f}  "
                f"(déjà en tokens — vendeable)",
            )
        self.save_state()

    def seed_bags(self) -> None:
        """Bag de départ (paper) : ~SEED_BAGS_USDT en bags maison dès le boot.

        Entrée seedée ~SEED_BAGS_ENTRY_DD_PCT% au-dessus du prix → bandeau DCA actif
        immédiatement (BAG_SELL + DCA armé dès le 1er tick = test de la boucle bag jour 1).
        flag seed:true (réalisme paper, ne pollue pas l'analyse du PnL).
        """
        if not self.seed_bags_on or self.seed_bags_usdt < 1.0:
            return
        targets = [p for p in self.pairs if p in self.seed_bags_pairs and p not in self.bags]
        if not targets:
            return
        prices = {}
        for pair in targets:
            try:
                px = last_price(pair)
            except Exception:
                px = None
            if px and px > 0:
                prices[pair] = px
        if not prices:
            say("warn", f"[{utc_now()}] SEED_BAGS skip — aucune paire avec prix")
            return
        per = self.seed_bags_usdt / len(prices)
        for pair, px in prices.items():
            entry = px * (1.0 + self.seed_bags_dd / 100.0)  # entrée seedée au-dessus → dd immédiat
            qty = per / entry
            self.bags[pair] = {
                "entry": entry,
                "qty": qty,
                "stake": per,
                "ts": utc_now(),
                "high": px,
                "seed": True,
            }
            say(
                "bag",
                f"[{utc_now()}] SEED_BAG {pair}  {per:.2f}$  entry={entry:.6f} "
                f"(dd={self.seed_bags_dd:.0f}% actif) → boucle bag testable dès maintenant",
            )

    def refresh_cortana_pilot(self):
        """Contrat Cortana : lire/valider/logguer (ADVISORY = pas appliqué < 60%)."""
        try:
            pending, applied, warns = process_pilot(self.cortana_pilot, default_mode=self.cortana_mode)
        except Exception as e:
            say("warn", f"[{utc_now()}] cortana_pilot ERR: {e}")
            return
        self.cortana_pending = pending
        self.cortana_applied = applied
        for w in warns:
            say("warn", f"[{utc_now()}] cortana: {w}")
        if applied:
            say("heart", f"[{utc_now()}] cortana PILOT AUTO → {applied}")
        elif pending:
            say("heart", f"[{utc_now()}] cortana PILOT ADVISORY → {len(pending)} proposition(s)")

    def run(self) -> int:
        say(
            "hdr",
            "=== HULK PAPER v1.5 — mise→2×→bag | cooldown stop | skip RED veille ===",
        )
        print(f"pairs={','.join(self.pairs)}")
        print(
            f"MISE_BASE={self.base_notional}$  "
            f"SEED={'ON '+str(self.seed_usdt)+'$' if self.seed_on else 'OFF'}  "
            f"STAKE_OUT={self.double_mult:.0f}×→sell {self.stake_sell_frac*100:.0f}%  "
            f"BAG crash−{self.bag_crash_dd:.0f}%→{self.bag_crash_sell_frac*100:.0f}%  "
            f"lent−{self.bag_slow_dd:.0f}% DCA  "
            f"COMPOUND={'ON' if self.compound_on else 'OFF'} "
            f"POLL={self.poll}s"
        )
        print(
            f"GATES: STOP_COOLDOWN={self.stop_cooldown_h:.0f}h  "
            f"VEILLE_SKIP_RED={'ON' if self.veille_skip_red else 'OFF'}  "
            f"window={self.veille_window_min}m  "
            f"cache={RUNS / '.hulk_stop_cache.json'}  "
            f"status={RUNS / '.veille_status.json'}"
        )
        print(f"csv={self.csv_path}")
        print(f"stop: Ctrl+C ou touch {STOP_FILE}")
        print("ACE NUAGE genesis non touché.")
        legend()
        self.refresh_scores()
        self.refresh_cortana_pilot()
        self.seed_inventory()
        self.seed_bags()
        n = 0
        while self.alive:
            if STOP_FILE.exists():
                say("warn", f"[{utc_now()}] STOP_PAPER détecté")
                break
            if n > 0 and n % self.score_every == 0:
                self.refresh_scores()
                self.refresh_cortana_pilot()
            # Sonde aspiration (mode observation) : paires actives, toutes les N cycles
            self.probe_aspiration(n)
            for pair in self.pairs:
                try:
                    self.tick_pair(pair)
                except Exception as e:
                    say("err", f"[{utc_now()}] ERR {pair}: {e}")
            n += 1
            if n % 3 == 0:
                open_n = len(self.pos)
                bags_n = len(self.bags)
                cash_n = sum(1 for v in self.pair_cash.values() if v > 0)
                cash_sum = sum(self.pair_cash.values())
                notion = self.current_notional()
                regimes = ",".join(
                    f"{p[0]}:{self.scores.get(p,{}).get('regime','?')[:3]}"
                    for p in self.pairs[:5]
                )
                _stale, _sreason = veille_stale(RUNS, max_age_hours=self.veille_stale_h)
                standby = f" | STANDBY({_sreason})" if _stale else ""
                _bag_open = sum(1 for p in self.pos if self.is_bag(p))
                say(
                    "heart",
                    f"[{utc_now()}] heartbeat open={open_n} bags={bags_n} "
                    f"dca={len(self.bag_dca)} cash_pairs={cash_n}({cash_sum:.1f}$) "
                    f"mise={notion:.2f}$ trades={self.trades} "
                    f"pnl={self.pnl_total:+.4f}$ | {regimes}{standby} "
                    f"cortana={len(self.cortana_pending)} bag={_bag_open}/{self.bag_max_positions}",
                )
                self.save_state()
            time.sleep(self.poll)
        self.save_state()
        say(
            "hdr",
            f"[{utc_now()}] FIN paper trades={self.trades} pnl={self.pnl_total:+.4f}$ "
            f"bags={len(self.bags)} cash={sum(self.pair_cash.values()):.2f}$",
        )
        if self.bags:
            say("bag", "Bags maison :")
            for p, b in self.bags.items():
                say("bag", f"  {p} qty={b['qty']:.6f} entry={b['entry']:.6f}")
        return 0


def main() -> int:
    cfg = load_env(CFG)
    if cfg.get("MODE", "paper") != "paper":
        print("MODE doit être paper pour ce script")
        return 2
    inv = load_inventory()
    pairs = pick_pairs(cfg, inv)
    return PaperBot(cfg, pairs, inv).run()


if __name__ == "__main__":
    sys.exit(main())
