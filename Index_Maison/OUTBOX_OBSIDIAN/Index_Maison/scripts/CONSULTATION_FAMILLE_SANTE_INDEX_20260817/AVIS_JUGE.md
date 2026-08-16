# AVIS JUGE (task juge.tranche, provider NVIDIA build.nvidia.com (100+ modeles), 70.2s)

**VERDICT : GO-AVEC-RÉSERVES**  
**CONFIANCE : 78 %**

---

**1. VERDICT**  
GO sur la conception (maillon par maillon + cockpit + plist 5 min). C'est exactement ce qui manquait : la veilleuse vérifie l'intégrité, pas la traversée. La chaîne BALEINES est le cas d'école qui justifie ce pré-vol.

**2. LES 6 CHAÎNES — manques et défauts**
- **MANQUE CRITIQUE : chaîne HUB LLM** (providers → routage → réponse). Si le hub tombe ou route mal, tout le système décisionnel est aveugle — et rien ne le montre aujourd'hui. À ajouter.
- **MANQUE : chaîne GIT PUSH AUTO** (commit → push → registre). Un push silencieusement cassé = perte d'historique sans alerte.
- **SAISON (6 indices)** : trop laxiste si le seuil d'âge est > 15 min sur un marché actif. Un indice figé pendant 30 min sur du CALME est normal, mais sur du VOLATIL c'est un faux négatif.
- **CPFP (observation 7j)** : chaîne trop longue pour un pré-vol « santé ». Elle mesure une tendance, pas une santé. À sortir du panneau principal.

**3. FAUX POSITIFS / FAUX NÉGATIFS**
- **Faux positif** : fichier append-only vide sur marché calme (BETA sonde peu → CSV quasi vide → crié rouge à tort). Seuil d'âge doit être adapté à la saison.
- **Faux négatif** : process vivant mais avec un label différent (ex. `python3` vs `python`) → maillon déclaré mort alors qu'il tourne. Vérifier par port/pid, pas par nom.
- **Faux négatif** : fichier frais mais vide (le scan tourne, écrit, mais ne produit rien) — la fraîcheur seule ne prouve pas la donnée.

**4. ALERTE VOCALE — pertinente mais à escalader**
- Pertinente pour les chaînes critiques (BALEINES, HULK, LIVE), pas pour SAISON.
- **Escalade proposée** : log (1er échec) → carte rouge cockpit (2e échec consécutif) → voix (3e échec consécutif ou chaîne critique). Évite de crier pour un maillon transitoire.
- Sur-alerte réelle si un seul échec déclenche la voix. Imposer 2 échecs consécutifs minimum.

**5. AMÉLIORATION PROPOSÉE (clause permanente)**
**Ajouter un « test de traversée » actif** : toutes les 5 min, injecter un jeton de test (ex. `ping-{timestamp}`) dans la source de chaque chaîne et vérifier qu'il arrive chez le consommateur final. Ça prouve la traversée réelle, pas juste la fraîcheur des fichiers. Coût : quasi nul (un champ JSON), bénéfice : détecte les ponts morts en 5 min, pas en 24 h.

---

**HYPOTHÈSES**
1. Les plists 5 min sont correctement configurées et surveillées par la veilleuse.
2. Les seuils d'âge sont adaptables par chaîne et par saison.
3. Le cockpit est accessible à Ada/Cortana pour voir la carte 🩺.

**CE QUI CHANGERAIT L'AVIS**
- Preuve que le test de traversée est impossible techniquement (coût > bénéfice).
- Découverte que les plists 5 min ne survivent pas à un redémarrage.
- Un faux négatif avéré sur une chaîne critique en conditions réelles.

**SYNTHÈSE**  
Pré-vol solide, direction juste. Manque la chaîne HUB LLM (critique) et le test de traversée actif. Escalade voix à 3 échecs consécutifs pour éviter le sur-alarme. Seuils d'âge à rendre sensibles à la saison. GO avec réserves — les réserves sont levables en une itération.
