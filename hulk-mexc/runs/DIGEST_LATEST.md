# Hulk DIGEST — 2026-08-22T02:52:35Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.62 | 11.02 | 0.47 | 0.17 | 7302703.42 | 3.79 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 12.56 | 0.08 | 0.19 | 158072538.19 | 3.24 | skipped_fast |
| HBARUSDT | IDLE | 2.54 | 6.38 | 0.24 | 0.09 | 988658.94 | 2.45 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 9.41 | 0.07 | 0.18 | 659536.73 | 8.44 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.76 | 0.1 | 540529.31 | 36.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.51 | 5.8 | 0.03 | -0.02 | 452362.39 | 2.98 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.2 | 8.18 | 1.93 | 0.09 | 194139.11 | 2.99 | skipped_fast |
| WUSDT | IDLE | 2.03 | 6.13 | 0.14 | 0.11 | 415077.76 | 13.9 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 5.02 | 2.61 | -0.03 | 79884.04 | 22.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.42 | 0.1 | 61363.7 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.95 | 0.19 | 157797.67 | 19.2 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.22 | 0.09 | 172525.35 | 5.95 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9385.21 | 43.36 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.24 | 0.12 | 62452.29 | 14.36 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.13 | 0.06 | 174040.61 | 41.37 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.08 | 0.0 | 0.04 | 55884.63 | 24.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
