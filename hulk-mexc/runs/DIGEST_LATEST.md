# Hulk DIGEST — 2026-08-22T03:59:17Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 11.77 | 1.28 | 0.17 | 9220038.38 | 3.75 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.87 | 0.19 | 166190230.94 | 2.55 | skipped_fast |
| HBARUSDT | IDLE | 2.42 | 6.93 | 0.75 | 0.1 | 1023024.16 | 1.21 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.36 | 0.2 | 701862.53 | 8.3 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 5.36 | 1.53 | -0.02 | 458786.72 | 2.99 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.32 | 0.07 | 199180.42 | 6.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 5.37 | 1.46 | 0.13 | 537725.36 | 20.0 | skipped_fast |
| WUSDT | IDLE | 1.88 | 6.27 | 0.32 | 0.13 | 425360.29 | 10.79 | skipped_fast |
| RIZEUSDT | IDLE | 1.83 | 7.71 | 4.62 | 0.1 | 59307.93 | 23.84 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80627.49 | 22.47 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.77 | 0.22 | 157659.41 | 17.17 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.28 | 0.13 | 67491.23 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 54.47 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.53 | 0.09 | 178544.22 | 11.87 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.62 | 3.22 | 0.16 | 0.06 | 56360.36 | 8.01 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.36 | 0.07 | 174202.48 | 30.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 17.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
