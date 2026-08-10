# 🗳️ SYNTHÈSE CONSULTATION AVANT FUSION 27→13 (10/08/2026)

## Verdicts — UNANIMITÉ : AMÉLIORER D'ABORD

| Voix | Rôle | Verdict |
|---|---|---|
| GEMINI | audit.protocol | **AMÉLIORER D'ABORD** (« fusion sur base instable = bugs en cascade ») |
| JUGE | signets.juge | **AMÉLIORER D'ABORD** (« réduire la charge de travail de la fusion ») |
| CODEUR | code.ia (nvidia) | **AMÉLIORER D'ABORD** (« on ne fusionne pas pour fusionner, on prépare le terrain ») |

## ⚠️ Constat partagé (mesuré, pas de mémoire)
- **29 services chargés mais seulement 4 vivants** (cockpit-http, cockpit-pont,
  cortana.horaire, prise-ia + les 2 nouveaux état/backup)
- state.json = STALE (vrai : feeds trading/vocal figés — bots arrêtés)
- → **tenter la fusion sur 29 services dont 25 dormants = complexité inutile**

## 📋 PLAN D'AMÉLIORATION AVANT FUSION (3 actions, consensus des 3 voix)

### Action 1 — Purge des services morts/redondants (12)
Jamais vivants, à désactiver proprement (unload + plist dans DESACTIVES) :
`analyse-usage · analyste-cadence · graph-cerveau · observatoire ·
pulse-sous-loeil · qwen-btc · qwen-elabore · rotation-logs ·
surveillance-quotas · veille-hub · verif-setup · vigie`
→ 29 - 12 = **17 services restants, terrain nettoyé**
(⚠️ vérif-setup + vigie : les 3 voix les citent — à confirmer avant unload)

### Action 2 — Créer la colonne vertébrale AVANT de casser : superviseur_core.sh
- 1 script bash léger qui absorbe : heartbeat + pulse-sous-loeil + vigie
  (monitoring), puis les hooks pour analyse/tri
- Testé manuellement AVANT de désactiver quoi que ce soit
- Règle codeur : le superviseur LIT state.json (jamais ne l'écrit — le
  state-generator est le SEUL écrivain) + KeepAlive + intervalle > 120 s

### Action 3 — FUSION_MAP.md : la carte de la fusion
Documenter pour CHAQUE service : ce qu'il fait, ce que le superviseur doit
absorber, l'ordre de désactivation → on ne relit jamais le code pendant la
fusion. Anti-risque « oubli de fonctionnalité » (codeur : risque n°2).

## 🛡️ Les 3 risques (consensus) et parades
| Risque | Parade |
|---|---|
| R1 : superviseur unique = point de rupture unique | KeepAlive strict + log stderr indépendant + state.json reste source de vérité (mode dégradé possible) |
| R2 : RAM 8 Go saturée (LLM simultanés) | Sémaphore : 1 seul appel LLM lourd à la fois |
| R3 : zombies plists / conflits | unload propre AVANT load + plists backupés dans DESACTIVES + FUSION_MAP + fenêtre maintenance + point restauration |

## ✅ Ce qui reste INTACT (consensus des 3 voix)
- `state-generator` (source de vérité) · `backup-check` (contrôle backup)
- `cockpit-http` + `cockpit-pont` (interface) — jamais absorbés
- `cortana.horaire` + `cortana.urgent` (vocal, protégé par la loi)

## 🔜 Prochaine étape (après GO Christophe)
Exécuter les 3 actions d'amélioration (purge 12 + superviseur_core.sh +
FUSION_MAP.md) → vérifier stabilité (state.json, hub, 5 services critiques)
→ puis concevoir le superviseur unique sur un terrain propre.
