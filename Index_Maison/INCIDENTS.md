# INCIDENTS.md — journal RCA obligatoire (pratique des prop shops, GO C. 15/09)

> Règle : TOUT incident → 5 lignes AVANT de retoucher du code.
> (1) Ça a pété · (2) Pourquoi le radar ne l'a pas vu · (3) Le correctif exact ·
> (4) Le test qui l'aurait attrapé · (5) Cause racine (R1-R7, voir RECAP_ERREURS_SEMAINE_20260915.md).
> Blameless : on décrit le mécanisme, pas la personne. Une ligne par incident, la plus récente en haut.

## Causes racines de référence (audit semaine 36)

| Code | Cause |
|---|---|
| R1 | Nommage : organe ≠ stem de sa plist → grisaille fantôme |
| R2 | Silence des échecs : exception avalée, bug invisible pendant des semaines |
| R3 | « Corrigé » non propagé : fix écrit dans une fiche, jamais avalé par le bout |
| R4 | Dialecte non vérifié : décimal lu en hex, s vs ms, pagination oubliée |
| R5 | Seuil fixé au pif (60 s codé, 63 s réel) |
| R6 | Infra instable : hub mono-provider, réseau partagé, coupures |
| R7 | Erreur de l'agent : verdict ancien cité, sceau auto-réécrit |

## Journal

> **20/09/2026 — la journée « incassable auto-réparant »**. 11 incidents consignés, tous réparés à la source
> (aucun contournement, aucun ordre, 0 €). Fil rouge : **la boucle mesurait beaucoup et concluait peu** —
> sept faux verts, dont un grave : le drill de restauration répondait « ACE777 reviendrait » alors que
> 27 instruments exécutés par la boucle n'étaient pas dans git. Détail complet dans `thermo/REVUE_ORGANES.md`,
> `thermo/PROTOCOLES_VERDICTS.json` et `MEMOIRE_COLLAB.md` (20/09).

### 2026-09-20 — 27 instruments que la boucle EXÉCUTE hors git, sous un drill « READY »
1. Le drill de restauration répondait « oui, ACE777 reviendrait » alors que 27 scripts que la boucle exécute (le chien de garde lui-même, la page vol, la sentinelle indépendante, les moteurs croisements/paternes, `preuve_lecture`, `verifier_regles_or`, `installer_depuis_repo`…) n'étaient dans AUCUN commit.
2. Le radar le CALCULAIT (`non_suivis_critiques`) mais ne le comptait pas dans ses trous : un indicateur mesuré mais absent du verdict est un faux vert. Second angle mort : les appels écrits `"$REPO_DIR/…"` étaient mal extraits (le `$` cassait le motif) → `verifier_regles_or.py` et `installer_depuis_repo.sh` échappaient même au détecteur.
3. Nouvelle étape `etape_instruments()` (tout script invoqué par un agent launchd, par `git_push_auto.sh` ou importé localement doit être suivi par git, sinon TROU) ; 27 instruments + 5 fichiers de vérité indexés — dont `REGISTRE_ORGANES.json`, sans lequel le chien refuse de démarrer.
4. Le test : `drill_restauration.py` doit lister 0 instrument hors git — et DOIT passer TROU si on retire un fichier de git.
5. Cause racine **R2/R3** : le contrôle existait, la conclusion ne l'incluait pas ; et le correctif n'avait jamais été propagé du chien au reste de la boucle.

### 2026-09-20 — short BTC aveugle 5 h : la rotation détruisait l'historique récent
1. Le signal short BTC (CRITIQUE) a eu `score: null` pendant ~5 h : plist exit 0, produit frais, chien « short-btc vivant », veilleuse verte, bloc vide sur la page.
2. La rotation archivait TOUT puis vidait le fichier : à 13:12Z `croisement_contexte.jsonl` est tombé à 5 h d'historique alors que le signal en exige ≥ 10 h distinctes.
3. Fenêtre gardée 24 h + plafond 60 Mo, réécriture **en place** (même inode : les écrivains gardent leur fd) ; nouveau gardien **« vivant mais aveugle »** (`strategie/sens_declares.json`) + **cri vivant** (`thermo/cris.json`, auto-effacé).
4. Le test : simuler une rotation sur copie et vérifier que le signal garde toujours ≥ 10 h (6 cas testés hors vol, dont plafond et lignes sans ts).
5. Cause racine **R2 + R5** : la rotation gardait 0 h alors qu'un lecteur en attendait 10 ; personne ne mesurait la décision, seulement la fraîcheur.

