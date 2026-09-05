#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from compare_observation_runs import report


class CompareObservationTests(unittest.TestCase):
    def test_report_counts_and_keeps_run_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "run_ALPHA_OBSERVATIONS.csv"
            output = root / "comparison.md"
            fields = ["ts", "run_id", "unit", "cycle", "symbol", "bid", "ask", "mid", "spread_bps", "momentum_bps", "regime", "decision", "side", "confidence", "reason"]
            with source.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"run_id": "r1", "unit": "ALPHA", "decision": "SKIP", "reason": "csv_engine:gate"})
                writer.writerow({"run_id": "r1", "unit": "ALPHA", "decision": "ALLOW", "mid": "70000", "reason": "csv_engine:filled"})
            report([source], output)
            text = output.read_text(encoding="utf-8")
            self.assertIn("| 1 | 1 | 1 |", text)
            self.assertIn("r1", text)
            self.assertIn("Missing bid/ask", text)


if __name__ == "__main__":
    unittest.main()
