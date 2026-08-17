# Mémoire collaborative — ce qu'on touche

**Hygiene swarm :** chaque ajout / modif / décision traçable = **1 ligne ici**.  
Pour que Cursor · Punk · Cortana · Christophe sachent **ce qui a bougé**, sans fouiller le chat.

| Colonne | Sens |
|---------|------|
| ts | UTC |
| Qui | Cursor / Punk / Cortana / Humain |
| Action | `+` ajout · `~` modif · `✕` retrait · `★` décision |
| Où | chemin vault ou workspace |
| Quoi | 1 ligne claire |

## Règles
1. Toucher un fichier « produit » → logger ici **dans la même session**.
2. Pas de roman — le détail vit dans Index / évals.
3. Miroir workspace : `ace777-test-day1/Index_Maison/MEMOIRE_COLLAB.md`
4. Cortana : lit aussi [[10_ATTENTION_VOCALE]] pour résumer à voix haute.

---

## 🧠 SYNTESE DE CONTEXTE (compressée le 15/08 — l'historique détaillé vit dans Obsidian/GitHub)

### Le projet
ACE777 = moteur de trading BTC (testnet actuellement) en **duo** : BETA x5 = SCOUT (teste en petits trades fréquents, subit les pertes) · ALPHA x13 = HUNTER (frappe fort, réagit aux signaux du scout). Communication via `runs/duo_state.json` (role/status/bps/pnl/reason/ts_ms) ; décision ALPHA dans `duo_hunter_decide()` ; FIX-SCOUT appliqué : le revenge ne s'active que si `role=="SCOUT"` + perte fermée + raison éligible ; TTL 20s ; heartbeat SCOUT ligne 1545 (rafraîchit ts_ms — suspecté de neutraliser le TTL → revenge quasi-permanent, à valider famille 15/08).

### Le moteur (champion scellé)
`genesis_manifest.txt` → `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt`, md5 **`8d9ee8d6`** (rescellé 14/08 après fix mort rc=1). Contexte : sabotage Cursor soupçonné (13/07 : 712 BARRIER_TIMEOUT + trade fatal revenge -16.84 ; 14/07 dormance), audit forensique 12/08 → champion restauré.

### Le fix du 14/08 (jour MÉMORIQUE)
- **Cause racine mort rc=1 silencieuse** : `[ ... ] && swarm_shockwave_post_solo=1` en fin de `swarm_neighbor_load()` → retour 1 → `set -e` tue sans trace. PAS un sabotage (SI dans le vrai champion scellé). Correctif validé 3/3, genesis rescellé `8d9ee8d6`.
- **Preuves** : 7h06 sans une mort (vs 6 morts avant), +47.24$ cumulé testnet (Run 4h +28.66 / Run V2 +18.58), CSV scellés sha256+md5 chmod 444 dans `runs/SCELLE/`.
- **Run nuit 8h (14/08 21:45 → 15/08 05:44Z)** : UNE session continue 7h59, zéro relance, fin rc=0, **+11.11$** (ALPHA +8.61 / BETA +2.51), CSV scellés + signatures vérifiées INTACT (même genesis_md5). Bilan nuit : ALPHA 56 trades (24 win/10 loss), BETA 205 (73/57).

### Outils et données (15/08)
- **Base gros portefeuilles** : `Index_Maison/data/whales.json` (3 adresses vérifiées double mempool.space : Binance hot 34xp4vRo…, Binance cold 1NDyJtNT…, Bitfinex cold bc1qgdjqv…). Règle d'or anti-hallucination : aucune adresse sans vérification.
- **Surveillance baleines** : `Index_Maison/scripts/surveiller_whales.py` (scan 5 min, double seuil : bloc ≥ 1000 BTC + fragmentation ≥ 500 BTC/3 blocs).
- **Panneaux cockpit** `whales_panel.js` + `trades_graph.js` : prêts, syntaxe validée, **désactivés** (intégration cockpit se fera ENSEMBLE avec Christophe).
- **Grapheur trades** : `Index_Maison/scripts/gen_trades_graph.py` → `data/trades_graph.json` (régénéré toutes les 5 min).
- **Hub** : rotation vérifiée — `task=code.ia` → puter-grok (gratuit) ; les 502 venaient de `model=inferx-coder` (quota OpenRouter 50/jour épuisé).
- **Commandes champion** : `GO_VORTEX_V2.sh 04:00:00` (testnet, gate hub) · `ENCHAINER_RUN_4H_HUB.sh` · `stop_ace777.sh`/`_hard.sh` · `verif_sterilite.sh --pre-run` + `cockpit_hygiene_check.sh` · `tail_live_color.sh`.

