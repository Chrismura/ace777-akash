# Index Maison — Tableau vivant (garder / enlever / preuve)

**Rôle :** une seule page claire. On ajoute, on raye, on exige une preuve.  
**Règle ACE :** champion Binance testnet **jamais modifié** sans GO humain. Ici = cold path / thermo / pistes.

Dernière MAJ : 2026-07-30 · cockpit ZONE TEST · **S26 validation avant réel**

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
| A1–A6 | Fond : MA, structure, beta, vol 7–30j, DD, range/trend | 🟢 GARDÉ | — | `00_INDICATEURS` |
| B7–B12 | Jour/book : BTC 1h/4h/24h, lev signature, largeur panier, vol courte, heat, freins RED | 🟢 GARDÉ | — | idem |
| C13 | Open interest (OI) | 🟢 GARDÉ | — | à brancher data |
| C14 | Levier total (proxy) | 🟢 GARDÉ | — | |
| C15 | Whales ≥ 50 M$ → **proxy free** gros prints ≥500k$ | 🟢 GARDÉ proxy | aggTrades | [[THERMO_SOURCES_API]] |
| C23 | **Dark/OTC proxy** — OI + taker B/S (pas dark US free) | 🟢 GARDÉ proxy | thermo free | [[THERMO_SOURCES_API]] |
| C16 | Multi-couches → 1 score | 🟢 GARDÉ | — | #01 macro_synergy |
| C17 | Score régime (proxy → HMM plus tard) | 🟡 PISTE | — | #07 RuujSs |
| C18 | **Tension / mur** (vide liquidité book) — wall_drop / profondeur | 🟢 GARDÉ | CSV tension ACE | V8 Tension · [[FORMULE_BASINE_POINTEUR]] |
| C19 | **Impulse / froid** — seuil calme vs choc (SKIP vs entrée) | 🟢 GARDÉ | skips LIVE | V8 Resonance · Syntonie |
| C20 | **Bassine / zone trempe** — range d’attente avant aspiration | 🔵 WATCH | — | thermo multi-actif · pas formule en clair |
| C21 | **Taux de SKIP / sagesse** — bruit vs vraie tension (journée) | 🟡 PISTE | count SKIP/fills | [[PROTOCOLE_VALIDATION_PATTERN_V8]] |
| C22 | **Verre d’eau / DD session** — stop global visible en thermo | 🟢 GARDÉ soft | GlobalStop / STOP | cockpit d’époque · ACE |
| C23 | **Dark pool** — concept ; **proxy free** = OI/vol Binance (pas abo US) | 🔵 WATCH proxy | [[THERMO_DERNIER]] | [[THERMO_SOURCES_API]] · REFUS API payante |
| C24 | **Régime stress levier** — proxy free funding + OI (idée type GEX) | 🟢 GARDÉ soft auto | thermo free | ZeroGEX = *exemple* concept |
| C25 | **Niveaux « walls »** — idée ZeroGEX ; chez nous = lecture soft funding/OI | 🔵 WATCH | — | pas dashboard payant |
| — | « Dump + vol spike » = stress levier | 🟢 GARDÉ | — | #02 SSRN leverage (thermo only) |
| — | Sort equity leverage-correlation | ⚫ JETÉ | — | #02 |

---

## 2 — TA classique (D)

| ID | Amélioration | Statut | Preuve | Éval |
|----|--------------|--------|--------|------|
| D-keep | Candles, breakouts, reversals, momentum, S&D | 🟢 GARDÉ | — | #04 |
| D-soft | Fib, Heikin, FVG, Renko | 🔵 WATCH | — | #04 |
| D-junk | Gann, harmonics, Elliott (sauf curiosité) | ⚫ JETÉ | — | #04 |

---

## 3 — Mindsets (E) — lunettes, pas triggers

| ID | Amélioration | Statut | Preuve | Éval |
|----|--------------|--------|--------|------|
| M1 | Liquidité d’abord (BTC/Nasdaq trackent la marée ; hot/cold ≠ cassé) | 🟢 GARDÉ | — | #08 RaoulGMI |
| M2 | Sniper : rare, cote vs réalité, size par width IC | 🟢 GARDÉ | — | #09 (+ #03) |
| M3 | Judge avant worker : PASS/FAIL machine, rulebook, state disque | 🟢 GARDÉ | — | #10 (+ #05) |
| M4 | IA adversariale (« prove me wrong » / 2ᵉ test) | 🔵 WATCH | — | #06 · voisin #15 CONTRA (toi vs toi) |
| M5 | **Anti-si fixes** (Christophe) | 🟢 GARDÉ | — | Doctrine v2 : scores / régimes / judges évolutifs > if hardcodés ; débloquer le bon en phase 2 |
| M6 | Value capture d’abord (réseau ≠ token ; fees → accrual mesurable) | 🟢 GARDÉ | — | #25 LongViewCrypto / S&P Pantera |

