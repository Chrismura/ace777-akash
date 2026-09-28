# Hulk DIGEST — 2026-09-28T12:23:35Z

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
| QNTUSDT | IDLE | 1.44 | 47.4 | 15.41 | 0.48 | 19947095.58 | 6.58 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.48 | 29.82 | 0.16 | 0.31 | 5997204.05 | 13.64 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 14.75 | 10.0 | -0.04 | 1197438.9 | 9.06 | skipped_fast |
| WUSDT | IDLE | 1.27 | 5.62 | 1.15 | -0.02 | 3284697.98 | 9.08 | skipped_fast |
| XRPUSDT | IDLE | 1.69 | 3.33 | 0.3 | -0.02 | 55439319.38 | 1.98 | skipped_fast |
| PYTHUSDT | IDLE | 1.89 | 4.6 | 1.74 | -0.07 | 1561632.36 | 2.46 | skipped_fast |
| ETHUSDT | IDLE | 1.06 | 2.07 | 0.32 | -0.01 | 321290530.2 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.06 | 0.17 | -0.02 | 677365070.41 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.6 | 24.05 | 3.4 | 0.04 | 191200.08 | 16.74 | skipped_fast |
| KITEUSDT | IDLE | 1.98 | 6.31 | 3.68 | -0.08 | 103770.26 | 9.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 2.32 | 0.49 | -0.05 | 212428.84 | 18.24 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 3.28 | 0.6 | -0.06 | 106129.69 | 3.33 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 3.29 | 0.19 | -0.04 | 61130.89 | 13.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 3.27 | 0.31 | -0.08 | 86198.2 | 13.3 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 3.87 | 2.08 | 0.0 | 162210.75 | 27.94 | skipped_fast |
| RIZEUSDT | IDLE | 0.4 | 2.49 | 0.54 | -0.14 | 59773.78 | 27.1 | skipped_fast |
| RWAINCUSDT | IDLE | 0.38 | 3.96 | 0.04 | 0.14 | 33261.6 | 87.75 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.53 | 0.79 | -0.02 | 59783.07 | 7.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 2.38 | 0.86 | -0.06 | 3276.58 | 21.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.73 | 0.63 | -0.02 | 35175.62 | 59.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
