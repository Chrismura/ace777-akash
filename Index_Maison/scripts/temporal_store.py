#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
temporal_store.py — Store temporel LMDB + Dead Man's Switch
Famille ACE777 — Étape 3 : isolation Hot/Warm/Cold + DMS

Utilisation :
    with TemporalStore() as store:
        store.write("hot", "btc_price", {"price": 64200})
        data = store.read("hot", "btc_price")
        store.heartbeat("thermo")
        dead = store.dead_man_check("thermo", max_silence=15.0)
"""
import os
import time
import json
from typing import Optional, Dict, Any

try:
    import lmdb
except ImportError:
    raise ImportError("lmdb requis : pip install lmdb")


DEFAULT_TTLS = {
    "hot": 10.0,       # prix, spread, liquidations
    "warm": 3600.0,    # funding, corrélations, score
    "cold": 86400.0,   # baleines, ETF, macro
}


class TemporalStore:
    """Store temporel LMDB avec isolation par tier et Dead Man's Switch."""

    def __init__(self, db_path: str = None, map_size: int = 200 * 1024 * 1024):
        if db_path is None:
            db_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "..", "data", "temporal_bus.lmdb"
            )
        self.db_path = os.path.abspath(db_path)
        db_dir = os.path.dirname(self.db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)

        self.env = lmdb.open(
            self.db_path,
            map_size=map_size,
            max_dbs=4,
            sync=True,
            metasync=True,
        )
        self.dbs = {
            "hot": self.env.open_db(b"hot"),
            "warm": self.env.open_db(b"warm"),
            "cold": self.env.open_db(b"cold"),
            "meta": self.env.open_db(b"meta"),
        }

    def close(self):
        if self.env:
            self.env.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def write(self, tier: str, key: str, data: Dict[str, Any]) -> None:
        if tier not in ("hot", "warm", "cold"):
            raise ValueError(f"Tier invalide: {tier}")
        payload = {"data": data, "ts": time.time()}
        serialized = json.dumps(payload).encode("utf-8")
        with self.env.begin(db=self.dbs[tier], write=True) as txn:
            txn.put(key.encode("utf-8"), serialized)

    def read(self, tier: str, key: str) -> Optional[Dict[str, Any]]:
        max_age = DEFAULT_TTLS.get(tier, 86400.0)
        return self.read_fresh(tier, key, max_age)

    def read_fresh(self, tier: str, key: str, max_age_seconds: float) -> Optional[Dict[str, Any]]:
        if tier not in ("hot", "warm", "cold"):
            return None
        with self.env.begin(db=self.dbs[tier], write=False) as txn:
            raw = txn.get(key.encode("utf-8"))
            if not raw:
                return None
        try:
            item = json.loads(raw.decode("utf-8"))
            ts = item.get("ts", 0.0)
            if (time.time() - ts) > max_age_seconds:
                return None
            return item.get("data")
        except (json.JSONDecodeError, KeyError):
            return None

    def heartbeat(self, writer_name: str) -> None:
        now = time.time()
        with self.env.begin(db=self.dbs["meta"], write=True) as txn:
            txn.put(f"hb_{writer_name}".encode("utf-8"), str(now).encode("utf-8"))

    def dead_man_check(self, writer_name: str, max_silence: float = 15.0) -> bool:
        """Retourne True si le writer est MORT (pas de heartbeat depuis max_silence)."""
        with self.env.begin(db=self.dbs["meta"], write=False) as txn:
            raw = txn.get(f"hb_{writer_name}".encode("utf-8"))
        if not raw:
            return True
        try:
            last_hb = float(raw.decode("utf-8"))
            return (time.time() - last_hb) > max_silence
        except (ValueError, TypeError):
            return True


if __name__ == "__main__":
    import tempfile

    print("=== TEST TEMPORAL STORE ===")
    with tempfile.TemporaryDirectory() as td:
        db = os.path.join(td, "test.lmdb")
        with TemporalStore(db_path=db) as store:
            # Write Hot
            store.write("hot", "btc_price", {"price": 64200.0, "side": "buy"})
            store.write("hot", "funding", {"rate": 0.0001})
            store.write("warm", "gex", {"callWall": 82000, "putWall": 60000})
            store.write("cold", "whales", {"dir": "neutral", "blocs": 16})

            # Read
            hot = store.read("hot", "btc_price")
            print(f"Hot btc_price: {hot}")
            assert hot["price"] == 64200.0

            warm = store.read("warm", "gex")
            print(f"Warm gex: {warm}")
            assert warm["callWall"] == 82000

            cold = store.read("cold", "whales")
            print(f"Cold whales: {cold}")
            assert cold["dir"] == "neutral"

            # TTL test (hot expire après 10s)
            store.write("hot", "old_tick", {"price": 100})
            fresh = store.read_fresh("hot", "old_tick", max_age_seconds=999)
            assert fresh is not None
            expired = store.read_fresh("hot", "old_tick", max_age_seconds=0)
            assert expired is None
            print("TTL test: ✅")

            # DMS
            store.heartbeat("thermo")
            assert not store.dead_man_check("thermo", max_silence=10)
            assert store.dead_man_check("thermo", max_silence=0)
            assert store.dead_man_check("unknown_writer", max_silence=10)
            print("DMS test: ✅")

    print("\n✅ TOUS LES TESTS PASSÉS")