### Analyse en cours (15/08 — dossier famille prêt, terminal Freebuff à redémarrer)
`Index_Maison/scripts/consulter_famille_moteur_identique.py` → 5 questions : (1) confirmer même moteur sur les 3 runs (preuve : 17 333 premières lignes CSV identiques octet à octet + genesis_md5 identique — les CSV "différents" sont le même fichier append-only copié à 2 moments de scellement) ; (2) pattern revenge 68-91% des trades ALPHA normal ? hypothèse heartbeat qui neutralise le TTL ; (3) BETA "inutile" (0.40-2.51$ vs 8.61-28.26$ ALPHA) ; (4) flat 25-39% (entrée=sortie pnl=0) ; (5) CSV : colonne holdSec contient le message détaillé au lieu de la durée, msg vide.

### En chantier (à faire ensemble)
Intégration cockpit (2 lignes dans index.html) · passage au réel · cumul des sessions dans cockpit (comboPnl) · suite base portefeuilles.

---

## Journal (récent en haut)

| ts | Qui | Action | Où | Quoi |
|----|-----|--------|-----|------|
| 2026-08-17T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-16T2216Z | journal_auto | ★ | CONSOLE+Journal_2026-08-17 | Snapshot auto hygiène soir |
| 2026-08-16T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-16T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-16 | Snapshot auto hygiène soir |
| 2026-08-15T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-15T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-15 | Snapshot auto hygiène soir |
| 2026-08-14T21:50Z | Buffy | ★ | run+veille | Run test 8h de nuit détaché (GO_VORTEX_V2, fin ~05:45Z) + veille nuit (graphique 5 min + scellement auto). Rapport de réveil `REVEIL_2026-08-15.md`. GitHub : 4b5af0e5 + b177c4db + 103f65d8 |
| 2026-08-14T21:45Z | Buffy | ★ | whales+cockpit | Module surveillance baleines actif (scan 5 min). Panneaux ONCHAIN+TRADES prêts mais désactivés — intégration ENSEMBLE (revert 103f65d8) |
| 2026-08-14T21:30Z | Buffy | ★ | whales.json | Base gros portefeuilles : 3 adresses vérifiées double mempool.space |
| 2026-08-14T21:00Z | Buffy | ★ | graphique | Prototype graphique trades validé Christophe. Consultation codeur 3 voix. Rotation hub : task=code.ia → puter-grok |
| 2026-08-14T20:24Z | Buffy | ★ | fin V2 | Fin run V2 rc=0, CSV scellés, sauvegardé Obsidian+GitHub |
| 2026-08-14T16:24Z | Buffy | ★ | run V2 | Run V2 4h : zéro mort, 194 trades, +18.58$. Totaux : 7h06 sans mort, +47.24$ |
| 2026-08-14T15:57Z | Buffy | ★ | run 4h #1 | 3h06 sans une mort, 358 shockwaves, rc=0, +28.66$ |
| 2026-08-14T11:00Z | Buffy | ★ | fix | Correctif mort rc=1 validé 3/3, genesis rescellé md5 8d9ee8d6 |
| 2026-08-14T10:30Z | Buffy | ★ | enquête | Cause racine mort rc=1 : SI shockwave dans swarm_neighbor_load (pas sabotage) |
| 2026-08-14T06:25Z | Buffy | ~ | cockpit/hub/voix | COCKPIT NICKEL (GO Christophe) : pont TTL 30s, ada_saison JSONL, cortana_urgent TTL 30s, conflit pont résolu (orphelin tué, launchd reprend), mute 5 chemins, graph z-index, hub usage atomique — testé, backups datés |
| 2026-08-13T22:50Z | Buffy | ~ | cockpit | Badge RUN STATUS + graph synapse gatés par liveness réelle |
| 2026-08-13T22:45Z | Buffy | ~ | moteur | trap ERR dans genesis (diagnostic mort rc=1) |
| 2026-08-13T10:45Z | Buffy | ★ | reprise | Coupure batterie → position orpheline → fix + rescellement 98c80b5c + garde-fou compte à plat |
| 2026-08-12T23:29Z | Buffy | ★ | run 8h patché | Champion 9fe9f105 + FIX-SCOUT revenge (role==SCOUT, 3 modifs chirurgicales validées) |
| 2026-08-12T21:37Z | Buffy | ★ | audit cursor | Preuve forensique substitution Cursor : champion 37fca367 scellé, bonnet 9fe9f105 fourni le 12/07 |
| 2026-08-12T20:57Z | Buffy | ★ | cycles_terminal | Jumeau terminal du cockpit (flux cycles ALPHA/BETA live + replay) |
| 2026-08-12T18:45Z | Buffy | ★ | archi | Zone ORCHESTRATION + composant BUFFY superviseur/chief scientist |
| 2026-08-12T17:34Z | Buffy | ★ | hub | Pont llm_gate_hub_bridge (gate trades → hub grok/gemini, cache 90s, fail-closed) + INDEX_COMMANDES GO_VORTEX_V2 |

