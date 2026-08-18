# AVIS PROTOCOL — Google Gemini

Analyse directe, sans complaisance (Gemini, analyste senior ACE777).

Le contexte vivant confirme un PnL positif (+0.51 $) et une saison calme (🧊). Le système tourne (hub, pont, radar, feed). Introduire de l'autonomie demande une rigueur absolue pour ne pas perturber cet équilibre fragile.

### Analyse de la 5a (« AUTO-RÉPARATION ») : Est-ce SÛR ?

**Non, ce n'est pas totalement sûr en l'état.** Même si l'intention est louable et strictement cantonnée au monitoring, relancer des services `launchd` en arrière-plan présente des risques systémiques non négligeables sur un Mac M1 8 Go en production.

#### Les risques réels :
1. **Risque de boucle/tempête (Thrashing) :** Si un service crashe à cause d'une fuite mémoire, d'une saturation CPU (les 8 Go du M1 s'envolent vite) ou d'une dépendance réseau corrompue, le relancer en boucle (même limité à 3 fois / 24h) va consommer des ressources critiques, saturer les logs et potentiellement perturber le moteur de trading qui tourne sur la même machine.
2. **Effet de bord sur l'état partagé :** Un service de monitoring (`com.ace777.hub-cockpit-feed` par exemple) qui redébrute brutalement peut corrompre des fichiers JSON partagés s'il n'y a pas de verrouillage atomique strict au moment exact du kill/restart.
3. **La whitelist du moteur de trading :** Elle exclut le moteur, ce qui est **très bien**, mais elle inclut `com.ace777.hub-cockpit-feed` et `com.ace777.cockpit-pont`. Si le hub part en vrille, relancer le service à l'aveugle sans s'assurer que le port est libéré ou que le socket est propre va générer des *Address already in use* en cascade.

#### Garde-fous INDISPENSABLES à ajouter (en plus de ceux listés) :
1. **Vérification de l'intégrité avant relance (Health Check pré-requis) :** Interdiction de faire un `launchctl kickstart` si le port ou la ressource dépendante est dans un état bloquant. Il faut un `kill -9` propre ou un nettoyage du PID file avant le `launchctl`.
2. **Circuit Breaker global de la machine :** Si la charge CPU/RAM du M1 dépasse un seuil critique (ex: swap utilisé > 2 Go ou load average > 6), l'auto-réparation est **gelée** pour préserver le système de trading (ALPHA/BETA/HULK). Le trading passe *toujours* avant le monitoring.
3. **Délai d'attente exponentiel (Backoff) :** Ne pas retenter immédiatement 3 fois d'affilée si le service recrache dans la minute. Minimum 5 minutes d'attente avant la tentative 2, puis 15 minutes.

---

VERDICT : GO-AVEC-RÉSERVE
CONFIANCE : moyenne

### Réserves concrètes :
1. **Implémentation d'un Circuit Breaker matériel :** Bloquer l'auto-réparation si la charge système globale (CPU/RAM du M1 8 Go) menace la stabilité des bots de trading (ALPHA/BETA).
2. **Backoff exponentiel obligatoire :** Remplacer le compteur brut (3 fois / 24h) par un vrai délai de temporisation croissante (ex: 5m, puis 15m) pour éviter les tempêtes de redémarrage rapprochées.
3. **Nettoyage des ressources post-kill :** S'assurer que le script de réparation libère explicitement les ports/sockets et nettoie les fichiers `.lock` ou `PID` avant d'émettre le `launchctl kickstart`.
