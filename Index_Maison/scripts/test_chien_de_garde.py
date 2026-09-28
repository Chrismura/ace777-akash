#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harnais de test (selftest shadow) pour chien_de_garde.py (9 cas minimum).
"""

import sys
import unittest
import tempfile
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

# Import du module à tester (en ajustant le sys.path si besoin)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import chien_de_garde

class TestChienDeGarde(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.base_path = Path(self.test_dir.name)
        
        # Redirection des chemins globaux du chien pour le test
        chien_de_garde.BASE_DIR = self.base_path
        chien_de_garde.INDEX_MAISON = self.base_path / "Index_Maison"
        chien_de_garde.REGISTRE_PATH = chien_de_garde.INDEX_MAISON / "strategie" / "REGISTRE_ORGANES.json"
        chien_de_garde.POULS_DIR = chien_de_garde.INDEX_MAISON / "pouls"
        chien_de_garde.ETAT_CHIEN = chien_de_garde.POULS_DIR / ".chien_etat.json"
        chien_de_garde.RAPPORT_JSON = chien_de_garde.INDEX_MAISON / "thermo" / "CHIEN_RAPPORT.json"
        chien_de_garde.RAPPORT_MD = chien_de_garde.INDEX_MAISON / "thermo" / "CHIEN_RAPPORT.md"
        chien_de_garde.MEMOIRE_COLLAB = chien_de_garde.INDEX_MAISON / "MEMOIRE_COLLAB.md"
        chien_de_garde.ALERTES_LOG = chien_de_garde.INDEX_MAISON / "thermo" / "CHIEN_ALERTES.md"
        chien_de_garde.STOP_FILE = chien_de_garde.INDEX_MAISON / "strategie" / "STOP"
        chien_de_garde.STOP_ALL_FILE = chien_de_garde.INDEX_MAISON / "strategie" / "STOP_ALL"
        chien_de_garde.MAINT_FILE = chien_de_garde.INDEX_MAISON / "strategie" / "MAINTENANCE_PREVUE"

        chien_de_garde.POULS_DIR.mkdir(parents=True, exist_ok=True)
        (chien_de_garde.INDEX_MAISON / "strategie").mkdir(parents=True, exist_ok=True)
        (chien_de_garde.INDEX_MAISON / "thermo").mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_1_organe_vivant(self):
        """Cas 1 : Organe vivant (pouls récent)"""
        reg = {
            "organes": [{
                "organe": "test_org", "mode": "pouls_direct", "frequence_attendue_sec": 60, "tolerance_mult": 2.0, "criticite": "CRITIQUE"
            }]
        }
        chien_de_garde.ecriture_atomique(chien_de_garde.REGISTRE_PATH, json.dumps(reg))
        
        pouls_data = {"dernier_battement": datetime.now(timezone.utc).isoformat()}
        chien_de_garde.ecriture_atomique(chien_de_garde.POULS_DIR / "test_org.json", json.dumps(pouls_data))
        
        age = chien_de_garde.evaluer_age_organe(reg["organes"][0])
        self.assertLess(age, 10.0)

    def test_2_organe_mort(self):
        """Cas 2 : Organe mort (pouls ancien)"""
        reg = {
            "organes": [{
                "organe": "mort_org", "mode": "pouls_direct", "frequence_attendue_sec": 60, "tolerance_mult": 2.0, "criticite": "CRITIQUE"
            }]
        }
        ancien_temps = (datetime.now(timezone.utc) - timedelta(seconds=500)).isoformat()
        pouls_data = {"dernier_battement": ancien_temps}
        chien_de_garde.ecriture_atomique(chien_de_garde.POULS_DIR / "mort_org.json", json.dumps(pouls_data))
        
        age = chien_de_garde.evaluer_age_organe(reg["organes"][0])
        self.assertGreater(age, 200.0)

    def test_3_pouls_manquant_fail_open(self):
        """Cas 3 : Pouls manquant (fail-open sur données, détecté vieux)"""
        reg = {
            "organes": [{
                "organe": "inexistant", "mode": "pouls_direct", "frequence_attendue_sec": 60, "tolerance_mult": 2.0, "criticite": "CRITIQUE"
            }]
        }
        age = chien_de_garde.evaluer_age_organe(reg["organes"][0])
        self.assertEqual(age, float('inf'))

    def test_4_registre_corrompu_fail_fast(self):
        """Cas 4 : Registre corrompu (fail-fast, sortie system exit 1)"""
        chien_de_garde.ecriture_atomique(chien_de_garde.REGISTRE_PATH, "{ json malforme")
        with self.assertRaises(SystemExit) as cm:
            chien_de_garde.main()
        self.assertEqual(cm.exception.code, 1)

    def test_5_kill_switch(self):
        """Cas 5 : Kill-switch actif (le chien se tait proprement)"""
        chien_de_garde.STOP_FILE.touch()
        # Ne doit pas lever d'erreur ni crasher
        try:
            chien_de_garde.main()
        except SystemExit as e:
            self.assertEqual(e.code, 0)

    def test_6_anti_tempete(self):
        """Cas 6 : Anti-tempête (2e cri dans l'heure bloqué)"""
        chien_de_garde.crier("org_test", "Erreur 1")
        etat_avant = chien_de_garde.charger_json_securise(chien_de_garde.ETAT_CHIEN)
        ts_1 = etat_avant.get("org_test")
        
        # Second cri immédiat
        chien_de_garde.crier("org_test", "Erreur 2")
        etat_apres = chien_de_garde.charger_json_securise(chien_de_garde.ETAT_CHIEN)
        ts_2 = etat_apres.get("org_test")
        
        self.assertEqual(ts_1, ts_2) # Le timestamp n'a pas été écrasé (bloqué)

    def test_7_organe_zone_grise(self):
        """Cas 7 : Organe zone grise (surveillé sans crier)"""
        reg = {
            "organes": [{
                "organe": "grise_org", "mode": "pouls_direct", "frequence_attendue_sec": 10, "tolerance_mult": 2.0, "criticite": "CRITIQUE", "zone_grise": True
            }]
        }
        chien_de_garde.ecriture_atomique(chien_de_garde.REGISTRE_PATH, json.dumps(reg))
        # Même sans pouls, comme zone_grise=True, il ne déclenche pas de crier dans main()
        try:
            chien_de_garde.main()
        except Exception:
            self.fail("La zone grise a déclenché une exception inattendue.")

    def test_8_maintenance_prevue(self):
        """Cas 8 : Chien muet si MAINTENANCE_PREVUE"""
        chien_de_garde.MAINT_FILE.touch()
        try:
            chien_de_garde.main()
        except SystemExit as e:
            self.assertEqual(e.code, 0)

    def test_9_idempotence_relance(self):
        """Cas 9 : Idempotence (relançable sans doublons ni crash)"""
        reg = {
            "organes": [{
                "organe": "idempotent_org", "mode": "pouls_direct", "frequence_attendue_sec": 60, "tolerance_mult": 2.0, "criticite": "MINEUR"
            }]
        }
        chien_de_garde.ecriture_atomique(chien_de_garde.REGISTRE_PATH, json.dumps(reg))
        chien_de_garde.main()
        # Seconde relance immédiate
        try:
            chien_de_garde.main()
        except Exception as e:
            self.fail(f"L'idempotence a échoué avec l'erreur : {e}")

if __name__ == "__main__":
    unittest.main()
