# Hulk DIGEST — 2026-09-14T06:42:20Z

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
| XRPUSDT | IDLE | 1.9 | 3.74 | 0.41 | 0.01 | 26740617.86 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 1.09 | 2.14 | 0.29 | -0.0 | 326307348.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.58 | 0.28 | 0.0 | 389029168.32 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 49.46 | 13.64 | 0.34 | 81614.23 | 76.46 | skipped_fast |
| REDUSDT | IDLE | 3.64 | 8.4 | 4.66 | 0.01 | 114159.92 | 16.33 | skipped_fast |
| PYTHUSDT | IDLE | 1.85 | 4.2 | 1.61 | 0.05 | 520285.26 | 5.21 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 9.48 | 1.27 | 0.13 | 229731.07 | 14.26 | skipped_fast |
| WUSDT | IDLE | 2.39 | 4.7 | 0.48 | 0.02 | 220942.11 | 6.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.1 | 7.62 | 3.54 | -0.1 | 103801.24 | 16.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.86 | 3.47 | 1.65 | -0.01 | 204151.57 | 21.41 | skipped_fast |
| CCUSDT | IDLE | 1.07 | 2.0 | 0.92 | -0.02 | 271823.82 | 6.23 | skipped_fast |
| KITEUSDT | IDLE | 1.74 | 3.2 | 1.87 | -0.02 | 61777.25 | 6.51 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 3.08 | 0.62 | -0.0 | 67428.97 | 3.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.07 | 0.71 | 0.0 | 9612.57 | 5.51 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 2.18 | 0.51 | 0.01 | 272002.79 | 1.31 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.64 | 0.31 | -0.0 | 36137.36 | 4.69 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.18 | 1.38 | -0.02 | 84901.81 | 31.62 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.75 | 0.85 | -0.0 | 813.34 | 21.68 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.74 | 0.3 | 0.0 | 52850.41 | 22.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.08 | 0.15 | 0.13 | -0.0 | 29883.82 | 4.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
