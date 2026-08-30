#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TEST de résolution — 20/08/2026 (Buffy, demande Christophe).

Objectif : discriminer entre
  (A) artefact de résolution : tx publiques entrées/minées entre deux
      snapshots espacés (10 min) -> faussement « fantômes »
  (B) vraies tx privées : jamais vues dans la mempool publique (OTC/CPFP
      masqué) -> le signal de la pépite de Christophe.

Méthode : snapshots denses (60 s) accumulés dans un historique glissant,
comparés aux txids des blocs successifs. Si le taux chute avec la densité
=> (A). S'il reste élevé => (B).
"""
import os, sys, time, json, urllib.request

BASE_DIR = os.path.expanduser("~/ace777-test-day1")
DATA_DIR = os.path.join(BASE_DIR, "Index_Maison", "data")
HIST = os.path.join(DATA_DIR, "mempool_vus_TEST_DENSE.jsonl")
UA = {"User-Agent": "ACE777-TestResolution/1.0"}

def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode())

def get_text(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode().strip()

def load_history():
    seen = set()
    if os.path.exists(HIST):
        for line in open(HIST):
            try:
                seen.update(json.loads(line).get("txids", []))
            except Exception:
                pass
    return seen

os.makedirs(DATA_DIR, exist_ok=True)
seen = load_history()
last_bloc = None
start = time.time()
print(f"[TEST] Démarrage {time.strftime('%H:%M:%S')} — historique initial: {len(seen)} txids")

while time.time() - start < 1500:  # ~25 min
    try:
        tip = get_text("https://mempool.space/api/blocks/tip/hash")
        txids_bloc = get_json(f"https://mempool.space/api/block/{tip}/txids")
        mp = get_json("https://mempool.space/api/mempool/txids")
        seen.update(mp)
        with open(HIST, "a") as f:
            f.write(json.dumps({"ts": int(time.time()), "txids": mp}) + "\n")
        if tip != last_bloc:
            last_bloc = tip
            fantomes = [t for t in txids_bloc if t not in seen]
            taux = len(fantomes) / len(txids_bloc) * 100
            print(f"[TEST] {time.strftime('%H:%M:%S')} NOUVEAU bloc {tip[:12]} "
                  f"| tx={len(txids_bloc)} fantômes={len(fantomes)} taux={taux:.1f}% "
                  f"| historique={len(seen)} txids")
        else:
            print(f"[TEST] {time.strftime('%H:%M:%S')} snapshot +{len(mp)} "
                  f"(historique={len(seen)}) — bloc inchangé")
    except Exception as e:
        print(f"[TEST] erreur: {e}")
    time.sleep(60)
print("[TEST] Terminé")
