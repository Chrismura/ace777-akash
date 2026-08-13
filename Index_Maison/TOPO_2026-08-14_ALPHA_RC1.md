# TOPO — 14/08/2026 · Run MASTER_VORTEX_V2_COLLAB_4H · Enquête ALPHA rc=1

> État figé au moment du topo (aucune modification en cours). Point de référence pour la famille et Christophe.

---

## 1. LE RUN (vérifié, données réelles)

| Élément | Valeur |
|---|---|
| Session | 18:12:39 → 20:37:04 UTC (2h24m) — **terminé à SA fin planifiée** (`near_timer`, vs_planned −0.1 min) |
| PNL TOTAL | **+1.3718 USDT** (BETA +0.5452 · ALPHA +0.8266) — statut POSITIF |
| ALPHA (x13, HUNTER) | 5 fills · +0.8266 · win rate 80% · best +0.617 |
| BETA (x5, SCOUT) | 83 fills · +0.5452 · win rate 34.9% |
| Cycles | 1026 (BETA) · 81 (ALPHA) |
| **Ce qui tourne maintenant** | **RIEN** — les deux bots sont morts, le run est fini |

## 2. L'ANOMALIE (ce que Christophe a senti)

**ALPHA est mort en plein run : PROCESS_EXIT rc=1 à 18:25:42Z — 13 min après le début de la session.**
- Dernier événement : fill cycle 81 à 18:25:34 (+0.13168, `shock_inversion_stop`).
- **0 relance après** → ALPHA a raté ~2h de session (BETA a tourné seul).
- Les **212 « E-DUO »** du rapport d'erreurs = désynchronisation scout/hunter causée par ce crash.
- **Récurrent** : ALPHA meurt en `rc=1` à presque chaque session (16:39, 17:11, 17:30, 17:42, 18:08, 18:25). BETA survit systématiquement (rc=0 à 20:37).

## 3. L'ENQUÊTE — pourquoi ALPHA se tue (faits prouvés)

1. **Le bot tourne avec `set -euo pipefail`** (genesis_manifest.txt, ligne 86) → **toute commande qui échoue = mort rc=1 silencieuse** si le stderr est avalé (un `2>/dev/null` dans une substitution).
2. **Mort ~13 min après chaque départ, juste après un fill** — pattern répété, pas un accident.
3. **Le chemin de fermeture de position est ROBUSTE** (vérifié ligne par ligne : `|| true`, `EXIT_ERROR` géré, `continue`) → la mort n'est PAS là.
4. **Les 2 seuls `exit 1` du code sont des checks de DÉMARRAGE** (BASE_URL testnet, erreur levier) → pas eux non plus (Alpha a tourné 13 min avant de mourir).
5. **Aucun message d'erreur dans le log au moment du décès** (fenêtre 18:25:37→18:25:42 vide) → mort avalée.
6. **Le lanceur ne relance pas** : `launch_alpha` appelle `run_unit` une fois, puis `wait $PID_ALPHA` → session à une jambe jusqu'à la fin planifiée.
7. Suspect : la zone entre le log du fill (ligne 2497) et le début du cycle suivant (appels API radar/depth — le « curl tolérant » fait 3 tentatives × 5s pause, soit jusqu'à 15s sans sortie ; un helper `json_get`/`num_*`/`ruby -e` peut échouer sous set -e).

## 4. CE QUI A ÉTÉ FAIT (avant le « touche à rien »)

- **Trap ERR posé dans genesis_manifest.txt** (ligne 89, après `set -euo pipefail`) :
  `trap 'echo "FATAL_RC1 ts=… ligne=$LINENO cmd=[${BASH_COMMAND}]"' ERR` → écrit dans le log du run **et** `/tmp/ace777_fatal_rc1.log`.
  **Testé en réel** : `false` → `FATAL_RC1 ligne=5 cmd=[false]`, rc=1, fichier écrit. **Zéro changement de comportement** — purement diagnostic.
  Backup : `/tmp/genesis_manifest.txt.bak-errtrap-20260814-*`
- **Rappel des corrections déjà en place aujourd'hui** :
  - Double voix : règle « une seule piste » (`killall say` + `killall afplay` + pause 0.05s) appliquée aux **6 chemins voix** (vérifié + testé : rafale → 1 seul afplay).
  - Offres IA : `queue_offres.py` en production (8h15/14h/20h), intégration **active** (`enabled: True`, validation IA auto — décision Christophe 14/08), routeur conservateur comme garde-fou.
  - Cockpit : badge **RUN STATUS** en haut de l'onglet OPS (🟢 EN COURS / 🟡 SIGNAL FAIBLE / 🔴 À L'ARRÊT, poll 5s via /status) — l'`agent_status.js` était figé depuis le 30/07 (affichait RUNNING en permanence).

## 5. CE QUI RESTE À FAIRE (chantiers ouverts)

| # | Action | Statut |
|---|---|---|
| 1 | **Relancer un run** → attraper le `FATAL_RC1 ligne=N cmd=[…]` au prochain crash d'Alpha → corriger la commande fautive à la racine | En attente GO |
| 2 | **Auto-relance Alpha** (lanceur : relancer l'unité morte en session, max 3, avec pause) → plus de session à une jambe | Chantier famille → codeur |
| 3 | Cockpit : RAPPORT_PNL session en cours vs total (distinction demandée par Christophe) | Chantier |
| 4 | Baromètre conso, brief Cortana 4/j, budget cloud, schéma architecture | Tableau des chantiers |

## 6. AUDIT FAMILLE ENVOYÉ

`Index_Maison/scripts/audit_famille_alpha_rc1.py` — 6 membres, chacun : (1) verdict sur le diagnostic, (2) la commande la plus probablement fautive, (3) une amélioration logique/perf/stabilité. Résultats dans `Index_Maison/AUDIT_ALPHA_RC1_2026-08-14/`.