---

## 4 — Pistes couteau suisse (guillemets)

| ID | Amélioration | Statut | Preuve | Éval |
|----|--------------|--------|--------|------|
| P-Poly | Polymarket / prediction BTC courts | 🟡 PISTE | paper fills un jour | #03 |
| P-Sniper | Beta–Binômiale + buckets + fallback + Brier/logloss | 🟡 PISTE | calibration live | #09 |
| P-Graph | Agent = graphe + checkpoints (cold path) | 🟡 PISTE | — | #05 #10 |
| P-HMM | HMM régimes factors (equity lit.) | 🔵 WATCH | — | #07 — proxy simple d’abord |
| — | Copier wallets Poly / PnL $424k Ridark | 🔴 REFUS | — | #09 |
| — | One-sentence → strat live ACE | 🔴 REFUS | — | #06 |
| — | Réécrire champion en LangGraph | 🔴 REFUS | — | #05 #10 |

---

## 5 — Améliorations process swarm (à ne pas oublier)

| ID | Amélioration | Statut | Preuve | Source |
|----|--------------|--------|--------|--------|
| S1 | CSV / fills = juge (pas le récit) | 🟢 GARDÉ | fills ACE/Hulk | doctrine maison |
| S2 | Gates avant size (RED, heat, width sniper) | 🟢 GARDÉ | — | B12 + M2 + M3 |
| S3 | Context filter (ce que l’agent a le droit de savoir) | 🔵 WATCH | — | #06 |
| S4 | Judge.sh pattern : check vide + section / tests | 🟡 PISTE | commande PASS | #10 |
| S5 | 2 reviewers froids + citer la règle | 🔵 WATCH | — | #10 |
| S6 | State / queue sur disque (resume crash Mac) | 🟡 PISTE | — | #05 #10 |
| S6b | Daemon batch : `rebuild_requests` → rebuild 1× → `test_affected` → clear | 🟡 PISTE | — | #10 daemon.sh |
| S7 | Bug BTC crash gate avant BUY Hulk | 🔵 WATCH | — | idée session (pas codé) |
| S8 | Suivi comptes → filtre vs tableau → résumé Cortana | 🟡 PISTE | — | `Suivi_Info/COMPTES.md` |
| S9 | Audit survie : PF 1.2–1.7 · Monte Carlo · OOS · frais/slippage | 🟢 GARDÉ | fills un jour | #12 |
| S10 | Frais réels : Binance funding/VIP · MEXC spread (pas 0%) | 🟢 GARDÉ | — | #12 |
| S11 | Ghost fill : claim API ≠ vérité fill/chain · reconcile + tear-down | 🟢 GARDÉ | — | #14 |
| S12 | Edge net = gross − fees(courbe) − gas ; zone prix = structure | 🟢 GARDÉ | — | #14 suite |
| S13 | CONTRA soft : claim/assumption + Pass 2 manuel (`CONTRA.md`) · pas cron LLM | 🟡 PISTE | 1 collision utile | #15 · [[PROTOCOLE_CONTRA_SOFT]] |
| S14 | Valeur info : **A** économie (temps/RAM) · **B** $ (frais/fills/DD) | 🟢 GARDÉ | ★ validé 29 juil. | #17 · [[VALEUR_INFORMATION]] |
| S15 | Ollama Launch ×9 → **1** agent cold (Hermes/OpenClaw) pour jobs Index/console/plans | 🔵 WATCH | schéma posé | [[ARCHITECTURE_AGORA]] |
| S16 | Archive **ACE Diamant** (EIP-2535 / 79 facettes) — idées modularité ; pas relance dump | 🟢 GARDÉ archive | cahier clair | #18 · [[ACE_DIAMANT_ARCHIVE]] |
| S17 | Mémoire **Syntonie / Permabel** — mythe fondateur + constantes V8 ; pas doctrine médicale | 🟢 GARDÉ mémoire | cahier #19 | [[MEMOIRE_PERSO_SYNTONIE_PERMABEL]] |
| S18 | Pointeur **formule Bassine** (discret) — Bureau + V8 Tension ; pas d’équation dans l’Index | 🟢 GARDÉ pointeur | #20 | [[FORMULE_BASINE_POINTEUR]] |
| S19 | **Ossature Index** anti-éparpillement + flux entre-nourris | 🟢 GARDÉ loi | #21 | [[OSSATURE_INDEX]] |
| S20 | Archive **Escalier synaptique** (fév.) — soft hold / anomaly · pas relance auto | 🟢 GARDÉ histo | #21 | [[HISTO_ESCALIER_SYNAPTIQUE]] |
| S21 | Archive **Trinity-02 Abondance Hybride** (Gemini) — bassine/rotation/verre d’eau | 🟢 GARDÉ histo | #22 | [[HISTO_TRINITY_ABONDANCE_HYBRIDE]] |
| S22 | **Cockpit ACE777** Arcade Radar — **ZONE TEST** sur runs | 🟡 TEST | feed live + hygiène | [[COCKPIT_LOOK_FIGE]] · [[2026-07-30_cockpit_zone_test]] |
| S22b | **Thermo Index live** — board A/B/C + free Binance | 🟢 GARDÉ | live.json | `thermo/index.html` · script free · onglet BOARD |
| S26 | **Validation test avant réel** — UAT / go-no-go / journal erreurs | 🟢 GARDÉ | doctrine | #27 · [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]] · [[JOURNAL_ERREURS_TEST]] |
| S27 | **Session début/fin auto** + **cockpit app native** (pywebview) | 🟡 GO 31 juil. | — | [[PROTOCOLE_SESSION_DEBUT_FIN]] · [[JOURNAL_COCKPIT]] |
| S28 | **Kill-switch ROUGE** cockpit — flatten A/B + confirm (pas d’entrée UI) | 🟡 PLAN | testnet d’abord | [[PLAN_DE_VOL]] · C-05 |
| S23 | **Research Desk** backtest local (Miles-Deutscher) — labo, pas live | 🔵 WATCH | #23 | [[HISTO_RESEARCH_DESK]] |
| S24 | **Local RAG** Obsidian↔Ollama — mémoire notes · après P2 | 🔵 WATCH | #24 | [[HISTO_LOCAL_RAG_OBSIDIAN]] |
| S25 | **Kimi archi** Risk Guardian / WARM / C7–C8 · Cortana résumé horaire | 🟢 GARDÉ spec | #15 | [[Evaluations/15_kimi_archi_risk_warm]] · `tech.html` |
| — | Cron Contrarian Loop 6 h (Claude Sonnet/Haiku) | 🔴 REFUS | — | #15 — Mac 8 Go / ACE |
| — | Underground Trading / Bitunix « free tools » | 🔴 REFUS | — | #12 |
| — | Pair trading / momentum niche retail | 🔵 WATCH | — | #12 |
| — | herdr / multi-agent terminal (@lumendriada) | 🔵 WATCH | — | #13 · chemin [[PHASE_EQUIPE_AGENTS]] marche 3 |
| — | Meridian Company OS (@Av1dlive / Kimi) | 🔵 WATCH | — | #16 · approvals+audit · pas ACE |
| — | Préférence API agents = **Kimi** (qualité/prix) | 🟢 GARDÉ soft | — | [[PREFS_STACK]] · #16 |

