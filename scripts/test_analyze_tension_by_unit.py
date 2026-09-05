#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from analyze_tension_by_unit import analyze, percentile


class TensionAnalysisTests(unittest.TestCase):
    def test_percentile_and_groups(self):
        self.assertEqual(percentile([1.0, 2.0, 3.0], 0.5), 2.0)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "x.csv"
            fields = ["ts", "run_id", "unit", "cycle", "symbol", "bid", "ask", "mid", "spread_bps", "momentum_bps", "regime", "decision", "side", "confidence", "reason"]
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"run_id": "r", "unit": "ALPHA", "decision": "SKIP", "reason": "engine;tension=0.1"})
                writer.writerow({"run_id": "r", "unit": "ALPHA", "decision": "SKIP", "reason": "engine;tension=0.9"})
            result = analyze([path])
            self.assertEqual(result["groups"][("r", "ALPHA")], [0.1, 0.9])
            self.assertEqual(result["decisions"][(("r", "ALPHA"), "SKIP")], 2)


if __name__ == "__main__":
    unittest.main()
