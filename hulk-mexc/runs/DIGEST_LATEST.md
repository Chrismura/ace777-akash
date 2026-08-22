# Hulk DIGEST — 2026-08-22T01:37:06Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.93 | 0.15 | 6776511.66 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.26 | 9.29 | 0.1 | 0.15 | 150995636.0 | 8.05 | skipped_fast |
| HBARUSDT | IDLE | 2.96 | 6.36 | 0.09 | 0.09 | 955498.15 | 6.2 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.75 | 0.09 | 551465.17 | 3.39 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.17 | 0.17 | 662332.5 | 9.59 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.65 | 0.59 | 0.09 | 391355.32 | 9.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.01 | 513640.7 | 6.13 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.57 | 1.04 | 0.04 | 186411.69 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79516.21 | 11.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.1 | 0.11 | 60789.87 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 5.38 | 0.17 | 158702.14 | 9.63 | skipped_fast |
| KITEUSDT | IDLE | 1.57 | 5.07 | 0.0 | 0.13 | 61108.83 | 9.84 | skipped_fast |
| QNTUSDT | IDLE | 2.4 | 5.18 | 0.72 | 0.07 | 170056.92 | 9.03 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.92 | 0.05 | 181983.74 | 51.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.64 | 3.27 | 0.0 | 0.06 | 9647.88 | 42.67 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 19.02 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54837.94 | 16.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
