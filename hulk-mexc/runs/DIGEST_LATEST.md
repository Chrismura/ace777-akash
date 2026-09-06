# Hulk DIGEST — 2026-09-06T15:31:46Z

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
| XRPUSDT | IDLE | 1.09 | 2.0 | 1.21 | -0.0 | 26203036.06 | 2.13 | n/a |
| ETHUSDT | IDLE | 0.94 | 1.72 | 1.02 | 0.01 | 258310892.96 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.55 | 1.03 | 0.45 | -0.0 | 405660417.5 | 0.0 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.0 | 7.8 | 7.24 | -0.02 | 441471.2 | 1.77 | no_map |
| PYTHUSDT | IDLE | 2.61 | 4.73 | 3.22 | -0.0 | 505753.35 | 1.84 | tvl≈123,271,808 |
| WUSDT | IDLE | 2.29 | 4.42 | 1.01 | 0.05 | 250071.65 | 13.49 | tvl≈1,663,589,288 |
| EDELUSDT | IDLE | 3.22 | 5.72 | 4.86 | -0.01 | 65931.37 | 48.24 | no_map |
| CCUSDT | IDLE | 1.4 | 2.55 | 1.73 | 0.0 | 331378.93 | 7.31 | no_map |
| RIZEUSDT | IDLE | 1.92 | 12.98 | 10.46 | -0.08 | 80995.03 | 64.46 | no_map |
| ZBCNUSDT | IDLE | 1.87 | 3.32 | 2.84 | -0.01 | 199301.97 | 13.95 | n/a |
| BIOUSDT | IDLE | 2.07 | 3.74 | 2.64 | -0.02 | 92067.12 | 3.67 | n/a |
| REDUSDT | IDLE | 2.29 | 4.14 | 2.95 | 0.02 | 63294.68 | 18.9 | tvl≈2,331,573 |
| RWAINCUSDT | IDLE | 2.18 | 4.61 | 3.35 | 0.05 | 6271.22 | 31.19 | no_map |
| HBARUSDT | IDLE | 1.02 | 1.83 | 1.35 | -0.0 | 416581.69 | 1.24 | empty_tvl |
| KITEUSDT | IDLE | 1.17 | 2.05 | 1.87 | -0.01 | 60698.63 | 7.93 | no_map |
| TELUSDT | IDLE | 1.1 | 1.95 | 1.62 | -0.01 | 65509.85 | 41.16 | no_map |
| RWAUSDT | IDLE | 0.83 | 1.44 | 1.42 | -0.02 | 54436.99 | 7.2 | no_map |
| QNTUSDT | IDLE | 0.82 | 1.52 | 0.85 | 0.02 | 38864.12 | 4.59 | n/a |
| MNSRYUSDT | IDLE | 0.37 | 0.67 | 0.43 | 0.02 | 41932.5 | 5.37 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.03 | 341.7 | 21.29 | tvl≈2,659,762,913 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
