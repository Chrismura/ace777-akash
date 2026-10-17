# Hulk DIGEST — 2026-10-17T05:13:03Z

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
| PYTHUSDT | IDLE | 1.01 | 3.25 | 2.92 | -0.09 | 1782422.72 | 1.18 | skipped_fast |
| XRPUSDT | IDLE | 0.37 | 0.71 | 0.16 | -0.02 | 25373646.84 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.56 | 0.1 | -0.01 | 195228258.38 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.17 | 0.33 | 0.06 | -0.01 | 304430149.67 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.37 | 3.67 | 0.49 | -0.04 | 1251548.67 | 16.55 | skipped_fast |
| QNTUSDT | IDLE | 1.24 | 2.48 | 0.05 | -0.02 | 701837.35 | 0.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.78 | 6.07 | 3.79 | -0.04 | 50687.36 | 34.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.87 | 3.37 | 2.47 | -0.03 | 203257.54 | 15.13 | skipped_fast |
| REDUSDT | IDLE | 1.94 | 3.73 | 2.6 | -0.04 | 73599.83 | 7.66 | skipped_fast |
| CCUSDT | IDLE | 0.8 | 1.57 | 0.22 | -0.02 | 353822.56 | 6.72 | skipped_fast |
| EDELUSDT | IDLE | 1.07 | 1.95 | 1.24 | 0.01 | 192114.33 | 23.77 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.48 | 0.0 | 0.01 | 57199.53 | 9.71 | skipped_fast |
| RWAINCUSDT | IDLE | 1.1 | 5.19 | 3.33 | -0.09 | 23790.38 | 16.66 | skipped_fast |
| CHIPUSDT | IDLE | 0.75 | 2.42 | 0.87 | -0.06 | 118103.81 | 12.9 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.32 | 0.47 | -0.03 | 65325.75 | 7.95 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.45 | 0.52 | -0.02 | 316392.26 | 8.33 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.58 | 0.87 | -0.04 | 95937.79 | 29.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.61 | 1.58 | -0.01 | 4738.52 | 21.41 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.01 | 52950.89 | 7.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.09 | 0.16 | 0.13 | -0.0 | 32239.58 | 4.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
