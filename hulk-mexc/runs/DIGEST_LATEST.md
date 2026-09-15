# Hulk DIGEST — 2026-09-15T09:44:58Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.27 | 2.36 | 1.24 | 0.01 | 74724052.6 | 2.85 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.41 | 1.04 | -0.02 | 455979209.0 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.35 | 1.02 | -0.01 | 545631261.27 | 0.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 22.32 | 13.42 | 0.02 | 146047.07 | 14.19 | skipped_fast |
| EDELUSDT | IDLE | 1.24 | 16.9 | 9.12 | 0.31 | 448903.73 | 60.19 | skipped_fast |
| PYTHUSDT | IDLE | 2.21 | 3.93 | 3.3 | -0.02 | 293286.93 | 3.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.43 | 4.56 | 2.04 | 0.04 | 223734.64 | 35.01 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 21.94 | 1.25 | -0.03 | 51467.78 | 95.95 | skipped_fast |
| CCUSDT | IDLE | 1.08 | 2.01 | 1.05 | 0.0 | 367170.6 | 5.24 | skipped_fast |
| WUSDT | IDLE | 1.75 | 3.12 | 2.51 | -0.04 | 161616.46 | 14.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.63 | 2.85 | 2.77 | -0.02 | 7381.51 | 5.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 2.7 | 0.74 | 0.01 | 66302.37 | 14.44 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.03 | 1.56 | -0.01 | 91765.41 | 7.92 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.13 | 0.66 | 0.0 | 63531.98 | 12.18 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.76 | 0.19 | 0.01 | 364828.81 | 2.58 | skipped_fast |
| FLUIDUSDT | IDLE | 2.23 | 3.9 | 3.75 | -0.03 | 2076.5 | 22.4 | skipped_fast |
| QNTUSDT | IDLE | 1.77 | 3.12 | 2.84 | -0.01 | 44254.34 | 6.33 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 3.7 | 3.38 | -0.01 | 97539.76 | 38.22 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.37 | -0.01 | 53976.83 | 14.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.9 | 0.57 | 0.0 | 33524.22 | 34.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
