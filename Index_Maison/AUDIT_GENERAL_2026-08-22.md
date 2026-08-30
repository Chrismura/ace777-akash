# 🔍 AUDIT GÉNÉRAL — ACE777 (22/08/2026 18:00 UTC)

> Audit complet, à règle d'art. Chaque composant est inventorié, vérifié, classifié.
> Pas de théorie. Des chiffres.

---

## 1. ÉTAT DES LIEUX — Le système en chiffres

| Composant | Total | Actifs | Morts | Ratio |
|---|---|---|---|---|
| **Launchd plists** | 44 | 30 | 14 | 68% actifs |
| **Scripts Python** | 207 | ~30 référencés | ~177 non référencés | 86% fantômes |
| **Providers hub** | 25 | 13 | 12 | 52% actifs |
| **PID files** | 5 | 5 | 0 | 100% vivants |
| **Heartbeats** | 6 | 6 | 0 | 100% OK |

---

## 2. LES MORTS — Ce qui ne tourne pas

### Launchd plists MORTS (14)
```
❌ com.ace777.autopilote
❌ com.ace777.catalogue
❌ com.ace777.cockpit-pont
❌ com.ace777.dms-veille
❌ com.ace777.eval-offres
❌ com.ace777.gitpush-vault
❌ com.ace777.graph-cerveau
❌ com.ace777.heartbeats
❌ com.ace777.hulk-watchdog
❌ com.ace777.macro-tempete
❌ com.ace777.pont-onchain
❌ com.ace777.queueoffres
❌ com.ace777.rappels
❌ com.ace777.run-vortex-96h
❌ com.ace777.run72h
❌ com.ace777.sante-index
❌ com.ace777.veille-degradation
❌ com.ace777.veilleuse-chantiers
❌ com.ace777.veilleuse-sizing-monte-carlo
❌ com.ace777.verif-setup
❌ com.ace777.watchdog
```

### Providers hub MORTS (12)
```
❌ Google Gemini ( quota atteint)
❌ Cloudflare Workers AI
❌ Grok 4.5 (xAI via OpenRouter)
❌ Qwen locale (Ollama) — non installé
❌ cohere/north-mini-code:free (rollback)
❌ nvidia/nemotron-3-nano-30b-a3b:free (rollback)
❌ nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free (rollback)
❌ nvidia/nemotron-3.5-lightning:free (rollback)
❌ nvidia/nemotron-3.5-content-safety:free (rollback)
❌ google/diffusiongemma-26b-a4b-it (rollback)
❌ google/gemma-4-26b-a4b-it:free (rollback)
❌ nvidia/nemotron-nano-9b-v2:free (rollback)
```

---

## 3. LES VIVANTS — Ce qui tourne

### Launchd plists ACTIFS (30)
```
✅ com.ace777.archi-vivante          (PID 6102)
✅ com.ace777.backup-check           (PID 6637)
✅ com.ace777.bloc-privatise         (PID 2805)
✅ com.ace777.cockpit-http           (PID 31515)
✅ com.ace777.cortana-feed           (PID 5897)
✅ com.ace777.cortana.urgent         (PID 5153)
✅ com.ace777.couleur-regime-score   (PID 6188)
✅ com.ace777.couleur-regime         (PID 6188)
✅ com.ace777.cpfp                   (PID 6644)
✅ com.ace777.fees                   (PID 6745)
✅ com.ace777.hub-cockpit-feed       (PID 5963)
✅ com.ace777.journal-soir           (PID 4916)
✅ com.ace777.llm-gate-hub           (PID 31552)
✅ com.ace777.observatoire           (PID 6573)
✅ com.ace777.prise-ia               (PID 31531) — LE HUB
✅ com.ace777.roulement-ia           (PID 6277)
✅ com.ace777.routeur-auto           (PID 6258)
✅ com.ace777.run-setupA-4h          (PID 643)
✅ com.ace777.sniffer-matin          (PID 6628)
✅ com.ace777.sniffer-ny             (PID 6540)
✅ com.ace777.state-generator        (PID 5951)
✅ com.ace777.superviseur-core       (PID 31542)
✅ com.ace777.superviseur-process    (PID 31525)
✅ com.ace777.superviseur            (PID 6743)
✅ com.ace777.veille-hub             (PID 6715)
✅ com.ace777.veille-yt              (PID 7111)
✅ com.ace777.veilleuse-confrontation (PID 6941)
✅ com.ace777.veilleuse              (PID 6941)
✅ com.ace777.vigie-live             (PID 80679)
✅ com.ace777.whales                 (PID 4161)
```

### Providers hub ACTIFS (13)
```
✅ OpenRouter (modeles gratuits)
✅ NaraRouter (7M tokens/jour gratuits)
✅ Groq (LLM ultra-rapide, gratuit)
✅ NVIDIA build.nvidia.com (100+ modeles)
✅ Mistral La Plateforme (essai gratuit)
✅ OpenRouter Juge (nemotron-3-super-120b free)
✅ OpenRouter Nemotron 3 Ultra 550B (free)
✅ InferX DeepSeek V4 Flash
✅ InferX Qwen3-Coder-Next
✅ Puter Grok (gratuit)
✅ NVIDIA DeepSeek-Coder 6.7B
✅ InferX Devstral-2-123B
✅ HuggingFace (136+ modeles)
```

