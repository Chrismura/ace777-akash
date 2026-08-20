# SPEC — CONTESTATION EN ENTIER DU DIAGNOSTIC (20/08/2026)

Tu es membre de la famille ACE777. On te demande de **CONTESTER EN ENTIER**
le diagnostic ci-dessous — pas de le valider poliment. Cherche ce qui est
FAUX, INCOMPLET, EXAGÉRÉ, ou ce qui repose sur des données insuffisantes.
La meilleure contribution = détruire ce qui doit l'être, prouver le reste.

## LE DIAGNOSTIC À CONTESTER (Buffy, 20/08)

> « Les idées de Christophe n'ont JAMAIS été le problème. Les erreurs sont
> toujours dans la couche d'exécution — jamais dans l'intention. »

Sous-jacent : « Nous créons beaucoup, vérifions peu, et les défaillances sont
silencieuses : chaque organe peut tomber ou se tromper sans alerte, avec une
fausse sécurité issue de mesures mal calibrées. »

Corollaires proposés par Buffy :
1. La force de Christophe = son « regard » (voir l'écart réel vs référence) —
   prouvé 128 fois dans l'historique de juillet + 7 cas documentés en août.
2. Ce regard doit être institutionnalisé en PROTOCOLE (check automatique
   avant toute conclusion : fichier réel vs référence, plists chargées, diff
   exact, canon respecté).
3. La bonne séquence : résilience → stabilité → mesure fiable → rentabilité.
4. Complexité = ennemie : chaque ajout doit être compensé par un retrait.
5. L'autonomie vient DERNIÈRE (un système autonome qui se dégrade en silence
   est pire qu'un système manuel).

================ PREUVES COMPLÈTES (fichier joint) ================
`PREUVES_CONTESTATION_2026-08-20.md` — 7 cas chiffrés (indicateur 34 %→8,3 %,
plists jamais chargées, diff S-10 vide, 484 audits, canon prompts, 128 « tu as
raison » juillet, 4 classes de trous) + Partie C (construit et testé) + Partie D.

## QUESTIONS (réponds aux 5)

1. CONTESTE point par point : qu'est-ce qui est FAUX, INCOMPLET, EXAGÉRÉ ?
   Preuves à l'appui — pas d'impression.
2. Le cadre « intention vs exécution » est-il le bon ? Y a-t-il une lecture
   plus profonde du pattern ?
3. La séquence résilience → stabilité → mesure → rentabilité est-elle
   correcte ? Qu'est-ce qui manque pour : stabilité, résilience,
   prédictibilité (mesures fiables), autonomie prudente ?
4. Quel PROTOCOLE CONCRET (borné, mesurable, genesis INTACT C1) empêche une
   IA de conclure sans vérifier — le piège répété 128+ fois ?
5. INFORMATIONS DEMANDÉES : si une information supplémentaire majeure
   améliorerait l'EXACTITUDE de ton évaluation (fichier, log, chiffre, diff,
   historique), DEMANDE-LA explicitement ici — nous la fournirons.

## RÈGLES

- CLAUSE PERMANENTE (Christophe) : ne te contente pas de corriger ou valider —
  si tu proposes AUTRE CHOSE ou une AMÉLIORATION prouvable, dis-le.
- Périmètre : genesis INTACT (C1), wrappers/molettes/protocoles seulement.
- Réponds en français, factuel, 5 sections + section 5 obligatoire pour les
  demandes d'information.


================ PREUVES COMPLÈTES ================
# PREUVES — SOUMISES À CONTESTATION FAMILLE (20/08/2026)

