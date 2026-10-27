# Hulk DIGEST — 2026-10-27T00:35:29Z

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
| XRPUSDT | IDLE | 1.12 | 2.19 | 0.32 | 0.01 | 25117236.35 | 2.29 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.18 | 0.1 | -0.0 | 135577613.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.74 | 0.07 | -0.0 | 360077162.17 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 0.5 | 2.21 | 0.94 | 0.07 | 1414666.35 | 2.95 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 3.12 | 0.86 | -0.01 | 729270.43 | 4.01 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.91 | 0.51 | 0.05 | 640673.96 | 28.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 8.65 | 6.03 | 0.17 | 324157.69 | 13.55 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 8.07 | 6.93 | -0.11 | 59386.09 | 25.66 | skipped_fast |
| REDUSDT | IDLE | 1.56 | 2.95 | 1.09 | 0.02 | 62014.87 | 8.81 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 2.05 | 0.3 | -0.02 | 184715.06 | 8.01 | skipped_fast |
| ZBCNUSDT | IDLE | 0.89 | 1.65 | 0.93 | -0.06 | 217430.75 | 28.01 | skipped_fast |
| EDELUSDT | IDLE | 1.09 | 2.0 | 1.26 | 0.02 | 139442.62 | 24.84 | skipped_fast |
| FLUIDUSDT | IDLE | 2.72 | 5.41 | 0.18 | 0.03 | 2299.73 | 21.59 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 2.1 | 0.13 | -0.0 | 57203.27 | 8.95 | skipped_fast |
| KITEUSDT | IDLE | 0.67 | 1.26 | 0.51 | 0.0 | 53946.85 | 14.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.03 | 1.95 | 0.74 | -0.0 | 44444.48 | 60.47 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.66 | 0.21 | -0.0 | 241744.94 | 7.75 | skipped_fast |
| IOTAUSDT | IDLE | 1.43 | 2.75 | 0.7 | -0.01 | 85769.18 | 28.08 | skipped_fast |
| LAUSDT | IDLE | 1.4 | 2.82 | 1.56 | 0.04 | 67754.99 | 37.49 | skipped_fast |
| WAXLUSDT | IDLE | 1.38 | 2.76 | 0.02 | -0.02 | 53659.76 | 62.46 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.21 | 0.4 | -0.0 | 53255.9 | 15.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.45 | -0.01 | 41530.26 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