---

## 6 — Journal des décisions (ajouter / enlever ici)

| Date | Action | Item | Pourquoi |
|------|--------|------|----------|
| 2026-07-28 | + | A–C base + whales/OI | Session Index v1 |
| 2026-07-28 | + | D tri Rebellio | #04 |
| 2026-07-28 | + | C16 multi-couches | #01 |
| 2026-07-28 | + | C17 régime | #07 |
| 2026-07-28 | + | M1 liquidité | #08 |
| 2026-07-28 | + | M2 sniper + P-Poly/P-Sniper | #03 #09 |
| 2026-07-28 | + | M3 judge / graphe | #05 #10 |
| 2026-07-28 | + | M5 anti-si fixes | Doctrine Christophe : v1 = inventaire ; v2 = débloquer (scores soft, pas if figés) |
| 2026-07-29 | + | S9 audit survie + S10 frais | #12 texte Christophe (WF/MC/PF/kill) |
| 2026-07-29 | + | S11 ghost fill reconcile | #14 Punisher — matched≠settled |
| 2026-07-29 | + | S12 fee curve / edge net | #14 suite — 0.99 zone · pas drift book |
| 2026-07-29 | ✕ | Underground Trading Bitunix | #12 REFUS abo/referral ; page = boutique |
| 2026-07-29 | + | S13 CONTRA soft | #15 N01ennn — claim/assumption + Pass 2 manuel ; REFUS cron 6 h |
| 2026-07-29 | ✕ | Contrarian Loop auto Claude | #15 — RAM/coût ; human-in-loop déjà coutume |
| 2026-07-29 | + | Suivi @Av1dlive + pref Kimi API | #16 Meridian OS WATCH · auto-add comptes validés |
| 2026-07-29 | + | S14 valeur info A·B | #17 — ★ validé Christophe (filtre recherche) |
| 2026-07-29 | + | S15 Ollama Launch cold + schéma archi | [[ARCHITECTURE_AGORA]] — 1 agent froid max |
| 2026-07-29 | + | S16 ACE Diamant archive | #18 — R&D fév. clarifiée · WATCH idées / REFUS dump |
| 2026-07-29 | + | S17 Syntonie/Permabel · S18 pointeur Bassine | #19 #20 |
| 2026-07-29 | + | **C18–C22 thermo** (tension, impulse, bassine, SKIP, verre d’eau) | Hygiène Vide/V8 → thermomètre |
| 2026-07-29 | + | **C23–C25** dark pool + GEX / ZeroGEX walls | [[THERMO_SOURCES_API]] — APIs listées · pas d’abo auto |
| 2026-07-29 | + | **S19 ossature** + **S20 escalier** histo | #21 — anti-éparpillement · commande fév. archivée |
| 2026-07-30 | + | **S22b Thermo Index live** | Board A–C HTML + live.json Binance free · validé liste |
| 2026-07-30 | ★ | **S22 cockpit → ZONE TEST** | Prototype OPS/THERMO/BOARD/VOL + Cortana · hygiène indicateurs · runs test |
| 2026-07-30 | + | **S26 validation test avant réel** | UAT léger · journal erreurs · go-no-go avant argent réel |
| 2026-07-30 | ★ | **S27 demain** | App native pywebview + protocole session début/fin auto |
| | | | |