### 2026-09-20 — La sauvegarde du coffre morte 2 jours, le script disait « à jour »
1. 55 fichiers du vault non sauvés depuis le 18/09 18:55 : `.git/index.lock` orphelin de 0 octet → tout `git add` échouait.
2. Le script avalait l'erreur (`2>/dev/null`) puis affichait « à jour » : panne totale, zéro bruit. Et le garde-fou qui rattrape exactement ce cas existait **depuis le 05/09 dans `git_push_auto.sh`** — jamais recopié dans `git_push_vault.sh` : la boucle était coupée en deux.
3. Garde-fou recopié (verrou mis de côté en `/tmp`, jamais supprimé) + plus aucune erreur avalée + sérialisation des passages ; le pouls n'est écrit que si le coffre est **prouvé** à jour.
4. Le test : poser un `index.lock` orphelin → le script doit sauver quand même et écrire un pouls daté.
5. Cause racine **R2 + R3** : silence des échecs et correctif non propagé d'un script à son jumeau.

### 2026-09-20 — RAM du heartbeat figée à 0 Mo (RAM_FREE ≠ ram_free)
1. Le heartbeat annonçait « 0 Mo de RAM libre » en permanence ; la valeur réelle était ~50 % (2 040 Mo).
2. Le producteur imprimait `RAM_FREE=` (majuscules), le lecteur lisait `$ram_free` (minuscules) → la variable restait à son 0 d'initiation. Personne ne lisait la valeur pour la contredire.
3. Corrigé à la source + garde numérique ; preuve après rechargement du daemon : heartbeat `ram_free_mb: 2040`.
4. Le test : comparer le heartbeat à `memory_pressure` (tolérance 20 %) à chaque cycle.
5. Cause racine **R4** : un nom qui ne correspond pas à son usage — 3ᵉ occurrence de cette famille dans la maison.

