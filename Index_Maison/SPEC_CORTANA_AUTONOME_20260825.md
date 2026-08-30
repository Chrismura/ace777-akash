# 🎓 SPÉCIFICATION — Cortana Analyse Autonome

> **Objectif** : Apprendre à Cortana à faire des analyses comme celle des blocs privatisés, en autonomie.

---

## 🧠 CE QUE CORTANA DOIT APPRENDRE

### Le pattern d'analyse (schéma réutilisable)

```
1. DÉTECTION    → Un indicateur sort de la normale
2. CHRONOLOGIE  → Quand a commencé ? Est-ce en cours ?
3. CONTEXTE     → Que disent les autres indicateurs ?
4. CORRÉLATION  → Est-ce cohérent avec le prix ? Le narratif ?
5. INTERPRÉTATION → Qu'est-ce que ça veut dire pour Hulk ?
6. RECOMMANDATION → Que doit faire Hulk ?
```

### Les fiches d'analyse (templates)

Chaque type d'anomalie a une **fiche** que Cortana peut remplir :

#### FICHE BLOCS PRIVATISÉS
```json
{
  "type": "blocs_privatises",
  "trigger": "taux_fantome > 25%",
  "questions": [
    "Le pic est-il prolongé (>10 min) ou bref (<5 min) ?",
    "Le volume est-il important (>100 BTC) ?",
    "Le prix a-t-il bougé pendant le pic ?",
    "Le SDI est-il élevé (>0.3) ?",
    "Le RBF est-il élevé (>0.6) ?"
  ],
  "interpretations": {
    "pic_bref_volume_haut": "Consolidation exchange — neutre",
    "pic_prolonge_volume_haut": "Distribution possible — surveiller",
    "pic_sans_mouvement_prix": "OTC — neutre à haussier",
    "pic_avec_sd_eleve": "Drainage silencieux — dangereux"
  },
  "actions": {
    "neutre": "Garder les positions, observer",
    "surveiller": "Réduire taille de 25%, stops plus serrés",
    "dangereux": "Réduire taille de 50%, sortir des positions fragiles"
  }
}
```

#### FICHE RBF ÉLEVÉ
```json
{
  "type": "rbf_eleve",
  "trigger": "rbf_score > 0.6",
  "questions": [
    "Est-ce lié à un mouvement de prix ?",
    "Combien de paires sont concernées ?",
    "Le funding est-il en hausse ?"
  ],
  "interpretations": {
    "rbf_sans_prix": "Accumulation silencieuse — neutre",
    "rbf_avec_prix_baisse": "Panique — dangereux",
    "rbf_avec_prix_hausse": "Momentum — haussier"
  }
}
```

#### FICHE PIPELINE HEALTH DÉGRADÉ
```json
{
  "type": "health_degrade",
  "trigger": "global_score < 0.85",
  "questions": [
    "Quelle source est en erreur ?",
    "Est-ce temporaire ou persistant ?",
    "Hulk est-il exposé sur cette source ?"
  ],
  "interpretations": {
    "binance_timeout": "Pas de prix fiable — KILL SWITCH",
    "deribit_timeout": "GEX indisponible — réduire tailles",
    "mempool_timeout": "Onchain indisponible — ignorer signaux onchain"
  }
}
```

---

## 🏗️ ARCHITECTURE CORTANA AUTONOME

```
┌─────────────────────────────────────────────────────────────┐
│                    PIPELINE DE DONNÉES                       │
│  thermo → live.json → sentinel → signals.json               │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CORTANA AUTONOME                          │
│                                                              │
│  1. Écoute les signaux (sentinel.py → signals.json)         │
│  2. Charge la fiche d'analyse correspondante                │
│  3. Pose les questions de la fiche                           │
│  4. Remplit l'interprétation                                 │
│  5. Génère la recommandation                                │
│  6. Écrit dans cortana_analysis.json                        │
│  7. Si URGENT → alerte vocale                               │
│  8. Si SURVEILLER → note dans le journal                    │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    HULK                                       │
│  Lit cortana_analysis.json                                  │
│  Applique la recommandation (taille × mult, stops, etc.)    │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 ÉTAPES D'IMPLÉMENTATION

| Étape | Action | Temps |
|---|---|---|
| **1** | Créer les fiches d'analyse (JSON) | 1h |
| **2** | Créer `cortana_analyzer.py` (lit signaux + fiches) | 2h |
| **3** | Intégrer dans le pipeline (après sentinel) | 1h |
| **4** | Tester avec le cas des blocs privatisés | 1h |
| **5** | Ajouter la lecture par Hulk | 1h |

---

## 🎯 RÉSULTAT ATTENDU

Quand le taux_fantome dépasse 25%, Cortana doit automatiquement :

1. **Détecter** : "Le taux de blocs privatisés est à 31%"
2. **Chronologie** : "Ça a commencé à 14:46, ça dure depuis 17 minutes"
3. **Contexte** : "Le prix est stable, le SDI est bas, le RBF est élevé"
4. **Corrélation** : "C'est cohérent avec une opération OTC, pas une distribution"
5. **Interprétation** : "Signal neutre à haussier"
6. **Recommandation** : "Garder les positions, observer"

**Et tout ça en AUTONOMIE**, sans que tu aies à demander.

---

*Document généré le 2026-08-25. Prêt pour implémentation.*
