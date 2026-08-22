# Hulk DIGEST — 2026-08-22T00:45:10Z

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
| PYTHUSDT | IDLE | 1.99 | 7.38 | 0.36 | 0.13 | 6466026.05 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.34 | 0.15 | 147216227.92 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 2.82 | 6.36 | 1.89 | 0.07 | 940699.45 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.92 | 11.25 | 3.54 | 0.11 | 543892.21 | 38.53 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 7.42 | 1.31 | 0.14 | 640958.96 | 4.46 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.91 | 0.39 | 0.1 | 386061.53 | 11.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.67 | 0.03 | 549289.54 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.5 | 5.62 | 0.37 | 0.03 | 186341.16 | 6.15 | skipped_fast |
| EDELUSDT | IDLE | 2.55 | 5.5 | 0.87 | -0.01 | 79905.19 | 10.95 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 2.5 | 0.14 | 60074.21 | 66.74 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.07 | 184200.72 | 30.9 | skipped_fast |
| QNTUSDT | IDLE | 2.56 | 5.42 | 1.48 | 0.06 | 170517.91 | 4.55 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 7.82 | 0.89 | 0.25 | 158678.55 | 29.38 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.03 | 9754.98 | 53.97 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.27 | 0.1 | 61123.94 | 22.06 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 54819.23 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