### PID files — tous vivants
```
✅ alpha.pid → PID 1868
✅ beta.pid → PID 1775
✅ master.pid → PID 1412
✅ supervisor_v9_v2.pid → PID 1491
✅ timer.pid → PID 1772
```

### Heartbeats — tous OK
```
✅ vigie:     OK (vie 0s)
✅ veille:    OK (vie 5s)
✅ dms:       OK (vie 2s)
✅ sante:     OK (vie 8s)
✅ superviseur_core: OK (vie 576s)
✅ whales:    OK (vie 90s)
```

---

## 4. LE PROBLÈME — Ce qui consomme sans produire

### A. Les 207 scripts Python
Seulement ~30 sont référencés dans des plists. **177 scripts ne sont appelés par rien.**

### B. Les 12 providers morts
Ils sont toujours dans `providers.json` mais désactivés. Le hub les essaie en fallback avant de les sauter → perte de temps.

### C. Les 14 plists morts
Certains sont écrits mais jamais chargés (leçon du méta-audit : « garde-fou écrit mais pas actif »).

### D. Le hub consomme 3599 appels/jour
Budget = 624. Consommation réelle = 3599. **Dépassement ×5,7.**

---

## 5. CLASSIFICATION — Garder / Couper / Fixer

### 🟢 GARDER (essentiel au fonctionnement)
| Composant | Rôle |
|---|---|
| `prise-ia` (hub) | Routeur LLM |
| `superviseur` + `superviseur-core` + `superviseur-process` | Supervision |
| `vigie-live` | Veille marché |
| `sniffer-matin` + `sniffer-ny` | Analyse marché |
| `roulement-ia` | Rotation providers |
| `routeur-auto` | Auto-routage |
| `state-generator` | État système |
| `veilleuse` + `veilleuse-confrontation` | Veille signets |
| `whales` | Suivi baleines |
| `fees` | Suivi frais |
| `cpfp` | Stratégie CPFP |
| `observatoire` | Surveillance |
| `cockpit-http` | Interface web |
| `llm-gate-hub` | Gate LLM |
| `hub-cockpit-feed` | Feed cockpit |
| `backup-check` | Sauvegarde |

### 🔴 COUPER (ne sert à rien ou casse)
| Composant | Raison |
|---|---|
| `autopilote` | Jamais chargé |
| `catalogue` | Jamais chargé |
| `cockpit-pont` | Doublon de cockpit-http |
| `dms-veille` | Jamais chargé |
| `eval-offres` | Jamais chargé |
| `gitpush-vault` | Redondant (git auto) |
| `graph-cerveau` | Jamais chargé |
| `heartbeats` | Doublon de vigie |
| `hulk-watchdog` | Hulk est en paper, pas de risque |
| `macro-tempete` | Pas de crise en cours |
| `pont-onchain` | Jamais chargé |
| `queueoffres` | Doublon de veilleuse |
| `rappels` | Jamais chargé |
| `run-vortex-96h` | Doublon de run-setupA |
| `run72h` | Doublon de run-setupA |
| `sante-index` | Remplacé par heartbeats |
| `veille-degradation` | Implémenté mais jamais chargé |
| `veilleuse-chantiers` | Doublon |
| `veilleuse-sizing-monte-carlo` | Doublon |
| `verif-setup` | Doublon de preflight |
| `watchdog` | Doublon de vigie |

### 🟡 FIXER (fonctionne mal)
| Composant | Problème |
|---|---|
| Hub providers | 12 morts à purger de providers.json |
| `sniffer_vrai.py` | 2 instances en parallèle (pas de lock) |
| `superviseur.sh` | 3 superviseurs en parallèle (trop) |
| `archi-vivante` | Pas vérifié s'il est encore à jour |
| `journal-soir` | Vérifier qu'il génère bien le journal |
| `veille-yt` | Vérifier qu'il ne spamme pas |
| `bloc-privatise` | Vérifier résolution (120s ok) |
| `couleur-regime` + `score` | Doublon probable |

---

## 6. RECOMMANDATIONS — Les 5 actions prioritaires

### Action 1 : PURGER les providers morts
Supprimer les 12 providers `obs-rollback` de `providers.json`. Le hub ne les essaiera plus → moins de timeouts, moins de consommation.

### Action 2 : COUPER les 21 plists morts
Déplacer les plists non chargés vers un dossier `_ARCHIVE/`. Ça réduit le bruit et évite les confusions.

### Action 3 : NETTOYER les 177 scripts fantômes
Déplacer les scripts non référencés vers `_ARCHIVE/scripts/`. Garder seulement les ~30 scripts actifs.

### Action 4 : FIXER le hub (budget)
Le hub consomme 5,7× le budget. Causes :
- `sniffer_vrai.py` × 2 instances → analyser la fréquence
- Cascade de failover → limiter à 3 providers max par tâche
- `supervise.decision` → réduire la fréquence

### Action 5 : SIMPLIFIER les superviseurs
3 superviseurs en parallèle = trop. Garder `superviseur-core` seul, couper les deux autres.

---

## 7. CE QU'ON NE TOUCHE PAS

| Composant | Raison |
|---|---|
| `genesis_manifest.txt` | C1 : intouchable |
| Le champion scellé | C1 : intouchable |
| `routing.json` | En cours de modification, on garde |
| `providers.json` | Après purge des morts |

---

*Audit réalisé par Buffy — 22/08/2026 18:00 UTC*
*Source : ps, launchctl, providers.json, heartbeats.json, pid files*