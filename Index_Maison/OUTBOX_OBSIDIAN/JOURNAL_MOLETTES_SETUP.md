# Journal des molettes / setups (qui · quoi · pourquoi)

**Rôle :** une seule page — **chaque changement de setup** (ON/OFF, défaut, commande) avec **qui** et **pourquoi**.  
Sans ça → l’autre IA (et nous) jugent faux.

**Règle :** 1 ligne (ou 1 bloc) **dans la même session** que le changement. Pas « on classera ce soir ».

**Pas ici :** fills PnL (→ CSV / CONSOLE) · cosmétique cockpit.

---

## Comment lire

| Colonne | Sens |
|---------|------|
| ts | UTC |
| Qui | Humain / Cursor / script |
| Molette | nom env (`NUAGE_…`) |
| Avant → Après | état |
| Pourquoi | **obligatoire** — 1–3 phrases |
| Run / preuve | tag ou « pas encore » |

---

## Journal (récent en haut)

### 2026-08-12 — `LLM_OLLAMA_URL` http://127.0.0.1:11434 → http://127.0.0.1:11439

| | |
|--|--|
| **Qui** | Buffy |
| **Molette** | `LLM_OLLAMA_URL` |
| **Avant → Après** | http://127.0.0.1:11434 → **http://127.0.0.1:11439** |
| **Pourquoi** | bascule gate trades de l IA locale vers le pont hub (directive plus d IA locale) |
| **Preuve** | pas encore |
| **ts** | 2026-08-12T17:34Z |



### 2026-08-12 — `VORTEX_LLM_BUDGET_SEC` 1.2 → 20

| | |
|--|--|
| **Qui** | Buffy |
| **Molette** | `VORTEX_LLM_BUDGET_SEC` |
| **Avant → Après** | 1.2 → **20** |
| **Pourquoi** | profil vortex_v2_collab ecrasait le budget -> juge classe llm_slow au lieu de llm_wind (revue famille) |
| **Preuve** | pas encore |
| **ts** | 2026-08-12T17:34Z |



### 2026-07-31 — `NUAGE_STORM_HUNTER` 0 → OFF défaut · E-07 retest

| | |
|--|--|
| **Qui** | Cursor+Humain |
| **Molette** | `NUAGE_STORM_HUNTER` |
| **Avant → Après** | 0 → **OFF défaut · E-07 retest** |
| **Pourquoi** | Confirmé journal auto: défaut OFF usine; retest GO plus tard (cycle 14:14) |
| **Preuve** | JOURNAL_MOLETTES + E-07 |
| **ts** | 2026-07-31T14:34Z |



### 2026-07-31 — STORM_HUNTER à retester (pas encore remis ON)

| | |
|--|--|
| **Qui** | Christophe + Cursor |
| **Molette** | `NUAGE_STORM_HUNTER` |
| **État actuel** | **OFF** (défaut `GO_USINE` = `0`) |
| **Action** | 🟡 **à faire** — option setup, **pas oubliée** · pas de GO aujourd’hui |
| **Pourquoi on l’avait laissé OFF (défaut usine)** | 1) Retour baseline « usine » : **1 molette à la fois**, revenge duo = chemin normal. 2) Avec STORM_HUNTER, Alpha peut **armer sans perte scout** (anti `no_trigger`) — utile en mèche, mais plus agressif / risque de coups hors discipline scout. 3) Terrain : même armé, `spread_too_wide` / `tension_stale` peuvent quand même bloquer le fill (cf. cycle 14:14 31 juil. — shockwave OK, Alpha skip spread). 4) Briefing 23 juil. avait **toutes** les storm ON ; depuis, relances souvent **sans** repasser le paquet storm → défaut 0 = « safe forget ». |
| **Pourquoi on veut le retester** | Aujourd’hui Beta claque + shockwave ; Alpha silencieux à cause du **spread** — STORM_HUNTER élargit la fenêtre hunter en tempête (K2). À mesurer en **A/B** vs baseline, pas en fantaisie. |
| **Comment (plus tard, GO explicite)** | `NUAGE_STORM_HUNTER=1` (+ idéalement LATCH/HOLD comme stack 23 juil.) · 4h · une molette claire |
| **Réf** | [[engle/PLAN_STORM_WICK]] · [[BRIEFING_ACE_DERNIER_SETUP_20260727]] · cycle LIVE 31 juil. 14:14 |

### 2026-07-23 — référence « dernière stack qui a tourné » (toutes storm ON)

| | |
|--|--|
| **Qui** | Humain (prod testnet) |
| **Molettes** | BIDIR=1 · STORM_LATCH=1 · STORM_HOLD=1 · **STORM_HUNTER=1** · MIN_ENTRY 2.5 puis 3.0 |
| **Pourquoi** | Pack tempête complet (K1+K2+K3) — Alpha pouvait armer sans attendre revenge |
| **Preuve** | Combo matin ≈ +13.8 · après-midi ≈ +8.1 · **caveat** 1 gros trade Alpha |
| **Réf** | [[BRIEFING_ACE_DERNIER_SETUP_20260727]] |

### 2026-07-21 — K2 STORM_HUNTER créé (E13)

| | |
|--|--|
| **Qui** | Cursor + plan Engle |
| **Pourquoi** | Répondre à `duo no_trigger` + `spread_too_wide` pendant le pic (Alpha dormante pendant mèche) |
| **Réf** | [[engle/PLAN_STORM_WICK]] |

---

## Molettes connues (aide-mémoire — défauts GO_USINE)

| Molette | Défaut | Sens court |
|---------|--------|------------|
| `NUAGE_DUO_PID_WATCHDOG` | 1 | Relance jambe morte |
| `NUAGE_BIDIR_SIDES` | 0* | Sens dynamiques (*vérifier banner boot) |
| `NUAGE_STORM_LATCH` | 0 | Bypass Mode Écoute si tension haute |
| `NUAGE_STORM_SCOUT_HOLD` | 0 | Hold min en tempête |
| `NUAGE_STORM_HUNTER` | **0** | Alpha percute sans revenge scout |
| `NUAGE_MIN_ENTRY_TENSION` | (si set) | Filtre entrée |

\*Confirmer sur le banner `GO_USINE` au boot — la vérité = le log du run.

---

## Liens

[[CHOSES_A_FINIR_REVOIR]] · [[PLAN_DE_VOL]] · [[BRIEFING_ACE_DERNIER_SETUP_20260727]] · [[engle/PLAN_STORM_WICK]] · [[REGLES_SCRIPTS_SETUPS]] · [[SAUVEGARDE_SETUP_ACTUEL]]
