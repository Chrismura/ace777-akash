# Hulk DIGEST — 2026-08-22T03:48:32Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.61 | 0.17 | 8524328.0 | 16.92 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.36 | 0.2 | 165555910.87 | 2.54 | skipped_fast |
| HBARUSDT | IDLE | 2.43 | 6.93 | 0.89 | 0.1 | 1033494.51 | 2.42 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 10.39 | 0.02 | 0.2 | 696910.09 | 10.73 | skipped_fast |
| CHIPUSDT | IDLE | 2.49 | 5.36 | 1.47 | -0.02 | 454103.22 | 5.98 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.96 | 0.08 | 199224.82 | 2.99 | skipped_fast |
| WUSDT | IDLE | 1.81 | 5.83 | 0.16 | 0.12 | 424161.83 | 13.76 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 5.37 | 0.51 | 0.15 | 537529.03 | 57.88 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 3.95 | 2.93 | -0.03 | 80426.89 | 33.58 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.02 | 0.12 | 59499.01 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 3.09 | 0.22 | 157971.3 | 10.21 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 4.86 | 0.2 | 0.12 | 67671.25 | 9.78 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 43.55 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.4 | 0.09 | 174992.9 | 2.96 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.0 | 0.06 | 56290.33 | 8.01 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.61 | 0.07 | 173801.28 | 46.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
