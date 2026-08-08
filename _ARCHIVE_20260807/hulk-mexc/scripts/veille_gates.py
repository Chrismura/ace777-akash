#!/usr/bin/env python3
"""
Gates Hulk P0 — anti-reentry (stop cache) + skip RED veille.

Fichiers (dans hulk-mexc/runs/) :
  .hulk_stop_cache.json   — écrit par paper au stop
  .veille_status.json     — écrit par scoreur (ou refresh léger)

Écriture JSON : TOUJOURS via `_safe_write` (.tmp + Path.replace) — atomique POSIX.
  → P1 race condition = CLOSED (2026-07-30). Writers : write_veille_status*,
    stop cache, digests via write_veille_status_from_digest. Lecture : `_safe_load`
    fail-open → {}.

0 API. try/except partout → fail-open (ne bloque pas si fichier HS).
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

NEG_HINT_PREFIXES = (
    "WATCH_PULLBACK",
    "IMPULSE_WAIT",
    "WAIT",
    "AVOID",
    "NO_TRADE",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ts(ts: str) -> datetime:
    ts = (ts or "").strip()
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return datetime.fromisoformat(ts)


def hint_is_negative(hint: str) -> bool:
    h = (hint or "").strip().upper()
    return any(h.startswith(p) for p in NEG_HINT_PREFIXES)


def _safe_load(path: Path) -> dict[str, Any]:
    try:
        if not path.exists():
            return {}
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _safe_write(path: Path, data: dict[str, Any]) -> bool:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
        tmp.replace(path)
        return True
    except Exception:
        return False


# ─── Stop cooldown cache ───


def stop_cache_path(runs: Path) -> Path:
    return runs / ".hulk_stop_cache.json"


def record_stop(runs: Path, pair: str, ts: Optional[str] = None) -> None:
    path = stop_cache_path(runs)
    cache = _safe_load(path)
    prev = cache.get(pair) if isinstance(cache.get(pair), dict) else {}
    count = int(prev.get("count") or 0) + 1
    cache[pair] = {
        "last_stop_ts": ts or utc_now(),
        "count": count,
    }
    _safe_write(path, cache)


def is_cooldown(
    runs: Path, pair: str, cooldown_hours: float = 2.0
) -> tuple[bool, str]:
    """True si la paire est encore en cooldown post-stop."""
    cache = _safe_load(stop_cache_path(runs))
    info = cache.get(pair)
    if not isinstance(info, dict) or not info.get("last_stop_ts"):
        return False, ""
    try:
        last = parse_ts(str(info["last_stop_ts"]))
        until = last + timedelta(hours=float(cooldown_hours))
        now = datetime.now(timezone.utc)
        if now < until:
            left = (until - now).total_seconds() / 60.0
            return True, (
                f"stop@{info['last_stop_ts']} "
                f"count={info.get('count', 1)} left≈{left:.0f}m"
            )
    except Exception:
        return False, ""
    return False, ""


# ─── Veille status (hot JSON) ───


def veille_status_path(runs: Path) -> Path:
    return runs / ".veille_status.json"


def build_veille_status_from_jsonl(
    jsonl_path: Path,
    *,
    max_lines: int = 800,
    red_lookback_min: int = 30,
) -> dict[str, Any]:
    """
    Construit un status compact par paire (dernières lignes JSONL seulement).
    RED si dernier hint négatif < red_lookback_min (sinon on marque quand même
    le dernier hint ; paper ignore si ts trop vieux).
    """
    out: dict[str, Any] = {
        "_meta": {
            "updated": utc_now(),
            "source": str(jsonl_path.name),
            "red_lookback_min": red_lookback_min,
        }
    }
    if not jsonl_path.exists():
        return out

    try:
        raw = jsonl_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return out

    lines = raw[-max_lines:] if len(raw) > max_lines else raw
    # last hint per pair
    last: dict[str, dict[str, Any]] = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        batch_ts = o.get("ts") or utc_now()
        for c in o.get("calls") or []:
            pair = c.get("pair")
            if not pair:
                continue
            hint = str(c.get("hint") or "")
            last[pair] = {
                "ts": batch_ts,
                "hint": hint,
                "negative": hint_is_negative(hint),
                "tension": c.get("tension"),
                "priority": c.get("priority"),
            }

    now = datetime.now(timezone.utc)
    for pair, info in last.items():
        try:
            age_min = (now - parse_ts(str(info["ts"]))).total_seconds() / 60.0
        except Exception:
            age_min = 9999.0
        neg = bool(info.get("negative"))
        # Status pour Hulk : RED seulement si négatif ET frais
        if neg and age_min <= float(red_lookback_min):
            status = "RED"
        elif neg:
            status = "AMBER"  # caution stale — paper ne bloque pas
        else:
            status = "GREEN"
        short = (info.get("hint") or "").split("—")[0].strip()
        out[pair] = {
            "status": status,
            "ts": info["ts"],
            "reason": short or status,
            "age_min": round(age_min, 1),
        }
    return out


def write_veille_status(
    runs: Path,
    jsonl_path: Optional[Path] = None,
    *,
    red_lookback_min: int = 30,
) -> Path:
    jl = jsonl_path or (runs / "VEILLE_CALLS.jsonl")
    data = build_veille_status_from_jsonl(
        jl, red_lookback_min=red_lookback_min
    )
    path = veille_status_path(runs)
    _safe_write(path, data)
    return path


def write_veille_status_from_digest(
    runs: Path,
    dig: dict[str, Any],
    *,
    red_lookback_min: int = 30,
) -> Path:
    """
    Hot path live : écrit .veille_status.json depuis le digest courant
    (même si VEILLE_CALLS n'est pas append — dédup).
    """
    out: dict[str, Any] = {
        "_meta": {
            "updated": utc_now(),
            "source": "DIGEST_LIVE",
            "red_lookback_min": red_lookback_min,
            "digest_ts": dig.get("ts"),
        }
    }
    dig_ts = str(dig.get("ts") or utc_now())
    now = datetime.now(timezone.utc)
    try:
        base_age = (now - parse_ts(dig_ts)).total_seconds() / 60.0
    except Exception:
        base_age = 0.0

    for r in dig.get("pairs") or []:
        pair = r.get("pair")
        if not pair or r.get("error"):
            continue
        hint = str(r.get("hint") or "")
        if hint in ("IDLE", "ERR", ""):
            continue
        neg = hint_is_negative(hint)
        if neg and base_age <= float(red_lookback_min):
            status = "RED"
        elif neg:
            status = "AMBER"
        else:
            status = "GREEN"
        out[pair] = {
            "status": status,
            "ts": dig_ts,
            "reason": hint.split("—")[0].strip() or status,
            "age_min": round(base_age, 1),
        }
    path = veille_status_path(runs)
    _safe_write(path, out)
    return path


# ─── Dédup hints (VEILLE_CALLS) ───


def hint_cooldown_path(runs: Path) -> Path:
    return runs / ".hint_cooldown.json"


def hint_type_key(hint: str) -> str:
    return (hint or "").split("—")[0].strip().upper() or "UNKNOWN"


def filter_calls_cooldown(
    runs: Path,
    calls: list[dict[str, Any]],
    *,
    cooldown_sec: float = 3600.0,
) -> tuple[list[dict[str, Any]], list[str]]:
    """
    Garde seulement les hints dont pair:type n'a pas été émis
    depuis cooldown_sec. Persiste dans .hint_cooldown.json.
    """
    path = hint_cooldown_path(runs)
    cache = _safe_load(path)
    now = datetime.now(timezone.utc).timestamp()
    kept: list[dict[str, Any]] = []
    skipped: list[str] = []
    for c in calls:
        pair = str(c.get("pair") or "")
        htype = hint_type_key(str(c.get("hint") or ""))
        key = f"{pair}:{htype}"
        last = float(cache.get(key) or 0)
        if last and (now - last) < float(cooldown_sec):
            skipped.append(key)
            continue
        kept.append(c)
        cache[key] = now
    if kept:
        # purge entrées > 7j
        cutoff = now - 7 * 86400
        cache = {k: v for k, v in cache.items() if float(v or 0) >= cutoff}
        _safe_write(path, cache)
    return kept, skipped


def refresh_veille_status_if_stale(
    runs: Path,
    *,
    refresh_sec: float = 60.0,
    red_lookback_min: int = 30,
) -> None:
    """Régénère .veille_status.json si absent ou trop vieux."""
    path = veille_status_path(runs)
    try:
        if path.exists():
            age = datetime.now(timezone.utc).timestamp() - path.stat().st_mtime
            if age < refresh_sec:
                return
    except Exception:
        pass
    write_veille_status(runs, red_lookback_min=red_lookback_min)


def veille_blocks(
    runs: Path,
    pair: str,
    *,
    window_min: int = 30,
) -> tuple[bool, str]:
    """
    True si status RED frais → skip buy.
    Absent / corrompu / trop vieux / non-RED → False (fail-open).
    """
    data = _safe_load(veille_status_path(runs))
    info = data.get(pair)
    if not isinstance(info, dict):
        return False, ""
    if str(info.get("status") or "").upper() != "RED":
        return False, ""
    try:
        status_ts = parse_ts(str(info.get("ts") or ""))
        age = datetime.now(timezone.utc) - status_ts
        if age > timedelta(minutes=float(window_min)):
            return False, ""
    except Exception:
        return False, ""
    reason = str(info.get("reason") or "RED")
    return True, reason


def entry_gate_check(
    runs: Path,
    pair: str,
    *,
    cooldown_hours: float = 2.0,
    skip_red: bool = True,
    window_min: int = 30,
    refresh_sec: float = 60.0,
) -> tuple[bool, str, str]:
    """
    Returns (allowed, code, detail).
    code: OK | SKIP_COOLDOWN | SKIP_VEILLE_RED
    """
    cool, detail = is_cooldown(runs, pair, cooldown_hours=cooldown_hours)
    if cool:
        return False, "SKIP_COOLDOWN", detail

    if skip_red:
        refresh_veille_status_if_stale(
            runs, refresh_sec=refresh_sec, red_lookback_min=window_min
        )
        blocked, reason = veille_blocks(runs, pair, window_min=window_min)
        if blocked:
            return False, "SKIP_VEILLE_RED", reason

    return True, "OK", ""
