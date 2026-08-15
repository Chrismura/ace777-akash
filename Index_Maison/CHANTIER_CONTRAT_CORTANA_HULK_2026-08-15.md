# CHANTIER — Contrat JSON Cortana ↔ moteur Hulk (v1 ADVISORY) — 15/08/2026

**Statut : APPLIQUÉ + TESTÉ (bout en bout)** · hors genesis · réversible.

## Décision famille (gemini 85% / nvidia 72%)
GO-AVEC-RÉSERVE : contrat JSON + **ADVISORY strict** ; **NO auto-application tant que justesse < 60%** (Cortana = 44% aujourd'hui). Liste blanche : DIP/RIP_FLOOR_MULT ±15%, STOP_FLOOR_MULT ±10%, NOTIONAL_MULT ±10%. Anti-gaming : whitelist, bornes, `expiry`, `param_class`, confidence « haute » ignorée < 60%. Fail-safe : fichier absent/corrompu → paramètres GELÉS.

## Livré
1. **`hulk-mexc/scripts/cortana_contract.py`** (nouveau) : `BOUNDS`, `load_proposals` (fail-safe), `validate_proposals` (whitelist/bornes/expiry/confiance), `apply_overrides` (clampé, gated ≥0.60), `process_pilot`.
2. **`hulk-mexc/strategie/cortana_pilot.json`** (nouveau) : contrat initial (score 0.44, ADVISORY, proposals []).
3. **`paper_diprip.py`** : import `process_pilot` + config (`CORTANA_MODE`, `CORTANA_PILOT_FILE`) + `refresh_cortana_pilot()` (boot + chaque cycle) + heartbeat `cortana=N`.
4. **`defaults.env`** : `CORTANA_MODE=ADVISORY`, `CORTANA_PILOT_FILE=strategie/cortana_pilot.json`.
5. **`hulk-mexc/scripts/cortana_propose_params.py`** (nouveau) : côté écriture — Cortana lit état Hulk + score justesse, propose (hub cortana.analyse), valide, écrit le pilot (atomique).

## Vérifications (toutes vertes)
- `py_compile` ×3 → OK.
- Test contrat **6/6** : absent→GELÉ · valide→pending=1/applied={} · hors bornes→rejet · haute+44%→rejet · AUTO+44%→applied={} (gated) · AUTO+80%→clampé 0.5→0.85.
- **Bout en bout réel** : `cortana_propose_params.py` → Cortana a proposé DIP_FLOOR_MULT=0.88 (confiance **faible**, raison ancrée : « 11 positions en négatif, score 44% → filtrer faux dips ») → écrit en ADVISORY. La discipline F1 est respectée (pas de « haute » à 44%).

## Prise d'effet
Le process Hulk tourne encore (PID 68481) → hooks moteur actifs au prochain redémarrage. En ADVISORY, rien n'est appliqué : les propositions sont loggées (données shadow pour la boucle A/B).

## Retour arrière (réversible)
- Supprimer les 3 fichiers neufs + `git checkout -- hulk-mexc/scripts/paper_diprip.py` + supprimer les 2 lignes CORTANA_* de defaults.env.

## Suite (validée Christophe, GO reçu)
- **Chantier « 2 classes de paires Hulk »** (core liquides vs small caps bag) — concept validé famille ce jour.
- Objectif justesse Cortana → 93% : analyse par indice, boucle F1 renforcée, discipline « zéro faute » (NEUTRE < 60%), re-mesure continue.