*(Quand tu ajoutes ou rayes : 1 ligne ici + MAJ statut dans le tableau du dessus.)*

---

## 7 — Prochaines preuves à coller (checklist)

- [ ] **Phase 2 :** revoir le 🟢 GARDÉ et « débloquer » — scores / régimes / width / rulebook vivant > indicateurs figés + `si X alors Y` durs
- [ ] Définir 1 proxy simple pour C17 (sans HMM)
- [ ] Brancher data OI / funding (C13–C14) en lecture seule
- [ ] **C23–C25 :** essai FlashAlpha free 1×/jour SPY levels → note CONSOLE (preuve)
- [ ] **C21 :** Voie A — run A (pack strict) vs B (témoin) · grille [[PROTOCOLE_VALIDATION_PATTERN_V8]]
- [ ] **C20 :** 1 définition opérationnelle « zone trempe » (sans formule secrète)
- [ ] Si Poly paper un jour : Brier + log loss + `width` gate
- [ ] Punk/Index : 1 `judge` minimal (fichier note non vide + sections)
- [ ] Hulk : décider oui/non crash-gate BTC (S7)

---

## Fichiers liés

| Fichier | Rôle |
|---------|------|
| `00_INDICATEURS_V1.md` | Liste A–E courte |
| `01_TABLEAU_VIVANT.md` | **Ce fichier** — board add/remove/preuve |
| `Evaluations/01`…`15` | Détail par post / note |
| `PROTOCOLE_CONTRA_SOFT.md` | Chat cold-path → prototype (évolutif) |
| `CONTRA.md` | Journal collisions Pass 2 |
| `VALEUR_INFORMATION.md` | Grille A (économie) · B ($) — S14 |
| `THERMO_SOURCES_API.md` | Dark pool + GEX/ZeroGEX — liens API à brancher |

**Opinion :** oui, c’est le bon format — sinon on rediscute chaque tweet. Une ligne = une décision traçable.
