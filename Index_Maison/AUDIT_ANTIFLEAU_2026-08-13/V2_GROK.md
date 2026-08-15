# V2 — GROK

Les 4 points sont correctement implémentés dans les extraits fournis : cache TTL 15s opérationnel, plancher `max(5, ...)` appliqué en boucle et filet, break immédiat sur `ReseauIndisponible` quand `reseau_ok=False` (mode dégradé) vs continue sinon, et `REQUEST_MAX_SECONDS=180` par défaut surchargeable.

GO
