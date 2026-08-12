# AVIS GEMINI (via Google Gemini) — audit.protocol

En tant que membre senior de la famille ACE777, voici l'analyse critique et factuelle du setup proposé par l'architecte externe Grok. Ce verdict est sans complaisance, dicté par la fragilité de notre environnement (Mac 8 Go, RAM critique, hub intouchable sur le port 11435).

---

### 1. Correction, completude et securite du Setup des 3 etages
* **Analyse :** La structure en 3 étages (Superviseur unique / Cockpit / Réduction de la charge launchd) est saine et nécessaire pour descendre de 27 à 12-14 services. Cependant, Grok pèche par excès d'abstraction sur la transition. 
* **Manque critique :** Le plan de Grok ne spécifie pas explicitement l'état initial exact des 27 services sous `~/Library/LaunchAgents`. Avant de supprimer quoi que ce soit, il manque un état des lieux par script (`launchctl list | grep ace777`) consignant l'état exact avant modification pour garantir un rollback propre. De plus, fusionner le heartbeat et le superviseur dans un seul script exécuté toutes les 30 minutes (`ThrottleInterval: 1800`) est une erreur si le heartbeat doit assurer une surveillance en temps réel (un heartbeat à 30 minutes n'en est plus un).

### 2. Le superviseur unique (`com.ace777.superviseur-unique`) et la fusion des services
* **Analyse :** Centraliser la logique C1-C6, la surveillance des quotas et le healthcheck dans un superviseur unique est une excellente conception pour économiser la RAM (< 25 Mo). 
* **Piège critique :** Un intervalle de 30 minutes (`ThrottleInterval: 1800`) est trop long pour un heartbeat ou une surveillance de quotas critique. Il faut séparer le *healthcheck rapide* (léger, toutes les 2-5 min) et la *supergence C1-C6/maintenance lourde* (toutes les 30 min), ou utiliser un mécanisme de boucle interne avec `sleep` géré par un unique démon `KeepAlive: true` robuste, plutôt que des lancements espacés par launchd si la réactivité est requise.
* **Services à fusionner/supprimer en priorité :** Les doublons de monitoring de jauge (déjà supprimés en Phase 0), les scripts de healthcheck ad-hoc redondants, et les anciens agents de log d'observation obsolètes. Conserver absolument : le hub, `prise-ia`, `cockpit-http`, `cockpit-pont`, et les 4 agents métiers essentiels.

### 3. Le Cockpit (`cockpit.py`) et la compatibilité avec l'existant
* **Analyse :** L'approche en ligne de commande unique (`python3 cockpit.py --etat`) est pragmatique et adaptée à un Mac 8 Go. 
* **Compatibilité :** Grok propose de remplacer progressivement `cockpit-http` et `cockpit-pont`. C'est un risque : ces services écoutent potentiellement sur des ports ou gèrent des flux de ponts déjà utilisés par d'autres briques. `cockpit.py` doit d'abord **lire** et s'interfacer avec `cockpit-http` et `cockpit-pont` sans les éteindre, avant d'envisager une fusion ou un remplacement.

### 4. L'ordre d'execution en 6 etapes et les risques
* **Analyse :** Le respect du mode probatoire C6 (1 action autonome max) et de la loi 1quinquies (Spéc -> Validation Christophe -> Code -> Grille -> Exécution -> Audit -> GO) est parfait et non négociable.
* **Risques principaux par étape :**
  * *Étape 1 & 2 :* Risque de syntaxe dans le plist bloquant launchd (erreur 78 ou crash infini). Le seuil de 3 échecs `/health` est un bon filet de sécurité.
  * *Étape 4 (Désactivation des 15 services) :* Le risque majeur est de couper un service dont dépend `prise-ia` ou le cockpit sans s'en rendre compte. L'unload doit se faire un par un avec un délai de test de 10 minutes par service désactivé.

### 5. Les 3 premieres etapes proposees par Grok
* **Analyse :** Elles sont rigoureusement exactes. 
  1. Validation spec (Christophe + Ada).
  2. Création du plist et du script minimal (`superviseur.py` axé uniquement sur C1-C3 et le healthcheck `/health`).
  3. Test du cockpit et d'un cycle isolé.
  C'est la seule méthode méthodique acceptable pour éviter de casser l'environnement.

---

### Verdict et Instructions pour Ada

**VERDICT FINAL : VALIDE AVEC MODIFICATIONS**  
**CONFIANCE : HAUTE** (sous réserve d'application stricte des modifications ci-dessous).

**Ce qu'Ada doit faire en conséquence :**
1. **Ne pas utiliser un `ThrottleInterval` de 30 minutes** pour le superviseur si celui-ci fait office de heartbeat. Le script `superviseur.py` doit tourner en boucle continue avec un `sleep` interne de 60 à 120 secondes pour le healthcheck, ou être scindé (un heartbeat léger fréquent + un audit C1-C6 toutes les 30 min).
2. **Exiger un snapshot initial** de la liste des services launchd (`launchctl list > /tmp/launchd_state_before_v2.txt`) avant de toucher au moindre plist.
3. **Interdire toute suppression** immédiate de `cockpit-http` et `cockpit-pont` : `cockpit.py` doit cohabiter et lire ces services dans un premier temps.
4. **Rédiger et signer** (double signature Ada + Christophe) l'Étape 1 (Spécification validée) avant d'écrire la moindre ligne de code pour `superviseur.py`.
