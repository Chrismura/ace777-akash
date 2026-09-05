# Hulk DIGEST — 2026-09-05T23:29:55Z

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
| XRPUSDT | IDLE | 0.6 | 1.05 | 0.95 | 0.01 | 22344894.8 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.43 | 0.78 | 0.47 | 0.01 | 160443034.23 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.49 | 0.34 | 0.0 | 351424932.49 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 18.85 | 15.71 | -0.04 | 133913.63 | 59.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 3.82 | 1.33 | 0.08 | 426937.28 | 3.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.86 | 5.2 | 3.49 | 0.0 | 8098.8 | 10.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.09 | 4.0 | 1.25 | -0.0 | 209737.63 | 23.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.01 | 1.91 | 0.76 | 0.01 | 337811.92 | 1.82 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.69 | 1.38 | 0.02 | 274976.93 | 8.26 | skipped_fast |
| WUSDT | IDLE | 1.01 | 1.95 | 0.49 | 0.04 | 143256.55 | 18.03 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.51 | 1.38 | 0.03 | 81881.75 | 3.6 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 1.92 | 0.74 | 0.05 | 60837.36 | 10.27 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.38 | 1.26 | 0.03 | 362701.91 | 1.25 | skipped_fast |
| EDELUSDT | IDLE | 0.12 | 2.28 | 0.0 | -0.01 | 167531.15 | 18.59 | skipped_fast |
| KITEUSDT | IDLE | 0.51 | 1.21 | 0.66 | -0.06 | 64153.43 | 8.72 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 3.58 | 2.24 | -0.01 | 71874.23 | 41.19 | skipped_fast |
| RWAUSDT | IDLE | 1.62 | 2.96 | 1.92 | 0.04 | 52707.08 | 27.89 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 1.5 | 0.87 | 0.02 | 36528.71 | 3.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.26 | 0.05 | 0.0 | 38019.38 | 2.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.43 | 0.79 | 0.5 | 0.02 | 515.49 | 20.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
