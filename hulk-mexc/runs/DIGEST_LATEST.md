# Hulk DIGEST — 2026-10-26T02:12:03Z

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
| ETHUSDT | IDLE | 1.24 | 2.23 | 1.63 | -0.02 | 97249066.05 | 0.48 | skipped_fast |
| BTCUSDT | IDLE | 0.92 | 1.67 | 1.1 | -0.01 | 173038000.76 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.81 | 1.49 | 0.87 | -0.01 | 15633474.64 | 2.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.28 | 2.77 | 1.57 | 0.05 | 718055.43 | 2.67 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.55 | 1.38 | -0.03 | 605587.25 | 16.93 | skipped_fast |
| ZBCNUSDT | IDLE | 2.75 | 4.95 | 4.18 | 0.0 | 181713.24 | 22.92 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 4.71 | 3.67 | -0.04 | 88558.31 | 16.28 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.44 | 1.27 | 0.05 | 674688.45 | 2.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.49 | 3.04 | -0.04 | 63385.96 | 39.81 | skipped_fast |
| EDELUSDT | IDLE | 0.9 | 2.13 | 1.68 | 0.05 | 252819.75 | 28.45 | skipped_fast |
| REDUSDT | IDLE | 1.63 | 2.97 | 1.9 | -0.02 | 59875.81 | 15.35 | skipped_fast |
| CCUSDT | IDLE | 1.08 | 2.01 | 0.99 | 0.0 | 182990.14 | 10.86 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 2.09 | 1.25 | -0.03 | 60178.65 | 9.05 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.1 | 1.18 | -0.02 | 54087.17 | 13.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 1.99 | 0.32 | 0.01 | 32878.52 | 62.16 | skipped_fast |
| LAUSDT | IDLE | 1.75 | 4.61 | 3.37 | -0.06 | 63856.28 | 39.57 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.04 | 1.36 | -0.01 | 178800.52 | 5.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 4.86 | 4.63 | -0.03 | 19110.91 | 21.24 | skipped_fast |
| IOTAUSDT | IDLE | 1.23 | 2.23 | 1.6 | -0.03 | 60197.64 | 25.91 | skipped_fast |
| WAXLUSDT | IDLE | 1.25 | 2.25 | 1.6 | 0.0 | 53971.78 | 43.16 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.0 | 52603.0 | 7.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.59 | 0.04 | -0.01 | 38100.94 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
