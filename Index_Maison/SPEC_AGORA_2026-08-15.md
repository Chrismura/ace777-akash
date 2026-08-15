# SPEC — AGORA : canaliser la connaissance ACE777 (15/08/2026)

**Statut :** approuvée famille (GO-AVEC-RÉSERVE gemini 91% / nvidia 82%) + GO Christophe
**Supervision :** Buffy · **Codeur :** à exécuter

---

## 1. Vision

Une **place centrale** où toute la connaissance ACE777 converge (agora), puis se diffuse
vers les bons acteurs dans **leur langue** :
- **Cortana** (cerveau qui LIT) → synthèses **textuelles** pré-mâchées
- **Ada** (gardienne qui CALCULE) → **valeurs chiffrées** validées (jamais de texte)

**Légèreté :** 1 fichier JSON + scripts stdlib. PAS de base de données (SQLite seulement
si >500 fiches ou >5 Mo — famille).

## 2. Ce qui existe déjà (à NE PAS casser)

| Brique | Fichier | État |
|---|---|---|
| Place centrale | `strategie/CONNAISSANCE_PROJETS.json` | ✅ |
| Collecteur | `scripts/construire_connaissance.py` | ✅ |
| Injecteur | `scripts/injecter_connaissance.py` | ✅ |
| Option A (pépite gravée) | `PROMPT_MASTER_ANALYSTE.md` section `<knowledge_base>` | ✅ |
| Option B (injection auto) | `cortana_analyse.py` `contexte_systeme()` | ✅ |
| Ada valeurs | `ada_gardienne.py` modulateurs (onchain ±10%, CPFP −7%) | ✅ |
| HIT/MISS calculés | `score_justesse.py` + `justesse_v2.json` | ✅ (mais NON réinjectés) |

## 3. LIVRABLE 1 — `scripts/lecons_auto.py` (NOUVEAU) — la boucle E4

**Rôle :** chaque analyse notée de Cortana (HIT/MISS/FLAT par indice) devient une **leçon
actionnable** dans la base. Boucle : erreur → leçon → réinjectée → moins d'erreurs.

### 3.1 Entrée (source de vérité)
- `strategie/justesse_v2.json` : `par_indice` (hit/n par indice) + `pct` global.
- Historique des analyses notées (dossier analyses / history).

### 3.2 Format de leçon (famille — axiome ≤20 mots)
```
[indice] → [constat] → [action recommandée]
```
Exemples :
- `funding → positif mais 7/20 de fiabilité → corroborer avec fearGreed avant LONG`
- `fearGreed → extrême 6/18 → méfiance, souvent contre-signal`
- `onchain → nouveau signal v2 → le z-score adaptatif est le signal fiable, pas les seuils fixes`

**PAS de chiffres bruts dans la fiche injectée** (seulement dans le staging pour la décision).

### 3.3 Staging + validation en 2 temps (nvidia)
1. `lecons_auto.py --scan` écrit dans **`strategie/lecons_brutes.json`** (STAGING) :
   les constats bruts par indice avec leur taux (hit/n), classés par fiabilité.
2. La **discipline 07h15** (après la note Cortana) appelle `lecons_auto.py --valider` :
   fusionne dans `CONNAISSANCE_PROJETS.json` sous une section `lecons_agora` les axiomes
   qui passent les seuils (ex. n ≥ 5 analyses, fiabilité < 70% = leçon « corroborer »,
   fiabilité > 75% = leçon « confiance »). Jamais de bruit non relu.

### 3.4 TTL (gemini)
- Les leçons HIT/MISS ont un **TTL de 7 jours** avant validation en « règle structurelle »
  (champ `ttl_expire`). Une leçon contradictoire ne pollue pas : elle expire.

### 3.5 Cadence
- Quotidienne, déclenchée par la discipline 07h15 **APRÈS** la note de Cortana (jamais avant).

## 4. LIVRABLE 2 — `CONNAISSANCE_PROJETS.json` (MODIF schéma)

Ajouter au schéma (famille — cloisonnement strict) :
- **`namespace`** OBLIGATOIRE : `"cortana"` (texte) ou `"ada"` (chiffres) — chaque entrée.
- Section **`lecons_agora`** : les axiomes validés (avec `indice`, `ttl_expire`, `source: HIT/MISS`).
- **`parametres_ada`** : uniquement des floats/int validés par la famille (ex.
  `facteur_onchain_outflow: 0.93`) — **Ada ne lit JAMAIS les leçons textuelles de Cortana**.

## 5. LIVRABLE 3 — Sorties (2 langues, cloisonnées)

- **Cortana** : `contexte_systeme()` (déjà branché) injecte les leçons de `lecons_agora`
  pertinentes (≤3, synthèse pré-mâchée) — MODIF MINIMALE pour ajouter les leçons aux fiches.
- **Ada** : `ada_gardienne.py` (INCHANGÉ) — elle consomme déjà les modulateurs via live.json
  (valeurs validées famille). **AUCUN texte de Cortana ne doit entrer dans Ada** (famille).

## 6. LIVRABLE 4 — Métrique A/B (mesure que l'AGORA fonctionne)

- Moyenne mobile 7j du `pct` de justesse vs baseline historique.
- Comparaison 30 jours AVANT vs APRÈS activation E4 (même périmètre d'indices).
- Rapport dans `thermo/SANTE_CONNAISSANCE.md` + `DISCIPLINE_QUOTIDIENNE.md`.

## 7. RÈGLES DE CODE ACE777

- Python 3.9+, stdlib uniquement, UTF-8, docstring de rôle.
- Écriture atomique (mkstemp + os.replace), kill-switch (strategie/STOP + STOP_ALL).
- Robustesse (jamais de crash si fichier manquant/corrompu), idempotence.
- **NE PAS toucher** au moteur Hulk (paper_diprip.py), ni à ada_gardienne.py (sauf si spec l'exige).
- `lecons_auto.py --valider` ne fusionne que si `justesse_v2.json` existe et est frais.

## 8. FORMAT DE RÉPONSE EXIGÉ DU CODEUR

- Blocs ```python complets et fermés, précédés du chemin.
- Pour les MODIFS (cortana_analyse.py, construire_connaissance.py) : ```diff EXACT.
- Une section « NOTES » finale : choix faits, points d'attention. Français, factuel.

## 9. CRITÈRES DE TEST (supervision)

1. `lecons_auto.py --scan` : écrit `lecons_brutes.json` (staging) sans toucher à la base.
2. `--valider` : fusionne les axiomes éligibles (n≥5, fiabilité seuils), respecte le TTL 7j.
3. Axiome formaté `[indice] → [constat] → [action]`, ≤20 mots, PAS de chiffres bruts.
4. Cloisonnement : les leçons sont namespace `cortana`, `parametres_ada` = valeurs seules.
5. Cortana reçoit les leçons (test réel hub) sans brouillage (structure complète).
6. Idempotence : 2 runs successifs → pas de doublons.
7. La discipline 07h15 reste fonctionnelle (les tests existants passent).
