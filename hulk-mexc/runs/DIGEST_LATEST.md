# Hulk DIGEST — 2026-08-22T04:09:22Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 12.59 | 0.17 | 0.2 | 10124018.53 | 14.72 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 12.22 | 1.63 | 0.19 | 166797029.36 | 2.54 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 11.33 | 0.15 | 0.22 | 719243.93 | 12.97 | skipped_fast |
| HBARUSDT | IDLE | 2.09 | 6.03 | 0.29 | 0.11 | 1008527.59 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.94 | 5.36 | 3.5 | -0.02 | 458772.35 | 3.04 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.49 | 0.07 | 199831.14 | 3.01 | skipped_fast |
| WUSDT | IDLE | 1.98 | 7.18 | 0.87 | 0.14 | 428488.42 | 13.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.62 | 0.13 | 536553.03 | 17.65 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.37 | -0.05 | 80385.32 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.99 | 0.1 | 59136.98 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.96 | 0.2 | 157873.76 | 10.29 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.45 | 0.13 | 67615.25 | 13.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.6 | 2.32 | 0.02 | 9399.91 | 27.21 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 3.8 | 0.8 | 0.09 | 178541.79 | 4.46 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56345.03 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.4 | 0.2 | 0.07 | 174261.28 | 51.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 20.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
