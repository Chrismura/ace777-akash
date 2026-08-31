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
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# FIX CRITIQUE 28/08 : timeout global sur les sockets (connect inclus)
# Sans ça, urlopen bloque indéfiniment sur SYN_SENT (macOS Darwin)
# — le SIGALRM ne délivre PAS le signal pendant connect() bloquant.
socket.setdefaulttimeout(30)

# capteurs F1-like (module local Hulk — pas ACE genesis)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ace_sense_mexc import aspiration_sense, book_sense, entry_gate, tension_score  # noqa: E402
from veille_gates import entry_gate_check, record_stop, veille_stale  # noqa: E402
from cortana_contract import process_pilot  # noqa: E402
from circuit_breaker import TradeCircuitBreaker, CircuitOpenException  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "defaults.env"
INV = ROOT / "data" / "universe_mexc_inventory.csv"
RUNS = ROOT / "runs"
STOP_FILE = ROOT / "STOP_PAPER"

# Profils comportementaux par paire (universe_profils.json, 27/08 GO Christophe).
# Chaque crypto a SON caractère : murs, spoof, drop, spread, ET désormais ses
# propres seuils dip/rip/stop (volatilité réelle 30j). Chargé une fois en cache
# module-level pour que score_pair (fonction, pas méthode) puisse y accéder sans
# relire le disque à chaque cycle.
_PROFILS_CACHE: dict[str, dict] | None = None


def _profils() -> dict[str, dict]:
    global _PROFILS_CACHE
    if _PROFILS_CACHE is not None:
        return _PROFILS_CACHE
    _PROFILS_CACHE = {}
    p = ROOT / "strategie" / "universe_profils.json"
    try:
        if p.exists():
            data = json.loads(p.read_text())
            for k, v in data.items():
                if k in ("version", "updated", "note"):
                    continue
                if isinstance(v, dict) and "calib" in v:
                    _PROFILS_CACHE[k] = v
    except Exception:
        _PROFILS_CACHE = {}
    return _PROFILS_CACHE


def mode_entree(pair: str) -> str:
    """Mode d'entrée configuré pour la paire (calib). Vide = défaut (COOLING+IMPULSE).

    Set-up régime (30/08, GO Christophe) : `mode_entree = "IMPULSE"` signifie que la
    paire ne s'achète QUE quand le moteur la voit en régime IMPULSE (allumage de rafale
    + pullback) — jamais en COOLING/WATCH/QUIET. Découverte EDEL : cet actif ne bouge
    que par rafales IMPULSE (m6 70% vs 4%), donc entrer hors rafale = acheter du mort."""
    return str(((_profils().get(pair) or {}).get("calib") or {}).get("mode_entree") or "")
# Kill-switch global : même sémantique que la veilleuse (touch → tous les bots s'arrêtent)
STOP_ALL = Path.home() / "ace777-test-day1" / "Index_Maison" / "STOP_ALL"

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


class _AlarmTimeout(Exception):
    """Levée par SIGALRM quand un black-hole SYN bloque la connexion."""


def _alarm_handler(signum, frame):
    raise _AlarmTimeout(f"SIGALRM {signum}")


def http_json(url: str, timeout: float = 15.0, retries: int = 2):
    """GET JSON avec retries (timeouts MEXC fréquents).

    Ceinture SIGALRM (24/08, leçon black-hole du 23/08) : le timeout socket
    d'urllib ne se déclenche PAS sur un SYN black-hole (vu en réel : process
    bloqué 5 min en SYN_SENT sur api.mexc.com, watchdog impuissant car le
    process est vivant). signal.alarm coupe à coup sûr, quel que soit l'état
    du connect().

    Phase 1 (31/08, famille 7/7 + codeur) : timeout ramené de 40s à 15s et
    retries ramenés de 4 à 2 (1 appel + 1 seul retry) — un prix qui met >15s
    est périmé de toute façon. Backoff exponentiel court UNIQUEMENT sur HTTP
    429 (rate-limit) / 5xx ; en cas de timeout réseau pur on ne martèle pas
    (l'appelant a son fallback cache).
    """
    last_err: Optional[Exception] = None
    for attempt in range(max(1, retries)):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hulk-paper/1.0"})
            prev = signal.signal(signal.SIGALRM, _alarm_handler)
            signal.alarm(int(timeout) + 2)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return json.loads(r.read().decode())
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, prev)
        except (
            _AlarmTimeout,
            urllib.error.URLError,
            urllib.error.HTTPError,
            TimeoutError,
            OSError,
        ) as e:
            last_err = e
            code = getattr(e, "code", None)
            rate_or_srv = code == 429 or (isinstance(code, int) and code >= 500)
            if rate_or_srv:
                # seul cas où l'on re-essaie avec backoff exponentiel (1s, 2s)
                time.sleep(1.0 * (attempt + 1))
            else:
                time.sleep(0.3 * (attempt + 1))
    assert last_err is not None
    raise last_err


# ---------------------------------------------------------------------------
# BATCH PRIX (Phase 1, 31/08 — famille 7/7 + codeur). Le moteur faisait 21
# appels GET single-pair par cycle (~200-270 req/min vs limite MEXC ~200).
# Désormais 1 appel GET /ticker/price (le marché entier) au début de chaque
# cycle, filtré sur les paires suivies, stocké en cache. last_price lit ce
# cache (0 appel réseau en régime normal) ; si une paire est absente/batch
# échoué → fallback GET unitaire ciblé ; dernier prix connu en dernier recours.
# Aucune logique métier n'est touchée (mêmes valeurs de prix, juste la source).
_PRICE_CACHE: dict[str, float] = {}
_LAST_KNOWN_PRICE: dict[str, float] = {}


def fetch_all_prices(pairs) -> dict[str, float]:
    """1 appel batch → prix des paires demandées (MEXC renvoie tout le marché,
    `symbols` ignoré — testé 31/08). Peuple le cache + le dernier connu."""
    out: dict[str, float] = {}
    try:
        data = http_json("https://api.mexc.com/api/v3/ticker/price")
    except Exception:
        return out
    if isinstance(data, list):
        wanted = set(pairs)
        for item in data:
            if not isinstance(item, dict):
                continue
            s = item.get("symbol")
            if s not in wanted:
                continue
            try:
                out[s] = float(item["price"])
            except (TypeError, ValueError):
                continue
    global _PRICE_CACHE, _LAST_KNOWN_PRICE
    _PRICE_CACHE = out
    for k, v in out.items():
        _LAST_KNOWN_PRICE[k] = v
    return out


