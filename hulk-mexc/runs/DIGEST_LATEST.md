# Hulk DIGEST — 2026-09-10T22:16:39Z

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
| XRPUSDT | IDLE | 0.7 | 1.28 | 0.84 | -0.03 | 42020343.52 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.11 | 0.66 | 0.0 | 421102032.57 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.69 | 0.5 | -0.01 | 536706175.49 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.85 | 4.98 | 4.74 | -0.03 | 201565.53 | 30.75 | skipped_fast |
| CHIPUSDT | IDLE | 2.95 | 7.89 | 2.5 | -0.01 | 81701.4 | 14.26 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.46 | 0.82 | 0.01 | 465897.59 | 1.92 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.24 | 1.34 | -0.04 | 479870.72 | 6.07 | skipped_fast |
| EDELUSDT | IDLE | 0.9 | 3.88 | 1.16 | 0.1 | 265507.6 | 17.95 | skipped_fast |
| WUSDT | IDLE | 1.11 | 1.99 | 1.55 | -0.02 | 176364.76 | 10.4 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.45 | 2.23 | -0.02 | 80555.6 | 4.0 | skipped_fast |
| RIZEUSDT | IDLE | 0.4 | 22.84 | 1.98 | -0.5 | 128419.56 | 100.7 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.16 | 2.08 | -0.03 | 56617.53 | 11.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.01 | 1.92 | 0.67 | 0.02 | 4641.79 | 33.78 | skipped_fast |
| REDUSDT | IDLE | 0.62 | 1.38 | 0.39 | -0.05 | 66557.46 | 20.59 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.17 | 0.38 | -0.01 | 219916.16 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.33 | 2.21 | -0.02 | 35880.32 | 3.08 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.15 | 0.5 | -0.0 | 83299.99 | 22.28 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 1.84 | 1.81 | -0.05 | 1750.98 | 22.28 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.68 | 0.53 | -0.02 | 51002.98 | 15.17 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.25 | 0.01 | -0.01 | 33034.01 | 5.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
