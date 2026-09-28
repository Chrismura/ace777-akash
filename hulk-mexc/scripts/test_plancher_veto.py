#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harnais de test du veto Plancher (décision pure plancher_veto_decision)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paper_diprip as p  # noqa: E402


class TestPlancherVeto(unittest.TestCase):

    def test_1_hors_couverture(self):
        """Paire non couverte (aucune donnée) -> pas de veto."""
        self.assertEqual(p.plancher_veto_decision(None), (False, "hors_couverture"))

    def test_2_couteau_non_confirme(self):
        """Chute >=25% + OBSERVATION (C1/C2/C3 non réunis) -> VETO."""
        d = {"phase": "OBSERVATION", "chute_seuil": True, "drop_depuis_pic_pct": 41.0,
             "C1_murs_stables": False, "C2_spread_ok": True, "C3_rebond_ok": False}
        veto, why = p.plancher_veto_decision(d)
        self.assertTrue(veto)
        self.assertIn("couteau non confirme", why)

    def test_3_confirme_libre(self):
        """Chute >=25% mais CONFIRME -> entrée libre (le Plancher approuve)."""
        d = {"phase": "CONFIRME", "chute_seuil": True, "drop_depuis_pic_pct": 30.0}
        self.assertEqual(p.plancher_veto_decision(d), (False, "CONFIRME"))

    def test_4_achete_libre(self):
        """Phase ACHETE -> libre."""
        d = {"phase": "ACHETE", "chute_seuil": True, "drop_depuis_pic_pct": 28.0}
        self.assertEqual(p.plancher_veto_decision(d), (False, "ACHETE"))

    def test_5_pas_de_chute_libre(self):
        """Pas en chute (drop < seuil) -> pas de veto, même en OBSERVATION."""
        d = {"phase": "OBSERVATION", "chute_seuil": False, "drop_depuis_pic_pct": 4.4}
        self.assertEqual(p.plancher_veto_decision(d), (False, "OBSERVATION"))

    def test_6_chute_seuil_absent_est_fail_open(self):
        """chute_seuil absent -> pas de veto (fail-open)."""
        d = {"phase": "OBSERVATION"}
        self.assertEqual(p.plancher_veto_decision(d), (False, "OBSERVATION"))


if __name__ == "__main__":
    unittest.main()
