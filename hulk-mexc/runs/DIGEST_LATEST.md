# Hulk DIGEST — 2026-09-01T20:27:33Z

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
| XRPUSDT | IDLE | 1.78 | 3.21 | 2.29 | -0.03 | 33526873.32 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 1.6 | 2.98 | 1.46 | -0.02 | 326349368.79 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.22 | 2.29 | 1.03 | -0.02 | 535359404.94 | 0.0 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 10.09 | 0.18 | 0.17 | 580245.9 | 2.2 | skipped_fast |
| PYTHUSDT | IDLE | 2.07 | 3.94 | 1.29 | 0.03 | 647277.53 | 1.98 | skipped_fast |
| ZBCNUSDT | IDLE | 3.45 | 6.37 | 3.47 | 0.02 | 201425.33 | 6.38 | skipped_fast |
| CCUSDT | IDLE | 1.72 | 3.62 | 3.08 | -0.09 | 348744.32 | 9.66 | skipped_fast |
| WUSDT | IDLE | 1.7 | 3.61 | 0.37 | 0.08 | 362021.34 | 12.18 | skipped_fast |
| REDUSDT | IDLE | 2.07 | 6.24 | 4.69 | 0.06 | 109718.73 | 14.19 | skipped_fast |
| RIZEUSDT | IDLE | 2.6 | 4.92 | 2.85 | -0.04 | 44345.9 | 71.98 | skipped_fast |
| BIOUSDT | IDLE | 1.81 | 3.31 | 2.1 | -0.03 | 70753.1 | 3.89 | skipped_fast |
| EDELUSDT | IDLE | 0.95 | 7.1 | 5.68 | -0.05 | 171995.06 | 36.43 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 3.03 | 0.24 | 0.04 | 69030.28 | 20.19 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 5.08 | 4.02 | -0.06 | 94705.31 | 66.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.4 | 2.8 | 0.0 | -0.0 | 6712.65 | 11.59 | skipped_fast |
| FLUIDUSDT | IDLE | 2.52 | 4.41 | 4.22 | -0.03 | 129.84 | 21.83 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.74 | 0.17 | 0.01 | 247358.34 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.32 | 2.4 | 1.6 | 0.03 | 47910.06 | 3.15 | skipped_fast |
| MNSRYUSDT | IDLE | 0.94 | 1.71 | 1.09 | -0.02 | 33987.01 | 19.2 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 1.01 | 0.84 | -0.02 | 59635.08 | 23.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
