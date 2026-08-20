# AVIS JUGE (task juge.tranche · Google Gemini · 2026-08-20T13:48Z)

VERDICT : GO AVEC RESERVES
CONFIANCE : 92 %

HYPOTHÈSES :
1. Le protocole unique (PAA-ACE777) couvre l'intégralité des failles observées les 19 et 20 août (absence de plist, mort silencieuse, faux positifs).
2. La combinaison launchd natif + DMS externe garantit la résilience sur 72h sans intervention humaine.

CE QUI CHANGERAIT L'AVIS : Un rapport de run démontrant une panne non interceptée par le double check `launchctl + pgrep` ou un contournement du fail-fast au démarrage.

AMÉLIORATION PROPOSÉE : 
1. **Intégration d'un heartbeat fichier obligatoire** pour chaque service surveillé : en plus du double check d'état (règle 4), exiger qu'un fichier `data/heartbeat/[service].ts` soit rafraîchi toutes les 60s max. Si le process tourne (PID actif, launchd OK) mais que le timestamp du heartbeat est > 120s, le service est déclaré "zombie fonctionnel" (bloqué dans une boucle) et relancé de force.
2. Remplacer le `subprocess.Popen` de la voix par un démon d'écoute de la file d'attente d'alertes JSON pour éliminer définitivement la mort par interruption du shell parent (signalée dans la Demande 2).

SYNTHÈSE :
Le protocole unique fusionné est rigoureux, testable et répond aux exigences de la famille. Mes réserves portent uniquement sur l'ajout d'un heartbeat fonctionnel pour contrer les "zombies logiciels" (processus vivants mais figés), point aveugle restant de la double validation actuelle. C'est validé sous réserve de cet ajout.
