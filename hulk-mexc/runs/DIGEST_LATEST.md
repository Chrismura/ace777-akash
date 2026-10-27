# Hulk DIGEST — 2026-10-27T20:16:22Z

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
| ETHUSDT | IDLE | 0.63 | 1.19 | 0.43 | 0.01 | 228599024.35 | 0.55 | skipped_fast |
| XRPUSDT | IDLE | 0.58 | 1.11 | 0.33 | 0.02 | 19369723.79 | 1.51 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.7 | 0.07 | 0.01 | 319393967.42 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.32 | 5.0 | 4.2 | 0.02 | 673897.3 | 15.6 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 2.23 | 2.03 | 0.01 | 480593.14 | 27.8 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.75 | 0.71 | -0.01 | 386996.15 | 4.11 | skipped_fast |
| QNTUSDT | IDLE | 1.19 | 2.27 | 0.78 | -0.01 | 724594.12 | 3.5 | skipped_fast |
| CHIPUSDT | IDLE | 1.9 | 4.68 | 0.07 | 0.05 | 130673.34 | 12.77 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 2.26 | 2.01 | -0.01 | 223200.54 | 6.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.08 | 2.94 | 2.15 | 0.03 | 241643.34 | 20.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 4.0 | 0.0 | -0.04 | 62675.2 | 6.5 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 3.08 | 0.75 | 0.02 | 58884.62 | 8.85 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 2.38 | 1.65 | 0.04 | 57587.9 | 9.29 | skipped_fast |
| LAUSDT | IDLE | 2.6 | 5.38 | 1.74 | 0.04 | 58621.06 | 21.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 3.34 | 0.69 | -0.0 | 32556.98 | 55.83 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.38 | 0.13 | 0.07 | 59984.9 | 14.11 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.75 | 0.67 | -0.01 | 258189.68 | 7.88 | skipped_fast |
| IOTAUSDT | IDLE | 1.02 | 1.82 | 1.5 | -0.01 | 80137.43 | 31.0 | skipped_fast |
| WAXLUSDT | IDLE | 0.78 | 1.5 | 0.34 | 0.04 | 55837.88 | 36.61 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.29 | 0.16 | -0.0 | 57234.1 | 31.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.47 | 0.63 | 0.01 | 2855.44 | 21.34 | skipped_fast |
| MNSRYUSDT | IDLE | 0.44 | 0.78 | 0.62 | -0.0 | 37499.18 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
