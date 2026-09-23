# Hulk DIGEST — 2026-09-23T23:09:18Z

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
| PYTHUSDT | IDLE | 1.25 | 3.93 | 2.68 | -0.07 | 1580402.15 | 4.78 | skipped_fast |
| XRPUSDT | IDLE | 0.76 | 2.19 | 0.67 | -0.05 | 111273537.5 | 1.33 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.47 | 0.4 | -0.03 | 476738447.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.18 | -0.02 | 835692606.76 | 0.1 | skipped_fast |
| HBARUSDT | IDLE | 0.48 | 1.56 | 0.63 | -0.09 | 1323606.06 | 1.1 | skipped_fast |
| CCUSDT | IDLE | 1.01 | 2.45 | 0.6 | -0.05 | 536852.82 | 6.4 | skipped_fast |
| WUSDT | IDLE | 1.05 | 2.91 | 1.98 | -0.08 | 381741.25 | 6.24 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 3.95 | 2.51 | -0.07 | 167455.92 | 21.44 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.54 | 0.34 | -0.05 | 174209.1 | 11.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.84 | 2.86 | 1.44 | -0.1 | 217888.63 | 16.7 | skipped_fast |
| ZBCNUSDT | IDLE | 0.97 | 2.58 | 0.42 | 0.01 | 239849.08 | 40.79 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 2.62 | 2.25 | -0.06 | 59367.8 | 14.58 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 2.04 | 0.98 | -0.06 | 95077.82 | 3.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.89 | 4.32 | 2.25 | 0.06 | 65769.36 | 115.26 | skipped_fast |
| RWAINCUSDT | IDLE | 0.71 | 1.31 | 0.7 | -0.01 | 19066.08 | 59.57 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.89 | 0.4 | -0.06 | 153319.12 | 23.03 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.39 | 0.87 | -0.04 | 131283.23 | 1.41 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.96 | 0.22 | -0.02 | 56246.6 | 29.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.94 | 2.08 | 0.68 | -0.05 | 5700.1 | 23.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.17 | -0.01 | 40972.7 | 16.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
