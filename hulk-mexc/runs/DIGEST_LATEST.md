# Hulk DIGEST — 2026-08-17T11:11:11Z

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
| XRPUSDT | IDLE | 0.58 | 1.07 | 0.62 | 0.0 | 10510537.62 | 1.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.71 | 12.21 | 7.77 | -0.01 | 355859.15 | 3.31 | skipped_fast |
| EDELUSDT | IDLE | 2.33 | 4.46 | 1.38 | 0.06 | 58136.29 | 25.45 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.75 | 29.21 | 1.93 | 0.36 | 70254.48 | 311.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 2.49 | 1.57 | 0.01 | 159029.31 | 21.53 | skipped_fast |
| REDUSDT | IDLE | 1.7 | 3.07 | 2.22 | -0.05 | 57233.21 | 26.48 | skipped_fast |
| CCUSDT | IDLE | 0.74 | 1.34 | 0.95 | -0.0 | 257460.57 | 11.57 | skipped_fast |
| PYTHUSDT | IDLE | 0.91 | 1.64 | 1.26 | -0.01 | 158109.11 | 5.12 | skipped_fast |
| WUSDT | IDLE | 0.88 | 1.58 | 1.26 | -0.01 | 187498.27 | 16.7 | skipped_fast |
| RWAINCUSDT | IDLE | 1.57 | 2.79 | 2.37 | -0.04 | 2259.82 | 17.25 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 2.39 | 0.99 | -0.01 | 53230.87 | 23.58 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.92 | 0.84 | -0.0 | 69032.84 | 4.04 | skipped_fast |
| QAITUSDT | IDLE | 1.42 | 2.63 | 1.39 | -0.01 | 1714.92 | 63.76 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 2.17 | 0.06 | 0.02 | 114814.27 | 1.51 | skipped_fast |
| TELUSDT | IDLE | 0.88 | 1.66 | 0.68 | 0.0 | 87440.34 | 47.96 | skipped_fast |
| FLUIDUSDT | IDLE | 0.86 | 1.5 | 1.48 | -0.01 | 772.36 | 22.08 | skipped_fast |
| QNTUSDT | IDLE | 0.54 | 0.99 | 0.62 | -0.03 | 32264.69 | 1.79 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.17 | 0.01 | 49184.17 | 26.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
