#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SHADOW MODE — SCÉNARIO C (Gemini R24) — ZÉRO ORDRE, ZÉRO CLÉ API, LECTURE SEULE DU MARCHÉ.

Règles GELÉES (validées R18→R24, protocole figé) :
  - ALPHA : LONG uniquement. BETA : SHORT uniquement. Flux séparés, jamais mélangés.
  - Gate H : H=1 ssi somme PnL brut des fills (t-120min, t] > 0 (causal).
    Source HYBRIDE : héritage des fills réels du champion (CSV runs/) + fills virtuels du shadow.
    Le champion étant à l'arrêt, la bascule champion→shadow se fait naturellement en 2h. Divulgation R25.
  - Entrée : à l'open de la barre 1m suivant un slot 5-min où H=1 et à plat (cadence 5-min = replay validé).
  - Sortie : trailing 30% avec plancher breakeven (armé après 1er dépassement d'entrée),
    cap +50 USDT, pire cas intra-barre (stop avant cap), sortie au close si H→0
    (vérifié aux bornes 5-min relatives à l'entrée, comme le replay v2).
  - Frais : 1,760 USDT/trade (testnet mesuré). Funding non simulé (holds 3-7 min) — divulgation R25.

Sorties (runs/) : SHADOW_SC_<TAG>_FILLS.csv, SHADOW_SC_<TAG>_TICKS.csv, SHADOW_SC_<TAG>.log
Arrêt : toucher runs/STOP_SHADOW (ou STOP pour l'arrêt famille).

Selftest : SHADOW_SELFTEST=1 python3 shadow_mode_sc.py  → assertions sur barres synthétiques.
"""
import csv, glob, json, os, sys, time, urllib.request
from datetime import datetime, timezone

# ---- PARAMÈTRES GELÉS (R24 : ne pas toucher pendant les 14 jours) ----
SYMBOL     = os.environ.get("SHADOW_SYMBOL", "BTCUSDT")
QTY        = float(os.environ.get("SHADOW_QTY", "0.10593"))
FEE_USDT   = float(os.environ.get("SHADOW_FEE_USDT", "1.760"))
RET        = float(os.environ.get("SHADOW_TRAIL_RET", "0.30"))
CAP_USDT   = float(os.environ.get("SHADOW_CAP_USDT", "50.0"))
CAP_PX     = CAP_USDT / QTY
H_WINDOW   = int(os.environ.get("SHADOW_H_WINDOW_SEC", "7200"))   # 2h
# BOOTSTRAP : champion à l'arrêt → seed 2h = 0 → H=0 → sans porte d'entrée, le shadow
# ne traderait JAMAIS (interrupteur débranché). BOOTSTRAP_MIN autorise les entrées
# (journalisées "BOOTSTRAP") pendant N minutes pour que les fills virtuels naissent.
# Les SORTIES restent gouvernées par H (disjoncteur actif dès la première minute).
BOOTSTRAP_MIN = float(os.environ.get("SHADOW_BOOTSTRAP_MIN", "0"))
ROOT       = os.path.expanduser(os.environ.get("ACE777_ROOT", "~/ace777-test-day1"))
RUNS       = os.path.join(ROOT, "runs")
TAG        = os.environ.get("SHADOW_TAG", datetime.now(timezone.utc).strftime("SHADOW_SC_%Y%m%d"))
BASE_URL   = os.environ.get("SHADOW_BASE_URL", "https://fapi.binance.com/fapi/v1/klines")

STOP_SHADOW = os.path.join(RUNS, "STOP_SHADOW")
STOP_FAMILY = os.path.join(RUNS, "STOP")
FILLS_CSV   = os.path.join(RUNS, f"{TAG}_FILLS.csv")
TICKS_CSV   = os.path.join(RUNS, f"{TAG}_TICKS.csv")
LOG_PATH    = os.path.join(RUNS, f"{TAG}.log")

os.makedirs(RUNS, exist_ok=True)

def log(msg):
    line = f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} {msg}"
    print(line, flush=True)
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")

# ---- GATE H : héritage champion + virtuel ----
def load_champion_fills(pattern, want_side):
    """Fills réels du champion (causal, déjà passés) — amorçage du gate."""
    ev = []
    for path in sorted(glob.glob(os.path.join(RUNS, pattern))):
        try:
            with open(path, errors="replace") as f:
                h = f.readline().strip().split(",")
                if not h or "ts" not in h:
                    continue
                ti, si, di, pi = h.index("ts"), h.index("status"), h.index("side"), h.index("pnl")
                for line in f:
                    c = line.strip().split(",")
                    if len(c) < 10 or c[si] != "FILLED":
                        continue
                    if c[di].upper() != want_side:
                        continue
                    t = datetime.strptime(c[ti][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc).timestamp()
                    ev.append((t, float(c[pi])))
        except Exception:
            continue
    ev.sort()
    return ev

class Stream:
    """Un flux virtuel indépendant (ALPHA=LONG, BETA=SHORT). Zéro ordre réel."""
    def __init__(self, name, side, champion_pattern):
        self.name = name
        self.side = side                       # "LONG" ou "SHORT"
        self.seed = load_champion_fills(champion_pattern, "BUY" if side == "LONG" else "SELL")
        self.virtual = []                      # [(ts, pnl_brut)] fills virtuels du shadow
        self.pos = None                        # dict(entry_ts, entry_px, ext, armed)
        log(f"[{self.name}] side={self.side} seed_champion={len(self.seed)} fills "
            f"(2h récentes: {sum(v for t, v in self.seed if t > time.time() - H_WINDOW):+.2f} USDT)")

    # -- gate H (causal : fills STRICTEMENT avant ts) --
    def H(self, ts):
        lo_b = sum(v for t, v in self.seed if ts - H_WINDOW < t < ts)
        lo_v = sum(v for t, v in self.virtual if ts - H_WINDOW < t < ts)
        src = "SHADOW" if self.virtual else ("CHAMP" if self.seed else "NONE")
        return (lo_b + lo_v) > 0, src, lo_b, lo_v

    # -- entrée virtuelle --
    def try_enter(self, bar_open_ts, entry_px, ts_now, boot_deadline=0.0):
        h, src, _, _ = self.H(ts_now)
        forced = False
        if not h and ts_now < boot_deadline:
            h, forced = True, True                      # porte BOOTSTRAP (journalisée)
        if not h or self.pos is not None:
            return
        self.pos = {"entry_ts": bar_open_ts, "entry_px": entry_px,
                    "ext": entry_px, "armed": False, "h_src": src}
        self._fill_log(bar_open_ts, "ENTRY", entry_px, 0.0,
                       ("BOOTSTRAP(H=0→entrée forcée)" if forced else f"H=1({src})"))

    # -- gestion de position sur une barre fermée (pire cas intra-barre : stop avant cap) --
    def on_bar(self, o, h, l, c, bar_open_ts, ts_now):
        p = self.pos
        if p is None:
            return
        entry, ext = p["entry_px"], p["ext"]
        exit_px, reason = None, None
        if self.side == "LONG":
            if h > entry:
                p["armed"] = True
            ext = max(ext, h)
            p["ext"] = ext
            if p["armed"]:
                stop = max(entry, ext - RET * (ext - entry))     # plancher breakeven
                if l <= stop:
                    exit_px, reason = stop, "trailing_stop"
                elif h >= entry + CAP_PX:
                    exit_px, reason = entry + CAP_PX, "cap"
        else:
            if l < entry:
                p["armed"] = True
            ext = min(ext, l)
            p["ext"] = ext
            if p["armed"]:
                stop = min(entry, ext + RET * (entry - ext))
                if h >= stop:
                    exit_px, reason = stop, "trailing_stop"
                elif l <= entry - CAP_PX:
                    exit_px, reason = entry - CAP_PX, "cap"
        # sortie H→0 : bornes 5-min relatives à l'entrée (identique replay v2)
        if exit_px is None and (bar_open_ts - p["entry_ts"]) % 300 == 0 and bar_open_ts > p["entry_ts"]:
            hh, src, _, _ = self.H(bar_open_ts - 1)
            if not hh:
                exit_px, reason = c, "h_gate_off"
        if exit_px is not None:
            self._close(bar_open_ts, exit_px, reason)

    def _close(self, ts, exit_px, reason):
        p = self.pos
        pnl = ((exit_px - p["entry_px"]) if self.side == "LONG"
               else (p["entry_px"] - exit_px)) * QTY
        net = pnl - FEE_USDT
        self.virtual.append((ts, pnl))
        self._fill_log(ts, "EXIT", exit_px, pnl,
                       f"{reason} net={net:+.4f} hold={int(ts - p['entry_ts'])}s")
        self.pos = None

    def _fill_log(self, ts, kind, px, pnl, msg):
        iso = datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        new = not os.path.exists(FILLS_CSV)
        with open(FILLS_CSV, "a", newline="") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["ts", "stream", "side", "kind", "px", "pnlGross", "msg"])
            w.writerow([iso, self.name, self.side, kind, f"{px:.2f}", f"{pnl:.4f}", msg])

# ---- boucle marché (klines 1m publiques, aucune clé) ----
def fetch_bars(limit=3):
    url = f"{BASE_URL}?symbol={SYMBOL}&interval=1m&limit={limit}"
    for a in range(3):
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                rows = json.loads(r.read())
            return [(int(x[0]) // 1000, float(x[1]), float(x[2]), float(x[3]), float(x[4])) for x in rows]
        except Exception:
            time.sleep(1 + a)
    return []

def run():
    alpha = Stream("ALPHA", "LONG",  "*ALPHA*.csv")
    beta  = Stream("BETA",  "SHORT", "*BETA*.csv")
    streams = [alpha, beta]
    last_closed = 0
    pending = []            # entrées programmées : (stream, slot_ts)
    boot_deadline = time.time() + BOOTSTRAP_MIN * 60 if BOOTSTRAP_MIN > 0 else 0.0
    log(f"SHADOW MODE ON — {TAG} | zéro ordre | symbole {SYMBOL} | "
        f"QTY={QTY} FEE={FEE_USDT} trail={RET:.0%} cap={CAP_USDT}$ | "
        f"bootstrap={BOOTSTRAP_MIN:g}min | arrêt: touch runs/STOP_SHADOW")
    with open(TICKS_CSV, "a", newline="") as tf:
        tw = csv.writer(tf)
        if tf.tell() == 0:
            tw.writerow(["ts", "px_close", "H_alpha", "H_beta", "h_src_alpha",
                         "h_src_beta", "pos_alpha", "pos_beta", "pnlVirtAlpha", "pnlVirtBeta"])
        while not (os.path.exists(STOP_SHADOW) or os.path.exists(STOP_FAMILY)):
            bars = fetch_bars()
            if bars:
                closed, forming = bars[:-1], bars[-1]
                for b in closed:
                    t, o, h, l, c = b
                    if t <= last_closed:
                        continue
                    last_closed = t
                    # 1) gérer positions ouvertes sur la barre fermée
                    for s in streams:
                        s.on_bar(o, h, l, c, t, t)
                    # 2) exécuter les entrées programmées (slot 5-min précédent → open de cette barre)
                    still = []
                    for s, slot_ts in pending:
                        if s.pos is None:
                            s.try_enter(t, o, t, boot_deadline)   # open barre suivante = replay
                        elif s.H(t)[0] or t < boot_deadline:
                            still.append((s, slot_ts))    # report d'un slot si position occupée
                    pending = still
                    # 3) programmer les entrées aux slots 5-min (cadence = replay validé)
                    if t % 300 == 0:
                        for s in streams:
                            if s.pos is None and (s.H(t)[0] or t < boot_deadline):
                                pending.append((s, t))
                    # 4) journal tick
                    ha, sa, _, _ = alpha.H(t)
                    hb, sb, _, _ = beta.H(t)
                    va = sum(v for _, v in alpha.virtual)
                    vb = sum(v for _, v in beta.virtual)
                    tw.writerow([datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
                                 f"{c:.2f}", int(ha), int(hb), sa, sb,
                                 alpha.pos["entry_px"] if alpha.pos else "",
                                 beta.pos["entry_px"] if beta.pos else "",
                                 f"{va:.4f}", f"{vb:.4f}"])
                    tf.flush()
            time.sleep(5)
    log("SHADOW MODE OFF (STOP détecté) — fills et ticks conservés.")

# ---- SELFTEST : barres synthétiques, assertions dures ----
def selftest():
    import random
    random.seed(7)
    # logs du selftest dérivés vers /tmp (jamais dans runs/)
    global FILLS_CSV, LOG_PATH
    FILLS_CSV = "/tmp/shadow_selftest_fills.csv"
    LOG_PATH = "/tmp/shadow_selftest.log"
    if os.path.exists(FILLS_CSV):
        os.remove(FILLS_CSV)
    fails = []
    def check(name, cond):
        print(f"  {'PASS' if cond else 'FAIL'} — {name}")
        if not cond:
            fails.append(name)

    now = 1_700_000_000
    def mk_stream(side, seed=None):
        # seed par défaut : fill positif récent → H=1 (permets try_enter)
        if seed is None:
            seed = [(now - 60, +5.0)]
        s = Stream.__new__(Stream)
        s.name, s.side, s.seed, s.virtual, s.pos = "T", side, list(seed), [], None
        return s
    # 1) LONG : armement, trailing 30%, plancher breakeven
    s = mk_stream("LONG"); s.try_enter(now, 100.0, now)
    s.on_bar(100, 110, 100, 105, now + 60, now + 60)          # armé, ext=110 → stop=107
    s.on_bar(107, 108, 106.5, 107, now + 120, now + 120)      # l<=107 → exit 107
    check("LONG trailing 30% stop=107", abs(s.virtual[-1][1] - 7 * QTY) < 1e-9)
    # 2) LONG : plancher breakeven (ext à peine au-dessus → stop>=entry)
    s = mk_stream("LONG"); s.try_enter(now, 100.0, now)
    s.on_bar(100, 100.5, 99.0, 100.2, now + 60, now + 60)     # armé, ext=100.5 → stop=100.35
    s.on_bar(100.3, 100.4, 99.5, 100.0, now + 120, now + 120) # l<=100.35 → exit 100.35 (PAS sous entrée)
    check("LONG plancher breakeven (exit>=entry)", s.virtual[-1][1] >= -1e-9)
    # 3) LONG : non armé → pas de stop (que le H-exit peut sortir)
    s = mk_stream("LONG"); s.try_enter(now, 100.0, now)
    s.on_bar(100, 100.0, 95.0, 96.0, now + 60, now + 60)
    check("LONG non armé → pas de stop", s.pos is not None and abs(s.pos["ext"] - 100.0) < 1e-9)
    # 4) cap : la barre touche le cap SANS redescendre sous le stop du trailing
    s = mk_stream("LONG"); s.try_enter(now, 100.0, now)
    s.on_bar(100, 100 + CAP_PX, 100 + 0.8 * CAP_PX, 100, now + 60, now + 60)
    check("LONG cap +50$", s.pos is None and abs(s.virtual[-1][1] - 50.0) < 1e-6)
    # 5) SHORT miroir
    s = mk_stream("SHORT"); s.try_enter(now, 100.0, now)
    s.on_bar(100, 100, 90, 93, now + 60, now + 60)            # armé, ext=90 → stop=93
    s.on_bar(93, 93.5, 93, 93.2, now + 120, now + 120)        # h>=93 → exit 93
    check("SHORT trailing miroir stop=93", abs(s.virtual[-1][1] - 7 * QTY) < 1e-9)
    # 6) H→0 exit à la borne 5-min relative à l'entrée
    #    (fill d'amorçage à now-7000 : H=1 à l'entrée, H=0 à now+300 — sorti de la fenêtre 2h)
    #    la barre ne doit NI armer le trailing vers un stop touché, ni casser l'entrée
    s = mk_stream("LONG", seed=[(now - 7000, +5.0)])
    s.try_enter(now, 100.0, now)
    check("préparation test 6 : entrée H=1", s.pos is not None)
    s.on_bar(100, 100.9, 100.8, 100.9, now + 60, now + 60)    # armé (h>entry), stop=100.63, l=100.8 → tient
    check("préparation test 6 : position vivante", s.pos is not None)
    s.on_bar(100.9, 101.0, 100.85, 100.95, now + 300, now + 300)  # borne 5-min, H=0 → exit close 100.95
    check("H→0 exit au close (borne 5-min)", s.pos is None and abs(s.virtual[-1][1] - 0.95 * QTY) < 1e-6)
    # 7) gate H bloque l'entrée si pertes récentes
    s = mk_stream("LONG", seed=[(now - 60, -5.0)])
    h, _, _, _ = s.H(now)
    check("H=0 si PnL 2h négatif", h is False)
    s2 = mk_stream("LONG", seed=[(now - 60, +5.0)])
    h2, src, _, _ = s2.H(now)
    check("H=1 si PnL 2h positif (source CHAMP)", h2 and src == "CHAMP")
    # 8) fills virtuels prennent le relais (bascule hybride)
    #    héritage champion SORTI de la fenêtre 2h → seul le virtuel décide (et il saigne → H=0)
    s3 = mk_stream("LONG", seed=[(now - 7300, +5.0)])
    s3.virtual = [(now - 60, -3.0)]
    h3, src3, _, _ = s3.H(now)
    check("bascule hybride : virtuel seul décide → H=0 (SHADOW)", (not h3) and src3 == "SHADOW")
    # 9) pire cas intra-barre (convention v2 gelée) : le STOP est vérifié AVANT le cap
    s = mk_stream("LONG"); s.try_enter(now, 100.0, now)
    s.on_bar(100, 100 + CAP_PX * 2, 100.5, 100, now + 60, now + 60)
    # stop = 100 + 0.7*(ext-100) → pnl attendu = 0.7 * 2 * CAP = 70$ (sortie trailing, pas cap)
    check("pire cas : stop avant cap (convention v2)",
          s.pos is None and abs(s.virtual[-1][1] - 0.7 * 2 * 50.0) < 1e-6)
    print(f"\nSELFTEST : {'9/9 PASS ✅' if not fails else 'ÉCHEC: ' + ', '.join(fails)}")
    return 0 if not fails else 1

if __name__ == "__main__":
    if os.environ.get("SHADOW_SELFTEST") == "1":
        sys.exit(selftest())
    run()
