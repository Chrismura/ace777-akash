#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from replay_radar_alignment import load_beta, replay_beta


class RadarReplayTests(unittest.TestCase):
    def test_flips_misaligned_pnl(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "BETA_X5.csv"
            fields = ["ts", "cycle", "side", "status", "entryPrice", "exitPrice", "qty", "bps", "pnl", "feeUsdt", "pnlNet", "exitReason", "holdSec", "msg"]
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                # Aligned: SELL + radar=short → PnL stays
                writer.writerow({"status": "FILLED", "entryPrice": "100", "exitPrice": "101", "side": "SELL", "qty": "0.01", "pnl": "-1", "feeUsdt": "0.2", "pnlNet": "-1.2", "exitReason": "stop_loss", "msg": "radar=short conf=0.9 tension=2.0"})
                # Misaligned: SELL + radar=long → PnL flips
                writer.writerow({"status": "FILLED", "entryPrice": "100", "exitPrice": "99", "side": "SELL", "qty": "0.01", "pnl": "1", "feeUsdt": "0.2", "pnlNet": "0.8", "exitReason": "trailing_stop", "msg": "radar=long conf=0.8 tension=1.0"})
            trades = load_beta(path)
            result = replay_beta(trades)
            self.assertEqual(len(result["aligned"]), 1)
            self.assertEqual(len(result["misaligned"]), 1)
            self.assertEqual(result["misaligned"][0]["pnl_flipped"], -1)
            self.assertEqual(result["misaligned"][0]["net_flipped"], -1.2)


if __name__ == "__main__":
    unittest.main()
