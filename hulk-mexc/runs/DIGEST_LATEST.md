# Hulk DIGEST — 2026-09-24T21:39:57Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.36 | 2.66 | 0.39 | 0.03 | 68179122.43 | 1.3 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.69 | 0.59 | 0.0 | 350761448.36 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 45.37 | 26.68 | 0.03 | 197674.89 | 48.49 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.2 | 0.57 | -0.0 | 714797661.08 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.77 | 6.21 | 4.22 | 0.08 | 1339627.1 | 2.94 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 3.91 | 1.46 | 0.04 | 478844.15 | 9.71 | skipped_fast |
| HBARUSDT | IDLE | 1.8 | 3.53 | 0.46 | 0.04 | 806878.83 | 2.13 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 12.34 | 0.49 | 0.17 | 93206.54 | 24.48 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 11.2 | 0.0 | 0.19 | 10451.07 | 9.12 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.5 | 1.23 | 0.05 | 244632.77 | 2.55 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 35.82 | 6.03 | 0.4 | 67076.22 | 404.07 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 2.11 | 2.01 | 0.01 | 210957.6 | 43.75 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 9.35 | 0.25 | 0.24 | 261111.93 | 6.79 | skipped_fast |
| BIOUSDT | IDLE | 1.1 | 3.36 | 1.71 | 0.1 | 87642.59 | 12.89 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.76 | 1.42 | 0.01 | 64992.77 | 9.82 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 2.07 | 1.11 | 0.06 | 100866.3 | 14.28 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 3.1 | 1.38 | -0.05 | 110145.48 | 54.79 | skipped_fast |
| RWAUSDT | IDLE | 0.95 | 1.77 | 0.87 | 0.01 | 57001.66 | 7.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 2.65 | 0.0 | 0.05 | 2057.74 | 22.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.6 | 0.41 | 0.0 | 37808.27 | 44.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
