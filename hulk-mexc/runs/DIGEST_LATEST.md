# Hulk DIGEST — 2026-10-25T07:36:11Z

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
| XRPUSDT | IDLE | 0.89 | 1.62 | 1.03 | 0.01 | 26832890.9 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.49 | 1.07 | -0.01 | 127272633.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.73 | 0.48 | -0.0 | 219596940.05 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.11 | 2.01 | 1.46 | -0.05 | 946522.94 | 14.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.31 | 2.41 | 1.34 | 0.0 | 498381.23 | 1.41 | skipped_fast |
| EDELUSDT | IDLE | 0.83 | 2.01 | 1.18 | -0.07 | 597398.36 | 36.64 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 2.81 | 2.59 | -0.06 | 59060.85 | 14.3 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 2.7 | 1.05 | 0.01 | 372685.01 | 2.18 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.59 | 0.96 | -0.02 | 207300.3 | 8.94 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.52 | 0.92 | 0.01 | 235395.08 | 18.99 | skipped_fast |
| BIOUSDT | IDLE | 1.2 | 2.1 | 2.01 | -0.03 | 64959.76 | 8.92 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 2.95 | 2.51 | 0.05 | 89991.73 | 15.84 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 2.21 | 1.47 | -0.02 | 81182.13 | 14.96 | skipped_fast |
| WAXLUSDT | IDLE | 2.71 | 5.02 | 4.6 | -0.02 | 55508.43 | 71.1 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 1.86 | 0.91 | -0.0 | 57551.56 | 10.85 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 1.98 | 1.06 | 0.01 | 207961.03 | 2.57 | skipped_fast |
| LAUSDT | IDLE | 0.88 | 4.73 | 4.52 | -0.11 | 95876.19 | 20.43 | skipped_fast |
| RIZEUSDT | IDLE | 0.32 | 0.91 | 0.14 | -0.04 | 41325.12 | 62.39 | skipped_fast |
| IOTAUSDT | IDLE | 0.95 | 1.69 | 1.39 | -0.01 | 65670.15 | 29.99 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 1.28 | 1.27 | -0.04 | 9982.01 | 21.4 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.52 | 0.47 | 0.0 | 52678.11 | 63.14 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.76 | 0.72 | -0.01 | 37410.72 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
