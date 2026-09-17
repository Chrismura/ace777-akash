# SYNTHÈSE — Les 6 hypothèses d'architecture pour Cortana (17/09/2026, 15:52Z)

Origine : demande de l'opérateur. Consultation : 3 IA via hub (2× Nemotron OpenRouter indépendants + 1× Gemini Juge). Brief complet dans ce dossier (BRIEF_HYPOTHESES_6.md). Avis bruts : AVIS_HYPOTHESES/.

## Ce que l'audit a d'abord révélé (important)
Plusieurs concepts demandés **existent déjà** dans Cortana : le fractal est déclaré dans son prompt (géométries multi-échelles), le z-score adaptatif (seuil invisible anti-baleines) est documenté, la section PATTERN est obligatoire, les tendances 24h/7j + historique horaire lui sont remis, et sa note est réinjectée (début de boucle hippocampe). Le vrai trou : **aucune consolidation** (le corpus grandit en brut, jamais synthétisé) et le raisonnement rétrograde n'est pas encadré.

## Verdicts convergents (2-3 voix sur 3)

| # | Hypothèse | Famille | Buffy | Décision |
|---|---|---|---|---|
| H1 | Raisonnement rétrograde | réserve / non | réserve (biais de confirmation, sauf avec preuve écrite obligatoire) | **PAS NOW** — à re-tester après consolidation |
| H2 | Seuils invisibles / points de bascule | GO (2/3) | réserve (n=60 trop petit pour prouver) | **PLAFOND À 30 J** — chantier piloté par l'Ombre-Scoreur |
| H3 | Information fractale (Hurst, données 4h/1h/15min) | GO réserve (GEMINI) / NON (DEEPSEEK) | **NON** (Cortana reçoit du TEXTE, pas des séries ; Hurst inutilisable par un LLM) | **REJETÉ** (peut-être +1 fenêtre 15min plus tard) |
| H4 | Hippocampe (consolidation hebdo en leçons) | **3/3 GO, chantier n°1** | GO | **GO — chantier n°1** |
| H5 | Entraînement patterns (few-shot étiquetés) | NON (GEMINI) / réserve (DEEPSEEK) | réserve (risque de récits fossilisés) | **PAS NOW** — réévalué à n=50 du professeur |
| H6 | Intelligence distribuée (débat multi-agents) | réserve (3/3 : déjà distribué, débat = overhead) | réserve — le « réseau qui pense » existe déjà (Cortana+Hulk+moteur+professeur+troupeau), c'est l'anti-fragilité | **PAS NOW** — le gain marginal ne paie pas la complexité |

## Le chantier GO : H4 — la consolidation hebdomadaire (l'hippocampe)
- Le professeur (`score_justesse.py`) génère le DIMANCHE une page « leçons » : les 5 réussites récurrentes + les 5 erreurs répétées des 30 derniers jours, avec compteurs.
- Injectée dans le prompt de Cortana (≈400 tokens) à chaque analyse — sa mémoire long terme.
- Chaque leçon porte une date de fraîcheur ; une leçon qui vieillit sans se confirmer **périmée** (anti-fossile, demande GEMINI).
- Test A/B sur 30 jours : score_justesse avec leçons vs sans (n≈60). Gain attendu ≥ 0,2 pt sinon on coupe.

## Les conditions de bascule (qui rouvrent un refus)
- H1 : si la consolidation prouve que Cortana suit mieux une démarche guidée → re-test en second.
- H2 : quand l'Ombre-Scoreur V3 aura n≥50 (3 semaines), on mesurera si les points de bascule prédisent réellement les mouvements.
- H5 : quand le professeur aura assez d'exemples étiquetés solides (n=50+), un few-shot **prouvé** redevient envisageable.
- H6 : si un jour les avis de Cortana et l'exécution de Hulk se contredisent régulièrement, un pont léger sera construit — pas avant.

## Réserve consignée
Voix de la consultation : Nemotron ×2 (indépendantes) + Gemini Juge. L'avis DEEPSEEK a bavardé (raisonnement visible, fuite de format) mais sa conclusion (H4 prioritaire) converge avec les deux autres.

— Buffy, pour ACE777
