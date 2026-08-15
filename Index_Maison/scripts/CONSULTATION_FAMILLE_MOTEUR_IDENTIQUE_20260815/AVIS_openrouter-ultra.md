# AVIS openrouter-ultra (provider OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte, 47.9s)

The user (Buffy, supervisor) wants a factual analysis of the ACE trading system based on provided context: system architecture (SCOUT/HUNTER duo), three runs on 14/08/2026, cycle sequences, key metrics, and CSV evidence.

I need to answer 5 specific questions factually, using the provided data. The core technical question is about the `duo_touch_heartbeat` mechanism potentially neutralizing the TTL (Time To Live) of the `duo_state.json`, causing ALPHA (HUNTER) to stay in `revenge` mode 1.5x continuously.

Let's break down the context:

**System:**
- BETA (SCOUT, x5 leverage): High freq, small trades, detects signals, takes losses.
- ALPHA (HUNTER, x13 leverage): Low freq, large trades, reacts to SCOUT signals via `duo_state.json`.
- `duo_state.json`: Shared state file. Written by `duo_publish_state()`. Read by `duo_hunter_decide()`.
- Key Modes:
  - `revenge`: Triggered if `role=="SCOUT" && status=="CLOSED" && pnl<0 && reason in [list]`. ALPHA enters at 1.5x size (`DUO_HUNTER_REVENGE_MULT=1.5`).
  - `suffer`: Triggered if `status=="OPEN" && bps<=threshold`. ALPHA helps without size change.
- TTL: `DUO_EVENT_TTL_SEC=20`. State stale after 20s.
- Heartbeat: `duo_touch_heartbeat()` (line 1545 genesis) refreshes `ts_ms` in `duo_state.json` at *every SCOUT cycle* without changing other fields.

**Runs:**
- Run 1 (4h): 12:51 - 15:57 (Bull +0.40%)
- Run 2 (V2): 16:24 - 20:24 (Bear -0.27%)
- Run 3 (Night): 21:45 - 05:44 (Bull +0.31%)

**ALPHA Sequences (Cycles):**
- Run 1: Cycles 458, 504, 515, 524. All `hunter_revenge_1.5x` except first `strong_conf_full`.
- Run 2: Cycles 230 (`strong_conf+aspiration`), 341, 408, 409 (`hunter_revenge_1.5x`).
- Run 3: Cycles 859, 861, 869, 872. Mostly `hunter_revenge_1.5x`.

**Key Stats:**
- ALPHA Revenge %: 80%, 68%, 91%.
- ALPHA Revenge PNL %: 91%, 57%, 96%.
- BETA Revenge %: 0% (all `strong_conf_full`).
- Correlation Revenge ALPHA <-> Loss BETA (<=30s): 14%. (<=5min): 59%.
- Flat trades (entry==exit, pnl=0): 25%, 32%, 39% of ALPHA trades.

**CSV Evidence:**
- 4 sealed CSVs (2 per bot).
- File 1 (sealed 14th 21:19Z): 17,333 lines (history up to 20:24Z).
- File 2 (sealed 15th 05:45Z): 20,962 lines.
- First 17,333 lines IDENTICAL byte-for-byte.
- File 2 = File 1 + 3,629 lines (Night run).
- Same `genesis_md5` (8d9ee8d6).
- Same headers.
- `holdSec` column contains detailed message string, `msg` column empty.

**Analysis for Questions:**

**Q1: Confirmation Same Engine?**
Yes. Byte-for-byte identical prefix of CSV logs + same genesis hash + append-only nature proves exact same binary/logic running continuously. No behavior difference suggested by sequences other than market regime reaction (which is expected). The sequences show ALPHA entering `revenge` mode repeatedly across all 3 runs.

