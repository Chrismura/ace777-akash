# CHANTIER — Quant desk v1 (boucle Bull/Bear/Risque, mode OMBRE) — 15/08/2026

**Statut : APPLIQUÉ + TESTÉ de bout en bout** · mode ombre (conseil différé) · réversible.

## Décision famille (gemini rang 2 « hulk_quant_loop » / nvidia structure quant desk)
Origine : signets N°25 + N°68 @antpalkin (trader top 0,04% WorldQuant qui réécrit ses stratégies perdantes) + N°50 @gippp69 (workflows Anthropic). **Supervision : v1 = conseil différé en ombre** — confronter des thèses et écrire un avis, RIEN appliqué (cohérent avec la famille : « conseil différé »).

## Livré
- `Index_Maison/scripts/quant_desk.py` : stdlib, lit l'état Hulk réel (state JSON le + récent) + digest veille + 3 dernières analyses Cortana + justesse → 3 avocats (BULL/BEAR/RISQUE, task `quant_desk`) → arbitre (task `quant_desk.arbitre`, format strict VERDICT/CONFIANCE/ACTION) → rapport + JSON.
- Rapport `thermo/QUANT_DESK.md` (plaidoiries verbatim + verdict + croisement Cortana + encadré « rien d'appliqué ») + JSON `strategie/quant_desk.json` (`applique: false`).
- **OFF par défaut** (pas dans le launchd quotidien — 4 appels hub/jour = coût réseau ; outil à la demande).
- Exit : 0 verdict rendu · 1 hub injoignable · 2 pas de state Hulk.

## Vérifications (vertes)
- `py_compile` OK · **run réel 4 appels hub** : BULL (garder EDEL/RIZE/CHIP, IMPULSE_WAIT) vs BEAR (purger QAIT/RWAINC, geler achats DEAD) vs RISQUE (sur-dilution 11 positions sur 19$, slippage vol DEAD, corrélation small caps) → **ARBITRE : PRUDENT / confiance moyenne / « maintenir les impulsions saines, geler les achats sur volume mort, surveiller le funding »** — cohérent avec les analyses Cortana (funding SHORT, radar NEUTRE).
- Croisement réel : l'arbitre rejoint la lecture de Cortana (funding = squeeze à risque) → le débat fonctionne.

## Notes honnêtes (corrections supervision)
- Codeur : `HUB_URL = 8787/chat` faux (hub = 11435/v1/chat/completions, payload `messages`) + `except` invalide (`socket_timeout` non défini) → corrigés. Le reste (structure avocats/arbitre, extraction du state, fail-open) vérifié ligne à ligne.
- Limite v1 connue : le rapport embarque les analyses Cortana en JSON brut (verbeux) — suffisant pour la v1, à alléger en v2.

## Retour arrière (réversible)
- `rm Index_Maison/scripts/quant_desk.py` (+ `thermo/QUANT_DESK.md` + `strategie/quant_desk.json`).

## Suite possible (v2, quand validé)
- Brancher dans la discipline quotidienne (décommenter) quand le coût réseau est accepté.
- Confronter le verdict du quant desk au PnL réel (fenêtre 48h) → boucle d'apprentissage du débat.
