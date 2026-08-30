# Hulk DIGEST — 2026-08-22T05:08:25Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 15.45 | 5.91 | 0.14 | 14237102.02 | 19.05 | skipped_fast |
| XRPUSDT | IDLE | 2.55 | 19.3 | 3.02 | 0.27 | 183777784.72 | 5.46 | skipped_fast |
| HBARUSDT | IDLE | 2.65 | 10.33 | 2.36 | 0.13 | 1132993.24 | 1.18 | skipped_fast |
| CCUSDT | IDLE | 2.18 | 11.56 | 2.51 | 0.19 | 752953.4 | 9.96 | skipped_fast |
| CHIPUSDT | IDLE | 2.91 | 5.36 | 3.06 | -0.01 | 446672.43 | 12.18 | skipped_fast |
| WUSDT | IDLE | 2.18 | 8.22 | 2.04 | 0.14 | 452254.35 | 25.27 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.09 | 9.0 | 1.39 | 0.09 | 203390.72 | 20.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.6 | 4.29 | 2.54 | 0.1 | 538557.07 | 57.95 | skipped_fast |
| QNTUSDT | IDLE | 2.76 | 9.16 | 4.77 | 0.1 | 187010.09 | 7.41 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 7.96 | 6.76 | 0.18 | 157671.49 | 12.23 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 6.62 | 0.63 | 0.14 | 68400.6 | 22.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.36 | 4.48 | 1.57 | 0.02 | 10360.76 | 37.38 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.28 | 1.2 | -0.02 | 81013.46 | 55.46 | skipped_fast |
| RIZEUSDT | IDLE | 1.11 | 4.41 | 4.22 | 0.09 | 58680.24 | 22.29 | skipped_fast |
| TELUSDT | IDLE | 1.98 | 5.52 | 0.89 | 0.1 | 184139.51 | 39.76 | skipped_fast |
| RWAUSDT | IDLE | 1.71 | 3.38 | 0.24 | 0.07 | 56885.41 | 15.96 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 42.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
