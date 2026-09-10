# Hulk DIGEST — 2026-09-10T02:14:48Z

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
| XRPUSDT | IDLE | 1.1 | 1.97 | 1.49 | -0.02 | 43604560.21 | 2.89 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.43 | 0.65 | -0.01 | 392279081.66 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 0.93 | 0.61 | -0.01 | 542773489.0 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.56 | 6.65 | 4.86 | -0.03 | 1011660.41 | 1.93 | skipped_fast |
| EDELUSDT | IDLE | 4.13 | 14.06 | 3.76 | 0.05 | 219865.08 | 45.52 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 2.75 | 1.86 | -0.04 | 643456.83 | 7.73 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 13.43 | 11.39 | -0.08 | 123826.17 | 14.29 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 7.24 | 5.78 | -0.08 | 102034.08 | 11.88 | skipped_fast |
| WUSDT | IDLE | 2.56 | 4.84 | 3.53 | -0.04 | 206967.29 | 11.21 | skipped_fast |
| REDUSDT | IDLE | 2.88 | 5.33 | 2.83 | -0.0 | 66612.67 | 18.84 | skipped_fast |
| KITEUSDT | IDLE | 1.98 | 3.5 | 3.08 | -0.02 | 57544.84 | 11.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.76 | 2.14 | -0.0 | 5978.02 | 28.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 2.08 | 1.4 | 0.02 | 185058.62 | 18.7 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 1.94 | 1.22 | -0.03 | 455350.86 | 1.31 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 9.66 | 0.0 | 0.05 | 60511.29 | 91.85 | skipped_fast |
| TELUSDT | IDLE | 1.53 | 2.76 | 1.97 | -0.01 | 96381.63 | 16.78 | skipped_fast |
| MNSRYUSDT | IDLE | 1.38 | 2.42 | 2.31 | -0.01 | 27722.87 | 2.78 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.02 | 1.43 | -0.01 | 45829.61 | 7.49 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.33 | -0.03 | 55008.2 | 14.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.97 | 1.69 | 1.67 | -0.08 | 1001.9 | 23.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
