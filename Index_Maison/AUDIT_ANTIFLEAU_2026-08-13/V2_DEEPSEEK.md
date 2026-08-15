# V2 — DEEPSEEK

**Verdict : GO**

Les 4 points sont couverts par les extraits fournis : cache TTL 15 s effectif dans `_reseau_disponible`, `max(5, ...)` appliqué à la fois dans la boucle et le filet, break immédiat sur `ReseauIndisponible` quand `reseau_ok` est faux (mode dégradé) et continue sinon, et `REQUEST_MAX_SECONDS=180` en dur. Aucune réserve restante sur ces items.
