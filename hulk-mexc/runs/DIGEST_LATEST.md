# Hulk DIGEST — 2026-08-22T03:12:56Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 10.96 | 0.89 | 0.17 | 7609540.75 | 3.76 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.27 | 11.43 | 0.48 | 0.19 | 160790223.17 | 5.16 | skipped_fast |
| HBARUSDT | IDLE | 2.14 | 5.29 | 0.05 | 0.1 | 997258.9 | 2.43 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 8.96 | 1.63 | 0.17 | 679128.54 | 13.59 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.2 | 0.06 | 195642.74 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.95 | 4.28 | 0.59 | -0.01 | 448852.26 | 2.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 5.16 | 2.65 | 0.12 | 541130.58 | 41.53 | skipped_fast |
| WUSDT | IDLE | 1.79 | 5.61 | 0.46 | 0.12 | 418152.57 | 11.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.36 | 0.1 | 59514.17 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.05 | 0.2 | 158074.45 | 10.32 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 3.83 | 2.82 | -0.03 | 80045.97 | 33.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 32.45 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 4.4 | 0.24 | 0.12 | 67671.64 | 11.61 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3813.17 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.27 | 0.08 | 174159.23 | 1.49 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 2.19 | 0.46 | 0.07 | 173297.1 | 56.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 14.0 | skipped_fast |
| RWAUSDT | IDLE | 1.2 | 2.39 | 0.0 | 0.05 | 56179.66 | 48.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
