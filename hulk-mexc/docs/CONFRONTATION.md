# Confrontation Hulk paper vs Veille/Qwen

Rempli automatiquement le **2026-07-26** (fin de campagne — process stoppés).

## Période

- Du : **2026-07-22T21:16Z** (paper start `PAPER_V1_20260722_211648`)
- Au : **2026-07-26T16:23Z** (dernier state paper / STOP)
- Heures paper approx : **~91 h** (~3,8 jours)
- Digests / notes « Qwen » : `VEILLE_CALLS.jsonl` **213** batches → **466** hints plats ; notes **~211** blocs `ALERT auto` (presque 0 analyse LLM manuelle)

> **Précision méthodologique :** la piste B est surtout le **digest auto** (`digest_watch`), pas une Qwen LLM qui a annoté à la main. Les notes `VEILLE_QWEN_NOTES.md` = miroir auto des hints. Verdict = **Paper (A) vs Digest/Veille (B)**.

## Scores (simple)

| Critère | Paper (A) | Veille/Qwen (B) | Gagnant |
|---------|-----------|-----------------|--------|
| A vu le gros move **avant** | Entrées RWAINC/RIZE/TEL avant la 1ʳᵉ alerte (paper ~21:17, veille dès ~21:50) | Flag EDEL & KITE **avant** buy paper | **Match** (A plus tôt en début ; B mieux sur EDEL/KITE) |
| A évité un fake spike / mur | **Non** — 5/5 sells = stops avant 2× ; reentries dump ont racheté la chute | Hints `WATCH_PULLBACK` / `IMPULSE_WAIT` répétés sur RWAINC/QAIT/RIZE **avant** les stops | **B** (aurait freiné ; A a pris le stop) |
| PnL / qualité des appels | Réalisé **−8.36 USDT** (5 stops) ; **0** trade gagnant 2× ; **7 bags/positions encore ouvertes** | Ne trade pas — pas de PnL ; signal très répétitif (445× `WATCH_PULLBACK`) | **B** (qualité signal « prudence ») / **A** perd sur exécution |
| Petites caps + volume | A tradé illiquides (QAIT spread élevé, RWAINC, EDEL) | Flag aussi ces caps + QNT/FLUID (watch-only, non tradés) | **B** légèrement (évite chase via `IMPULSE_WAIT`) |

## Preuves

- Paper : `runs/PAPER_V1_20260722_211648.csv` + `_state.json`
- Veille auto : `runs/VEILLE_CALLS.jsonl` + `DIGEST_*.md` / `DIGEST_LATEST.md`
- Notes Qwen : `runs/VEILLE_QWEN_NOTES.md` (auto, pas LLM)

## Exemples à noter

1. **RWAINCUSDT** — Paper BUY `21:17:35Z` (impulse pullback) **avant** 1ʳᵉ veille `21:50:07Z` (`WATCH_PULLBACK`). Stop `−2.62$` le 23@19:59 après 142 alerts pullback. **B avait raison de freiner ; A a payé.**
2. **QAITUSDT** — Paper BUY `08:02:32Z` le 23 ; veille `IMPULSE_WAIT` dès `10:08` (après). Stop `−1.27$` le 24 ; 158 alerts ensuite. Reentry dump immédiat. **A trop agressif post-stop.**
3. **EDELUSDT** — Veille `WATCH_PULLBACK` dès `14:40:44Z` le 24 (**11 alerts avant** buy). Paper BUY `15:27` → stop `−1.45$`. **B anticipait clairement.**
4. **KITEUSDT** — 21 alerts veille dès le 23 ; paper n’achète que le **25@17:50** (encore ouvert). **B beaucoup plus tôt.**
5. **BIO / CC / CHIP** — Paper a acheté **sans aucune** alerte veille sur ces paires (ouverts, MTM non clos). Blind spot B ou filtre digest trop étroit.

## Tableau PnL réalisé (A)

| Paire | Sell | PnL USDT | Reason |
|-------|------|----------|--------|
| RWAINCUSDT | 23 19:59Z | −2.62 | stop −12.85% avant 2× |
| TELUSDT | 24 13:44Z | −1.21 | stop −6% |
| QAITUSDT | 24 14:25Z | −1.27 | stop −6% |
| RIZEUSDT | 25 09:45Z | −1.81 | stop −8.84% |
| EDELUSDT | 25 19:38Z | −1.45 | stop −7.46% |
| **Total réalisé** | | **−8.36** | **0 winner** |

Positions encore ouvertes (state) : CC, CHIP, RWAINC(re), TEL(re), BIO, QAIT(re), KITE — capital immobilisé ~7×~18–20 USDT ; **PnL total campagne ≠ encore final**.

## Verdict

- Mieux en anticipation : **B (Veille/digest)** sur les paires qui ont stoppé + EDEL/KITE ; **A** plus rapide en tout début de session (avant que B n’écrive).
- Mieux en exécution / PnL : **aucun des deux n’a « gagné »** — A a perdu sur les closes ; B n’exécute pas. Si on avait **suivi B = no-trade / wait**, on aurait évité une partie des −8.36$.
- À garder pour la suite :
  - Séparation pistes A/B (bonne)
  - Hints `IMPULSE_WAIT` / `WATCH_PULLBACK` comme **filtre soft** avant buy paper (log, pas hard-kill aveugle)
  - Confrontation datée avec preuves CSV/jsonl
- À jeter / corriger :
  - Relabel « Qwen » → **digest auto** tant qu’il n’y a pas de notes LLM manuelles
  - Répétition 445× du même hint (bruit) — dédup / cooldown / severity
  - Reentry dump immédiat après stop (A) — trop punitif sur cette campagne
  - Ne pas juger A uniquement sur réalisé tant que 7 positions ouvertes

## Décision opérationnelle proposée

1. **Ne pas relancer paper tel quel** sans molette anti-reentry ou filtre veille.
2. Avant prochaine campagne : script scoreur `hint → outcome` (hit/miss à +1h/+6h).
3. Si on branche une vraie Qwen : 1 note/jour structurée (pas 200× ALERT auto).
