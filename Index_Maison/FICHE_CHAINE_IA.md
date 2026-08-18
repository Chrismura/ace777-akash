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
| **Coffre (RAG)** | Question → recherche vault Obsidian → réponse sourcée | `coffre_ask.py` | 🟢 **branché au chat** (18/08) |
| **Recherche web** | Analyse une crypto/sujet sur le net (CoinGecko + DuckDuckGo) → synthèse hub | `recherche_web.py` | 🟢 (branché au chat) |
| **Dashboard Cortana** | Vue complète maison (ACE+Hulk+marché) + synthèse | `cortana_dashboard.py` | ⚠️ dort (non branché au chat) |
| **État système** | state.json : services, hub, RAM, fraîcheur des feeds | `system_state_generator.py` | 🟢 |
| **Santé des index** | Vérifie chaque chaîne de bout en bout + alerte vocale | `sante_index.py` | 🟢 |
| **Auto-réparation** | Relance bornée des services de monitoring cassés (whitelist, backoff, circuit-breaker) | `auto_reparer.py` | 🟡 observation (dry-run) |
| **Rappels** | « rappelle-moi X à HH:MM » → alerte vocale à l'heure dite | `rappels.py` + plist 60 s | 🟢 branché au chat |
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

**Étape 4 — Coffre branché + AGORA vivante.**
- `coffre_ask.py` (RAG Obsidian, zéro dépendance) est branché au chat : « que dit le coffre sur X », « dans le coffre », « dans ma mémoire »… → réponse sourcée + voix.
- L'AGORA devient un journal **vivant** : (a) **relire** — les leçons actives (`lecons_agora`, namespace cortana, TTL 7 j) sont injectées dans le chat ; (b) **écrire** — chaque recherche/coffre trace 1 ligne dans `Swarm_Bus/09_MEMOIRE_COLLAB.md` (canon) + miroir `Index_Maison/MEMOIRE_COLLAB.md` (append-only, idempotent).
- Preuve 1 : « que dit le coffre sur la politique d'oubli » → réponse sourcée (`POLITIQUE_OUBLI.md`…), provider Google Gemini.
- Preuve 2 : le chat applique sa leçon — à la question « salut », Cortana répond que le *fear & greed à 41 « nécessite la corroboration d'autres indicateurs »* (sa leçon AGORA `fearGreed`).
- Découverte : le script de trace auto `memoire_log.py` (référencé partout) avait disparu — la trace est maintenant ré-intégrée directement dans le pont.

**Étape 5 — Actions sûres et autonomes** (validée par le **codeur + famille/juge** : verdict unanime **GO-AVEC-RÉSERVE**, confiance moyenne).
- **Auto-réparation** (`auto_reparer.py`) : relance bornée des services de monitoring cassés, avec les réserves de la famille — backoff exponentiel (1/5/15 min), circuit-breaker CPU/RAM (load>6 ou swap>2 Go), vérif hub, mutex fcntl, journal d'audit `reparations.jsonl`, max 3 essais/24 h, cooldown 10 min. **En mode observation (dry-run) par défaut** : détecte + trace ce qu'il *réparerait*, ne relance rien. Bascule actif = marqueur `AUTO_REPARER_ACTIF` (GO humain). Hooké dans `sante_index.py` (5 min).
- **Rappels** (`rappels.py`) : « rappelle-moi X à HH:MM » → alerte vocale à l'heure dite. Commandes ajouter/lister/supprimer branchées au chat + plist `com.ace777.rappels` (60 s).
- **Gros mouvement** : déjà branché (`surveiller_whales.py` → `pont_onchain.py` `alerte_bool` → `live.json.onchain` → ADA + `vigie_live.py` → `alarme.json` → `analyste.py --speak`). Vérifié, pas reconstruit.
- Preuve rappels : « rappelle-moi vérifier le disjoncteur à 23:59 » → enregistré → listé → supprimé. ✅

Fichiers modifiés : `cortana_cockpit_bridge.py` (`_contexte_bots`, `do_recherche`, `do_coffre`, `do_rappel`, `_agora_trace`, `_lecons_agora_actives`), `pont_onchain.py`, `sante_index.py` (hook auto-réparation), `recherche_web.py`, `auto_reparer.py`, `rappels.py`, `com.ace777.rappels.plist` (nouveaux).

---

## 6. GO à trancher par Christophe (je ne les fais pas seul)

- **Passer l'auto-réparation en actif** : poser le marqueur `Index_Maison/strategie/AUTO_REPARER_ACTIF`. Avant ça, elle reste en observation (trace, ne relance rien).
- **Passer le CPFP « poussières » en mode actif** (`detecter_cpfp.py --actif`) — prévu après validation 7 jours, **branche de vraies alertes** + modifie la voilure ADA (±10 %).
- **Ajouter l'onchain comme 7ᵉ indice ADA** — change le calcul de saison.

---

## 7. Garde-fous (non négociables)

- **C1** Champion genesis `37fca367…` intangible · **C2** 0 LLM dans le hot path · **C3** 1 GO = 1 vol · **C4** CSV = vérité · **C5** Mac M1 8 Go · **C7** drawdown 8 % · **C9** 0 IA locale (hub cloud = seule passerelle).
- **Doctrine** : « l'automation propose, l'humain approuve » · maker ≠ checker · jamais d'ordre sans GO.

---

*Généré par Buffy — à tenir à jour à chaque étape.*
