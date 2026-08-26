# Hulk DIGEST — 2026-08-26T04:09:55Z

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
| PYTHUSDT | IDLE | 2.6 | 5.41 | 1.19 | 0.0 | 2355460.21 | 3.88 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.92 | 76.3 | 36.8 | 0.14 | 59921.27 | 61.9 | skipped_fast |
| XRPUSDT | IDLE | 0.93 | 1.88 | 0.75 | -0.05 | 60903121.38 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.58 | 2.41 | -0.06 | 518767.06 | 9.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 4.71 | 1.97 | -0.01 | 398312.48 | 9.3 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.65 | 21.79 | 1.01 | 0.17 | 8256.66 | 10.13 | skipped_fast |
| WUSDT | IDLE | 1.55 | 3.09 | 0.38 | -0.01 | 291538.77 | 11.55 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 4.97 | 3.03 | -0.01 | 81064.07 | 13.04 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.84 | 0.43 | -0.06 | 607896.64 | 1.28 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 2.81 | 0.95 | -0.01 | 158891.15 | 7.9 | skipped_fast |
| EDELUSDT | IDLE | 0.68 | 9.5 | 8.34 | 0.06 | 158404.67 | 18.35 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.71 | 1.4 | -0.02 | 60494.79 | 13.22 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.04 | 1.73 | -0.02 | 95255.42 | 10.36 | skipped_fast |
| QAITUSDT | IDLE | 0.85 | 2.16 | 1.48 | 0.03 | 12825.21 | 30.02 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 1.83 | 1.72 | -0.05 | 55784.53 | 16.65 | skipped_fast |
| RWAINCUSDT | IDLE | 0.93 | 1.62 | 1.55 | -0.02 | 2337.44 | 131.05 | skipped_fast |
| QNTUSDT | IDLE | 0.55 | 1.05 | 0.34 | -0.03 | 131973.77 | 4.72 | skipped_fast |
| TELUSDT | IDLE | 0.83 | 1.61 | 0.38 | -0.03 | 93566.37 | 43.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
