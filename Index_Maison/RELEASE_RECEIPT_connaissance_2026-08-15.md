# RELEASE RECEIPT — Couche de connaissance (15/08/2026)

## 1. Propriétaire
- **Superviseur** : Buffy · **Approuvé** : Christophe (GO) + famille (GO-AVEC-RÉSERVE,
  gemini 85% / nvidia 78%) · **Codeur** : hub (ébauche, corrigée supervision)

## 2. Frontières (ce que ce chantier touche / ne touche pas)
- ✅ TOUCHE : `strategie/CONNAISSANCE_PROJETS.json` · `scripts/construire_connaissance.py`
  · `scripts/injecter_connaissance.py` · `thermo/SANTE_CONNAISSANCE.md`
- 🚫 NE TOUCHE PAS : moteur Hulk (`paper_diprip.py`), hub, config, kill-switch — vérifié

## 3. Gaps connus (honnêteté)
- Le collecteur ne parse QUE les verdicts famille dont le dossier matche un alias projet
  (CCUSDT/XRP/HBAR). Les autres dossiers sont ignorés proprement (loggé) — pas d'erreur.
- Le matching signets→projet est v1 par alias (Canton matche ; d'autres projets devront
  ajouter leurs alias dans `PROJET_ALIASES`).
- Injection non branchée dans la discipline quotidienne (volontaire : pas de sujet fixe).
  Utilisation à la demande + --sujet. Évolution possible plus tard.

## 4. Révocabilité
- `rm` des 4 fichiers = retour à l'état antérieur. Aucune modif hors de ces fichiers.

## 5. Tests réels effectués
- Collecteur : verdict Canton → fiche CCUSDT, score 71% correct, idempotence vérifiée
  (2 runs, pas de doublon), réserve préservée.
- Injecteur : mode auto (sans leçons) · --sujet détection auto · --lecons explicite.
- py_compile des 2 scripts OK · kill-switch respecté.

## 6. Rollback
- `rm ~/ace777-test-day1/Index_Maison/strategie/CONNAISSANCE_PROJETS.json \
  ~/ace777-test-day1/Index_Maison/scripts/construire_connaissance.py \
  ~/ace777-test-day1/Index_Maison/scripts/injecter_connaissance.py \
  ~/ace777-test-day1/Index_Maison/thermo/SANTE_CONNAISSANCE.md`
- Aucune autre action nécessaire.
