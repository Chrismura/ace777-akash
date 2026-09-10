# Hulk DIGEST — 2026-09-10T08:18:18Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.6 | 209.6 | 59.43 | -0.56 | 78114.06 | 126.72 | skipped_fast |
| XRPUSDT | IDLE | 0.69 | 1.25 | 0.93 | -0.04 | 41541909.71 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.82 | 0.53 | -0.02 | 350729019.23 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.79 | 0.57 | -0.02 | 524693290.19 | 0.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.11 | 2.82 | 2.59 | -0.06 | 1029878.9 | 1.93 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.66 | 1.04 | -0.04 | 641275.04 | 5.76 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 4.9 | 0.29 | 0.04 | 178393.45 | 29.98 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 5.35 | 2.5 | 0.06 | 246934.06 | 26.44 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.97 | 2.48 | -0.06 | 224853.34 | 8.28 | skipped_fast |
| REDUSDT | IDLE | 2.08 | 4.29 | 3.93 | -0.08 | 65246.92 | 18.76 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 2.14 | 1.59 | -0.07 | 102651.46 | 3.95 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.44 | 1.29 | -0.04 | 385521.56 | 1.31 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.92 | 0.43 | -0.02 | 56999.22 | 11.57 | skipped_fast |
| CHIPUSDT | IDLE | 0.46 | 2.71 | 1.51 | -0.18 | 115364.44 | 12.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.3 | 2.39 | 1.39 | 0.0 | 5859.36 | 45.02 | skipped_fast |
| QNTUSDT | IDLE | 1.27 | 2.26 | 1.81 | -0.04 | 39845.47 | 7.51 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.91 | 1.15 | -0.06 | 1432.84 | 21.29 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.34 | 0.55 | 0.01 | 84292.61 | 44.44 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.68 | 0.3 | -0.04 | 54339.61 | 14.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.52 | 0.94 | 0.65 | -0.02 | 25516.78 | 44.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
