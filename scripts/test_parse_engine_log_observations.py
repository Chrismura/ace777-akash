#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from parse_engine_log_observations import parse, parse_line


class EngineLogParserTests(unittest.TestCase):
    def test_parses_skip_telemetry(self):
        row = parse_line("[BETA_X5] 16:02:36 x5 #4 SKIP | radar_block conf=0.5 raw_mom_bps=1.2 spread_bps=4.5 tension=0.8", run_id="r", source="x.log")
        self.assertEqual(row["unit"], "BETA")
        self.assertEqual(row["decision"], "SKIP")
        self.assertEqual(row["spread_bps"], 4.5)
        self.assertEqual(row["momentum_bps"], 1.2)
        self.assertEqual(row["reason"], "engine_log:x.log;tension=0.8")

    def test_ignores_unrelated_line(self):
        self.assertIsNone(parse_line("Mission terminée", run_id="r", source="x.log"))

    def test_writes_only_matching_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "engine.log"
            output = root / "observations.csv"
            source.write_text("noise\n[BETA_X5] 16:02:36 x5 #4 SKIP | gate conf=0.5 spread_bps=4.5\n", encoding="utf-8")
            self.assertEqual(parse(source, output, run_id="r"), 1)
            with output.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["run_id"], "r")
            self.assertIn("tension=", rows[0]["reason"])


if __name__ == "__main__":
    unittest.main()
