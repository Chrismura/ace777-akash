# Hulk DIGEST — 2026-10-23T16:20:55Z

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
| XRPUSDT | IDLE | 0.93 | 1.69 | 1.11 | -0.01 | 28389744.89 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.84 | 1.6 | 0.59 | 0.0 | 221839245.41 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.15 | 0.52 | -0.0 | 311617728.56 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.67 | 3.17 | 1.14 | -0.05 | 1202070.19 | 0.55 | skipped_fast |
| EDELUSDT | IDLE | 2.6 | 4.93 | 1.82 | 0.01 | 468254.01 | 21.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.71 | 1.01 | -0.03 | 702400.35 | 1.39 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.45 | 1.6 | 0.0 | 623095.85 | 15.72 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 4.28 | 2.82 | 0.01 | 116215.32 | 15.86 | skipped_fast |
| CCUSDT | IDLE | 1.72 | 3.27 | 1.18 | 0.02 | 194577.82 | 0.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.75 | 3.34 | 1.7 | 0.02 | 198096.62 | 20.51 | skipped_fast |
| REDUSDT | IDLE | 2.09 | 4.13 | 0.38 | 0.01 | 60901.24 | 16.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 3.48 | 1.95 | 0.01 | 51530.28 | 11.06 | skipped_fast |
| RIZEUSDT | IDLE | 2.81 | 11.71 | 3.54 | -0.05 | 50293.09 | 216.18 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.29 | 0.08 | 0.02 | 70510.1 | 4.14 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.09 | 1.38 | -0.0 | 57865.73 | 10.82 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.16 | 1.87 | -0.02 | 303942.25 | 10.14 | skipped_fast |
| LAUSDT | IDLE | 2.09 | 4.11 | 0.45 | 0.06 | 56379.91 | 19.21 | skipped_fast |
| WAXLUSDT | IDLE | 1.99 | 3.95 | 0.22 | 0.02 | 57590.28 | 67.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.33 | 2.67 | 0.0 | -0.01 | 8317.6 | 21.85 | skipped_fast |
| IOTAUSDT | IDLE | 1.32 | 2.6 | 0.26 | 0.01 | 71547.5 | 53.11 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.55 | 0.08 | 0.02 | 52001.0 | 15.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.73 | 1.32 | 0.98 | -0.01 | 36379.19 | 74.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
