# Hulk DIGEST — 2026-09-11T14:21:21Z

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
| XRPUSDT | IDLE | 4.16 | 8.82 | 2.53 | 0.03 | 48733970.85 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 4.06 | 9.44 | 2.02 | 0.08 | 521503993.65 | 0.8 | skipped_fast |
| BTCUSDT | IDLE | 2.54 | 4.93 | 0.94 | 0.03 | 525279792.52 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 75.81 | 28.57 | 0.08 | 115153.6 | 54.89 | skipped_fast |
| CCUSDT | IDLE | 3.87 | 7.68 | 0.46 | 0.0 | 447711.02 | 10.83 | skipped_fast |
| PYTHUSDT | IDLE | 3.94 | 7.72 | 1.02 | 0.03 | 391960.02 | 1.87 | skipped_fast |
| WUSDT | IDLE | 3.43 | 6.71 | 1.01 | 0.02 | 139920.72 | 10.23 | skipped_fast |
| BIOUSDT | IDLE | 3.34 | 6.49 | 1.27 | 0.01 | 80051.71 | 3.91 | skipped_fast |
| REDUSDT | IDLE | 3.29 | 6.52 | 0.36 | 0.03 | 60776.75 | 11.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 5.61 | 0.81 | 0.02 | 173763.0 | 31.88 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.08 | 8.51 | 6.03 | 0.02 | 9247.82 | 121.35 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 7.14 | 0.5 | 0.01 | 136267.97 | 10.51 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.06 | 8.79 | 0.97 | 0.03 | 105372.75 | 60.03 | skipped_fast |
| EDELUSDT | IDLE | 1.58 | 7.66 | 0.8 | -0.0 | 197318.18 | 26.87 | skipped_fast |
| HBARUSDT | IDLE | 2.59 | 5.04 | 0.88 | 0.01 | 210378.32 | 1.31 | skipped_fast |
| KITEUSDT | IDLE | 1.79 | 3.5 | 0.52 | 0.01 | 58775.02 | 14.57 | skipped_fast |
| QNTUSDT | IDLE | 2.74 | 5.19 | 1.94 | 0.01 | 41035.43 | 9.13 | skipped_fast |
| FLUIDUSDT | IDLE | 2.25 | 4.49 | 0.0 | 0.03 | 1300.24 | 31.63 | skipped_fast |
| RWAUSDT | IDLE | 1.56 | 3.05 | 0.52 | 0.02 | 50517.02 | 14.84 | skipped_fast |
| MNSRYUSDT | IDLE | 1.61 | 3.1 | 0.79 | 0.02 | 38360.17 | 59.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
