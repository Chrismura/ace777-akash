# Hulk DIGEST — 2026-09-22T21:16:05Z

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
| XRPUSDT | IDLE | 2.19 | 4.05 | 2.14 | 0.04 | 116368466.69 | 1.9 | skipped_fast |
| HBARUSDT | IDLE | 2.49 | 6.27 | 1.41 | 0.08 | 1682150.45 | 1.01 | skipped_fast |
| PYTHUSDT | IDLE | 0.71 | 3.25 | 2.01 | 0.04 | 1676624.84 | 4.52 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.24 | 0.6 | -0.01 | 410816218.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.67 | 0.5 | -0.0 | 921056502.89 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.47 | 10.49 | 8.07 | -0.01 | 286807.9 | 53.4 | skipped_fast |
| CCUSDT | IDLE | 1.86 | 3.41 | 2.08 | -0.03 | 478780.84 | 13.21 | skipped_fast |
| ZBCNUSDT | IDLE | 2.55 | 4.6 | 3.3 | -0.02 | 215629.14 | 5.47 | skipped_fast |
| RWAINCUSDT | IDLE | 3.56 | 9.09 | 3.94 | 0.03 | 18864.36 | 94.89 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.81 | 1.84 | 0.02 | 335179.03 | 2.51 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 22.04 | 3.04 | -0.07 | 46895.45 | 111.73 | skipped_fast |
| CHIPUSDT | IDLE | 2.09 | 3.97 | 2.92 | -0.01 | 138651.38 | 17.69 | skipped_fast |
| BIOUSDT | IDLE | 1.7 | 3.19 | 1.41 | 0.02 | 136374.31 | 3.41 | skipped_fast |
| KITEUSDT | IDLE | 0.81 | 3.49 | 1.42 | 0.16 | 112780.55 | 9.42 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.14 | 0.64 | 0.05 | 63589.51 | 13.3 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 5.95 | 0.16 | 0.1 | 106683.23 | 27.31 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 2.93 | 0.0 | 0.09 | 172301.03 | 1.36 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.24 | 0.36 | -0.0 | 53588.19 | 7.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.18 | 0.12 | 0.01 | 7050.54 | 21.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.05 | -0.0 | 40308.67 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
