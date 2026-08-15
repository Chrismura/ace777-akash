# SPEC — Couche de connaissance ACE777 (15/08/2026)

**Statut** : approuvée famille (GO-AVEC-RÉSERVE, gemini 85% / nvidia 78%) + arbitrage
supervision Buffy. **Chantier = connaissance uniquement, ZÉRO touche au moteur Hulk.**

---

## 1. Objectif

Consolider la connaissance ACE777 (audits famille, thèses Christophe, signets X « garder »)
dans une **base structurée par projet**, et l'**injecter automatiquement** dans le contexte
famille/Cortana quand c'est pertinent. Fini le contexte réécrit à la main par le superviseur.

## 2. Livrables

| Fichier | Rôle |
|---|---|
| `Index_Maison/strategie/CONNAISSANCE_PROJETS.json` | Base par projet (schéma §3) |
| `Index_Maison/scripts/construire_connaissance.py` | Collecteur : ingère verdicts famille + signets gardés → consolide la base + auto-nettoyage |
| `Index_Maison/scripts/injecter_connaissance.py` | Injecteur : extrait la fiche pertinente + signets → sortie BRIEF prête à coller (≤500 tokens) |
| `Index_Maison/thermo/SANTE_CONNAISSANCE.md` | Dashboard de santé de la base (généré par le collecteur) |

## 3. Schéma de la base — `CONNAISSANCE_PROJETS.json`

```json
{
  "version": 1,
  "updated": "2026-08-15",
  "projets": {
    "CCUSDT": {
      "nom": "Canton Network",
      "these": "Institutionnel sous-radar : accumulation de dumps en bag, institutionnels vérifiés",
      "classe_hulk": "B_bag",
      "horizon_bag": "long",
      "capital_alloue_max": "5-10% portefeuille",
      "statut_verification": {
        "date": "2026-08-15",
        "verdict": "GO-AVEC-RÉSERVE",
        "score": 71,
        "reserve": "2 classes de paires + stop fondamental obligatoires"
      },
      "faits": [
        {
          "fait": "Goldman Sachs, BNY Mellon, CBOE, Microsoft, Moody's, Deutsche Börse = participants vérifiés",
          "source": "audit_famille",
          "fiabilite": 0.7,
          "expires_at": "2026-11-13",
          "etat": "verifie"
        }
      ],
      "lecons": [
        "Pas de stop technique (illiquide → chassé) — stop FONDAMENTAL",
        "Bag ≥ 12 mois, réévaluation trimestrielle",
        "Taille ≤ 5-10% du portefeuille, max 3-5 bags simultanés, max 20% total"
      ],
      "signets_cles": ["id1", "id2"],
      "updated": "2026-08-15"
    }
  }
}
```

### Règles de la base (anti-engraissement — verdict famille)
1. **Critère d'entrée d'un fait** : audit formel famille (source première) **OU** 2 sources
   indépendantes (institutionnel + on-chain, ou 2 audits distincts) **OU** signet « garder »
   à forte conviction. Tout fait sans source → refusé.
2. **Péremption** : `expires_at` — 90 jours (fondamentaux) / 30 jours (données marché).
   Fait périmé → `etat: "obsolete"`, **exclu des injections**.
3. **Fait non vérifié 7 jours** après entrée → `etat: "en_attente"`, hors injection.
4. **Quota** : max 50 faits/projet (au-delà → purge des plus anciens, loggé).
5. **Scoring** : fiabilité par source — institutionnel 0.9 · audit famille 0.7 · signet X 0.5.
   Score global d'un fait = moyenne pondérée des sources. **Seuil d'injection ≥ 0.6** ;
   en dessous → `etat: "a_confirmer"`, exclu de l'auto.
6. **Auto-nettoyage hebdo** (au run du collecteur) : purge des périmés, archive des projets
   inactifs > 90 jours (déplacés dans `projets_archives`).

## 4. Collecteur — `construire_connaissance.py`

- **Entrée 1** : dossier(s) `CONSULTATION_FAMILLE_*/VERDICT_FAMILLE.md` → parse verdict,
  score, réserves, leçons, faits → met à jour la fiche projet.
- **Entrée 2** : `strategie/SIGNETS_RESUMES.json` (signets `avis == "garder"`) → consolide
  les signets clés par projet (matching par symbole/nom dans le résumé) + alimente
  `signets_cles`.
- **Sorties** : base mise à jour (écriture atomique) + `thermo/SANTE_CONNAISSANCE.md`
  (nb projets, faits vérifiés/en_attente/obsoletes/a_confirmer, projets inactifs).
- **Idempotent** : relançable sans doublons (clé = hash du fait + source).
- **Kill-switch respecté** : vérifie `STOP` / `STOP_ALL` avant écriture.

## 5. Injecteur — `injecter_connaissance.py`

Usage : `python3 injecter_connaissance.py --projet CCUSDT [--lecons]` ou
`python3 injecter_connaissance.py --sujet "small caps bags" [--max-tokens 500]`.

- **Mode hybride** (verdict famille) :
  - **Auto** : si le texte du brief contient un nom/symbole de projet de la base →
    extrait le résumé exécutif (thèse + statut + faits vérifiés, ≤500 tokens),
    **SANS les leçons** (jamais en auto — ne pas polluer le contexte opérationnel).
  - **À la demande** : `--lecons` ajoute sizing/stops/garde-fous (usage explicite).
- **Rotation** : si >3 projets pertinents → 2 plus récents + 1 aléatoire (anti-biais de
  récence).
- **Filtrage** : seuls les faits `etat == "verifie"` et score ≥ 0.6 sont injectés.
- **Sortie** : section « CONNAISSANCE PROJET » prête à coller dans un BRIEF famille/Cortana
  (stdout + option `--fichier out.md`).

## 6. Pilote Canton (obligatoire avant déploiement large)

1. Le collecteur ingère `CONSULTATION_FAMILLE_SMALLCAPS_CANTON_20260815/VERDICT_FAMILLE.md`.
2. `CONNAISSANCE_PROJETS.json` contient CCUSDT complet (thèse, faits, leçons, statut).
3. L'injecteur produit le BRIEF Canton (≤500 tokens, sans leçons) + variante `--lecons`.
4. Critère de succès : l'injecteur ne sort **que** des faits vérifiés/sourcés, et le brief
   se colle tel quel dans une consultation famille.

## 7. Réversibilité

- Tout est dans `CONNAISSANCE_PROJETS.json` (1 fichier) + 2 scripts + 1 dashboard.
- `rm` des 4 fichiers = retour à l'état antérieur (aucune modif du moteur Hulk).
- Release Receipt à remplir à la fin du chantier.
