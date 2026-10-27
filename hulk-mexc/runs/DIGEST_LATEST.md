# Hulk DIGEST — 2026-10-27T18:15:07Z

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
| ETHUSDT | IDLE | 0.94 | 1.8 | 0.5 | 0.01 | 221721963.96 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.91 | 1.7 | 0.76 | 0.02 | 19522930.51 | 2.27 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.15 | 0.29 | 0.0 | 317568840.27 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.34 | 5.0 | 4.55 | 0.03 | 704435.15 | 14.11 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.67 | 1.74 | -0.04 | 779322.39 | 2.01 | skipped_fast |
| CHIPUSDT | IDLE | 2.51 | 5.97 | 2.83 | -0.04 | 148766.73 | 16.88 | skipped_fast |
| EDELUSDT | IDLE | 1.25 | 2.23 | 1.79 | 0.0 | 473563.55 | 24.65 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 2.32 | 0.64 | -0.02 | 414431.89 | 2.75 | skipped_fast |
| KITEUSDT | IDLE | 2.07 | 3.91 | 2.16 | 0.04 | 57817.56 | 9.29 | skipped_fast |
| REDUSDT | IDLE | 2.06 | 4.18 | 0.37 | 0.06 | 59320.15 | 16.72 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.9 | 1.23 | -0.01 | 233715.46 | 7.08 | skipped_fast |
| LAUSDT | IDLE | 3.18 | 6.62 | 1.8 | 0.04 | 58566.91 | 24.73 | skipped_fast |
| ZBCNUSDT | IDLE | 1.0 | 2.97 | 0.35 | 0.03 | 256986.07 | 45.27 | skipped_fast |
| BIOUSDT | IDLE | 1.56 | 3.06 | 0.35 | 0.01 | 58782.94 | 8.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 3.34 | 0.67 | -0.01 | 52805.72 | 48.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.65 | 2.32 | 0.07 | -0.1 | 62425.72 | 26.76 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.75 | 0.94 | -0.01 | 215484.58 | 6.59 | skipped_fast |
| IOTAUSDT | IDLE | 1.11 | 2.01 | 1.43 | -0.01 | 77802.7 | 16.68 | skipped_fast |
| WAXLUSDT | IDLE | 1.22 | 2.16 | 1.93 | 0.0 | 54725.96 | 47.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | 0.05 | 3238.71 | 22.21 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.37 | 0.24 | -0.01 | 57321.76 | 31.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.78 | 0.07 | 0.01 | 37400.92 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