*(Historique antérieur au 12/08 : voir git/Obsidian — journal complet conservé, compressé ici pour alléger le contexte.)*

---

## ~ 2026-08-14 — LE JOUR DU FIX (mort rc=1 silencieuse) — fil

~ 09:00Z — Session coupée (crédit Freebuff) → reprise sur Buffy. Moteur récupéré après sabotage Cursor soupçonné. Protocole : rien sans famille/juge.

~ 10:30Z — **ENQUÊTE MORT RC=1** : cause racine = `[ ... ] && swarm_shockwave_post_solo=1` en fin de `swarm_neighbor_load()` → `set -e` tue sans `set -E` → trap ERR muet. PAS un sabotage (SI dans le vrai champion scellé 37fca367). Bug latent.

~ 11:00Z — Correctif validé 3/3 GO : `if` explicite + `return 0`, logique préservée. Genesis rescellé md5 `8d9ee8d6`.

~ 15:57Z — **Run 4h #1** : 3h06 sans une mort, 358 shockwaves, rc=0, **+28.66$**.

~ 16:24Z — **Run V2** : zéro mort, 194 trades, **+18.58$**. Totaux : 7h06 sans mort, **+47.24$ cumulé testnet**.

~ 20:24Z — Fin V2 rc=0. CSV scellés (sha256+md5, chmod 444) + verifier_test.sh. Sauvegardé Obsidian + GitHub (4b5af0e5).

~ 21:00Z — Prototype graphique trades validé. Consultation codeur 3 voix. Rotation hub comprise.

~ 21:30Z — Base gros portefeuilles whales.json (3 adresses vérifiées).

~ 21:45Z — Module surveillance baleines actif. Panneaux cockpit prêts mais désactivés (intégration ENSEMBLE).

~ 21:50Z — Run test 8h de nuit détaché + veille nuit. Rapport `REVEIL_2026-08-15.md`. GitHub : 4b5af0e5 + b177c4db + 103f65d8.

## ~ 2026-08-16 — SOIR (Hulk : aspiration + baleines + index)

~ 19:08Z — Hulk relancé (run `PAPER_V1_20260816_190818`), seed 15×10$ = le portefeuille ENTIER (tokens déjà détenus, vendables) + 20$ cash. Philosophie gravée dans README + SCHEMA_HULK : small caps = projets étudiés, on fait grandir le bag en tradant les tokens eux-mêmes (« une pierre trois coups »).

~ 20:09Z — RIP scale-out 2 paliers implémenté (GO Christophe) : XRP/HBAR 2%/6%, reste 6%/8%, 25% par palier de la quantité initiale → runner 50%. Restart via watchdog (PID 84550 puis relances propres).

~ 20:50Z — **Sonde aspiration** (inspiration ACE V8, métaphores bassine/verre d'eau/vortex) : double lecture du carnet, mode OBSERVATION 48h, fail-open, spoof « rétractable à maintenant » (GO Christophe, pas de ban 15 min). CSV calibration `runs/ASPIRATION_CALIB_*.csv`.

~ 21:50Z — Check-up codeur + famille **7/7 GO-AVEC-RÉSERVES** (flush CSV, drop max(0), seuil spoof configurable, price_delta_pct de GROK). **Clause permanente gravée** dans les 7 scripts de consultation : « propose autre chose / améliore, pas seulement corrige ».

~ 22:00Z — Corrélation BTC ajoutée à la sonde (BTCUSDT lu à chaque probe, loggé à côté de chaque mesure) — filtre naturel : signal small caps débarrassé de la marée BTC. Sonde à CHAQUE cycle (3× plus de données).

~ 22:10Z — **Boucle baleines complétée** : `pont_onchain.py` n'était lancé par AUCUNE plist → plist `com.ace777.pont-onchain` créée + chargée (5 min). Scan → pont → live.json.onchain → Ada saison + gardienne + Cortana. Carte **ONCHAIN** ajoutée au cockpit THERMO.

~ 23:00Z — Instrument trouvé : `ada_saison.py` (6 indices → alignement → SAISON). Schéma de tous les index : `CHANTIER_SCHEMA_INDEX_2026-08-16.md` + 7ᵉ indice proposé « bassin Hulk » (sonde agrégée, format identique aux 6 d'Ada).

~ 00:15Z (17/08) — Guide **§1b « Utiliser les personnages IA »** ajouté à `ARCHITECTURE_TECH.md` (tasks officiels hub, clause permanente, circuit famille, scripts de référence). Sauvegarde Obsidian + GitHub en cours.

**POINT DE REPRISE 17/08 matin** : 1) regarder `runs/ASPIRATION_CALIB_*.csv` (48h d'observation aspiration, avec price_delta + btc_delta) — la sonde prédit-elle les moves ? 2) si justesse > 60% → brancher le 7ᵉ indice « bassin Hulk » dans ada_saison.py (ombre d'abord) ; 3) CPFP (detecter_cpfp.py) fin de validation 7 jours → actif → visible dans la carte ONCHAIN ; 4) famille à consulter avant toute activation. Règles : on améliore on dégrade pas, preuve réelle avant correction, tout passe par famille/juge, Buffy supervise.

