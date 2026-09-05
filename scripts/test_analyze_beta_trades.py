#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from analyze_beta_trades import analyze


class BetaAnalysisTests(unittest.TestCase):
    def test_groups_exit_reasons(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "BETA_X5.csv"
            fields = ["ts", "cycle", "side", "status", "entryPrice", "exitPrice", "qty", "bps", "pnl", "feeUsdt", "pnlNet", "exitReason", "holdSec", "msg"]
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow({"status": "FILLED", "pnl": "-1", "feeUsdt": "0.2", "pnlNet": "-1.2", "exitReason": "stop_loss"})
                writer.writerow({"status": "FILLED", "pnl": "0.5", "feeUsdt": "0.2", "pnlNet": "0.3", "exitReason": "trailing_stop"})
            result = analyze([path])
            self.assertEqual(result["by_exit"]["stop_loss"]["net"], -1.2)
            self.assertEqual(result["by_exit"]["trailing_stop"]["count"], 1)


if __name__ == "__main__":
    unittest.main()
