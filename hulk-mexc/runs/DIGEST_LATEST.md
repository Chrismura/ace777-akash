# Hulk DIGEST — 2026-10-19T20:03:02Z

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
| ETHUSDT | IDLE | 0.77 | 1.39 | 1.01 | 0.02 | 146255017.25 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.67 | 1.25 | 0.64 | 0.03 | 24983404.1 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.96 | 0.79 | 0.01 | 356639304.14 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.53 | 4.47 | 3.87 | -0.01 | 915696.88 | 1.39 | skipped_fast |
| WUSDT | IDLE | 2.67 | 5.03 | 2.08 | 0.04 | 671945.01 | 17.4 | skipped_fast |
| RIZEUSDT | IDLE | 3.05 | 10.48 | 4.04 | -0.05 | 52832.23 | 20.67 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 3.59 | 2.37 | 0.06 | 716783.26 | 2.06 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.95 | 2.46 | 0.06 | 417181.42 | 10.62 | skipped_fast |
| EDELUSDT | IDLE | 1.26 | 2.51 | 1.28 | 0.05 | 211734.23 | 7.41 | skipped_fast |
| ZBCNUSDT | IDLE | 0.9 | 3.07 | 2.35 | 0.03 | 255689.15 | 24.97 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.87 | 2.45 | 0.02 | 58263.37 | 16.93 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 3.65 | 2.75 | 0.08 | 67987.31 | 9.1 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 3.63 | 0.69 | 0.07 | 73111.1 | 19.08 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.38 | 0.95 | -0.0 | 485277.1 | 3.65 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.07 | 1.22 | 0.03 | 70061.25 | 4.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.05 | 2.33 | 0.56 | 0.05 | 84201.53 | 25.48 | skipped_fast |
| WAXLUSDT | IDLE | 1.16 | 2.74 | 1.86 | -0.01 | 65102.79 | 26.82 | skipped_fast |
| LAUSDT | IDLE | 1.12 | 2.07 | 1.1 | 0.03 | 56203.2 | 24.84 | skipped_fast |
| IOTAUSDT | IDLE | 0.86 | 1.63 | 0.56 | 0.04 | 93029.72 | 24.59 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.66 | 1.64 | 0.04 | 4870.83 | 21.52 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.71 | 0.16 | 0.02 | 54902.54 | 15.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.39 | 0.04 | -0.0 | 40175.76 | 15.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
