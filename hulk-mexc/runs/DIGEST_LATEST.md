# Hulk DIGEST — 2026-10-24T19:31:05Z

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
| ETHUSDT | IDLE | 1.99 | 3.79 | 1.23 | -0.02 | 139443956.45 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 2.69 | 0.01 | -0.01 | 30319285.07 | 0.78 | skipped_fast |
| BTCUSDT | IDLE | 0.96 | 1.88 | 0.25 | -0.01 | 281507425.2 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.57 | 5.0 | 0.87 | -0.02 | 667285.21 | 2.87 | skipped_fast |
| WUSDT | IDLE | 1.46 | 3.3 | 1.72 | -0.08 | 934179.63 | 59.68 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 4.99 | 2.04 | -0.04 | 609862.54 | 13.21 | skipped_fast |
| ZBCNUSDT | IDLE | 2.76 | 6.16 | 2.05 | -0.06 | 216294.83 | 22.98 | skipped_fast |
| CHIPUSDT | IDLE | 3.05 | 6.32 | 0.0 | -0.01 | 80790.57 | 13.78 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 3.8 | 0.66 | -0.01 | 241602.08 | 8.91 | skipped_fast |
| KITEUSDT | IDLE | 2.26 | 4.47 | 2.35 | -0.06 | 62664.05 | 11.47 | skipped_fast |
| BIOUSDT | IDLE | 2.16 | 4.07 | 1.61 | -0.05 | 70943.8 | 4.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.16 | 3.92 | 2.66 | -0.01 | 50727.08 | 10.93 | skipped_fast |
| RIZEUSDT | IDLE | 2.57 | 4.6 | 3.55 | -0.05 | 30643.07 | 67.22 | skipped_fast |
| QNTUSDT | IDLE | 1.75 | 3.41 | 0.63 | -0.02 | 375081.72 | 0.56 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 4.28 | 1.29 | 0.04 | 95659.79 | 15.68 | skipped_fast |
| LAUSDT | IDLE | 1.84 | 10.48 | 5.02 | 0.07 | 107638.31 | 20.52 | skipped_fast |
| HBARUSDT | IDLE | 1.68 | 3.34 | 0.13 | -0.01 | 221954.15 | 6.46 | skipped_fast |
| FLUIDUSDT | IDLE | 2.05 | 4.65 | 3.66 | -0.09 | 15243.97 | 21.53 | skipped_fast |
| IOTAUSDT | IDLE | 1.93 | 3.77 | 0.59 | -0.03 | 70365.75 | 34.49 | skipped_fast |
| WAXLUSDT | IDLE | 1.28 | 3.98 | 1.53 | 0.02 | 60660.14 | 67.37 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.28 | 0.71 | -0.01 | 53401.8 | 31.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.89 | 1.59 | 1.25 | -0.02 | 38798.07 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
