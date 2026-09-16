# Hulk DIGEST — 2026-09-16T12:13:07Z

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
| ETHUSDT | IDLE | 1.04 | 2.0 | 0.56 | -0.03 | 491862570.39 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.24 | 0.19 | -0.01 | 595678268.02 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.52 | 1.91 | 0.77 | -0.08 | 94738699.97 | 2.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.49 | 2.72 | 1.79 | -0.02 | 676683.79 | 1.9 | skipped_fast |
| CHIPUSDT | IDLE | 2.4 | 5.63 | 2.26 | -0.08 | 104433.55 | 13.29 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 8.49 | 1.06 | 0.52 | 439746.67 | 28.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 20.93 | 2.83 | 0.43 | 49833.07 | 49.74 | skipped_fast |
| CCUSDT | IDLE | 0.37 | 0.73 | 0.03 | -0.04 | 389531.6 | 7.66 | skipped_fast |
| REDUSDT | IDLE | 1.96 | 3.6 | 2.15 | -0.04 | 68072.75 | 54.3 | skipped_fast |
| WUSDT | IDLE | 0.91 | 2.06 | 1.2 | -0.07 | 217644.63 | 14.58 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 3.04 | 0.27 | -0.06 | 202321.19 | 28.32 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 2.0 | 0.44 | -0.01 | 80975.46 | 8.04 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.22 | 0.92 | -0.04 | 433953.39 | 1.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.2 | 2.1 | 2.06 | -0.04 | 13646.94 | 11.66 | skipped_fast |
| KITEUSDT | IDLE | 1.03 | 1.81 | 1.61 | -0.07 | 60643.84 | 15.08 | skipped_fast |
| TELUSDT | IDLE | 1.59 | 3.25 | 2.55 | -0.07 | 114494.39 | 27.55 | skipped_fast |
| QNTUSDT | IDLE | 0.92 | 1.67 | 1.08 | -0.05 | 45149.56 | 8.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.62 | 1.59 | -0.06 | 1910.63 | 21.24 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.61 | -0.01 | 52377.01 | 22.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.44 | 0.06 | -0.02 | 33596.78 | 5.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
