# BRIEF AUDIT FAMILLE E1 (loi 1quinquies) — 10/08

CONTEXTE : Systeme ACE777 - Mac 8 Go, hub local 11435 (9 providers gratuits),
29 services launchd. Setup des 3 étages validé par la famille (SPEC V2.1 : GO
unanime GEMINI + JUGE, 10/08). Loi 1quinquies : après la SPEC validée et le
code, vient l'AUDIT FAMILLE DIFF de l'implémentation avant le GO Christophe.

ÉTAPE E1 IMPLÉMENTÉE (voie additive, rien d'autre touché) :
- Index_Maison/scripts/system_state_generator.py v2.1 (NOUVEAU)
- Index_Maison/scripts/test_system_state_generator.py (NOUVEAU)
- Index_Maison/system/state.json (NOUVEAU, 2 169 octets)
Rien n'est chargé dans launchd (c'est E2). Aucun fichier existant modifié.
Backup 21 Go + ROLLBACK.md en place.

PREUVE RÉELLE (vérifiée à l'instant, pas de mémoire) :
- py_compile : OK
- tests unitaires : 7/7 OK
- state.json généré : status=STALE (cortana_feed + live figés 43 min = bots
  arrêtés), feed_hash valide, services 27 (running 3 / planned 24)

=== CODE RÉEL — system_state_generator.py ===
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""system_state_generator.py — v2.1 (SPEC V2.1 validée famille 10/08).

Génère state.json : la mémoire mécanique de la COUCHE SYSTÈME (la 3e, après
mission.json pour le trading et cortana_feed.json pour le vocal).

LOI DU BRUT (gravé dans la spec) : la machine ECRIT le brut, l'IA LIT le brut,
PERSONNE n'interprète entre les deux.
=> state.json ne contient AUCUNE prose, AUCUN résumé, AUCUNE interprétation.
   Uniquement des mesures brutes : timestamps, compteurs, status, hashs.
   Toute transformation éventuelle ira dans une couche analysis/ séparée.

Réserve famille P1 (GEMINI + JUGE) :
  - "status" : HEALTHY | STALE | DEGRADED (seuils mesurés)
  - "feed_hash" : SHA-256 des 4 feeds agrégés (ordre fixe)
  - load_json_safe() : un feed corrompu est ignoré, jamais bloquant

Écriture ATOMIQUE : .tmp puis os.replace() — jamais de state.json corrompu.

Usage:
    python3 system_state_generator.py            # écrit state.json (cadence 2 min via plist)
    python3 system_state_generator.py --check    # lit state.json et affiche status/hash
    python3 system_state_generator.py --dry-run  # calcule sans écrire
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1/Index_Maison")
SYSTEM_DIR = os.path.join(BASE, "system")
STATE_PATH = os.path.join(SYSTEM_DIR, "state.json")
COCKPIT = os.path.join(BASE, "cockpit")
THERMO = os.path.join(BASE, "thermo")
ROUTING = os.path.expanduser("~/prise-ia/routing.json")
HUB_HEALTH = "http://127.0.0.1:11435/health"

# Ordre FIXE des feeds pour le hash (réserve famille : "ordre fixe")
FEEDS = [
    ("mission", os.path.join(COCKPIT, "mission.json")),
    ("cortana_feed", os.path.join(THERMO, "cortana_feed.json")),
    ("live", os.path.join(THERMO, "live.json")),
    ("routing", ROUTING),
]

# Seuils de fraîcheur (réserve famille P1, validés) :
# live.json est temps réel (5 s) -> 15 s max. Les autres -> 2 min.
FRESH_SECONDS = {"live": 15, "mission": 120, "cortana_feed": 120, "routing": 120}

# Dossiers hors zone (contrôle de PRÉSENCE léger, réserve P5 — métadonnées
# uniquement, jamais de lecture récursive).
HORS_ZONE = {
    "mirofis": os.path.expanduser("~/mirofis"),
    "crypto_voice_core": os.path.expanduser("~/crypto-voice-assistant-core"),
    "archives_brutes": os.path.expanduser("~/ACE777_ARCHIVES_BRUTES_DONNEES"),
    "vocal_hors_vault": os.path.expanduser("~/Assistant_Vocal_HORS_VAULT"),
    "obsidian_backups": os.path.expanduser("~/Obsidian_BACKUPS_HORS_VAULT"),
}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json_safe(path):
    """Réserve P1-4 : un feed corrompu est ignoré, jamais bloquant."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def age_seconds(path):
    if not os.path.exists(path):
        return None
    return int(time.time() - os.path.getmtime(path))


def compute_status(feeds):
    """Réserve P1-1 : HEALTHY / STALE / DEGRADED selon la fraîcheur."""
    any_missing = False
    any_stale = False
    for name, path in FEEDS:
        present = feeds.get(name) is not None
        if not present:
            any_missing = True
            continue
        age = age_seconds(path)
        if age is None or age > FRESH_SECONDS.get(name, 120):
            any_stale = True
    if any_missing:
        return "DEGRADED"
    if any_stale:
        return "STALE"
    return "HEALTHY"


def compute_feed_hash(feeds):
    """Réserve P1-2 : SHA-256 des 4 feeds agrégés dans l'ordre fixe."""
    h = hashlib.sha256()
    for name, _path in FEEDS:
        data = feeds.get(name)
        if data is None:
            h.update(b"<absent>")
        else:
            h.update(json.dumps(data, sort_keys=True, ensure_ascii=False).encode())
    return h.hexdigest()


def run(cmd, timeout=6):
    try:
        return subprocess.check_output(cmd, shell=True, text=True,
                                       timeout=timeout).strip()
    except Exception:
        return ""


def services_etat():
    """Brut : vivants (PID) vs planifiés (-) — même logique que mon_cockpit."""
    out = run("launchctl list | grep ace777")
    vivants, planifies = [], []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) < 3:
            continue
        pid, name = parts[0], parts[2]
        (vivants if pid != "-" else planifies).append(name)
    return sorted(vivants), sorted(planifies)


