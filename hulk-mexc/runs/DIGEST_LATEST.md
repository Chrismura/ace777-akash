# Hulk DIGEST — 2026-08-22T01:19:30Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.78 | 9.96 | 0.27 | 0.15 | 6657654.39 | 13.68 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.4 | 0.74 | 0.15 | 150029256.14 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.93 | 0.08 | 955141.1 | 2.5 | skipped_fast |
| ZBCNUSDT | IDLE | 2.61 | 10.08 | 3.2 | 0.1 | 546764.81 | 25.27 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 7.18 | 0.38 | 0.16 | 659983.0 | 9.64 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.65 | 0.94 | 0.09 | 392482.31 | 14.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.52 | -0.01 | 522609.14 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.57 | 0.79 | 0.04 | 186466.73 | 3.07 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79560.32 | 11.08 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.03 | 0.11 | 60534.15 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.44 | 0.18 | 159670.52 | 13.51 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.87 | 0.07 | 170461.51 | 7.53 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.77 | 0.05 | 181118.28 | 41.22 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9620.22 | 16.16 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 4.48 | 0.11 | 0.11 | 60832.71 | 90.65 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.71 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 55148.5 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
