# TRI DES SIGNETS X — Synthèse (famille + Cortana) — 15/08/2026

**Source** : 200 signets X résumés (`SIGNETS_RESUMES.json`, 59k chars) · chacun a choisi ses **10 signets les plus utiles POUR LUI**, avec sa logique.

**Participants** : gemini ✅ · nvidia ✅ · cortana ✅ · openrouter-juge/ultra ❌ (HTTP 502, réseau — habituel chez nous)

---

## 🎯 Les intersections — choisis par ≥2 membres (le consensus)

| N° | Choisi par | Signet | Pourquoi (résumé) |
|---|---|---|---|
| **192** | **gemini + nvidia + cortana (3/3)** | @noisyb0y1 — Fuite Anthropic : **6 fichiers de suivi** (décisions, impasses, sources) au lieu de recharger l'historique | **−84% de tokens, +39% de précision** — la méthode d'organisation externe qui allège radicalement le coût |
| **12** | gemini + cortana | @tom_doerr — **Brain.md** : mémoire persistante en fichiers Markdown simples dans le repo | Nos agents (stratégie, audit, signets) gardent leur connaissance projet entre sessions, sans base de données |
| **53** | gemini + cortana | @franpradasAI — **TencentDB Agent Memory** : les agents mémorisent conversations, décisions, préférences | « Partie sauvegardée » — l'agent ne repart plus de zéro |
| **130** | nvidia + cortana | @_avichawla — **8 formats de précision** pour alléger les modèles (28 Go FP32 → 4 Go 4-bit) | Faire tourner nos modèles locaux sur 8 Go de RAM |
| **189** | gemini + cortana | @franpradasAI — **TradingAgents** : analyse de marché par agents autonomes open-source | Brique pour Hulk dip&rip + veille techno agents trading |

---

## Les choix de chacun (le reste)

### gemini — logique : contrainte matérielle stricte (8 Go RAM, hub local), optimisation tokens, archi agents
4 (Magnitude agent 100% local) · 44 (Kimi K3 sur CPU 8 Go) · 50 (3 schémas de workflow Anthropic) · 70 (spec-kit : spec avant code) · 142 (BitNet LLM 100B sur CPU) · 169 (12 libs Python données de marché) · + les 5 du consensus (12, 53, 189, 192)
**Verdict : PARTIEL**

### nvidia — logique : fiabilité multi-agents, gestion des risques, optimisation coûts ; écarte le « gratuit » déjà couvert
6 (LLMRouter 16+ modèles) · 15 (MPP : agents paient des services) · 30 (10 tests verts ≠ validé — Release Receipt 6 points) · 31 (trou de responsabilité multi-agents) · 43 (Burry : c'est le **sizing** qui compte) · 68 (trader top 0,04% WorldQuant qui réécrit ses stratégies perdantes) · 105 (paradoxe de Saint-Pétersbourg → critère de Kelly pour le sizing) · 124 (7 méthodes anti-hallucinations) · 130 · 192
**Verdict : OUI**

### cortana — logique : RAM 8 Go, persistance locale Markdown, orchestration multi-agents, combler l'écart vers 93%
5 (OmniParse → Markdown structuré pour nourrir son analyse) · 60 (boucles autonomes plutôt que prompts — Boris Cherny) · 111 (CheckCle : supervision CPU/RAM du hub) · 125 (AgentSwarms : essaim d'agents + dashboard) · 179 (MARCD : simulation de krachs extrêmes) · + consensus (12, 53, 130, 189, 192)
**Verdict : OUI**

---

## 🧠 Avis de supervision (Buffy)

**Ce tri valide ta question d'hier** : les signets sont une **vraie mine**, et chacun a choisi selon SON rôle — c'est exactement la logique qu'on veut voir.

1. **Le consensus 192 (fichiers de suivi Anthropic, −84% tokens)** est frappant : les 3 l'ont pris indépendamment. C'est **déjà presque notre philosophie** (Mémoire collab + fichiers par chantier) — le signet confirme et affine la méthode. → **Action directe possible**.
2. **Deux familles de pépites émergent** : (a) **alléger/exécuter local** (44, 130, 142, 4 — contrainte 8 Go), (b) **fiabiliser les agents** (30, 31, 124 — notre doctrine famille/juge/codeur en sort renforcée), (c) **sizing/risque** (43, 105, 68 — nourrit directement le chantier « 2 classes » et la discipline).
3. **Cortana choisit utile pour elle-même** (mémoire, orchestration, supervision hub, krachs) — sa logique est cohérente avec son rôle de cerveau. Bon signe.
4. **Mon tri prioritaire pour toi** (si on ne garde que 5 à creuser maintenant) : **192** (tokens, applicable tout de suite) → **43+105** (sizing/risque = chantier 2 classes) → **53/12** (mémoire agents) → **30/31** (garde-fous production).

**Aucune action appliquée** — c'est un tri, pas un chantier. À toi de choisir avec moi ce qu'on garde/creuse.

Fichiers bruts : `scripts/TRI_SIGNETS_20260815/CHOIX_{gemini,nvidia,cortana}.md`
