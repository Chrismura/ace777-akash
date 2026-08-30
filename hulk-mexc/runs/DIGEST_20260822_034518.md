# Hulk DIGEST — 2026-08-22T03:45:18Z

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
| PYTHUSDT | IDLE | 2.5 | 11.77 | 2.02 | 0.16 | 8317823.69 | 13.22 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 14.16 | 1.91 | 0.19 | 165457436.11 | 4.47 | skipped_fast |
| HBARUSDT | IDLE | 2.43 | 6.93 | 1.01 | 0.11 | 1033144.81 | 2.42 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 9.57 | 0.22 | 0.19 | 693999.25 | 12.5 | skipped_fast |
| CHIPUSDT | IDLE | 2.51 | 5.36 | 1.74 | -0.03 | 453971.28 | 3.0 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.07 | 199123.25 | 3.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 5.16 | 2.8 | 0.12 | 537095.14 | 34.83 | skipped_fast |
| WUSDT | IDLE | 1.82 | 5.83 | 0.52 | 0.12 | 424152.32 | 7.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.15 | 0.11 | 59481.25 | 45.81 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 3.95 | 2.06 | -0.02 | 80381.91 | 33.28 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.86 | 0.22 | 157978.64 | 11.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 38.1 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 4.86 | 0.03 | 0.13 | 67705.34 | 13.31 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3755.43 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.43 | 0.1 | 174989.4 | 14.84 | skipped_fast |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.08 | 0.06 | 56151.88 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.56 | 0.07 | 173704.6 | 46.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
