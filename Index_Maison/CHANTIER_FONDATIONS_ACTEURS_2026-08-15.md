# 🚧 Chantier — FONDATIONS DES ACTEURS (15/08/2026)

> **Rôle :** poser les fondations de l'équipe d'acteurs ACE777 (Ada, Cortana, Qwen, MiroFish) — rôles clairs, un seul aiguilleur, une identité par acteur, une justesse qui note vraiment.
> **Validé :** Christophe 15/08 — « je valide 100 %, poser fondation chantier, soumettre à la famille ».
> **Statut :** ✅ validé famille 4/4 (GO) — ordre F1→F2→F3→F4→F5 · verdict + améliorations : `scripts/CONSULTATION_FAMILLE_FONDATIONS_ACTEURS_20260815/VERDICT_FAMILLE.md` · en attente du GO de Christophe pour lancer F1.
> **Loi :** 1 chantier = 1 GO · champion intouchable · jamais de LLM dans la boucle d'ordre (C2/C3) · 8 Go (C5).

---

## 🧭 La vision (validée Christophe)

| Acteur | Rôle | Horizon |
|---|---|---|
| **Ada** | Gardienne + horizon : saison, bascule de tendance, voilure, gros mouvements | Long terme |
| **Cortana** | Cerveau / dashboard : sait tout, répond écrit + voix, analyste court terme ACE + Hulk | Court terme |
| **Qwen** | Apprentie junior : propose, ne décide jamais, notée par le professeur | Apprentissage |
| **MiroFish** | Simulation sociale multi-agents (scénarios, jamais d'exécution) | Froid |

**Principe :** garder les RÔLES (la spécialisation = la richesse), simplifier les CERVEAUX (un seul aiguilleur = le hub).

---

## Les 5 fondations

### F1 — Réparer la justesse (le professeur qui note juste)
**Quoi :** `score_justesse.py` note aujourd'hui TOUT contre le prix BTC uniquement. Une analyse de `funding`/`fearGreed`/`verre` est jugée « HIT/MISS » selon que le BTC a monté/descendu 24h plus tard — l'indice analysé n'est jamais vérifié contre lui-même. NEUTRE n'est pas noté (échappatoire). Seuil de victoire trop lâche (+0,05 %). Bug : `justesse_cockpit.json[derniere]` = la première analyse, pas la dernière.
**Pourquoi :** c'est le prérequis n°1 avant toute autonomie future de Cortana — on ne fait confiance qu'à une note vraie.
**Correctif :** (a) juger chaque indice contre sa propre évolution (mapping indice → métrique à comparer), (b) noter aussi le NEUTRE (un NEUTRE sur un marché qui bouge fort = miss d'opportunité, à définir), (c) seuil réaliste (ex. 0,3 %), (d) fixer `derniere`.
**Risque :** nul pour le trading (lecture seule). Touche `score_justesse.py` + éventuellement `justesse_cockpit.json`.
**✅ FAIT (15/08)** : `score_justesse.py` v2 (seuil 0,3 % · NEUTRE noté · self-move par indice · `derniere` fixé · sortie `justesse_v2.json` + compat cockpit). Tests hermétiques 8/8 verts. **Backfill 93 analyses → justesse réelle = 44 % (37/84)** — la note honnête est SOUS le pile-ou-face (l'ancienne 57 % était gonflée par le seuil 0,05 % + l'échappatoire NEUTRE). Conséquence : AUCUNE autonomie avant d'avoir compris POURQUOI 44 %.

### F2 — Carte d'identité ACE777 + une identité canon par acteur
**Quoi :** un fichier canon unique « Carte d'identité ACE777 » (carrosserie : duo BETA/ALPHA, Hulk, cockpit, hub, vault · moteur : genesis, scalper, duo scout/hunter · philosophie : Constitution, coutumes, essaim · stratégie : dip&rip Hulk, revenge duo) injecté au boot de chaque acteur. + un prompt canon par acteur (Ada, Cortana, Qwen) au lieu des identités dispersées (`persona.rs` générique, `PROMPT_MASTER_ANALYSTE`, prompts inline dans `qwen_*.py`).
**Pourquoi :** qu'un acteur « incarne » ACE777 dès la première seconde, automatisé, sans réinventer à chaque session.
**Risque :** aucun (documentation + prompts). Ne touche pas au champion.
**✅ FAIT (15/08)** : carte `Index_Maison/identity/ace777_core.md` (v1.1) + version compacte `ace777_core_compact.md` (~350 tokens, Qwen 4b) + prompts canon `prompts/{ada,cortana,qwen}.md`. Famille 4/4 GO-avec-réserve (~88 %) → réserves appliquées : C5 aligné (Cortex=hub local/gratuit), TTL/heartbeat retiré de la carte, horizons AVIS STRICT harmonisés (24h/48h/semaine), traçabilité (sources + 1 ligne mémoire + score<60%→NEUTRE), seuil source dégradée Ada, sortie JSON Ada. SHA-256 calculés (traçabilité boot). **Reste (hors F2)** : brancher l'injection au boot des acteurs (F4/F5).

### F3 — Cortana = dashboard : étendre l'analyste à ACE + Hulk
**Quoi :** `cortana_analyse.py` ne lit aujourd'hui que les indices BTC (thermo). L'étendre à : (a) les fills ACE (`runs/*.csv`, mission.json) et (b) Hulk (`hulk-mexc/runs/PAPER_V1_*.csv` + `.veille_status.json`). + unifier la voix sur le hub (une seule route).
**Pourquoi :** Cortana doit être l'analyste court terme d'ACE ET de Hulk, et répondre à « que s'est-il passé / que faire » sur les deux moteurs, écrit + voix.
**Risque :** lecture seule (fichiers CSV/JSON existants). Ne touche ni au moteur ni aux ordres.
**✅ FAIT (15/08)** : `scripts/cortana_dashboard.py` — module de normalisation (schéma unique ACE+Hulk+marché), sortie `strategie/cortana_snapshots/cortana_snapshot_{ts}.json` (rotation 50), synthèse via hub (task cortana.analyse, identité Cortana canon). Tests hermétiques 7/7. Améliorations famille intégrées : schéma unique, snapshot standard, rotation, PnL par raison (`pnl_by_reason`), sources listées. **1ʳᵉ synthèse live : 29 revenge/~38 fills ALPHA récents (76 %) + PnL négatif — confirme le diagnostic revenge.**

### F4 — Un seul aiguilleur : le hub
**Quoi :** le Rust (`brain.rs`) a sa propre logique parallèle Gemini/Ollama/hub, en doublon de `routing.json`. Le simplifier pour qu'il n'appelle QUE le hub (la rotation auto y est déjà). `app.toml` obsolète (`qwen2.5:3b`) à aligner.
**Pourquoi :** une seule source de vérité pour « qui répond à quoi ». Supprime l'incohérence 3 cerveaux pour la voix.
**Risque :** touche le Rust (app vocale, hors champion). Repli Ollama à conserver comme filet hors-ligne via le hub (`qwen-local`).

### F5 — Nettoyer le prompt voix (persona.rs)
**Quoi :** retirer « peut exécuter des ordres Binance dictés à la voix » (contredit C2/C3 : Cortana n'est autorisée à rien aujourd'hui). Greffer la Carte d'identité ACE777 + son rôle dashboard (F2).
**Pourquoi :** poser des fondations honnêtes — l'autonomie viendra plus tard, après validation + garde-fous déterministes (Risk Guardian C7), jamais avant.
**Risque :** aucun (prompt). Aligne le texte sur la doctrine.
**✅ FAIT (15/08)** : `crypto-voice-assistant-core/src/live/persona.rs` édité — « peux exécuter des ordres d’achat/vente Binance » → « LECTURE SEULE, aucun ordre, aucune action, validation humaine explicite de Christophe » + identité ACE (duo BETA/ALPHA, Hulk paper). **✅ REBUILD FAIT (15/08 14:56)** : `cargo build --release` OK (50s) hors run — binaire contient « validation humaine », ancienne phrase « exécute des ordres Binance » absente. Prise d'effet au prochain lancement Cortana.

---

## ⚠️ Rappels hors périmètre (ne pas toucher)
- Genesis champion (`8d9ee8d6` → `fe2a7bcc`) : intouchable ici.
- Aucun ordre, aucune autonomie accordée dans ce chantier.
- Qwen locale est en pause (10/08) — son rebranchement est une décision séparée (pas dans ce chantier).

## 🔗 Connexions
[[CHANTIERS]] · [[PROTOCOLE_PROMPTING]] · [[ACE777-Constitution]] · [[ADA_CONNAISSANCE_MAISON]] · [[PROMPT_MASTER_ANALYSTE]] · [[MEMOIRE_COLLAB]]
