# FICHE — Chaîne IA ACE777 (inventaire & état)

> Point de situation rédigé par **Buffy** le 18/08/2026. Vulgarisé : lisible par Christophe ET par une IA.
> Canon technique : [[Index_Maison/architecture/ARCHITECTURE_TECH]] · [[ARCHITECTURE_AGORA]]

---

## 1. La photo simple (comment ça marche)

ACE777 est un **organisme** :
- **1 cerveau** : le **hub** (`prise-ia`, port `11435`) — la seule porte d'entrée de toutes les IA (C9 : zéro LLM local).
- **Des organes** : ACE (trade testnet), Hulk (paper MEXC), ADA (gardienne), l'analyste, la veille.
- **Un tableau de bord** : le **cockpit** (onglets OPS/THERMO/BOARD/GRAPH/VOL/STRATÉGIE).
- **Une mémoire** : **Obsidian** (le coffre).

Les IA **ne se parlent pas directement** : tout passe par le hub. Le cockpit **ne parle pas aux IA** : il lit des fichiers JSON que les agents mettent à jour. Cortana (le chat du cockpit) est le **seul point de contact** avec l'humain.

---

## 2. Les acteurs (qui fait quoi)

| Composant | Rôle | Où | État |
|---|---|---|---|
| **Hub `prise-ia`** | Routeur LLM : reçoit une `task`, choisit le bon provider (gemini/nara/groq/nvidia…), bascule auto, budget cloud | `~/prise-ia/` · `:11435` | 🟢 prod |
| **Pont gate** | Garde-fou des trades ACE → hub, fail-closed | `llm_gate_hub_bridge.py` · `:11439` | 🟢 prod |
| **Pont cockpit** | Cockpit ↔ hub : `/status /mission /chat /analyse /panic …` | `cortana_cockpit_bridge.py` · `:17777` | 🟢 prod |
| **Cortana** | La voix + le chat : répond sur l'état, analyse, avis | chat cockpit + voix Vivienne | 🟢 prod |
| **Analyste** | Stratégie → `STRATEGIE.md` / `derniere_analyse.md` | `analyste.py` | 🟢 |
| **ADA gardienne + saison** | Voilure 0–100, zones VERT/JAUNE/ROUGE, 6 indices → saison | `ada_gardienne.py`, `ada_saison.py` | 🟢 |
| **Veille hub** | Scan providers/RSS/GitHub → offres & pépites | `veille_hub.py` | 🟢 |
| **Lecteur signets** | Lit Obsidian `Signets_X/` → résume via hub → cockpit | `signets_lecture.py` | 🟢 |
| **Fiches offres** | Fiches IA des offres détectées (quota 8/j) | `fiches_offres.py` | 🟢 |
| **Coffre (RAG)** | Question → recherche vault Obsidian → réponse sourcée | `coffre_ask.py` | 🟢 (pas branché au chat) |
| **Recherche web** | Analyse une crypto/sujet sur le net (CoinGecko + DuckDuckGo) → synthèse hub | `recherche_web.py` | 🟢 (branché au chat) |
| **Dashboard Cortana** | Vue complète maison (ACE+Hulk+marché) + synthèse | `cortana_dashboard.py` | ⚠️ dort (non branché au chat) |
| **État système** | state.json : services, hub, RAM, fraîcheur des feeds | `system_state_generator.py` | 🟢 |
| **Santé des index** | Vérifie chaque chaîne de bout en bout + alerte vocale | `sante_index.py` | 🟢 |
| **Détecteur CPFP** | « Pépite » onchain : arbre de poussière + tx enfant CPFP | `detecter_cpfp.py` | 🟡 observation |
| **Détecteur blocs privatisés** | Tx fantômes (jamais vues en mempool) | `detecter_bloc_privatise.py` | 🟡 observation |
| **Disjoncteur** | Bride les mises, Mur de Fer, réarmement manuel | `disjoncteur.py` | 🟢 |

**47 LaunchAgents** actifs — l'organisme est très câblé.

---

## 3. Le flux de données (d'où ça vient → où ça va)

```
Signets X (Obsidian) ──signets_lecture──► hub ──► SIGNETS_RESUMES.json ─┐
runs/*.csv (ACE) + Hulk state ──cockpit_mission_feed──► mission.json ───┤
thermo (funding/OI/GEX/baleines) ──► thermo/live.json ──────────────────┤
pont_onchain (scan baleines + CPFP/dust) ──► live.json.onchain ──────────┤
veille_hub ──► VEILLE_HUB_*.md ──bridge /offres──► onglet STRATÉGIE ─────┤
hub usage/events ──hub_cockpit_feed──► hub.json (santé/budget/queue) ───┘
                              ▼
                     cockpit (lecture seule + STOP/panic)
```

