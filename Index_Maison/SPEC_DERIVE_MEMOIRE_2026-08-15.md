# SPEC — Dérive mémoire (4 indicateurs @0xWast3) — 15/08/2026

**Chantier 2** (ordre famille validé : gemini 85% + nvidia 72%, consensus sur cette piste).
**Origine** : signet N°1 @0xWast3 — un système de mémoire qui surveille SA PROPRE santé : au lieu de stocker des faits à plat sans signal de vieillissement, 4 indicateurs détectent quand une connaissance devient obsolète AVANT qu'elle ne pollue les décisions.

**Principe ACE777** : Cortana est à 44% (F1). La discipline quotidienne (launchd 07h15) la note chaque jour. Ce chantier ajoute la couche **santé de la mémoire** : on surveille la QUALITÉ de ce qu'elle sait, indice par indice, pour détecter les règles périmées avant qu'elles ne fassent des dégâts. **Lecture seule — ne touche ni au moteur, ni au genesis, ni aux analyses. Aucun ordre.**

---

## Fichier à créer : `Index_Maison/scripts/derive_memoire.py`

Script autonome Python 3 (stdlib uniquement, comme le reste du projet — 0 dépendance, 0 API payante). Lisible depuis `~/ace777-test-day1`.

### Données d'entrée (lecture seule)
1. **Analyses Cortana** : `Index_Maison/thermo/analyses/*.jsonl` (93 lignes à ce jour, une par analyse). Chaque ligne : `ts`, `indice` (ex. "radar", "funding", "fearGreed"…), `analyse` (texte contenant `AVIS STRICT : LONG|SHORT|NEUTRE`, `HORIZON : 24h`, `CONFIANCE : faible|moyenne|haute`).
2. **Justesse** : `Index_Maison/scripts/justesse_v2.json` — `pct` global, `par_indice` (hit/n/neutre par indice), `derniere`.
3. **Journal Ada** : `Index_Maison/strategie/ada_gardienne_historique.jsonl` (facultatif — signal zone).

### Les 4 indicateurs (définition ACE777 concrète)

**I1. Fréquence de référence** — un savoir qu'on n'utilise plus meurt.
- Par indice : nombre d'analyses sur les 14 derniers jours / nombre de jours où l'indice a été analysé.
- **Dérive** : indice avec ≥7 jours sans analyse → « froid » (sa connaissance se dégrade). ≤2 analyses sur 14 jours → « sous-utilisé ».

**I2. Taux de contradiction** — un savoir qui se contredit souvent est instable.
- Par indice : pour chaque paire d'analyses SUCCESSIVES du même indice, comparer l'avis strict (LONG/SHORT/NEUTRE). Contradiction = LONG↔SHORT (retournement) OU même avis mais inverse de la vérité connue.
- Comptage simple : sur l'historique de l'indice, `nb_retournements / (nb_analyses - 1)` où retournement = avis ≠ avis précédent avec au moins un LONG ou SHORT impliqué (NEUTRE→NEUTRE ne compte pas).
- **Dérive** : taux > 50% → l'indice « flip-flop » → instable, à flagger.

**I3. Vitesse de décroissance** — une connaissance non révisée se périme.
- Par indice : âge de la dernière analyse (jours). 
- **Dérive** : > 7 jours → périmée. > 14 jours → critique (la connaissance date).

**I4. Dispersion de confiance** — la confiance doit refléter la justesse.
- Par indice : comparer la confiance déclarée (faible/moyenne/haute) au statut réel (HIT/MISS du scoreur).
- Extraction : reprendre `justesse_v2.json > par_indice` + les `analyse` récentes. **Score de calibration** : `justesse_sur_haute_confiance - justesse_sur_faible_confiance`.
- **Dérive** : si la justesse sur confiance HAUTE ≤ justesse sur confiance FAIBLE → « confiance déconnectée de la réalité » (elle est confiante à tort) → flag critique.

### Sortie
1. **Rapport** : `Index_Maison/thermo/DERIVE_MEMOIRE.md` (même style que DISCIPLINE_QUOTIDIENNE.md) :
   - Tableau par indice : `| indice | n_analyses | I1 fréquence | I2 contradiction | I3 âge | I4 calibration | statut |`
   - `statut` : STABLE / FROID / INSTABLE / PÉRIMÉ / CRITIQUE (le pire des 4 indicateurs déclencheurs).
   - **Alerte** : liste des indices « instables » (flip-flop) et « critiques » (confiance déconnectée).
   - Synthèse 3 lignes : la mémoire globale est-elle saine ?
2. **Fichier JSON** : `Index_Maison/strategie/derive_memoire.json` (pour traçabilité/API) : `{ts, global: {indices_instables: n, indices_critiques: n, note}, par_indice: {...}}`.
3. **Exit code** : `0` = sain · `1` = au moins 1 indice INSTABLE · `2` = au moins 1 indice CRITIQUE (utilisé par la boucle pour alerter).

### Branchement dans `discipline_quotidienne.py` (modification MINIMALE)
- Après l'étape 1 (re-note Cortana), exécuter `derive_memoire.py` (subprocess, timeout 60s, fail-open si erreur : la discipline continue).
- Si exit code ≥ 1 → ajouter une alerte dans DISCIPLINE_ALERT.md : `DÉRIVE MÉMOIRE : N indice(s) instable(s) / M critique(s) — voir DERIVE_MEMOIRE.md`.
- Ajouter une section « ## MÉMOIRE (dérive) » au rapport avec le statut global.

### Contraintes
- Stdlib uniquement, français, commenté, pas de dépendance réseau (les données sont locales).
- Ne MODIFIE JAMAIS : analyses/*.jsonl, justesse_v2.json, ada journal, moteur, genesis.
- Réversible : suppression du script + de la ligne d'appel = retour à l'état d'avant.
- Tolérant aux fichiers absents/corrompus (chaque fichier lu dans un try/except, on continue).

### Format de sortie attendu du codeur
Le code EXACT du nouveau fichier `derive_memoire.py` + le diff EXACT des 2 modifications dans `discipline_quotidienne.py` (ligne d'appel + section rapport). Zéro réécriture d'autre chose.
