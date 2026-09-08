# Hulk DIGEST — 2026-09-08T01:38:00Z

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
| XRPUSDT | IDLE | 0.86 | 1.68 | 0.24 | -0.0 | 35501915.6 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.17 | 0.2 | -0.0 | 317972440.41 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.85 | 0.17 | -0.01 | 421184745.41 | 0.1 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 3.25 | 0.02 | -0.03 | 452211.97 | 7.47 | skipped_fast |
| PYTHUSDT | IDLE | 1.36 | 2.5 | 1.47 | -0.04 | 451298.91 | 1.85 | skipped_fast |
| EDELUSDT | IDLE | 2.47 | 9.19 | 4.88 | -0.06 | 110440.78 | 40.24 | skipped_fast |
| KITEUSDT | IDLE | 2.18 | 4.48 | 0.57 | -0.03 | 62521.57 | 8.98 | skipped_fast |
| WUSDT | IDLE | 1.15 | 2.23 | 0.45 | -0.0 | 234353.77 | 13.53 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 3.04 | 1.79 | -0.04 | 229575.79 | 27.51 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 3.47 | 2.83 | -0.08 | 206661.64 | 13.07 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.83 | 0.37 | 0.02 | 515493.77 | 1.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 5.89 | 0.0 | -0.0 | 53163.88 | 64.79 | skipped_fast |
| BIOUSDT | IDLE | 1.32 | 2.56 | 0.58 | 0.0 | 64042.23 | 7.27 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 2.09 | 1.72 | 0.03 | 58134.19 | 9.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 3.65 | 2.29 | -0.1 | 4298.8 | 88.38 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.95 | 0.64 | -0.02 | 80678.75 | 46.73 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.52 | 0.45 | 0.0 | 60444.68 | 13.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.53 | -0.01 | 37819.14 | 2.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.41 | 0.0 | 0.0 | 1666.63 | 23.02 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.73 | 0.22 | -0.01 | 52726.44 | 14.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
