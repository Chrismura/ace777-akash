# Hulk DIGEST — 2026-08-22T04:04:23Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.77 | 11.77 | 0.43 | 0.18 | 9620844.38 | 11.15 | skipped_fast |
| XRPUSDT | IDLE | 2.18 | 12.22 | 2.64 | 0.18 | 166495641.92 | 4.5 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.02 | 10.49 | 0.16 | 0.21 | 711719.74 | 13.88 | skipped_fast |
| HBARUSDT | IDLE | 2.13 | 6.03 | 0.91 | 0.1 | 1013022.79 | 2.42 | skipped_fast |
| CHIPUSDT | IDLE | 2.89 | 5.36 | 2.79 | -0.04 | 458973.74 | 6.05 | skipped_fast |
| WUSDT | IDLE | 1.99 | 7.18 | 1.21 | 0.13 | 428435.45 | 12.7 | skipped_fast |
| BIOUSDT | IDLE | 3.03 | 7.36 | 2.64 | 0.07 | 199514.62 | 15.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 4.29 | 1.94 | 0.13 | 537206.05 | 20.57 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80602.41 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.25 | 0.09 | 59210.34 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.63 | 0.21 | 157783.37 | 10.26 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.55 | 0.13 | 67559.21 | 8.86 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.8 | 0.75 | 0.09 | 178557.03 | 7.44 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56328.61 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.51 | 0.07 | 174316.78 | 20.45 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
