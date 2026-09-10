# Hulk DIGEST — 2026-09-10T06:15:24Z

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
| XRPUSDT | IDLE | 0.74 | 1.37 | 0.76 | -0.03 | 42020850.82 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.11 | 0.31 | -0.01 | 366633421.15 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.74 | 0.3 | -0.01 | 519845521.62 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.05 | 2.94 | 0.58 | -0.04 | 1035320.43 | 1.89 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.41 | 1.08 | -0.04 | 617558.86 | 7.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.69 | 5.11 | 1.86 | 0.04 | 185546.34 | 25.77 | skipped_fast |
| REDUSDT | IDLE | 2.74 | 4.8 | 4.55 | -0.04 | 63474.32 | 18.57 | skipped_fast |
| EDELUSDT | IDLE | 1.83 | 6.99 | 2.75 | 0.07 | 244505.52 | 35.49 | skipped_fast |
| WUSDT | IDLE | 1.56 | 2.92 | 2.41 | -0.04 | 211486.38 | 11.29 | skipped_fast |
| CHIPUSDT | IDLE | 0.9 | 5.04 | 3.95 | -0.07 | 124483.63 | 16.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.29 | 15.41 | 2.93 | 0.13 | 62218.33 | 101.97 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 2.47 | 0.93 | -0.06 | 104504.25 | 7.84 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.46 | 0.43 | -0.03 | 428381.16 | 1.3 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 1.86 | 1.66 | -0.01 | 56683.66 | 11.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.39 | 0.89 | -0.0 | 5938.39 | 55.8 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 2.0 | 1.9 | -0.03 | 41576.84 | 6.01 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.09 | 0.66 | 0.01 | 87579.84 | 49.96 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.91 | 0.0 | -0.05 | 1391.88 | 21.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 1.0 | 0.12 | -0.02 | 27134.73 | 4.13 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.68 | 0.07 | -0.03 | 54937.07 | 7.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
