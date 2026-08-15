# AVIS gemini (provider Google Gemini, 4.4s)

### 1. Validation / correction du schéma du contrat JSON (`cortana_pilot.json`)
* **Champs validés/ajoutés** : Le schéma de base (ts, source, proposals) est correct mais incomplet pour garantir la sécurité et l'auditabilité.
* **Champs manquants indispensables** : 
  - `cortana_accuracy_score` : Rappel obligatoire du score de justesse au moment de la génération (ex: `0.44`).
  - `enforced_mode` : Indique si la proposition est `ADVISORY` ou `AUTO`.
  - `hash` : Empreinte cryptographique ou checksum pour éviter toute corruption ou injection externe dans le fichier.
* **Anti-gaming** : Imposer un taux de rafraîchissement minimal (ex: max 1 modification par paramètre toutes les 6 heures) pour empêcher Cortana de faire du *flip-flop* permanent sur les seuils suite à du bruit de marché.

---

### 2. Tranchage A, B et C
* **A. Liste blanche et bornes (Paramètres autorisés)** :
  - `DIP_FLOOR_MULT` ∈ `[0.85, 1.15]` (Étroit ±15%)
  - `RIP_FLOOR_MULT` ∈ `[0.85, 1.15]`
  - `NOTIONAL_USDT` ∈ `[0.5, 1.0]` (Multiplicateur de mise de base uniquement à la baisse en cas de score faible).
  - *Interdiction absolue* : Touche aux stops de sécurité, aux régimes (IMPULSE/COOLING) et au kill-switch.
* **B. Mode d'application vu le score de 44%** :
  - **Option (2) STRICTE : ADVISORY PUR**. Vu le score de 44% (sous le pile-ou-face) et la discipline F1, **aucune application automatique n'est tolérée**. Le JSON est écrit, affiché sur le dashboard de Buffy, mais le moteur Hulk **ignore** les valeurs pour l'exécution tant que la justesse de Cortana ne dépasse pas durablement 60%.
* **C. Mesure d'impact (Boucle d'apprentissage)** :
  - Shadow-tracking : Le moteur enregistre en parallèle (dans les logs CSV) le PnL réel (sans Cortana) et le PnL théorique qu'aurait généré Hulk si les propositions d'ajustement avaient été suivies. Comparaison par fenêtres glissantes de 7 jours.

---

### 3. Risques précis
* **Sur-apprentissage / Rétro-fitting** : Cortana pourrait ajuster les seuils pour coller aux derniers mouvements passés (courte vue), augmentant le risque de faux signaux sur le dip&rip suivant.
* **Bruit statistique** : Avec 44% de justesse, laisser un mode automatique (même clampé) détériorera mathématiquement l'espérance de gain du bot Hulk par rapport aux paramètres par défaut robustes.

---

### FICHE DE SYNTHÈSE

* **VERDICT** : GO-AVEC-RÉSERVE (Valide l'architecture du contrat JSON et le mode Advisory, mais **REFUSE** tout auto-pilotage tant que la justesse < 60%).
* **CONFIANCE** : 85 %
* **HYPOTHÈSES** : 
  1. Le moteur Hulk dispose d'un mécanisme de lecture robuste gérant les fichiers JSON absents ou malformés.
  2. Buffy surveille activement le dashboard pour valider ou rejeter manuellement les propositions Cortana.
* **CE QUI CHANGERAIT L'AVIS** : Une remontée documentée et audité du score de justesse de Cortana au-dessus de 60% sur les 3 derniers cycles d'évaluation.
* **AMÉLIORATION PROPOSÉE** : 
  1. Ajouter un champ `validation_status` (`PENDING`, `APPROVED_HUMAN`, `REJECTED`) géré par Buffy pour valider la boucle d'apprentissage.

**SYNTHÈSE** : 
Contrat JSON validé avec ajout de métadonnées de traçabilité et de hachage. Mode d'application strictement **ADVISORY** (zéro auto-pilotage) en raison du score de 44% sous le seuil critique. Mesure d'impact par *shadow-tracking* comparant le PnL réel au PnL théorique conseillé. Liste blanche restreinte aux multiplicateurs de seuils (±15%).
