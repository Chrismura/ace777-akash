#!/usr/bin/env python3
"""
Digest veille Hulk — MEXC (source trading) + DefiLlama (amont, best-effort).

Sortie Qwen-friendly :
  runs/DIGEST_<ts>.md
  runs/DIGEST_<ts>.json
  runs/DIGEST_LATEST.md  (symlink logique = copie)

Aucune clé requise pour le v0. ~/.mexc.env lu si présent (prépare live).
Genesis ACE / NUAGE : non touché.
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "defaults.env"
INV = ROOT / "data" / "universe_mexc_inventory.csv"
RUNS = ROOT / "runs"
MEXC_ENV = Path.home() / ".mexc.env"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ace_sense_mexc import book_sense, tension_score  # noqa: E402
from veille_gates import (  # noqa: E402
    filter_calls_cooldown,
    write_veille_status_from_digest,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_env(path: Path) -> dict:
    d: dict[str, str] = {}
    if not path.exists():
        return d
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        d[k.strip()] = v.strip()
    return d


# ─── Robustesse réseau (WiFi/alpage) : timeout strict + back-off + circuit-breaker ───
_CB: dict[str, dict[str, float]] = {}


def _host_of(url: str) -> str:
    return urllib.parse.urlparse(url).netloc


def _circuit_open(host: str, failures: int, cooldown_sec: float) -> bool:
    st = _CB.get(host)
    if not st:
        return False
    if st["fails"] >= failures:
        if time.time() - st["opened_at"] < cooldown_sec:
            return True
        _CB.pop(host, None)  # cooldown écoulé → on réessaie
    return False


def _record_failure(host: str) -> None:
    st = _CB.setdefault(host, {"fails": 0, "opened_at": 0.0})
    st["fails"] += 1
    st["opened_at"] = time.time()


def _record_success(host: str) -> None:
    _CB.pop(host, None)


def http_json(
    url: str,
    timeout: float = 12.0,
    retries: int = 3,
    *,
    failures: int = 3,
    cooldown_sec: float = 60.0,
) -> Any:
    host = _host_of(url)
    last: Optional[Exception] = None
    for i in range(retries):
        if _circuit_open(host, failures, cooldown_sec):
            raise TimeoutError(
                f"circuit-open {host} (réseau dégradé, pause {int(cooldown_sec)}s)"
            )
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hulk-digest/0.1"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                _record_success(host)
                return json.loads(r.read().decode())
        except Exception as e:
            last = e
            # 4xx/5xx = le serveur répond → PAS une panne réseau (ne compte pas pour le circuit)
            if not isinstance(e, urllib.error.HTTPError):
                _record_failure(host)
            time.sleep(min(2.0 ** i, 8.0))  # back-off exponentiel 1→2→4s (plafonné 8s)
    raise last  # type: ignore[misc]


def pairs_from_cfg(cfg: dict) -> list[str]:
    raw = cfg.get("PAPER_PAIRS", "").strip()
    if raw:
        core = [p.strip().upper() for p in raw.split(",") if p.strip()]
    else:
        core = ["XRPUSDT", "QAITUSDT"]
    watch = [
        p.strip().upper()
        for p in cfg.get("PAPER_WATCH_PAIRS", "").split(",")
        if p.strip()
    ]
    # digest = core + watch (dédup)
    out = []
    for p in core + watch:
        if p not in out:
            out.append(p)
    return out


def trade_pairs_from_cfg(cfg: dict) -> list[str]:
    """Paires réellement tradées par paper (sans WATCH-only)."""
    raw = cfg.get("PAPER_PAIRS", "").strip()
    if raw:
        return [p.strip().upper() for p in raw.split(",") if p.strip()]
    return ["XRPUSDT", "QAITUSDT"]


def ticker_24h(pair: str) -> dict:
    q = urllib.parse.urlencode({"symbol": pair})
    j = http_json(f"https://api.mexc.com/api/v3/ticker/24hr?{q}")
    return {
        "last": float(j.get("lastPrice") or j.get("close") or 0),
        "chg_pct": float(j.get("priceChangePercent") or 0),
        "high": float(j.get("highPrice") or 0),
        "low": float(j.get("lowPrice") or 0),
        "quote_vol": float(j.get("quoteVolume") or 0),
        "base_vol": float(j.get("volume") or 0),
    }


def kline_move(pair: str) -> dict:
    q = urllib.parse.urlencode({"symbol": pair, "interval": "60m", "limit": 24})
    kl = http_json(f"https://api.mexc.com/api/v3/klines?{q}")
    highs = [float(c[2]) for c in kl]
    lows = [float(c[3]) for c in kl]
    closes = [float(c[4]) for c in kl]
    if not closes:
        return {"move6": 0.0, "move24": 0.0, "dd6": 0.0, "cadence": 3.0}
    h6, l6 = highs[-6:], lows[-6:]
    peak6, trough6 = max(h6), min(l6)
    peak24, trough24 = max(highs), min(lows)
    px = closes[-1]
    move6 = (peak6 / trough6 - 1) * 100 if trough6 else 0
    move24 = (peak24 / trough24 - 1) * 100 if trough24 else 0
    dd6 = (1 - px / peak6) * 100 if peak6 else 0
    return {
        "move6": round(move6, 2),
        "move24": round(move24, 2),
        "dd6": round(dd6, 2),
        "cadence": round(max(move24 / 4, 2.0), 2),
        "price": px,
    }


def defillama_hint(symbol: str) -> dict:
    """
    Best-effort DefiLlama (API DeFi — pas Ollama/LLM).
    Échec → note claire, jamais bloquant pour le digest.
    """
    base = symbol.replace("USDT", "").upper()
    aliases = {
        "W": "wormhole",
        "ZBCN": "zebec-protocol",
        "RED": "redstone-oracles",
        "SEI": "sei",
        "HBAR": "hedera",
        "XRP": "ripple",
        "XLM": "stellar",
        "PYTH": "pyth-network",
        "BIO": "bioprotocol",
        "QNT": "quant-network",
        "ONDO": "ondo-finance",
        "FLUID": "fluid",
    }
    slug = aliases.get(base)
    out: dict[str, Any] = {
        "symbol": base,
        "slug": slug,
        "tvl": None,
        "note": "no_map" if not slug else "pending",
    }
    if not slug:
        return out
    try:
        j = http_json(f"https://api.llama.fi/protocol/{slug}", timeout=20, retries=2)
        tvl = j.get("currentChainTvls") or j.get("tvl")
        if isinstance(tvl, dict):
            out["tvl"] = round(
                sum(float(v) for v in tvl.values() if isinstance(v, (int, float))), 0
            )
        elif isinstance(tvl, (int, float)):
            out["tvl"] = float(tvl)
        elif isinstance(tvl, list) and tvl:
            last = tvl[-1]
            out["tvl"] = (
                last.get("totalLiquidityUSD") if isinstance(last, dict) else None
            )
        out["note"] = "ok" if out["tvl"] is not None else "empty_tvl"
        out["url"] = f"https://defillama.com/protocol/{slug}"
    except Exception as e:
        msg = str(e)
        if "400" in msg or "404" in msg:
            out["note"] = "n/a"
        else:
            out["note"] = f"miss:{type(e).__name__}"
    return out


def priority_score(row: dict) -> float:
    """Score simple pour tri Qwen : move + vol + tension − pénalité spread."""
    t = float(row.get("tension") or 0)
    m = float(row.get("move6") or 0)
    vol = float(row.get("quote_vol") or 0)
    sp = float(row.get("spread_bps") or 0)
    dd = float(row.get("dd6") or 0)
    score = t * 2 + m * 0.15 + min(vol / 1e5, 20) + dd * 0.1 - min(sp / 50, 8)
    if row.get("pair") in {
        "RIZEUSDT",
        "ZBCNUSDT",
        "WUSDT",
        "REDUSDT",
        "QAITUSDT",
        "CCUSDT",
        "PYTHUSDT",
        "BIOUSDT",
        "KITEUSDT",
        "CHIPUSDT",
        "RWAINCUSDT",
        "EDELUSDT",
    }:
        score += 3
    return round(score, 2)


def build_digest(
    cfg: dict, *, with_llama: bool = True, deadline_sec: float = 90.0
) -> dict:
    pairs = pairs_from_cfg(cfg)
    mexc_meta = load_env(MEXC_ENV)
    has_keys = bool(mexc_meta.get("MEXC_API_KEY") and mexc_meta.get("MEXC_API_SECRET"))
    rows = []
    degraded = False
    t0 = time.time()
    for pair in pairs:
        if time.time() - t0 > deadline_sec:
            degraded = True
            rows.append(
                {"pair": pair, "error": "scan_deadline", "priority": -1, "hint": "ERR"}
            )
            continue
        try:
            t24 = ticker_24h(pair)
            kl = kline_move(pair)
            sense = book_sense(pair, http_json)
            tens = tension_score(kl["move6"], kl["cadence"], kl["dd6"])
            base = pair.replace("USDT", "")
            llama = (
                defillama_hint(pair)
                if with_llama
                else {"symbol": base, "slug": None, "tvl": None, "note": "skipped_fast"}
            )
            row = {
                "pair": pair,
                "base": base,
                "last": t24["last"] or kl.get("price"),
                "chg_24h_pct": round(t24["chg_pct"], 2),
                "quote_vol": round(t24["quote_vol"], 2),
                "high_24h": t24["high"],
                "low_24h": t24["low"],
                "move6": kl["move6"],
                "move24": kl["move24"],
                "dd6": kl["dd6"],
                "cadence": kl["cadence"],
                "tension": tens,
                "spread_bps": sense.get("spread_bps"),
                "imbalance": sense.get("imbalance"),
                "wall_bid_usdt": sense.get("wall_bid_usdt"),
                "wall_ask_usdt": sense.get("wall_ask_usdt"),
                "defillama": llama,
            }
            row["priority"] = priority_score(row)
            if tens >= 2.5 and kl["dd6"] >= 5:
                row["hint"] = "WATCH_PULLBACK — tension haute + reflux"
            elif tens >= 2.0 and kl["move6"] >= 8 and kl["dd6"] < 2:
                row["hint"] = "IMPULSE_WAIT — spike en cours, pas chase"
            elif t24["chg_pct"] <= -8:
                row["hint"] = "COOLING_CANDIDATE — rouge 24h"
            else:
                row["hint"] = "IDLE"
            rows.append(row)
            time.sleep(0.12)
        except Exception as e:
            rows.append({"pair": pair, "error": str(e), "priority": -1, "hint": "ERR"})
    rows.sort(key=lambda r: -float(r.get("priority") or -1))
    return {
        "ts": utc_now(),
        "degraded": degraded,
        "mexc_keys_loaded": has_keys,
        "source_truth": "MEXC spot",
        "upstream": ["DefiLlama best-effort"],
        "supervisor": "Qwen (lire digest — ne trade pas — piste séparée)",
        "trade_pairs": trade_pairs_from_cfg(cfg),
        "watch_pairs": [
            p.strip().upper()
            for p in cfg.get("PAPER_WATCH_PAIRS", "").split(",")
            if p.strip()
        ],
        "pairs": rows,
    }


def _calls_signature(calls: list) -> str:
    """Signature stable pour ne logger que si le signal change."""
    parts = [f"{c.get('pair')}|{c.get('hint','')}" for c in calls]
    return "|".join(parts)


def collect_calls(dig: dict) -> list:
    calls = []
    for r in dig.get("pairs") or []:
        hint = r.get("hint") or ""
        if hint in ("IDLE", "ERR", "") or r.get("error"):
            continue
        calls.append(
            {
                "pair": r.get("pair"),
                "hint": hint,
                "tension": r.get("tension"),
                "move6": r.get("move6"),
                "dd6": r.get("dd6"),
                "chg_24h_pct": r.get("chg_24h_pct"),
                "priority": r.get("priority"),
                "quote_vol": r.get("quote_vol"),
            }
        )
    return calls[:5]


def append_veille_calls_if_new(
    dig: dict,
    prev_sig: str,
    *,
    hint_cooldown_sec: float = 3600.0,
) -> tuple[Path, str, bool]:
    """
    N'écrit dans VEILLE_CALLS que si quelque chose d'intéressant
    apparaît ou change — et passe le cooldown 1h par paire:type (dédup).
    """
    path = RUNS / "VEILLE_CALLS.jsonl"
    calls_raw = collect_calls(dig)
    sig = _calls_signature(calls_raw)
    if not calls_raw:
        return path, sig, False
    if sig == prev_sig:
        return path, sig, False
    calls, skipped = filter_calls_cooldown(
        RUNS, calls_raw, cooldown_sec=hint_cooldown_sec
    )
    if skipped and not calls:
        print(
            f"[{utc_now()}] hint dédup — skip écriture "
            f"({len(skipped)} en cooldown {int(hint_cooldown_sec)}s)"
        )
        return path, sig, False
    if not calls:
        return path, sig, False
    if skipped:
        print(
            f"[{utc_now()}] hint dédup — émis {len(calls)}, "
            f"filtrés {len(skipped)} (cooldown {int(hint_cooldown_sec)}s)"
        )
    entry = {
        "ts": dig.get("ts"),
        "track": "VEILLE_QWEN",
        "n_calls": len(calls),
        "calls": calls,
        "note": "signal nouveau/changé — Qwen peut enrichir VEILLE_QWEN_NOTES.md",
    }
    with path.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    # Alerte courte lisible tout de suite
    alert = RUNS / "VEILLE_ALERT.md"
    lines = [
        f"# VEILLE ALERT — {dig.get('ts')}",
        "",
        "Signal détecté (piste B, sync paper). **Pas un ordre.**",
        "",
    ]
    for c in calls:
        lines.append(
            f"- **{c['pair']}** — {c['hint']}  "
            f"(t={c.get('tension')} m6={c.get('move6')} dd6={c.get('dd6')} "
            f"chg24={c.get('chg_24h_pct')}%)"
        )
    lines += [
        "",
        "→ Lire `DIGEST_LATEST.md` et noter dans `VEILLE_QWEN_NOTES.md` si tu confirmes.",
        "",
    ]
    alert.write_text("\n".join(lines))
    # Append stub daté dans notes Qwen (elle / toi complétez)
    notes = RUNS / "VEILLE_QWEN_NOTES.md"
    stub = (
        f"\n### {dig.get('ts')} — ALERT auto\n"
        + "\n".join(
            f"- {c['pair']}: {c['hint']}" for c in calls
        )
        + "\n(compléter: confirmé ? risque ?)\n"
    )
    with notes.open("a") as f:
        f.write(stub)
    return path, sig, True


def paper_aligned_loop_sec(cfg: dict) -> int:
    """
    Pause entre deux scans complets.
    0 = enchaîne tout de suite (mode direct / live).
    Le vrai délai ≈ durée du scan MEXC (~20–40s pour 15 paires), pas une attente artificielle.
    """
    override = (cfg.get("DIGEST_LOOP_SEC") or "live").strip().lower()
    if override in ("live", "direct", "0", "auto"):
        return 0
    return max(0, int(float(override)))


def to_markdown(dig: dict) -> str:
    lines = [
        f"# Hulk DIGEST — {dig['ts']}",
        "",
    ]
    if dig.get("degraded"):
        lines += [
            "> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.",
            "",
        ]
    lines += [
        f"- **Piste :** VEILLE (séparée du paper Hulk)",
        f"- Source trading : **{dig['source_truth']}**",
        f"- Amont : {', '.join(dig['upstream'])} (= API DeFi, **pas** Llama LLM)",
        f"- Clés MEXC (`~/.mexc.env`) : {'oui' if dig['mexc_keys_loaded'] else 'non (public OK)'}",
        f"- Superviseur : {dig['supervisor']}",
        f"- Trade CORE (réf.) : {', '.join(dig.get('trade_pairs') or [])}",
        f"- Watch only : {', '.join(dig.get('watch_pairs') or []) or '—'}",
        "",
        "## Priorité (haut → bas)",
        "",
        "| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |",
        "|------|------|---------|--------|------|--------|----------|------------|-----------|",
    ]
    for r in dig["pairs"]:
        if r.get("error"):
            lines.append(
                f"| {r['pair']} | ERR | — | — | — | — | — | — | {str(r['error'])[:40]} |"
            )
            continue
        ll = r.get("defillama") or {}
        ll_s = ll.get("note", "")
        if ll.get("tvl") is not None:
            ll_s = f"tvl≈{ll['tvl']:,.0f}"
        lines.append(
            f"| {r['pair']} | {r.get('hint','')} | {r.get('tension')} | {r.get('move6')} | "
            f"{r.get('dd6')} | {r.get('chg_24h_pct')} | {r.get('quote_vol')} | "
            f"{r.get('spread_bps')} | {ll_s} |"
        )
    lines += [
        "",
        "## Consignes Qwen (manuel — ne pilote pas le paper)",
        "1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).",
        "2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.",
        "3. Signaler murs ask/bid ou spread dangereux.",
        "4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.",
        "",
        "## Séparation des pistes",
        "- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)",
        "- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)",
        "- Fin de campagne : `docs/CONFRONTATION.md`",
        "",
    ]
    return "\n".join(lines)


def run_once(cfg: dict, *, prev_sig: str = "", cycle: int = 0, loop: bool = False) -> tuple[dict, str]:
    """
    Digest sync paper.
    - Toujours met à jour DIGEST_LATEST (tableau de bord).
    - N'écrit VEILLE_CALLS / ALERT / notes que si signal NOUVEAU.
    """
    # DefiLlama seulement 1 cycle sur 5 en boucle (sinon trop lent vs paper)
    with_llama = (not loop) or (cycle % 5 == 0)
    print(
        f"[{utc_now()}] digest MEXC… piste VEILLE "
        f"(llama={'ON' if with_llama else 'skip'})"
    )
    deadline = float(cfg.get("SCAN_DEADLINE_SEC", "90") or 90)
    dig = build_digest(cfg, with_llama=with_llama, deadline_sec=deadline)
    if dig.get("degraded"):
        print(
            f"[{utc_now()}] ⚠ scan dégradé (deadline {deadline:.0f}s atteinte) — réseau lent, "
            f"données partielles"
        )
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    # JSON/MD complets : latest toujours ; snapshot fichier seulement si alerte ou 1er
    latest = RUNS / "DIGEST_LATEST.md"
    md = to_markdown(dig)
    latest.write_text(md)
    # Hot status pour paper skip RED — chaque cycle (indépendant de la dédup JSONL)
    try:
        write_veille_status_from_digest(RUNS, dig, red_lookback_min=30)
    except Exception as e:
        print(f"[{utc_now()}] veille_status warn: {e}")
    cooldown = float(cfg.get("HINT_COOLDOWN_SEC", "3600"))
    calls_path, sig, wrote = append_veille_calls_if_new(
        dig, prev_sig, hint_cooldown_sec=cooldown
    )
    if wrote:
        jp = RUNS / f"DIGEST_{ts}.json"
        mp = RUNS / f"DIGEST_{ts}.md"
        jp.write_text(json.dumps(dig, indent=2))
        mp.write_text(md)
        print(md)
        print(f"\n*** SIGNAL → écrit {calls_path.name} + VEILLE_ALERT.md + notes ***")
        print(f"écrit: {mp}")
    else:
        n_hot = len(collect_calls(dig))
        print(
            f"[{utc_now()}] digest OK — "
            f"{'même signal, pas de re-écriture' if n_hot else 'rien à signaler (IDLE)'} "
            f"| latest={latest.name}"
        )
    return dig, sig


def main() -> int:
    cfg = load_env(CFG)
    RUNS.mkdir(parents=True, exist_ok=True)
    # Mode direct : --loop / --live = enchaîne les scans sans pause 60s
    loop_sec = -1  # -1 = one-shot
    args = sys.argv[1:]
    live = "--live" in args or "--loop" in args
    if live:
        if "--loop" in args:
            i = args.index("--loop")
            if i + 1 < len(args) and not args[i + 1].startswith("-"):
                loop_sec = int(float(args[i + 1]))
            else:
                loop_sec = paper_aligned_loop_sec(cfg)
        else:
            loop_sec = paper_aligned_loop_sec(cfg)
    else:
        raw = (cfg.get("DIGEST_LOOP_SEC") or "0").strip().lower()
        if raw in ("live", "direct", "auto"):
            loop_sec = -1  # une passe sauf si --live/--loop
        elif raw in ("0", ""):
            loop_sec = -1
        else:
            loop_sec = int(float(raw))

    stop = ROOT / "STOP_DIGEST"
    prev_sig = ""
    cycle = 0
    if loop_sec >= 0:
        pause = f"{loop_sec}s" if loop_sec > 0 else "0s (direct — enchaîne dès scan fini)"
        print(
            f"[{utc_now()}] VEILLE LIVE pause={pause} | "
            f"écrit seulement si signal nouveau | stop: touch STOP_DIGEST"
        )
        print(
            "Note: Qwen n'est pas branchée à MEXC. Ce script = ses yeux en boucle. "
            "Délai mini ≈ temps de scan des paires (~20–40s)."
        )
    while True:
        if stop.exists():
            print(f"[{utc_now()}] STOP_DIGEST — fin veille")
            break
        t0 = time.time()
        try:
            _, prev_sig = run_once(
                cfg, prev_sig=prev_sig, cycle=cycle, loop=(loop_sec >= 0)
            )
        except Exception as e:
            print(f"[{utc_now()}] DIGEST_ERR: {e}", file=sys.stderr)
        cycle += 1
        if loop_sec < 0:
            break
        elapsed = time.time() - t0
        if loop_sec > 0:
            print(
                f"[{utc_now()}] scan {elapsed:.0f}s — pause {loop_sec}s "
                f"(touch STOP_DIGEST)"
            )
            time.sleep(loop_sec)
        else:
            print(
                f"[{utc_now()}] scan {elapsed:.0f}s — relance directe "
                f"(touch STOP_DIGEST)"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
