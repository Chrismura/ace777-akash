# Hulk DIGEST — 2026-10-25T19:07:42Z

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
| XRPUSDT | IDLE | 0.8 | 1.46 | 0.87 | 0.01 | 14396024.1 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.45 | 0.54 | 0.01 | 82432422.58 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.8 | 0.4 | 0.0 | 144285636.28 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 4.17 | 8.0 | 3.08 | 0.05 | 200267.82 | 9.84 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.47 | 8.06 | 0.66 | 0.03 | 401614.53 | 31.75 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.99 | 1.14 | -0.02 | 578025.03 | 2.48 | skipped_fast |
| QNTUSDT | IDLE | 2.91 | 9.11 | 3.69 | 0.08 | 609389.65 | 9.86 | skipped_fast |
| PYTHUSDT | IDLE | 2.47 | 4.79 | 0.99 | 0.05 | 454049.04 | 4.07 | skipped_fast |
| CHIPUSDT | IDLE | 3.08 | 5.84 | 2.14 | 0.04 | 91775.47 | 15.49 | skipped_fast |
| KITEUSDT | IDLE | 2.77 | 5.12 | 2.74 | -0.01 | 53472.05 | 13.31 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.19 | 16.72 | 0.15 | 0.06 | 19331.52 | 21.41 | skipped_fast |
| REDUSDT | IDLE | 2.19 | 4.24 | 0.9 | -0.01 | 63681.37 | 16.48 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 2.64 | 0.55 | 0.01 | 178044.84 | 8.78 | skipped_fast |
| BIOUSDT | IDLE | 1.2 | 2.26 | 0.88 | -0.01 | 59629.69 | 4.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.03 | 1.83 | 1.53 | -0.01 | 62064.0 | 5.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 1.83 | 0.23 | 0.0 | 44838.43 | 53.16 | skipped_fast |
| WAXLUSDT | IDLE | 1.92 | 3.56 | 1.84 | 0.0 | 53047.68 | 50.85 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.14 | 0.52 | 0.0 | 127935.48 | 9.02 | skipped_fast |
| LAUSDT | IDLE | 0.98 | 3.89 | 0.8 | -0.1 | 71125.61 | 18.95 | skipped_fast |
| IOTAUSDT | IDLE | 1.16 | 2.19 | 0.92 | -0.01 | 63808.35 | 30.14 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.96 | 0.24 | 0.0 | 51437.95 | 7.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.9 | 1.57 | 1.52 | -0.01 | 37033.58 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
