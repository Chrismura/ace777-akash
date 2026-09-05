#!/usr/bin/env python3
"""Hermetic regression checks for clean-run diagnostic policy."""


def classify_alpha(alpha_fills: int, beta_fills: int) -> str:
    ratio = alpha_fills / beta_fills if beta_fills else (1.0 if alpha_fills else 0.0)
    if alpha_fills == 0:
        return "CRITIQUE — ALPHA n'a exécuté aucun trade"
    if alpha_fills < 3 and ratio < 0.5:
        return "ALERTE — ALPHA activité faible"
    return f"OK — ALPHA active ({alpha_fills} fills, ratio BETA={ratio:.0%})"


def main() -> None:
    assert classify_alpha(3, 4).startswith("OK — ALPHA active")
    assert classify_alpha(1, 10).startswith("ALERTE — ALPHA activité faible")
    assert classify_alpha(0, 4).startswith("CRITIQUE")
    print("ACE_DIAGNOSTICS_TESTS_OK")


if __name__ == "__main__":
    main()
