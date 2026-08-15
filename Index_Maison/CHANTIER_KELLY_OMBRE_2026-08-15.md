# CHANTIER — Kelly fractionnaire ¼ en mode OMBRE (sizing Hulk) — 15/08/2026

**Statut : APPLIQUÉ + TESTÉ** · mode ombre pur (rien d'appliqué) · réversible.

## Décision famille (nvidia 72%, rang 1 — « la plus value immédiate »)
Origine : signets N°43 @kryneeex (Burry : « c'est la taille de position qui compte ») + N°105 @CorvusXBT (paradoxe de Saint-Pétersbourg → critère de Kelly). **Supervision : mode OMBRE** — on calcule et on affiche, on n'applique RIEN (justesse 44% + win-rate réel 0/3 → Kelly plein = 0 → paralysie sinon ; même philosophie que le contrat ADVISORY).

## Livré
- `Index_Maison/scripts/kelly_ombre.py` : stdlib, lit `justesse_v2.json` (44%) + le dernier CSV Hulk **ayant** des trades clos, calcule Kelly plein → ¼ → planchers (win_rate<50% → 0 · n<20 → ×0,5 · plafond 2%).
- Rapport `hulk-mexc/runs/KELLY_OMBRE.md` + JSON `hulk-mexc/strategie/kelly_ombre.json` (champ `applique: false` TOUJOURS).
- Hook 3 lignes dans `discipline_quotidienne.py` (après dérive mémoire, fail-open) → le Kelly se calcule chaque jour à 07h15 avec la discipline.
- Règle de passage à l'application (affichée dans le rapport) : win_rate ≥ 50% sur ≥ 20 trades ET justesse Cortana ≥ 50% + validation humaine.

## Vérifications (vertes)
- `py_compile` OK · run réel : win_rate 0% (0/3), avg_loss 1.51$, Kelly 0, motif honnête anti-paralysie affiché ✅
- Discipline complète : 3 hooks (Cortana + dérive + Kelly) tournent ensemble, 0 erreur, exit=3 (alertes attendues).

## Notes honnêtes
- Correction supervision : le codeur lisait `row.get("action")` mais le CSV Hulk utilise `event` (vérifié dans `log()`) → corrigé. Il prenait aussi le dernier CSV quel que soit son contenu (run de test d'aujourd'hui = 0 trades clos) → corrigé : on prend le 1er CSV avec des trades clos du plus récent au plus ancien.
- La donnée dit la vérité : avec 0/3 wins et 44% de justesse, **le Kelly interdit le sizing adaptatif** — c'est le plancher qui protège (règle d'or anti-paralysie de nvidia).

## Retour arrière (réversible)
- `rm Index_Maison/scripts/kelly_ombre.py` + retirer les 3 lignes du hook dans discipline_quotidienne.py (+ `rm hulk-mexc/strategie/kelly_ombre.json hulk-mexc/runs/KELLY_OMBRE.md`).
