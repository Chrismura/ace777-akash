# 12 indicateurs (+ extensions) — Index Maison

Validé avec Christophe 2026-07-28. Vulgarisé. ACE = couteau suisse (inspiration multi-débouchés).

## A — Tendance de fond (jours → semaines)

| # | Indicateur |
|---|------------|
| 1 | Prix vs moyenne lente (MA 50/200) |
| 2 | Structure (plus hauts / plus bas) |
| 3 | BTC dominance / beta alts |
| 4 | Volatilité de fond (7–30j) |
| 5 | Drawdown depuis plus haut |
| 6 | Régime large (range vs tendance) |

## B — Journalier / gestion book (minutes → 1 jour)

| # | Indicateur |
|---|------------|
| 7 | BTC 1h / 4h / 24h |
| 8 | Leverage signature (prix↓ + vol↑) |
| 9 | Largeur panier (combien d’alts plongent) |
| 10 | Vol / volume courte |
| 11 | Heat portefeuille (distance aux stops) |
| 12 | Freins veille (RED / pullback) |

## C — Extensions (ajoutées / à brancher)

| # | Indicateur | Rôle |
|---|------------|------|
| 13 | **Open interest (OI)** | Pari ouvert futures — gonfle = levier dans le système |
| 14 | **Levier total** (proxy : OI / market cap ou funding extrême) | Combien le marché est « à crédit » |
| 15 | **Whales ≥ 50 M$** | Gros flux : pas le retail ; signal rare mais lourd |
| 16 | Multi-couches → un score (idée @macro_synergy) | Fusion thermo |
| 17 | Score régime (proxy simple → HMM plus tard) | Météo fond (éval #7 @RuujSs) — pas alpha prix |
| 18 | **Tension / mur** (vide liquidité book) | Déjà dans ACE V8 — lire CSV `tension` / wall_drop |
| 19 | **Impulse / froid** (seuil calme vs choc) | Resonance — SKIP = froid ; entrée = choc |
| 20 | **Bassine / zone trempe** | WATCH — range d’attente avant move (multi-actif) |
| 21 | **Taux SKIP / sagesse** (jour) | PISTE — bruit vs vraie tension |
| 22 | **Verre d’eau / DD session** | Soft — stop global comme thermo survie |
| 23 | **Dark** — proxy free OI/vol (pas abo) | concept · [[THERMO_SOURCES_API]] |
| 24 | **Stress levier** — funding+OI auto | [[THERMO_DERNIER]] · idée type GEX |
| 25 | **Walls / flip** — concept ZeroGEX | proxy soft · pas dashboard payant |

## D — Analyse classique (TA) — noyau retenu

Liste type Rebellio = packaging « 1% » → on trie.

| Garder | Parfois | Jeter (priorité) |
|--------|---------|------------------|
| Candlesticks | Fibonacci | Gann Angles |
| Breakouts | Heikin Ashi | Harmonic Patterns |
| Reversals | FVG | Elliott Wave (sauf curiosité) |
| Momentum | Renko | |
| Supply & Demand | | |

→ Détail : `Evaluations/04_rebellio_12_ta_skills.md`

## E — Mindsets (lunettes, pas signaux)

Pas des indicateurs à « trigger ». Des cadrages qui changent **comment** on lit A/B/C.

| # | Mindset | En une phrase |
|---|---------|---------------|
| M1 | **Liquidité d’abord** (@RaoulGMI) | BTC/Nasdaq trackent surtout l’argent dans le système ; le récit de la semaine est bruit. BTC amplifie (hot/cold vs la ligne) ≠ « cassé ». |
| M2 | **Sniper** (Poly / calibration) | Peu de tirs ; cote vs réalité (Beta+IC) ; size par width — pas le PnL tweet. |
| M3 | **Judge avant worker** | PASS/FAIL machine + rulebook + state disque ; pas « l’agent sent que c’est fini ». |

→ Détail mindsets : `Evaluations/08` `#09` `#10` · **Board complet :** `01_TABLEAU_VIVANT.md`

## Rappel
- A = météo semaine · B = météo jour/book · C = carburant / stress levier / **vide book** · E = lunettes
- Fond haussier ≠ journée safe
- Liquidité macro ok ≠ safe sur un book levier 4h
- **Hygiène :** nouvelle idée thermo → MAJ ce fichier + `01_TABLEAU_VIVANT` **dans la même session** (voir coutume recherche)

Board : `01_TABLEAU_VIVANT.md` · pointeur formule : `FORMULE_BASINE_POINTEUR.md`