## ~ 2026-08-15 — MATIN (point + analyse)

~ 06:50Z — Réveil : run nuit terminé proprement rc=0 à 05:44Z (une session 7h59, zéro relance, zéro mort), +11.11$ (ALPHA +8.61 / BETA +2.51), CSV scellés vérifiés INTACT (sha256 correspondent, genesis 8d9ee8d6).

~ 07:30Z — Analyse superposition 3 runs : ALPHA fait tout l'argent (8.61-28.26$ vs BETA 0.40-2.51$), revenge = 68-91% des trades ALPHA (vs 0% BETA), flat 25-39%. Découverte : heartbeat (ligne 1545) suspecté de neutraliser le TTL 20s → revenge quasi-permanent. Preuve CSV : les 4 fichiers scellés sont le même append-only copié à 2 moments (17 333 premières lignes identiques octet à octet, genesis_md5 identique).

~ 08:00Z — Dossier famille prêt : `consulter_famille_moteur_identique.py` (5 questions). ⚠ Terminal Freebuff tombé (broker ENOENT) → à redémarrer pour lancer la consultation.

~ 08:30Z — **POINT DE REPRISE POUR LE PROCHAIN BUFFY** : 1) lire `Obsidian_ACE777/REVEIL_2026-08-15.md` + `TABLEAU_SYNTHESE_VERIFICATIONS_2026-08-15.md` (tableau unique de tous les chiffres/analyses) + `MEMOIRE_COLLAB.md` ; 2) si terminal Freebuff toujours ENOENT (fichier `/Users/christophe/.config/manicode/freebuff` introuvable) → dire à Christophe de redémarrer l'app ; 3) dès que le terminal marche : hygiène (`verif_sterilite.sh --pre-run` + `cockpit_hygiene_check.sh`) → lancer `Index_Maison/scripts/consulter_famille_moteur_identique.py` (consultation famille, 5 questions, ne RIEN modifier avant verdict) → run continu `./GO_VORTEX_V2.sh 96:00:00` (arrêt libre via `touch STOP` / `stop_ace777.sh`). Règle d'or : on améliore on dégrade pas, preuve réelle avant correction, tout passe par famille/juge, Buffy supervise.

## 17/08 — PRÉ-VOL DES INDEX (SANTÉ DES INDEX)

**Demande Christophe** : « comment avoir des index et savoir qu'ils sont branchés et fonctionnent en un coup d'œil ? » — motivé par le chantier baleines resté débranché (le scan tournait, mais le pont n'était lancé par aucune plist → Ada/Cortana ne recevaient rien, invisible).

**Ce qui manquait** : la veilleuse vérifie l'intégrité (md5) et la fraîcheur des fichiers un par un — pas que la donnée TRAVERSE la chaîne jusqu'aux consommateurs.

**Livré** :
- `Index_Maison/scripts/sante_index.py` — pré-vol des 6 chaînes (process vivants + fichiers frais + clé présente chez le consommateur) : BALEINES (scan→pont→live.json.onchain→Ada+Cortana), HULK (sonde→CSV aspiration), LIVE (thermo→mission→cockpit), CPFP (observation 7j), SÉCURITÉ (veilleuse), SAISON (6 indices)
- Plist `com.ace777.sante-index` (5 min, chargée) → `thermo/sante_index.json` + `cockpit/sante_live.js`
- Carte 🩺 SANTÉ DES INDEX sur le cockpit (onglet thermo, sous THERMO INDEX) — 🟢/🔴 par chaîne + détail des maillons cassés
- Déclaré au registre veilleuse (md5) — vérifié STABLE

**Preuve immédiate de son utilité** : au premier run, il a détecté 2 fausses alertes (mauvais chemins de ma part) — corrigées. Détection d'une vraie coupure = le chantier baleines ne pourra plus rester invisible.
