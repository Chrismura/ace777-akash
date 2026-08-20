# SPEC — TOUR 2 : TRANCHER SUR UN PROTOCOLE UNIQUE (20/08/2026)

Tu es membre de la famille ACE777. Au TOUR 1 (contestation), chacun de vous a
contesté le diagnostic de Buffy et proposé un protocole anti-validation-aveugle
(PAA-C1, SVE-C1, PZVC-1, P0-VERIFY, Hard Interlock, Protocole de l'Œil Blanc).
Vos 6 propositions convergent vers le même principe. Vous avez aussi demandé
des informations — elles sont fournies ci-dessous, factuelles.

## CE QUI EST DEMANDÉ — UNE SEULE QUESTION

**Fusionnez vos 6 protocoles en UN SEUL protocole opérationnel**, applicable
par les wrappers (genesis INTACT, C1), mesurable, borné, testable. Répondez en
2 parties :

### PARTIE 1 — LE PROTOCOLE UNIQUE (obligatoire)
Donnez le protocole final sous forme de RÈGLES numérotées (max 8), chacune
avec : (a) la règle exacte, (b) où elle s'applique (wrapper/script/point
d'entrée), (c) comment on la TESTE (preuve de non-régression), (d) son coût.
Le protocole doit inclure au minimum vos points communs :
1. Interdiction de valider ("c'est corrigé", "le système tourne", "c'est sain")
   sans la sortie brute d'une commande système de vérification.
2. Fail-fast absolu au démarrage (aucun lancement si un garde-fou manque).
3. Miroir inversé / Red Team (chercher la preuve d'échec avant de conclure).
4. Double validation d'état (fichier présent ≠ service actif ; 2 checks indépendants).
5. Le terminal a toujours raison (si IA et réel divergent → le réel gagne, l'IA crie).

### PARTIE 2 — TRANCHER LES DIVERGENCES (obligatoire)
Vos propositions divergent sur des points précis. TRANCHER pour chacun :
(a) Un seul démon watchdog unifié (Rust/Python) vs plists launchd multiples ?
(b) L'alerte vocale seule suffit-elle, ou faut-il un canal externe (webhook) ?
(c) Le verrou md5 anti-patch-en-plein-run : obligatoire partout ou seulement
    sur le champion ?
(d) Faut-il un hook git pre-commit exécutant sante_index.py, ou un check
    runtime uniquement ?
(e) 72h d'autonomie sans intervention : est-ce le critère de validation final ?

================ RÉPONSES À VOS DEMANDES D'INFORMATIONS (TOUR 1) ================
(contenu : REPONSES_ENVOI_FAMILLE_2026-08-20.md)

## RÈGLES
- CLAUSE PERMANENTE : ne te contente pas de valider — propose mieux si prouvable.
- Périmètre : genesis INTACT (C1), wrappers/molettes/protocoles seulement.
- Format : VERDICT · CONFIANCE · HYPOTHÈSES · CE QUI CHANGERAIT L'AVIS ·
  AMÉLIORATION PROPOSÉE · SYNTHÈSE (5 lignes max). Français, factuel.
