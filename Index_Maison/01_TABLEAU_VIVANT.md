# Index Maison — Tableau vivant (garder / enlever / preuve)

**Rôle :** une seule page claire. On ajoute, on raye, on exige une preuve.  
**Règle ACE :** champion Binance testnet **jamais modifié** sans GO humain. Ici = cold path / thermo / pistes.

Dernière MAJ : 2026-11-02 · cockpit LIVE 22h20 · **découvertes 02/11 intégrées**

---

## Comment lire

| Colonne | Sens |
|---------|------|
| **Statut** | `GARDÉ` = dans l’Index · `PISTE` = guillemets, pas codé · `WATCH` = idée soft · `JETÉ` = on n’en parle plus · `REFUS` = explicitement non |
| **Preuve** | Ce qui valide (paper fills, CSV, Brier, judge PASS…) — vide = pas encore |
| **Éval** | Fiche détail dans `Evaluations/` |

Légende statut rapide : 🟢 GARDÉ · 🟡 PISTE · 🔵 WATCH · ⚫ JETÉ · 🔴 REFUS

**Hygiène (au fur et à mesure) :** validation recherche qui touche météo / book / levier / vide → **1 ligne thermo** ici (et miroir `00_INDICATEURS`) + OUTBOX dans la **même** session. Pas de « plus tard ».

---

## 1 — Thermo / indicateurs (A B C)

| ID | Amélioration | Statut | Preuve | Éval / note |
|----|--------------|--------|--------|-------------|
| A1–A6 | Fond : MA, structure, beta, vol 7–30j, DD, range/trend | 🟢 GARDÉ | live 02/11 | `00_INDICATEURS` |
| B7–B12 | Jour/book : BTC 1h/4h/24h, lev signature, largeur panier, vol courte, heat, freins RED | 🟢 GARDÉ | live 02/11 BTC 76892$ | idem |
| C13 | Open interest (OI) | 🟢 GARDÉ branché | live 98888 free | thermo 02/11 |
| C14 | Funding / levier (proxy) | 🟢 GARDÉ branché | funding 0.0001, moy30j 4.6e-05 | thermo 02/11 |
| C15 | Whales ≥ 500k$ proxy free aggTrades | 🟢 GARDÉ proxy | 1 print 661k$ 02/11 | [[THERMO_SOURCES_API]] |
| C23 | **Dark/OTC proxy** — OI + taker B/S | 🟢 GARDÉ proxy | taker 1.029 02/11 | [[THERMO_SOURCES_API]] |
| C16 | Multi-couches → 1 score | 🟢 GARDÉ | score 54/100 warn 02/11 | #01 macro_synergy |
| C17 | Score régime (proxy → HMM plus tard) | 🟡 PISTE | tendance / sans HMM | #07 |
| C18 | **Tension / mur** — wall_drop / profondeur | 🟢 GARDÉ mesuré | mur_mesure.json k=5 σ20j 2.22% seuil 11.14% / 100$ | V8 + grille sandbox 02/11 §72 |
| C19 | **Impulse / froid** — SKIP vs entrée | 🟢 GARDÉ | skips LIVE 935 | V8 Resonance |
| C20 | **Bassine / zone trempe** | 🔵 WATCH | soft ops | pas formule en clair |
| C21 | **SKIP / sagesse** | 🟢 GARDÉ | count SKIP/fills | [[PROTOCOLE_VALIDATION_PATTERN_V8]] |
| C22 | **Verre d'eau / DD session** | 🟢 GARDÉ soft | score 54 proxy | ACE |
| C24 | **Stress levier** funding+OI (type GEX) | 🟢 GARDÉ soft auto | L/S 2.45 + fund | ZeroGEX exemple |
| C25 | **Walls proxy options** | 🔵 WATCH | funding/crowding | pas dashboard payant |
| C26 | **OFI top-of-book CKS normalisé** | 🟢 GARDÉ | ofi_latest 02/11 21h19 NEUTRE 0.0019 brut interdit | test 08/09 + L2 Nov |
| C27 | **Mur mesuré quotidien** | 🟢 GARDÉ | mur_mesure 02/11 15h34 | k_origine grille §72 |
| C28 | **Kelly S2 / m_kelly** — juste taille | 🟢 GARDÉ | m_kelly 02/11 m=8.1 maxS2 4.84 | CHIP sain / BTC-FLUID-RWA aveugles |
| D26–D34 | F&G 37 Fear, MC 2.6T, alt 80% down, liq 2.48M, ETF BTC 62.49M, GEX P/C 0.69, volumes cachés | 🟢 GARDÉ | live free 02/11 | D26–D34 free + proxies |

---

## 2 — TA classique (D)

| ID | Amélioration | Statut | Preuve | Éval |
|----|--------------|--------|--------|------|
| D-keep | Candles, breakouts, reversals, momentum, S&D | 🟢 GARDÉ | — | #04 |
| D-soft | Fib, Heikin, FVG, Renko | 🔵 WATCH | — | #04 |
| D-junk | Gann, harmonics, Elliott | ⚫ JETÉ | — | #04 |

---

## 3 — Mindsets (E)

| ID | Amélioration | Statut | Preuve | Éval |
|----|--------------|--------|--------|------|
| M1 | Liquidité d'abord | 🟢 GARDÉ | — | #08 |
| M2 | Sniper rare + size par width | 🟢 GARDÉ | m_kelly S2 02/11 | #09 |
| M3 | Judge avant worker | 🟢 GARDÉ | verdicteur micro + discipline | #10 |
| M4 | IA adversariale prove-me-wrong | 🔵 WATCH | CONTRA soft | #06 #15 |
| M5 | **Anti-si fixes — mesure > fixe** | 🟢 GARDÉ loi 02/11 | 46 seuils sans mesure listés, 8 non rangés | Doctrine v2 + R17 §73 |
| M6 | Value capture d'abord | 🟢 GARDÉ | — | #25 |
| M7 | **Dureté mesurée, jamais fixe** (02/11) | 🟢 GARDÉ | Kelly + Mur k×σ | mindset maison couturier |
| M8 | **Anti-boucle vide** — OFI/flux/whales dédupliqués, atomiques | 🟢 GARDÉ loi 02/11 | OFI 315 lignes propres (vs 71k), flux 54 uniques | §65 + atomic write |

