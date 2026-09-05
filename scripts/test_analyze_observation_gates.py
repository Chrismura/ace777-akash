#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from analyze_observation_gates import analyze


class GateAnalysisTests(unittest.TestCase):
    def test_counts_gates_and_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "x_ALPHA_OBSERVATIONS.csv"
            fields = ["ts", "run_id", "unit", "cycle", "symbol", "bid", "ask", "mid", "spread_bps", "momentum_bps", "regime", "decision", "side", "confidence", "reason"]
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"unit": "ALPHA", "decision": "SKIP", "reason": "csv_engine:regime_gate", "spread_bps": "2"})
                writer.writerow({"unit": "ALPHA", "decision": "ALLOW", "mid": "70000", "confidence": "0.8", "reason": "csv_engine:filled"})
            result = analyze([path])
            self.assertEqual(result["totals"]["SKIP"], 1)
            self.assertEqual(result["totals"]["ALLOW"], 1)
            self.assertEqual(result["files"][0]["populated"]["mid"], 1)
            self.assertEqual(result["files"][0]["populated"]["spread_bps"], 1)


if __name__ == "__main__":
    unittest.main()
