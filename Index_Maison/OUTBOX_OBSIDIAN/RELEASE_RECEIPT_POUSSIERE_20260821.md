# RELEASE RECEIPT — PÉPITE POUSSIÈRE / BLOCS PRIVATISÉS branchée en ACTIF (21/08/2026)

**Décision :** Christophe (GO direct) — **famille mise de côté** pour ce chantier
(la formule n'est pas à expliquer en un coup, on verra plus tard).
**Contexte :** la pépite fonctionnait depuis le 15/08 mais personne ne branchait sa sortie.
Preuve : 36 blocs analysés, taux fantôme 0,12-62,53 % (médiane 8,39 %), 13 blocs > 10 %.
**Supervision :** Buffy

---

## Problèmes trouvés (le « rien ne bouge » expliqué)

1. **`detecter_bloc_privatise.py`** (LA pépite) : tournait en mode observation silencieux,
   résultat **écrasé à chaque run** (aucun historique), aucune alerte.
2. **`detecter_cpfp.py`** (les 3 cartes) : 2 bugs le rendaient aveugle depuis le 15/08 :
   - Endpoint `/v1/mempool/recent` → **404 Not Found** → carte 3 (poussière) = 0 permanent
   - Pré-filtre « frais > 20× médiane » → **ne passait jamais** en marché calme
     (frais réels 1-8 sat/vB vs seuil 20) → carte 2 ne creusait jamais
   - Résultat : **817 runs / 6 jours / ZÉRO détection** (le script vivait à l'aveugle)
3. **Le pont** lisait déjà `bloc_privatise.json` → la visibilité cockpit existait,
   il manquait juste le mode actif.

## Fichiers modifiés

| Fichier | Action | Rôle |
|---|---|---|
| `Index_Maison/scripts/detecter_bloc_privatise.py` | ✏️ MODIF | Mode ACTIF par défaut (fichier `bloc_privatise_mode.json`) + alerte taux ≥ 10 % + historique append `bloc_privatise_hist.jsonl` + flags `--actif/--observation` |
| `Index_Maison/scripts/detecter_cpfp.py` | ✏️ MODIF | Fix endpoint 404 (`/mempool/recent`) + pré-filtre 20× → 1,5× (creusage enfin possible) |
| `Index_Maison/data/bloc_privatise_hist.jsonl` | ➕ NOUVEAU | Historique des taux (append, pour corrélation prix) |
| `Index_Maison/data/bloc_privatise_mode.json` | ➕ NOUVEAU | Mode actif/observation (réversible) |
| `Index_Maison/data/cpfp_mode.json` | ✏️ MODIF | Mode = actif (déjà prévu par le script) |

## Non modifiés (volontairement)

- `surveiller_whales.py` (scan baleines) — inchangé
- Moteur Hulk / champion ACE — **intouchés**
- `pont_onchain.py` — **aucune modification nécessaire** (il lisait déjà la pépite)

## Preuves (vérifiées en direct le 21/08 17:18)

- Pépite : `bloc_privatise.json` → mode **actif**, taux 0,84 % (bloc courant), 25 snapshots
- Historique : `bloc_privatise_hist.jsonl` → append OK (0,84 %, 56 BTC volume)
- CPFP : `cpfp_detect.json` → mode **actif**, `dust=8` ce run, 21 cumulées 48h
  (avant le fix : dust=0 permanent)
- Chaîne : `live.json.onchain` → `blocPrivatiseMode: actif` + `cpfpMode: actif` + synthèse
  « CPFP actif » → **carte ONCHAIN du cockpit alimentée**

## Réversibilité

- **Pépite en observation :** `python3 Index_Maison/scripts/detecter_bloc_privatise.py --observation`
- **CPFP en observation :** `python3 Index_Maison/scripts/detecter_cpfp.py --once` puis
  éditer `cpfp_mode.json` → `{"mode": "observation"}`
- **Retour complet :** restaurer les 2 scripts depuis le backup git/archives du 21/08

## Alertes (seuils)

- **Pépite :** alerte si taux fantôme ≥ 10 % **ET** volume ≥ 500 BTC (matrice du Juge,
  double condition — corrigé 17:26 après lecture de l'ENQUETE 20/08) + fiable (≥3 snapshots)
- **CPFP :** alerte si carte1 (z≥3σ + plancher 500 BTC) **ET** carte2 (enfant ≥20× médiane)
  simultanément, confirmées 2 runs (mécanisme D5/D6 conservé)

## Setup SNIFFER_VRAI appliqué (17:37 — les 2 améliorations de la méthode)

1. **Poussière NORMALISÉE par le régime de frais** (SNIFFER_VRAI, setup Christophe) :
   seuil = `max(2 sat/vB, minFee × 1.5)` au lieu de l'absolu 2 sat/vB. La poussière
   ne se lit que RELATIVE aux frais du moment (sinon on confond accumulation et
   frais bas). Preuve : minFee 2 → seuil 3.0 sat/vB, 4 vues ce run, 25 cumulées 48h.
2. **SCORE ONCHAIN UNIFIÉ** (comme la voilure ADA) : blocs privatisés ×0.5 +
   poussière ×0.3 + z-score ×0.2 → `indiceOnchain` 0-100 + label + composantes,
   injecté dans `live.json.onchain`. Preuve : indice 6.5/100 (FAIBLE — nominal),
   composantes visibles. C'est l'étalon de la méthode sniffer du vrai : un seul
   chiffre lisible au lieu de 3 observations séparées.

## Corrections suite à lecture de l'historique (17:26)

1. **Alerte pépite** : taux seul → **taux ≥ 10 % ET volume ≥ 500 BTC** (matrice du Juge,
   l'ENQUETE 20/08 le spécifiait noir sur blanc — je l'avais lu et ignoré).
2. **Résolution** : plist vérifiée = déjà 120 s (l'enquête disait 600 s, mais elle avait
   déjà été corrigée) — rien à faire, confirmé par écart moyen 124 s entre runs.
3. **Chaîne 9 MACRO TEMPÊTE ajoutée à sante_index.py** : l'exogène existait déjà
   (detecteur_macro_tempete.py → macro_tempete.json → radar_gate.rb bloque les trades
   contre-choc) mais RIEN ne surveillait sa mort (leçon 8). Désormais : **9/9 chaînes OK**,
   alerte si la plist meurt ou le fichier se fige.

## RÉPARATION BALEINES / COULEUR RÉGIME (17:50 — suite alerte Cortana 16:27Z)

**Déclencheur :** Cortana a crié « Gros print 3 505 221 $ (Binance) » à 16:27Z pendant
que la couleur régime restait ORANGE (« pas assez de signal ») → incohérence totale :
les 2 systèmes baleines ne parlaient pas le même langage.

**Cause racine (prouvée) :** `surveiller_whales.py` était **structurellement aveugle** :
- ne regardait que les **50 premières tx de 6 blocs** (~1,3 % d'un bloc de 4000 tx)
- seuil ≥ **1000 BTC en une seule tx** (~78 M$) → quasi jamais atteint
- résultat : **0 détection depuis le 14/08** (le fichier `whales_mouvements.jsonl`
  n'a même jamais été créé) → `whaleDir` toujours neutral → couleur ORANGE figée.

**Fixes appliqués (GO Christophe) :**
1. `surveiller_whales.py` : scanne désormais les **adresses surveillées directement**
   (4 appels API au lieu de 300+, filtre récence 48 h).
2. `thermo_quotidien_free.py` : stocke la **direction des prints** (champ `m` des
   aggTrades) → `whaleBuyUsd` / `whaleSellUsd` / `whaleDirProxy` (bullish/bearish/neutral).
3. `pont_onchain.py` : **combine scan + proxy** dans `whaleDir` final + expose
   `whaleDirScan` / `whaleDirProxy` / `whaleDirLabel` (inflow→bullish, outflow→bearish).
4. `couleur_regime.py` : normalise inflow/outflow → bullish/bearish pour la matrice.

**Preuve décisive (testé en direct) :** avec le print 3,5 M$ injecté (celui de 16:27Z) :
```
AVANT :  COULEUR RÉGIME : ORANGE  (onchain=neutral)
APRÈS :  COULEUR RÉGIME : VERT    (onchain=bullish + narratif=bullish)
```
La couleur réagit désormais aux baleines que Cortana voit. Valeurs restaurées après test.

**Reste à surveiller :** le scan onchain voit toujours 0 gros bloc ≥1000 BTC sur 48 h
(c'est la réalité du marché — les vrais signaux passent par le proxy ≥500 k$, qui est
maintenant branché). La boucle justesse continue d'accumuler (5 échantillons ORANGE).

## BOUCLE FERMÉE : 4 SOURCES BRANCHÉES (19:50 — couleur regime.py)

**Problème :** la couleur regime.py n'écoutait que 2 sources (onchain + narratif).
Les 2 autres sources du systeme (mission trading + avis IA) ecrivaient des fichiers
mais n'etaient JAMAIS relus pour influencer la couleur → boucle ouverte, data perdue.

**Ce qui a ete branche (GO Christophe) :**

| Source | Fichier lu | Role | Avant | Apres |
|---|---|---|---|---|
| **Thermo** (mission trading) | `cockpit/mission.json` | alert=red → prudence | ❌ ignoré | ✅ `direction_thermo()` : alert=red → bearish, freine VERT→ORANGE |
| **Avis IA** (LLMs analystes) | `thermo/analyses/*.jsonl` | consensus LONG/SHORT | ❌ ignoré | ✅ `direction_avis_ia()` : 4 LONG/2 SHORT → bullish, confirme ou affaiblit |

**Matrice enrichie (maintenant 4 sources) :**
```
thermo bearish + onchain=bullish → VERT affaibli → ORANGE (combo perd → pas confiant)
thermo bearish + onchain=bearish → ROUGE/NOIR confirme (double signal)
avis IA divergent (SHORT vs bullish onchain) → VERT affaibli → ORANGE
```

**Record regime_couleur.json enrichi :**
`avis_ia_dir` · `thermo_dir` · `detail_avis` · `detail_thermo` (traçabilité)

**Preuve (test reel 19:50) :**
```
onchain=neutral (dust=3.7 | blocs_fantomes=17.3%)
narratif=bullish (F&G 72)
avis_ia=bullish (4 LONG / 2 SHORT)
thermo=bearish (alert=red, combo net=-344$)
→ ORANGE (onchain neutre, frein thermo visible)
```
Si onchain devenait bullish, le thermo bearish freinerait : VERT→ORANGE.
Si thermo passait ok, le VERT resterait VERT.

**Tests :** 15 hermetiques OK (6 matrice + 2 scoring + 4 thermo + 3 avis IA).

**Documentation :**
- MEMOIRE_COLLAB.md : ligne 21/08 19:50Z
- `COULEUR_REGIME.md` dans docs/ (a mettre a jour si present)
- Architecture : le schema ci-dessous reflete l'etat actuel.

## Schema d'architecture — flux complet (21/08 19:50)

```
                          ┌─────────────────────┐
                          │   COCKPIT (index.html)│
                          │  regime-swatch, feed, │
                          │  mission, alerts      │
                          └──────────┬────────────┘
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
   ┌──────────▼──────────┐ ┌────────▼────────┐ ┌───────────▼──────────┐
   │  regime_couleur.json │ │  cortana_feed   │ │  alerts_day.json     │
   │  (couleur regime)    │ │  (bullets)      │ │  (12 URGENT today)   │
   └──────────┬──────────┘ └────────┬────────┘ └───────────┬──────────┘
              │                     │                      │
   ┌──────────▼──────────┐  ┌───────▼───────┐  ┌──────────▼──────────┐
   │ couleur_regime.py   │  │cortana_thermo │  │cortana_watch.py     │
   │ 4 sources :         │  │   .py         │  │  fills/baleine/     │
   │  1. onchain (whale) │  │  alertes      │  │  trend/move/dual    │
   │  2. narratif (F&G)  │  │  resume       │  └──────────┬──────────┘
   │  3. avis IA (LLMs)  │  │  voice        │             │
   │  4. thermo (alert)  │  └───────┬───────┘             │
   └──────────┬──────────┘          │                     │
              │                     │                     │
   ┌──────────▼──────────┐  ┌───────▼───────┐  ┌──────────▼──────────┐
   │ thermo/live.json    │  │thermo/analyses│  │ thermo/             │
   │ (score, whaleDir,   │  │  *.jsonl      │  │  cortana_alerts_    │
   │  funding, F&G...)   │  │ (avis IA)     │  │  YYYY-MM-DD.json    │
   └──────────┬──────────┘  └───────▲───────┘  └─────────────────────┘
              │                     │
   ┌──────────▼──────────┐  ┌───────┴───────┐
   │thermo_quotidien_    │  │cortana_       │
   │  free.py            │  │  analyse.py   │
   │ (toutes les sources │  │ (LLM → avis) │
   │  marche, proxy)     │  └───────────────┘
   └──────────┬──────────┘
              │
   ┌──────────▼──────────┐  ┌────────────────┐  ┌────────────────────┐
   │pont_onchain.py      │  │cockpit_mission │  │surveiller_whales.py│
   │(blocs+CPFP+whale    │  │  _feed.py      │  │(adresses, 48h)     │
   │ +proxy → onchain)   │  │(PnL, alerts)   │  └────────────────────┘
   └──────────┬──────────┘  └────────┬───────┘
              │                      │
   ┌──────────▼──────────┐  ┌────────▼───────┐
   │ live.json.onchain   │  │ cockpit/       │
   │ (indiceOnchain,     │  │  mission.json  │
   │  whaleDir, dust...) │  │ (alert=red,    │
   └─────────────────────┘  │  comboPnl...)  │
                            └────────────────┘
```

## Règle veilleuse

Toute nouvelle modif de ces fichiers SANS passer par un chantier = **INTRUSION**.
Toujours mettre à jour la mémoire collab (fait : lignes 21/08 17:18Z, 16:50Z, 19:50Z).
