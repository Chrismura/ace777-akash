# Avis nvidia — graver la pépite (provider NVIDIA build.nvidia.com (100+ modeles), 43.8s)

**VERDICT : GO-AVEC-RÉSERVE** (Option A immédiate, Option B en pilote contrôlé)

**CONFIANCE : 78 %**

---

**RÉPONSES AUX QUESTIONS**

**Q1 — A seule, B seule, ou A PUIS B ?**
**A PUIS B.** A est un filet de sécurité immédiat (gravé dans le canon, garanti à chaque analyse). B est la vraie solution mais elle exige un pilote contrôlé pour ne pas noyer Cortana. Ordre : A maintenant, B en parallèle avec métriques de non-régression.

**Q2 — Pour A, version complète ou condensée ?**
**Condensée (b)**. Le prompt canon doit rester un squelette de raisonnement, pas une encyclopédie. 5 points complets = risque de dilution des priorités. La version condensée : le principe (UTXO indivisible → arbre de poussière → CPFP) + le signal (z-score adaptatif, pas de seuil fixe). Les détails opérationnels vont dans la couche connaissance (B).

**Q3 — Risques d'une section permanente ?**
- **Dérive** : le prompt devient un fourre-tout. Atténuation : section balisée `[CONNAISSANCE ONCHAIN — v1]`, révision trimestrielle obligatoire.
- **Longueur** : +15 lignes max, sinon on perd la focalisation. Atténuation : version condensée (Q2).
- **Confusion données/instructions** : Cortana pourrait traiter la section comme une donnée d'entrée. Atténuation : préfixe `INSTRUCTION PERMANENTE —` et test de non-régression sur 10 analyses connues.

**Q4 — Pour B, éviter l'infobésité à 44 % de justesse ?**
- **Synthèse pré-mâchée obligatoire** : jamais de chiffres bruts, uniquement des conclusions actionnables (« ce projet a un historique de faux positifs → méfiance »).
- **Filtre par pertinence stricte** : injection uniquement si le sujet de l'analyse matche un tag de la fiche (pas de fuzzy matching).
- **Plafond de 3 fiches par analyse** : au-delà, on ne charge rien (évite la surcharge cognitive).

---

**HYPOTHÈSES**
1. La justesse de 44 % est due à un manque de contexte, pas à un défaut structurel du raisonnement de Cortana.
2. Le mécanisme CPFP est stable et ne changera pas fondamentalement dans les 6 prochains mois.
3. L'injection automatique peut être testée en mode « observation seule » sans dégrader les performances actuelles.

---

**CE QUI CHANGERAIT L'AVIS**
- **Preuve de non-régression** : si après A, les scores de justesse baissent de plus de 5 points sur 20 analyses, on retire la section.
- **Échec du pilote B** : si l'injection auto provoque une confusion manifeste (ex. Cortana cite des fiches non pertinentes), on repasse en manuel.
- **Découverte d'un mécanisme alternatif** : si un autre schéma d'évasion onchain émerge, la section A devient obsolète et doit être révisée.

---

**AMÉLIORATIONS PROPOSÉES**
1. **Ajouter un test de non-régression automatique** : après chaque modification du prompt canon, rejouer 10 analyses historiques et comparer les scores.
2. **Créer un registre des leçons apprises** : chaque HIT/MISS de Cortana alimente une fiche dans CONNAISSANCE_PROJETS.json, avec tag « onchain » pour B.
3. **Horodater la section A** : `[CONNAISSANCE ONCHAIN — v1 — 15/08/2026]` pour forcer la revue périodique et éviter la fossilisation.
