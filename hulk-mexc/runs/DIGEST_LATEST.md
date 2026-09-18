# Hulk DIGEST — 2026-09-18T20:55:11Z

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
| ETHUSDT | IDLE | 1.49 | 3.11 | 0.5 | 0.07 | 600080778.52 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 3.14 | 0.88 | 0.08 | 62749924.08 | 1.43 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.11 | 0.33 | 0.06 | 733718250.15 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.85 | 11.01 | 4.26 | 0.1 | 886332.87 | 8.25 | skipped_fast |
| PYTHUSDT | IDLE | 1.12 | 2.6 | 1.32 | 0.07 | 696435.65 | 1.67 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 2.79 | 0.0 | 0.12 | 672008.32 | 9.01 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 11.26 | 9.64 | 0.2 | 203709.06 | 39.88 | skipped_fast |
| RIZEUSDT | IDLE | 1.38 | 23.08 | 5.92 | -0.09 | 57708.59 | 63.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.86 | 3.53 | 1.33 | 0.04 | 213768.47 | 43.67 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 2.23 | 0.25 | 0.05 | 596842.21 | 1.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 5.8 | 0.33 | 0.19 | 189656.84 | 15.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 3.12 | 0.51 | 0.03 | 7751.93 | 17.23 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 2.3 | 0.65 | 0.09 | 87455.7 | 3.65 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 1.82 | 0.36 | 0.06 | 76621.05 | 13.51 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 9.74 | 0.0 | 0.17 | 2447.56 | 21.82 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 2.84 | 0.64 | 0.12 | 63810.19 | 15.1 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 2.09 | 1.29 | 0.04 | 72390.3 | 4.71 | skipped_fast |
| MNSRYUSDT | IDLE | 1.24 | 2.47 | 0.01 | 0.07 | 43143.77 | 6.54 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 3.02 | 0.96 | 0.07 | 101977.03 | 71.04 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.63 | 1.24 | 0.01 | 58486.42 | 59.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
