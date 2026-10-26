# Hulk DIGEST — 2026-10-26T15:25:07Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.08 | 2.11 | 0.33 | 0.0 | 132183851.79 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.03 | 2.01 | 0.27 | 0.01 | 22638920.34 | 2.3 | skipped_fast |
| BTCUSDT | IDLE | 0.86 | 1.69 | 0.21 | 0.0 | 312992807.59 | 0.24 | skipped_fast |
| QNTUSDT | IDLE | 1.89 | 8.84 | 5.21 | 0.15 | 1501100.32 | 13.69 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 3.05 | 0.51 | 0.06 | 921558.3 | 5.26 | skipped_fast |
| WUSDT | IDLE | 3.07 | 5.96 | 1.24 | 0.03 | 560024.39 | 44.18 | skipped_fast |
| CHIPUSDT | IDLE | 2.39 | 13.6 | 2.76 | 0.16 | 164833.45 | 17.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.09 | 2.79 | 0.0 | -0.02 | 215298.93 | 33.07 | skipped_fast |
| CCUSDT | IDLE | 0.9 | 1.74 | 0.43 | -0.01 | 185524.62 | 6.92 | skipped_fast |
| REDUSDT | IDLE | 1.5 | 2.98 | 0.07 | 0.05 | 61330.03 | 14.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.42 | 1.27 | -0.06 | 64241.31 | 5.83 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.78 | 0.04 | 0.01 | 59710.02 | 8.87 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 2.74 | 0.38 | 0.02 | 53307.47 | 12.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 3.33 | 1.93 | 0.0 | 34200.37 | 64.89 | skipped_fast |
| EDELUSDT | IDLE | 1.01 | 2.24 | 1.36 | 0.08 | 130259.78 | 24.98 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.48 | 0.04 | 0.02 | 225016.38 | 8.97 | skipped_fast |
| WAXLUSDT | IDLE | 1.79 | 3.57 | 0.12 | -0.01 | 53178.04 | 50.97 | skipped_fast |
| LAUSDT | IDLE | 1.34 | 2.81 | 0.8 | 0.03 | 63633.22 | 18.82 | skipped_fast |
| IOTAUSDT | IDLE | 1.25 | 2.44 | 0.39 | 0.01 | 73808.82 | 23.22 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.99 | 0.34 | -0.02 | 1803.36 | 21.32 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.44 | 0.71 | -0.0 | 54293.69 | 31.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.74 | 0.29 | -0.01 | 42715.49 | 73.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
