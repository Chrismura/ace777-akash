# Hulk DIGEST — 2026-08-22T11:31:48Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.77 | -0.0 | 51633517.67 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.76 | 0.07 | 217481842.61 | 3.37 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 10.24 | 7.42 | 0.11 | 807049.94 | 7.77 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.67 | 0.0 | 1255738.31 | 6.48 | skipped_fast |
| WUSDT | IDLE | 1.58 | 6.27 | 4.36 | 0.01 | 589042.09 | 14.92 | skipped_fast |
| ZBCNUSDT | IDLE | 2.34 | 5.93 | 5.19 | -0.04 | 395820.47 | 16.14 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.11 | -0.1 | 637088.62 | 6.75 | skipped_fast |
| EDELUSDT | IDLE | 2.82 | 4.93 | 4.69 | -0.05 | 78957.36 | 34.19 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.64 | 3.05 | -0.06 | 237406.79 | 3.24 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.81 | -0.04 | 167938.08 | 21.47 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 4.3 | 0.71 | 0.03 | 73642.43 | 11.72 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.76 | 0.03 | 155196.6 | 11.74 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | 0.0 | 11178.17 | 38.12 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 3.47 | 2.14 | -0.01 | 188594.05 | 6.26 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.99 | -0.03 | 48736.52 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 56.68 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.8 | 1.69 | 0.01 | 57656.13 | 16.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
