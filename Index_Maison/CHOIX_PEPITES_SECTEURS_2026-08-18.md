# CHOIX DES PÉPITES À INSTALLER — synthèse croisée (18/08/2026)

**But** : avant d'installer quoi que ce soit, diagnostiquer le système par SECTEURS
pour trouver le goulot d'étranglement — puis choisir les pépites qui débloquent LE
goulot, pas celles qui font joli. (Logique Christophe, 18/08.)
**Timing** : pendant l'attente de la fin des runtests (22/08) — la machine tourne seule.

---

## 1. Les tableaux qui distinguent déjà les pépites (sources Obsidian)

| Source | Où | Ce qu'elle dit |
|---|---|---|
| `Evaluations/TAGS_138_SIGNETS_RECAP.md` | vault Obsidian | 10 tags / 2 familles · 120/138 signets taggés · famille ACE777 (agents, mémoire, données, backtest-edge, sorties, volumes, GEX) vs Veille (outils-agents, modèles-ia, macro) |
| `Evaluations/PEPITES_SIGNETS_APPLICATION.md` | vault Obsidian | 19 pépites GARDÉ/PISTE avec « applicable à » (backtest vs live, ONE NUMBER, sorties > position, Alpha Orchestration, Stop Prompting, Loop→Graph…) |
| `TRI_SIGNETS_SYNTHESE_2026-08-15.md` | Index_Maison | 200 signets · chacun choisit ses 10 · 5 consensus ≥2 membres (192, 12, 53, 130, 189) |
| `CONSULTATION_FAMILLE_SIGNETS_FRAIS_20260815/SYNTHESE.md` | Index_Maison | 35 signets frais · gemini + nvidia → 3 améliorations (mémoire-drift, Kelly, Release Receipt) |

## 2. Les pépites candidates — croisées (le vrai short-list)

| Pépite | Consensus | Où ça s'applique | Secteur |
|---|---|---|---|
| **N°192 — 6 fichiers de suivi (Anthropic)** | **3/3** (gemini+nvidia+cortana) | −84 % tokens, +39 % précision — organisation mémoire externe | MÉMOIRE |
| **N°43+105 — Kelly / sizing (Burry + St-Pétersbourg)** | nvidia + tri du jour | **= notre chantier sizing ouvert ce matin** (32,5 % ruine) | EXÉCUTION |
| **N°53/12 — mémoire agents (TencentDB / Brain.md)** | gemini+cortana | les agents ne repartent plus de zéro | MÉMOIRE |
| **N°30/31 — garde-fous production / trou de responsabilité** | nvidia | Release Receipt 6 points + ownership par agent (déjà à moitié chez nous) | GOUVERNANCE |
| **N°130 — formats 4-bit** | nvidia+cortana | 28 Go FP32 → 4 Go — tourner sur 8 Go RAM | INFRA |
| **N°189 — TradingAgents** | gemini+cortana | analyse de marché par agents autonomes → Hulk dip&rip | STRATÉGIE |
| **@0xWast3 N°1 — 4 indicateurs de dérive mémoire** | **gemini+nvidia (indépendants)** | surveiller la SANTÉ de ce que Cortana sait (branche directe sur discipline 7h15) | MÉMOIRE |
| **Data Formulator (Microsoft)** | Buffy + Christophe 18/08 | visualisation des runs ACE pilotée IA, local, gratuit | VEILLE/ANALYSE |

## 3. Découpage du système en secteurs (proposition pour la famille)

> Objectif : rendre le diagnostic lisible — chaque secteur a ses goulots, ses pépites, son propriétaire.

| Secteur | Contenu | Goulot suspect (à vérifier par la famille) | Pépites candidates |
|---|---|---|---|
| **EXÉCUTION (hot)** | ACE, Hulk, moteur, fills, stops, sizing | 🔴 **sizing → ruine 32,5 %** (Monte Carlo 18/08) | Kelly (43+105), sorties (pépite 4) |
| **DÉCISION / STRATÉGIE** | radar, indices, decision engine, modes | 🟡 filtre strict → P(fill) 6,5 % | TradingAgents (189), Alpha Orchestration (17) |
| **MÉMOIRE / CONNAISSANCE** | Cortana, Ada, vault, justesse, leçons, agora | 🟡 Cortana stateless, leçons auto sans plist propre, justesse 44,4 % | 6 fichiers (192), mémoire agents (53/12), mémoire-drift (0xWast3) |
| **INFRA / HUB IA** | providers, routeur, chaîne 7h, roulement | 🟡 6 obs-* morts aux sondes (0/5), nara/nvidia lents | formats 4-bit (130), LLMRouter (6) |
| **SURVEILLANCE / SANTÉ** | veilleuses, superviseur, préflight, alertes | 🟢 bien armé (3 veilleuses) | CheckCle (111) |
| **VEILLE / INGESTION** | flotille, signets, scan GitHub, données | 🟡 signets = mine mais non ingérés automatiquement | Data Formulator, pipeline 8 étages (16) |
| **GOUVERNANCE / PROCESS** | famille, juge, codeur, Release Receipt, protocoles | 🟡 release receipts existent mais pas standardisés partout | garde-fous (30/31) |

## 4. Ma proposition (Buffy) — séquentiel, pas parallèle (réserve famille)

1. **Diagnostic par secteurs** : consultation famille sur le tableau ci-dessus — chaque membre
   désigne LE goulot n°1 de SON secteur + le goulot n°1 GLOBAL du système.
2. **Une seule pépite par goulot** : on n'installe que la pépite qui débloque le goulot n°1
   global (pas les 8 en même temps — la réserve « séquentiel » de la famille du 15/08).
3. **Pendant l'attente des runtests** : rien ne touche le moteur. On prépare le diagnostic,
   la famille répond, et le 22/08 (fin du run 96h + confrontation + sizing) on a tout pour
   décider avec les données.

## 5. Verdict honnête

Le goulot le plus probable **aujourd'hui, chiffres à l'appui** : **EXÉCUTION / SIZING**
(ruine 32,5 %, Monte Carlo 18/08) — et la pépite Kelly (43+105) est **déjà alignée**
avec le chantier sizing ouvert ce matin. MAIS la famille doit confirmer : peut-être
qu'elle verra un goulot plus urgent ailleurs (mémoire ? hub ?).

**Aucune action appliquée** — document de préparation. GO Christophe + famille avant toute installation.
