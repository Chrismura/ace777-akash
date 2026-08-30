# SPEC — RACE CONDITION SUR thermo/live.json (27/08/2026)

## Contexte

`thermo/live.json` est la source de vérité du cockpit (64 clés : mark, gex, onchain,
sdi, rbf, pipeline_health, geopol…). 36 scripts le lisent. Le geopol est calculé par
`indice_app/` (5 modules) et injecté par `thermo_quotidien_free.py` (~1h).

## Le problème (prouvé le 27/08)

1. **3 scripts écrivent live.json séparément** (déclaré dans le code du 25/08,
   `consulter_famille_pipeline_unifie_20260825.py` ligne 35 : « RACE CONDITION : 3
   scripts écrivent dans live.json séparément ») :
   - `thermo_quotidien_free.py` → payload COMPLET (64 clés, dont geopol)
   - `pont_onchain.py` → injecte seulement la section `onchain` (SafeLiveWriter,
     lecture-modification-écriture atomique)
   - un 3e écrivain de sous-ensemble (11 clés : chg1h, volQuote, funding, whaleUsd,
     liq24Usd, sdi, ipt, onchain, longShort, takerRatio, fearGreed) — celui-ci a
     ÉCRASÉ le payload complet le 27/08 à 21:06 → geopol/mark/gex ont disparu →
     Cortana a signalé « geo ne marche pas ».

2. **Symptôme observé** : `live.json` réduit à 11 clés (2307 octets) au lieu de 64
   (≈15 ko). Le cockpit perd geopol, mark, gex. Le juge affiche `geopol=[absent]`.
   Restauré depuis live.js (la copie complète), le thermo a réécrit le payload complet
   à 21:12 (auto-réparation) — mais la course peut recasser à tout moment.

3. **Le code du 25/08 le savait** : le script pipeline_unifie documentait la race
   condition mais l'IA l'a laissée en place (« le pipeline est FRAGILE »).

## Question posée à la famille

Quel est le fix structurel PROPRE et SÛR pour garantir qu'un seul écrivain produit le
payload complet de live.json, et que les injecteurs partiels (onchain) ne peuvent
jamais écraser geopol/mark/gex ?

Contraintes :
- Ne pas casser les 36 lecteurs (mêmes clés, même fichier).
- Le thermo tourne ~1h : les injecteurs onchain (5 min) doivent survivre entre deux runs.
- Fail-open : si un écrivain plante, live.json doit rester le dernier payload complet.
- Style maison : écrivain atomique existant (`atomic_write.py` / SafeLiveWriter),
  verrous, un seul point d'écriture, pas de réécriture inventée.

VERDICT attendu : GO / GO-AVEC-RÉSERVE / NON, avec la conception concrète
(fichier, fonction, verrou) et les risques résiduels.
