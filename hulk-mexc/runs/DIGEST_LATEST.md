# Hulk DIGEST — 2026-08-22T03:55:03Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 11.77 | 1.04 | 0.17 | 8890944.5 | 1.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.97 | 0.19 | 166081984.1 | 3.19 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 6.93 | 0.5 | 0.11 | 1034152.96 | 4.81 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.43 | 0.19 | 701070.06 | 12.44 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 5.36 | 1.26 | -0.03 | 459586.63 | 5.96 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.11 | 0.07 | 199263.65 | 5.99 | skipped_fast |
| WUSDT | IDLE | 1.86 | 6.2 | 0.06 | 0.13 | 424848.06 | 7.83 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 5.37 | 1.15 | 0.13 | 537719.0 | 24.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.39 | 0.11 | 59280.39 | 22.13 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80658.63 | 33.73 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 7.96 | 2.14 | 0.23 | 157604.1 | 7.76 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 5.3 | 0.3 | 0.13 | 67657.91 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 54.47 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.53 | 0.09 | 178499.4 | 5.94 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.61 | 3.22 | 0.0 | 0.06 | 56282.38 | 8.01 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.45 | 0.25 | 0.07 | 173972.41 | 40.84 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 19.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
