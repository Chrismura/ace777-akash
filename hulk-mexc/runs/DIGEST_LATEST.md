# Hulk DIGEST — 2026-09-16T14:12:43Z

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
| ETHUSDT | IDLE | 1.04 | 1.82 | 1.71 | -0.03 | 461735377.47 | 0.21 | skipped_fast |
| XRPUSDT | IDLE | 0.9 | 2.32 | 2.08 | -0.1 | 84774725.2 | 2.36 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.04 | 1.02 | -0.01 | 584332314.26 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.37 | 2.4 | 2.3 | -0.03 | 690548.74 | 5.75 | skipped_fast |
| REDUSDT | IDLE | 2.92 | 5.12 | 4.86 | -0.07 | 66257.96 | 18.87 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 5.63 | 5.17 | -0.06 | 96145.29 | 13.7 | skipped_fast |
| EDELUSDT | IDLE | 0.53 | 7.66 | 5.56 | 0.27 | 424939.09 | 29.96 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.38 | 1.27 | -0.03 | 372330.0 | 8.81 | skipped_fast |
| WUSDT | IDLE | 1.07 | 2.33 | 1.64 | -0.08 | 225453.23 | 12.49 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 23.53 | 10.48 | 0.53 | 53874.56 | 174.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.0 | 2.59 | 1.57 | -0.04 | 198084.06 | 21.11 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 2.39 | 2.33 | -0.08 | 377773.23 | 1.37 | skipped_fast |
| KITEUSDT | IDLE | 1.44 | 2.71 | 2.57 | -0.08 | 60644.72 | 15.39 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 1.87 | 1.84 | -0.03 | 81599.36 | 8.15 | skipped_fast |
| TELUSDT | IDLE | 1.98 | 5.81 | 5.02 | -0.1 | 125249.04 | 35.73 | skipped_fast |
| RWAINCUSDT | IDLE | 0.44 | 0.76 | 0.75 | -0.02 | 12594.66 | 23.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.24 | 2.19 | -0.06 | 1852.48 | 21.65 | skipped_fast |
| QNTUSDT | IDLE | 0.91 | 1.62 | 1.27 | -0.05 | 46287.09 | 5.07 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.69 | 0.0 | -0.01 | 52880.4 | 7.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.09 | 0.18 | 0.01 | -0.02 | 33290.54 | 2.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
