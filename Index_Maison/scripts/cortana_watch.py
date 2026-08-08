#!/usr/bin/env python3
"""
Cortana WATCH — sniffe fills / bags / trend / move / baleine / Attention
et pousse UNE alerte sur le bus urgent (contrat P3).

  python3 cortana_watch.py            # un passage
  python3 cortana_watch.py --dry      # détecte, n'écrit pas
  python3 cortana_watch.py --seed     # mémorise l'état sans parler

Pas de trading. Voice = bus → cortana_thermo poll.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1")
SCRIPTS = ROOT / "Index_Maison" / "scripts"
THERMO_LIVE = ROOT / "Index_Maison" / "thermo" / "live.json"
ATTENTION = ROOT / "Index_Maison" / "A_Mon_Attention"
STATE_PATH = Path("/tmp/ace777_swarm_pids/.cortana_watch_state.json")
STATE_MIRROR = ROOT / "Index_Maison" / "thermo" / ".cortana_watch_state.json"
URGENT_PATH = Path("/tmp/ace777_swarm_pids/.urgent_alert.json")

sys.path.insert(0, str(SCRIPTS))

BTC_1H_PCT = float(os.environ.get("CORTANA_BTC_1H_PCT", "1.5"))
BTC_4H_PCT = float(os.environ.get("CORTANA_BTC_4H_PCT", "2.5"))
WHALE_USD_MIN = float(os.environ.get("CORTANA_WHALE_USD", "500000"))
DUAL_WINDOW_SEC = int(os.environ.get("CORTANA_DUAL_WINDOW", "120"))
# Fills individuels : silencieux par défaut (sinon spam Bêta). Voix si |pnl| ≥ seuil.
FILL_VOICE = os.environ.get("CORTANA_WATCH_FILLS", "0") == "1"
FILL_ALERT_MIN = float(os.environ.get("CORTANA_FILL_ALERT_MIN", "0.50"))
HULK_VOICE = os.environ.get("CORTANA_WATCH_HULK", "0") == "1"
COOLDOWN = {
    "fill": int(os.environ.get("CORTANA_CD_FILL", "180")),
    "hulk": int(os.environ.get("CORTANA_CD_HULK", "180")),
    "dual": int(os.environ.get("CORTANA_CD_DUAL", "60")),
    "whale": int(os.environ.get("CORTANA_CD_WHALE", "120")),
    "move": int(os.environ.get("CORTANA_CD_MOVE", "180")),
    "trend": int(os.environ.get("CORTANA_CD_TREND", "300")),
    "tweet": int(os.environ.get("CORTANA_CD_TWEET", "60")),
}

ATTENTION_SKIP = {
    "INDEX.md",
    "00_LIRE_MOI.md",
    "ATTENTION_VOCALE.md",
    ".DS_Store",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def now_unix() -> float:
    return time.time()


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_MIRROR.parent.mkdir(parents=True, exist_ok=True)
    blob = json.dumps(state, ensure_ascii=False, indent=2) + "\n"
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(blob, encoding="utf-8")
    tmp.replace(STATE_PATH)
    STATE_MIRROR.write_text(blob, encoding="utf-8")


def fill_fp(fill: dict | None) -> str | None:
    if not fill:
        return None
    return "|".join(
        str(fill.get(k) or "")
        for k in ("ts", "side", "status", "pnl", "entry", "exit", "qty")
    )


def hulk_fp(hulk: dict) -> str | None:
    last = (hulk.get("last") or [None])[0]
    if not last:
        return f"bags:{hulk.get('bags')}:trades:{hulk.get('trades')}"
    return "|".join(
        str(last.get(k) or "")
        for k in ("ts", "pair", "event", "pnl", "price")
    ) + f"|bags:{hulk.get('bags')}"


def attention_files() -> list[tuple[str, float]]:
    if not ATTENTION.exists():
        return []
    out = []
    for p in ATTENTION.iterdir():
        if not p.is_file():
            continue
        if p.name in ATTENTION_SKIP or p.name.startswith("CHECKUP"):
            continue
        if p.suffix.lower() not in (".md", ".txt"):
            continue
        out.append((p.name, p.stat().st_mtime))
    return sorted(out, key=lambda x: x[1], reverse=True)


def describe_fill(who: str, fill: dict) -> str:
    side = (fill.get("side") or fill.get("status") or "?").upper()
    pnl = fill.get("pnl")
    pnl_s = f"{pnl:+.2f} dollars" if isinstance(pnl, (int, float)) else "pnl inconnu"
    lev = fill.get("lev_hint")
    lev_s = f", levier {lev}" if lev else ""
    return f"{who} : {side}, {pnl_s}{lev_s}"


def describe_hulk(hulk: dict) -> str:
    last = (hulk.get("last") or [None])[0]
    bags = hulk.get("bags") or 0
    if last:
        ev = last.get("event") or last.get("dir") or "mouvement"
        pair = last.get("pair") or "paire"
        return f"Hulk {ev} sur {pair}, {bags} bags ouverts"
    return f"Hulk : {bags} bags"


def cooled(state: dict, key: str) -> bool:
    last = float((state.get("cooldown") or {}).get(key) or 0)
    return (now_unix() - last) >= COOLDOWN.get(key, 60)


def mark_cool(state: dict, key: str) -> None:
    state.setdefault("cooldown", {})[key] = now_unix()


def bus_busy() -> bool:
    if not URGENT_PATH.exists():
        return False
    try:
        d = json.loads(URGENT_PATH.read_text(encoding="utf-8"))
        return isinstance(d, dict) and not d.get("ack")
    except Exception:
        return True


def emit(title: str, msg: str, *, level: str, source: str, dry: bool) -> int:
    if dry:
        print(f"[DRY][{level}] {title}: {msg}")
        return 0
    if bus_busy():
        print(f"[watch] bus occupé — report: {title}")
        return 3
    from cortana_thermo import write_urgent_alert

    write_urgent_alert(msg, source=source, level=level, title=title)
    print(f"[watch] → bus [{level}] {title}: {msg}")
    return 0


def snapshot_engines():
    from cockpit_mission_feed import (
        find_ace_pair,
        load_ace_side,
        load_hulk,
        session_start_from_live,
    )

    a_path, b_path, live_path = find_ace_pair()
    since = session_start_from_live(live_path)
    return load_ace_side(a_path, since=since), load_ace_side(b_path, since=since), load_hulk()


def _sign(x) -> str:
    try:
        v = float(x)
    except Exception:
        return "0"
    if v > 0.05:
        return "+"
    if v < -0.05:
        return "-"
    return "0"


def build_seed() -> dict:
    alpha, beta, hulk = snapshot_engines()
    live = load_json(THERMO_LIVE)
    a2 = ((live.get("indicators") or {}).get("A2") or {}).get("value")
    return {
        "seeded_at": now_iso(),
        "alpha_fp": fill_fp(alpha.get("lastFill")),
        "beta_fp": fill_fp(beta.get("lastFill")),
        "hulk_fp": hulk_fp(hulk),
        "hulk_bags": hulk.get("bags") or 0,
        "whaleMax": live.get("whaleMax") or live.get("whaleUsd") or 0,
        "whaleN": live.get("whaleN") or 0,
        "chg1h": live.get("chg1h"),
        "chg4h": live.get("chg4h"),
        "trend": a2,
        "trend_sign": _sign(live.get("chg1h")),
        "attention": {n: m for n, m in attention_files()},
        "last_ace_event_ts": 0,
        "last_hulk_event_ts": 0,
        "dual_key": None,
        "cooldown": {},
    }


def apply_patch(state: dict, patch: dict) -> None:
    for k, v in patch.items():
        if k == "_cool":
            mark_cool(state, str(v))
        elif k == "_attention_add":
            name, mtime = v
            state.setdefault("attention", {})[name] = mtime
        else:
            state[k] = v


def collect_events(state: dict) -> list[dict]:
    events: list[dict] = []
    alpha, beta, hulk = snapshot_engines()
    live = load_json(THERMO_LIVE)
    tnow = now_unix()
    pending_ace = False
    pending_hulk = False

    silent_patches: list[dict] = []

    for who, side, key_fp in (
        ("Alfa", alpha, "alpha_fp"),
        ("Bêta", beta, "beta_fp"),
    ):
        fp = fill_fp(side.get("lastFill"))
        if fp and fp != state.get(key_fp):
            pending_ace = True
            fill = side.get("lastFill") or {}
            pnl = abs(float(fill.get("pnl") or 0))
            patch = {key_fp: fp, "last_ace_event_ts": tnow, "_cool": "fill"}
            # Silence par défaut — évite « Fill Bêta » toutes les 30 s
            if (FILL_VOICE or pnl >= FILL_ALERT_MIN) and cooled(state, "fill"):
                events.append(
                    {
                        "prio": 40,
                        "kind": "fill",
                        "title": f"Fill {who}",
                        "msg": describe_fill(who, fill),
                        "level": "SOFT",
                        "source": "cortana_watch_fill",
                        "patch": patch,
                    }
                )
            else:
                silent_patches.append(patch)

    hfp = hulk_fp(hulk)
    if hfp and hfp != state.get("hulk_fp"):
        pending_hulk = True
        patch = {
            "hulk_fp": hfp,
            "hulk_bags": hulk.get("bags") or 0,
            "last_hulk_event_ts": tnow,
            "_cool": "hulk",
        }
        if HULK_VOICE and cooled(state, "hulk"):
            events.append(
                {
                    "prio": 35,
                    "kind": "hulk",
                    "title": "Hulk bag",
                    "msg": describe_hulk(hulk),
                    "level": "SOFT",
                    "source": "cortana_watch_hulk",
                    "patch": patch,
                }
            )
        else:
            silent_patches.append(patch)


    ace_ts = tnow if pending_ace else float(state.get("last_ace_event_ts") or 0)
    hulk_ts = tnow if pending_hulk else float(state.get("last_hulk_event_ts") or 0)
    if (
        ace_ts
        and hulk_ts
        and abs(ace_ts - hulk_ts) <= DUAL_WINDOW_SEC
        and cooled(state, "dual")
    ):
        dual_key = f"{int(ace_ts)}-{int(hulk_ts)}"
        if dual_key != state.get("dual_key"):
            events.append(
                {
                    "prio": 10,
                    "kind": "dual",
                    "title": "Deux portefeuilles",
                    "msg": (
                        "Activité sur Ace et Hulk dans la même fenêtre. "
                        "Les deux stacks bougent — sniffe, pas de GO."
                    ),
                    "level": "URGENT",
                    "source": "cortana_watch_dual",
                    "patch": {"dual_key": dual_key, "_cool": "dual"},
                }
            )

    wmax = float(live.get("whaleMax") or live.get("whaleUsd") or 0)
    wn = int(live.get("whaleN") or 0)
    prev_max = float(state.get("whaleMax") or 0)
    if wmax >= WHALE_USD_MIN and wmax > prev_max + 1 and cooled(state, "whale"):
        events.append(
            {
                "prio": 15,
                "kind": "whale",
                "title": "Baleine",
                "msg": (
                    f"Gros print détecté, environ {int(wmax)} dollars, "
                    f"{wn} transaction proxy. Source Binance."
                ),
                "level": "URGENT",
                "source": "cortana_watch_whale",
                "patch": {"whaleMax": wmax, "whaleN": wn, "_cool": "whale"},
            }
        )

    try:
        c1 = float(live.get("chg1h") or 0)
        c4 = float(live.get("chg4h") or 0)
    except Exception:
        c1 = c4 = 0.0
    big = abs(c1) >= BTC_1H_PCT or abs(c4) >= BTC_4H_PCT
    prev1 = state.get("chg1h")
    moved = prev1 is None or abs(c1 - float(prev1 or 0)) >= 0.3
    if big and moved and cooled(state, "move"):
        events.append(
            {
                "prio": 20,
                "kind": "move",
                "title": "Gros mouvement",
                "msg": (
                    f"Bitcoin une heure {c1:+.2f} pour cent, "
                    f"quatre heures {c4:+.2f} pour cent."
                ),
                "level": "URGENT",
                "source": "cortana_watch_move",
                "patch": {"chg1h": c1, "chg4h": c4, "_cool": "move"},
            }
        )

    a2 = ((live.get("indicators") or {}).get("A2") or {}).get("value")
    sign = _sign(c1)
    prev_sign = state.get("trend_sign")
    trend_change = (a2 and a2 != state.get("trend")) or (
        sign != "0" and prev_sign not in (None, "0") and sign != prev_sign
    )
    if trend_change and cooled(state, "trend"):
        events.append(
            {
                "prio": 25,
                "kind": "trend",
                "title": "Changement de tendance",
                "msg": f"Structure {a2 or 'inconnue'}, signe une heure {sign}.",
                "level": "SOFT",
                "source": "cortana_watch_trend",
                "patch": {
                    "trend": a2,
                    "trend_sign": sign,
                    "chg1h": c1,
                    "chg4h": c4,
                    "_cool": "trend",
                },
            }
        )

    known = dict(state.get("attention") or {})
    for name, mtime in attention_files():
        if name not in known and cooled(state, "tweet"):
            label = name.replace(".md", "").replace(".txt", "")
            # enlève date ISO en tête — évite lecture « deux mille… »
            if len(label) > 10 and label[4] == "-" and label[7] == "-":
                label = label[11:].lstrip("_- ") or "note"
            label = label.replace("_", " ")
            events.append(
                {
                    "prio": 30,
                    "kind": "tweet",
                    "title": "Nouveau à ton attention",
                    "msg": (
                        f"Nouvelle note : {label}. "
                        "Peut servir au prototype — à lire dans Attention."
                    ),
                    "level": "SOFT",
                    "source": "cortana_watch_attention",
                    "patch": {"_attention_add": (name, mtime), "_cool": "tweet"},
                }
            )
            break

    return events, silent_patches


def run(*, dry: bool, seed: bool) -> int:
    if seed or not STATE_PATH.exists():
        st = build_seed()
        save_state(st)
        print(f"[watch] seed OK ({now_iso()}) — pas d'alerte")
        if seed:
            return 0

    state = load_json(STATE_PATH) or build_seed()
    events, silent_patches = collect_events(state)
    for sp in silent_patches:
        apply_patch(state, sp)
    if silent_patches and not events:
        save_state(state)
        print(f"[watch] fills/bags mémorisés silencieux ({len(silent_patches)}) — pas de voix")
        return 2
    if not events:
        print("[watch] rien de nouveau")
        return 2

    events.sort(key=lambda e: e["prio"])
    chosen = events[0]
    for ev in events:
        apply_patch(state, ev.get("patch") or {})
    save_state(state)

    rc = emit(
        chosen["title"],
        chosen["msg"],
        level=chosen["level"],
        source=chosen["source"],
        dry=dry,
    )
    if len(events) > 1:
        print(f"[watch] +{len(events) - 1} autre(s) event(s) mémorisé(s) sans voix")
    return rc


def main() -> int:
    ap = argparse.ArgumentParser(description="Cortana watch → bus urgent")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--seed", action="store_true")
    args = ap.parse_args()
    try:
        return run(dry=args.dry, seed=args.seed)
    except Exception as e:
        print(f"[watch:ERR] {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
