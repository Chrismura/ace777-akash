#!/usr/bin/env python3
"""Test the radar-aligned launcher patch logic without executing anything."""

import os
import re
import tempfile
import unittest
from pathlib import Path


SAMPLE_LAUNCHER = r"""#!/usr/bin/env bash
set -euo pipefail

launch_beta() {
  (
    export LOG_FILE="beta.csv"
    export FORCE_ENTRY_SIDE="SELL"
    export LEVERAGE="5"
    run_unit "BETA_X5"
  ) &
  PID_BETA=$!
}

launch_alpha() {
  (
    export LOG_FILE="alpha.csv"
    export FORCE_ENTRY_SIDE="BUY"
    export LEVERAGE="13"
    run_unit "ALPHA_X13_BURST13"
  ) &
  PID_ALPHA=$!
}
"""


def patch_launcher(source: Path, dest: Path) -> str:
    """Apply the same patch as launch_radar_aligned.sh."""
    content = source.read_text(encoding="utf-8")
    beta_start = content.find("launch_beta()")
    beta_end = content.find(") &", beta_start)
    beta_block = content[beta_start:beta_end]
    new_block = re.sub(r'\s*export FORCE_ENTRY_SIDE="SELL"\n', '\n', beta_block)
    content = content[:beta_start] + new_block + content[beta_end:]
    dest.write_text(content, encoding="utf-8")
    return content


class RadarAlignedPatchTests(unittest.TestCase):
    def test_removes_sell_from_beta(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "original.sh"
            dst = Path(d) / "patched.sh"
            src.write_text(SAMPLE_LAUNCHER, encoding="utf-8")
            result = patch_launcher(src, dst)
            # FORCE_ENTRY_SIDE="SELL" should be gone
            self.assertNotIn('FORCE_ENTRY_SIDE="SELL"', result)
            # FORCE_ENTRY_SIDE="BUY" should remain (alpha)
            self.assertIn('FORCE_ENTRY_SIDE="BUY"', result)

    def test_original_not_modified(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "original.sh"
            dst = Path(d) / "patched.sh"
            src.write_text(SAMPLE_LAUNCHER, encoding="utf-8")
            patch_launcher(src, dst)
            self.assertEqual(src.read_text(encoding="utf-8"), SAMPLE_LAUNCHER)


if __name__ == "__main__":
    unittest.main()
