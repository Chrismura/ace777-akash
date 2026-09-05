# AVIS JUGE (task juge.tranche · Google Gemini · 2026-09-01T07:51Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 90 %

HYPOTHÈSES :
1. **L'I/O disque étouffe le CSV :** Sur près de 19 000 SKIP, l'écriture séquentielle synchrone dans le fichier CSV représente le véritable goulet d'étranglement, bien plus que le calcul pur des gates.
2. **La redondance indicielle :** Réévaluer à chaque poll de 20 secondes des conditions inchangées (notamment le volume `VOL` à 86 %) brûle inutilement des cycles CPU locaux et sature la télémétrie.

CE QUI CHANGERAIT L'AVIS :
- Un profilage mesurant une latence réseau (`fetch_all_prices`) représentant 99 % du temps total, rendant l'impact des écritures CSV totalement négligeable.
- Une dépendance critique des scripts d'analyse aval sur chaque ligne unitaire de SKIP brute sans agrégation possible.

AMÉLIORATION PROPOSÉE :
1. **Implémentation d'un buffer circulaire asynchrone (Ring Buffer) pour les logs :** Déporter l'écriture des SKIP dans un thread ou une file d'attente non bloquante pour découpler totalement l'I/O disque de la boucle critique du bot.
2. **Mémoïsation d'état par TTL glissant :** Introduire un cache local éphémère (durée calée sur `SCORE_EVERY`) stockant le dernier motif de SKIP par paire. Si le motif et le contexte de prix ne changent pas, seule l'émission d'un compteur interne est incrémentée, évitant la redondance des logs et du calcul.
3. *Alternative architecturale (Christophe)* : **Architecture d'observabilité par "Delta d'État"** : Remplacer l'enregistrement brut de chaque SKIP par un heartbeat d'état par paire qui ne logue que la *transition* (ex: passage de `VOL` à `VALIDÉ` ou inversement), couplé à un compteur global de refus pompé à chaque fin de cycle.

SYNTHÈSE (5 lignes max) :
Les SKIP massifs saturent l'I/O sans altérer les règles de risque, mais pénalisent la propreté de l'observabilité. Une déduplication à TTL court combinée à une journalisation asynchrone est indispensable. Les seuils et boucles métier restent strictement inchangés. Validation sous réserve du maintien des compteurs agrégés en mémoire.
