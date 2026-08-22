# Hulk DIGEST — 2026-08-22T01:08:56Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 8.23 | 0.24 | 0.14 | 6587999.97 | 1.98 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.4 | 0.86 | 0.16 | 149045049.0 | 4.77 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.58 | 0.09 | 955765.63 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.86 | 0.11 | 542603.55 | 20.83 | skipped_fast |
| CCUSDT | IDLE | 1.73 | 6.94 | 0.19 | 0.16 | 653475.84 | 7.89 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.53 | 0.09 | 392286.2 | 9.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.64 | 0.01 | 536343.29 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.53 | 0.37 | 0.04 | 187140.93 | 3.06 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.28 | -0.03 | 79701.98 | 22.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.08 | 0.11 | 60418.91 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 8.27 | 2.36 | 0.22 | 159849.45 | 11.66 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.78 | 0.07 | 170389.31 | 4.52 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.72 | 0.05 | 181208.8 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 4.1 | 0.01 | 0.11 | 60877.97 | 10.84 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 55142.23 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.09 | 4845.77 | 21.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
