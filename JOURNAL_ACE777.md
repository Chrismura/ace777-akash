
## 30/08 22:50 — FIX : ETH sans seed (tableau à 0)
- Diagnostic : ETH (banc de preuve, ajouté 27/08) n'avait JAMAIS eu de SEED_START → colonne bag du début = 0 au cockpit, ligne classée "observe" → son +0,37$ du 28-30/08 (BUY 2449 → SELL 2495, trailing) invisible dans le score.
- Cause : le label "banc_de_preuve" de universe_profils.json n'est pas lu par le moteur (seul PAPER_OBSERVE_PAIRS bloque) → ETH était tradable sans seed. Décision Christophe : ETH TRADABLE + seed 10$ comme les 19 autres.
- Action : seed injecté (état : pos ETH 10$ @ 2497.44 seed:true, cash 19.96→9.96) + ligne SEED_START ajoutée au CSV. Redémarrage moteur via watchdog launchd (--resume, positions tenues). Vérifié : 14 pos + ETH, trades 34.
