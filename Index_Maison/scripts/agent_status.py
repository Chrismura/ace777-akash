#!/usr/bin/env python3
"""
AGENT ON AIR — pastille multi-agents (BOARD / WARM).
Fichier hot: /tmp/ace777_swarm_pids/.agent_status.json
Miroir JS: Index_Maison/architecture/agent_status.js (+ thermo/cockpit optionnel)

Usage:
  python3 agent_status.py heartbeat          # scan ACE/Hulk + stamp CURSOR
  python3 agent_status.py set CURSOR ON_AIR
  python3 agent_status.py set KIMI IDLE
  python3 agent_status.py set ACE RUNNING
  python3 agent_status.py clear CURSOR
  python3 agent_status.py show
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

WS = Path("/Users/christophe/ace777-test-day1/Index_Maison")
ROOT = WS.parent
HOT = Path(
    os.environ.get(
        "ACE777_AGENT_STATUS",
        "/tmp/ace777_swarm_pids/.agent_status.json",
    )
)
MIRROR_JS = WS / "architecture" / "agent_status.js"
MIRROR_JSON = WS / "architecture" / "agent_status.json"
COCKPIT_JS = WS / "cockpit" / "agent_status.js"

KNOWN = ("ACE", "HULK", "CURSOR", "KIMI", "CORTANA", "OTHER")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def _safe_load() -> dict:
    if not HOT.exists():
        return {"updated": utc_now(), "on_air": None, "agents": {}}
    try:
        data = json.loads(HOT.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return {"updated": utc_now(), "on_air": None, "agents": {}}
        data.setdefault("agents", {})
        return data
    except Exception:
        return {"updated": utc_now(), "on_air": None, "agents": {}}


def _safe_write(data: dict) -> Path:
    HOT.parent.mkdir(parents=True, exist_ok=True)
    data["updated"] = utc_now()
    tmp = HOT.with_suffix(HOT.suffix + ".tmp")
    raw = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    tmp.write_text(raw, encoding="utf-8")
    tmp.replace(HOT)
    MIRROR_JSON.parent.mkdir(parents=True, exist_ok=True)
    MIRROR_JSON.write_text(raw, encoding="utf-8")
    js = "window.__AGENT_STATUS__ = " + json.dumps(data, ensure_ascii=False) + ";\n"
    MIRROR_JS.write_text(js, encoding="utf-8")
    if COCKPIT_JS.parent.exists():
        COCKPIT_JS.write_text(js, encoding="utf-8")
    return HOT


def set_agent(agent: str, status: str, *, on_air: bool | None = None) -> dict:
    agent = agent.upper().strip()
    status = status.upper().strip()
    data = _safe_load()
    agents = data.setdefault("agents", {})
    agents[agent] = {"status": status, "ts": utc_now()}
    if on_air is True or status in ("ON_AIR", "SPEAKING"):
        data["on_air"] = agent
    elif on_air is False and data.get("on_air") == agent:
        data["on_air"] = None
    elif status in ("IDLE", "STOPPED", "OFF") and data.get("on_air") == agent:
        data["on_air"] = None
    _safe_write(data)
    return data


def clear_agent(agent: str) -> dict:
    agent = agent.upper().strip()
    data = _safe_load()
    data.get("agents", {}).pop(agent, None)
    if data.get("on_air") == agent:
        data["on_air"] = None
    _safe_write(data)
    return data


def _pgrep(pattern: str) -> bool:
    try:
        r = subprocess.run(
            ["pgrep", "-f", pattern],
            capture_output=True,
            text=True,
            check=False,
        )
        return bool(r.stdout.strip())
    except Exception:
        return False


def heartbeat(stamp_cursor: bool = True) -> dict:
    """Scan process ACE/Hulk + marque CURSOR ON_AIR (session board)."""
    ace_on = _pgrep("launch_vide_froid_4h_binance_NUAGE|GO_USINE_NUAGE|ace777_launch_v85")
    # Hulk paper
    hulk_on = _pgrep("paper_diprip|digest_watch.py")

    if ace_on:
        set_agent("ACE", "RUNNING")
    else:
        set_agent("ACE", "STOPPED")

    if hulk_on:
        set_agent("HULK", "RUNNING")
    else:
        set_agent("HULK", "STOPPED")

    if stamp_cursor:
        set_agent("CURSOR", "ON_AIR", on_air=True)

    return _safe_load()


def main() -> int:
    ap = argparse.ArgumentParser(description="AGENT ON AIR status")
    ap.add_argument("cmd", nargs="?", default="show", help="show|set|clear|heartbeat")
    ap.add_argument("agent", nargs="?", default="CURSOR")
    ap.add_argument("status", nargs="?", default="ON_AIR")
    ap.add_argument("--no-cursor", action="store_true", help="heartbeat sans stamp CURSOR")
    args = ap.parse_args()
    cmd = args.cmd.lower()

    if cmd == "set":
        data = set_agent(args.agent, args.status)
    elif cmd == "clear":
        data = clear_agent(args.agent)
    elif cmd == "heartbeat":
        data = heartbeat(stamp_cursor=not args.no_cursor)
    else:
        data = _safe_load()
        if not HOT.exists():
            data = heartbeat(stamp_cursor=True)

    print(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"HOT={HOT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