def _est_vierge(st: dict) -> bool:
    """True si l'état est un re-seed VIERGE (aucune activité réelle) : 0 trade,
    aucun cash de paire, pnl ≈ 0, pas de bags ni bag_dca. Un tel état est un
    artefact de re-seed après coupure — pas les bags accumulés à reprendre."""
    if int(st.get("trades") or 0) > 0:
        return False
    cash = st.get("pair_cash") or {}
    if any(v and v > 0 for v in cash.values()):
        return False
    if abs(float(st.get("pnl_total") or 0.0)) > 0.01:
        return False
    if st.get("bags") or st.get("bag_dca"):
        return False
    return True


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
    # Régime normal : le prix vient du cache batch du cycle (0 appel réseau).
    p = _PRICE_CACHE.get(pair)
    if p is not None:
        return p
    # Paire absente du batch (delistée / non renvoyée) → fallback GET unitaire ciblé.
    try:
        q = urllib.parse.urlencode({"symbol": pair})
        j = http_json(f"https://api.mexc.com/api/v3/ticker/price?{q}")
        p = float(j["price"])
        _PRICE_CACHE[pair] = p
        _LAST_KNOWN_PRICE[pair] = p
        return p
    except Exception:
        if pair in _LAST_KNOWN_PRICE:
            return _LAST_KNOWN_PRICE[pair]
        raise


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
    """Régime + cadence + sniff volume (15j 1h).

    27/08 (2e passe) : les seuils de DÉTECTION (impulsion/refroidissement)
    viennent AUSSI du profil par paire — sinon BTC/ETH (banc de preuve) avec
    les floors globaux (impulsion 8%, refroidissement 6%) ne déclencheraient
    JAMAIS : un banc de preuve qui ne trade pas ne teste rien."""
    _cal = (_profils().get(pair) or {}).get("calib") or {}
    quiet_min = float(cfg.get("QUIET_RANGE_PCT", "8"))
    spike_15 = float(cfg.get("SPIKE_15D_PCT", "25"))
    impulse_th = float(_cal.get("impulse_pct", cfg.get("IMPULSE_PCT", "8")))
    cooling_dd = float(_cal.get("cooling_dd_pct", cfg.get("COOLING_DD_MIN_PCT", "6")))

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
    change24 = None  # vrai % 24h (priceChangePercent MEXC) — pour l'affichage cockpit
    try:
        t24 = ticker_24h(pair)
        vol24 = float(t24.get("quote_vol") or 0)
        if t24.get("price"):
            price = float(t24["price"])
            dd15 = ((1.0 - price / peak15) * 100.0) if peak15 > 0 else dd15
        change24 = t24.get("change_pct")
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

    # seuils adaptés à la cadence, avec plancher PAR PAIRE (profil 27/08) :
    # chaque crypto a SON setup — XRP ne se trade pas comme QAIT. Le profil
    # (dip_pct/rip_pct/stop_pct, volatilité réelle 30j) prime ; repli sur les
    # floors globaux si la paire n'a pas de profil (fail-open).
    dip_floor = float(_cal.get("dip_pct", cfg.get("DIP_FLOOR_PCT", "2.5")))
    rip_floor = float(_cal.get("rip_pct", cfg.get("RIP_FLOOR_PCT", "1.5")))
    stop_floor = float(_cal.get("stop_pct", cfg.get("STOP_FLOOR_PCT", "4.0")))
    dip = max(dip_floor, cadence * float(cfg.get("DIP_CADENCE_MULT", "0.45")))
    rip = max(rip_floor, cadence * float(cfg.get("RIP_CADENCE_MULT", "0.35")))
    stop = max(stop_floor, cadence * float(cfg.get("STOP_CADENCE_MULT", "0.70")))

    had_spike = range15 >= spike_15 or move24 >= impulse_th
    impulse_now = move6 >= impulse_th or move24 >= impulse_th * 1.2
    # COOLING strict : vrai spike 15j + drawdown significatif (pas un micro -2%)
    cooling = had_spike and dd15 >= cooling_dd and not (impulse_now and dd6 < 1.0)
    quiet = range15 < quiet_min and move24 < quiet_min * 0.6

    # pullback min pour entrer (fraction du range 15j, floor cooling_dd)
    cool_entry = max(
        cooling_dd,
        dip,
        range15 * float(_cal.get("cooling_pullback_frac", cfg.get("COOLING_PULLBACK_FRAC", "0.25"))),
    )
    impulse_entry = max(
        dip,
        float(_cal.get("impulse_pullback_min_pct", cfg.get("IMPULSE_PULLBACK_MIN_PCT", "5"))),
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
        "change24_pct": change24,
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
        # SPEC v2 SELL FULL (29/08) — garde-fou amplitude + verrou 3 (config réversible)
        self.sell_full_amplitude_guard = float(cfg.get("SELL_FULL_AMPLITUDE_GUARD", "12.0"))
        self.sell_full_require_invalidation = int(cfg.get("SELL_FULL_REQUIRE_INVALIDATION", "1"))
        self.sell_full_guard_degraded = int(cfg.get("SELL_FULL_GUARD_DEGRADED", "1"))
        self.dust_sweep_min_notional = float(cfg.get("DUST_SWEEP_MIN_NOTIONAL", "1.0"))
        self.sell_partial_cascade = int(cfg.get("SELL_PARTIAL_CASCADE", "1"))
        self.reentry_max = max(1, int(float(cfg.get("REENTRY_MAX", "1"))))
        self.reentry_count: dict[str, int] = {}
        # Bag de départ (test boucle bag dès le 1er jour) — 15/08 Christophe
        self.seed_bags_on = cfg.get("SEED_BAGS_ON", "1").strip() not in ("0", "false", "False")
        self.seed_bags_usdt = float(cfg.get("SEED_BAGS_USDT", "10"))
        self.seed_bags_dd = float(cfg.get("SEED_BAGS_ENTRY_DD_PCT", "8"))
        self.seed_bags_pairs = {
            p.strip().upper() for p in (cfg.get("SEED_BAGS_PAIRS") or "CCUSDT").split(",") if p.strip()
        }
        # FIX 30/08 (Buffy) : mode OBSERVE-ONLY — paires journalisées en continu
        # (score, murs, poussière, régimes, indices → croisement_contexte.jsonl)
        # mais BLOQUÉES de toute entrée/trade. C'est l'intention originelle de
        # PAPER_WATCH_PAIRS, qui ne capturait RIEN. Ici on garde la richesse des
        # données SANS que Hulk ne mette de positions (erreur corrigée 30/08).
        self.observe_only = {
            p.strip().upper()
            for p in (cfg.get("PAPER_OBSERVE_PAIRS") or "").split(",")
            if p.strip()
        }
        self.cortana_mode = (cfg.get("CORTANA_MODE", "ADVISORY") or "ADVISORY").strip().upper()
        self.cortana_pilot = ROOT / (cfg.get("CORTANA_PILOT_FILE") or "strategie/cortana_pilot.json")
        self.cortana_pending: list = []
        self.cortana_applied: dict = {}
        self.sense_on = cfg.get("SENSE_ON", "1").strip() not in ("0", "false", "False")
        # Phase 2 (31/08, famille) : carnet en cache TTL — on relit le depth d'une
        # paire au plus 1×/SENSE_CACHE_TTL_SEC (rotation). Les décisions d'une
        # paire sont bien plus espacées que 45s, le cache ne change pas la logique
        # mais divise les appels carnet par ~20 (le gros résiduel réseau).
        self.sense_cache: dict[str, tuple[float, dict]] = {}
        self.sense_cache_ttl = float(cfg.get("SENSE_CACHE_TTL_SEC", "45"))
        self.vol_spike_min_small = float(cfg.get("VOL_SPIKE_MIN_SMALL", "1.5"))
        # === Sonde aspiration (16/08, mode OBSERVATION 48h — zéro effet sur les entrées) ===
        # Consensus codeur 4/4 + famille 6/6 + Cortana : double lecture du carnet (pattern V8 ACE),
        # log + radar + calibration CSV, SANS agir sur le moteur. Fail-open sur timeout MEXC.
        self.aspiration_on = cfg.get("ASPIRATION_ON", "1").strip() not in ("0", "false", "False")
        # Phase 3 (31/08) : source de l'aspiration/murs. "fichier" = le satellite
        # écrit runs/aspiration_live.json (le cœur LIT, 0 appel depth) ; "inline" =
        # comportement historique (probe fait ses propres appels). Réversible à chaud
        # via ASPIRATION_SRC dans defaults.env (relu au démarrage).
        self.aspiration_src = (cfg.get("ASPIRATION_SRC", "fichier") or "fichier").strip().lower()
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
        # === DÉTECTEUR ACCUMULATION 24H (28/08, GO Christophe — OBSERVATION SEULE) ===
        # Thèse validée sur 12j de données aspiration : descente ≥ 2% (30 min) + prise
        # du mur SUD (drop_bid ≥ 5%/s, mur ≥ 2000$) → +24h : win 58%, R:R 3.7 (échantillon
        # concentré sur 2 jours haussiers → à confirmer). ZÉRO effet trade : on journalise
        # chaque candidat + suivi +6h/+24h dans runs/accumulation_signal.jsonl.
        self.acc_px_mem: dict[str, list[tuple[float, float]]] = {}  # pair -> [(ts, prix)] 30 min
        self.acc_open: dict[str, dict] = {}  # pair -> {ts0, px0, suivi} candidat en cours
        self.acc_acc1 = float(cfg.get("ACCUM_DESCENTE_PCT", "2.0"))
        self.acc_drop = float(cfg.get("ACCUM_DROP_PCT_S", "5.0"))
        self.acc_mur = float(cfg.get("ACCUM_MUR_USDT", "2000.0"))
        self.acc_memo = float(cfg.get("ACCUM_MEMO_SEC", "1800.0"))
        self.acc_signal_csv = RUNS / "accumulation_signal.jsonl"
        # === MURS DE LIQUIDITÉ (25/08, GO Christophe) — corrélation murs × BTC ===
        # Charge le rapport historique d'observer_murs.py pour scorer la force
        # de chaque paire (mur bid moyen/max, taux de spoof, taux de drop).
        self.murs_observations: dict[str, dict] = {}
        # Profils comportementaux par paire (universe_profils.json, 27/08 GO Christophe)
        # Chaque crypto a SON caractère : médiane de mur, spoof baseline, drops,
        # fenêtres horaires → wall_strength RELATIF + plafond de mise par profondeur.
        self.profils: dict[str, dict] = {}
        self._load_profils()
        self.wall_btc_prev: float = 0.0  # BTC price au tick précédent (détection choc)
        self.wall_melt_events: list[dict] = []  # murs qui fondent post-choc BTC
        self.gex_call_wall: float = 0.0  # call wall Deribit (mis à jour depuis live.json)
        # === CROISEMENT indices × murs (28/08, GO Christophe) — mode OBSERVATION, RÉVERSIBLE ===
        # Journalise le contexte (mur de la paire + poussière/SDI/pipeline_health) par paire
        # par cycle dans runs/croisement_contexte.jsonl. ZÉRO effet sur les entrées.
        # Interrupteur : strategie/croisement_config.json ({"on": false} désactive sans redémarrer).
        self.croisement_on: bool = False
        self._ctx_indices_cache: dict = {}
        self._ctx_indices_ts: float = 0.0
        self.gex_put_wall: float = 0.0
        self._load_wall_observations()
        # === CIRCUIT BREAKER (25/08) — bloque le trading si données stale ===
        # FIX 27/08 : TTL gex aligné sur la cadence RÉELLE du gex — thermo tourne
        # ~1h (écart moyen 55,9 min mesuré). Avec TTL 300 s, le circuit serait
        # ouvert en PERMANENCE (faux positif → Hulk ne traderait jamais).
        # 7200 s = 2h = marge x2 sur la cadence 1h (cohérent avec sante_index x2.5).
        # FIX 31/08 (Phase 3) : le TTL BTC doit épouser la cadence RÉELLE de la source
        # (même principe que le GEX ci-dessous). En mode inline, le cœur sonde le prix
        # chaque probe → TTL 10s cohérent. En mode fichier, le satellite écrit
        # aspiration_live.json avec un intervalle RÉEL de ~29s (StartInterval 20s + ~9s
        # d'exécution mesurés : 5 profondeurs de carnet). Le cœur n'accepte le fichier
        # que s'il a ≤45s (`frais` dans probe_aspiration) → on aligne le TTL sur cette
        # MÊME fenêtre (45s) pour éliminer les faux positifs par intermittence.
        _btc_ttl = 10.0 if self.aspiration_src != "fichier" else 45.0
        self.cb_btc = TradeCircuitBreaker(ttl_seconds=_btc_ttl, failure_threshold=3, cooldown_seconds=30.0)
        self.cb_gex = TradeCircuitBreaker(ttl_seconds=7200.0, failure_threshold=2, cooldown_seconds=60.0)
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
        # VERROU ANTI-DOUBLE-RUN (24/08, codeur) : fcntl.flock sur un fichier lock —
        # si une 2e instance démarre (watchdog pendant qu'un zombie traîne), elle
        # échoue immédiatement au lieu de doubler les ordres sur le compte réel.
        import fcntl
        self.lock_path = RUNS / ".paper_diprip.lock"
        self._lock_fd = open(self.lock_path, "w")
        try:
            fcntl.flock(self._lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            print("❌ Une autre instance de paper_diprip.py tourne déjà "
                  f"(verrou {self.lock_path}). Abandon.")
            sys.exit(3)
        self._lock_fd.write(str(os.getpid()))
        self._lock_fd.flush()
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

    def get_pipeline_health_mult(self) -> float:
        """Lit pipeline_health.json et retourne le multiplicateur de taille (0-1)."""
        try:
            health_file = Path(__file__).parent.parent.parent / "Index_Maison" / "data" / "pipeline_health.json"
            if health_file.exists():
                health = json.loads(health_file.read_text(encoding="utf-8"))
                return float(health.get("position_multiplier", 1.0))
        except Exception:
            pass
        return 1.0  # Défaut = nominal

    def get_cortana_recommendation(self) -> dict:
        """Lit cortana_analysis.json et retourne la recommandation.
        Fraîcheur : l'analyzer tourne toutes les 5 min → TTL 30 min (6 cycles manqués).
        Si le fichier est stale, retourne niveau 'stale' pour l'afficher honnêtement."""
        try:
            analysis_file = Path(__file__).parent.parent.parent / "Index_Maison" / "data" / "cortana_analysis.json"
            if analysis_file.exists():
                analysis = json.loads(analysis_file.read_text(encoding="utf-8"))
                ts = analysis.get("timestamp", 0)
                if isinstance(ts, str):
                    ts = 0
                if time.time() - float(ts) > 1800:  # TTL 30 min
                    return {"niveau": "stale", "action": "STALE", "lecture": "", "resume": ""}
                # Prendre l'analyse la PLUS SÉVÈRE (pas la dernière)
                analyses = analysis.get("analyses", [])
                sev = {"critique": 0, "dangereux": 1, "surveiller": 2, "haussier": 3, "neutre": 4, "inconnu": 5}
                if analyses:
                    best = min(analyses, key=lambda a: sev.get(a.get("niveau", "inconnu"), 5))
                    return {
                        "niveau": best.get("niveau", "inconnu"),
                        "action": best.get("action", "Observer"),
                        "lecture": best.get("interpretation", {}).get("lecture", ""),
                        "resume": analysis.get("resume", "")
                    }
        except Exception:
            pass
        return {"niveau": "inconnu", "action": "Observer", "lecture": "", "resume": ""}

    def current_notional(self) -> float:
        """Taille trade : base + fraction du PnL réalisé (compound), plafonnée, × health."""
        if not self.compound_on:
            self.notional = self.base_notional
        else:
            grown = self.base_notional + max(0.0, self.pnl_total) * self.compound_frac
            if self.pnl_total < 0:
                grown = max(self.base_notional * 0.5, self.base_notional + self.pnl_total * 0.25)
            cap = self.base_notional * self.compound_max_mult
            self.notional = min(max(grown, self.base_notional * 0.5), cap)
        # Appliquer le multiplicateur pipeline health
        health_mult = self.get_pipeline_health_mult()
        self.notional *= health_mult
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

    # === MURS DE LIQUIDITÉ — scoring & corrélation BTC (25/08) ===

    def _load_wall_observations(self):
        """Charge murs_observations.json (produit par observer_murs.py).
        Donne par paire : bid_avg_usd, bid_max_usd, spoof_pct, drop_n.
        """
        murs_path = ROOT / "runs" / "murs_observations.json"
        if not murs_path.exists():
            return
        try:
            data = json.loads(murs_path.read_text())
            for p in data.get("top_murs", []):
                sym = p.get("pair", "")
                if not sym:
                    continue
                self.murs_observations[sym] = {
                    "bid_moy": float(p.get("bid_avg_usd") or 0),
                    "bid_max": float(p.get("bid_max_usd") or 0),
                    "ask_moy": float(p.get("ask_avg_usd") or 0),
                    "n": int(p.get("n") or 0),
                    "spoof_rate": float(p.get("spoof_pct") or 0),
                    "drop_rate": float(p.get("drop_n") or 0),
                }
            say("hdr", f"[murs] {len(self.murs_observations)} paires chargées depuis {murs_path.name}")
        except Exception as e:
            say("err", f"[murs] chargement échoué: {e}")

    def _load_croisement_config(self) -> None:
        """Charge l'interrupteur du croisement indices × murs (28/08, GO Christophe).
        RÉVERSIBLE : strategie/croisement_config.json avec on:true/false — relu à
        chaque cycle (léger), donc on peut couper SANS redémarrer le moteur.
        Fail-open : config absente/invalide → off (zéro changement de comportement).
        """
        try:
            cfg_path = ROOT / "strategie" / "croisement_config.json"
            if cfg_path.exists():
                self.croisement_on = bool(json.loads(cfg_path.read_text()).get("on"))
        except Exception:
            self.croisement_on = False

    def _ctx_indices(self) -> dict:
        """Lit les indices globaux (poussière/SDI/pipeline_health) avec cache TTL 60 s.
        Fail-open total : tout échec de lecture → champ absent, jamais d'exception.
        Chemins : Index_Maison/data/ (produits par les agents launchd).
        """
        now = time.time()
        if self._ctx_indices_cache and (now - self._ctx_indices_ts) < 60:
            return self._ctx_indices_cache
        idx: dict = {}
        base = Path(__file__).resolve().parents[2] / "Index_Maison" / "data"
        try:
            p = base / "bloc_privatise.json"
            if p.exists():
                d = json.loads(p.read_text())
                idx["poussiere_taux_fantome"] = d.get("taux_fantome")
                idx["poussiere_nb_cachees"] = d.get("nb_tx_cachees")
        except Exception:
            pass
        try:
            p = base / "sdi_latest.json"
            if p.exists():
                d = json.loads(p.read_text())
                sdi_obj = d.get("sdi")
                idx["sdi"] = sdi_obj.get("sdi") if isinstance(sdi_obj, dict) else sdi_obj
                idx["ipt"] = d.get("ipt")
                idx["rbf"] = d.get("rbf")
                idx["fee_pressure"] = d.get("fee_pressure")
        except Exception:
            pass
        try:
            p = base / "pipeline_health.json"
            if p.exists():
                d = json.loads(p.read_text())
                idx["pipeline_mult"] = d.get("position_multiplier")
                idx["pipeline_score"] = d.get("global_score")
        except Exception:
            pass
        if self.gex_call_wall > 0:
            idx["gex_call_wall"] = self.gex_call_wall
        self._ctx_indices_cache = idx
        self._ctx_indices_ts = now
        return idx

    def log_contexte(self, pair: str, sc: dict, price: float) -> None:
        """Journalise le contexte de décision : mur de la paire + indices globaux.
        Mode OBSERVATION (28/08, GO Christophe) : append-only dans
        runs/croisement_contexte.jsonl, ZÉRO effet sur les entrées. RÉVERSIBLE via
        croisement_config.json (relu à chaque cycle).
        """
        if not self.croisement_on:
            return
        try:
            m = self.murs_observations.get(pair) or {}
            ligne = {
                "ts": int(time.time()),
                "utc": utc_now(),
                "pair": pair,
                "price": round(float(price), 6),
                "regime": (sc or {}).get("regime"),
                "m6_pct": (sc or {}).get("move6_pct"),
                "dd15_pct": (sc or {}).get("dd15_pct"),
                "wall_strength": self.wall_strength(pair),
                "mur_bid_moy_usd": m.get("bid_moy"),
                "mur_bid_max_usd": m.get("bid_max"),
                "mur_n_mesures": m.get("n"),
                "mur_spoof_pct": m.get("spoof_rate"),
            }
            ligne.update(self._ctx_indices())
            with open(ROOT / "runs" / "croisement_contexte.jsonl", "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
        except Exception:
            pass  # fail-open : le croisement ne doit JAMAIS casser le moteur

    def _load_profils(self) -> None:
        """Charge universe_profils.json (profils comportementaux par paire).
        Fail-open : si absent, Hulk garde l'ancienne normalisation absolue.
        """
        profils_path = ROOT / "strategie" / "universe_profils.json"
        if not profils_path.exists():
            return
        try:
            data = json.loads(profils_path.read_text())
            for k, v in data.items():
                if k in ("version", "updated", "note"):
                    continue
                if isinstance(v, dict) and "calib" in v:
                    self.profils[k] = v
            say("hdr", f"[profils] {len(self.profils)} profils comportementaux chargés ({profils_path.name})")
        except Exception as e:
            say("err", f"[profils] chargement échoué: {e}")

    def wall_strength(self, pair: str) -> float:
        """Score 0-1 de la force du mur bid d'une paire.
        1 = mur épais, stable, peu de spoof.
        0 = mur inexistant ou de façade.
        Fix 27/08 (GO Christophe) : normalisation RELATIVE au profil de la paire
        (universe_profils.json) — XRP 84k$ est NORMAL pour XRP, EDEL 909$ est
        NORMAL pour EDEL. On juge le mur actuel vs SA médiane, plus l'absolu.
        """
        m = self.murs_observations.get(pair)
        if not m or m["n"] < 50:
            return 0.5  # pas assez de données = neutre
        prof = self.profils.get(pair) or {}
        med = prof.get("mur_bid_med")
        # Mur de référence : live (sonde) si dispo, sinon moyenne historique
        asp = self.aspiration.get(pair) or {}
        live_wall = float(asp.get("wall_bid_usdt") or 0)
        bid_ref = live_wall if live_wall > 0 else float(m.get("bid_moy") or 0)
        if med and med > 0:
            bid_score = min(bid_ref / med, 1.0)  # relatif à SA médiane
        else:
            bid_score = min(bid_ref / 30_000, 1.0)  # repli absolu (pas de profil)
        # Pénalité spoof (0-1, plus spoof = plus bas)
        spoof_penalty = 1.0 - min(m["spoof_rate"] / 10.0, 0.5)  # max -50%
        # Bonus drop_rate (les drops = signal ACE, ça montre de l'activité)
        drop_bonus = 1.0 + min(m["drop_rate"] / 500, 0.2)  # max +20%
        return max(0.1, min(1.0, bid_score * spoof_penalty * drop_bonus))

    def wall_mult(self, pair: str) -> float:
        """Multiplicateur de taille de position basé sur la force du mur.
        Mur solide (score 0.8+) → ×1.2 (plus gros).
        Mur fragile (score <0.3) → ×0.6 (plus petit).
        """
        s = self.wall_strength(pair)
        if s >= 0.7:
            return 1.2
        elif s >= 0.4:
            return 1.0
        else:
            return 0.6

    def check_wall_melt(self, pair: str):
        """Détection post-choc : si BTC a chuté >$150 et que le mur bid fond >20% →
        signal d'alerte (la liquidité retire)."""
        asp = self.aspiration.get(pair) or {}
        if not asp or self.btc_prev <= 0 or self.btc_price <= 0:
            return
        btc_delta = self.btc_price - self.btc_prev
        if btc_delta > -150:  # pas assez de choc
            return
        # Comparer le mur bid actuel au précédent
        prev = self.aspiration_prev.get(pair)
        if not prev:
            return
        wall_now = float(asp.get("wall_bid_usdt") or 0)
        wall_prev = float(prev.get("wall_bid_usdt") or 0)
        if wall_prev <= 0 or wall_now <= 0:
            return
        melt_pct = (wall_now - wall_prev) / wall_prev * 100
        if melt_pct < -20:  # mur fond de >20%
            event = {
                "ts": utc_now(),
                "pair": pair,
                "btc_delta": round(btc_delta, 2),
                "wall_prev": round(wall_prev, 2),
                "wall_now": round(wall_now, 2),
                "melt_pct": round(melt_pct, 1),
            }
            self.wall_melt_events.append(event)
            say("warn", f"[MUR-FOND] {pair} mur bid {wall_prev:.0f}→{wall_now:.0f}"
                f" ({melt_pct:+.0f}%) post-choc BTC {btc_delta:+.0f}$")

    def check_gex_wall(self):
        """Vérifie si BTC approche le call wall GEX ($82K).
        Si BTC > 98% du call wall → signal 'squeeze imminent'.
        """
        if self.gex_call_wall <= 0 or self.btc_price <= 0:
            return
        dist_pct = (self.gex_call_wall - self.btc_price) / self.btc_price * 100
        if dist_pct <= 2.0 and dist_pct > 0:
            say("hdr", f"[GEX] BTC ${self.btc_price:,.0f} → call wall ${self.gex_call_wall:,.0f}"
                f" ({dist_pct:.1f}% de distance) — SQUEEZE IMMINENT")
        elif dist_pct <= 0:
            say("hdr", f"[GEX] BTC ${self.btc_price:,.0f} A DÉPASSÉ le call wall"
                f" ${self.gex_call_wall:,.0f} — SQUEEZE ACTIF")

    def tier(self, pair: str) -> str:
        return (self.inv.get(pair) or {}).get("tier", "A")

    def is_bag(self, pair: str) -> bool:
        """Classe B (small caps bag) : règles d'exception."""
        return pair in self.bag_pairs

    def sense_ok(self, pair: str, sc: dict, regime: str) -> tuple[bool, str]:
        if not self.sense_on:
            return True, "sense_off"
        # Phase 2 (31/08) : carnet en cache TTL. Première lecture = appels réels ;
        # ensuite on réutilise le book tant qu'il dure < SENSE_CACHE_TTL_SEC. Si le
        # cache/la lecture échoue → sense_ok bloque (comportement conservateur intact).
        now = time.time()
        cached = self.sense_cache.get(pair)
        if cached and (now - cached[0]) < self.sense_cache_ttl:
            sense = cached[1]
        else:
            try:
                sense = book_sense(pair, http_json)
                self.sense_cache[pair] = (now, sense)
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
        # Phase 3 (31/08, GO Christophe) : mode FICHIER. Le satellite_aspiration.py
        # tourne en continu et écrit runs/aspiration_live.json (atomique). On LIT ce
        # fichier au lieu de sonder le carnet soi-même → moins d'appels réseau dans le
        # cœur + isolation des pannes réseau. RÉVERSIBLE via ASPIRATION_SRC (fichier|inline).
        # Si le fichier est absent / stale (>45s), on retombe en inline (fallback sûr).
        if self.aspiration_src == "fichier":
            try:
                live = json.loads((RUNS / "aspiration_live.json").read_text(encoding="utf-8"))
                frais = (int(live.get("ts") or 0) and
                         (time.time() - int(live.get("ts") or 0)) <= 45)
                if frais:
                    for pair, a in (live.get("paires") or {}).items():
                        if a.get("ok"):
                            self.aspiration[pair] = dict(a)
                    btc_p = float(live.get("btc_price") or 0)
                    if btc_p > 0:
                        self.btc_prev = self.btc_price
                        self.btc_price = btc_p
                        try:
                            self.cb_btc.validate(
                                {"timestamp": int(live.get("ts") or 0), "price": btc_p},
                                source="btc",
                            )
                        except CircuitOpenException:
                            say("warn", "[CB] BTC stale (satellite) — entrées bloquées")
                    return
            except Exception:
                pass
        # paires actives : COOLING / IMPULSE (prêtes à trader) — pas les WATCH/QUIET
        active = [
            p
            for p in self.pairs
            if (self.scores.get(p) or {}).get("regime") in ("COOLING", "IMPULSE")
        ]
        if not active:
            return
        # BTC 1× par probe (pas par paire) — corrélation avec les signaux
        # FIX 27/08 : cb_btc était défini mais JAMAIS validé (seule sa status()
        # s'affichait au heartbeat). La doc 25/08 promettait « vérifie la fraîcheur
        # btc (TTL 10s) avant de trader ». Maintenant : fetch OK → validate frais,
        # fetch KO → fail compté → circuit s'ouvre après failure_threshold.
        try:
            self.btc_prev = self.btc_price
            self.btc_price = last_price("BTCUSDT")
            self.cb_btc.validate(
                {"timestamp": time.time(), "price": self.btc_price}, source="btc"
            )
        except CircuitOpenException:
            say("warn", f"[{utc_now()}] [CB] BTC injoignable — circuit ouvert, entrées bloquées")
        except Exception:
            try:
                self.cb_btc.validate({"timestamp": 0, "price": 0}, source="btc")
            except CircuitOpenException:
                say("warn", f"[{utc_now()}] [CB] BTC stale ×3 — circuit ouvert, entrées bloquées")
        btc_delta_pct = 0.0
        if self.btc_prev > 0 and self.btc_price > 0:
            btc_delta_pct = (self.btc_price - self.btc_prev) / self.btc_prev * 100.0
        # GEX refresh (1× par probe) — call/put wall Deribit
        try:
            live_path = Path(__file__).resolve().parents[2] / "Index_Maison" / "thermo" / "live.json"
            if live_path.exists():
                live = json.loads(live_path.read_text())
                gex = live.get("gex", {})
                if gex.get("ok"):
                    # FIX 27/08 : le timestamp était time.time() = TOUJOURS frais →
                    # le circuit ne s'ouvrait jamais. On valide avec le ts RÉEL de
                    # live.json (dernier run thermo) : si live.json est vieux > TTL
                    # (300 s), le circuit s'ouvre et les murs GEX sont gelés.
                    gex_ts = float(live.get("tsUnix") or live_path.stat().st_mtime or 0)
                    gex_data = {
                        "timestamp": gex_ts,
                        "price": gex.get("callWall", 0),
                    }
                    try:
                        self.cb_gex.validate(gex_data, source="gex")
                        self.gex_call_wall = float(gex.get("callWall", 0) or 0)
                        self.gex_put_wall = float(gex.get("putWall", 0) or 0)
                    except CircuitOpenException:
                        say("warn", f"[CB] GEX stale — garde les murs précédents")
        except Exception:
            pass
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
            # === DÉTECTEUR ACCUMULATION 24H (28/08, OBSERVATION SEULE — aucun trade) ===
            self.detecter_accumulation(pair, a, price)

    def detecter_accumulation(self, pair: str, a: dict, price: float):
        """Journalise les candidats accumulation 24h (thèse Christophe, validée sur
        12j de données : descente ≥ 2% + prise mur SUD → +24h win 58%, R:R 3.7).
        OBSERVATION : aucun ordre, aucun effet moteur — on écrit runs/accumulation_signal.jsonl
        avec le suivi +6h/+24h pour confirmer l'edge sur un échantillon varié."""
        ts = time.time()
        # 1) mémoire des prix (~30 min) pour la descente
        mem = self.acc_px_mem.setdefault(pair, [])
        if price > 0:
            mem.append((ts, price))
            cutoff = ts - self.acc_memo
            while mem and mem[0][0] < cutoff:
                mem.pop(0)
        # 2) suivi des candidats déjà ouverts (+6h/+24h)
        cand = self.acc_open.get(pair)
        if cand:
            if cand["px0"] > 0 and price > 0:
                chg = (price / cand["px0"] - 1) * 100
                if not cand.get("m6") and ts >= cand["ts0"] + 6 * 3600:
                    cand["m6"] = round(chg, 2)
                if not cand.get("m24") and ts >= cand["ts0"] + 24 * 3600:
                    cand["m24"] = round(chg, 2)
                    self._write_acc_signal(cand)
                    del self.acc_open[pair]
                    return
        # 3) détection d'un nouveau signal
        if cand:
            return  # un candidat déjà en cours sur cette paire (pas de spam)
        drop_bid = float(a.get("drop_bid_pct_per_s") or 0)
        wall_bid = float(a.get("wall_bid_usdt") or 0)
        if drop_bid < self.acc_drop or wall_bid < self.acc_mur:
            return
        if len(mem) < 5:
            return
        descente = (mem[-1][1] / mem[0][1] - 1) * 100 if mem[0][1] else 0
        if descente > -self.acc_acc1:
            return
        # spoof ? (mur reconstruit) — on ne journalise pas les manipulations
        spoof = bool(a.get("spoof"))
        self.acc_open[pair] = {
            "ts0": ts, "ts": utc_now(), "pair": pair,
            "px0": round(price, 8),
            "descente_avant_pct": round(descente, 2),
            "drop_bid_pct_s": round(drop_bid, 2),
            "mur_bid_usdt": round(wall_bid, 0),
            "spoof": spoof, "m6": None, "m24": None,
        }
        say("hdr", f"[ACCUM] {pair} signal descente {descente:.1f}% + prise mur "
                   f"{wall_bid:,.0f}$ ({drop_bid:.1f}%/s) — OBSERVATION (suivi +6h/+24h)")

    def _write_acc_signal(self, cand: dict):
        try:
            with self.acc_signal_csv.open("a", encoding="utf-8") as f:
                f.write(json.dumps(cand, ensure_ascii=False) + "\n")
        except Exception as e:
            say("err", f"[ACCUM] write_err {e}")

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
        # SET-UP RÉGIME (30/08) : mode_entree="IMPULSE" → re-entry UNIQUEMENT en IMPULSE.
        if mode_entree(pair) == "IMPULSE" and sc.get("regime") != "IMPULSE":
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
        # Écriture ATOMIQUE (24/08, codeur) : .tmp puis os.replace — jamais d'état
        # à moitié écrit si le Mac coupe en plein save (corruption JSON au resume).
        import tempfile
        data = json.dumps(
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
                "wall_melt_events": self.wall_melt_events[-50:],  # garder les 50 derniers
            },
            indent=2,
        )
        fd, tmp_path = tempfile.mkstemp(dir=str(self.state_path.parent), text=True)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(data)
            os.replace(tmp_path, self.state_path)
            # Pointeur canonique (24/08, fix resume) : le DERNIER état réellement
            # sauvegardé, quel que soit le nom du run. Résout la collision de nom
            # de run (2 démarrages dans la même seconde → même state_path → le
            # 2e voyait « son propre état » et re-seedait au lieu de reprendre).
            try:
                (RUNS / ".hulk_resume_pointer").write_text(
                    self.state_path.name, encoding="utf-8"
                )
            except Exception:
                pass
        except Exception:
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
            raise

    def resume_state(self) -> bool:
        """Reprend le DERNIER état NON VIERGE (positions + bags + cash) au lieu
        de re-seed. --resume (24/08, Christophe : « tenir les positions pendant
        les coupures »). Retourne True si reprise faite. Le CSV/state_path
        restent neufs (traçabilité du run), mais l'ÉTAT (pos/bags/cash/pnl) est
        restauré.

        Sélection (24/08, 3e fix — un seed frais écrasait les bags accumulés et
        un score de substance favorisait un état ANCIEN plus riche) : on scanne
        du plus récent au plus ancien et on reprend le premier état qui a de la
        SUBSTANCE, c.-à-d. pas un re-seed vierge (0 trade + 0 cash + pnl ≈ 0 +
        pas de bags) et pas un état vide (0 position et 0 bag). Le plus récent
        état réel = la continuation d'aujourd'hui (ex. 3 trades du jour) — pas
        la régression vers un état d'hier, pas le re-seed d'après-coupure."""
        for f in sorted(RUNS.glob("PAPER_V1_*_state.json"), reverse=True):
            if f == self.state_path:
                continue  # le run courant n'a pas encore d'historique à reprendre
            try:
                st = json.loads(f.read_text(encoding="utf-8"))
            except Exception as e:
                say("err", f"RESUME fail lecture {f.name}: {e}")
                continue
            pos = st.get("positions") or {}
            if not pos and not (st.get("bags") or {}):
                continue  # état vide (0 pos, 0 bag) : pas candidat
            if _est_vierge(st):
                say("wrn", f"RESUME {f.name} = re-seed vierge (0 trade, 0 cash) — on cherche plus ancien")
                continue
            self.pos = {k: v for k, v in pos.items()}
            self.bags = st.get("bags") or {}
            self.bag_dca = st.get("bag_dca") or {}
            self.pair_cash = st.get("pair_cash") or {}
            self.reentry = st.get("reentry") or {}
            self.scores = st.get("scores") or {}
            self.pnl_total = float(st.get("pnl_total") or 0.0)
            self.trades = int(st.get("trades") or 0)
            self.wall_melt_events = st.get("wall_melt_events") or []
            # mémorise la source (pour log/audit) — sans toucher au state courant
            self.resume_source = f.name
            break  # premier état non vierge = le bon (du plus récent au plus ancien)
        # Copie l'ancien CSV dans le nouveau pour que le journal (cockpit) ait
        # l'historique complet des trades — sinon le journal est vide après un resume.
        ancien_csv = RUNS / f.name.replace("_state.json", ".csv")
        if ancien_csv.exists() and ancien_csv != self.csv_path:
            try:
                import shutil
                shutil.copy2(str(ancien_csv), str(self.csv_path))
            except Exception:
                pass
        say("hdr", f"RESUME depuis {f.name} — {len(self.pos)} pos, "
                   f"{len(self.bags)} bags, cash {sum(self.pair_cash.values()):.2f}$, "
                   f"pnl {self.pnl_total:+.4f}$, trades {self.trades}")
        return True
        return False

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

    # ─── Filtre lots MEXC (codeur, 27/08) ─────────────────────
    # baseSizePrecision = stepSize quantité · quoteAmountPrecision = pas du montant USDT
    # Fail-open : si l'API ne répond pas, on trade comme avant (paper ne bloque jamais).
    def lot_filter(self, pair: str):
        """Retourne (step_size, min_notional) pour une paire, ou (None, None) si inconnu."""
        if hasattr(self, "lot_cache") and pair in self.lot_cache:
            return self.lot_cache[pair]
        if not hasattr(self, "lot_cache"):
            self.lot_cache: dict = {}
        try:
            j = http_json("https://api.mexc.com/api/v3/exchangeInfo", timeout=15, retries=1)
            step, min_not = None, None
            for s in j.get("symbols", []):
                if s.get("symbol") == pair:
                    bsp = str(s.get("baseSizePrecision") or "")
                    try:
                        step = float(bsp) if bsp not in ("", "0") else 10.0 ** (-int(s.get("baseAssetPrecision", 2)))
                    except Exception:
                        step = 10.0 ** (-int(s.get("baseAssetPrecision", 2)))
                    try:
                        min_not = float(s.get("quoteAmountPrecision") or 1)
                    except Exception:
                        min_not = 1.0
                    break
            self.lot_cache[pair] = (step, min_not)
            return self.lot_cache[pair]
        except Exception:
            self.lot_cache[pair] = (None, None)
            return (None, None)

    @staticmethod
    def _floor_step(qty: float, step: Optional[float]):
        """Arrondit la quantité vers le bas au multiple du stepSize (jamais au-dessus)."""
        if not step or step <= 0 or qty <= 0:
            return qty
        return float(int(qty / step + 1e-9) * step)

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
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"SENSE:{why}",
            )
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
        # TAILLE ADAPTATIVE MURS (25/08, GO Christophe) : mur solide → ×1.2, mur fragile → ×0.6
        if notion is None:  # pas de cash_redeploy (déjà calibré)
            trade_n = trade_n * self.wall_mult(pair)
        # PLAFOND PAR PROFONDEUR DE MUR (27/08, GO Christophe) : jamais plus de X%
        # du mur médian de la paire — EDEL 909$ ne peut pas absorber 20$ sans
        # slippage, XRP 84k$ oui. Chaque crypto a SA capacité (profil).
        prof = self.profils.get(pair) or {}
        med = prof.get("mur_bid_med")
        if med:
            cap = med * float((prof.get("calib") or {}).get("mise_max_pct_mur", 0.02))
            if cap > 0 and trade_n > cap:
                say("heart", f"[{utc_now()}] {pair} mise {trade_n:.2f}$ → plafonnée {cap:.2f}$ (mur médian {med:,.0f}$)")
                trade_n = cap
        if trade_n < 1.0:
            return
        # famille 16/08 : garde spread au buy (même tier A) — paires mal classées (ex. QAIT 327 bps)
        inv_spread = float((self.inv.get(pair) or {}).get("spread_bps") or 0.0)
        if inv_spread > self.buy_spread_max:
            say("warn", f"[{utc_now()}] BUY skip {pair} spread={inv_spread:.0f}bps > {self.buy_spread_max:.0f}")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"SPREAD:{inv_spread:.0f}bps",
            )
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
        # Filtre lots MEXC (codeur, 27/08) : quantité au stepSize + minNotional
        step, min_not = self.lot_filter(pair)
        if step:
            trade_qty = self._floor_step(trade_qty, step)
            trade_n = trade_qty * price  # notional RÉEL sur le carnet (honnête)
            if min_not and trade_n < min_not:
                say("warn", f"[{utc_now()}] BUY skip {pair} notional {trade_n:.2f}$ < minNotional {min_not:.2f}$")
                self.log(
                    pair, "SKIP", regime, price, price, 0.0, 0.0,
                    sc.get("cadence_pct"), f"MIN_NOTIONAL:{min_not}",
                )
                return
        if trade_qty <= 0:
            say("warn", f"[{utc_now()}] BUY skip {pair} qty={trade_qty} (stepSize {step})")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"QTY:{trade_qty}",
            )
            return
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
        # Filtre lots MEXC (codeur, 27/08) : quantité au stepSize sur les sorties aussi
        step, _mn = self.lot_filter(pair)
        if step:
            rounded = self._floor_step(sell_qty, step)
            if rounded <= 0:
                # poussière : on sort tout (un solde < stepSize est invendable, on le ferme)
                rounded = full_qty
            if rounded < sell_qty:
                sell_qty = rounded
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
        """Trade : 2× → stake-out ; sinon stop.

        MODE TRAILING (28/08, pattern HUNTER du champion 61-82% win) : si le
        profil de la paire porte trail_arm_pct/trail_giveback_pct (banc de
        preuve BTC/ETH), on laisse courir le gagnant — stop fixe en backstop,
        sortie quand le prix redonne giveback sous le pic. Zéro 2× / zéro rip
        paliers (ils contrediraient le « laisser courir »)."""
        p = self.pos[pair]
        sc = self.scores.get(pair) or {}  # SPEC v2 (29/08) : contexte amplitude pour la garde SELL full
        entry = float(p["entry"])
        qty = float(p["qty"])
        stake = float(p.get("stake") or entry * qty)
        p["high"] = max(float(p.get("high") or entry), price)
        value = price * qty
        chg = (price / entry - 1.0) * 100.0

        _cal = (_profils().get(pair) or {}).get("calib") or {}
        t_arm = float(_cal.get("trail_arm_pct") or 0)
        t_gb = float(_cal.get("trail_giveback_pct") or 0)
        if t_arm > 0 and t_gb > 0:
            # backstop dur : le stop fixe reste (protection)
            if chg <= -float(p.get("stop") or 6):
                # SPEC v2 (29/08) — Verrous 1&2 et Bloc 1/2 : garde-fou SELL full en forte amplitude
                move24 = float(sc.get("move24_pct") or 0.0)
                vol_spike = sc.get("vol_spike")
                dd15 = float(sc.get("dd15_pct") or 0.0)
                is_degraded = (vol_spike is None)
                invalidation_valid = (not self.sell_full_require_invalidation) or is_degraded or (dd15 < -5.0 or vol_spike == 0)
                if move24 > self.sell_full_amplitude_guard and not invalidation_valid and not (is_degraded and not self.sell_full_guard_degraded):
                    full_qty = float(p["qty"])
                    part_qty = full_qty * 0.5
                    step, _mn = self.lot_filter(pair)
                    rem_qty = full_qty - part_qty
                    rem_val = rem_qty * price
                    min_q = step if step else 0.0
                    if rem_qty < min_q or rem_val < self.dust_sweep_min_notional:
                        proceeds = self.sell_trade(pair, price, f"dust_sweep_stop_guard_{pair}")
                        guard_tag = "DUST_SWEEP"
                    else:
                        proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_guard_partial_50", qty=part_qty)
                        guard_tag = "SELL_PARTIAL"
                    self.add_pair_cash(pair, proceeds)
                    p["guard_last"] = guard_tag
                else:
                    proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_avant_2x")
                    self.add_pair_cash(pair, proceeds)
                return
            # trailing : armé quand le pic ≥ arm, sortie si le prix redonne
            # giveback sous le pic (pattern HUNTER : sélectif, laisse courir).
            peak = float(p.get("high") or entry)
            peak_chg = (peak / entry - 1.0) * 100.0
            if peak_chg >= t_arm:
                floor = peak_chg - t_gb
                if chg <= floor:
                    proceeds = self.sell_trade(
                        pair, price,
                        f"trailing_peak{peak_chg:.1f}pct_giveback{t_gb:g}",
                    )
                    self.add_pair_cash(pair, proceeds)
                    return
            return  # on laisse courir : pas de 2×, pas de rip paliers

        if value >= stake * self.double_mult:
            self.stake_out_half(pair, price)
            return

        if not (self.is_bag(pair) and self.bag_no_tech_stop):
            if chg <= -float(p.get("stop") or 6):
                # SPEC v2 (29/08) — garde-fou SELL full (branche standard, non-trailing)
                move24 = float(sc.get("move24_pct") or 0.0)
                vol_spike = sc.get("vol_spike")
                dd15 = float(sc.get("dd15_pct") or 0.0)
                is_degraded = (vol_spike is None)
                invalidation_valid = (not self.sell_full_require_invalidation) or is_degraded or (dd15 < -5.0 or vol_spike == 0)
                if move24 > self.sell_full_amplitude_guard and not invalidation_valid and not (is_degraded and not self.sell_full_guard_degraded):
                    full_qty = float(p["qty"])
                    part_qty = full_qty * 0.5
                    step, _mn = self.lot_filter(pair)
                    rem_qty = full_qty - part_qty
                    rem_val = rem_qty * price
                    min_q = step if step else 0.0
                    if rem_qty < min_q or rem_val < self.dust_sweep_min_notional:
                        proceeds = self.sell_trade(pair, price, f"dust_sweep_stop_guard_{pair}")
                        guard_tag = "DUST_SWEEP"
                    else:
                        proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_guard_partial_50", qty=part_qty)
                        guard_tag = "SELL_PARTIAL"
                    self.add_pair_cash(pair, proceeds)
                    p["guard_last"] = guard_tag
                else:
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
        # SET-UP RÉGIME (30/08) : mode_entree="IMPULSE" → redeploy UNIQUEMENT en IMPULSE.
        if mode_entree(pair) == "IMPULSE" and regime != "IMPULSE":
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
        # FIX 31/08 (Buffy) : `regime` était utilisé dans les chemins de retour
        # (CB ouvert, ligne self.log ci-dessous) AVANT son assignation plus bas
        # `regime = sc["regime"]` → comme cette assignation existe dans la fonction,
        # Python traite `regime` en LOCAL pour tout le corps → NameError
        # « referenced before assignment » quand le chemin CB était pris (bug PRÉ-EXISTANT
        # vu dès le 30/08). On assigne en tête (sc.get, ne lève jamais) pour tous les chemins.
        regime = sc.get("regime") or "QUIET"
        # FIX 27/08 : les circuits breaker étaient décoratifs — is_ok() n'était
        # JAMAIS appelé, le trading continuait même circuit ouvert. La doc 25/08
        # promettait « circuit ouvert → trading bloqué ». Désormais : si BTC ou
        # GEX est stale, AUCUNE entrée nouvelle (les ventes manage_open restent
        # libres — on ne bloque jamais une sortie).
        if not self.cb_btc.is_ok() or not self.cb_gex.is_ok():
            say("warn", f"[{utc_now()}] BUY skip {pair} CB ouvert "
                        f"(btc={self.cb_btc.status()} gex={self.cb_gex.status()}) — données stale")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"CB:{self.cb_btc.status()}/{self.cb_gex.status()}",
            )
            return
        if self.maybe_redeploy_cash(pair, price, sc):
            return
        if regime in ("QUIET", "WATCH", "IMPULSE_WAIT"):
            return
        # SET-UP RÉGIME (30/08, GO Christophe) : mode_entree="IMPULSE" → n'entrer
        # QUE si le moteur voit la paire en régime IMPULSE (allumage de rafale).
        # EDEL : ne bouge que par rafales IMPULSE (découverte m6 70% vs 4%) —
        # entrer hors rafale = acheter un actif mort (fenêtre horaire abandonnée).
        _mode = mode_entree(pair)
        if _mode == "IMPULSE" and regime != "IMPULSE":
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"MODE_REGIME:IMPULSE_ONLY({regime})",
            )
            return
        if pair in self.pos or pair in self.bags:
            return
        # FILTRE MURS (24/08, codeur) : ne PAS acheter si la sonde aspiration a
        # détecté un spoof (mur de façade reconstruit) ou une chute de mur ≥ 15%/s
        # sur CETTE paire — les murs observés servent à la décision, pas qu'au radar.
        asp = self.aspiration.get(pair) or {}
        if asp.get("spoof"):
            say("warn", f"[{utc_now()}] BUY skip {pair} MUR-SPOOF (façade détectée)")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), "MUR-SPOOF:façade",
            )
            return
        drop_now = max(
            abs(float(asp.get("drop_bid_pct_per_s") or 0)),
            abs(float(asp.get("drop_ask_pct_per_s") or 0)),
        )
        if asp and drop_now >= self.aspiration_spoof_drop:
            say("warn", f"[{utc_now()}] BUY skip {pair} MUR-CASSE "
                        f"(drop {drop_now:.1f}%/s ≥ {self.aspiration_spoof_drop:.0f})")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"),
                f"MUR-CASSE:{drop_now:.1f}%/s",
            )
            return
        # FILTRE MURS HISTORIQUES (25/08, GO Christophe) : ne pas acheter
        # si le mur bid historique est trop faible (<$500 moyen = pas de support)
        ws = self.wall_strength(pair)
        if ws < 0.2:
            say("warn", f"[{utc_now()}] BUY skip {pair} MUR-FAIBLE (score={ws:.2f}, pas de support)")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"MUR-FAIBLE:{ws:.2f}",
            )
            return
        vok, vwhy = self.vol_ok_for_entry(sc, regime)
        if not vok:
            say("warn", f"[{utc_now()}] BUY skip {pair} {vwhy}")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"VOL:{vwhy}",
            )
            return
        # WALL BOOST : si le mur renforce post-choc BTC → favoriser l'entrée
        wall_note = ""
        if ws >= 0.7:
            wall_note = f" wall={ws:.2f}🛡️"
        elif ws >= 0.4:
            wall_note = f" wall={ws:.2f}"
        else:
            wall_note = f" wall={ws:.2f}⚠️"
        if regime == "COOLING":
            need = sc.get("cool_entry_pct", sc["dip_pct"])
            dd = sc["dd15_pct"]
            if dd >= need:
                self.buy(pair, price, sc,
                    f"cooling_dd15={dd:.1f}>={need:.1f}{wall_note}")
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
                    f"impulse_pullback_dd6={sc['dd6_pct']:.1f}>={need:.1f}"
                    f" m6={sc['move6_pct']:.1f}{wall_note}",
                )
            return

    def tick_pair(self, pair: str):
        price = last_price(pair)
        sc = self.scores.get(pair)
        if not sc:
            return
        sc["price"] = price
        # Croisement indices × murs (28/08, mode OBSERVATION, réversible) :
        # journalise le contexte de décision sans toucher aux entrées.
        try:
            self.log_contexte(pair, sc, price)
        except Exception:
            pass
        # FIX 30/08 : OBSERVE-ONLY — on journalise MAIS on ne trade JAMAIS ces paires.
        # Bloque toute entrée/ré-entry/bag/seed (l'erreur corrigée : elles étaient
        # devenues tradées via PAPER_PAIRS). Les données de contexte sont bien capturées.
        if pair in self.observe_only:
            return
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
            if pair in self.pos or pair in self.observe_only:
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
        # RESUME (24/08, Christophe « tenir les positions pendant les coupures ») :
        # si --resume, on reprend le dernier état (pos/bags/cash) au lieu de re-seed.
        # Sans --resume, comportement historique (seed au boot) conservé.
        if getattr(self, "resume", False):
            if not self.resume_state():
                say("warn", "RESUME: aucun état à reprendre — seed au boot (comportement normal)")
                self.seed_inventory()
                self.seed_bags()
        else:
            self.seed_inventory()
            self.seed_bags()
        n = 0
        while self.alive:
            # Phase 1 (31/08) : cadence anti-drift + UN SEUL appel batch prix par
            # cycle → le cache alimente last_price (0 appel réseau ensuite). Si le
            # batch échoue, last_price fait le fallback unitaire/dernier prix connu.
            loop_start = time.time()
            try:
                fetch_all_prices(self.pairs)
            except Exception:
                pass
            # Croisement indices × murs : config relue à chaque cycle → on peut
            # couper/rallumer à chaud (croisement_config.json) sans redémarrer.
            self._load_croisement_config()
            if STOP_FILE.exists():
                say("warn", f"[{utc_now()}] STOP_PAPER détecté")
                break
            if STOP_ALL.exists():
                say("warn", f"[{utc_now()}] STOP_ALL détecté (kill-switch global)")
                break
            if n > 0 and n % self.score_every == 0:
                self.refresh_scores()
                self.refresh_cortana_pilot()
            # Sonde aspiration (mode observation) : paires actives, toutes les N cycles
            self.probe_aspiration(n)
            # === MURS: détection post-choc + GEX wall (25/08) ===
            try:
                for pair in self.pairs:
                    self.check_wall_melt(pair)
                self.check_gex_wall()
            except Exception as e:
                say("err", f"[murs] check_err: {e}")
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
                _melt = len(self.wall_melt_events)
                _gex_note = f" gex=$82K" if self.gex_call_wall > 0 else ""
                _cb = f" cb:{self.cb_btc.status()}"
                _health = self.get_pipeline_health_mult()
                _health_note = f" health={_health:.2f}" if _health < 1.0 else ""
                _cortana_rec = self.get_cortana_recommendation()
                _cortana_note = f" | Cortana: {_cortana_rec.get('action', '?')}" if _cortana_rec.get('niveau') not in ('inconnu', None) else ""
                say(
                    "heart",
                    f"[{utc_now()}] heartbeat open={open_n} bags={bags_n} "
                    f"dca={len(self.bag_dca)} cash_pairs={cash_n}({cash_sum:.1f}$) "
                    f"mise={notion:.2f}$ trades={self.trades} "
                    f"pnl={self.pnl_total:+.4f}$ | {regimes}{standby} "
                    f"cortana={len(self.cortana_pending)} bag={_bag_open}/{self.bag_max_positions}"
                    f" melts={_melt}{_gex_note}{_cb}{_health_note}{_cortana_note}",
                )
                self.save_state()
            # Phase 1 (31/08) : anti-drift — on dort jusqu'au prochain tick absolu,
            # pas 20s fixes (sinon temps de calcul cumulé qui décale toute la boucle).
            elapsed = time.time() - loop_start
            time.sleep(max(0.0, self.poll - elapsed))
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
    import argparse
    ap = argparse.ArgumentParser(description="Hulk paper MEXC")
    ap.add_argument("--resume", action="store_true",
                    help="Reprendre le dernier état (positions/bags/cash) au lieu de re-seed")
    args = ap.parse_args()
    cfg = load_env(CFG)
    if cfg.get("MODE", "paper") != "paper":
        print("MODE doit être paper pour ce script")
        return 2
    inv = load_inventory()
    pairs = pick_pairs(cfg, inv)
    bot = PaperBot(cfg, pairs, inv)
    bot.resume = args.resume
    return bot.run()


if __name__ == "__main__":
    sys.exit(main())
