# Hulk DIGEST — 2026-10-26T06:14:26Z

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
| XRPUSDT | IDLE | 1.05 | 1.96 | 0.88 | -0.01 | 16833029.03 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.75 | 0.59 | -0.01 | 106775435.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.14 | 0.24 | -0.01 | 201259260.94 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 3.15 | 2.82 | 0.05 | 761208.38 | 5.44 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.07 | 10.37 | 1.21 | 0.05 | 101249.52 | 19.38 | skipped_fast |
| WUSDT | IDLE | 1.28 | 2.31 | 1.61 | -0.03 | 584922.7 | 17.92 | skipped_fast |
| QNTUSDT | IDLE | 1.15 | 3.44 | 0.5 | 0.06 | 739779.93 | 4.13 | skipped_fast |
| LAUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.12 | 8.72 | 1.77 | -0.01 | 61409.15 | 25.57 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.22 | 3.26 | -0.07 | 66620.74 | 17.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.58 | 2.92 | 1.96 | 0.01 | 184052.37 | 22.87 | skipped_fast |
| REDUSDT | IDLE | 2.02 | 3.84 | 1.3 | -0.01 | 61192.45 | 15.14 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 3.01 | 1.04 | 0.0 | 53652.96 | 12.42 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.52 | 1.07 | -0.02 | 61540.55 | 4.52 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.58 | 0.97 | 0.01 | 163495.8 | 5.95 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 2.13 | 1.18 | 0.06 | 171352.54 | 31.55 | skipped_fast |
| WAXLUSDT | IDLE | 2.06 | 3.78 | 2.32 | -0.01 | 53232.99 | 47.91 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.85 | 1.26 | -0.01 | 181136.19 | 11.74 | skipped_fast |
| IOTAUSDT | IDLE | 1.47 | 2.7 | 1.61 | -0.03 | 62636.52 | 25.98 | skipped_fast |
| RIZEUSDT | IDLE | 0.54 | 1.0 | 0.57 | -0.0 | 33114.81 | 64.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.55 | 2.7 | 1.17 | -0.02 | 19116.06 | 22.35 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.32 | 0.16 | -0.01 | 52695.02 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.57 | 0.4 | -0.01 | 37866.72 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
