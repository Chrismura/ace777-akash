# Hulk DIGEST — 2026-10-03T23:58:32Z

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
| QNTUSDT | IDLE | 2.89 | 7.05 | 4.9 | 0.04 | 3423561.98 | 6.62 | skipped_fast |
| XRPUSDT | IDLE | 0.4 | 0.71 | 0.54 | 0.0 | 17957463.43 | 1.35 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.56 | 0.31 | 0.0 | 290166598.91 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.16 | 0.31 | 0.08 | 0.01 | 106037364.1 | 0.07 | skipped_fast |
| EDELUSDT | IDLE | 1.58 | 9.53 | 2.24 | 0.13 | 408516.64 | 8.39 | skipped_fast |
| RIZEUSDT | IDLE | 2.45 | 13.92 | 5.51 | -0.12 | 47895.16 | 27.82 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 5.2 | 4.55 | 0.01 | 77411.26 | 9.93 | skipped_fast |
| WUSDT | IDLE | 1.65 | 3.06 | 1.62 | 0.03 | 341618.44 | 7.97 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 2.61 | 0.0 | 0.03 | 297425.69 | 8.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 2.76 | 1.74 | -0.03 | 235207.65 | 27.2 | skipped_fast |
| PYTHUSDT | IDLE | 0.66 | 1.25 | 0.47 | -0.01 | 390861.83 | 2.56 | skipped_fast |
| TELUSDT | IDLE | 3.37 | 6.69 | 1.69 | 0.0 | 130875.03 | 40.51 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.9 | 0.51 | 0.05 | 4187.48 | 31.26 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 3.45 | 1.65 | 0.08 | 64367.72 | 7.18 | skipped_fast |
| BIOUSDT | IDLE | 0.71 | 1.29 | 0.86 | 0.01 | 69134.06 | 6.41 | skipped_fast |
| CHIPUSDT | IDLE | 0.84 | 1.63 | 0.34 | -0.0 | 57714.6 | 15.89 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.16 | 0.71 | -0.0 | 361632.58 | 4.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.59 | 3.19 | 0.0 | 0.07 | 1302.05 | 21.04 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.81 | 0.44 | 0.0 | 55153.49 | 14.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.62 | 0.17 | -0.0 | 35054.21 | 23.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