def hub_sante():
    """Brut : {"status": "ok", "providers": N} ou null."""
    try:
        import urllib.request
        with urllib.request.urlopen(HUB_HEALTH, timeout=4) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None


def generate_state():
    """Construit le state brut. Ne lève JAMAIS (loi non-fatale)."""
    feeds = {name: load_json_safe(path) for name, path in FEEDS}
    vivants, planifies = services_etat()
    hub = hub_sante()
    ram = run("memory_pressure 2>/dev/null | head -2")

    # Présence des dossiers hors zone : métadonnées uniquement (réserve P5)
    hors_zone = {}
    for name, path in HORS_ZONE.items():
        try:
            present = os.path.isdir(path)
            size_ko = int(os.path.getsize(path) / 1024) if present else 0
            hors_zone[name] = {"present": present, "size_ko": size_ko}
        except Exception:
            hors_zone[name] = {"present": False, "size_ko": 0}

    state = {
        "timestamp": now_iso(),
        "generation_source": "system_state_generator.py v2.1",
        "status": compute_status(feeds),
        "feed_hash": compute_feed_hash(feeds),
        "feeds": {
            name: {
                "present": feeds.get(name) is not None,
                "age_seconds": age_seconds(path),
                "fresh_limit_s": FRESH_SECONDS.get(name, 120),
            }
            for name, path in FEEDS
        },
        "services": {
            "total": len(vivants) + len(planifies),
            "running": len(vivants),
            "planned": len(planifies),
            "running_list": vivants,
            "planned_list": planifies,
        },
        "hub": hub,
        "ram_raw": ram or None,
        "hors_zone": hors_zone,
    }
    return state


def write_atomic(state):
    """Écriture ATOMIQUE : .tmp puis os.replace() (jamais de fichier corrompu)."""
    os.makedirs(SYSTEM_DIR, exist_ok=True)
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, STATE_PATH)


def verify_hash(state):
    """Réserve P1-3 : vérifie que le feed_hash du state correspond aux feeds actuels."""
    feeds = {name: load_json_safe(path) for name, path in FEEDS}
    return state.get("feed_hash") == compute_feed_hash(feeds)