**Q2: Revenge Pattern & Heartbeat Hypothesis.**
*Design Intent:* Revenge is punctual. SCOUT loses -> publishes state (CLOSED, pnl<0, reason in list) -> ALPHA reads within 20s (TTL) -> triggers revenge 1.5x -> ALPHA trades -> State becomes stale (20s) -> ALPHA reverts to normal sizing.
*Observed:* 68-91% of ALPHA trades are revenge. Correlation with SCOUT loss <30s is only 14%.
*Heartbeat Mechanism:* `duo_touch_heartbeat()` runs at *every SCOUT cycle* (~200 trades/night = ~1 trade/30s avg, but bursts faster). It updates `ts_ms` in `duo_state.json`.
*Critical Logic:* Does `duo_touch_heartbeat` preserve the *content* (role=SCOUT, status=CLOSED, pnl<0, reason=stop_loss) while updating timestamp?
Context says: "rafraîchit ts_ms du duo_state à CHAQUE cycle du SCOUT sans changer le reste".
If TRUE: The "SCOUT loss event" timestamp is refreshed every ~few seconds by the SCOUT's next cycle. The state *never goes stale* (TTL 20s never expires because heartbeat resets clock every cycle).
*Result:* ALPHA reads `duo_state.json`, sees `ts_ms` < 20s old, sees `role=SCOUT, status=CLOSED, pnl<0, reason=valid`. Condition `duo_hunter_decide` for revenge remains TRUE permanently after the first SCOUT loss that matches criteria.
*Plausibility:* **Extremely High.** This perfectly explains:
1. Persistent revenge mode (68-91%).
2. Low correlation with *recent* SCOUT loss (<30s = 14%) because the triggering loss could have been minutes/hours ago, kept alive by heartbeat.
3. High correlation <5min (59%) because SCOUT trades frequently, so a loss happens often enough to "re-arm" or simply the heartbeat keeps the last loss alive.
4. BETA 0% revenge (BETA is SCOUT, doesn't read duo_state for sizing in same way, or logic prevents self-revenge).

*Alternative:* Maybe `duo_hunter_decide` clears state after reading? But context says ALPHA decides *reading* state. If state persists, decision persists.
*Verdict:* Mechanism is plausible and the prime suspect.

**Q3: BETA "Useless"?**
SCOUT role: "teste le marché en continu... détecte les signaux, subit les pertes."
BETA PNL: +0.40, +1.97, +2.51. Positive but small.
ALPHA PNL: +28, +16, +8. Driven by Revenge (91%, 57%, 96% of PNL).
Functionally: BETA provides the *signal* (the loss event triggering revenge) and liquidity/flow. The PNL asymmetry is *by design* (Hunter vs Scout). However, if Revenge is stuck ON due to heartbeat bug, ALPHA is just trading 1.5x size constantly, not *reacting* to signals. BETA becomes a "heartbeat generator" rather than a signal generator. The "uselessness" is exacerbated by the bug, but the role definition implies low PNL / high info.

**Q4: Flat Trades (25-39% entry==exit).**
`exitReason` in sequences: `fluid_exit_inversion`, `shock_inversion_stop`, `fluid_exit_brake`.
Flat trades (pnl=0, entry=exit) usually mean immediate exit (same tick/bar) or fee-only loss (but pnl=0 here).
Context: "colonne holdSec contient le message détaillé... vrai hold_sec n'est pas tracé".
If hold_sec = 0 (immediate), it's a filter/quality rejection (signal vanished).
If hold_sec > 0 but price didn't move (unlikely on BTC perp), or entry/exit logic bug (limit orders filled same price).
Given `exitReason` names (`inversion`, `brake`), suggests signal invalidated immediately after entry.
"Capital immobilisé pour rien" -> Yes, opportunity cost + fees (if fees not in pnl). 25-39% is high. Suggests noisy signals or over-sensitive entry/exit logic (churn).

**Q5: CSV Anomaly `holdSec` vs `msg`.**
Context explicitly states: "la colonne holdSec contient en réalité le message détaillé... la colonne msg est vide. Le vrai hold_sec n'est pas tracé".
Confirmation: Yes, anomaly. Logging bug: `msg` field gets the structured log string, `holdSec` field gets the message string (or vice versa in code mapping), `holdSec` (duration) not logged.

**Structure of Response:**
1.  **Moteur Unique**: Confirmé (Preuve CSV byte-à-byte + Genesis MD5).
2.  **Pattern Revenge & Heartbeat**: Valider l'hypothèse. C'est l'explication technique #1. Le heartbeat maintient l'état "perte SCOUT" frais indéfiniment. Preuves : Taux revenge 68-91% vs design ponctuel, Corrélation faible <30s (14%) vs forte <5min (59%), Logique du code (heartbeat ne change que ts_ms).
3.  **BETA**: Rôle SCOUT
