# V2 — JUGE

1. **Cache Réseau** : TTL 15s validé, évite les surcharges DNS par requête.
2. **Plancher Timeout** : `max(5, ...)` appliqué boucle et filet, protège les réponses lentes légitimes.
3. **Circuit-Breaker** : Arrêt immédiat si réseau déjà KO, bascule tolérée en mode normal.
4. **Budget 180s** : Bornage efficace contre le fléau tout en laissant passer DeepSeek.

**Verdict : GO**
