# Hulk DIGEST — 2026-09-20T10:01:43Z

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
| XRPUSDT | IDLE | 0.62 | 1.18 | 0.45 | -0.02 | 53141212.89 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.66 | 0.23 | -0.02 | 239966515.68 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 0.29 | 0.56 | 0.15 | -0.01 | 492107742.81 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.27 | 5.83 | 4.77 | -0.01 | 494136.41 | 3.69 | skipped_fast |
| PYTHUSDT | IDLE | 1.03 | 1.87 | 1.21 | -0.03 | 691645.24 | 5.15 | skipped_fast |
| HBARUSDT | IDLE | 1.38 | 2.52 | 1.56 | 0.02 | 804208.37 | 1.23 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 2.4 | 1.87 | -0.06 | 346009.26 | 8.68 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 6.46 | 2.02 | -0.03 | 70165.51 | 65.51 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 2.55 | 2.45 | 0.01 | 78420.82 | 9.98 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 2.86 | 0.84 | 0.05 | 232970.38 | 46.69 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 1.9 | 1.72 | -0.01 | 89292.15 | 11.16 | skipped_fast |
| CHIPUSDT | IDLE | 0.94 | 2.38 | 0.95 | -0.08 | 102232.49 | 11.97 | skipped_fast |
| KITEUSDT | IDLE | 0.91 | 1.6 | 1.5 | -0.03 | 72625.22 | 11.51 | skipped_fast |
| RWAINCUSDT | IDLE | 0.85 | 1.85 | 1.64 | -0.05 | 10052.7 | 17.88 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 2.7 | 2.13 | -0.08 | 36494.07 | 105.09 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.0 | 1.01 | -0.07 | 100773.94 | 54.57 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.45 | 0.85 | -0.01 | 56228.84 | 7.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.52 | 0.93 | 0.75 | -0.01 | 33241.17 | 3.99 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.22 | 0.97 | -0.03 | 3272.57 | 21.09 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.6 | 0.52 | -0.01 | 51586.08 | 44.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
