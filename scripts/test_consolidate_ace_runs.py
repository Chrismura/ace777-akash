#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from consolidate_ace_runs import write_report


class ConsolidationTests(unittest.TestCase):
    def test_report_contains_local_facts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fields = ["ts", "cycle", "side", "status", "entryPrice", "exitPrice", "qty", "bps", "pnl", "feeUsdt", "pnlNet", "exitReason", "holdSec", "msg"]
            trades = root / "R_ALPHA_X13_BURST13.csv"
            with trades.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"status": "FILLED", "pnl": "1", "feeUsdt": "0.2", "pnlNet": "0.8", "exitReason": "stop_loss"})
            obs = root / "R_ALPHA_X13_BURST13_OBSERVATIONS.csv"
            obs_fields = ["ts", "run_id", "unit", "cycle", "symbol", "bid", "ask", "mid", "spread_bps", "momentum_bps", "regime", "decision", "side", "confidence", "reason"]
            with obs.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=obs_fields)
                writer.writeheader()
                writer.writerow({"run_id": "R", "unit": "ALPHA", "decision": "ALLOW", "reason": "tension=1"})
            output = root / "report.md"
            write_report(root, output, ["R"])
            text = output.read_text(encoding="utf-8")
            self.assertIn("+0.8000", text)
            self.assertIn("stop_loss=1", text)
            self.assertIn("no Binance reconciliation", text)


if __name__ == "__main__":
    unittest.main()
