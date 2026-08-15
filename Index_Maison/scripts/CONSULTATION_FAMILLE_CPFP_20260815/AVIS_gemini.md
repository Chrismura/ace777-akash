# AVIS gemini (provider Google Gemini, 5.8s)

### 1. Évaluation des 3 cartes (gardées ou rejetées + seuils v1)
* **Carte 1 (Seuils statistiques adaptatifs - Z-score) :** **GARDÉE.** Évite la rigidité des seuils fixes connus des baleines. **Seuil v1 :** Déclenchement à $z > 3.5\sigma$ (moyenne mobile sur 7 jours glissants) sur le volume de frais ou la complexité topologique des arbres de transactions de la mempool.
* **Carte 2 (Signature CPFP par frais) :** **GARDÉE.** Incontournable car la physique du réseau impose de payer l'enfant au prix fort pour purger l'arbre à frais nuls. **Seuil v1 :** Tx enfant avec des frais $> 25\times$ la médiane courante de la mempool, couplée à un parent dont les frais sont $< 1.1\text{ sat/vB}$.
* **Carte 3 (Anticipation par accumulation dust) :** **GARDÉE AVEC RÉSERVE.** Pertinent mais coûteux en requêtes. **Seuil v1 :** Fenêtre glissante de 48h, détection d'un cluster $\ge 500$ adresses de sortie dust (montant $< 546\text{ sats}$) alimentées par une source unique ou un ensemble d'UTXO apparentés.

### 2. Gestion des faux positifs (CPFP légitime vs Camouflage)
Pour distinguer un CPFP d'urgence (ex: un utilisateur lambda voulant accélérer une tx bloquée) du camouflage de baleine :
* **Critère topologique :** Le camouflage présente un arbre binaire ou en étoile profond et large (centaines de branches à frais nuls alimentant un unique nœud final). Un CPFP d'urgence isole une seule transaction parent.
* **Critère de valeur :** Le montant global du UTXO monnaie rendue (change) réinjecté dans l'enfant doit être significatif (ex: $> 50\text{ BTC}$ équivalent), filtrant ainsi les micro-accélérations de particuliers.

### 3. Coût API mempool.space (Contraintes free tier)
* **Charge technique :** Récupérer les parents (`/tx/:txid/parent`), les enfants (`/tx/:txid/children`) et analyser les clusters de poussière exige de multiples appels séquentiels par bloc ou par tx suspecte.
* **Budget (scan 5 min / 288 scans/jour) :** Le plan gratuit de mempool.space limite généralement les requêtes à ~1/sec sans clé payante. Un scan complet d'un arbre CPFP profond peut consommer 20 à 50 appels d'un coup. Répété toutes les 5 minutes, cela sature le rate-limit public.
* **Limite de robustesse :** Risque critique de ban IP (`HTTP 429 Too Many Requests`). **Solution v1 impérative :** Ne requêter les parents/enfants *que* si un pré-filtre sur la mempool brute (`/mempool/recent` ou `/mempool`) détecte une anomalie de frais extrêmes ($>25\times$).

### 4. Intégration et pondération
* **Pont onchain :** Oui, injection dans `live.json` pour alimenter la synthèse Cortana et le modulateur de voilure Ada ($\pm 10\%$).
* **Pondération :** Le signal "Camouflage CPFP/Dust" est une alerte avancée (intention ou exécution). Pondération proposée :
  * Gros blocs traditionnels ($\ge 1000$ BTC) : 30%
  * Fragmentation classique : 30%
  * **Détection Camouflage CPFP/Dust (v2) : 40%** (car plus furtif et imminent).
* Si le signal v2 s'active, il force le score onchain en territoire négatif (si asymétrie baissière/manipulation détectée) ou neutre si ambigu, modulant Ada à la baisse.

---

* **VERDICT :** GO-AVEC-RÉSERVE
* **CONFIANCE :** 75 %
* **HYPOTHÈSES :** 
  1. L'API mempool.space tolèrera les requêtes ciblées sur les tx à hauts frais sans bannir l'IP du script `launchd`.
  2. Les baleines utilisent systématiquement un différentiel de frais $\ge 25\times$ pour purger leurs arbres dust.
* **CE QUI CHANGERSIT L'AVIS :** Un blocage récurrent de l'API mempool.space (rate-limit 429) rendant la surveillance de l'arbre CPFP impossible en mode 100% gratuit.
* **AMÉLIORATION PROPOSÉE :** 
  1. Implémenter un système de backoff exponentiel et de cache local JSON pour les tx déjà analysées afin d'économiser les appels API.
  2. Limiter la profondeur d'exploration des arbres CPFP à 2 niveaux maximum pour préserver la stdlib et le temps d'exécution $< 30$ secondes.

---
**SYNTHÈSE :** 
Cartes retenues : Z-score statistique ($\sigma > 3.5$), signature frais CPFP ($>25\times$ médiane, parent $<1.1\text{ sat/vB}$) et accumulation dust (48h, seuil $\ge 500$ outputs). Intégration via le pont onchain existant vers `live.json` (pondération v2 à 40% dans le mix global) avec déclenchement conditionnel des appels API pour respecter les quotas gratuits de mempool.space.
