#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests hermétiques du chantier anti-fléau timeout hub (13/08).
C1 : erreurs DNS/connexion = ReseauIndisponible, pas de blacklist.
C2 : budget temps global par requête (REQUEST_MAX_SECONDS).
C3 : détection réseau pas prêt (mode dégradé)."""
import os
import sys
import time
import socket
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hub_prise_ia as hub


class TestAntifleau(unittest.TestCase):

    def test_1_raw_call_dns_inexistant_leve_reseau(self):
        """C1 : un hôte DNS inexistant doit lever ReseauIndisponible rapidement."""
        prov = {"base_url": "http://aucun-nom-xyz.invalid", "model": "test"}
        t0 = time.time()
        with self.assertRaises(hub.ReseauIndisponible):
            hub._raw_call(prov, [{"role": "user", "content": "hi"}], 0.7, 10, 5)
        self.assertLess(time.time() - t0, 10, "doit échouer vite, pas de PATIENCE")

    def test_2_pas_de_blacklist_sur_erreur_reseau(self):
        """C1 : 3 échecs réseau NE doivent PAS blacklister le provider."""
        prov = {"id": "test-reseau", "name": "Test Réseau",
                "base_url": "http://aucun-nom-xyz.invalid", "model": "test"}
        hub._fails.clear()
        hub._blacklist.clear()
        for _ in range(3):
            with self.assertRaises(hub.ReseauIndisponible):
                hub.call_provider(prov, [{"role": "user", "content": "hi"}], 0.7, 10)
        self.assertEqual(hub._fails.get(prov["id"], 0), 0,
                         "échec réseau ne doit pas compter comme échec provider")
        self.assertNotIn(prov["id"], hub._blacklist, "pas de backoff réseau")

    def test_3_reseau_disponible_detecte_dns(self):
        """C3 : le test DNS répond (True si DNS OK, False si KO, sans bloquer)."""
        t0 = time.time()
        hub._reseau_disponible()
        self.assertLess(time.time() - t0, 5, "test DNS non bloquant")

    def test_4_timeout_budget_borne(self):
        """C2 : timeout_budget borne le timeout effectif du provider."""
        prov = {"id": "test-budget", "name": "Test Budget", "timeout": 600,
                "base_url": "http://aucun-nom-xyz.invalid", "model": "test"}
        hub._fails.clear()
        hub._blacklist.clear()
        t0 = time.time()
        with self.assertRaises(hub.ReseauIndisponible):
            hub.call_provider(prov, [{"role": "user", "content": "hi"}], 0.7, 10,
                              timeout_budget=5)
        self.assertLess(time.time() - t0, 10, "budget 5s -> échec rapide, pas 600s")


if __name__ == "__main__":
    unittest.main(verbosity=2)
