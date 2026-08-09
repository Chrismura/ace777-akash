# ⚙️ SCHÉMA DE FONCTIONNEMENT DU HUB (09/08/2026 — v3, grok branché)

> Comment le hub vit au quotidien : cycle automatique décalé (RAM 8 Go), checkup,
> auto-évaluation, observation 48 h, jauge à la demande. Source de vérité :
> `~/prise-ia/{providers.json, routing.json, .env}` + scripts `Index_Maison/scripts/`.
> Voir aussi `CATALOGUE_PROVIDERS.md` (généré chaque matin, 1 vue d'ensemble).

## 🕘 Le cycle quotidien — ORCHESTRATEUR TEMPOREL (correction famille 09/08)

```
09:05  veille_hub.py          scan seul : santé hub + énergie + 5 catalogues (dont Puter)
                              -> VEILLE_HUB_<date>.md (nouvelles offres non intégrées)
09:30  eval_offres.py         A/B RÉEL (offre vs meilleur actuel, VRAI JUGE) -> intégration
                              EN OBSERVATION (enabled:false = jamais routé) si GRATUIT+MIEUX
10:00  catalog_providers.py   -> CATALOGUE_PROVIDERS.md (1 vue : actifs/observation/attente/côté)
10:30  propose_ameliorations.py  backlog -> TOP 3 (juge) -> CONTRE-VÉRIF GEMINI -> Christophe
11:00  observatoire.py        sondes 5×/jour sur les providers en observation ; après 48 h :
                              erreurs >5% -> ROLLBACK AUTO ; sinon ACTIF après GO hebdo
```

- **Vérification auto** : après CHAQUE changement, `verifier_setup.py` (compile + hub + providers + routing + appel réel + launchd + soumission FAMILLE au brief auto-généré) → rapport `A_Mon_Attention/VERIF_SETUP_<date>.md`
- **Kill switch** : `Index_Maison/STOP_HUB` présent → toutes les étapes s'arrêtent SAUF le hub.
- **Jauge d'énergie** : plus de KeepAlive permanent → **à la demande** (`scripts/jauge.sh start|stop|status`, serveur :8898, auto-refresh 30 s). RAM libérée.

## 🧭 Routage (routing.json — tâche → provider + fallback, budget cloud 480/j)

```
ada.sanity / chat.local / qwen.*  -> qwen-local (Ollama, gratuit)  fallback: gemini
cortana.brief/analyse, coffre.ask -> GEMINI (voix, analyse)        fallback: qwen-local
signets.juge                       -> openrouter-juge (Nemotron 120B, maker≠checker)
ultra.analyse                      -> openrouter-ultra (Nemotron 550B) fallback: nvidia
analyse.profonde / mission         -> nvidia (DeepSeek V4 Flash)    fallback: GROK (Puter)
code.ia                            -> inferx-coder (Qwen3-Coder)    fallback: nvidia
signets.lot2                       -> openrouter-free               fallback: gemini
```

## 🤖 Providers ACTIFS (7 — 09/08, catalogue du jour)

| Provider | Modèle | Rôle |
|---|---|---|
| qwen-local | Qwen 2.5 3B (Ollama) | local, gratuit, démarrage/chat |
| gemini | Gemini Flash Lite | voix, analyse, coffre RAG |
| openrouter-free | GPT-OSS 20B :free | tri signets |
| nvidia | DeepSeek V4 Flash | analyses profondes, missions |
| openrouter-juge | Nemotron 3 120B | JUGE indépendant (maker≠checker) |
| openrouter-ultra | Nemotron Ultra 550B :free | analyse forte (meilleur mesuré) |
| **puter-grok** | **x-ai/grok-4.3 (Puter, gratuit)** | **complément résilience (GO Christophe 09/08), fallback mission** |

Puter = **500+ modèles avec le même token** (gpt-5.x, claude, gemini, deepseek…) —
candidats permanents de l'auto-éval (section `puter` de la veille).

## 🔁 Auto-évaluation + INTÉGRATION (protocole zéro faute, validé 4 familles)

```
veille (détection) -> eval_offres (A/B réel, juge famille différente)
  -> GRATUIT + MIEUX -> intégration ADDITIVE EN OBSERVATION (enabled:false, backup, atomique)
  -> observatoire (48 h de sondes) -> >5% erreurs = ROLLBACK AUTO ; sinon liste hebdo
  -> GO hebdomadaire Christophe (go_hebdo.json) -> ACTIF + NOTICE
Règle : AUCUN provider ne devient actif directement. Mesure, jamais réputation.
```

## 🗺️ La flottille — OÙ elle va chercher (liste des sources)

**A. Catalogues API (mécanique, chaque matin — veille_hub.py)**
1. OpenRouter → `/models` (filtre `:free`, quota 1000/j)
2. NVIDIA build → `/models`
3. InferX → `/models` (offre gratuite jusqu'au 12/08)
4. **Puter** (NOUVEAU 09/08) → modèles connus (gpt-5.4, claude-sonnet-4-5, grok-3-mini-fast, deepseek-v4-flash, gpt-4o) via token gratuit
5. Groq / Mistral / Cloudflare → `/models` (clés en attente)
6. **OmniRoute free-tiers** → catalogue 43 pools gratuits (`freeModelCatalog.data.ts`), MAJ bi-hebdo

**B. Flux veille (collecté en continu, trié en session)**
7. Signets X (`Signets_X/` dans le vault) — posts bookmarkés
8. Comptes suivis : @FareaNFts, @pengsonal, @slash1sol, @RoundtableSpace, @XFreeze…
9. **Agent-Reach** (venv `~/.agent-reach-venv`) : X/Reddit/YouTube/GitHub/RSS/web sans API payante

**C. Recherche web (flottille manuelle, en session)**
10. Hacker News / Reddit r/LocalLLaMA — annonces de modèles/offres
11. Pages tarifs des providers + roundups « free AI credits » + statut OpenRouter

**D. Mesure (avant d'intégrer)**
12. `eval_offres.py` / batterie A/B — même question, VRAI JUGE, preuve écrite

## 💡 Rituel d'amélioration proactive (corrige « tu ne proposes pas »)

```
Début de session : lire backlog (pépites INTEGRER + idées + veille)
  -> JUGE choisit TOP 3 -> GEMINI contre-vérifie (famille différente)
  -> A_Mon_Attention/PROPOSITIONS_AMELIORATIONS.md -> Christophe tranche
```

## 🧾 Journal / mémoire

- Événements : `~/prise-ia/events.jsonl` · usage : `~/prise-ia/usage.jsonl`
- Traçabilité : `test-freebuff/journal_erreurs.md` + `MEMOIRE_COLLAB.md` (★)
- Préférences/lois : POLITIQUE_OUBLI.md (1 info = 1 place), manifeste, PROTOCOLE_DELEGATION.md

_Archiver dans Obsidian (mémoire). Généré/mis à jour par Buffy le 09/08/2026._
