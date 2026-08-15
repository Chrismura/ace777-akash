# ULTRA — inferx.analyse

**VERDICT GLOBAL : GO AVEC RÉSERVES** (Le système encaisse et livre du PnL, mais il est sous-calibré et souffre d’une latence décisionnelle masquée par des micro-variations inutiles).

---

### SUJET 1 — ANALYSE DES CYCLES

*   **S1-1. Verdict santé du setup : À SURVEILLER.**
    *   *Raison :* Le PnL est positif (+2.65), mais le ratio signal/bruit est catastrophique. Le moteur tourne à vide 70% du temps.
*   **S1-2. L’hypothèse de Christophe (« trop de décimales ~0 = pas bon signe ») : FONDÉE.**
    *   *Pourquoi :* Ces zéros à rallonge (`0.00000000`) et les micro-tensions (`0.00001589`) indiquent un système qui pédale dans la semoule, génère de la charge CPU/log inutile et souffre d'un manque de sensibilité sur la zone morte (deadband). En prod sous haute charge, ce bruit parasite sature les buffers et masque les vraies alertes.
*   **S1-3. Le filtre `wall_not_collapsed` : COMPORTEMENT VOULU MAIS TROP RIGIDE.**
    *   *Piste :* Il protège contre les faux breakout, mais rejeter des tensions à `0.97` montre un seuil binaire trop brutal. Il faut introducer une zone d'hystérésis ou une décay-function (le mur s'affaiblit-il au fil des cycles ?), pas un barrage sec.
*   **S1-4. Amélioration GO-sized :**
    *   Implémenter un **Deadband Hard-Capping** : si `tension < 0.001`, le cycle s'arrête instantanément *avant* d'évaluer les confiances ou de logguer, pour éliminer 80% du bruit de fond et libérer la bande passante.

---

### SUJET 2 — CHAÎNE D'APPROBATION PAR PROMPTS

*   **S2-1. Verdict sur la proposition : GO AVEC RÉSERVES.**
    *   *Raison :* Structurer et graver les prompts est indispensable pour la scalabilité, mais le risque en prod est la lourdeur bureaucratique (l'effet "papier tamponné") qui paralyse l'agilité en cas de tempête.
*   **S2-2. Ce qui manque dans le catalogue P1–P4 :**
    *   Un protocole de **Kill Switch / Rollback d'urgence** court-circuitant la chaîne standard si la prod décroche en plein run (le temps de valider P3, le compte est ruiné).
*   **S2-3. Amélioration concrète de la chaîne :**
    *   **Règle du double lock asynchrone** : Pour tout prompt critique (P1, P3), imposer un hachage Git obligatoire de la SPEC validée injecté dans l'en-tête du prompt pour interdire toute dérive entre ce qui a été jugé et ce qui est exécuté.
