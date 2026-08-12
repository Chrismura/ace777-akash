# ⚖️ SYNTHESE FAMILLE — SPEC SETUP DES 3 ETAGES (Grok) — 2026-08-10

**Dossier soumis :** DOSSIER_SPEC_3ETAGES_FAMILLE_2026-08-10.md (spec Grok intégrale)
**Modèles réels (vérifiés usage.jsonl — leçon 16:25) :** Gemini (gemini-flash-lite) · DeepSeek (deepseek-v4-flash) · Juge (nemotron-3-super-120b, VRAI) · Ultra (nemotron-3-ultra-550b, VRAI)

---

## ⚖️ VERDICT : VALIDE AVEC MODIFICATIONS (unanime) — confiance haute ×1, moyenne ×2, (Ultra = critique, réponse tronquée avant ligne de verdict)

**Personne ne refuse le setup. Personne ne le valide tel quel.** 3 familles rendent un verdict explicite (Gemini haute, DeepSeek moyenne, Juge moyenne) ; Ultra identifie 3 contradictions graves mais sa réponse a été tronquée par le provider avant la ligne finale.

---

## CONSENSUS (les 4 s'accordent)

| # | Consensus | Détail |
|---|---|---|
| C1 | **Inventaire exact des 27 services AVANT toute suppression** (Étape 0) | `launchctl list` + `launchctl print` par service + dépendances inter-services + budget RAM mesuré par service (Ultra : « sans inventaire, réduction 27→13 = tir à l'aveugle » ; 24/27 services sont morts/zombies — anomalie surveillance-quotas PID 0) |
| C2 | **`KeepAlive:false` + `ThrottleInterval:1800` = FAUX** | Avec KeepAlive:false, launchd ne relance jamais le superviseur après sa sortie → il ne tourne qu'une fois. Remplacer par `StartInterval:1800` (Juge + DeepSeek) ou `KeepAlive:true` + boucle interne sleep 60-120s (Gemini). Un heartbeat à 30 min n'en est plus un. |
| C3 | **Backup plists obligatoire avant Étape 4** | Copie tar de ~/Library/LaunchAgents + checksums (DeepSeek, Juge) + test de réversibilité (restore + reload) avant de passer à l'étape suivante |
| C4 | **Ne PAS toucher cockpit-http/pont au départ** | cockpit.py doit d'abord LIRE/cohabiter avec eux, ne les remplacer qu'après avoir exposé la même API et basculé les consommateurs (Gemini, Ultra) |
| C5 | **Unload un par un avec test 10 min** | Étape 4 : un service désactivé à la fois + délai de test (Gemini) + audit des dépendances avant chaque suppression (DeepSeek) |
| C6 | **Mode probatoire C6 + boucle 30 min = CONTRADICTION** | 48 cycles/jour vs 1 action/jour → soit C6 = « 1 type d'action/jour », soit observation seule (dry-run) en phase probatoire, soit compteur journalier persistant dans state.json (Ultra) |
| C7 | **C1 = détection + alerte, JAMAIS chmod auto** | `chmod 444` EST une écriture : le superviseur violerait C1 en l'appliquant. C1 = stat + alerte + journalisation + sanction via C5 (unload service fautif) (Ultra) |
| C8 | **RAM < 25 Mo irréaliste en Python** | Python + psutil + requests ≈ 35-50 Mo RSS → stdlib only (urllib, subprocess vm_stat/launchctl) ou cible < 50 Mo (Ultra) |
| C9 | **Test de charge AVANT activation pleine** | 1h de superviseur avec 13 services, mesurer RAM/CPU, /health reste OK (DeepSeek) + métriques de référence AVANT pour comparer APRÈS (DeepSeek) |
| C10 | **Gestion du crash du superviseur** | Qui relance le superviseur s'il meurt ? Wrapper KeepAlive:true ou watchdog (DeepSeek) |
| C11 | **Timeout par provider dans cockpit.py** | max 2s/provider pour ne jamais bloquer le cockpit (DeepSeek) |

---

## CE QUE ADA DOIT FAIRE (ordre des familles)

1. **Faire corriger la spec par Grok** (v2) avec : StartInterval:1800 (ou KeepAlive:true + boucle), Étape 0 = inventaire 27 services + dépendances + RAM par service, backup plists + réversibilité, cockpit.py en cohabitation (pas de remplacement immédiat), C1 sans chmod auto, compteur C6 persistant, stdlib only, timeout provider 2s, test de charge + métriques de référence
2. **Présenter la spec v2 à Christophe pour validation finale** (double signature Ada + Christophe) — non négociable
3. **Ne RIEN exécuter avant la validation explicite de Christophe**

---

*Références : DOSSIER_SPEC_3ETAGES_FAMILLE_2026-08-10.md · AVIS_{gemini,deepseek,juge,ultra}.md · _verification_modeles.txt · REPONSE_GROK_3ETAGES.md*
