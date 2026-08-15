# ULTRA — inferx.analyse

**Verdict global :** GO AVEC RÉSERVES (Stabilité à l'échelle compromise si le lanceur n'embarque pas le diagnostic sous charge).

**Q1. PROTOCLE DU RUN TEST — quel lanceur ?**
c) Ajouter d'abord le crash dump à GEMINI_TEST, puis lancer avec GEMINI_TEST.
*Justification :* On ne reproduit pas un bug en aveugle ; pour trouver la cause racine en prod/test sans pansement, il faut la stricte configuration du run crashé (GEMINI_TEST) augmentée du mécanisme de capture d'erreur (crash dump).

**Q2. CHAMPION — genesis = af307996 (98c80b5c + trap ERR diagnostic).**
a) RE-SCELLER af307996.
*Justification :* Le trap est l'instrument chirurgical exigé par la famille pour percer le silence de la mort rc=1 ; le sceller valide formellement cette modification sémantiquement légitime.

**Q3. PLAN DE RETOUR — valides-tu les points de rollback ci-dessus ?**
Oui (avec réserve sur la synchronisation des manifests).

**Amélioration concrète GO-sized :**
Avant le top départ, automatiser une vérification d'intégrité croisée (checksum sha256) entre le manifeste `genesis_manifest.txt` et l'état réel injecté en mémoire pour interdire tout faux positif de préflight dû au trap.
