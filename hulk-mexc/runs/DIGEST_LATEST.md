# Hulk DIGEST — 2026-08-22T03:54:21Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 11.77 | 1.09 | 0.17 | 8851826.07 | 7.48 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.98 | 0.19 | 166077294.95 | 2.56 | skipped_fast |
| HBARUSDT | IDLE | 2.4 | 6.93 | 0.34 | 0.11 | 1034032.01 | 3.61 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.45 | 0.19 | 701118.27 | 13.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.47 | 5.36 | 1.15 | -0.03 | 460118.37 | 2.97 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.08 | 0.07 | 199359.02 | 5.99 | skipped_fast |
| WUSDT | IDLE | 1.85 | 6.13 | 0.0 | 0.13 | 424851.36 | 7.83 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 5.37 | 1.12 | 0.13 | 537721.76 | 28.0 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80709.84 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.18 | 0.11 | 59512.05 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 7.96 | 2.14 | 0.23 | 157551.96 | 17.1 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 5.3 | 0.21 | 0.13 | 67720.04 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 54.47 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.47 | 0.1 | 178490.7 | 7.41 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.63 | 3.22 | 0.24 | 0.06 | 56281.16 | 16.0 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.46 | 0.07 | 173976.41 | 56.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 17.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
