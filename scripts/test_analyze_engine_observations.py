#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from analyze_engine_observations import summarize


class EngineObservationQualityTests(unittest.TestCase):
    def test_counts_available_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "engine.csv"
            fields = ["ts", "run_id", "unit", "cycle", "symbol", "bid", "ask", "mid", "spread_bps", "momentum_bps", "regime", "decision", "side", "confidence", "reason"]
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"run_id": "r", "unit": "BETA", "decision": "SKIP", "spread_bps": "3.2", "reason": "x;tension=0.4"})
                writer.writerow({"run_id": "r", "unit": "BETA", "decision": "ALLOW", "confidence": "0.8", "reason": "y"})
            result = summarize(path)
            self.assertEqual(result["rows"], 2)
            self.assertEqual(result["decisions"]["SKIP"], 1)
            self.assertEqual(result["fields"]["spread_bps"], 1)
            self.assertEqual(result["fields"]["confidence"], 1)
            self.assertEqual(result["tensions"], [0.4])


if __name__ == "__main__":
    unittest.main()