**Chaîne onchain (la pépite « poussières »)** :
`detecter_cpfp.py` (3 cartes : z-score, signature CPFP, poussière) + `detecter_bloc_privatise.py` → `data/*.json` → `pont_onchain.py` → `live.json.onchain` → `mission.json` → cockpit + Cortana.

---

## 4. Ce qui était branché vs ce qui dormait

**✅ Branché et qui marche** : hub routeur (20 providers gratuits, bascule auto), cockpit (17777/17800/11435/11439 UP), ADA (voilure, saison, 6 indices), justesse, gate trades fail-closed, coffre_ask.

**⚠️ Qui dormait (existe mais pas câblé)** :
- `cortana_dashboard.py` : la « vue complète maison » n'était appelée nulle part.
- `system_state_generator.py` / `agent_status.py` : existent, branchés par plists, mais non lus par le chat.
- La donnée **poussières** (CPFP/dust) et **blocs privatisés** : tournaient mais ne sortaient jamais de `data/*.json` (mode observation) → invisibles pour ADA et Cortana.

**🧹 À simplifier** : contexte codé en dur de Cortana (remplacé), ~60 fichiers `.bak`, app Rust vocale (doublon en veille), qwen/signets.lot2 (inactifs → couper les plists). **MiroFish = atout à GARDER** (pause budgétaire — servira le moment venu).

**📈 À maximiser (offres trouvées dans les signets)** : `api-airforce` (grok-3, claude-3.7, kimi-k2.6, gemini-2.5-flash en quotas récurrents), `baidu/ernie-4.0` (gratuit sans plafond), `omniroute-free-tiers` (43 pools), AMD 10$/j.

---

## 5. Réparations du 18/08 (étapes 1-3)

**Étape 1 — Cortana voit tout le cockpit.** Remplacement du contexte codé en dur (2 CSV) par une lecture de `mission.json` (source unique) : ACE, Hulk, saison ADA, voilure, thermo, onchain, disjoncteur.
- Preuve : « quelle est la saison et l'onchain ? » → *« saison calme, voilure 91 zone vert, onchain neutre »* (avant : elle ne répondait que le PnL).

**Étape 2 — l'indice onchain « poussières » est branché.** La donnée CPFP (poussière < 2 sat/vB) + blocs privatisés remonte dans `live.json.onchain` → `mission.json` → contexte Cortana, **toujours visible, jamais d'alerte** (le signal actif reste verrouillé sur « actif + confirmation ≥ 2 »).
- Preuve : « quel est l'état de l'indice poussières ? » → *« 0 vues ce run, 0 cumulées 48h (seuil 1000). Blocs privatisés 27,61 % fantômes (observation) »*.

**Étape 3 — Recherche web à la demande.** Nouveau `recherche_web.py` (stdlib, gratuit, sans clé) : CoinGecko (marché + description + catégories = relations gros acteurs) + DuckDuckGo (résumé web). Déclenché dans le chat par « recherche/analyse <crypto|sujet> » → synthèse par le hub (task `cortana.analyse`).
- Preuve : « analyse la crypto solana » → faits (prix 76,94 $, cap 44,8 Md$, +1,27 %), résumé, relations (Multicoin Capital, Alameda, a16z, FTX), avis NEUTRE + sources.

Fichiers modifiés : `cortana_cockpit_bridge.py` (fonction `_contexte_bots` + `do_recherche` + déclencheur), `pont_onchain.py` (section `onchain` enrichie), `recherche_web.py` (nouveau).

---

## 6. À faire (étapes 4-5) + 2 GO à trancher

1. **📚 Coffre + AGORA** (étape 4) — brancher `coffre_ask` au chat + faire de l'AGORA le journal d'apprentissage vivant.
2. **🔧 Actions sûres** (étape 5) — réparer un index, alerter un gros mouvement, rappels de tâches.

**GO à trancher par Christophe (je ne les fais pas seul)** :
- **Passer le CPFP « poussières » en mode actif** (`detecter_cpfp.py --actif`) — prévu après validation 7 jours, **branche de vraies alertes** + modifie la voilure ADA (±10 %).
- **Ajouter l'onchain comme 7ᵉ indice ADA** — change le calcul de saison.

---

## 7. Garde-fous (non négociables)

- **C1** Champion genesis `37fca367…` intangible · **C2** 0 LLM dans le hot path · **C3** 1 GO = 1 vol · **C4** CSV = vérité · **C5** Mac M1 8 Go · **C7** drawdown 8 % · **C9** 0 IA locale (hub cloud = seule passerelle).
- **Doctrine** : « l'automation propose, l'humain approuve » · maker ≠ checker · jamais d'ordre sans GO.

---

*Généré par Buffy — à tenir à jour à chaque étape.*
