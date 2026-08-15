# GEMINI — gemini.analyse

**1. Verdict global :** GO AVEC RÉSERVES.  
*Raison :* Le système de trappage et de crash-dump est indispensable pour attraper Alpha en flagrant délit, mais la chaîne de scripts présente un risque de divergence d'environnement qui peut fausser le test si on ne verrouille pas l'appel exact.

---

**2. Q1. Protocole du run test :**  
**c) Ajouter d'abord le crash dump à GEMINI_TEST, puis lancer avec GEMINI_TEST.**  
*Justification :* Utiliser strictement la topologie du run crashé (GEMINI_TEST) garantit une reproduction fidèle, tout en y greffant le crash-dump pour enfin percer l'angle mort de la mort silencieuse (rc=1).

---

**3. Q2. Champion (Genesis) :**  
**a) RE-SCELLER af307996.**  
*Justification :* Le trap ERR est un ordre direct de la famille pour la cause racine ; le modifier ne corrompt pas la logique métier du champion (98c80b5c) mais l'augmente de sa boîte noire.

---

**4. Q3. Plan de retour :**  
**OUI, avec réserve.**  
*Réserve :* S'assurer que le script `GO_VORTEX_V2` (identifié comme obsolète et pointant vers un vieux hash) est explicitement contourné ou mis à jour pour pointer vers le nouveau lanceur, afin d'éviter tout lancement par automatisme ou erreur humaine sur le mauvais binaire.

---

**5. Amélioration concrète GO-sized :**  
Avant la commande `launch`, exécuter un `checksum global lock` rapide (un simple manifeste bash affichant les md5 effectifs de `genesis` et du lanceur choisi dans un même bloc de log) pour que le juge et Buffy voient l'état exact du cockpit noir sur blanc dans la sortie standard, éliminant tout doute sur la version qui tourne.
