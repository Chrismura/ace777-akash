# Journal d’erreurs — zone test (avant réel)

**Rôle :** un seul endroit pour bugs / écarts pendant les runs **test**.  
**Protocole :** [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]]  
**Règle :** 1 anomalie = 1 ligne (ou fiche courte). Pas de roman dans le chat.

| Colonne | Sens |
|---------|------|
| id | `E-YYYYMMDD-N` |
| sev | P0 / P1 / P2 / P3 |
| statut | OUVERT · FIXÉ · WONTFIX · SURVEILLÉ |
| où | ACE / Hulk / cockpit / thermo / pont / hygiène |
| quoi | 1 ligne |
| repro | comment revoir |
| suite | fix ou décision |

---

## Ouverts

| id | sev | statut | où | quoi | repro | suite |
|----|-----|--------|-----|------|-------|-------|
| E-20260920-1 | P0 | **FIXÉ** | hygiène / git | **27 instruments que la boucle EXÉCUTE n'étaient dans aucun commit** (chien, page vol, sentinelle, moteurs croisements/paternes, preuve_lecture, verifier_regles_or, installer_depuis_repo…) **sous un drill qui disait READY** | `python3 scripts/drill_restauration.py` → ligne « Instruments de la boucle » doit afficher 0 hors git ; retirer un fichier de git ⇒ doit passer TROU | étape `etape_instruments()` ajoutée au drill (agent launchd + git_push_auto + imports locaux) ; 27 instruments + 5 fichiers de vérité indexés · INCIDENTS 20/09 · LECON-052 |
| E-20260920-2 | P0 | **FIXÉ** | boucle / rotation | **short BTC AVEUGLE ~5 h** (`score: null`) : la rotation vidait `croisement_contexte.jsonl` alors que le signal exige ≥ 10 h d'historique — plist exit 0, produit frais, chien vert | `python3 -c "import json;print(json.load(open('hulk-mexc/runs/short_btc_state.json'))['ok'])"` ; simuler une rotation sur copie | fenêtre gardée 24 h + plafond 60 Mo (réécriture en place) · gardien « vivant mais aveugle » + cri vivant · LECON-053 |
| E-20260920-3 | P0 | **FIXÉ** | coffre / sauvegarde | **Sauvegarde du vault morte 2 jours** (55 fichiers) : `index.lock` orphelin + erreur avalée (`2>/dev/null`) → le script disait « à jour » | poser un `.git/index.lock` orphelin → le script doit sauver quand même et écrire un pouls daté | garde-fou recopié de `git_push_auto.sh` (verrou en `/tmp`) · plus d'erreur avalée · pouls seulement si prouvé à jour · LECON-054 |
| E-20260920-4 | P1 | **FIXÉ** | thermo / heartbeat | RAM annoncée à **0 Mo** en permanence (~50 % réels) : `RAM_FREE=` imprimé, `$ram_free` lu | heartbeat vs `memory_pressure` (tolérance 20 %) | corrigé + garde numérique · preuve en vol `ram_free_mb: 2040` · LECON-055 |
| E-20260920-5 | P1 | **FIXÉ** | registre / cadence | **22 organes calendaires déclarés à 300 s** (défaut inventé) → faux positif garanti le jour où ils reçoivent un produit | `python3 scripts/revue_organes.py` → 0 « cadence déclarée ≠ déclencheur réel » non déclarée | générateur lit le vrai déclencheur (calendrier/KeepAlive/…), 18 cadences corrigées, 0 perte · LECON-056 |
| E-20260920-6 | P1 | **FIXÉ** | chien / résolution | `suivi-setup-red` (produit à **glob**) jamais jugé sur son produit : une panne de celui-ci était invisible | la revue doit le classer OK sur son produit (54 vivants, 0 hors délai) | `resoudre_chemin_produit` gère les jokers (une seule vérité partagée chien/revue) · LECON-057 |
| E-20260920-7 | P1 | **FIXÉ** | chien / organes | `geopol` (figé 17/09) et `croisements-indices` (figé 18/09) **morts cachés** par un marquage « dormant » (le faux positif était éteint, le mort restait) | chien : 99 organes, ces deux-là vivants, 0 grisaille, 0 dormant | réinstallés + chargés, marquage retiré (plutil -lint OK) · INCIDENTS 20/09 |
| E-20260920-8 | P1 | **FIXÉ** | cockpit / page vol | 2 blocs **jamais affichés** (« Chargement… » à vie) + gardien « Chien de garde » en **faux vert permanent** (lit `chien_rapport.txt`, fichier que personne n'écrit) | rendu hors navigateur avec DOM simulé (les deux ordres remplissent) ; page vol : 0 échec | rendu après DOM · export `window.chargerShortBtc` + boot · gardien lit `CHIEN_RAPPORT.json` (> 15 min figé = rouge) |
| E-20260920-9 | P2 | **FIXÉ** | protocole / troupeau-inv | Le plist ne lance que `--cycle` → **`--juger` jamais exécuté** : paire-008 attendait son T+72h du 17/09 (3 j de retard). Critère R6 (≥ 20 cas au 08/11) inatteignable (1 divergence/semaine ⇒ ~8 cas) | `python3 scripts/troupeau_inv.py --status` ; un cycle sans paire due doit juger 0 | cycle juge ce qui est dû (idempotent) · paire-008 = **MISS** · protocole documenté dans `PROTOCOLES_VERDICTS.json` |
| E-20260920-10 | P2 | **SURVEILLÉ** | protocole / arbitrage LLM | **0 alerte microstructure en 7 jours** (`data/micro_alerts.jsonl` = 0 octet depuis le 09/09) → le verdict du **27/09 ne pourra pas être rendu** (0 cas) | `wc -l Index_Maison/data/micro_alerts.jsonl` ; `cortana_micro_score.json` (`n_alertes`) | trancher : module microstructure mort, ou rien à alerter ? (décision C.) |
| E-20260920-11 | P3 | **SURVEILLÉ** | hygiène / chien | **48 organes jugés sur leur seule sortie launchd** (aucun produit déclaré) : leur mort se verrait, leur **silence** non | `python3 scripts/revue_organes.py` → seau « JUGÉ SUR SORTIE » | soit câbler un produit, soit déclarer « produit à la demande » · choix C. |
| E-20260920-12 | P2 | **SURVEILLÉ** | boucle / short-btc | short BTC encore aveugle jusqu'à ~23:12Z (fenêtre de 10 h des données reconstituées) — désormais visible (cri vivant + page vol) | `thermo/cris.json` doit repasser à 0 cri après ~23:30Z | si toujours aveugle après : la lecture du `.1.gz` en complément (option B non retenue le 20/09) |
| E-20260812-1 | P1 | **CLASSE** | Cursor / vie privée | Ban Cursor des lignes ops — clés API : scan Mac au lieu dossiers canon · quota flou · contexte chat sur question simple | Demander clés CMC/MEXC · voir dashboard tokens | [[ERREURS_AI/RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812]] · ops = Terminal humain |
| E-20260730-1 | P2 | SURVEILLÉ | cockpit OPS | PnL α parfois « bizarre » à l’œil vs intuition LIVE (CSV FILLED ≈ -4.35 OK) | Comparer `a-pnl` vs somme `pnl` CSV FILLED | Ne pas juger edge dessus · raffiner feed plus tard |
| E-20260730-2 | P2 | OUVERT | pont Cortana | Bridge `:17777` souvent OFF après coupure / sleep | `curl 127.0.0.1:17777/status` | Lancer `cortana_cockpit_bridge.py` avant lecture |
| E-20260730-3 | P3 | WONTFIX* | thermo free | LIQ 24h / ETF souvent n/d | BOARD pills LIQ/ETF | Free API flaky · pas bloquant (*tant que free) |

---

## Clos / histo

| id | sev | statut | où | quoi | suite |
|----|-----|--------|-----|------|-------|
| E-20260730-0 | P1 | FIXÉ* | ACE run | Coupe WiFi → Beta NET_RETRY rc=6 · ACE ne repart pas seul | *comportement attendu* · hygiène + relance manuelle GO |

---

## Template (copier)

```
| E-YYYYMMDD-N | P? | OUVERT | où | quoi | repro | suite |
```

Fiche longue (si P0/P1) → `Index_Maison/A_Mon_Attention/` ou `ERREURS_AI/` + lien ici.

---

## Compteur go-no-go

| Date | Run / tag | Porte 0 | Porte 1 | Porte 2 | Verdict | Notes |
|------|-----------|---------|---------|---------|---------|-------|
| 2026-07-30 | `NUAGE_SETUP_AVANT` (soir) | — | BOARD OK · pont souvent OFF | run en cours / WiFi déjà vu | INCONCLUSIF outils | Zone test cockpit ouverte |

*Après chaque run test : 1 ligne ici.*
