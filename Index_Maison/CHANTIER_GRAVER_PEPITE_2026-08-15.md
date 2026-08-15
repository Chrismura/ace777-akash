# CHANTIER — GRAVER LA PÉPITE (15/08/2026 soir)

**Statut :** ✅ LIVRÉ + TESTÉ (options A et B)
**Décision :** GO Christophe (voix, pendant le dîner) · Famille GO-AVEC-RÉSERVE (92/78%)
**But :** que Cortana connaisse la pépite CPFP **demain**, sans qu'on ait à la lui re-injecter.

---

## Le problème (limite du système)

Cortana n'a **aucune mémoire entre deux appels** (stateless). La pépite CPFP lui avait été
révélée dans une question ponctuelle → aujourd'hui elle la connaît, **demain elle a oublié**.

## La solution (2 options, A puis B — ordre famille)

### OPTION A — gravée dans le prompt canon ✅
- Section `<knowledge_base> INSTRUCTION PERMANENTE — CONNAISSANCE ONCHAIN v1 (15/08/2026)`
  ajoutée dans `PROMPT_MASTER_ANALYSTE.md` (les 2 copies : vault Obsidian + scripts/prompts/).
- Version **condensée** (famille) : le mécanisme UTXO+CPFP en résumé + le signal fiable
  (z-score adaptatif + signature CPFP par frais) + la lecture (« préparation imminente »).
- **Test décisif** : question posée à Cortana SANS aucun brief → elle a expliqué le mécanisme
  exact et cité le signal « z-score adaptatif croisé avec la signature CPFP » d'elle-même. ✅

### OPTION B — couche connaissance en auto ✅
- `contexte_systeme()` dans `cortana_analyse.py` : injecte maintenant les fiches de
  `CONNAISSANCE_PROJETS.json` automatiquement (via `injecter_connaissance`).
- **Garde-fous famille respectés** : synthèse pré-mâchée (jamais de chiffres bruts),
  plafond 3 fiches/analyse, filtre par sujet (fallback rotation), mode observation.
- **Test** : `INDICE_COURANT=CCUSDT` → la fiche Canton (thèse + verdict) injectée dans le prompt. ✅

## Garde-fous famille (condition du GO)

1. **Non-régression** : si justesse Cortana <40% ou baisse >5pts sur 20 analyses → retrait de la section
2. **Versionnement** : pépite tracée (cette consignation + mémoire + git)
3. **Horodatage** : `v1 (15/08/2026)` dans la balise → revue périodique
4. **B en pilote** : observation seule, retour manuel si confusion manifeste

## Réversibilité

- **Option A** : retirer la balise `<knowledge_base>...</knowledge_base>` du prompt (2 copies)
- **Option B** : retirer le bloc « Couche connaissance AUTO » dans `contexte_systeme()`
- **Registre** : `git checkout` des fichiers + restauration md5

## Fichiers touchés

| Fichier | Action |
|---|---|
| `~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md` | ✏️ section connaissance onchain v1 |
| `Index_Maison/scripts/prompts/PROMPT_MASTER_ANALYSTE.md` | ✏️ idem (copie lue en premier) |
| `Index_Maison/scripts/cortana_analyse.py` | ✏️ option B (contexte_systeme) |
| `Index_Maison/strategie/REGISTRE_SYNAPSES.json` | ✏️ v1.2.0 (20 items, prompt indexé) |

## Tests effectués

| Test | Résultat |
|---|---|
| Prompt lu contient CPFP + knowledge_base (A) | ✅ |
| Cortana SANS brief explique le mécanisme + le signal | ✅ (test décisif) |
| Connaissance Canton injectée en auto (B) | ✅ |
| Analyse réelle hub (onchain) : fonctionne, structure complète | ✅ |
| build_facts / load_system_prompt : pas de régression | ✅ |
| Veilleuse : rc=0 état sain | ✅ |

## À noter (non bloquant)

- Artefact observé : « soixante-qu十四 cents » (caractère chinois parasite) dans la lecture
  des nombres en toutes lettres par le modèle — bug de sortie Gemini, pas de notre code.
- Prochain chantier possible : registre des leçons (chaque HIT/MISS alimente une fiche avec
  tag « onchain » — amélioration famille nvidia) + test de non-régression automatique.
