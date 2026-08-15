# GEMINI — gemini.analyse

**VERDICT GLOBAL : GO AVEC RÉSERVES**
*Raison courte : Le testnet prouve que le moteur génère du PnL sur ses pics, mais l'inactivité chronique (décimales à zéro) et la lourdeur du process manuel exigent un encadrement strict (filtrage et systématisation).*

---

### SUJET 1 — ANALYSE DES CYCLES

* **S1-1. Verdict santé du setup :** À surveiller.
  * *Raison :* Il produit de la valeur positive (PnL vert), mais souffre d'une anoxie opérationnelle (il dort 80% du temps).
* **S1-2. L'hypothèse de Christophe (« trop de décimales ~0 = pas bon signe ») :** Fondée, mais avec une nuance.
  * *Nuance :* Les décimales à `0.00000000` ne sont pas un bug technique, elles traduisent une **carence de volatilité ou un seuil de sensibilité mal calibré**. Ce n'est pas le signe d'un crash, mais d'un système qui rate du flux exploitable en restant aveugle en-dessous de certains seuils.
* **S1-3. Le filtre `wall_not_collapsed` rejette-t-il trop ?**
  * *Comportement voulu, mais potentiellement trop restrictif.* Il protège contre les fausses cassures, mais bloquer des tensions à 0.97 (proche du sommet) suggère un seuil de validation du mur binaire ou trop rigide. À ajuster avec une pente de tolérance plutôt qu'un mur binaire.
* **S1-4. Amélioration GO-sized (Sujet 1) :**
  * Implanter un **Dynamic Deadzone Adjuster** : si >20 cycles consécutifs tombent à `momentum_too_small`, baisser automatiquement le plancher de sensibilité de 15% pour forcer le radar à capter le micro-momentum.

---

### SUJET 2 — CHAÎNE D'APPROBATION PAR PROMPTS

* **S2-1. Verdict sur la proposition :** GO AVEC RÉSERVES.
  * *Raison :* Structurer et graver les prompts dans le double dépôt (Obsidian + Akash) est indispensable pour tuer l'improvisation, mais le catalogue risque de créer de la bureaucratie si les gates prennent trop de temps en live.
* **S2-2. Ce qui manque / corrections dans P1–P4 :**
  * *Manque :* Une **procédure de rollback d'urgence** (Kill Switch) intégrée directement dans le prompt P1 (si divergence de cockpit, arrêt immédiat sans passer par 12 validations).
* **S2-3. Amélioration concrète de la chaîne (GO-sized) :**
  * **Atomisation des rôles :** Formaliser la règle *Maker ≠ Checker* par un hash cryptographique ou un tag obligatoire dans le commit Akash/Obsidian (le compte qui valide ne peut pas être celui qui a généré le code/la spec).
