# Attention — Validation test avant réel

**Date :** 2026-07-30  
**Statut :** `GARDÉ` · S26 · #27  
**Canon :** [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]] · [[JOURNAL_ERREURS_TEST]]

## 3 lignes
Oui : valider en test avant le réel — doctrine métier (UAT / go-no-go).  
3 portes : hygiène → cockpit/BOARD → run test → signature Christophe pour tout réel.  
Journal d’erreurs ouvert (P0–P3) — une anomalie = une ligne.

## Avant le prochain run test
```bash
cd ~/ace777-test-day1 && ./scripts/verif_sterilite.sh --pre-run
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_hygiene_check.sh
# pont + open cockpit si lecture UI
# puis GO explicite → ./GO_USINE_NUAGE.sh …
```