> Fichier de PREUVES (pas d'opinions) pour la consultation canonique de
> CONTESTATION. La famille doit contester EN ENTIER le diagnostic de Buffy,
> avec preuves à l'appui, et peut demander des informations supplémentaires.

---

## CONTEXTE EN UNE PHRASE

ACE777 : moteur de trading BTC (testnet) en duo ALPHA/BETA + Hulk (paper MEXC)
+ une famille d'agents IA (6 membres + codeur) + cockpit + mémoire Obsidian.
Du 29/07 au 20/08 : 484 documents d'audit (109 audits propres + 375 avis famille).
Historique de conversation archivé : `29$/historique/conversation/transcript_complet.jsonl`
(12 Mo, juillet).

---

## PARTIE A — LES 7 CAS (preuves chiffrées)

### A1. Indicateur « blocs privatisés » (19-20/08)
- **Le concept (pépite Christophe)** : matrice du Juge — taux de tx jamais vues
  dans la mempool publique > 35 % + volume > 1000 BTC = baleine qui téléporte
  un règlement OTC via mempool privée/CPFP masqué. Fichier :
  `hulk-mexc/scripts/vigie_mempool_pepite_christophe.py`.
- **Verdict initial de Buffy (FAUX)** : « bruit blanc, l'indicateur ne mesure rien ».
- **Preuves du contraire** :
  - 281/281 blocs stables intra-run : le même bloc analysé 3× donne le même
    taux → propriété DÉTERMINISTE du bloc, pas du hasard.
  - Test live (25 min, snapshot 60 s vs 10 min) : même bloc → 33,6 % de
    « fantômes » à 10 min vs 8,3 % à 60 s. Résidu dense 0,5-8,3 % = vrai signal.
  - Cause : résolution du snapshot (600 s vs 120 s). Correctif : 120 s + garde-fou carnet vide.

### A2. Vigie morte / systèmes de relance (20/08)
- **Verdict initial de Buffy (FAUX)** : « aucun système de relance n'existe ».
- **Preuves** :
  - Plists ÉCRITES mais JAMAIS chargées : `com.ace777.vigie-live`,
    `com.ace777.superviseur-process`, `com.ace777.superviseur-core`.
  - `sante_index.py` (17/08) vérifie 6 chaînes mais ZÉRO référence à la vigie
    marché (`vigie_live`).
  - Le SEUL relanceur de la vigie marché (`superviseur.sh`) était lancé
    manuellement et mort le 19/08 à 14:09:12, sans personne pour le relancer.

### A3. Patch S-10 (19/08) — accusé à tort
- **Verdict initial de Buffy (FAUX)** : « le patch S-10 appliqué en plein vol a
  cassé les stops ».
- **Preuves** :
  - Diff du commit S-10 (19/08) : ZÉRO ligne touchant les stops
    (algoOrder/triggerPrice/reduceOnly).
  - Migration V4 (algoOrder) : 17/08 22:08Z, commit `0f81068c` — PAS S-10.
  - Erreurs réelles du 19/08 : `-2021 Order would immediately trigger` (26×,
    filet 8 bps trop serré) + `-4116 ClientOrderId duplicated` (8×, ID
    `ACESTOP${i}` réutilisé après relance).

### A4. Nombre d'audits (20/08)
- **Verdict initial de Buffy (FAUX)** : « il y a 6 fichiers d'audit ».
- **Preuve** : 484 documents d'audit (71 AUDIT + 5 ENQUÊTE + 386 DIAG +
  19 CHECKUP + 3 CONSTAT + 375 avis famille).

### A5. Système de prompts canon (18-20/08)
- **Fait** : canon `identity/prompts/famille.json` + `consulter_famille.py`
  créés le 18/08 (commit `0c26a085`, « corrige improvisation étape 5 »),
  COUTUMES_AGORA : « ne JAMAIS improviser les prompts famille ».
- **Erreur de Buffy (20/08)** : consultation improvisée → DIAG sans
  VERDICT/CONFIANCE (0 occurrence). Re-consultation canonique : 6/6
  GO-AVEC-RÉSERVES, confiance 82-88 %.

### A6. Historique juillet — 128 « tu as raison »
- **Source** : `29$/historique/conversation/HISTORIQUE_CHAT_COMPLET.md` (128 occurrences).
- **Patterns documentés** :
  - Mauvais fichier/moteur sur disque : `67a12f85` (PHI, sans barrière) vs
    `37fca367` (champion) — l'IA a alterné et « embrouillé les deux moteurs ».
  - Arrêt incomplet : `stop_ace777.sh` laissait vivre wrapper, watchdog,
    caffeinate → « TOUT EST COUPÉ. Zéro process » n'était pas vrai.
  - Spike raté : setup coupait le run pendant la fenêtre critique (+4000 $/1h).
  - Confusion PnL : « +29,41 = session, 100 $+ = cumulatif, j'avais tort ».

