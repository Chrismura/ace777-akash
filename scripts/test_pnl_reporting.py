#!/usr/bin/env python3
import csv
import tempfile
from pathlib import Path


def summarize(path: Path):
    rows = list(csv.DictReader(path.open(newline="")))
    fills = [r for r in rows if r.get("status") == "FILLED"]
    gross = sum(float(r.get("pnl") or 0) for r in fills)
    net = sum(float(r.get("pnlNet") or r.get("pnl") or 0) for r in fills)
    fees = gross - net
    return gross, fees, net


def main():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "run.csv"
        fields = ["ts", "status", "pnl", "feeUsdt", "pnlNet"]
        with path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows([
                {"ts": "1", "status": "FILLED", "pnl": "1.0", "feeUsdt": "0.2", "pnlNet": "0.8"},
                {"ts": "2", "status": "FILLED", "pnl": "-2.0", "feeUsdt": "0.3", "pnlNet": "-2.3"},
                {"ts": "3", "status": "SKIPPED", "pnl": "0", "feeUsdt": "", "pnlNet": ""},
            ])
        gross, fees, net = summarize(path)
        assert round(gross, 6) == -1.0
        assert round(fees, 6) == 0.5
        assert round(net, 6) == -1.5
        assert round(gross - fees, 6) == round(net, 6)
    print("ACE_PNL_REPORTING_TESTS_OK")


if __name__ == "__main__":
    main()
