#!/usr/bin/env python3
import csv
import os
import tempfile
import unittest
from pathlib import Path

from observation_recorder import OBSERVATION_FIELDS, ObservationRecorder, record_observation


class ObservationRecorderTests(unittest.TestCase):
    def test_disabled_by_default_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "observations.csv"
            self.assertFalse(record_observation(path, {"run_id": "x"}))
            self.assertFalse(path.exists())

    def test_enabled_writes_header_and_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "observations.csv"
            recorder = ObservationRecorder(path, enabled=True)
            self.assertTrue(recorder.record({"run_id": "run-1", "decision": "SKIP", "cycle": 2}))
            self.assertTrue(recorder.record({"run_id": "run-1", "decision": "ALLOW", "cycle": 3}))

            with path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.reader(handle))
            self.assertEqual(rows[0], list(OBSERVATION_FIELDS))
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[1][1], "run-1")
            self.assertEqual(rows[1][10], "")
            self.assertEqual(rows[1][11], "SKIP")
            self.assertEqual(rows[1][12], "")
            self.assertEqual(rows[1][13], "")
            self.assertEqual(rows[2][11], "ALLOW")

    def test_environment_flag_enables_recording(self):
        previous = os.environ.get("ACE_OBSERVATION_RECORDING")
        os.environ["ACE_OBSERVATION_RECORDING"] = "TRUE"
        try:
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "observations.csv"
                recorder = ObservationRecorder(path)
                self.assertTrue(recorder.record({"run_id": "env-run"}))
                self.assertTrue(path.exists())
        finally:
            if previous is None:
                os.environ.pop("ACE_OBSERVATION_RECORDING", None)
            else:
                os.environ["ACE_OBSERVATION_RECORDING"] = previous


if __name__ == "__main__":
    unittest.main()
