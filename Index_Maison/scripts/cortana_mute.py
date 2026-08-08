#!/usr/bin/env python3
"""Cortana mute — coupe toute synthèse (edge/say) sans tuer les feeds.

Usage:
  python3 cortana_mute.py on|off|status|toggle
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

MUTE = Path("/tmp/ace777_swarm_pids/.cortana_mute")
MIRROR = Path("/Users/christophe/ace777-test-day1/Index_Maison/thermo/cortana_mute.json")


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def is_muted() -> bool:
    return MUTE.exists()


def set_mute(on: bool) -> None:
    MUTE.parent.mkdir(parents=True, exist_ok=True)
    if on:
        MUTE.write_text(f"muted_at={utc()}\n", encoding="utf-8")
    else:
        MUTE.unlink(missing_ok=True)
    payload = {"muted": on, "ts": utc()}
    MIRROR.parent.mkdir(parents=True, exist_ok=True)
    MIRROR.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    # cockpit mirror
    cock = Path("/Users/christophe/ace777-test-day1/Index_Maison/cockpit/cortana_mute.json")
    if cock.parent.exists():
        cock.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    cmd = (sys.argv[1] if len(sys.argv) > 1 else "status").lower()
    if cmd in ("on", "mute", "1", "true"):
        set_mute(True)
        print("CORTANA_MUTE=ON — silence (vidéo OK)")
    elif cmd in ("off", "unmute", "0", "false"):
        set_mute(False)
        print("CORTANA_MUTE=OFF — voix réactivée")
    elif cmd == "toggle":
        set_mute(not is_muted())
        print("CORTANA_MUTE=" + ("ON" if is_muted() else "OFF"))
    else:
        print("CORTANA_MUTE=" + ("ON" if is_muted() else "OFF"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
