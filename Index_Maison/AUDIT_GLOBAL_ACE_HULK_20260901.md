# AUDIT GLOBAL ACE / HULK — 2026-09-01

## Périmètre
Audit approfondi, en lecture seule, de la séparation ACE Duo Alpha/Beta et Hulk : moteurs, CSV, états, bus duo, données de marché, frais et cockpit. Aucun moteur et aucun ordre n'a été relancé.

## Verdict corrigé
La séparation est globalement réelle et intentionnelle. Mon premier verdict était trop large : il assimilait l'état historique ACE `LIVE_COLOR` au statut Hulk. Ce n'est pas correct.

- **ACE Duo Alpha/Beta** : moteur Bash/genesis déterministe, Binance Futures testnet, deux rôles reliés par un bus duo.
- **Hulk** : moteur Python distinct, MEXC spot paper, états et CSV séparés.
- **Cockpit** : agrégateur qui affiche les deux familles; la séparation des sources existe, mais certains libellés historiques peuvent encore prêter à confusion.

## ACE Duo — séparation vérifiée

### Alpha
- Rôle : HUNTER.
- Taille historique de référence : environ 800 USDT.
- CSV principal : `runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`.
- Échantillon présent : 55 318 lignes, 1 751 lignes `FILLED/CLOSED`, PnL brut CSV additionné : environ +292,0142 USDT sur l'historique disponible.

### Beta
- Rôle : SCOUT.
- Taille historique de référence : environ 200 USDT.
- CSV principal : `runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`.
- Échantillon présent : 63 540 lignes, 5 969 lignes `FILLED/CLOSED`, PnL brut CSV additionné : environ +26,5628 USDT.

### Bus Duo
Le bus prévu est séparé des CSV :

```text
/tmp/ace777_ram_exchange/{duo_state,swarm_telemetry}.json
```

Dans le dépôt, les wrappers utilisent aussi `runs/duo_state.json`, `runs/duo_session.json` et `runs/swarm_telemetry.json` selon le profil. Les fichiers sont absents au moment de l'audit, ce qui est cohérent avec ACE arrêté; cela ne prouve pas une panne.

### Contrat Alpha/Beta
Le duo n'est pas deux moteurs indépendants sans coordination :

```text
BETA = SCOUT → publie état/événement
ALPHA = HUNTER → lit état, revenge/handover selon TTL et règles
```

Les historiques montrent que les problèmes anciens étaient surtout des problèmes de coordination et de supervision : `stale_state`, `duo_wait`, mort d'une jambe, faux positif watchdog et relance sans resynchronisation. Ces problèmes ont fait l'objet de corrections de wrappers et d'instrumentation, sans modification du champion genesis dans les correctifs documentés.

## Ce qui est réellement partagé avec Hulk
Hulk ne consomme pas directement les CSV Alpha/Beta pour ses décisions. Il possède ses propres modules locaux :

```text
hulk-mexc/scripts/ace_sense_mexc.py
hulk-mexc/scripts/veille_gates.py
```

Il reprend des concepts ACE : carnet, tension, murs, régimes et gates. C'est une réutilisation conceptuelle et partiellement logicielle, pas un partage de portefeuille ou de flux de fills.

## Frais
### ACE / Binance
`Index_Maison/scripts/fees_platforme.py` interroge Binance Futures `/fapi/v1/income` et agrège `COMMISSION`, `REALIZED_PNL` et `FUNDING_FEE`. Le modèle de frais Binance apparaît aussi dans l'historique champion sous forme de `FEE_ROUND_TRIP_BPS` et de colonnes `feeUsdt`/`pnlNet` dans certaines versions.

### Hulk / MEXC
Hulk ne lit pas les frais Binance pour ses décisions. Son feed estime actuellement MEXC à 0,05 % par opération et soustrait cette estimation du PnL brut dans `pnlNetEstimated`. Cette séparation est correcte conceptuellement, mais ce n'est pas une preuve de coût MEXC réel.

