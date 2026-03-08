# ACE777 — Journal Quotidien Calibration (Phase 2)

## Date
- YYYY-MM-DD:
- Opérateur:

## Baseline du jour
- Config: `genesis_active.1437`
- Dataset: `input_minute.csv`
- Seed: `1437`

---

## Run 1 — BASELINE
- Config:
- Net Client (%):
- Net Client ($):
- IR (Net/Calories):
- IR_total (Net/(Cal+Exec+Arch)):
- Passed/Skipped:
- Shock/Safe cycles:
- Observations:

## Run 2 — V3.2
- Config:
- Net Client (%):
- Net Client ($):
- IR:
- IR_total:
- Passed/Skipped:
- Shock/Safe cycles:
- Observations:

## Run 3 — CANDIDATE
- Config:
- Net Client (%):
- Net Client ($):
- IR:
- IR_total:
- Passed/Skipped:
- Shock/Safe cycles:
- Observations:

---

## Comparatif du jour (delta vs BASELINE)
- Delta Net %:
- Delta IR:
- Delta IR_total:
- Delta coût exécution:
- Delta skip rate:

## Check invariants (obligatoire)
- 1:1 respecté: [OK/KO]
- SAFE/TTL/quorum corrects: [OK/KO]
- Pas d’anomalie critique: [OK/KO]

## Décision
- [ ] GO candidat
- [ ] NO-GO candidat
- Motif:
- Actions demain (Top 3):
  1.
  2.
  3.

## Run 1 — BASELINE (rempli)
- Config: `genesis_active.1437`
- Net Client (%): `13.47`
- Net Client ($): `134.75`
- IR (Net/Calories): `5.16`
- IR_total (Net/(Cal+Exec+Arch)): `3.42`
- Passed/Skipped: `1428 / 12`
- Shock/Safe cycles: `216 / 12`
- Observations: `Run stable, coûts contenus, cible >15% non atteinte`

## Run 2 — V3.2 (rempli)
- Config: `vortex_v3_2_final.1437`
- Net Client (%): `13.47`
- Net Client ($): `134.75`
- IR (Net/Calories): `5.16`
- IR_total (Net/(Cal+Exec+Arch)): `3.42`
- Passed/Skipped: `1428 / 12`
- Shock/Safe cycles: `216 / 12`
- Observations: `Preset performant et robuste, mais cible >15% non atteinte sur dataset hard`
