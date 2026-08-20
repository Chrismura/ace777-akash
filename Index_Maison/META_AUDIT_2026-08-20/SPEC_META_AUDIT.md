# SPEC — Re-validation canonique de la méta-analyse des audits (20/08)

MÉTA-ANALYSE DES AUDITS ACE777 — nous avons inventorié 484 documents d'audit
(109 audits propres + 375 avis famille) depuis le 29/07. Nous avons croisé les
CAUSES RACINES et dégagé 4 classes de trous :

1. **DÉGRADATION SILENCIEUSE** : chaque organe peut tomber ou se tromper sans
   que rien ne crie (mort rc=1 sans alerte 14/08, vigie morte 19/08, filet qui
   échoue loggé mais invisible, champion patché en plein run chargé
   silencieusement).
2. **GARDE-FOU ÉCRIT MAIS PAS ACTIF** : plists vigie-live, superviseur-process,
   superviseur-core écrites mais JAMAIS chargées ; sante_index oubliait la vigie
   marché.
3. **FAUSSE SÉCURITÉ** : filet à 8 bps refusé par Binance (-2021) mais le bot
   CROIT être protégé ; indicateur blocs privatisés mal calibré (résolution
   10 min) affichait 34 % de bruit ; PnL BRUT +14 alors que NET −278.
4. **VUE PARTIELLE** : 109 audits propres et AUCUN index unique — le pattern
   était invisible faute de vue d'ensemble (créé aujourd'hui).

PATTERN EN UNE PHRASE : « Nous créons beaucoup, vérifions peu, et les
défaillances sont silencieuses : chaque organe peut tomber ou se tromper sans
alerte, avec une fausse sécurité issue de mesures mal calibrées. »

================ MÉTA-ANALYSE COMPLÈTE ================

(contenu : Index_Maison/INDEX_AUDITS_ET_META_ANALYSE_2026-08-20.md)

QUESTION FAMILLE :
(1) Le pattern des 4 classes est-il juste et complet ?
(2) Quelle classe est la PLUS dangereuse et pourquoi ?
(3) Quelle correction SYSTÉMIQUE (pas rustine) recommandes-tu, mesurable et bornée ?
(4) Réserves.

Une brique « veille_degradation.py » a déjà été implémentée sur cette base
(10 plists + 4 heartbeats + plages d'indicateurs, chaîne 8 dans sante_index,
8/8 chaînes OK) — tu peux la valider ou la contredire.

Périmètre : genesis INTACT (C1), wrappers/molettes seulement.
