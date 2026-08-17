# Hulk DIGEST — 2026-08-17T21:14:33Z

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
| XRPUSDT | IDLE | 0.41 | 0.75 | 0.45 | 0.0 | 12984144.82 | 1.99 | skipped_fast |
| CHIPUSDT | IDLE | 0.96 | 4.24 | 3.14 | -0.02 | 336655.54 | 3.53 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 11.55 | 9.53 | 0.08 | 85769.58 | 17.87 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 2.39 | 1.61 | -0.05 | 249623.99 | 6.61 | skipped_fast |
| EDELUSDT | IDLE | 2.42 | 4.47 | 2.52 | 0.01 | 66325.26 | 51.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.12 | 1.5 | 0.01 | 200894.42 | 15.19 | skipped_fast |
| REDUSDT | IDLE | 1.84 | 3.54 | 0.94 | -0.01 | 58782.35 | 26.53 | skipped_fast |
| QAITUSDT | IDLE | 2.21 | 4.15 | 1.84 | -0.01 | 1026.03 | 46.08 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.49 | 1.95 | 0.02 | 81004.68 | 4.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 1.92 | 0.76 | 0.01 | 157838.02 | 2.57 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 5.93 | 2.03 | -0.03 | 137238.51 | 49.98 | skipped_fast |
| WUSDT | IDLE | 0.98 | 1.71 | 1.61 | -0.02 | 141488.65 | 16.94 | skipped_fast |
| FLUIDUSDT | IDLE | 2.31 | 4.04 | 3.89 | -0.04 | 762.34 | 21.69 | skipped_fast |
| KITEUSDT | IDLE | 0.53 | 1.03 | 0.25 | -0.01 | 60502.74 | 16.16 | skipped_fast |
| HBARUSDT | IDLE | 0.54 | 0.97 | 0.78 | 0.01 | 120739.36 | 1.52 | skipped_fast |
| QNTUSDT | IDLE | 0.68 | 1.27 | 0.61 | 0.01 | 36823.43 | 3.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 1125.68 | 63.97 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.61 | 0.52 | 0.01 | 49494.08 | 8.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
