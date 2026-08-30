# 🏗️ SCHÉMA D'ARCHITECTURE — ACE777 (21/08/2026, 19:50Z)

> **Pour qui vient après** : ce document montre comment les données circulent dans le système.
> Chaque flèche = un script qui lit un fichier et en écrit un autre.
> Si un maillon meurt, la chaîne下游 ne reçoit plus rien.

---

## 🔴 LE CŒUR : COULEUR RÉGIME (4 sources → 1 décision)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     COULEUR RÉGIME (couleur_regime.py)                  │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐ │
│  │  1. ONCHAIN  │  │ 2. NARRATIF  │  │  3. AVIS IA  │  │ 4. THERMO   │ │
│  │  whaleDir    │  │  Fear&Greed  │  │  LLMs (4/2)  │  │ alert=red   │ │
│  │  (bullish/   │  │  (bullish/   │  │  (bullish/   │  │ combo net   │ │
│  │   bearish/   │  │   bearish)   │  │   bearish/   │  │ (bearish/   │ │
│  │   neutral)   │  │              │  │   neutral)   │  │  neutral)   │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬──────┘ │
│         │                 │                 │                  │        │
│         └────────┬────────┴────────┬────────┘                  │        │
│                  │   MATRICE       │                           │        │
│         onchain × narratif = couleur de base                   │        │
│                  │                                         │        │
│                  ├── thermos bearish + VERT → ORANGE (frein)  │        │
│                  ├── avis divergent + VERT → ORANGE           │        │
│                  └── résultat final ─────────────────────────►│        │
│                                                               │        │
│  ┌────────────────────────────────────────────────────────────┘        │
│  │  VERT   = tout confirme → favorable à l'entrée                     │
│  │  JAUNE  = contrarian → accumulation discrète                       │
│  │  ROUGE  = piège → NE PAS ENTRER                                   │
│  │  NOIR   = aligné baissier → rester dehors                         │
│  │  ORANGE = pas assez de signal → attendre                           │
│  └─────────────────────────────────────────────────────────────────────┘
│                                                                         │
│  📝 Boucle auto-nourrie : couleur → attente 24h → HIT/MISS → leçons   │
│  📝 Mode OBSERVATION par défaut (pas de trading, famille → juge → GO)  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 FLUX COMPLET DES DONNÉES

### Couches haute (décision)

```
                          ┌─────────────────────────┐
                          │   COCKPIT (index.html)   │
                          │  regime-swatch, feed,     │
                          │  mission, alerts, justesse│
                          └────────────┬────────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
   ┌──────────▼──────────┐  ┌──────────▼──────────┐  ┌─────────▼──────────┐
   │ regime_couleur.json │  │  cortana_feed.json   │  │  alerts_day.json   │
   │ (couleur du moment) │  │  (bullets, sentiment)│  │  (12 URGENT today) │
   │ + regime_justesse   │  │  + regime_justesse   │  │                    │
   │   .json             │  │                      │  │                    │
   └──────────┬──────────┘  └──────────┬──────────┘  └─────────┬──────────┘
              │                        │                        │
   ┌──────────▼──────────┐  ┌──────────▼──────────┐  ┌─────────▼──────────┐
   │ couleur_regime.py   │  │ cortana_thermo.py    │  │ cortana_watch.py   │
   │ 4 sources:          │  │  alertes, resume,    │  │  fills, baleine,   │
   │  onchain, narratif, │  │  voice, feed         │  │  trend, move, dual │
   │  avis IA, thermo    │  └──────────┬──────────┘  └─────────┬──────────┘
   └──────────┬──────────┘             │                        │
              │                        │                        │
```

### Couches moyenne (collecte)

```
   ┌──────────────────────────────────────────────────────────────────────┐
   │                          THERMO (live.json)                          │
   │  score, climate, funding, F&G, whales, OI, L/S, liq, ETF, GEX...    │
   └───────────────┬──────────────────────────────────┬───────────────────┘
                   │                                  │
   ┌───────────────▼──────────┐  ┌────────────────────▼─────────────────┐
   │  thermo_quotidien_free   │  │  pont_onchain.py                     │
   │  .py                     │  │  (blocs+CPFP+whale+proxy → onchain)  │
   │  (toutes les sources     │  └───────────────┬──────────────────────┘
   │   marché, proxy Binance) │                  │
   └───────────────┬──────────┘  ┌───────────────▼──────────────────────┐
                   │             │  live.json.onchain                    │
   ┌───────────────▼──────────┐  │  (indiceOnchain, whaleDir, dust,     │
   │  cockpit_mission_feed.py │  │   blocs privatisés, score unifié)    │
   │  (PnL, alerts, combo)    │  └──────────────────────────────────────┘
   └───────────────┬──────────┘
                   │
   ┌───────────────▼──────────┐  ┌──────────────────────────────────────┐
   │  cockpit/mission.json    │  │  thermo/analyses/*.jsonl             │
   │  (alert=red, comboPnl,   │  │  (avis LONG/SHORT des LLMs,         │
   │   comboPnlNet, session)  │  │   horizon, confiance)                │
   └──────────────────────────┘  └──────────────────────────────────────┘
```

