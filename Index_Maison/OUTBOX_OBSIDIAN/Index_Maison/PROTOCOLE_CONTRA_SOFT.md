# Protocole CONTRA soft — chat → prototype Index

**Statut :** évolutif (garder si utile, sinon rayer).  
**Source idée :** [[Evaluations/15_n01ennn_contrarian_vault]] (@N01ennn) — on ne copie **pas** le cron 6 h.  
**Pour :** cold-path (Cursor / Punk / Gemini) + Christophe.  
**Pas pour :** lancer ACE/Hulk, modifier champion, auto-merge.

---

## 1 — But
Empêcher de **répéter** les mêmes erreurs / décisions sans les voir.  
Le vault (Index) doit parfois **te contredire** avec *tes* notes — pas inventer une strat.

---

## 2 — Déroulement d’un chat cold-path (ordre)

```text
1. LIEN / idée reçue
2. PROTOCOLE_LIENS → LU_COMPLET | LU_PARTIEL | BLOQUÉ
3. BRIEF_IA_SNIFF → pertinent Index ? sinon stop (bruit)
4. Essence 5–10 lignes + verdict (GARDÉ / WATCH / REFUS / JETÉ)
5. Si GARDÉ ou WATCH utile :
   a. Éval #N (ou MAJ éval existante)
   b. 1 ligne 01_TABLEAU_VIVANT (+ journal décisions)
   c. 1 ligne MEMOIRE_COLLAB
   d. Option Attention si Christophe doit trancher
6. Si la note porte une thèse forte → ajouter claim + assumption (voir §3)
7. Proposer (1 ligne) : « Stack / Pass 2 CONTRA ? » — SANS lancer
8. STOP. Humain dit GO si pass CONTRA ou sync Obsidian
```

**Règle :** le chat **propose** ; le coffre **décide** (après écriture). Chat ≠ loi ([[COUTUMES_AGORA]]).

---

## 3 — Frontmatter minimal (Loop 1 soft)

Sur une note **qui compte** (éval, décision, Attention PERTINENT) — pas sur chaque tweet :

```yaml
---
claim: ce que la note affirme en 1 phrase
assumption: ce qui doit être vrai pour que claim tienne
ready_for_contra: false
---
```

- Si `assumption` floue → laisser vide + flag « revue humaine ».  
- Ne pas backfiller tout l’historique d’un coup (3 semaines d’habitude chez N01ennn → chez nous : **au fil de l’eau**).

---

## 4 — Pass 2 manuel (seul pass prioritaire)

**Quand :** mot `GO contra` · ou fin de session veille · ou doute « on s’est déjà contredit ».  
**Où écrire :** `Index_Maison/CONTRA.md` (append).

Pour chaque collision :
1. Note A `claim` vs note B `assumption` (ou l’inverse)
2. **Quotes** des deux notes (pas de résumé flou)
3. Humain décide : garder les deux (contextes différents) · noter la leçon · **jamais auto-merge**

Passes **non** planifiées pour l’instant :
- Pass 1 steelman random — seulement si Christophe demande
- Pass 3 bridges — curiosité
- Pass 4 ghost — lire `ERREURS_AI/` + journal ; pas de cron

---

## 5 — Amélioration du prototype (ce qu’on accepte)

| OK évolutif | Pas OK |
|-------------|--------|
| Nouvelle ligne tableau / S13 | Cron LLM 6 h |
| Éval + Attention | Install plugin / service cloud |
| CONTRA.md append manuel | Réécrire champion / genesis |
| claim/assumption sur 1–3 notes/semaine | Gonfler vault avec `*-contra.md` auto |
| Sync OUTBOX après écriture | GO trading implicite |

Preuve que ça marche : **une** collision utile qui évite une bêtise (ex. fee 0 % vs S10) → alors on garde S13.  
Si les Pass 2 ne surprennent jamais → **rayer** S13 (mode évolutif).

---

## 6 — Mots magiques

| Mot | Effet |
|-----|--------|
| `GO contra` | 1 Pass 2 manuel (cold-path lit claim/assumption récents → append CONTRA.md) |
| `LIS CA` + collage | Priorité lecture complète ([[PROTOCOLE_LIENS]]) |
| `COMPLETE #15` | Compléter l’éval avec collage si trou |

---

## Fichiers liés
- [[BRIEF_IA_SNIFF]] · [[PROTOCOLE_LIENS]] · [[01_TABLEAU_VIVANT]] · [[COUTUMES_AGORA]]  
- [[Evaluations/15_n01ennn_contrarian_vault]] · `CONTRA.md`
