# CHANTIER — Couche de connaissance ACE777 (15/08/2026)

**Statut** : ✅ LIVRÉ et TESTÉ (pilote Canton réussi)

## Ce qui a été fait
| Livrable | Fichier | Rôle |
|---|---|---|
| Base par projet | `strategie/CONNAISSANCE_PROJETS.json` | Schéma famille affiné (thèse, classe_hulk, horizon_bag, statut structuré, faits+expires_at, leçons, signets) |
| Collecteur | `scripts/construire_connaissance.py` | Ingère verdicts famille (idempotent) + signets « garder » + règles anti-engraissement + dashboard santé |
| Injecteur | `scripts/injecter_connaissance.py` | Extraction fiche ≤500 tokens, leçons exclues en auto, détection par --sujet, rotation, filtrage score≥0.6 |
| Dashboard santé | `thermo/SANTE_CONNAISSANCE.md` | Projets suivis, faits par état, archive |

## Pilote Canton — résultats réels
- Verdict famille `CONSULTATION_FAMILLE_SMALLCAPS_CANTON_20260815` → fiche **CCUSDT** complète
  (thèse, statut GO-AVEC-RÉSERVE **71%**, 3 faits vérifiés 0.7 + fait d'audit idempotent, 4 leçons).
- Injecteur : mode auto (sans leçons) ✅ · `--sujet` détection ✅ · `--lecons` explicite ✅.
- **Score extrait correctement** (71% = moyenne 70+72) après correction de la regex
  (capturait les % du contenu au lieu de la ligne « Avis reçus »).

## Erreurs du codeur corrigées par la supervision
1. **SyntaxError** dans le code reçu (`faits = [],` dans un dict) → réécrit.
2. **Chemins faux** (signets vers `Index_Maison/signets/`, dossiers verdicts à la racine).
3. **Structure signets supposée fausse** (champs projet/garder/titre inexistants — la vraie
   structure est `{id: {author, url, resume, avis}}`) → matching par alias + avis=="garder".
4. **JSON initial inventé** (faits 2025) → fiche réelle d'après le verdict famille.
5. **Regex score** capturait tous les % du texte (30% au lieu de 71%) → ligne ciblée.
6. **Comparaison datetime naive/aware** → dates uniquement.

## Règles anti-engraissement actives (verdict famille)
- Entrée : audit famille OU 2 sources indépendantes OU signet gardé fort.
- Péremption : `expires_at` 90 j (fondamentaux) / 30 j (marché) → `obsolete` + archive.
- Quota : 50 faits/projet · archive froide 180 j · non vérifié 7 j → `en_attente`.
- Injection : `etat==verifie` ET score ≥ 0.6 uniquement.

## Utilisation
```bash
# Avant une consultation famille/Cortana sur un projet :
python3 ~/ace777-test-day1/Index_Maison/scripts/injecter_connaissance.py --sujet "votre sujet"
# Avec garde-fous (sizing/stops) — usage EXPLICITE :
python3 ~/ace777-test-day1/Index_Maison/scripts/injecter_connaissance.py --projet CCUSDT --lecons
# Après un nouvel audit famille :
python3 ~/ace777-test-day1/Index_Maison/scripts/construire_connaissance.py
```

## Réversibilité
`rm` de CONNAISSANCE_PROJETS.json + construire_connaissance.py + injecter_connaissance.py
+ thermo/SANTE_CONNAISSANCE.md = retour à l'état antérieur (zéro touche moteur Hulk).
