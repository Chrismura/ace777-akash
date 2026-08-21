# Hulk DIGEST — 2026-08-21T01:29:07Z

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
| XRPUSDT | IDLE | 0.8 | 4.69 | 0.02 | 0.16 | 105038217.96 | 0.78 | skipped_fast |
| PYTHUSDT | IDLE | 1.33 | 2.55 | 0.67 | 0.05 | 1510945.66 | 2.25 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 11.45 | 0.58 | 0.16 | 350354.69 | 15.28 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.46 | 1.81 | -0.01 | 468660.71 | 8.11 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 6.3 | 0.73 | 0.04 | 283384.34 | 22.95 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 5.22 | 2.75 | 0.02 | 92144.5 | 21.69 | skipped_fast |
| WUSDT | IDLE | 1.27 | 2.39 | 1.04 | 0.04 | 255298.25 | 13.3 | skipped_fast |
| RIZEUSDT | IDLE | 1.78 | 9.36 | 5.95 | -0.12 | 43244.96 | 51.01 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.74 | 0.32 | 0.04 | 453296.44 | 1.35 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 2.91 | 1.92 | 0.1 | 232033.19 | 6.42 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 2.92 | 0.56 | 0.03 | 62640.7 | 13.11 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 3.43 | 2.29 | 0.01 | 7972.57 | 38.73 | skipped_fast |
| REDUSDT | IDLE | 0.62 | 3.84 | 0.21 | 0.07 | 184744.38 | 22.47 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 3.22 | 2.82 | -0.03 | 6244.55 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 4.98 | 2.79 | 0.14 | 192137.95 | 37.95 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.9 | 0.25 | 0.01 | 54114.7 | 16.99 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 1.81 | 0.93 | 0.05 | 63955.14 | 16.14 | skipped_fast |
| FLUIDUSDT | IDLE | 0.56 | 1.3 | 0.02 | 0.09 | 1524.34 | 22.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
