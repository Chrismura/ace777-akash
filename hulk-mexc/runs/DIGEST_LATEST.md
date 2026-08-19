# Hulk DIGEST — 2026-08-19T14:14:02Z

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
| XRPUSDT | IDLE | 1.06 | 2.05 | 0.49 | 0.02 | 12479525.59 | 0.98 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.1 | 11.36 | 1.87 | 0.04 | 158805.79 | 10.8 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 12.24 | 5.21 | 0.05 | 20543.25 | 28.34 | skipped_fast |
| BIOUSDT | IDLE | 3.23 | 7.08 | 1.05 | 0.08 | 76499.34 | 22.94 | skipped_fast |
| QAITUSDT | IDLE | 3.29 | 6.35 | 3.27 | 0.03 | 10261.36 | 66.45 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.26 | 0.8 | 0.02 | 177941.09 | 5.18 | skipped_fast |
| RIZEUSDT | IDLE | 1.95 | 5.21 | 4.46 | -0.09 | 34262.12 | 53.01 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.67 | 0.94 | -0.01 | 221759.35 | 7.75 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 3.25 | 0.66 | 0.02 | 59852.68 | 26.39 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 2.88 | 1.53 | -0.09 | 130483.2 | 9.09 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.89 | 0.22 | 0.01 | 56403.94 | 14.05 | skipped_fast |
| ZBCNUSDT | IDLE | 0.83 | 1.63 | 0.19 | 0.02 | 164562.46 | 15.61 | skipped_fast |
| WUSDT | IDLE | 0.76 | 1.48 | 0.23 | 0.01 | 103368.31 | 15.94 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 3.46 | 2.46 | 0.01 | 84896.17 | 56.02 | skipped_fast |
| HBARUSDT | IDLE | 0.45 | 0.89 | 0.0 | 0.03 | 151537.83 | 1.47 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.28 | 0.7 | 0.02 | 37377.54 | 8.83 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.06 | 0.61 | -0.01 | 53184.28 | 8.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.49 | 0.99 | 0.0 | -0.01 | 1234.14 | 21.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
