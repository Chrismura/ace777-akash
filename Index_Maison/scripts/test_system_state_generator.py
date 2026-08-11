#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests unitaires — system_state_generator.py v2.1 (SPEC V2.1, E1).

Couvre les exigences validées par la famille (loi 1quinquies) :
- P1-1 : status HEALTHY/STALE/DEGRADED selon la fraîcheur
- P1-2 : feed_hash SHA-256 (ordre fixe, stable)
- P1-3 : verify_hash détecte un state corrompu
- P1-4 : un feed corrompu/absent ne bloque jamais la génération
- Loi du brut : state.json ne contient AUCUNE prose (aucune clé texte longue)

Usage : python3 test_system_state_generator.py
"""
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import system_state_generator as g


def test_status_healthy():
    # feeds frais : status HEALTHY
    g.FEEDS = [
        ("mission", os.path.join(tempfile.mkdtemp(), "mission.json")),
    ]
    g.FRESH_SECONDS = {"mission": 120}
    path = g.FEEDS[0][1]
    with open(path, "w") as f:
        json.dump({"ts": "x"}, f)
    feeds = {n: g.load_json_safe(p) for n, p in g.FEEDS}
    assert g.compute_status(feeds) == "HEALTHY", g.compute_status(feeds)
    print("  [OK] status HEALTHY quand feed frais")


def test_status_degraded_feed_absent():
    # feed absent -> DEGRADED
    g.FEEDS = [("mission", "/tmp/feed_absent_xyz.json")]
    feeds = {n: g.load_json_safe(p) for n, p in g.FEEDS}
    assert g.compute_status(feeds) == "DEGRADED"
    print("  [OK] status DEGRADED quand feed absent")


def test_feed_corrompu_non_bloquant():
    # un JSON corrompu -> load_json_safe renvoie None, pas d'exception
    d = tempfile.mkdtemp()
    p = os.path.join(d, "corrompu.json")
    with open(p, "w") as f:
        f.write("{ pas du json valide !")
    assert g.load_json_safe(p) is None
    # et generate_state() ne leve jamais meme avec un feed corrompu
    g.FEEDS = [("corrompu", p)]
    state = g.generate_state()
    assert state is not None
    assert state["feeds"]["corrompu"]["present"] is False
    print("  [OK] feed corrompu : ignore, generate_state() ne leve pas")


def test_feed_hash_stable_ordre_fixe():
    # hash identique pour memes donnees, different si donnees changent
    d = tempfile.mkdtemp()
    p = os.path.join(d, "a.json")
    with open(p, "w") as f:
        json.dump({"v": 1}, f)
    g.FEEDS = [("a", p)]
    feeds1 = {n: g.load_json_safe(p) for n, p in g.FEEDS}
    h1 = g.compute_feed_hash(feeds1)
    h2 = g.compute_feed_hash(feeds1)
    assert h1 == h2, "hash doit etre stable"
    with open(p, "w") as f:
        json.dump({"v": 2}, f)
    feeds2 = {n: g.load_json_safe(p) for n, p in g.FEEDS}
    assert h1 != g.compute_feed_hash(feeds2), "hash doit changer si le feed change"
    print("  [OK] feed_hash stable (ordre fixe) et sensible aux changements")


def test_verify_hash_detecte_corruption():
    # verify_hash(False) si le state a un hash different des feeds actuels
    d = tempfile.mkdtemp()
    p = os.path.join(d, "a.json")
    with open(p, "w") as f:
        json.dump({"v": 1}, f)
    g.FEEDS = [("a", p)]
    feeds = {n: g.load_json_safe(p) for n, p in g.FEEDS}
    state = {"feed_hash": g.compute_feed_hash(feeds)}
    assert g.verify_hash(state) is True
    state_bad = {"feed_hash": "0" * 64}
    assert g.verify_hash(state_bad) is False
    print("  [OK] verify_hash detecte un state au hash invalide")


def test_ecriture_atomique():
    # write_atomic produit un state.json valide, jamais de .tmp residuel
    d = tempfile.mkdtemp()
    g.SYSTEM_DIR = d
    g.STATE_PATH = os.path.join(d, "state.json")
    state = {"timestamp": "t", "status": "HEALTHY", "v": 1}
    g.write_atomic(state)
    with open(g.STATE_PATH) as f:
        loaded = json.load(f)
    assert loaded == state
    assert not os.path.exists(g.STATE_PATH + ".tmp"), "pas de .tmp residuel"
    print("  [OK] ecriture atomique : JSON valide, pas de .tmp residuel")


def test_zero_prose():
    # Loi du brut : state.json ne doit contenir aucune valeur texte longue
    d = tempfile.mkdtemp()
    p = os.path.join(d, "a.json")
    with open(p, "w") as f:
        json.dump({"ts": "2026-08-10T00:00:00Z"}, f)
    g.FEEDS = [("a", p)]
    g.FRESH_SECONDS = {"a": 120}
    state = g.generate_state()
    raw = json.dumps(state, ensure_ascii=False)
    # aucune chaine de plus de 80 chars = pas de prose/resume narratif
    import re
    long_strings = re.findall(r'"[^"]{80,}"', raw)
    assert not long_strings, "prose detectee dans state: %s" % long_strings[:2]
    print("  [OK] loi du brut : aucune prose (aucune chaine longue) dans state")


def main():
    print("=== Tests system_state_generator v2.1 ===")
    tests = [
        test_status_healthy,
        test_status_degraded_feed_absent,
        test_feed_corrompu_non_bloquant,
        test_feed_hash_stable_ordre_fixe,
        test_verify_hash_detecte_corruption,
        test_ecriture_atomique,
        test_zero_prose,
    ]
    ok = 0
    for t in tests:
        t()
        ok += 1
    print("\n%s/%s tests OK ✅" % (ok, len(tests)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
