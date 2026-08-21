# Mémoire collaborative — ce qu'on touche

**Hygiene swarm :** chaque ajout / modif / décision traçable = **1 ligne ici**.  
Pour que Cursor · Punk · Cortana · Christophe sachent **ce qui a bougé**, sans fouiller le chat.

| Colonne | Sens |
|---------|------|
| 2026-08-21T1710Z | Buffy | ★ | strategie/AUTO_REPARER_ACTIF (marqueur GO) | **AUTO-RÉPARATION NIVEAU 2 PASSÉE EN ACTIF (GO Christophe 19:09)** : le marqueur `strategie/AUTO_REPARER_ACTIF` est posé → `auto_reparer.py` (hooké dans sante_index, 5 min) relance désormais réellement les plists de veille cassées (avant : dry-run depuis le 20/08). Garde-fous conservés : backoff 3 essais/24h, circuit-breaker CPU/RAM (load>6, swap>2Go), vérif hub strict, kill-switch, cooldown 10 min. Vérifié : est_actif()=True + sante_index 9/9 OK. Le superviseur.sh (niveau 1) reste le garde-fou principal — relances prouvées aujourd'hui (vigie 11:24, cockpit 13:06). Demain : rien à refaire. |
| 2026-08-21T1650Z | Buffy | ★ | surveiller_whales.py + thermo_quotidien_free.py + pont_onchain.py + couleur_regime.py | **RÉPARATION BALEINES / COULEUR RÉGIME (GO Christophe)** : le scan baleines était aveugle (50 premières tx de 6 blocs ≈1,3% + seuil ≥1000 BTC en une tx → 0 détection depuis le 14/08) → whaleDir toujours neutral → couleur figée ORANGE. Fix : (1) surveiller_whales.py scanne désormais les adresses surveillées directement (4 appels API, filtre récence 48h) ; (2) thermo_quotidien_free.py stocke la direction des prints (whaleBuyUsd/whaleSellUsd/whaleDirProxy via champ m aggTrades) ; (3) pont_onchain.py combine scan+proxy dans whaleDir (whaleDirScan/whaleDirProxy/whaleDirLabel) ; (4) couleur_regime.py normalise inflow/outflow→bullish/bearish. Preuve : print 3,5M$ simulé (celui vu par Cortana 16:27Z) → couleur passe ORANGE→VERT. |
| 2026-08-20T1300Z | Buffy | + | Index_Maison/MEMOIRE_TRAGEDIE_OR_2026-08-20.md | mémoire : récit 2 demandes/2 réponses (tragédie→mine d'or), 8 leçons, sync Obsidian + GitHub |
| 2026-08-20T1326Z | Buffy | + | Index_Maison/APPLICATION_8_LECONS_2026-08-20.md | corrections 8 leçons appliquées : détecteur 120s, vigie dans sante_index (7/7), garde-fou filet BPS≥20, verrou md5 anti-patch-en-plein-run, superviseur-core rechargée |
| 2026-08-18T2104Z | Cortana | ~ | cockpit chat | coffre : sur la politique d'oubli (Google Gemini) |
| 2026-08-18T2104Z | Cortana | ~ | cockpit chat | coffre : politique d'oubli (Google Gemini) |
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
| 2026-08-21T2022Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2022Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2021Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2021Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2020Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2020Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2019Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2019Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2018Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2018Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2017Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2017Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2016Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2016Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2015Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2015Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2014Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2014Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2013Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2013Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2012Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2012Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2011Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2011Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2010Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2010Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2009Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2009Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2008Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2008Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2007Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2007Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2006Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2006Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2005Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2005Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2004Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2004Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2003Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2003Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2002Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2002Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2001Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2001Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2000Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2000Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1959Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1959Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1958Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1958Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1957Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1957Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1956Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1956Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1955Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1955Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1954Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1954Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1953Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1953Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1952Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1952Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1951Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1951Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1950Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1950Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1949Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1949Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1948Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1948Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1947Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1947Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1946Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1946Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1945Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1945Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1944Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1944Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1943Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1940Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1940Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1939Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1939Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1938Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1938Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1937Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1937Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1936Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T2045Z | Buffy | ★ | CSV_Binance + wallet | **VÉRITÉ RÉVÉLÉE : le CSV moteur est un mirage**. 1448 trades Binance vs 258 fills CSV (12% seulement). Le bot a PERDU -432$ aujourd'hui (realized -131$ + commission -301$). Wallet = 2130$. CSV réconcilié créé (runs/BINANCE_RECONCILED_20260821.csv). Script reconcilier_binance.py opérationnel. Positions fermées, wallet clean. Le moteur tel qu'il est structurellement perdant (partial fills + frais). **GO requis pour prochaine étape : fixer le moteur OU changer d'exchange.** |
| 2026-08-21T1950Z | Buffy | ★ | scripts/couleur_regime.py | **BOUCLE FERMÉE : 4 SOURCES BRANCHÉES DANS LA COULEUR RÉGIME** : (1) `direction_thermo()` lit `cockpit/mission.json` (alert=red, comboPnlNet → bearish si alert=red) ; (2) `direction_avis_ia()` lit `thermo/analyses/*.jsonl` (consensus LONG/SHORT des LLMs) ; (3) matrice enrichie : thermo bearish affaiblit VERT→ORANGE (le combo trading qui perd freine l'entrée) + avis IA divergent affaiblit aussi ; (4) record enrichi avec `avis_ia_dir/thermo_dir/detail_avis/detail_thermo`. Résultat réel : onchain=neutral | narratif=bullish (F&G 72) | avis_ia=bullish (4 LONG/2 SHORT) | thermo=bearish (alert=red, combo net=-344$) → ORANGE. 15 tests hermétiques OK. |
| 2026-08-21T1737Z | Buffy | ★ | detecter_cpfp.py + pont_onchain.py | **SETUP SNIFFER_VRAI appliqué (les 2 améliorations) :** (1) poussière NORMALISÉE par le régime de frais (seuil = max(2 sat/vB, minFee×1.5) — fini l'absolu qui confond accumulation et frais bas ; preuve : seuil 3.0 sat/vB avec minFee 2) ; (2) SCORE ONCHAIN UNIFIÉ dans pont_onchain.py : blocs privatisés ×0.5 + poussière ×0.3 + z-score ×0.2 → indiceOnchain 0-100 + label + composantes, injecté live.json.onchain (preuve : indice 6.5/100 FAIBLE). Validé : syntaxe OK, 9/9 chaînes OK, run trading intact, pépite active (7.1%, 11 lignes historique). |
| 2026-08-21T1726Z | Buffy | ★ | detecter_bloc_privatise.py + sante_index.py + plist bloc-privatise | **CORRECTIONS PÉPITE (lecture historique ENQUETE 20/08) :** (1) alerte pépite → double condition matrice Juge : taux ≥10% ET volume ≥500 BTC (j'avais mis taux seul, trop sensible) ; (2) résolution plist vérifiée = déjà 120s (OK, pas 600 comme l'enquête — déjà corrigé) ; (3) chaîne 9 MACRO TEMPÊTE ajoutée à sante_index (l'exogène existait : detecteur_macro_tempete.py + macro_tempete.json + radar_gate.rb, mais RIEN ne surveillait s'il meurt — leçon 8) → **9/9 chaînes OK**. Test réel : taux 7.1%/135 BTC → pas d'alerte (volume<500) = double condition OK. |
| 2026-08-21T1718Z | Buffy | ★ | detecter_bloc_privatise.py + detecter_cpfp.py + pont_onchain.py | **PÉPITE BRANCHÉE EN ACTIF (GO Christophe direct — famille mise de côté) :** (1) pépite blocs privatisés → mode ACTIF (défaut), alerte taux fantôme ≥10% (matrice Juge), historique append `bloc_privatise_hist.jsonl` (fini l'écrasement) ; (2) fix bugs détecteur CPFP : endpoint /v1/mempool/recent → 404 → /mempool/recent (dust=0 depuis 15/08) + pré-filtre 20× médiane → 1.5× (jamais de creusage, 817 runs à zéro en 6j) ; (3) les 2 en ACTIF, visibles live.json.onchain → carte ONCHAIN cockpit. Preuve : pépite détectait 0.12-62.5% fantômes sur 36 blocs (médiane 8.4%) depuis 15/08, personne ne regardait. RELEASE_RECEIPT_POUSSIERE_20260821.md écrit. |
| 2026-08-21T1655Z | Buffy | + | ~/Library/LaunchAgents/desactivees_briefs/ | DOC décision 19/08 : Christophe a demandé d'ARRÊTER les plists de briefs (journal-intention, brief-matin, analyste-cadence, brief-offres, propose-ameliorations, verif-predictions, discipline-quotidienne, cortana.horaire) car INUTILES tels que Cortana les produisait. journal-soir était dans le lot par erreur → RÉACTIVÉ le 21/08 (bootstrap OK, test manuel OK 16:53). README ajouté dans desactivees_briefs/. |
| 2026-08-21T1453Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1453Z | journal_auto | ★ | CONSOLE+Journal_2026-08-21 | Snapshot auto hygiène soir |
| 2026-08-21T1034Z | Buffy | ★ | Index_Maison/strategie/SPEC_REGIME_ENTREES_20260821.md | Consultation famille RÉGIME D'ENTRÉES : moteur trade 88.5% en COMPRESSÉ (edge brut quasi nul, NET -210$ sur 154 trades) → verdict JUGE GO-AVEC-RÉSERVES : gate HARD SKIP COMPRESSÉ + Expected_Alpha > frais×3 + trailing stop. Avis dans scripts/CONSULTATION_FAMILLE_REGIME_ENTREES_20260821/ |
| 2026-08-21T1230Z | Buffy | ★ | LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt (+ launcher v8_5) | ÉTAPE 1 REGIME GATE appliquée : HARD SKIP si tension < IRM_T_COMPRESSED (0.05) = régime COMPRESSÉ, bypass si force_tension_entry. Champion rescellé 64fb153f→14bcf868, CHAMPION_ACTIF maj (BAK conservé), IRM_REGIME_GATE=TRUE exporté BETA+ALPHA (défaut FALSE dans le code, activation par le launcher). Backup : .BAK_avant_gate_regime_20260821-123607. |
| 2026-08-21T0816Z | add | ★ | ~ | PATCH CHAMPION 64fb153f (sur 01c38510) — fix filet STOP_MARKET : (1) -4116 clientAlgoId unique par session (suffixe ACE_STOP_SESSION_ID horodaté) (2) -2021 retry à distance doublée (8->16->32->64 bps). C1 : backup .BAK_avant_patch_filet_* + manifest rescelé + CHAMPION_ACTIF=64fb153f + GO_USINE_NUAGE maj. Syntaxe bash OK + test logique retry OK. Réversible : cp .BAK_avant_patch_filet_20260821-100947 + restore manifest + CHAMPION_ACTIF=01c38510. |
| 2026-08-19T2116Z | session_debut | ★ | session | début mode=froid |
| 2026-08-18T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-18T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-18 | Snapshot auto hygiène soir |
| 2026-08-17T1853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-17T1853Z | journal_auto | ★ | CONSOLE+Journal_2026-08-17 | Snapshot auto hygiène soir |
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

## 17/08 — CONSULTATION SANTÉ DES INDEX (codeur + famille)

**Envoyé au codeur + aux 6 IA (clause permanente gravée)** — réponses dans `Index_Maison/scripts/` :
- `REPONSE_CODEUR_SANTE_INDEX_2026-08-17.md` : ⚠️ **le codeur (code.ia) a halluciné** — chemins inventés (data/scan_baleines.json, data/thermo.json…) incompatibles avec le vrai système. Les IDÉES étaient bonnes (alerte vocale, historique, panneau dépliable, seuil DÉGRADÉ) → appliquées par Buffy avec les chemins RÉELS.
- `CONSULTATION_FAMILLE_SANTE_INDEX_20260817/` : **6/6 avis, VERDICT UNANIME GO-AVEC-RÉSERVES (confiance 70-78%)**. Points retenus : escalade douce (log → orange → rouge → voix, pas de sur-alerte), historique pour distinguer panne transitoire/durable, seuils par chaîne.

**Appliqué à sante_index.py** (chemins réels, registre md5 mis à jour, veilleuse STABLE) :
1. Alerte vocale sur chaîne rouge (anti-empilement, MAINTENANCE_PREVUE respectée, kill-switch)
2. Historique append-only `data/alertes/sante_index.log` (chaque run, même OK)
3. État DÉGRADÉ (🟠 orange) entre vert et rouge — ralentissement sans crier

**Note canal** : `code.ia` renvoie 502 sur les gros payloads (fallback inferx mort) — réponse obtenue via `model: gemini` (352 s).

## 20/08 — AUDIT DES AUDITS (méta-analyse)
- `INDEX_AUDITS_ET_META_ANALYSE_2026-08-20.md` : **109 audits propres + 484 documents d'audit recensés** (71 AUDIT, 5 ENQUÊTE, 386 DIAG, 19 CHECKUP, 3 CONSTAT + 375 avis famille). Pattern dominant : **DÉGRADATION SILENCIEUSE** (mort sans alerte, garde-fou écrit ≠ actif, fausse sécurité, dérive externe). Famille consultée (codeur + 6 juges) : **Classe 3 fausse sécurité = la plus dangereuse**.
- Brique `veille_degradation.py` (codeur, corrigée Buffy : chemins + `True`) implémentée + plist 60 s chargée + chaîne 8 dans sante_index → **8/8 chaînes OK**.
- **ERREUR CORRIGÉE (Christophe)** : 1ʳᵉ consultation famille improvisée au lieu du canon `consulter_famille.py`+`famille.json` → re-consultation CANONIQUE : **UNANIME GO-AVEC-RÉSERVES (82-88%)**, exigence DMS externe + Fail-Fast + chaos test → `dms_veille.py` (plist 60 s, alertes + rapport cockpit) + fail-fast 5 plists dans `GO_VORTEX_V2.sh` + `--test-panne` (alerte prouvée par le feu) → tout testé, **8/8 chaînes OK**.
- `MEMOIRE_SUFFRANCE_EN_FORCE_2026-08-20.md` : analyse honnête (demande Christophe, strict) — les idées n'ont jamais été le problème, les erreurs sont dans la couche d'exécution ; verdict par objectif (stabilité/résilience atteignables, prédiction magique non) ; la bonne séquence résilience→stabilité→mesure→rentabilité ; plan famille (contester en entier) discuté, PAS exécuté. Sync Obsidian + GitHub.