### Couches basse (capteurs)

```
   ┌──────────────────────────────────────────────────────────────────────┐
   │                        SOURCES DE DONNÉES                            │
   │                                                                      │
   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌───────────────┐ │
   │  │ Binance API │ │ Mempool     │ │ CoinGecko   │ │ Deribit       │ │
   │  │ (funding,   │ │ (CPFP,      │ │ (F&G, MC)   │ │ (GEX, options)│ │
   │  │  aggTrades, │ │  blocs,     │ │             │ │               │ │
   │  │  ticker)    │ │  poussière) │ │             │ │               │ │
   │  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └───────┬───────┘ │
   │         │               │               │                 │         │
   │  ┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐ ┌───────▼───────┐ │
   │  │surveiller_  │ │detecter_    │ │sniffer_vrai │ │ fees_platforme│ │
   │  │whales.py    │ │cpfp.py      │ │.py          │ │ .py           │ │
   │  │(4 adresses, │ │(3 cartes:   │ │(brut_onchain│ │               │ │
   │  │ 48h, proxy) │ │ z, dust,    │ │ + F&G)      │ │               │ │
   │  └─────────────┘ │ minFee)     │ └─────────────┘ └───────────────┘ │
   │                   └─────────────┘                                   │
   │  ┌─────────────────────────────┐ ┌────────────────────────────────┐ │
   │  │detecter_bloc_privatise.py   │ │detecteur_macro_tempete.py      │ │
   │  │(taux fantôme, pépite)       │ │(exogène, anti-choc)            │ │
   │  └─────────────────────────────┘ └────────────────────────────────┘ │
   └──────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 LES BOUCLES DE FEEDBACK

### Boucle 1 : Couleur régime → observation → score → leçons
```
couleur_regime.py --run  →  regime_couleur.json  →  cockpit affiche
         │                                              │
         ▼                                              ▼
regime_couleur.jsonl  ←  (historique)           attente 24h
         │                                              │
         ▼                                              ▼
couleur_regime.py --score  →  regime_justesse.json (HIT/MISS)
         │
         ▼
couleur_regime.py --lecons  →  verdict par couleur
  (FIABLE si ≥75% / PEU FIABLE si ≤50% → ramollir le signal)
```

### Boucle 2 : Cortana → alertes → feed → cockpit
```
cortana_watch.py (10s)  →  .urgent_alert.json  →  cortana_thermo.py poll
                                                          │
                                                          ▼
                                              cortana_feed.json  →  cockpit
                                              cortana_alerts_*.json (historique)
```

### Boucle 3 : Thermo → live.json → tout le monde
```
thermo_quotidien_free.py  →  thermo/live.json  →  couleur_regime.py
                                          │        cortana_thermo.py
                                          │        pont_onchain.py
                                          │        cockpit_mission_feed.py
                                          │        sante_index.py
                                          ▼
                                  cockpit/mission.json  →  couleur_regime.py
