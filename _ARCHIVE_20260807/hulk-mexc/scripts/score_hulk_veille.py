#!/usr/bin/env python3
"""
Scoreur P0 — croise paper Hulk ↔ hints veille (0 API, lecture seule).

Lit :
  runs/PAPER_*.csv (dernier ou --paper)
  runs/VEILLE_CALLS.jsonl

Écrit :
  runs/HULK_SCORE_LATEST.md
  runs/.veille_status.json   (hot path pour paper skip RED)
  optionnel : Obsidian Swarm_Bus/03_HULK_SCORE.md (--obsidian)

Ne modifie pas digest_watch.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
DEFAULT_OBSIDIAN = Path.home() / "Documents/Obsidian_ACE777/Swarm_Bus/03_HULK_SCORE.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from veille_gates import write_veille_status  # noqa: E402

# Hints « frein » (veille dit d’attendre / pas chase)
NEG_HINT_PREFIXES = (
    "WATCH_PULLBACK",
    "IMPULSE_WAIT",
    "WAIT",
    "AVOID",
    "NO_TRADE",
)


def parse_ts(ts: str) -> datetime:
    ts = ts.strip()
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return datetime.fromisoformat(ts)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def hint_is_negative(hint: str) -> bool:
    h = (hint or "").strip().upper()
    return any(h.startswith(p) for p in NEG_HINT_PREFIXES)


@dataclass
class FlatHint:
    ts: datetime
    pair: str
    hint: str
    tension: float
    priority: float


@dataclass
class TradeScore:
    pair: str
    ts: datetime
    event: str
    regime: str
    price: float
    pnl_usdt: float
    reason: str
    score: str  # GREEN | YELLOW | RED | AMBER
    detail: str
    n_neg_30m: int
    n_neg_6h: int
    sell_pnl: Optional[float]


def load_paper_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_flat_hints(path: Path) -> list[FlatHint]:
    out: list[FlatHint] = []
    if not path.exists():
        return out
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            batch_ts = parse_ts(o["ts"])
            for c in o.get("calls") or []:
                pair = c.get("pair") or ""
                if not pair:
                    continue
                out.append(
                    FlatHint(
                        ts=batch_ts,
                        pair=pair,
                        hint=str(c.get("hint") or ""),
                        tension=float(c.get("tension") or 0),
                        priority=float(c.get("priority") or 0),
                    )
                )
    out.sort(key=lambda x: x.ts)
    return out


def resolve_paper(path: Optional[Path]) -> Path:
    if path:
        return path
    cands = sorted(RUNS.glob("PAPER_*V*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    # préfère session avec le plus d'events / récente
    all_csv = sorted(RUNS.glob("PAPER_*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not all_csv:
        raise SystemExit(f"Aucun PAPER_*.csv dans {RUNS}")
    return all_csv[0]


def score_buy(
    buy: dict[str, str],
    hints: list[FlatHint],
    sells_by_pair: dict[str, list[dict[str, str]]],
    window_min: int,
    stale_h: int,
) -> TradeScore:
    pair = buy["pair"]
    t = parse_ts(buy["ts"])
    t30 = t - timedelta(minutes=window_min)
    t6h = t - timedelta(hours=stale_h)

    neg_30 = [
        h
        for h in hints
        if h.pair == pair and t30 <= h.ts < t and hint_is_negative(h.hint)
    ]
    neg_6h = [
        h
        for h in hints
        if h.pair == pair and t6h <= h.ts < t and hint_is_negative(h.hint)
    ]
    any_pair = [h for h in hints if h.pair == pair and h.ts < t]

    # PnL realized later on this pair (first sell after buy)
    sell_pnl: Optional[float] = None
    for s in sells_by_pair.get(pair, []):
        st = parse_ts(s["ts"])
        if st >= t:
            try:
                sell_pnl = float(s.get("pnl_usdt") or 0)
            except ValueError:
                sell_pnl = None
            break

    if neg_30:
        last = neg_30[-1]
        mins = int((t - last.ts).total_seconds() // 60)
        score = "RED"
        detail = (
            f"Veille {last.hint.split('—')[0].strip()} "
            f"{mins} min avant (×{len(neg_30)} dans {window_min}m)"
        )
    elif neg_6h:
        last = neg_6h[-1]
        hrs = (t - last.ts).total_seconds() / 3600
        score = "AMBER"
        detail = (
            f"Pas de hint dans {window_min}m, mais caution stale "
            f"({last.hint.split('—')[0].strip()} il y a {hrs:.1f}h, ×{len(neg_6h)}/{stale_h}h)"
        )
    elif not any_pair:
        # aucune alerte veille sur cette paire avant le trade
        score = "YELLOW"
        detail = "Blind spot veille — aucune alerte sur cette paire avant le trade"
    else:
        score = "GREEN"
        detail = (
            f"Pas d'alerte négative dans {window_min}m "
            f"(veille a déjà parlé de la paire avant, sans frein récent)"
        )

    return TradeScore(
        pair=pair,
        ts=t,
        event=buy.get("event") or "BUY",
        regime=buy.get("regime") or "",
        price=float(buy.get("price") or 0),
        pnl_usdt=float(buy.get("pnl_usdt") or 0),
        reason=buy.get("reason") or "",
        score=score,
        detail=detail,
        n_neg_30m=len(neg_30),
        n_neg_6h=len(neg_6h),
        sell_pnl=sell_pnl,
    )


def emoji(score: str) -> str:
    return {"GREEN": "🟢", "YELLOW": "🟡", "RED": "🔴", "AMBER": "🟠"}.get(score, "⬜")


def render_md(
    paper: Path,
    scores: list[TradeScore],
    hints: list[FlatHint],
    window_min: int,
    stale_h: int,
) -> str:
    counts = {"RED": 0, "AMBER": 0, "YELLOW": 0, "GREEN": 0}
    for s in scores:
        counts[s.score] = counts.get(s.score, 0) + 1

    red_then_loss = [
        s
        for s in scores
        if s.score == "RED" and s.sell_pnl is not None and s.sell_pnl < 0
    ]
    realized = [s.sell_pnl for s in scores if s.sell_pnl is not None]
    sum_realized = sum(realized) if realized else 0.0

    lines = [
        "---",
        f"ts: {utc_now()}",
        "agent: score_hulk_veille",
        "mode: P0_read_only",
        f"paper: {paper.name}",
        f"window_min: {window_min}",
        f"stale_hours: {stale_h}",
        f"n_buys: {len(scores)}",
        f"n_hints_flat: {len(hints)}",
        "---",
        "",
        f"# Score Hulk ↔ Veille — `{paper.name}`",
        "",
        f"Généré : `{utc_now()}` · **0 API** · lecture seule.",
        "",
        "## Légende",
        "",
        f"- 🔴 **RED** — hint négatif (`WATCH_PULLBACK` / `IMPULSE_WAIT`…) dans les **{window_min} min** avant le BUY",
        f"- 🟠 **AMBER** — pas de hint {window_min}m, mais caution dans les **{stale_h} h** (stale)",
        "- 🟡 **YELLOW** — blind spot : la veille n’a jamais parlé de cette paire avant le trade",
        f"- 🟢 **GREEN** — pas de frein veille dans {window_min}m (et la paire était déjà connue)",
        "",
        "> Correction vs pitch externe : RWAINC/QAIT early = **YELLOW** (veille après le buy), pas RED. "
        "KITE GREEN ≠ « la veille confirme un long » : ça veut dire *pas de frein récent* "
        "(les vieux WATCH_PULLBACK hors fenêtre ne comptent plus).",
        "",
        "## Synthèse",
        "",
        f"| Score | n |",
        f"|-------|---|",
        f"| 🔴 RED | {counts['RED']} |",
        f"| 🟠 AMBER | {counts['AMBER']} |",
        f"| 🟡 YELLOW | {counts['YELLOW']} |",
        f"| 🟢 GREEN | {counts['GREEN']} |",
        "",
        f"- BUY scorés : **{len(scores)}**",
        f"- Hints plats veille : **{len(hints)}**",
        f"- RED puis stop négatif (preuve confrontation) : **{len(red_then_loss)}**",
        f"- Somme PnL des sells liés (1er sell après buy) : **{sum_realized:+.2f} USDT** "
        f"(incomplet si positions encore ouvertes)",
        "",
        "## Tableau",
        "",
        "| Paire | Heure BUY (UTC) | Score | Résultat sell | Détail |",
        "|-------|-----------------|-------|---------------|--------|",
    ]

    for s in scores:
        res = "ouvert / pas de sell après"
        if s.sell_pnl is not None:
            res = f"{s.sell_pnl:+.2f}$"
        lines.append(
            f"| {s.pair} | {s.ts.strftime('%Y-%m-%d %H:%M')} | "
            f"{emoji(s.score)} {s.score} | {res} | {s.detail} |"
        )

    lines += [
        "",
        "## Lecture",
        "",
        "1. **RED + stop** = Hulk a ignoré un frein veille récent → filtre soft utile.",
        "2. **YELLOW** = veille trop lente / filtre trop étroit (début de session ou paire hors radar).",
        "3. **AMBER** = bruit ou caution trop vieille — ne suffit pas seul à bloquer, à croiser avec prix.",
        "4. Ne pas juger la campagne sur le seul réalisé tant que des positions restent ouvertes.",
        "",
        "## Fichiers source",
        "",
        f"- Paper : `{paper}`",
        f"- Veille : `{RUNS / 'VEILLE_CALLS.jsonl'}`",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Scoreur Hulk ↔ Veille (P0)")
    ap.add_argument("--paper", type=Path, default=None, help="CSV paper (défaut: plus récent)")
    ap.add_argument("--veille", type=Path, default=RUNS / "VEILLE_CALLS.jsonl")
    ap.add_argument("--window-min", type=int, default=30)
    ap.add_argument("--stale-hours", type=int, default=6)
    ap.add_argument(
        "--obsidian",
        type=Path,
        nargs="?",
        const=DEFAULT_OBSIDIAN,
        default=None,
        help=f"Écrit aussi dans Obsidian (défaut si flag: {DEFAULT_OBSIDIAN})",
    )
    ap.add_argument(
        "--status-only",
        action="store_true",
        help="Écrit seulement runs/.veille_status.json (pas de rapport MD)",
    )
    args = ap.parse_args()

    # Hot JSON pour paper (skip RED) — toujours
    status_path = write_veille_status(
        RUNS, args.veille, red_lookback_min=args.window_min
    )
    print(f"OK → {status_path}")
    if args.status_only:
        return 0

    paper = resolve_paper(args.paper)
    rows = load_paper_csv(paper)
    hints = load_flat_hints(args.veille)

    sells_by_pair: dict[str, list[dict[str, str]]] = {}
    for r in rows:
        if r.get("event") == "SELL":
            sells_by_pair.setdefault(r["pair"], []).append(r)

    buys = [r for r in rows if r.get("event") == "BUY"]
    scores = [
        score_buy(b, hints, sells_by_pair, args.window_min, args.stale_hours) for b in buys
    ]

    md = render_md(paper, scores, hints, args.window_min, args.stale_hours)

    out_runs = RUNS / "HULK_SCORE_LATEST.md"
    out_runs.write_text(md, encoding="utf-8")
    stamped = RUNS / f"HULK_SCORE_{utc_now().replace(':', '')}.md"
    stamped.write_text(md, encoding="utf-8")
    print(f"OK → {out_runs}")
    print(f"OK → {stamped}")

    if args.obsidian is not None:
        args.obsidian.parent.mkdir(parents=True, exist_ok=True)
        args.obsidian.write_text(md, encoding="utf-8")
        print(f"OK → {args.obsidian}")

    # résumé terminal
    for s in scores:
        print(f"  {emoji(s.score)} {s.pair} {s.ts.isoformat()} | {s.detail[:70]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
