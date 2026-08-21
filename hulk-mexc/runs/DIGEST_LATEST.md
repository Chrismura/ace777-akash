# Hulk DIGEST — 2026-08-21T23:48:27Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.59 | 0.1 | 6183698.98 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.17 | 0.15 | 141815715.87 | 3.43 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 11.25 | 1.98 | 0.13 | 514201.46 | 12.0 | skipped_fast |
| HBARUSDT | IDLE | 2.62 | 6.36 | 1.06 | 0.09 | 906950.57 | 2.5 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.01 | 0.13 | 644724.31 | 7.12 | skipped_fast |
| WUSDT | IDLE | 2.78 | 6.91 | 1.95 | 0.08 | 378298.01 | 13.39 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.31 | 0.03 | 546923.86 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.17 | 0.02 | 186655.43 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | -0.0 | 80173.0 | 22.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.78 | 0.12 | 58832.82 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.31 | 0.07 | 190409.94 | 25.66 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.05 | 0.18 | 157923.82 | 16.99 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.03 | 0.08 | 148449.09 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10306.4 | 69.69 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 1.04 | 0.09 | 61360.06 | 11.1 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54552.16 | 16.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
