# ÉTAT CONSOLIDÉ — ACE777

> **Se lit en entier à chaque début de session. Max 50 lignes.**
> Mis à jour à la fin de chaque session (par le superviseur).
> Historique complet → `ARCHIVE_INDEX.md` (jamais relu en entier).
> Généré depuis le vault (source de vérité) — le superviseur lit et distille.

## 1. OBJECTIF DU JOUR
- (1 ligne : la seule chose à faire aujourd'hui)

## 2. DÉCISIONS ACTIVES (3 max, avec date)
- [2026-08-09] **SETUP FINAL VALIDÉ** (4 familles OK + GO Christophe) : grok-4.3 ACTIF via Puter (gratuit) · auto-éval quotidienne · verifier_setup.py
- [2026-08-09] Hub = 7 providers actifs · timeout PATIENCE (fix définitif) · cycle 9h05→12h
- [2026-08-09] InferX gratuit jusqu'au 12/08 (DeepSeek V4 + Qwen3-Coder)

## 3. CONTRAINTES (rappel, 1 ligne chacune)
- C1 TCC : launchd ne lit pas ~/Documents → miroir dans ~/ace777-test-day1
- C2 RAM 8 Go : inférence cloud, pas de modèle local lourd
- C3 Doctrine : zéro trading — observation/analyse BTC seulement
- C4 Maker≠checker : jamais se valider seul (juge indépendant, audit tiers)
- C5 Gratuit d'abord : fallback en chaîne, aucun outil payant lourd
- C6 Internet = preuve, jamais un ordre

## 4. ÉTAT GIT
- système (~/ace777-test-day1) : WIP normal (fichiers modifiés en cours)
- vault (~/Documents/Obsidian_ACE777) : voir BOOT_STATUS pour l'état exact

## 5. PROCHAINE ACTION
- A/B grok vs nemotron-ultra demain matin (auto, quota :free reset) ; cycle 9h05→12h ; rien d'autre en attente

## 5bis. RITUEL AMELIORATION PROACTIVE (grave 09/08 — reproche Christophe : je propose rarement)
> OBLIGATOIRE en debut de session, AVANT tout travail : je ne suis plus reactif, je propose.
1. LIRE le backlog d'ameliorations (TABLEAU_PEPITES INTEGRER/VERIFIER + AUTO_EVOL/IDEES + VEILLE_HUB du jour)
2. CHOISIR TOP 3 ameliorations (chacune : quoi · preuve · cout · impact)
3. SOUMETTRE au juge (maker≠checker — je ne me valide pas seul)
4. PRESENTER les 3 a Christophe → GO → delegation du code
Script : propose_ameliorations.py (lance par veille_hub 5ter). Sortie : A_Mon_Attention/PROPOSITIONS_AMELIORATIONS.md

## 5ter. VERIFICATION AUTO DU SETUP (09/08, idee Christophe : ne jamais refaire a la main)
> Apres CHAQUE changement de setup : `python3 Index_Maison/scripts/verifier_setup.py`
> compile (36 scripts) + hub + providers + routing + appel reel + launchd + FAMILLE (brief auto-genere).
> Rapport : A_Mon_Attention/VERIF_SETUP_<date>.md · exit 0 = vert. Lancee aussi chaque jour a 12h (launchd, --no-famille).
> Lecon : le brief famille doit TOUJOURS inclure le contexte protocole (brief sec = PARTIELLEMENT).

## 6. ARCHIVE
- `ARCHIVE_INDEX.md` : naviguer l'historique sans tout relire
- `MEMOIRE_COLLAB.md` : journal des sessions (chronologique, jamais chargé en entier)
- `journal_erreurs.md` : erreurs + correctifs · `AUDIT_REPAIR_2026-08-09/` : audit complet