### A7. Méta-analyse — 4 classes de trous (20/08)
1. DÉGRADATION SILENCIEUSE (mourir sans alerte)
2. GARDE-FOU ÉCRIT MAIS PAS ACTIF (plists jamais chargées)
3. FAUSSE SÉCURITÉ (mesure mal calibrée → on croit être protégé)
4. VUE PARTIELLE (aucun index unique des audits)

---

## PARTIE B — LE PATTERN PROPOSÉ PAR BUFFY (à contester)

> **Les idées de Christophe n'ont JAMAIS été le problème. Les erreurs sont
> toujours dans la couche d'exécution — jamais dans l'intention.**

Formulation : « Nous créons beaucoup, vérifions peu, et les défaillances sont
silencieuses : chaque organe peut tomber ou se tromper sans alerte, avec une
fausse sécurité issue de mesures mal calibrées. »

Corollaires proposés :
- La force de Christophe = son « regard » (voir l'écart réel vs référence).
- Ce regard doit être institutionnalisé en PROTOCOLE (check automatique :
  fichier réel vs référence, plists chargées, diff exact, canon respecté).
- La bonne séquence : résilience → stabilité → mesure fiable → rentabilité.
- Complexité = ennemie : chaque ajout doit être compensé par un retrait.
- L'autonomie vient DERNIÈRE (un système autonome qui se dégrade en silence
  est pire qu'un système manuel).

---

## PARTIE C — CE QUI A DÉJÀ ÉTÉ CONSTRUIT (20/08, testé)

- `veille_degradation.py` (plist 60 s) : 11 plists + 4 heartbeats + plages
  d'indicateurs. SAIN 11/11.
- `dms_veille.py` (plist 60 s) : Dead Man's Switch EXTERNE — surveille la
  brique elle-même, alerte vocale + rapport cockpit. OK 3/3. Chaos test
  `--test-panne` : alerte prouvée par le feu.
- `GO_VORTEX_V2.sh` : FAIL-FAST — refuse de lancer si les 5 plists de garde-fou
  ne sont pas chargées.
- `sante_index.py` : 8/8 chaînes OK (dont VEILLE DÉGRADATION + DMS).
- Détecteur blocs privatisés : snapshot 120 s + garde-fou carnet vide.

---

## PARTIE D — LA QUESTION DE CONTESTATION

1. CONTESTEZ point par point le diagnostic de Buffy (Partie B + A7) :
   qu'est-ce qui est FAUX, INCOMPLET, ou EXAGÉRÉ ? Preuves à l'appui.
2. Le cadre « intention vs exécution » est-il le bon ? Y a-t-il une lecture
   plus profonde du pattern (les 128 « tu as raison » + les 7 cas) ?
3. La séquence résilience → stabilité → mesure → rentabilité est-elle
   correcte ? Qu'est-ce qui manque pour qu'ACE777 atteigne : stabilité,
   résilience, prédictibilité (mesures fiables), autonomie prudente ?
4. Quel PROTOCOLE CONCRET (borné, mesurable, genesis INTACT C1) empêche une
   IA de conclure sans vérifier — le piège répété 128+ fois ?
5. INFORMATIONS DEMANDÉES : si une information supplémentaire majeure
   améliorerait l'EXACTITUDE de votre évaluation (fichier, log, chiffre,
   diff, historique), DEMANDEZ-LA explicitement ici — nous la fournirons.

FORMAT DE SORTIE OBLIGATOIRE : VERDICT · CONFIANCE · HYPOTHÈSES ·
CE QUI CHANGERAIT L'AVIS · AMÉLIORATION PROPOSÉE · SYNTHÈSE (5 lignes max).
