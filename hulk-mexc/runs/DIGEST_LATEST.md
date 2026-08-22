# Hulk DIGEST — 2026-08-22T04:01:06Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.78 | 11.77 | 0.98 | 0.18 | 9319385.34 | 11.21 | skipped_fast |
| XRPUSDT | IDLE | 2.16 | 12.22 | 2.15 | 0.2 | 166202606.75 | 1.28 | skipped_fast |
| HBARUSDT | IDLE | 2.12 | 6.03 | 0.78 | 0.1 | 1013485.76 | 1.2 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 10.1 | 0.0 | 0.21 | 708754.85 | 13.12 | skipped_fast |
| CHIPUSDT | IDLE | 2.83 | 5.36 | 2.06 | -0.03 | 459013.16 | 6.0 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.32 | 0.07 | 199224.43 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.94 | 7.18 | 0.05 | 0.14 | 426877.71 | 22.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.71 | 0.13 | 537585.2 | 26.24 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80652.46 | 11.24 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.44 | 0.11 | 59266.11 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.85 | 0.22 | 157718.23 | 10.94 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.29 | 0.13 | 67535.89 | 10.61 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.56 | 0.09 | 178523.07 | 8.9 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56360.45 | 24.05 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.4 | 0.41 | 0.07 | 174229.39 | 30.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 4710.05 | 21.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
