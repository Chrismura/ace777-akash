# Hulk DIGEST — 2026-08-21T20:53:27Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.44 | 0.08 | 5562226.46 | 2.1 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.54 | 0.1 | 128441140.89 | 2.19 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.79 | 0.17 | 153009.78 | 8.95 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.51 | 0.12 | 478958.48 | 25.48 | n/a |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.31 | 0.1 | 642118.61 | 6.44 | no_map |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.81 | 0.06 | 809557.42 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.64 | 0.08 | 514548.0 | 6.19 | no_map |
| WUSDT | IDLE | 2.05 | 3.92 | 1.22 | 0.07 | 367710.56 | 14.73 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.48 | 0.01 | 188240.95 | 3.15 | n/a |
| EDELUSDT | IDLE | 2.93 | 5.73 | 4.98 | -0.06 | 82458.14 | 34.11 | no_map |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.61 | 0.02 | 56243.23 | 46.99 | no_map |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 37.62 | no_map |
| KITEUSDT | IDLE | 1.24 | 4.0 | 2.24 | 0.11 | 61237.27 | 12.98 | no_map |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.43 | 0.01 | 181289.67 | 37.56 | no_map |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.04 | 60028.89 | 1.56 | n/a |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.02 | 2798.65 | 175.02 | no_map |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53951.82 | 8.31 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.49 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
