# Hulk DIGEST — 2026-10-18T03:26:02Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 7.25 | 5.35 | -0.09 | 1264558.75 | 3.85 | skipped_fast |
| ETHUSDT | IDLE | 0.97 | 1.89 | 0.29 | -0.0 | 94698029.59 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.37 | 0.4 | -0.01 | 17905086.16 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.98 | 0.17 | 0.0 | 184226200.65 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.8 | 2.4 | 1.24 | -0.03 | 1083523.97 | 16.0 | skipped_fast |
| EDELUSDT | IDLE | 2.68 | 8.69 | 4.7 | -0.08 | 180111.18 | 22.28 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 2.51 | 1.86 | -0.04 | 583785.54 | 1.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 3.48 | 2.57 | -0.04 | 177739.85 | 29.47 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 2.22 | 1.61 | -0.01 | 246813.17 | 5.83 | skipped_fast |
| HBARUSDT | IDLE | 1.93 | 3.7 | 1.09 | 0.02 | 268219.51 | 8.15 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.13 | 1.23 | -0.04 | 71881.21 | 4.14 | skipped_fast |
| CHIPUSDT | IDLE | 0.99 | 2.63 | 1.92 | -0.07 | 80935.69 | 14.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 3.48 | 1.86 | 0.06 | 20201.01 | 5.27 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 2.01 | 1.1 | -0.03 | 60774.47 | 17.29 | skipped_fast |
| KITEUSDT | IDLE | 0.81 | 1.99 | 1.47 | -0.05 | 70989.19 | 12.16 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 2.2 | 1.82 | -0.02 | 45870.6 | 57.44 | skipped_fast |
| TELUSDT | IDLE | 1.16 | 2.06 | 1.71 | -0.06 | 102905.08 | 18.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 0.97 | 0.65 | -0.0 | 29885.23 | 21.34 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.72 | 0.08 | -0.0 | 51883.28 | 15.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.61 | 1.23 | 0.0 | -0.01 | 1661.58 | 21.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
