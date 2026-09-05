#!/usr/bin/env python3
"""Patch the ACE launcher to remove FORCE_ENTRY_SIDE=SELL from launch_beta.

Usage: python3 scripts/patch_launcher_radar.py <source> <dest>
"""

import re
import sys


def patch(source: str, dest: str) -> None:
    with open(source) as f:
        content = f.read()

    # Remove FORCE_ENTRY_SIDE=SELL from launch_beta only
    beta_start = content.find("launch_beta()")
    if beta_start != -1:
        beta_end = content.find(") &", beta_start)
        if beta_end != -1:
            block = content[beta_start:beta_end]
            new_block = re.sub(r'[ \t]*export FORCE_ENTRY_SIDE="SELL"\n', '', block)
            content = content[:beta_start] + new_block + content[beta_end:]

    # NOTE: keep the original `cd` block untouched. The copied launcher runs from
    # /tmp, and its own `cd` resolves relative paths (./scripts/...) to the
    # user's original working directory, which is the project root.

    with open(dest, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <source> <dest>", file=sys.stderr)
        sys.exit(1)
    patch(sys.argv[1], sys.argv[2])
    print("PATCH_OK")
