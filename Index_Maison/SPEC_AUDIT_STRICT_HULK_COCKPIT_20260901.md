# AUDIT STRICT HULK / COCKPIT — 2026-09-01

## Mandat
Auditer Hulk paper et son cockpit comme un organisme lié : remonter chaque modification à sa source, tracer producteurs/consommateurs, éviter les doublons, ne rien appliquer sans périmètre réversible. Demander un avis strict, des contestations et des améliorations concrètes.

## Faits vérifiés
- Moteur : `hulk-mexc/scripts/paper_diprip.py`, paper MEXC, boucle principale documentée à 20 s.
- Source aspiration active : `runs/aspiration_live.json` en mode `ASPIRATION_SRC=fichier`.
- Le satellite écrit ce JSON atomiquement ; le moteur le lit dans `probe_aspiration()`.
- Le moteur retombe actuellement sur la sonde inline si le JSON est absent ou stale (>45 s).
- Les circuits `cb_btc` et `cb_gex` sont contrôlés par `maybe_enter()` ; les sorties restent libres.
- Les gates existantes sont déjà séparées : `entry_gate()` dans `ace_sense_mexc.py`, `entry_gate_check()` dans `veille_gates.py`, puis contrôles dans `maybe_enter()` et `buy()`.
- Le moteur possède déjà des garde-fous : STOP_PAPER/STOP_ALL, veille stale, cooldown, lock anti-double-instance, sizing par profil/tier/mur, lot filter, persistance d’état.
- Le cockpit `index.html` affiche des lignes `portfolio` ou `positions` et les présente dans une section “bags”; il calcule aussi `totSeed`, `totPos`, `totCash` et `Hulk = bags + cash`.
- Le cockpit et le moteur n’ont pas exactement la même sémantique : le moteur distingue `pos`, `bags`, `pair_cash`; le cockpit peut présenter des positions comme “bags”.
- Les données historiques du cockpit contiennent des snapshots anciens ; ne pas les confondre avec la preuve du runtime actuel.

## Architecture source → sortie
1. MEXC / thermo / veille → données de marché et contexte.
2. `satellite_aspiration.py` → `hulk-mexc/runs/aspiration_live.json`.
3. `paper_diprip.py::probe_aspiration()` → `self.aspiration`, `btc_price`, circuit BTC ; fallback inline actuel si JSON stale.
4. `paper_diprip.py::maybe_enter()` → gates d’entrée et appel `buy()`.
5. `buy()` → `pos`, cash, CSV paper, state JSON.
6. `manage_open()` / `manage_bag()` → sorties, bags, cash, journal et state.
7. Feed cockpit → `mission.json`/`live.js`/`index.html`, lecture des états et visualisation.
8. `sante_index.py`, watchdog et veille → supervision/alertes, sans décision de trading directe selon le code audité.

## Risques à challenger
### R1 — Fallback aspiration ambigu
Le commentaire du moteur appelle le fallback inline “sûr”, mais une panne du producteur satellite peut alors augmenter les appels réseau exactement pendant la dégradation de la source. Il faut décider si le mode dégradé doit être :
- `NO_NEW_ENTRIES` mais gestion des positions autorisée ;
- fallback inline borné et explicitement observé ;
- ou maintien actuel pour paper uniquement.
Toute proposition doit préserver les sorties et ne pas ajouter de boucle parallèle.

### R2 — Freshness vs fraîcheur réelle
`sante_index.py` possède une référence monotone de timestamp aspiration, mais le moteur ne partage pas directement cet état. La famille doit proposer une façon sans doublon de faire respecter le contrat : réutiliser le validateur existant, module partagé, ou simple état moteur — sans créer deux mémoires concurrentes.

### R3 — Sémantique portefeuille/cockpit
Le moteur distingue `trade position`, `seed holding`, `house bag`, `cash`; l’UI affiche des “bags” depuis des lignes `portfolio`/`positions`. Risque de mauvaise interprétation opérateur. Proposer un contrat de schéma canonique, avec compatibilité rétroactive, sans recalculer le portefeuille dans plusieurs endroits.

### R4 — Accumulation de gates et doublons
Ne pas créer de nouvelle fonction `entry_gate`. Examiner si les contrôles doivent être instrumentés par motif plutôt que dupliqués. Les catégories souhaitées : DATA_QUALITY, CIRCUIT, REGIME, POSITION, LIQUIDITY/WALL, VOLUME, VEILLE, COOLDOWN, SIZING.

### R5 — Risque de preuve paper trompeuse
Le paper ne déduit pas nécessairement tous les frais, spread et slippage dans le PnL moteur. Le cockpit peut afficher un résultat qui n’est pas comparable à HOLD. Proposer une comptabilité séparée : brut, frais estimés, slippage estimé, net, benchmark HOLD, sans changer les décisions avant validation.

### R6 — EDEL/bags et absence de stop technique
Le traitement bag peut désactiver le stop technique et autoriser DCA/crash rules. Demander si le crash-stop est réellement indépendant, borné et testé ; ne pas accepter “bag” comme justification d’une perte non bornée.

### R7 — Persistance/reprise
L’état est atomique et resume existe, mais demander des invariants de reprise : aucune duplication de position, cash non créé, événements idempotents, seed non recréé après restart.

## Questions obligatoires à la famille
1. Avis strict global : PAPER GO, GO conditionnel ou NO-GO ? LIVE interdit-il toujours ?
2. Fallback : quelle politique fail-safe minimale est correcte et dans quel fichier doit-elle vivre ?
3. Comment aligner le cockpit sur le schéma moteur sans créer de second calcul de vérité ?
4. Quels invariants de risque et tests hermétiques sont prioritaires ?
5. Quelles améliorations sont nécessaires maintenant, lesquelles doivent rester en observation ?
6. Donner une coordination : fichiers autorisés/interdits, ordre, rollback, preuves et critères d’arrêt.

## Contraintes
- Aucun ordre réel, aucun live, aucune activation Kelly/Cortana automatique.
- Aucun changement de `defaults.env`, LaunchAgents, positions ou état runtime sans validation dédiée.
- Ne pas modifier `satellite_aspiration.py` et `paper_diprip.py` simultanément sans contrat de test.
- Ne pas remplacer les consommateurs historiques CSV sans preuve de dépendances.
- Ne pas créer de nouveau serveur, daemon, boucle ou source de vérité.
- Les propositions doivent distinguer correction de supervision, correction moteur, et correction UI.
