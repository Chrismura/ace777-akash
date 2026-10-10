# Hulk DIGEST — 2026-10-10T04:36:49Z

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
| WUSDT | IDLE | 1.88 | 5.96 | 4.54 | 0.04 | 2080390.65 | 8.84 | skipped_fast |
| PYTHUSDT | IDLE | 1.57 | 3.64 | 3.06 | -0.03 | 1535824.75 | 2.51 | skipped_fast |
| XRPUSDT | IDLE | 0.61 | 1.17 | 0.37 | 0.01 | 24738423.4 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.22 | 0.42 | 0.13 | -0.0 | 152682804.89 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.25 | 0.13 | 0.0 | 252444539.15 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 1.96 | 1.04 | 0.05 | 1336259.48 | 1.61 | skipped_fast |
| CCUSDT | IDLE | 1.52 | 3.05 | 2.84 | 0.02 | 569106.92 | 7.44 | skipped_fast |
| BIOUSDT | IDLE | 1.85 | 3.61 | 0.58 | 0.03 | 62129.23 | 6.86 | skipped_fast |
| ZBCNUSDT | IDLE | 0.91 | 2.86 | 1.22 | -0.05 | 265180.98 | 16.77 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.25 | 0.91 | 0.02 | 60459.99 | 14.64 | skipped_fast |
| EDELUSDT | IDLE | 0.84 | 3.43 | 2.66 | 0.14 | 211490.29 | 17.51 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.72 | 0.42 | -0.03 | 76652.88 | 12.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.15 | 3.52 | 1.37 | 0.04 | 91085.31 | 15.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.0 | 5.37 | 4.86 | 0.1 | 70595.36 | 25.75 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.75 | 1.26 | 0.0 | 328029.04 | 1.09 | skipped_fast |
| RWAINCUSDT | IDLE | 1.11 | 2.29 | 1.38 | -0.02 | 9699.16 | 86.58 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 2.61 | 0.9 | 0.01 | 112330.64 | 37.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.76 | 1.44 | 0.48 | 0.01 | 42331.82 | 39.2 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.63 | 0.16 | -0.0 | 51429.82 | 15.74 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 1.72 | 0.28 | 0.01 | 18793.86 | 20.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