## Données et CSV
- ACE Alpha/Beta utilisent un schéma historique de type `ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,...`.
- Hulk utilise un autre schéma paper (`pair,event,regime,price,entry,qty,pnl_usdt,...`).
- Les données de prix ne sont pas les mêmes : Binance Futures pour ACE, MEXC spot pour Hulk.
- Il ne faut donc pas réconcilier ou additionner les CSV comme s'ils provenaient d'un même moteur.

## Problématiques ACE encore ouvertes
1. **CSV** : le schéma est exploitable mais plusieurs générations historiques coexistent; il faut identifier `schema_version`, venue, rôle, run_id et fee model dans les métadonnées plutôt que par le nom du fichier.
2. **Données correctes** : les anciens incidents montrent des états stale et des pertes de preuve lorsqu'un raw log était effacé; l'instrumentation actuelle réduit le risque mais la preuve doit rester append-only.
3. **Frais Binance** : la collecte existe, mais le PnL historique n'est pas uniformément net selon toutes les générations de CSV. Les colonnes doivent être vérifiées avant toute comparaison.
4. **Duo Alpha/Beta** : le design est cohérent, mais le bus doit être contrôlé par session/run_id pour éviter de lire un état d'une ancienne session.
5. **Relance** : les corrections de wrapper documentent le reset d'harmonie et l'arrêt sur double mort; elles doivent rester testées sans modifier le champion.

## Problématiques Hulk encore ouvertes
1. PnL paper Hulk négatif sur l'état observé; échantillon courant trop court pour conclure.
2. Frais/slippage MEXC estimés, pas exécutés dans le moteur paper.
3. Bags/DCA nécessitent un test de perte cumulée bornée.
4. Les `SKIP` doivent rester catégorisés par motif pour distinguer données, risque et stratégie.

## Cockpit
Le cockpit peut agréger ACE et Hulk, ce qui est légitime. Le défaut n'est pas l'absence de séparation des fichiers, mais le risque de présentation :

- `ACE / Binance / Alpha / Beta` doit être identifié comme un bloc.
- `Hulk / MEXC / Paper` doit être un autre bloc.
- Le statut ACE `OFF` ne doit pas être présenté comme le statut Hulk.
- Les frais Binance réels et les frais MEXC estimés doivent porter des libellés distincts.

## Tests déjà vérifiés
- Compilation ciblée des scripts critiques : OK.
- SELL FULL : 4/4 OK.
- Reprise Hulk : 16/16 OK.
- Aspiration fraîche au dernier contrôle : environ 24 secondes.
- Invariants portefeuille Hulk : valides.

La compilation complète reste polluée par un script historique incomplet :

```text
Index_Maison/scripts/PROD_SUPERVISEUR_GEMINI.py — unexpected EOF
```

Ce fichier n'est pas dans le chemin critique ACE Duo/Hulk et n'a pas été modifié.

## Verdict final

```text
Séparation ACE Alpha/Beta ↔ Hulk : OUI, architecture confirmée.
ACE Duo : cohérent mais nécessite validation dédiée des CSV, états de session et frais.
Hulk PAPER : utilisable en observation sous réserves.
ACE LIVE : non recommandé sans résoudre les problématiques CSV/données/frais et sans nouveau run de preuve.
Hulk LIVE : NO-GO.
Kelly/Cortana automatique : interdits.
```

## Ordre recommandé
1. Ne pas toucher au champion genesis.
2. Auditer/normaliser les métadonnées CSV ACE Alpha/Beta.
3. Vérifier un run ACE Duo complet avec `run_id`, état Alpha/Beta et frais Binance réconciliés.
4. Corriger uniquement l'affichage cockpit si nécessaire pour rendre les venues et rôles impossibles à confondre.
5. Continuer Hulk en PAPER séparément; ne jamais utiliser son PnL comme preuve ACE.
