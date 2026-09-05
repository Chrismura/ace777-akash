# AUDIT ACE DUO ALPHA/BETA — 2026-09-01

## Méthode
Audit en lecture seule des wrappers, configurations, CSV historiques, `STATE.md`, métadonnées de run, `PROCESS_EXIT.log` et contrat de frais. Aucun lancement ACE et aucun appel d'ordre.

## Identité et séparation

```text
ACE Duo
  BETA  = SCOUT, masse de référence 200 USDT
  ALPHA = HUNTER, masse de référence 800 USDT
  Venue = Binance Futures testnet
  Champion = genesis_manifest.txt / LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt
  Bus = duo_state + duo_session + swarm_telemetry
```

ACE Alpha/Beta est séparé de Hulk. Hulk ne lit pas les CSV ACE pour prendre ses décisions.

## CSV historiques

| Rôle | Fichier | Lignes | Fills | PnL brut additionné |
|---|---|---:|---:|---:|
| ALPHA | `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv` | 55 318 | 1 751 | +292,0142 USDT |
| BETA | `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` | 63 540 | 5 969 | +26,5628 USDT |

Ces CSV sont bien Alpha/Beta et ne sont pas des CSV Hulk. Leur schéma est ancien et ne contient pas toujours `feeUsdt`/`pnlNet`.

La somme historique brute n'est donc pas un PnL net certifié. Elle doit rester étiquetée `gross_csv_legacy` tant qu'une réconciliation par session et par frais n'a pas été faite.

## Dernier run Vortex de référence

```text
Tag          : MASTER_VORTEX_V2_COLLAB_4H
Début        : 2026-08-22T15:44:10Z
Fin prévue   : 2026-08-22T19:43:51Z
Dernier état : ENDED à 2026-08-22T19:13:14Z
```

`STATE.md` indique :

```text
BETA  : 13 fills · -0,7378 USDT
ALPHA :  9 fills · +2,0052 USDT
TOTAL : 22 fills · +1,2674 USDT
```

Le duo a terminé arrêté; ce n'est pas une preuve de panne actuelle.

## Bus et relance

Les fichiers `duo_state.json`, `duo_session.json` et `swarm_telemetry.json` ne sont pas présents actuellement, ce qui est attendu puisque ACE est arrêté.

Les documents historiques montrent toutefois les problèmes réels rencontrés : `stale_state`, `duo_wait`, mort d'une jambe, faux positif watchdog, relance sans resynchronisation et logs parfois insuffisants. Les wrappers actuels ont des protections de reset, MD5 champion, arrêt sur STOP, instrumentation d'exit et fail-fast supervision.

## Frais Binance

Le champion ACE possède un modèle de frais round-trip :

```text
FEE_ROUND_TRIP_BPS = 8
```

Les versions instrumentées calculent :

```text
fee_usdt = notional × 8 / 10000
pnl_net = pnl_brut - fee_usdt
```

et publient le PnL net dans le bus duo pour les versions qui possèdent les colonnes `feeUsdt,pnlNet`.

Parallèlement, `fees_platforme.py` interroge Binance Futures `/fapi/v1/income` en lecture seule et récupère les commissions/funding réellement enregistrés. Ces deux niveaux doivent être comparés par `run_id` et période, pas additionnés aveuglément.

## P0/P1/P2 réalisés

### P0 — identité de session
Le wrapper `launch_test_master_base_v8_5_impact.sh` crée désormais un sidecar atomique par session :

```text
runs/<run_id>_session.json
```

Le sidecar déclare `engine`, `venue`, rôles, `schema_version`, `fee_model`, frais configurés, MD5 champion, horaires et noms des CSV. Le champion n'est pas modifié.

### P1 — scénarios du Duo
Le test hermétique `scripts/test_ace_duo_scenarios.py` valide sans réseau :

- Beta arrêté → `NO_NEW_ENTRIES`;
- Alpha arrêté → `NO_NEW_ENTRIES`;
- bus stale → `NO_NEW_ENTRIES`;
- ancien `run_id` → rejet;
- double mort → `STOP_NO_RELAUNCH`;
- deux jambes fraîches de la même session → `NORMAL`.

Résultat :

```text
ACE_DUO_SCENARIO_TESTS_OK
```

### P2 — schéma et audit
Le validateur `scripts/audit_ace_duo_readonly.py` confirme les schémas et filtre les lignes antérieures à la session. Le dernier run donne :

```text
Alpha : 9 fills · +2,00521 brut
Beta  : 13 fills · -0,73782 brut
Duo   : +1,26739 brut
Session alignée : oui
```

Tests :

```text
ACE_DUO_READONLY_TESTS_OK
```

## Validation intégrité

```text
bash -n wrappers : OK
Python compile   : OK
MD5 champion     : 14bcf868d46effba010cac577cbb004c
MD5 stable       : oui
ACE lancé        : non
Ordre envoyé     : non
```

## Reste à faire avant un run testnet

1. Vérifier que le sidecar est effectivement créé par le chemin de lancement choisi, car cette vérification n'a pas exécuté le wrapper.
2. Comparer un run réel futur avec `/fapi/v1/income` pour certifier commissions et funding.
3. Tester le watchdog réel sur une session courte et explicitement autorisée, sans relance automatique au premier essai.
4. Ne pas utiliser les CSV historiques cumulés comme métrique de performance nette.

## Verdict final

```text
Séparation Alpha/Beta : confirmée
Séparation ACE/Hulk  : confirmée
P0 identité session   : implémenté côté wrapper
P1 scénarios duo     : testé hermétiquement
P2 métadonnées       : implémenté côté wrapper/rapport
Dernier run ACE      : terminé proprement
PnL net historique   : non certifié sans réconciliation Binance
ACE LIVE             : interdit
ACE testnet          : possible après pré-vol humain contrôlé
Hulk PAPER           : séparé, observation indépendante
```

Aucune modification de stratégie, du champion genesis, des positions ou des paramètres de trading n'a été effectuée.
