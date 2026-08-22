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
| 2026-08-22T1211Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1210Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1209Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1208Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1207Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1206Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1205Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1204Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1203Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1202Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1201Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1200Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1159Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1158Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1157Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1156Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1155Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1154Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1153Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1152Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1151Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1150Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1149Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1148Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1147Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1146Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1145Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1144Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1143Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1142Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1141Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1140Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1139Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1138Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1137Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1136Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1135Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1134Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1133Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1132Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1131Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1130Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1129Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1128Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1127Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1126Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1125Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1124Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1123Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1122Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1121Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1120Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1119Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1118Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1117Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1116Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1115Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1114Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1113Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1112Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1111Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1110Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1109Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1108Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1107Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1106Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1105Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1104Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1103Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1102Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1101Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1100Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1059Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1058Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1057Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1056Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1055Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1054Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1053Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1052Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1051Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1050Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1049Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1048Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1047Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1046Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1045Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1044Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1043Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1042Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1041Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1040Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1039Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1038Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1037Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1036Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1035Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1034Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1033Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1032Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1031Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1030Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1029Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1028Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1027Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1026Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1025Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1024Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1023Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1022Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1021Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1020Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1019Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1018Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1017Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1016Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1015Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1014Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1013Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1012Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1011Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1010Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1009Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1008Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1007Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1006Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1005Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1004Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1003Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1002Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1001Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T1000Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0959Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0958Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0957Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0956Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0955Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0954Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0953Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0952Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0951Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0950Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0949Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0948Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0947Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0946Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0945Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0944Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0943Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0942Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0941Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0940Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0939Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0938Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0937Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0936Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0935Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0934Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0933Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0932Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0931Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0930Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0929Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0928Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0927Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0926Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0925Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0924Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0923Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0922Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0921Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0920Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0919Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0918Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0917Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0916Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0915Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0914Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0913Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0912Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0911Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0910Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0909Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0908Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0907Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0906Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0905Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0904Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0903Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0902Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0901Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0900Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0859Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0858Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0857Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0856Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0855Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0854Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0853Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0852Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0851Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0850Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0849Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0848Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0847Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0846Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0845Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0844Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0843Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0842Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0841Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0840Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0839Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0838Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0837Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0836Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0835Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0834Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0833Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0832Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0831Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0830Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0829Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0828Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0827Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0826Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0825Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0824Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0823Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0822Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0821Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0820Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0819Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0818Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0817Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0816Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0815Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0814Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0813Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0812Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0811Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0810Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0809Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0808Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0807Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0806Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0805Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0804Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0803Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0802Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0801Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0800Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0759Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0758Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0757Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0756Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0755Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0754Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0753Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0752Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0751Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0750Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0749Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0748Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0747Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0746Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0745Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0744Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0743Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0742Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0741Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0740Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0739Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0738Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0737Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0736Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0735Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0734Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0733Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0732Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0731Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0730Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0729Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0728Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0727Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0726Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0725Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0724Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0723Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0722Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0721Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0720Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0719Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0718Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0717Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0716Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0715Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0714Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0713Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0712Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0711Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0710Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0709Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0708Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0707Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0706Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0705Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0704Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0703Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0702Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0701Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0700Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0659Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0658Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0657Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0656Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0655Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0654Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0653Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0652Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0651Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0650Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0649Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0648Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0647Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0646Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0645Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0644Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0643Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0642Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0641Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0640Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0639Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0638Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0637Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0636Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0635Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0634Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0633Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0632Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0631Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0630Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0629Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0628Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0627Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0626Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0625Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0624Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0623Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0622Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0621Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0620Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0619Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0618Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0617Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0616Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0615Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0614Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0613Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0612Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0611Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0610Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0609Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0608Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0607Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0606Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0605Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0604Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0603Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0602Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0601Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0600Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0559Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0558Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0557Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0556Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0555Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0554Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0553Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0552Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0551Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0550Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0549Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0548Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0547Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0546Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0545Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0544Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0543Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0542Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0541Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0540Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0539Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0538Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0537Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0536Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0535Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0534Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0533Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0532Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0531Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0530Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0529Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0528Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0527Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0526Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0525Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0524Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0523Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0522Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0521Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0520Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0519Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0518Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0517Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0516Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0515Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0514Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0513Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0512Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0511Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0510Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0509Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0508Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0507Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0506Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0505Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0504Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0503Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0502Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0501Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0500Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0459Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0458Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0457Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0456Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0455Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0454Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0453Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0452Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0451Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0450Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0449Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0448Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0447Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0446Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0445Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0444Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0443Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0442Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0441Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0440Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0439Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0438Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0437Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0436Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0435Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0434Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0433Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0432Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0431Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0430Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0429Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0428Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0427Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0426Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0425Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0424Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0423Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0422Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0421Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0420Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0419Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0418Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0417Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0416Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0415Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0414Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0413Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0412Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0411Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0410Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0409Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0408Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0407Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0406Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0405Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0404Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0403Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0402Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0401Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0400Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0359Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0358Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0357Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0356Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0355Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0354Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0353Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0352Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0351Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0350Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0349Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0348Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0347Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0346Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0345Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0344Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0343Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0342Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0341Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0340Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0339Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0338Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0337Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0336Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0335Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0334Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0333Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0332Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0331Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0330Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0329Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0328Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0327Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0326Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0325Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0324Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0323Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0322Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0321Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0320Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0319Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0318Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0317Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0316Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0315Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0314Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0313Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0312Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0311Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0310Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0309Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0308Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0307Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0306Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0305Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0304Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0303Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0302Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0301Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0300Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0259Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0258Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0257Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0256Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0255Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0254Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0253Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0252Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0251Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0250Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0249Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0248Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0247Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0246Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0245Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0244Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0243Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0242Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0241Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0240Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0239Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0238Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0237Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0236Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0235Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0234Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0233Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0232Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0231Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0230Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0229Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0228Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0227Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0226Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0225Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0224Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0223Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0222Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0221Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0220Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0219Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0218Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0217Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0216Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0215Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0214Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0213Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0212Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0211Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0210Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0209Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0208Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0207Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0206Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0205Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0204Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0203Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0202Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0201Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0200Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0159Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0158Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0157Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0156Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0155Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0154Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0153Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0152Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0151Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0150Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0149Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0148Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0147Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0146Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0145Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0144Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0143Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0142Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0141Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0140Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0139Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0138Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0137Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0136Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0135Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0134Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0133Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0132Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0131Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0130Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0129Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0128Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0127Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0126Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0125Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0124Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0123Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0122Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0121Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0120Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0119Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0118Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0117Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0116Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0115Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0114Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0113Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0112Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0111Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0110Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0109Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0108Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0107Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0106Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0105Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0104Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0103Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0102Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0101Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0100Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0059Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0058Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0057Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0056Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0055Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0054Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0053Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0052Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0051Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0050Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0049Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0048Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0047Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0046Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0045Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0044Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0043Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0042Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0041Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0040Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0039Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0038Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0037Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0036Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0035Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0034Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0033Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0032Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0031Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0030Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0029Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0028Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0027Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0026Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0025Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0024Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0023Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0022Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0021Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0020Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0019Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0018Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0017Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0016Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0015Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0014Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0013Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0012Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0011Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0010Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0009Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0008Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0007Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0006Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0005Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0004Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0003Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0002Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0001Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-22T0000Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2359Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2358Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2357Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2356Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2355Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2354Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2353Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2352Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2351Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2350Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2349Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2348Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2347Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2346Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2345Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2344Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2343Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2342Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2341Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2340Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2339Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2338Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2337Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2336Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2335Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2334Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2333Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2332Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2331Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2330Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2329Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2328Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2327Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2326Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2325Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2324Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2323Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2322Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2321Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2320Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2319Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2318Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2317Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2316Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2315Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2314Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2313Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2312Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2311Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2310Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2309Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2308Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2307Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2306Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2305Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2304Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2303Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2302Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2301Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2300Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2259Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2258Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2257Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2256Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2255Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2254Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2253Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2252Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2251Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2250Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2249Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2248Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2247Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2246Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2245Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2244Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2243Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2242Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2241Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2240Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2239Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2238Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2237Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2236Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2235Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2234Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2233Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2232Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2231Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2230Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2229Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2228Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2227Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2226Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2225Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2224Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2223Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2222Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2221Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2220Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2219Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2218Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2217Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2216Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2215Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2214Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2213Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2212Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2211Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2210Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2209Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2208Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2207Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2206Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2205Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2204Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2203Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2202Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2201Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2200Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2159Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2158Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2157Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2156Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2155Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2154Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2153Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2152Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2151Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2150Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2149Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2148Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2147Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2146Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2145Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2144Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2143Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2142Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2141Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2140Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2139Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2138Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2137Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2136Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2135Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2134Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2133Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2132Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2131Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2130Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2129Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2128Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2127Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2126Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2125Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2124Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2123Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2122Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2121Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2120Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2119Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2118Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2117Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2116Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2115Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2114Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2113Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2112Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2111Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2110Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2109Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2108Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2107Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2106Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2105Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2104Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2103Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2102Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2101Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2100Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2059Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2058Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2057Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2056Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2055Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2054Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2053Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2052Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2051Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2050Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2049Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2048Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2047Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2046Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2045Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2044Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2043Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2042Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2041Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2040Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2039Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2038Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2037Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2036Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2035Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2034Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2033Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2032Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2031Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2030Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2029Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2028Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2027Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2026Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2025Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2024Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2023Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2022Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2021Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2020Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2019Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2018Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2017Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2016Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2015Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2014Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2013Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2012Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2011Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2010Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2009Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2008Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2007Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2006Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2005Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2004Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2003Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2002Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2001Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T2000Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1959Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1958Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1957Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1956Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1955Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1954Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1953Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1952Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1951Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1950Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1949Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1948Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1947Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1946Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1945Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1944Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1943Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1940Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1939Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1938Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1937Z | journal_soir | ★ | journal | snapshot soir auto |
| 2026-08-21T1853Z | journal_soir | ★ | journal | snapshot soir auto |
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