### 2026-09-20 — Cadence déclarée FAUSSE sur 22 organes (300 s par défaut)
1. 22 organes à déclencheur CALENDAIRE (journal-soir, veille-yt, verif-setup, suivi-setup-red…) portaient une cadence de 5 min dans le registre.
2. `generer_registre_organes.py` retombait sur `freq = 300` dès qu'il n'y avait pas de `StartInterval` : le défaut n'était pas mesuré, il était **inventé**. Inerte tant que l'organe n'a pas de produit — mais le jour où il en reçoit un, le seuil tombe à 600 s : faux positif permanent (R14) ou organe déclaré mort à tort.
3. Le générateur lit le VRAI déclencheur (intervalle, calendrier quotidien/hebdo/passages multiples, KeepAlive/WatchPaths/RunAtLoad = événementiel) et écrit les faits (`declencheur`, `cadence_plist_sec`) ; la vérité humaine (25 organes) reste prioritaire.
4. Le test : régénérer le registre et différencier avant/après (99 organes, 0 clé perdue, 0 commentaire modifié) — **18 cadences corrigées**.
5. Cause racine **R5** : seuil fixé au pif (60 s codé, 63 s réel — même famille que l'audit semaine 36).

### 2026-09-20 — suivi-setup-red jamais jugé sur son produit (glob lu comme un chemin littéral)
1. Un organe dont le produit est déclaré `hulk-mexc/runs/SUIVI_SETUP_*.jsonl` était classé « sans produit » et jugé sur sa seule sortie launchd : une panne de son produit était **invisible**.
2. Le résolveur ne traitait que le jeton `dernier:` puis ouvrait le reste comme un chemin littéral → le joker ne correspondait à rien.
3. `resoudre_chemin_produit` (une seule vérité, partagée avec la revue des organes) gère les jokers (fichier le plus récent, comme `dernier:`) ; la cadence réelle (quotidienne) a été alignée en même temps pour ne pas créer de faux positif.
4. Le test : la revue doit classer suivi-setup-red « OK » sur son produit (54 vivants, 0 hors délai).
5. Cause racine **R1 + R7** : on croyait l'organe surveillé parce qu'un ancien verdict le disait.

### 2026-09-20 — Deux organes morts cachés par un marquage « dormant »
1. `geopol` (figé depuis le 17/09) et `croisements-indices` (figé depuis le 18/09) : plists versionnés mais plus chargés. Le marquage « dormant » du 19/09 avait arrêté le faux positif du chien **en cachant un vrai mort**.
2. Un drapeau « dormant » posé sans date ni justification vaut un silence : personne ne revient jamais dessus.
3. Réinstallés + chargés, marquage retiré (`plutil -lint` OK).
4. Le test : le chien doit compter ces deux-là vivants, 0 grisaille, 0 dormant.
5. Cause racine **R1 + R3**.

### 2026-09-20 — Page vol : deux blocs jamais affichés et un gardien en faux vert permanent
1. « Chargement du shadow plancher… » et « Chargement du signal short BTC… » à vie ; et le gardien « Chien de garde » affichait un OK VERT quoi qu'il arrive.
2. (a) `plancher_live.js` est chargé AVANT la carte → `if(!b) return` : le bloc ne s'est jamais rempli depuis sa création ; (b) `chargerShortBtc` jamais attachée à `window` alors que le seul appel passait par `window.chargerShortBtc` → test toujours faux, en silence ; (c) le gardien lisait `thermo/chien_rapport.txt`, **un fichier que PERSONNE n'écrit** (`tail` échoue, subprocess ne lève rien → stdout vide).
3. Le rendu attend le DOM ; l'export + le chargement au boot sont ajoutés ; le gardien lit `CHIEN_RAPPORT.json` et un rapport figé > 15 min devient rouge.
4. Le test : rendu hors navigateur avec DOM simulé (les deux ordres d'exécution remplissent le bloc) ; page vol : **0 échec**.
5. Cause racine **R2** : trois silences qui se cumulaient — une page qui rassure à tort endort la boucle entière.

### 2026-09-20 — TROUPEAU-INV : un protocole qui ne pouvait pas rendre son verdict
1. La seule paire divergente (paire-008, graine du 14/09 04:00Z) attendait son verdict T+72h du 17/09 : **3 jours de retard, personne ne le voyait**.
2. Le plist ne lance QUE `--cycle` → `--juger` n'était jamais exécuté. Conséquence : le critère R6 (≥ 20 cas au 08/11) était inatteignable — 1 divergence par semaine mesurée → ~8 cas au 08/11 → « dossier fermé » sans jamais avoir été testé.
3. Le cycle juge désormais ce qui est dû (idempotent : ne rejuge jamais une paire jugée). **Verdict récupéré : paire-008 = MISS** (B disait « up », le marché a fait « down »).
4. Le test : un cycle sans paire arrivée à échéance ne doit rien juger (vérifié : 0 paire).
5. Cause racine **R3 + R7** : le protocole existait, sa conclusion non — et un ancien statut « enregistrée (T+72h) » faisait croire que le jugement était pris en charge.

### 2026-09-20 — Les verdicts des protocoles étaient recopiés d'un document du 14/09
1. La page vol affichait des « verdicts datés » recopiés d'un MD écrit le 14/09 : aucun verdict n'était **calculé**. Un protocole sans matériel (arbitrage LLM-vs-règle : 0 alerte produite en 7 jours) ou au seuil hors d'échelle (RWA : top 20 TVL composé de pools à ~0 % de rendement) passait pour « en cours d'observation ».
2. Les critères sont PRÉ-ENREGISTRÉS (fixés AVANT de voir les données) : donc leurs verdicts sont calculables. Personne ne les calculait.
3. `scripts/verdicts_protocoles.py` (scellé au registre) écrit `thermo/PROTOCOLES_VERDICTS.json` ; la page lit ce fichier, plus le document. Un protocole qui ne peut pas conclure est affiché **IMPOSSIBLE/⚠**, jamais « ça suit son cours ».
4. Le test : chaque protocole doit rendre un verdict commençant par SUCCES/ECHEC/EN ATTENTE/IMPOSSIBLE, et une ligne ⚠ quand il ne peut pas conclure.
5. Cause racine **R3 + R7** : « corrigé » non propagé et verdict ancien cité comme actuel.

### 2026-09-15 — lib_dialectes : assertion fausse du codeur hub
1. Le modèle codeur (Qwen3-Coder) a écrit `0x660F6BB == 106985659` — faux (vrai : 107 017 915).
2. Pas de radar sur le code GÉNÉRÉ : le self-test du codeur testait sa propre erreur.
3. Buffy recalcule chaque assertion à la main avant installation ; assertion corrigée avec la vraie paire du bug x402 (`0x66077A5 = 106985381`).
4. `lib_dialectes.self_test()` corrigé + règle : tout code généré passe une vérification Buffy avant sceau.
5. **R7** (erreur de l'agent/codeur) — attrapée AVANT la mise en service.

### 2026-09-15 — geopol-indice / cockpit-vol en grisaille fantôme
1. Le chien classait 2 organes vivants en zone grise depuis des jours.
2. Le scanner associait organe ↔ plist par nom EXACT ; « geopol-indice » ≠ plist « com.ace777.geopol ».
3. Organes renommés sur le stem de leur plist (« geopol », « gen-cockpit-vol ») + re-scan.
4. Règle gravée : le nom de l'organe DOIT être le stem de sa plist — à transformer en check automatique (usine U1).
5. **R1**.

### 2026-09-15 — SKIP_VEILLE_RED : le verrou temporel qui coûtait des %
1. Un hint négatif de la veille bloquait tout achat 30 min ; RIZE +38,7 % et EDEL +60,9 % ratés pendant les blocages.
2. Aucun organe ne mesurait le COÛT des refus du moteur (on comptait les refus, pas ce qu'ils coûtaient).
3. `VEILLE_SKIP_RED_ON=0` + audit complet des verrous : cooldown 4 h → 1 h, REENTRY_MAX 1 → 3.
4. Compteur de coût des refus à intégrer au rapport quotidien (refus + variation de prix pendant le refus).
5. **R5** (+ conception : timer à la place d'un état de marché).

### 2026-09-14 — x402 : index de ledger 4,4 milliards
1. L'anti-figage du radar agentique comparait des index absurdes.
2. `ledger_index` arrive en chaîne DÉCIMALE ('106985381') ; le code la lisait en base 16.
3. Conversion base 10 uniquement, préfixe 0x = seul cas hex ; état réinitialisé (backup /tmp avant).
4. Désormais codée UNE fois pour toutes dans `lib_dialectes.py` (to_int), self-testé.
5. **R4** — l'usine U3 est née de cet incident.

### 2026-09-14 — rotation_jsonl.py écritures refusées « mystérieusement »
1. Écritures échouaient sans raison apparente.
2. Le sceau du matin avait mis le fichier en 444 (lecture seule) ; rien ne le documentait.
3. Procédure maison fixée : déclaration d'évolution → chmod → édition → re-sceau → reverrouillage.
4. Le chien vérifie qu'un fichier scellé modifié a bien son md5 mis à jour au registre (sinon alerte).
5. **R7** — le scellement doit toujours annoncer son propre cycle de vie.

---
*Fin du journal initial. Prochaine entrée à la prochaine panne — les 5 lignes AVANT le code.*
