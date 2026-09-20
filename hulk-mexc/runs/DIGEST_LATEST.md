# Hulk DIGEST — 2026-09-20T05:01:12Z

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
| XRPUSDT | IDLE | 1.72 | 3.13 | 2.12 | -0.02 | 57692823.77 | 2.9 | n/a |
| ETHUSDT | IDLE | 1.49 | 2.67 | 2.01 | -0.01 | 249117356.17 | 0.31 | no_map |
| BTCUSDT | IDLE | 0.83 | 1.49 | 1.1 | -0.01 | 471010339.15 | 0.0 | no_map |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 6.71 | 5.49 | -0.03 | 725958.76 | 3.4 | tvl≈136,183,975 |
| WUSDT | IDLE | 2.72 | 4.91 | 3.52 | 0.02 | 507698.21 | 6.37 | tvl≈1,608,705,445 |
| HBARUSDT | IDLE | 3.0 | 5.43 | 3.79 | 0.02 | 689407.38 | 1.24 | empty_tvl |
| CCUSDT | IDLE | 2.52 | 5.16 | 3.69 | -0.05 | 327075.58 | 7.58 | no_map |
| CHIPUSDT | IDLE | 2.47 | 6.39 | 5.1 | -0.08 | 110581.1 | 16.72 | no_map |
| BIOUSDT | IDLE | 2.63 | 4.75 | 3.37 | 0.01 | 88357.31 | 7.34 | n/a |
| ZBCNUSDT | IDLE | 1.68 | 6.3 | 4.06 | 0.06 | 217328.88 | 31.26 | n/a |
| REDUSDT | IDLE | 1.95 | 3.81 | 0.65 | 0.04 | 100039.01 | 13.92 | tvl≈2,691,927 |
| RIZEUSDT | IDLE | 2.37 | 8.99 | 3.51 | -0.02 | 39336.01 | 103.41 | no_map |
| KITEUSDT | IDLE | 1.54 | 2.81 | 1.82 | 0.0 | 76350.69 | 11.49 | no_map |
| EDELUSDT | IDLE | 1.36 | 5.56 | 4.27 | -0.12 | 102305.14 | 57.04 | no_map |
| QNTUSDT | IDLE | 1.74 | 3.12 | 2.44 | 0.02 | 55476.91 | 9.31 | n/a |
| FLUIDUSDT | IDLE | 1.94 | 3.45 | 2.85 | -0.02 | 6692.04 | 21.61 | tvl≈2,629,131,794 |
| RWAINCUSDT | IDLE | 0.3 | 0.66 | 0.59 | -0.03 | 7299.21 | 5.96 | no_map |
| TELUSDT | IDLE | 1.04 | 2.06 | 1.28 | -0.07 | 105539.6 | 47.64 | no_map |
| RWAUSDT | IDLE | 0.95 | 1.72 | 1.17 | -0.0 | 52759.28 | 22.26 | no_map |
| MNSRYUSDT | IDLE | 0.38 | 0.75 | 0.09 | -0.01 | 34320.11 | 72.97 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
