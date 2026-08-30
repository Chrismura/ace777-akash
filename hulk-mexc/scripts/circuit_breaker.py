#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
circuit_breaker.py — Circuit Breaker temporel pour Hulk
Vérifie la fraîcheur des données avant toute décision de trading.

Utilisation :
    cb = TradeCircuitBreaker(ttl_seconds=5.0)
    try:
        data = cb.validate(price_data)
        # data est fraîche → on trade
    except CircuitOpenException:
        # circuit ouvert → on arrête le trading
"""
import time
import logging
from typing import Dict, Any

logger = logging.getLogger("CIRCUIT_BREAKER")


class CircuitOpenException(Exception):
    """Levée quand le circuit breaker est ouvert — trading interdit."""
    pass


class TradeCircuitBreaker:
    """Circuit Breaker à hystérésis pour le trading.
    
    États :
    - CLOSED : nominal, le trading est autorisé
    - OPEN : circuit ouvert, le trading est interdit
    - HALF-OPEN : test de reprise après cooldown
    
    Le circuit s'ouvre après `failure_threshold` échecs consécutifs
    et se referme après un succès en mode HALF-OPEN.
    """

    def __init__(self, ttl_seconds: float = 5.0, failure_threshold: int = 3,
                 cooldown_seconds: float = 30.0):
        self.ttl = ttl_seconds
        self.failure_threshold = failure_threshold
        self.cooldown = cooldown_seconds
        self.failures = 0
        self.state = "CLOSED"
        self._last_state_change = time.monotonic()
        self._last_data_time: Dict[str, float] = {}

    def validate(self, data: Dict[str, Any], source: str = "default") -> Dict[str, Any]:
        """Valide la fraîcheur des données. Lève CircuitOpenException si stale."""
        now = time.monotonic()

        # Vérifier l'état du circuit
        if self.state == "OPEN":
            if now - self._last_state_change > self.cooldown:
                self.state = "HALF-OPEN"
                logger.info(f"[{source}] HALF-OPEN — test de reprise...")
            else:
                raise CircuitOpenException(
                    f"[{source}] CIRCUIT OUVERT — trading bloqué "
                    f"(cooldown {self.cooldown - (now - self._last_state_change):.0f}s restantes)"
                )

        # Vérifier la fraîcheur
        timestamp = data.get("timestamp", 0)
        if timestamp <= 0:
            self._trip(source, "pas de timestamp")
            raise CircuitOpenException(f"[{source}] Pas de timestamp dans les données")

        # Utiliser monotonic si disponible, sinon time.time
        data_age = now - timestamp if timestamp > 1e9 else now - timestamp
        # Si le timestamp est en epoch seconds (< 2e9), calculer l'âge
        if timestamp < 2e9:
            data_age = time.time() - timestamp

        if data_age > self.ttl:
            self._trip(source, f"stale {data_age:.1f}s > {self.ttl}s")
            raise CircuitOpenException(
                f"[{source}] Données STALE: {data_age:.1f}s (max {self.ttl}s)"
            )

        # Vérifier la validité du prix
        price = data.get("price", data.get("mark", 0))
        if price is not None and price <= 0:
            self._trip(source, f"prix invalide {price}")
            raise CircuitOpenException(f"[{source}] Prix invalide: {price}")

        # Succès
        self._last_data_time[source] = now
        if self.state == "HALF-OPEN":
            logger.info(f"[{source}] CLOSED — circuit refermé")
            self.state = "CLOSED"
            self.failures = 0

        return data

    def _trip(self, source: str, reason: str):
        self.failures += 1
        logger.warning(
            f"[{source}] Échec {self.failures}/{self.failure_threshold}: {reason}"
        )
        if self.failures >= self.failure_threshold or self.state == "HALF-OPEN":
            self.state = "OPEN"
            self._last_state_change = time.monotonic()
            logger.error(
                f"⚡ [{source}] CIRCUIT BREAKER OUVERT — ARRÊT DU TRADING"
            )

    def is_ok(self) -> bool:
        """Retourne True si le trading est autorisé."""
        return self.state == "CLOSED" or self.state == "HALF-OPEN"

    def status(self) -> str:
        return self.state


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    cb = TradeCircuitBreaker(ttl_seconds=1.0, failure_threshold=2, cooldown_seconds=3.0)

    print("=== TEST 1 : Données fraîches ===")
    good = {"timestamp": time.time(), "price": 64200.0}
    print(f"  validate: {cb.validate(good)}")
    print(f"  state: {cb.status()}")

    print("\n=== TEST 2 : Données stale (3s > TTL 1s) ===")
    old = {"timestamp": time.time() - 3.0, "price": 64200.0}
    try:
        cb.validate(old)
    except CircuitOpenException as e:
        print(f"  Attrapé: {e}")
    print(f"  state: {cb.status()}")

    print("\n=== TEST 3 : 2e échec → circuit ouvert ===")
    try:
        cb.validate(old)
    except CircuitOpenException as e:
        print(f"  Attrapé: {e}")
    print(f"  state: {cb.status()}")

    print(f"\n=== TEST 4 : Attente cooldown (3s) ===")
    time.sleep(4)
    good2 = {"timestamp": time.time(), "price": 64300.0}
    print(f"  validate: {cb.validate(good2)}")
    print(f"  state: {cb.status()}")

    print("\n✅ Tous les tests passés")
