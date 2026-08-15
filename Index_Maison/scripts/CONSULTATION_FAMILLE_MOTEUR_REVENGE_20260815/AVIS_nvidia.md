# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 122.6s)

**ANALYSE**

**1. Technique**  
Le couple `shock_inversion_stop` (~80% des exits) + `revenge 1.5x` forme une **boucle mécanique** : BETA est stoppé sur choc d'inversion → ALPHA ré-entre à 1.5x → subit le même choc (marché directionnel) → re-stoppé → re-revanche. Les chiffres montrent une **volatilité extrême** du PnL revenge (+51 le 14, -3.6 le 13) sans edge stable. Le %revenge croissant (58→89%) indique une **dérive comportementale** : le système devient un "machine à churn" plutôt qu'une stratégie discriminante. Le PnL normal est positif sur 2 jours sur 3 (sauf le 15, faible échantillon n=9), tandis que le revenge est négatif 2 jours sur 3. **Conclusion : le revenge est net négatif ou neutre, pas un edge.**

**2. Risque/Impact**  
Pour trancher, il manque :  
- **PnL par séquence complète** (scout → hunter → résultat final) et non par fill isolé.  
- **Frais cumulés** (taker fees × 2 par cycle) — probablement 50-70% du PnL brut.  
- **Hold moyen revenge vs normal** (si revenge tient plus longtemps, risque de gap).  
- **Corrélation entre shock_inversion_stop et la direction du marché** (si le stop est systématiquement du mauvais côté, le revenge amplifie une erreur systématique).

**3. Priorité**  
**OUI, infra d'abord.** E-STALE 1032 (feed lag 8-12s) et E-PROC 75 (morts de process) faussent les données de tension et les décisions. Un bot qui skippe 1032 fois ou meurt 75 fois ne peut pas valider une stratégie. Le revenge est un **problème de design**, mais l'infra est un **prérequis de fiabilité**. Corriger l'infra avant de toucher au revenge.

---

**VERDICT** : Ouvrir un chantier correctif **en deux temps** : (1) **infra/feed** (E-STALE, E-PROC) en priorité absolue, (2) **désactiver ou plafonner le revenge** (max 1x, ou le limiter aux seuls cas où le scout a tenu > X secondes) après validation sur données corrigées.

**CONFIANCE** : 78%

**HYPOTHÈSES** :  
- Le shock_inversion_stop est un signal de **retournement violent** → le revenge 1.5x entre dans le sens opposé au momentum, donc perdant en moyenne.  
- Les frais de taker (0.1% × 2) sur ~80 fills/jour érodent 15-20% du PnL brut.  
- Le feed lag (E-STALE) a faussé les stops (entrées/sorties retardées) → les chiffres des 4 jours sont partiellement invalides.

**CE QUI CHANGERAIT L'AVIS** :  
- Si le PnL par séquence (scout+hunter) montre un **edge net positif** après déduction des frais, le revenge est justifié → priorité infra seule.  
- Si E-STALE revient à 0 et que le revenge reste négatif sur 5 jours, alors **désactivation définitive**.

**AMÉLIORATION PROPOSÉE** :  
1. **Désactiver le revenge** pendant 3 jours (mode observation pure) pour mesurer le PnL scout seul.  
2. **Ajouter un compteur de séquences** (scout → hunter → résultat) et un **calcul de frais cumulés** dans les CSV.  
3. **Augmenter la gate E-STALE** à 1500ms (au lieu de 800ms) pour réduire les skips, et **superviser les process** (restart auto).

---

**SYNTHÈSE** : Le revenge est une boucle de churn sans edge stable (PnL volatil, %revenge croissant). L'infra (E-STALE 1032, E-PROC 75) invalide les données actuelles. **Ordre : 1) corriger feed/process, 2) désactiver revenge temporairement, 3) re-mesurer sur 5 jours avec frais et séquences.**
