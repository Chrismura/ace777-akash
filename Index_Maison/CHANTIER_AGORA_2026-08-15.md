# CHANTIER — AGORA : canaliser la connaissance (15/08/2026 soir)

**Statut :** ✅ LIVRÉ + TESTÉ
**Décision :** GO Christophe (voix, au fourneau) · Famille GO-AVEC-RÉSERVE (91/82%)
**Idée :** Christophe — « un système agora pour canaliser la connaissance »

---

## La vision

Une **place centrale** où toute la connaissance converge, puis se diffuse vers les bons
acteurs **dans leur langue** :
- **Cortana** (cerveau qui LIT) → synthèses textuelles pré-mâchées
- **Ada** (gardienne qui CALCULE) → valeurs chiffrées validées (jamais de texte)

**Légèreté :** 1 fichier JSON + scripts stdlib. SQLite seulement si >500 fiches/5 Mo (famille).

## Ce qui a été fait

### La place (déjà là) + la boucle E4 (NOUVELLE — la pièce manquante)
| Pièce | État |
|---|---|
| Place centrale `CONNAISSANCE_PROJETS.json` | ✅ existant |
| Collecteur `construire_connaissance.py` | ✅ existant |
| Injecteur `injecter_connaissance.py` | ✅ existant |
| Option A (pépite gravée) + Option B (injection auto) | ✅ ce soir |
| **Boucle E4 `lecons_auto.py`** | ✅ **NOUVEAU** |

### Boucle E4 — chaque erreur devient une leçon
1. `--scan` : lit `justesse_v2.json` (HIT/MISS par indice) → staging `lecons_brutes.json`
2. `--valider` : axiomes `[indice] → [constat] → [action]` (≤20 mots, PAS de chiffres
   bruts), seuils (n≥5 ; <70% → « corroborer » ; >75% → « confiance »), TTL 7 jours,
   namespace `cortana`, fusion idempotente dans la base
3. Branché dans la discipline 07h15 (APRÈS la note Cortana — jamais avant, nvidia)
4. `contexte_systeme()` (cortana_analyse.py) injecte les leçons actives (≤3, pré-mâchées)

### Cloisonnement (famille — strict)
- `namespace: "cortana"` pour les leçons textuelles
- Ada **ne lit JAMAIS** les leçons de Cortana — ses modulateurs viennent des audits
  famille via live.json (inchangé)

## Résultats réels (la preuve que l'AGORA vit)

1. **4 leçons créées depuis les vraies données** : funding 38%, fearGreed 37%, btc 38%,
   radar 52% — toutes < 70% → « corroborer avec un autre indice avant de te positionner »
2. **Idempotence** : 2e run → 0 doublon, 4 actives
3. **Test de bout en bout (hub réel)** : analysant funding, Cortana a écrit :
   « *Compte tenu de mes précédents échecs sur cet indice en interprétant trop vite un
   financement positif comme un signal d'achat* » → **AVIS NEUTRE** au lieu de LONG.
   **Elle a lu sa leçon et en a tiré la conséquence.**

## Garde-fous famille (respectés)

- ✅ Namespace obligatoire (cortana/ada)
- ✅ TTL 7 jours sur les leçons
- ✅ Staging + validation en 2 temps (jamais de bruit non relu)
- ✅ Ada cloisonnée (jamais de leçons Cortana → modulateurs)
- ✅ Métrique : moyenne mobile 7j du pct + comparaison 30j avant/après E4

## Réversibilité

- Retirer le bloc « 1d) AGORA » dans `discipline_quotidienne.py`
- Retirer la section « 6) LEÇONS AGORA » dans `cortana_analyse.py`
- `rm strategie/lecons_brutes.json` + retirer `lecons_agora` de la base
- `rm scripts/lecons_auto.py`

## Fichiers touchés

| Fichier | Action |
|---|---|
| `Index_Maison/scripts/lecons_auto.py` | ➕ NOUVEAU (boucle E4) |
| `Index_Maison/scripts/discipline_quotidienne.py` | ✏️ hook AGORA (après la note) |
| `Index_Maison/scripts/cortana_analyse.py` | ✏️ injection des leçons (≤3) |
| `Index_Maison/strategie/CONNAISSANCE_PROJETS.json` | ✏️ section `lecons_agora` (4 leçons) |
| `Index_Maison/strategie/lecons_brutes.json` | ➕ staging |

## À noter

- Le codeur a encore fait 2 erreurs (chemin `CONNAISSANCE_PROJETS.json` faux, diff
  inventé `contexte`/`datetime`) → corrigées par la supervision.
- Erreur de supervision aussi : `justesse_v2.json` est dans `scripts/`, pas `strategie/`
  → corrigé en test (le scan écrivait 0 constats).
