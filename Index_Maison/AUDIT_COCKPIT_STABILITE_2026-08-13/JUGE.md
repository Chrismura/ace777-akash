**1. Verdict :**
**GO** — Les corrections ciblent précisément les causes racines identifiées (ré-initialisation parasite des coordonnées graphiques, nettoyage linguistique brut des cartes et synchronisation temporelle du feed hub.json). Les tests réels Chromium et WebKit valident la stabilité.

**2. Risque / Régression possible :**
Le passage de l'intervalle du feed hub de 120s à 30s (**C3**) va quadrupler la fréquence d'écriture disque/réseau et les appels liés. Sur une longue session ou si le démon `launchd` subit une dérive, cela peut accentuer la charge I/O inutilement si le hub n'a pas évolué entre-temps (risque de micro-saccades du cockpit lors des fetchs rapprochés).

**3. Suggestion d'amélioration concrète :**
Implémenter un **mécanisme de hachage (ou ETag/timestamp de version)** sur le `hub.json` côté serveur avant de déclencher le rendu complet côté client, combiné à un `ETag`/`Last-Modified` ou une comparaison de payload léger. Ainsi, le cockpit fetch toutes les 30s mais n'exécute le parsing/DOM update lourd *que* si le contenu a réellement changé, économisant ainsi le CPU et garantissant une fluidité absolue.