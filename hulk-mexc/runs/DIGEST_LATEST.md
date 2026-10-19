# Hulk DIGEST — 2026-10-19T23:57:05Z

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
| XRPUSDT | IDLE | 0.62 | 1.15 | 0.57 | -0.0 | 20684762.91 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.14 | 0.41 | -0.0 | 124478102.01 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.31 | 0.57 | 0.36 | -0.0 | 318965665.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 3.64 | 1.18 | -0.02 | 809294.71 | 1.36 | skipped_fast |
| WUSDT | IDLE | 2.26 | 4.1 | 2.79 | 0.0 | 706913.25 | 15.21 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.46 | 1.31 | 0.01 | 715182.06 | 2.57 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 3.95 | 1.79 | 0.01 | 194731.38 | 14.89 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.39 | 0.35 | 0.04 | 361765.79 | 6.65 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 3.71 | 1.19 | 0.07 | 76487.55 | 8.95 | skipped_fast |
| ZBCNUSDT | IDLE | 0.98 | 2.64 | 0.86 | 0.02 | 225710.99 | 21.94 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 2.93 | 0.47 | 0.04 | 79416.07 | 9.45 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 2.74 | 0.63 | -0.0 | 58249.4 | 15.93 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.79 | 0.29 | -0.03 | 447378.58 | 7.23 | skipped_fast |
| BIOUSDT | IDLE | 1.1 | 2.11 | 0.55 | -0.0 | 69093.77 | 8.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.86 | 1.7 | 1.68 | 0.04 | 69093.26 | 5.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 2.25 | 1.74 | -0.06 | 53428.65 | 65.34 | skipped_fast |
| IOTAUSDT | IDLE | 1.18 | 2.28 | 0.51 | 0.0 | 90768.64 | 31.08 | skipped_fast |
| LAUSDT | IDLE | 1.22 | 2.3 | 0.94 | -0.01 | 56165.05 | 20.97 | skipped_fast |
| WAXLUSDT | IDLE | 1.18 | 3.21 | 1.79 | -0.06 | 63018.33 | 73.93 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.87 | 0.08 | 0.01 | 54092.45 | 15.66 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.29 | 0.16 | 0.0 | 40923.6 | 5.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 4709.59 | 21.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
