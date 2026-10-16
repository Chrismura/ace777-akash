#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_seellfull_resume.py — Verrou 3 (compata --resume), lecture seule.

Ne lance AUCUNE boucle, ne touche à AUCUN state/CSV réel. Lit le dernier
PAPER_V1_*_state.json (lecture seule), l'injecte dans un bot de la COPIE test,
et appelle manage_open sur les positions ouvertes pour vérifier que la garde
SELL full ne crash pas sur des positions RESTAURÉES réelles (anciennes, sans
la clé guard_last → exactement le cas du --resume après déploiement).
"""
import importlib
import inspect
import json
import re
import shutil
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
HULK = SRC.parent
RUNS = HULK / "runs"
TMP = SRC / "_sci_test_module"
TMP.mkdir(exist_ok=True)
shutil.copy(SRC / "paper_diprip_SELLFULL_TEST.py", TMP / "paper_diprip_SELLFULL_TEST.py")
if str(TMP) not in sys.path:
    sys.path.insert(0, str(TMP))
PaperBot = importlib.import_module("paper_diprip_SELLFULL_TEST").PaperBot

# Sol du dernier état réel (lecture seule)
states = sorted(RUNS.glob("PAPER_V1_*_state.json"), reverse=True)
if not states:
    print("AUCUN état à tester"); sys.exit(0)
st = json.loads(states[0].read_text(encoding="utf-8"))
pos = st.get("positions") or {}

# Un bot factice, garde active (attributs par défaut)
bot = object.__new__(PaperBot)
bot.sell_full_amplitude_guard = 12.0
bot.sell_full_require_invalidation = 1
bot.sell_full_guard_degraded = 1
bot.dust_sweep_min_notional = 1.0
bot.pos = {k: dict(v) for k, v in pos.items()}
bot.scores = st.get("scores") or {}
bot.bags = st.get("bags") or {}
bot.bag_dca = st.get("bag_dca") or {}
bot.pair_cash = {}
bot.reentry_count = {}
bot.pnl_total = 0.0
bot.trades = 0
bot.double_mult = 2.0
# P1 (16/10/2026, GO P1-P4) : le chemin SELL-full lit self.stake_sell_frac (moteur
# l.2571, défaut cfg STAKE_SELL_FRAC=0.50, moteur l.748). Le harnais factice ne le
# posait pas → AttributeError sur RWAINC (même famille que gb_couple_on, 13/10).
bot.stake_sell_frac = 0.50
bot.bag_no_tech_stop = False
bot.inv = {}
bot.lot_cache = {}
bot.rip_early_pairs = {}
bot.rip_early_p1 = 2.0; bot.rip_early_p2 = 6.0
bot.rip_late_p1 = 6.0; bot.rip_late_p2 = 8.0
bot.rip_scaleout_frac = 0.25
bot.stop_cooldown_h = 24
bot.log = lambda *a, **k: None
bot.sell_trade = lambda *a, **k: 0.0          # stub : on ne vend VRAIMENT rien
bot.add_pair_cash = lambda *a, **k: None
bot.lot_filter = lambda p: (None, None)        # step inconnu → pas de filtre
bot.is_bag = lambda p: p in bot.bags
bot.arm_reentry = lambda *a, **k: None

probe_price = {k: (float(v.get("entry") or 1.0) * 0.90) for k, v in pos.items()}
crashes = 0
checked = 0
for pair in list(pos.keys()):
    price = probe_price[pair]
    try:
        bot.manage_open(pair, price)
        checked += 1
    except AttributeError as e:
        # GARDE ANTI-DÉRIVE harnais/moteur (P1, GO 16/10) : le harnais est construit
        # à la main (object.__new__) ; quand le moteur gagne un attribut lu par
        # manage_open, le harnais pourrit. On ÉCHOUE FORT (pas d'auto-remplissage :
        # il masquerait un vrai bug du chemin --resume en production), mais le message
        # dit EXACTEMENT quoi ajouter — la dérive devient une consigne, pas une énigme.
        crashes += 1
        _m = re.search(r"'(\w+)'", str(e))
        _attr = _m.group(1) if _m else "?"
        _dans_moteur = False
        try:
            _dans_moteur = f"self.{_attr} =" in inspect.getsource(PaperBot.__init__)
        except Exception:
            pass
        if _dans_moteur:
            print(f"[DÉRIVE-HARNAIS] {pair}: ajouter « bot.{_attr} = <défaut moteur> » "
                  f"(self.{_attr} existe dans PaperBot.__init__ mais pas dans le harnais)")
        else:
            print(f"[FAIL] {pair}: AttributeError: {e} (attribut inconnu du moteur — "
                  f"vrai bug du chemin resume ?)")
    except Exception as e:
        crashes += 1
        print(f"[FAIL] {pair}: {type(e).__name__}: {e}")

print(f"\n=== Resume: {len(pos)} positions réelles testées, {checked} OK, {crashes} crash ===")
sys.exit(1 if crashes else 0)