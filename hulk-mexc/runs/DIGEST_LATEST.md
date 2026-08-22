# Hulk DIGEST — 2026-08-22T04:29:50Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 13.61 | 0.91 | 0.19 | 11084657.0 | 7.35 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 12.41 | 0.55 | 0.23 | 170118868.54 | 1.89 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.63 | 0.2 | 732233.44 | 6.58 | skipped_fast |
| HBARUSDT | IDLE | 2.27 | 7.14 | 0.77 | 0.12 | 1033515.2 | 1.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.75 | 5.36 | 0.97 | 0.02 | 441044.1 | 5.94 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.17 | 0.07 | 200694.78 | 2.99 | skipped_fast |
| WUSDT | IDLE | 1.96 | 7.18 | 0.41 | 0.14 | 434158.56 | 11.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 0.96 | 0.14 | 535302.88 | 23.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.89 | 0.09 | 59201.84 | 44.52 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.47 | -0.04 | 80073.19 | 56.21 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.74 | 0.21 | 158419.52 | 17.56 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.62 | 0.13 | 67848.31 | 12.43 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | -0.0 | 9290.79 | 81.41 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.32 | 0.1 | 179066.86 | 1.48 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 3.12 | 0.35 | 0.08 | 176606.92 | 40.57 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56285.37 | 24.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
