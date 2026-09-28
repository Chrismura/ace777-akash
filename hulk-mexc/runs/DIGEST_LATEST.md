# Hulk DIGEST — 2026-09-28T17:28:02Z

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
| WUSDT | IDLE | 1.79 | 8.49 | 5.73 | -0.12 | 2755692.64 | 7.31 | skipped_fast |
| XRPUSDT | IDLE | 2.13 | 3.98 | 1.85 | -0.01 | 66565873.27 | 1.99 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 11.23 | 0.23 | 0.37 | 9796776.4 | 9.37 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 16.43 | 1.26 | 0.34 | 21887201.99 | 9.58 | skipped_fast |
| ETHUSDT | IDLE | 1.33 | 2.55 | 0.68 | 0.01 | 390986544.08 | 0.15 | skipped_fast |
| PYTHUSDT | IDLE | 2.35 | 5.98 | 4.2 | -0.08 | 1377914.17 | 3.79 | skipped_fast |
| BTCUSDT | IDLE | 1.11 | 2.14 | 0.52 | -0.01 | 814684734.03 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 5.56 | 1.99 | -0.03 | 1372906.7 | 8.41 | skipped_fast |
| CHIPUSDT | IDLE | 2.75 | 6.46 | 4.31 | -0.07 | 69411.75 | 13.65 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 6.35 | 2.15 | -0.09 | 101864.16 | 9.4 | skipped_fast |
| REDUSDT | IDLE | 1.95 | 4.49 | 2.17 | -0.05 | 61709.89 | 13.02 | skipped_fast |
| BIOUSDT | IDLE | 1.61 | 4.83 | 2.12 | -0.07 | 112737.92 | 6.78 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.59 | 8.73 | 0.0 | 0.04 | 150909.17 | 93.9 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 2.53 | 1.04 | -0.04 | 236809.46 | 28.27 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 6.44 | 3.91 | 0.08 | 191106.44 | 20.51 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 9.21 | 5.66 | 0.12 | 15978.33 | 78.69 | skipped_fast |
| RIZEUSDT | IDLE | 0.44 | 2.69 | 0.24 | -0.12 | 66943.48 | 53.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 3.66 | 0.0 | -0.04 | 3933.8 | 21.82 | skipped_fast |
| RWAUSDT | IDLE | 0.85 | 1.67 | 0.21 | -0.01 | 60797.11 | 35.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 0.96 | 0.46 | -0.02 | 34339.16 | 47.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
