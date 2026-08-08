# Protocole Voie A — Validation pattern V8 (paper / testnet)

**Statut :** 🔵 WATCH · prêt si GO Christophe  
**But :** valider le pattern **Radar → Fenêtre → Mur → Aspiration/SKIP** — pas la Bassine 1.437, pas le manifeste.  
**Environnement :** paper ou testnet **uniquement** (pas de live implicite).

---

## 1. Pourquoi ça vaut le coup (avis)

Oui : c’est le seul endroit où tu as déjà **capteur + action + fills**.  
Si le pattern ne bat pas un témoin ici, le mythe ailleurs ne le sauvera pas.  
Si il bat le témoin → valeur **réelle** mesurée.

---

## 2. Pack figé AVANT le run (ne pas toucher pendant le test)

| Param | Pack PATTERN (A) | Pack TÉMOIN (B) |
|-------|------------------|-----------------|
| radar / filter | **0.85** | 0.70 (plus permissif) ou OFF |
| impulse / MOM | **0.96** | 0.70 |
| wall_drop | **6.5%** | 16% (mur « facile ») ou ignore mur |
| dt_ms | **128** | 128 (même cadence) |
| aspiration | 1.618 @ 37.8° | size fixe 1.0 (sans φ) |
| void_lock | **ON** | OFF |
| durée | **même** (ex. 4 h) | **même** |
| marché / jambe | **identique** | **identique** |

Une seule variable d’intérêt : **sévérité du filtre** (A strict vs B lâche).

---

## 3. Grille de score (colonnes à logger)

Remplir **par jambe** (BETA / ALPHA) et **total combo**.

| # | Métrique | Comment lire |
|---|----------|--------------|
| M1 | `n_fills` | Moins n’est pas mieux tout seul |
| M2 | `n_skip` | Pattern A doit SKIP **plus** que B |
| M3 | `skip_ratio` = SKIP / (SKIP+fills candidatures) | A > B attendu |
| M4 | `pnl_usd` | Net session |
| M5 | `pnl_bps` moyen / trade | Qualité par coup |
| M6 | `max_dd_usd` | Douleur max |
| M7 | `fills_bruit` = fills avec \|hold\| &lt; 30s **ou** \|pnl\| &lt; 2 bps | Bruit |
| M8 | `bruit_pct` = fills_bruit / n_fills | A doit être **plus bas** |
| M9 | `expectancy` = pnl / n_fills (si fills&gt;0) | Qualité |
| M10 | `pf` profit factor (gros gains / gros pertes) si dispo | Optionnel |

Fichier cible suggéré :  
`logs/validation_pattern_voie_A_YYYYMMDD.csv`  
une ligne = un run (A ou B) + timestamp + pack_id.

---

## 4. Critères de succès (écrire AVANT — ne pas bouger après)

**Run valide seulement si** durée atteinte et pas de crash / pas de changement de pack en cours.

### Succès PATTERN (A bat B) — il faut **au moins 2 sur 3** :

1. **`max_dd_usd(A) ≤ max_dd_usd(B)`** (moins ou égal de douleur)  
2. **`bruit_pct(A) < bruit_pct(B)`** d’au moins **20 % relatifs**  
   (ex. B=50 % bruit → A ≤ 40 %)  
3. **Expectancy ou pnl** :  
   - soit `pnl(A) ≥ pnl(B)`  
   - soit `pnl(A) ≥ 0.8 × pnl(B)` **et** `n_fills(A) ≤ 0.6 × n_fills(B)`  
     (presque autant de sous, beaucoup moins de coups)

### Échec clair :
- A a **plus** de DD **et** plus de bruit que B  
- ou A « gagne » seulement grâce à **1** trade outlier (noter ; refaire)

### Inconcluant :
- moins de **10 fills combinés** A+B sur la fenêtre → rallonger (autre 4 h), ne pas conclure

---

## 5. Plan minimal (3 fenêtres)

| Fenêtre | Contenu |
|---------|---------|
| F1 | 4 h A puis 4 h B (ou parallèle si 2 jambes isolables) |
| F2 | autre créneau (ex. soir ≠ matin) — mêmes packs |
| F3 | troisième créneau |

**Validation soft :** A gagne F1+F2 ou F1+F3 (2/3).  
**Validation dure :** A gagne 3/3 sur la règle « 2 sur 3 critères ».

---

## 6. Ce qu’on ne compte PAS comme preuve

- Phrase manifeste / scellage  
- Une session +$ sans témoin B  
- Changer wall_drop mid-run « pour aider A »  
- PnL live réel

---

## 7. GO type (copier quand tu veux lancer)

```text
GO VALIDATION VOIE A
Pack A: radar 0.85 | MOM 0.96 | wall 6.5% | dt 128 | void ON | mass 1.618
Pack B: témoin lâche (radar 0.70 | wall 16% | void OFF | mass 1.0)
Durée: 4h × 2 (A puis B) — paper/testnet
Critères: §4 PROTOCOLE_VALIDATION_PATTERN_V8
```

---

## Liens
[[FORMULE_BASINE_POINTEUR]] · Bureau `FORMULE_BASSINE_PRIVEE_RESTAUREE.txt` · thermo C18–C21
