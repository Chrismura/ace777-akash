#!/usr/bin/env python3
import csv
import tempfile
import unittest
from pathlib import Path

from generate_observation_fixture import generate
from run_observation_shadow import run


class ObservationShadowTests(unittest.TestCase):
    def test_fixture_is_explicitly_synthetic(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "fixture.jsonl"
            generate(source, run_id="synthetic-1", rows=3)
            content = source.read_text(encoding="utf-8")
            self.assertIn("SYNTHETIC_FIXTURE", content)
            self.assertNotIn("https://", content)

    def test_replays_local_snapshots(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "snapshots.jsonl"
            output = root / "out" / "observations.csv"
            source.write_text(
                '{"ts":"2026-09-01T00:00:00Z","unit":"BETA","cycle":1,"decision":"SKIP"}\n'
                '{"ts":"2026-09-01T00:00:01Z","unit":"BETA","cycle":2,"decision":"ALLOW","side":"SELL"}\n',
                encoding="utf-8",
            )
            self.assertEqual(run(source, output, run_id="shadow-1"), 0)
            with output.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 2)
            self.assertTrue(all(row["run_id"] == "shadow-1" for row in rows))

    def test_rejects_order_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "bad.jsonl"
            output = root / "out.csv"
            source.write_text('{"decision":"ALLOW","order":"MARKET"}\n', encoding="utf-8")
            self.assertEqual(run(source, output, run_id="shadow-2"), 2)
            self.assertFalse(output.exists())

    def test_rejects_network_urls(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "bad.jsonl"
            output = root / "out.csv"
            source.write_text('{"feed":"https://example.invalid"}\n', encoding="utf-8")
            self.assertEqual(run(source, output, run_id="shadow-3"), 2)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