```

---

## 📋 TABLEAU RAPIDE — QUI LIT QUOI

| Fichier produit | Script qui écrit | Scripts qui lisent |
|---|---|---|
| `thermo/live.json` | `thermo_quotidien_free.py` | `couleur_regime`, `cortana_thermo`, `pont_onchain`, `sniffer_vrai`, `sante_index`, `cockpit_mission_feed` |
| `thermo/live.json.onchain` | `pont_onchain.py` | `sante_index`, `couleur_regime` (via `brut_onchain`) |
| `cockpit/mission.json` | `cockpit_mission_feed.py` | `cortana_thermo`, `couleur_regime` 🆕, `sante_index`, `cortana_cockpit_bridge` |
| `thermo/regime_couleur.json` | `couleur_regime.py` | `cortana_cockpit_bridge`, `veilleuse_chantiers` |
| `thermo/regime_justesse.json` | `couleur_regime.py` | `cortana_cockpit_bridge`, `veilleuse_chantiers` |
| `thermo/cortana_feed.json` | `cortana_thermo.py` | `sante_index`, `mon_cockpit`, `system_state_generator` |
| `thermo/analyses/*.jsonl` | `cortana_analyse.py` | `cortana_thermo` (derniers_avis_ia), `couleur_regime` 🆕 |
| `thermo/cortana_alerts_*.json` | `cortana_thermo.py` | `cortana_thermo` (historique), cockpit |
| `cockpit/alerts_day.json` | `cortana_thermo.py` | cockpit |
| `thermo/sante_index.json` | `sante_index.py` | `auto_reparer`, `veille_degradation` |

---

## ⚙️ AUTO-RÉPARATION (2 niveaux)

| Niveau | Mécanisme | Cadence | Preuve |
|---|---|---|---|
| **1. Processus vitaux** | `superviseur.sh` + `watchdog_superviseur.sh` | chaque minute | Relances prouvées 21/08 (vigie 11:24, cockpit 13:06) |
| **2. Plists de veille** | `auto_reparer.py` dans `sante_index` | 5 min | Actif depuis 21/08 19:09 (GO Christophe) |

---

## 🔐 GARDE-FOUS

| Garde-fou | Fichier | Rôle |
|---|---|---|
| **Md5 veilleuse** | `REGISTRE_SYNAPSES.json` | Alerte si un script surveillé est modifié non déclaré |
| **Backoff** | `auto_reparer.py` | Max 3 essais/24h, cooldown 10 min |
| **Circuit-breaker** | `auto_reparer.py` | Pas de relance si load>6 ou swap>2Go |
| **Mode observation** | `couleur_regime.py` | Pas de trading tant que famille→juge→backtest→GO |

---

# 🧭 CARTE DES 56 AGENTS + LEURS BOUCLES (MAJ 23/08/2026 23h60Z)

> Ajout Buffy 23/08 23:55Z · scan réel `~/Library/LaunchAgents/com.ace777.*.plist` (56 plists) + `launchctl list` (57 chargées, dont dialogue-gemini créé ce soir).
> **Légende boucle** : `🔁 [N s]` = launchd relance toutes les N s · `☀️ HH:MM` = 1 fois/jour à cette heure · `🔴 alive` = démon permanent (KeepAlive, boucle interne) · `🔄 = se suffit à lui-même`.

---

## FAMILLE A — CŒUR : démons permanents (la base, ne jamais éteindre)

| Agent (plist) | Cerveau/script | Boucle | Rôle |
|---|---|---|---|
| `prise-ia` | `hub_prise_ia.py` | 🔴 alive (KeepAlive) | **LE HUB IA** : route toutes les requêtes des IA (gemini, groq, nara, huggingface…), budgets, quota, filets, bascules |
| `vigie-live` | `vigie_live.py` | 🔴 alive | Surveille le marché en direct (10 s), alarme si secousse ≥1 %, écrit `alarme.json` |
| `cockpit-http` | `cockpit_http_server.py` | 🔴 alive | Serveur HTTP du cockpit (l'interface graphique) |
| `cockpit-pont` | `cortana_cockpit_bridge.py` | 🔴 alive | Pont cockpit ↔ système : pousse les données vers l'interface |
| `llm-gate-hub` | `llm_gate_hub_bridge.py` | 🔴 alive | Grille LLM → hub (un seul point d'entrée pour les IA) |
| `superviseur-process` | `superviseur.sh` | 🔴 alive + ⏲ 1 min | Niveau 1 : relance les process vitaux morts (preuves 21/08) |
| `superviseur-core` | `superviseur_core.sh` | 🔴 alive + ⏲ 15 min | Niveau 1 bis : relance les plists de base (cœur) |

## FAMILLE B — CAPTEURS MARCHÉ (mempool + binance + indice)

| Agent | Script | Boucle | Rôle |
|---|---|---|---|
| `bloc-privatise` | `detecter_bloc_privatise.py` | 🌀 [120 s] | **LA PÉPITE** : tx jamais vues dans la mempool publique = OTC baleine → taux fantôme + volume (fix 23/08 : repli blockstream + SIGALRM + fiable) |
| `cpfp` | `detecter_cpfp.py` | 🌀 [600 s] | La poussière : CPFP/dust → 3 cartes (z, dust, minFee) → indice |
| `whales` | `surveiller_whales.py` | 🌀 [300 s] | Adresses baleines (4) : print achat/vente → whaleDir |
| `pont-onchain` | `pont_onchain.py` | 🌀 [300 s] | Ponte onchain : combine blocs+dust+whale+proxy → live.json.onchain (indiceOnchain, whaleDir, dust, score) |
| `fees` | `fees_platforme.py` | 🌀 [300 s] | Frais plateformes (Binance…) → live.json |
| `macro-tempete` | `detecteur_macro_tempete.py` | 🌀 [60 s] | Choc exogène (macro/Fed/Trésor) : bloque trades anti-choc → macro_tempete.json |
| `hulk-watchdog` | `watchdog_hulk_ghost.sh` | 🌀 [120 s] | Gardien du bot Hulk (MEXC) |
| `cortana.urgent` | `cortana_urgent_poll.sh` | 🌀 [10 s] | Poll des alertes urgentes (cortana_watch) → vocal/feed |
| `hub-cockpit-feed` | `hub_cockpit_feed.py` | 🌀 [30 s] | Pousse les événements hub → cockpit (feed) |

## FAMILLE C — MÉTA-ÉTAT : santé + dégradation + réparation

| Agent | Script | Boucle | Rôle |
|---|---|---|---|
| `sante-index` | `sante_index.py` | 🌀 [300 s] | **LA SANTÉ GLOBALE** : 9/9 chaînes (capteurs, veille, hub…) → sante_index.json + ALERTE |
| `veille-degradation` | `veille_degradation.py` | 🌀 [60 s] | **MÉTA-ANALYSE** : plists 14/14 + heartbeats frais + indicateurs + pattern boucle → SAIN / ALERTE (fix 23/08 : ignore le « non fiable » ) |
| `dms-veille` | `dms_veille.py` | 🌀 [60 s] | **DEAD MAN'S SWITCH** : qui surveille la surveillante ? Vérifie la fraîcheur de veille-degradation + launchctl → DMS_VEILLE.json |
| `watchdog` | `watchdog_superviseur.sh` | 🌀 [120 s] | Gardien du superviseur lui-même |
| `heartbeats` | `heartbeats.py` | 🌀 [60 s] | Écrit les heartbeats (vie) des services |
| `rappels` | `rappels.py` | 🌀 [60 s] | Rappels vocaux/notifs programmés |
| `veilleuse` | `veilleuse_synapses.py` | 🌀 [600 s] | Intégrité md5 des scripts surveillés + kill-switches → REGISTRE_SYNAPSES |
| `autopilote` | `autopilote.sh` | 🌀 [900 s] | Démarreur ACE777 (relance les services manquants, CONTRAT_AUTOGESTION) |
| `backup-check` | `backup_light_check.sh` | 🌀 [1800 s] | Vérifie les backups / points de restauration |
| `state-generator` | `system_state_generator.py` | 🌀 [120 s] | Génère l'état système global (pastilles cockpit) |

## FAMILLE D — ANALYSES IA + PROFESSEUR (justesse)

| Agent | Script | Boucle | Rôle |
|---|---|---|---|
| `sniffer-matin` | `sniffer_vrai.py` | ☀ 08:00 | Sniff matinal (brut onchain + F&G) → brief |
| `sniffer-ny` | `sniffer_vrai.py` | ☀ 15:50 | Sniff de l'après-midi (NY) |
| `couleur-regime` | `couleur_regime.py` | ☀ 08:05 + 15:55 (run) | **CŒUR DÉCISIONNEL** : 4 sources (onchain × narratif × IA × thermo) → couleur VERT/JAUNE/ROUGE/NOIR/ORANGE → regime_couleur.json |
| `couleur-regime-score` | `couleur_regime.py` | ☀ 16:30 (score) | Score HIT/MISS de la couleur → regime_justesse.json |
| `analyste-cadence` | `analyste_cadence.sh` | ☀ 08:30 + 20:30 | Production des analyses Cortana (le professeur) |
| `discipline-quotidienne` | `discipline_quotidienne.py` | ☀ 07:15 | Le professeur : re-note + alerte boucle affamée |
| `scoreur-registre` | `scoreur_registre_mecanique.py` | ☀ 07:30 | Scoreur du registre mécanique → JUSTESSE_REGISTRE.json |
| `eval-offres` | `eval_offres.py` | ☀ 07:05 | Éval comparative auto des IA gratuites |
| `roulement-ia` | `roulement_ia.py` | ☀ 07:08 | Roulement auto des IA (pas de provider mort) |
| `queueoffres` | `queue_offres.py` | ☀ 07:02/08:15/14:00/20:00 | File d'attente des offres IA gratuites |
| `catalogue` | `catalog_providers.py` | ☀ 10:00 | Génère CATALOGUE_PROVIDERS.md (vue des providers) |
| `observatoire` | `observatoire.py` | ☀ 11:00 | Observation 48 h + rollback auto + validation hebdo des IA |
| `veille-hub` | `veille_hub.py` | ☀ 07:00 | Checkup quotidien du hub (providers, budgets) |
| `routeur-auto` | `routeur_auto.py` | 🌀 [6 h] | Routeur intelligent: choisit le meilleur LLM (score) |

## FAMILLE E — OFFRE / VEILLE / CONTENU

| Agent | Script | Boucle | Rôle |
|---|---|---|---|
| `veille-yt` | `watch_chaines.py` | ☀ 09:15 + 18:15 | Veille YouTube (chaines) |
| `veilleuse-chantiers` | `veilleuse_chantiers.py` | ☀ 09:00 | Veille chantiers/alertes projet |
| `veilleuse-confrontation` | `veilleuse_confrontation_ace_hulk.sh` | 🌀 [6 h] | Confrontation ACE vs Hulk (performances) |
| `veilleuse-sizing-monte-carlo` | `veilleuse_sizing_monte_carlo.sh` | 🌀 [6 h] | Sizing Monte-Carlo (risques) |
| `graph-cerveau` | `rebuild_graph.sh` | ☀ 11:30 | Reconstruit le graphe du cerveau (Obsidian) |
| `archi-vivante` | `archi_vivante.py` | ☀ 07:00 | Réactualise l'architecture vivante |
| `journal-soir` | `journal_soir_launchd.sh` | ☀ 20:53 | Journal du soir (snapshot auto) |
| `verif-setup` | `verifier_setup.py` | ☀ 12:00 | Check du setup complet (les 4 fiches) |

## FAMILLE F — VORTEX (le moteur de trading testnet)

| plist | Script | Boucle | Rôle |
|---|---|---|---|
| `run-setupA-4h` | `GO_VORTEX_V2.sh --duration 04:00:00` | 🔴 alive (KeepAlive=true) | **Run 4h** : moteur Vortex v2 (testnet Binance) — ALPHA/BETA, duo SCOUT/HUNTER |
| `run-vortex-96h` | `GO_VORTEX_V2.sh 96:00:00` | 🔴 alive (KeepAlive + auto-relance) | **Run 96h** : moteur long (champion certific) |
| `run72h` | `GO_VORTEX_V2.sh 72:00:00` | 🔴 alive (auto-relance) | **Run 72h** : moteur (vieux leçon 6 : verrou md5 anti-patch) |

## FAMILLE G — SYNCHRO / DIVERS

| Agent | Script | Boucle | Rôle |
|---|---|---|---|
| `gitpush-vault` | `git_push_vault.sh` | 🌀 [3 h] | Commit/push du vault Obsidian (GitHub) |
| `gitpush` | `git_push_auto.sh` | 🌀 [3 h] | Push du workspace |
| `dialogue-gemini` (NEW 23/08) | `dialogue_gemini_direct.py` | 🔁 1x au boot (état sur disque) | **Dialogue protocole incassable avec Gemini** : attend le quota 429, enchaîne 3 tours avec historique |

---

## 🔄 LES BOUCLES EN RÉSUMÉ (flux entrant/grandes cadences)

```
[10s]  cortana.urgent ────────────► .urgent_alert.json
[30s]  hub-cockpit-feed ──────────► cockpit feed
[60s]  veille-degradation / DMS / heartbeats / rappels / macro-tempete ──► etat + alertes
[120s] bloc-privatise (pépite) ────► data/bloc_privatise.json · rate 2 min
[300s] whales / pont-onchain / fees / sante-index ──► live.json.onchain + sante_index.json
[600s] cpfp ──────────────────────► indice poussière
[900s] autopilote ────────────────► relance services
[15min] superviseur-core ─────────► relance proc cœur
[6h]   routeur-auto / veilleuse-confrontation / monte-carlo ──► routing.json / confrontations
[1x/h] cortana-feed ──────────────► cortana_feed.json
[quot] 08:05/08:30/15:50/16:30 ───► couleur régime + score (la décision du jour)
```

**⚠️ Le point sensible REBOOT** (détail ci-dessous) : les 3 plists vortex (A/F) se relancent TOUTES au boot et repèrent de zéro (le lanceur purge duo_state) — attendre 2-3 cycles pour la stabilisation.
