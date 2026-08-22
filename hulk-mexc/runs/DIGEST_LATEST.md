# Hulk DIGEST — 2026-08-22T04:21:30Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 13.61 | 0.71 | 0.2 | 10657024.05 | 16.48 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 12.22 | 0.69 | 0.21 | 168787471.4 | 2.52 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 11.56 | 0.7 | 0.21 | 728078.88 | 7.34 | skipped_fast |
| HBARUSDT | IDLE | 2.27 | 7.14 | 0.62 | 0.12 | 1019084.62 | 2.39 | skipped_fast |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.29 | 0.01 | 441141.46 | 2.98 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.08 | 0.07 | 199959.52 | 6.0 | skipped_fast |
| WUSDT | IDLE | 1.95 | 7.18 | 0.23 | 0.14 | 434391.88 | 13.55 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.34 | 0.11 | 535617.94 | 13.31 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.47 | -0.04 | 80125.43 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.96 | 0.1 | 59161.89 | 30.84 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.86 | 0.2 | 159824.9 | 10.39 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.53 | 0.13 | 67696.42 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | 0.01 | 9427.75 | 65.18 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.55 | 0.09 | 178594.43 | 8.9 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.4 | 0.06 | 56299.81 | 16.05 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.97 | 0.25 | 0.08 | 174927.84 | 71.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 19.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
