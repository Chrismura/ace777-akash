# AUDIT FINAL ACE V2–V4 — 2026-09-01

> Audit complet en lecture seule. Aucun moteur lancé, aucun ordre envoyé.
> Champion intact : `14bcf868d46effba010cac577cbb004c`

## Résumé exécutif

Sur 3 runs testnet de 15 minutes (V2, V3, V4), ACE a produit 16 trades au total.
Le résultat net cumulé est **-13,95 USDT** sur 45 minutes de trading.

La rentabilité n'est pas un problème de gate, de spread ou de frais seul.
Ce sont **trois défauts structurels combinés** qui rendent Beta non rentable.

---

## Trois racines de perte identifiées

### 1. Confiance inversée

La métrique `conf` du moteur est **positivement corrélée aux pertes** :

| Sortie | Trades | Conf moyenne | Net |
|---|---:|---:|---:|
| stop_loss | 8 | **0,848** | -17,08 |
| trailing_stop | 5 | 0,731 | +0,15 |
| kill_switch | 2 | 0,635 | -1,30 |

Les trades les plus confiants (0,9992, 0,9968) sont les plus perdants.
La confiance ne prédit pas la direction — elle prédit peut-être la volatilité.

### 2. Entrée à l'envers du radar

Beta utilise `FORCE_ENTRY_SIDE=SELL` (fixé par le lanceur) mais le radar indique parfois `long` :

- V2 cycle 13 : `radar=long` → entrée SELL → stop_loss (-0,88)
- V2 cycle 28 : `radar=long` → entrée SELL → stop_loss (-1,75)
- V2 cycle 44 : `radar=long` → entrée SELL → stop_loss (-0,83)

Le scout entre dans le mauvais sens car sa direction est imposée, pas décidée par le signal.

### 3. Trailing_stop gagne en brut mais pas après frais

Les 5 trailing_stops cumulent +5,33 brut mais seulement +0,15 net :

| Trade | Brut | Frais | Net |
|---|---:|---:|---:|
| V2 Alpha cycle 14 | +2,02 | +1,08 | +0,94 |
| V2 Alpha cycle 81 | +1,55 | +1,31 | +0,24 |
| V3 Alpha cycle 4 | +0,96 | +1,08 | **-0,12** |
| V3 Beta cycle 20 | +0,18 | +0,64 | **-0,46** |
| V4 Alpha cycle 20 | +0,62 | +1,08 | **-0,45** |

Seuls les trades Alpha à levier x13 avec hold court génèrent un net positif.
Les trades Beta à levier x5 avec hold long sont systématiquement négatifs après frais.

---

## Ce qui fonctionne

- Alpha trailing_stop avec hold court : positif net dans 2 cas sur 3.
- L'infrastructure de reporting est maintenant fiable.
- Les rapports brut/frais/net sont cohérents.
- Les observations structurées sont exploitables.

## Ce qui ne fonctionne pas

- Le modèle de confiance n'est pas un prédicteur de rentabilité.
- La direction fixe `FORCE_ENTRY_SIDE=SELL` ignore le signal radar.
- Les trades trop courts ou trop petits ne couvrent pas les frais.
- Le kill_switch ferme des positions à faible perte, mais les frais restent.

---

## Recommandations (sans modifier le champion)

### P0 — Ne pas relancer

```text
ACE LIVE : interdit
Nouveau testnet : déconseillé
```

### P1 — Analyse hors exécution

1. **Replay local** avec les données de tension déjà extraites pour tester si un filtre sur `conf > X` aurait amélioré le résultat.
2. **Comparaison Alpha/Beta** : Alpha est la seule unité capable de générer un net positif. Isoler ses paramètres.

### P2 — Prochaine instrumentation

1. Le moteur doit écrire une observation structurée avant chaque décision.
2. Le champ `conf` doit être validé comme prédicteur avant d'influencer les gates.
3. `FORCE_ENTRY_SIDE` doit être remplacé par une décision basée sur le signal radar.

---

## Fichiers générés cet audit

```text
scripts/observation_recorder.py          # enregistreur CSV
scripts/run_observation_shadow.py        # replay local
scripts/convert_csv_to_observations.py   # CSV → observations
scripts/parse_engine_log_observations.py # logs → observations
scripts/compare_observation_runs.py      # comparaison V2–V4
scripts/analyze_observation_gates.py     # analyse gates
scripts/analyze_engine_observations.py   # qualité instrumentation
scripts/analyze_tension_by_unit.py       # tension par unité
scripts/consolidate_ace_runs.py          # consolidation faits
scripts/analyze_beta_trades.py           # économie trades Beta
scripts/deep_beta_analysis.py            # analyse profonde msg field
scripts/audit_fee_model.py               # vérification frais
scripts/audit_historical_setups.py       # historique setups
scripts/replay_ramp_compare.py           # comparaison levier
scripts/test_*.py                        # tests hermétiques
```

```text
runs/ACE_OBSERVATION_COMPARISON_V2_V4.md
runs/ACE_GATE_ANALYSIS_V2_V4.md
runs/ACE_ENGINE_OBSERVATION_QUALITY_V2_V4.md
runs/ACE_TENSION_BY_UNIT_V2_V4.md
runs/ACE_CONSOLIDATED_V2_V4.md
runs/ACE_BETA_TRADE_ECONOMICS_V2_V4.md
runs/ACE_DEEP_ANALYSIS_V2_V4.md
```

---

## Verdict final

```text
Infrastructure : PASS
Comptabilité   : PASS
Rentabilité    : FAIL — racines identifiées
Champion       : intact
ACE LIVE       : NO-GO
```

La prochaine étape n'est pas un correctif de gate. C'est une revue de la logique
d'entrée Beta et du modèle de confiance, en replay local, avant tout nouveau testnet.

---
*Audit Buffy — 2026-09-01*
