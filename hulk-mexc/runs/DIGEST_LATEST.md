# Hulk DIGEST — 2026-10-20T00:07:27Z

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
| ETHUSDT | IDLE | 0.6 | 1.13 | 0.53 | -0.0 | 124127459.23 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.03 | 0.67 | -0.0 | 20405697.28 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.57 | 0.51 | -0.0 | 318869776.68 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.93 | 3.64 | 1.43 | -0.01 | 804169.94 | 2.73 | skipped_fast |
| WUSDT | IDLE | 2.23 | 4.01 | 3.06 | 0.0 | 708499.15 | 17.56 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 3.95 | 1.68 | 0.01 | 193685.81 | 11.17 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 1.95 | 1.36 | 0.01 | 713330.07 | 5.66 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.39 | 0.27 | 0.04 | 365411.71 | 6.64 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 3.49 | 1.23 | 0.07 | 76667.69 | 10.61 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 2.93 | 0.8 | 0.03 | 79446.83 | 11.85 | skipped_fast |
| ZBCNUSDT | IDLE | 0.91 | 2.56 | 0.14 | 0.02 | 222361.26 | 23.71 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.73 | 0.86 | -0.01 | 58156.67 | 10.16 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.79 | 0.44 | -0.03 | 446518.21 | 4.83 | skipped_fast |
| RWAINCUSDT | IDLE | 1.05 | 2.07 | 2.03 | 0.03 | 69310.69 | 5.19 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.63 | 0.72 | -0.01 | 69232.44 | 4.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.7 | 2.25 | 1.99 | -0.06 | 53418.14 | 65.34 | skipped_fast |
| IOTAUSDT | IDLE | 1.0 | 1.89 | 0.68 | 0.0 | 90633.57 | 26.7 | skipped_fast |
| LAUSDT | IDLE | 1.05 | 1.88 | 1.49 | -0.02 | 56067.26 | 23.01 | skipped_fast |
| WAXLUSDT | IDLE | 1.2 | 3.21 | 2.12 | -0.05 | 62744.8 | 73.93 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.79 | 0.0 | 0.01 | 54411.68 | 15.66 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.1 | 0.0 | 41045.23 | 8.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 4709.59 | 21.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