---

## 4 — Shorts / plancher / ADA (nouveau 02/11)

| ID | Amélioration | Statut | Preuve | Note |
|----|--------------|--------|--------|------|
| SH-BTC/ETH/XRP | Shorts shadow papier 3 paires | 🟢 GARDÉ papier | DIGEST_20261102 plancher OBSERVATION | C1/C2 ok, C3 pas rebond |
| PL | Plancher C1+C2+C3 3 paliers | 🟢 GARDÉ | plancher_live 21h24 | règle 11/09 |
| ADA | Gardienne saison + voilure | 🟡 PISTE | zone-acc 52.8% < 60% discipline 02/11 | à revoir voilure |
| REA | 15 régimes ou event→expo | 🟡 PISTE | §57 ouvert | calendrier sans-date |
| C3 | C3 directionnel quasi-muet | 🟡 PISTE | LONG n=1 SHORT n=0 / mois | seuil 5 BTC à revoir 16/11 |
| FANT | Fantôme short validation live | 🟢 GARDÉ papier | +2.74% puis -0.81% | verdict 16/11, moteur plist 5min 02/11 |

---

## 5 — Process swarm

| ID | Amélioration | Statut | Preuve | Source |
|----|--------------|--------|--------|--------|
| S1 | CSV / fills = juge | 🟢 GARDÉ | Hulk 43.13$ brut → 27.67$ net 02/11 | doctrine |
| S2 | Gates avant size | 🟢 GARDÉ | RED 0 heat 2.7 | B12+M2+M3 |
| S9 | Audit survie PF/MC/OOS/frais | 🟢 GARDÉ | FULL-30 778→742 crash chiffré 02/11 | #12 |
| S10 | Frais réels funding/spread | 🟢 GARDÉ | spread mesuré 201/390, 5bps/côté | #12 |
| S13 | CONTRA soft | 🟡 PISTE | 1 collision | #15 |
| S14 | Valeur info A·B | 🟢 GARDÉ | ★ validé | #17 |
| S22 | Cockpit Arcade Radar | 🟢 GARDÉ LIVE | mission/hub/live 22h20 | [[COCKPIT_LOOK_FIGE]] |
| S22b | Thermo Index live BOARD | 🟢 GARDÉ | live.json 22h20 | board A/B/C |
| S26 | Validation test avant réel | 🟢 GARDÉ | sandbox dégraissage §72-73 | #27 |
| S28 | Kill-switch ROUGE | 🟡 PLAN | testnet d'abord | [[PLAN_DE_VOL]] |

---

## 6 — Journal des décisions

| Date | Action | Item | Pourquoi |
|------|--------|------|----------|
| 2026-11-02 | + | C26 OFI normalisé GARDÉ | L2 Nov, brut interdit, NEUTRE 02/11 |
| 2026-11-02 | + | C27 Mur mesuré k=5 GARDÉ | grille §72 attrape 29/10 20h44 |
| 2026-11-02 | + | C28 Kelly S2 GARDÉ | m=8.1, CHIP/EDEL sains, BTC/FLUID/RWA aveugles TENIR |
| 2026-11-02 | + | M7 dureté mesurée + M8 anti-boucle | Toni 02/11 : fixes éliminés, atomique tmp+fsync |
| 2026-11-02 | ✂ | Fixes journalier/maxDD/plafond trade ÉLIMINÉS | §73 0 tir en 88j aveugles aux bags |
| 2026-11-02 | + | Délestage 1.5Go BACKUP_MINI | vieux L2 Sep/Oct + bak + logs, disque 5.5→7Go |
| 2026-11-02 | + | Fantôme moteur + géopol planifiés | plists 5min/1h créées 02/11 |
| 2026-11-02 | = | HOLD-30 crash chiffré CLOS | FULL-30 -36.54, HULK -25.38, écart +94.76 |
| 2026-11-02 | = | Verdict flux inversé CORRIGÉ CLOS | disait inverse depuis 08/09 |
| 2026-07-30 | ★ | S22 cockpit ZONE TEST → LIVE 02/11 | voir historique complet ci-dessous |

*(Historique 28-30/07 conservé en archive — voir git.)*

---

## 7 — Prochaines preuves

- [ ] Re-mesure OFI 09/11 + revue Mur 09/11 (calendrier)
- [ ] Trancher TROUPEAU 08/11 (3 cas / 20 requis — prolonger ou abandonner)
- [ ] Trancher biais long ETF 16/11 + fantôme 16/11 + C3 16/11
- [ ] Re-mesurer seuil whales 10k BTC 09/11 (fréquence +1h/+24h)
- [ ] Descendre 46 seuils sans mesure → mesure ou rangement (R17)
- [ ] Tester installateur MIGRATION_MINI sur mini 13/11 ($HOME portable)

---

## Fichiers liés

| Fichier | Rôle |
|---------|------|
| `00_INDICATEURS_V1.md` | Liste A–E courte |
| `01_TABLEAU_VIVANT.md` | **Ce fichier** |
| `THERMO_DERNIER.md` | Snapshot live 22h20 |
| `thermo/DISCIPLINE_QUOTIDIENNE.md` | Note fraîche 18h45 |
| `calendrier.json` | Échéances 09/11 16/11 13/11 |
