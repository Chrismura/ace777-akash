# Plan de vol

**Quoi / dans quel ordre / sans chercher partout.**  
**MAJ :** 2026-08-13 ~23:05Z (fin session 13/08 — journée difficile, voir A_Mon_Attention)

## Maintenant — ordre du jour (essentiel)

1. **Relancer un run test** → attraper la ligne `FATAL_RC1` (trap posé) → corriger la **cause racine Alpha rc=1** (E-08)  
2. **Auto-relance Alpha** + « jamais chasseur solitaire » (famille 6/6, E-09)  
3. **Cortana dit la vérité** : lire `/status` au lieu des fichiers figés (E-10) + aligner les 5 chemins voix sur le mute (E-11)  
4. Cockpit : badge RUN STATUS + graph synapse vérité **déjà en place** (14/08) — vérifier fenêtre info IA (E-13)  
5. **Deux briefs** : n'en garder qu'un (E-12)  
6. ⏸ Cosmétique / baromètre conso / budget cloud / schéma → [[CHOSES_A_FINIR_REVOIR]]

## 31 juil. — piste

| Ordre | Mission | Notes |
|-------|---------|-------|
| **0** | Cadence session début/fin | Ancrer usage · scripts prêts |
| **1** | Cockpit ops | Pont · feed session · hygiène H1–H6 |
| **2** | Validation mode pro | Portes P0→P2 · [[JOURNAL_ERREURS_TEST]] |
| **3** | Kill-switch A/B — preuve | Testnet/paper · pas polish |
| ⏸ | Cerveau / graphe Obsidian | Finition · [[CERVEAU_GALACTIQUE]] |

## Bouton ROUGE — urgence portefeuille (validé concept 31 juil.)

**Avis :** seul bouton « trade » légitime dans le cockpit : **sortie / stop**, pas d’entrée.  
Sert aussi de **test de validation** (chemin A/B sur testnet avant réel).

| Mode | Sens | Comportement cible |
|------|------|---------------------|
| **A — Propre** | Fermeture ordonnée | STOP + sortie · confirmation double |
| **B — Crash** | Urgence | Flatten agressif + stop hard · mot CRASH |

**Garde-fous :** confirmation · testnet d’abord · journal · pont `/panic` · pas d’ouverture depuis UI.  
**Preuve :** 1× A + 1× B (simu/paper) sans faux positif.

## Règle
Un vol = un GO. Kill-switch ≠ GO d’entrée.  
Cosmétique = finition. Matin = `session_debut` avant tout.

[[INDEX_COMMANDES]] · [[CHOSES_A_FINIR_REVOIR]] · [[PROTOCOLE_SESSION_DEBUT_FIN]] · [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]]
