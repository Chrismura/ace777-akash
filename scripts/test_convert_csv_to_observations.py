#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from convert_csv_to_observations import convert


class ConvertCsvTests(unittest.TestCase):
    def test_conversion_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "V4_BETA_X5.csv"
            destination = root / "observations.csv"
            source.write_text("ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,feeUsdt,pnlNet,exitReason,holdSec,msg\n2026-09-01T00:00:00Z,1,SKIP,SKIPPED,,,,,0,regime_gate,,reason=x\n", encoding="utf-8")
            self.assertEqual(convert(source, destination, run_id="one"), 1)
            first = destination.read_text(encoding="utf-8")
            self.assertEqual(convert(source, destination, run_id="one"), 1)
            self.assertEqual(destination.read_text(encoding="utf-8"), first)

    def test_projects_skips_and_fills(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "V4_BETA_X5.csv"
            destination = root / "observations.csv"
            source.write_text(
                "ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,feeUsdt,pnlNet,exitReason,holdSec,msg\n"
                "2026-09-01T00:00:00Z,1,SKIP,SKIPPED,,,,,0,regime_gate,,reason=COMPRESSE tension=0.01\n"
                "2026-09-01T00:00:10Z,2,SELL,FILLED,70000,70010,0.01,-1.4,-0.1,0.05,-0.15,stop_loss,10,radar=short conf=0.8 spread_bps=2.5 raw_mom_bps=-4\n",
                encoding="utf-8",
            )
            self.assertEqual(convert(source, destination, run_id="csv-run"), 2)
            with destination.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(rows[0]["decision"], "SKIP")
            self.assertTrue(rows[0]["reason"].startswith("csv_engine:"))
            self.assertEqual(rows[1]["decision"], "ALLOW")
            self.assertEqual(rows[1]["side"], "SELL")
            self.assertEqual(rows[1]["spread_bps"], "2.5")
            self.assertEqual(rows[1]["ask"], "")
            self.assertEqual(rows[1]["run_id"], "csv-run")
            self.assertEqual(rows[1]["unit"], "BETA")


if __name__ == "__main__":
    unittest.main()
