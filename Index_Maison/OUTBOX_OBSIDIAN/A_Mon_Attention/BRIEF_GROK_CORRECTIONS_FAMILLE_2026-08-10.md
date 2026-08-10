# BRIEF GROK — CORRECTIONS FAMILLE SPEC V2 (3 etages) — 10/08

Systeme ACE777 - Mac 8 Go, hub local port 11435, 9 providers gratuits.
Setup des 3 etages en cours (27 services launchd -> cible 12-14).

ETAT REEL (mesure mecaniquement, pas de memoire) :
- date : 2026-08-10 12:58:09 CEST
- hub /health : {"status": "ok", "providers": 9}
- nb services ace777 charges : 23
- services vivants : com.ace777.cockpit-http com.ace777.prise-ia com.ace777.cockpit-pont
- superviseur : -	0	com.ace777.superviseur
-	0	com.ace777.superviseur-core
- ram : The system has 8589934592 (524288 pages with a page size of 16384).

CONTEXTE : Tu as concu REPONSE_GROK_3ETAGES.md (spec setup des 3 etages) puis
REPONSE_GROK_V2_HARMONIE.md et REPONSE_GROK_V21_BRUT.md. La FAMILLE COMPLETE
(GEMINI + DEEPSEEK + JUGE + ULTRA) a juge ta spec le 10/08 : VERDICT
« VALIDE AVEC MODIFICATIONS » (unanime) — 11 points de consensus a integrer.
Ta mission : produire la SPEC V2 CORRIGEE, pas un plan : le texte spec exact,
pret a executer, avec les 11 corrections integrees POINT PAR POINT.

LES 11 CORRECTIONS (JUGEMENT FAMILLE 10/08, consensus des 4 membres) :

C1. INVENTAIRE EXACT AVANT TOUTE SUPPRESSION (Etape 0) : launchctl list + launchctl
    print par service + dependances inter-services + budget RAM mesure par
    service. (Sans inventaire, la reduction 27->13 = tir a l'aveugle.)

C2. KeepAlive:false + ThrottleInterval:1800 = FAUX : launchd ne relancera JAMAIS
    le superviseur apres sa sortie -> il ne tourne qu'une fois. Remplacer par
    StartInterval:1800 (ou KeepAlive:true + boucle interne sleep 60-120s).
    Un heartbeat a 30 min n'en est plus un.

C3. BACKUP PLISTS OBLIGATOIRE avant Etape 4 : copie tar de ~/Library/LaunchAgents
    + checksums + test de reversibilite (restore + reload) AVANT de continuer.

C4. NE PAS TOUCHER cockpit-http/pont au depart : cockpit.py doit d'abord
    LIRE/cohabiter avec eux, ne les remplacer qu'apres avoir expose la meme API
    et bascule les consommateurs.

C5. UNLOAD UN PAR UN avec test 10 min : un service desactive a la fois + delai
    de test + audit des dependances avant chaque suppression.

C6. Mode probatoire C6 + boucle 30 min = CONTRADICTION : 48 cycles/jour vs
    1 action/jour. Solution : compteur journalier persistant dans state.json
    (ou C6 = « 1 type d'action/jour », ou observation seule dry-run).

C7. C1 = detection + alerte, JAMAIS chmod auto : chmod 444 EST une ecriture,
    le superviseur violerait C1 en l'appliquant. C1 = stat + alerte + journal
    + sanction via C5 (unload service fautif).

C8. RAM < 25 Mo irrealiste en Python : Python + libs ≈ 35-50 Mo RSS. Stdlib
    only (urllib, subprocess vm_stat/launchctl) OU cible < 50 Mo assumee.

C9. TEST DE CHARGE AVANT activation pleine : 1h de superviseur avec 13 services,
    mesurer RAM/CPU, /health reste OK + metriques de reference AVANT pour
    comparer APRES.

C10. GESTION DU CRASH DU SUPERVISEUR : qui le relance s'il meurt ? Wrapper
     KeepAlive:true ou watchdog dedie.

C11. TIMEOUT PAR PROVIDER dans cockpit.py : max 2s/provider pour ne jamais
     bloquer le cockpit.

CONTRAT DE SORTIE : reponds avec 1) SPEC V2 CORRIGEE complete (le texte spec
exact, etape par etape, avec les 11 corrections marquees [C1]...[C11] a
l'endroit ou elles s'appliquent) 2) une ligne finale : VERDICT SPEC V2 : OK.

