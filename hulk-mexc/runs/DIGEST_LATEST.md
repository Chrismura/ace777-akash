# Hulk DIGEST — 2026-10-29T00:45:51Z

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
| ETHUSDT | IDLE | 1.01 | 1.8 | 1.43 | 0.0 | 204474652.23 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.94 | 1.65 | 1.55 | -0.0 | 22392967.42 | 2.27 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 0.98 | 0.74 | 0.01 | 318103623.44 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 4.11 | 0.66 | 0.01 | 437736.21 | 4.04 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.46 | 1.89 | -0.0 | 404191.07 | 18.01 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.92 | 2.0 | 0.01 | 433990.62 | 11.98 | skipped_fast |
| RIZEUSDT | IDLE | 3.34 | 6.07 | 4.77 | -0.03 | 39266.53 | 66.43 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 2.94 | 2.17 | -0.01 | 547909.14 | 7.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 2.64 | 1.47 | 0.0 | 290647.19 | 42.79 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 2.86 | 1.61 | -0.0 | 424767.97 | 2.51 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 2.68 | 1.97 | -0.03 | 171604.2 | 28.24 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.51 | 2.15 | 0.01 | 88412.34 | 8.77 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 3.23 | 1.47 | -0.09 | 234386.54 | 14.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.44 | 5.72 | 2.26 | -0.04 | 35759.44 | 28.05 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.55 | 1.52 | -0.01 | 55737.27 | 16.47 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.11 | 2.03 | -0.02 | 60877.64 | 9.53 | skipped_fast |
| IOTAUSDT | IDLE | 2.31 | 4.04 | 3.88 | -0.02 | 78483.77 | 24.24 | skipped_fast |
| LAUSDT | IDLE | 1.63 | 3.02 | 1.63 | -0.02 | 54216.23 | 18.82 | skipped_fast |
| FLUIDUSDT | IDLE | 1.36 | 2.4 | 2.09 | -0.01 | 4372.55 | 21.43 | skipped_fast |
| WAXLUSDT | IDLE | 1.33 | 2.35 | 2.11 | -0.01 | 53511.93 | 45.16 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.37 | 0.4 | 0.01 | 54511.7 | 15.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.51 | 0.36 | 0.0 | 36452.39 | 40.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
