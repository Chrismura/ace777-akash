# Hulk DIGEST — 2026-08-21T21:55:18Z

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
| PYTHUSDT | IDLE | 1.17 | 4.61 | 0.02 | 0.1 | 5678961.39 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.43 | 0.11 | 129938390.14 | 2.84 | skipped_fast |
| HBARUSDT | IDLE | 2.08 | 4.71 | 0.18 | 0.08 | 830623.94 | 3.78 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 5.61 | 3.34 | 0.04 | 526816.63 | 3.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.65 | 0.11 | 492058.02 | 21.86 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 3.89 | 0.21 | 0.11 | 635612.47 | 8.21 | skipped_fast |
| WUSDT | IDLE | 2.11 | 4.19 | 0.25 | 0.06 | 367056.77 | 11.43 | skipped_fast |
| BIOUSDT | IDLE | 2.38 | 5.2 | 1.32 | 0.04 | 186569.24 | 6.21 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.44 | 0.19 | 153800.09 | 12.18 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 10.4 | 0.62 | 0.05 | 56188.92 | 46.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.03 | 10222.59 | 10.66 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 4.12 | 0.55 | -0.03 | 83629.25 | 44.15 | skipped_fast |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.18 | 0.04 | 191919.43 | 36.28 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.13 | 0.11 | 61323.28 | 11.01 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.65 | 0.17 | 0.05 | 62561.58 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.17 | 0.0 | 0.04 | 54132.83 | 32.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 20.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
