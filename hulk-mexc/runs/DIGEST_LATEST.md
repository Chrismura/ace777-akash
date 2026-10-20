# Hulk DIGEST — 2026-10-20T19:22:51Z

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
| ETHUSDT | IDLE | 1.57 | 2.84 | 1.98 | 0.01 | 148536883.23 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.56 | 2.82 | 2.06 | 0.01 | 23764257.26 | 1.52 | skipped_fast |
| BTCUSDT | IDLE | 0.89 | 1.61 | 1.17 | 0.01 | 321380411.4 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.31 | 5.65 | 2.04 | 0.07 | 1089610.3 | 10.33 | skipped_fast |
| WUSDT | IDLE | 2.54 | 4.91 | 1.13 | 0.0 | 648538.47 | 15.7 | skipped_fast |
| QNTUSDT | IDLE | 2.93 | 5.15 | 4.74 | -0.0 | 735659.74 | 6.19 | skipped_fast |
| ZBCNUSDT | IDLE | 3.89 | 7.13 | 4.3 | 0.01 | 189570.84 | 18.92 | skipped_fast |
| EDELUSDT | IDLE | 1.55 | 14.65 | 2.9 | 0.31 | 350436.31 | 25.41 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 7.7 | 7.15 | 0.06 | 198425.85 | 6.81 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.55 | 1.82 | 0.02 | 390805.86 | 5.72 | skipped_fast |
| REDUSDT | IDLE | 2.4 | 4.44 | 2.4 | 0.03 | 59667.98 | 15.86 | skipped_fast |
| BIOUSDT | IDLE | 2.24 | 4.17 | 2.08 | 0.04 | 62967.71 | 8.19 | skipped_fast |
| HBARUSDT | IDLE | 2.08 | 3.68 | 3.2 | 0.01 | 388030.82 | 8.43 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 2.28 | 2.03 | 0.01 | 82961.66 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 4.0 | 2.13 | -0.04 | 69613.68 | 21.23 | skipped_fast |
| WAXLUSDT | IDLE | 2.71 | 4.75 | 4.53 | -0.05 | 55911.63 | 37.54 | skipped_fast |
| IOTAUSDT | IDLE | 2.29 | 4.03 | 3.85 | 0.04 | 73702.36 | 26.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.01 | 4.35 | 0.55 | 0.04 | 69748.72 | 55.35 | skipped_fast |
| LAUSDT | IDLE | 1.96 | 3.55 | 2.47 | 0.02 | 56106.07 | 20.66 | skipped_fast |
| FLUIDUSDT | IDLE | 2.13 | 4.1 | 1.02 | 0.05 | 6086.16 | 19.4 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.42 | 0.93 | 0.0 | 52560.99 | 7.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 1.02 | 0.38 | 0.0 | 40222.22 | 14.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
