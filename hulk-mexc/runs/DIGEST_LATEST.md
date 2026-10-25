# Hulk DIGEST — 2026-10-25T03:57:20Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.88 | 1.73 | 0.16 | 0.02 | 26052835.13 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.36 | 0.4 | -0.01 | 122190780.31 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.75 | 0.2 | -0.0 | 249755667.98 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.29 | 2.44 | 1.87 | -0.06 | 761496.28 | 52.75 | skipped_fast |
| PYTHUSDT | IDLE | 1.77 | 3.36 | 1.24 | 0.01 | 507186.18 | 4.22 | skipped_fast |
| EDELUSDT | IDLE | 0.84 | 2.08 | 0.79 | -0.06 | 593241.01 | 26.51 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.08 | 8.8 | 1.75 | -0.01 | 42349.99 | 34.7 | skipped_fast |
| QNTUSDT | IDLE | 2.02 | 3.98 | 0.35 | 0.01 | 369144.21 | 2.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.71 | 5.02 | 2.96 | 0.04 | 87520.79 | 15.61 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 3.21 | 3.03 | -0.05 | 59846.56 | 11.49 | skipped_fast |
| REDUSDT | IDLE | 1.58 | 3.84 | 2.76 | -0.0 | 99587.0 | 14.92 | skipped_fast |
| LAUSDT | IDLE | 2.06 | 11.5 | 7.68 | -0.06 | 107068.72 | 28.29 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 1.85 | 0.71 | 0.0 | 226397.0 | 14.33 | skipped_fast |
| CCUSDT | IDLE | 0.67 | 1.26 | 0.5 | -0.02 | 205182.72 | 5.92 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.89 | 1.6 | -0.03 | 66230.59 | 13.17 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 2.14 | 0.65 | 0.01 | 56121.64 | 16.26 | skipped_fast |
| WAXLUSDT | IDLE | 2.22 | 5.99 | 2.67 | 0.01 | 57013.89 | 44.36 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.75 | 0.09 | 0.01 | 202001.03 | 11.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.38 | 2.8 | 1.39 | -0.04 | 13034.03 | 21.39 | skipped_fast |
| IOTAUSDT | IDLE | 1.04 | 1.89 | 1.29 | -0.02 | 67997.5 | 25.2 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.64 | 0.4 | -0.0 | 53608.77 | 31.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.12 | -0.01 | 37566.58 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
