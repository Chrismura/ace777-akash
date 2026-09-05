#!/usr/bin/env python3
"""Hermetic tests for the read-only ACE Duo audit helper."""
from __future__ import annotations

import csv
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import audit_ace_duo_readonly as audit


def write_csv(path: Path, rows):
    fields = ["ts", "cycle", "side", "status", "entryPrice", "exitPrice", "qty", "bps", "pnl", "feeUsdt", "pnlNet"]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "x.csv"
        write_csv(p, [
            {"ts": "2026-09-01T10:00:00Z", "cycle": "1", "side": "BUY", "status": "FILLED", "entryPrice": "1", "exitPrice": "2", "qty": "1", "bps": "1", "pnl": "1.5", "feeUsdt": "0.1", "pnlNet": "1.4"},
            {"ts": "2026-08-31T23:00:00Z", "cycle": "0", "side": "SKIP", "status": "SKIPPED", "entryPrice": "", "exitPrice": "", "qty": "", "bps": "", "pnl": "0"},
        ])
        result = audit.inspect(p, datetime(2026, 9, 1, tzinfo=timezone.utc))
        assert result["schemaOk"]
        assert result["rows"] == 2
        assert result["fills"] == 1
        assert result["rowsBeforeSession"] == 1
        assert result["pnlGross"] == 1.5
        assert result["fees"] == 0.1
        assert result["pnlNet"] == 1.4
        assert result["netFieldsOk"]
        assert result["netRows"] == 1
        assert result["netConsistent"]
    print("ACE_DUO_READONLY_TESTS_OK")


if __name__ == "__main__":
    main()
