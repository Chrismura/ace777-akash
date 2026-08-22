# Hulk DIGEST — 2026-08-22T01:13:46Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.74 | 9.41 | 0.45 | 0.14 | 6631379.75 | 1.97 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 8.4 | 0.61 | 0.15 | 149404450.47 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.51 | 0.09 | 956664.78 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.84 | 0.1 | 540567.34 | 16.95 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 7.13 | 0.17 | 0.16 | 657585.15 | 8.75 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.65 | 0.6 | 0.09 | 392327.43 | 13.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.37 | 0.01 | 535425.78 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.57 | 0.18 | 0.04 | 186948.27 | 6.11 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.03 | 79630.31 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.16 | 0.11 | 60471.19 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 8.27 | 3.07 | 0.21 | 159662.37 | 3.14 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.82 | 0.07 | 170412.67 | 4.52 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.72 | 0.05 | 181082.46 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.48 | 4.48 | 0.41 | 0.12 | 61021.09 | 17.14 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.66 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 55242.21 | 24.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