def main():
    if "--check" in sys.argv:
        try:
            with open(STATE_PATH, encoding="utf-8") as f:
                s = json.load(f)
        except Exception as e:
            print("state.json illisible: %s" % e)
            return 2
        print("status: %s" % s.get("status"))
        print("timestamp: %s" % s.get("timestamp"))
        print("feed_hash: %s" % s.get("feed_hash"))
        print("hash valide maintenant: %s" % verify_hash(s))
        print("services: %d (running %d / planned %d)"
              % (s.get("services", {}).get("total", 0),
                 s.get("services", {}).get("running", 0),
                 s.get("services", {}).get("planned", 0)))
        return 0

    state = generate_state()
    if "--dry-run" in sys.argv:
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return 0

    write_atomic(state)
    print("[OK] state.json ecrit (%d o) — status=%s — %s"
          % (os.path.getsize(STATE_PATH), state["status"], state["timestamp"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())


=== TESTS — test_system_state_generator.py ===
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


=== state.json GÉNÉRÉ (brut, réel) ===
{
  "timestamp": "2026-08-10T08:13:11Z",
  "generation_source": "system_state_generator.py v2.1",
  "status": "STALE",
  "feed_hash": "2c99a06d80d9d683db4a41b80386d13b9070ff7d738ed32d0f57dedd1bca6f46",
  "feeds": {
    "mission": {
      "present": true,
      "age_seconds": 2,
      "fresh_limit_s": 120
    },
    "cortana_feed": {
      "present": true,
      "age_seconds": 2586,
      "fresh_limit_s": 120
    },
    "live": {
      "present": true,
      "age_seconds": 2592,
      "fresh_limit_s": 15
    },
    "routing": {
      "present": true,
      "age_seconds": 45587,
      "fresh_limit_s": 120
    }
  },
  "services": {
    "total": 27,
    "running": 3,
    "planned": 24,
    "running_list": [
      "com.ace777.cockpit-http",
      "com.ace777.cockpit-pont",
      "com.ace777.prise-ia"
    ],
    "planned_list": [
      "com.ace777.analyse-usage",
      "com.ace777.analyste-cadence",
      "com.ace777.autopilote",
      "com.ace777.brief-matin",
      "com.ace777.catalogue",
      "com.ace777.cortana.horaire",
      "com.ace777.cortana.urgent",
      "com.ace777.eval-offres",
      "com.ace777.gitpush",
      "com.ace777.gitpush-vault",
      "com.ace777.graph-cerveau",
      "com.ace777.heartbeat",
      "com.ace777.journal-soir",
      "com.ace777.observatoire",
      "com.ace777.propose-ameliorations",
      "com.ace777.pulse-sous-loeil",
      "com.ace777.qwen-btc",
      "com.ace777.qwen-elabore",
      "com.ace777.rotation-logs",
      "com.ace777.superviseur",
      "com.ace777.surveillance-quotas",
      "com.ace777.veille-hub",
      "com.ace777.verif-setup",
      "com.ace777.vigie"
    ]
  },
  "hub": {
    "status": "ok",
    "providers": 9
  },
  "ram_raw": "The system has 8589934592 (524288 pages with a page size of 16384).",
  "hors_zone": {
    "mirofis": {
      "present": true,
      "size_ko": 0
    },
    "crypto_voice_core": {
      "present": true,
      "size_ko": 0
    },
    "archives_brutes": {
      "present": true,
      "size_ko": 0
    },
    "vocal_hors_vault": {
      "present": true,
      "size_ko": 0
    },
    "obsidian_backups": {
      "present": true,
      "size_ko": 0
    }
  }
}


QUESTIONS À LA FAMILLE (audit diff de l'implémentation E1) :
1. Le code implémente-t-il correctement les 8 réserves de la SPEC V2.1
   (status, feed_hash, load_json_safe, atomicité) ?
2. La LOI DU BRUT est-elle respectée dans le code (aucune prose, aucune
   interprétation, transformation reportée en couche analysis/) ?
3. Y a-t-il un bug, une faille, un risque (RAM, I/O, chemins, sécurité) ?
4. L'écriture atomique (.tmp + os.replace) est-elle correcte ?
5. Verdict final sur l'implémentation E1 : GO / GO AVEC RESERVES / NON
   (avec 1 phrase de justification + réserves concrètes).

