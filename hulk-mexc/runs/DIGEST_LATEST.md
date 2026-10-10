# Hulk DIGEST — 2026-10-10T19:56:56Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.72 | 8.42 | 7.12 | 0.03 | 1261751.66 | 6.25 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.88 | 0.16 | 0.02 | 97494317.18 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.7 | 0.45 | 0.02 | 13885085.99 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.46 | 0.08 | 0.01 | 172714470.58 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.88 | 5.17 | 3.9 | -0.01 | 1220269.82 | 1.66 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.41 | 29.34 | 0.51 | 0.33 | 182894.69 | 12.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 2.34 | 1.16 | -0.01 | 797641.89 | 3.82 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.64 | 1.71 | -0.02 | 322359.25 | 10.92 | skipped_fast |
| EDELUSDT | IDLE | 1.77 | 3.92 | 0.48 | -0.03 | 225050.44 | 10.24 | skipped_fast |
| BIOUSDT | IDLE | 1.56 | 2.95 | 1.15 | 0.06 | 88014.87 | 6.83 | skipped_fast |
| ZBCNUSDT | IDLE | 1.07 | 1.96 | 1.14 | 0.01 | 202084.02 | 17.48 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 4.24 | 2.18 | -0.03 | 9650.09 | 69.07 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 3.16 | 2.81 | 0.08 | 71725.82 | 12.47 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.69 | 1.23 | 0.03 | 326598.82 | 6.49 | skipped_fast |
| TELUSDT | IDLE | 1.94 | 3.63 | 1.64 | -0.01 | 133353.73 | 44.54 | skipped_fast |
| REDUSDT | IDLE | 0.65 | 1.21 | 0.54 | 0.03 | 54648.92 | 15.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 1.1 | 0.87 | -0.03 | 43288.71 | 33.89 | skipped_fast |
| FLUIDUSDT | IDLE | 1.61 | 3.1 | 0.83 | 0.01 | 9926.52 | 21.37 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.79 | 0.63 | 0.01 | 54013.32 | 7.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.11 | 0.0 | 37827.84 | 12.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
