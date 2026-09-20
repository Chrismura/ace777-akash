#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hulk_stats.py — Stats mesurées de Hulk pour le prompt Cortana (09/09/2026).

Avant : cortana_propose_params n'envoyait que « PnL · positions · bags » — Cortana
ne pouvait rien fonder. Ici : lecture pure du CSV du run courant, aucune écriture,
fail-open total (toute erreur → chaîne vide, le prompt part quand même).

Produit :
  - PnL par régime d'entrée (lots FIFO, comme l'audit 09/09) ;
  - Glissement des stops : nominal (raison `stop-X%`) vs réalisé (|pnl|/notionnel) ;
  - Familles de sorties (trailing / stops / paliers) — le moteur du PnL.
"""
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

EXIT_EVENTS = {"SELL", "SELL_PARTIAL", "EXIT", "CLOSE"}
EXIT_EVENTS_W_BAG = EXIT_EVENTS | {"BAG_SELL"}
_STOP_RE = re.compile(r"stop-([\d.]+)")


def _latest_csv(runs: Path) -> Path | None:
    try:
        cands = sorted(runs.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
        return cands[0] if cands else None
    except Exception:
        return None


def build_stats_block(runs_dir: Path | str, max_chars: int = 2200) -> str:
    """Bloc texte compact pour le prompt Cortana. Fail-open : '' si tout échoue."""
    try:
        runs = Path(runs_dir)
        path = _latest_csv(runs)
        if not path:
            return ""
        rows = list(csv.DictReader(path.open(encoding="utf-8")))
    except Exception:
        return ""

    # --- PnL par régime d'entrée (FIFO par paire) ---
    reg_pnl: dict[str, list[float]] = defaultdict(lambda: [0.0, 0.0])  # [n, pnl]
    stack: dict[str, list[list]] = {}  # pair -> [[regime, qty_restante], ...]
    stop_slip: dict[str, list[float]] = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])
    # pair -> [n, somme_slip_pp, somme_pnl, n_glisses(>0.5pp)]
    fam_pnl: dict[str, float] = defaultdict(float)
    fam_n: dict[str, int] = defaultdict(int)

    for r in rows:
        try:
            ev = r.get("event", "")
            pair = r.get("pair", "")
            qty = float(r.get("qty") or 0)
            px = float(r.get("price") or 0)
            pnl = float(r.get("pnl_usdt") or 0)
        except (TypeError, ValueError):
            continue
        if ev == "BUY":
            stack.setdefault(pair, []).append([(r.get("regime") or "?"), qty])
            continue
        if ev in EXIT_EVENTS_W_BAG:
            # régime des lots consommés (FIFO)
            rem = qty
            regs: dict[str, int] = {}
            while rem > 1e-12 and stack.get(pair):
                lot = stack[pair][0]
                take = min(rem, lot[1])
                regs[lot[0]] = regs.get(lot[0], 0) + 1
                lot[1] -= take
                rem -= take
                if lot[1] <= 1e-12:
                    stack[pair].pop(0)
            for rg in regs:
                reg_pnl[rg][0] += 1
                reg_pnl[rg][1] += pnl / max(1, len(regs))
            # familles
            rs = r.get("reason") or ""
            if rs.startswith("trailing"):
                fam = "trailing_peak"
            elif _STOP_RE.search(rs):
                fam = "stop"
            elif "palier" in rs:
                fam = "rip_palier"
            elif "stake_out" in rs:
                fam = "stake_out"
            else:
                fam = ev.lower()
            fam_pnl[fam] += pnl
            fam_n[fam] += 1
            # glissement stops
            m = _STOP_RE.search(rs)
            if m and px * qty > 0:
                real = abs(pnl) / (px * qty) * 100.0
                slip = real - float(m.group(1))
                s = stop_slip[pair]
                s[0] += 1
                s[1] += slip
                s[2] += pnl
                if slip > 0.5:
                    s[3] += 1

    lines: list[str] = []
    if reg_pnl:
        parts = [f"{rg}={p:+.2f}$/{int(n)}sort" for rg, (n, p) in sorted(reg_pnl.items(), key=lambda x: -x[1][1])]
        lines.append("PNL_PAR_REGIME_ENTREE " + " ".join(parts))
    if stop_slip:
        worst = sorted(stop_slip.items(), key=lambda x: -x[1][1])[:5]
        parts = [f"{p}:moy{sl/n:+.1f}pp(n{int(n)},{int(g)}glisses)" for p, (n, sl, _pnl, g) in worst if n > 0]
        if parts:
            lines.append("GLISSEMENT_STOPS(pire) " + " ".join(parts))
    if fam_pnl:
        parts = [f"{f}={v:+.2f}$" for f, v in sorted(fam_pnl.items(), key=lambda x: -x[1])]
        lines.append("FAMILLES_SORTIE " + " ".join(parts))

    block = "\n".join(lines)[:max_chars]
    return block


if __name__ == "__main__":
    import sys

    d = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "runs"
    b = build_stats_block(d)
    print(b if b else "(aucune stat disponible)")
