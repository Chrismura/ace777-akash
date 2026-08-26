# Hulk DIGEST — 2026-08-26T04:45:11Z

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
| PYTHUSDT | IDLE | 2.62 | 5.59 | 0.31 | 0.01 | 2533259.58 | 1.92 | tvl≈112,350,117 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.91 | 76.3 | 34.44 | 0.18 | 61130.57 | 31.98 | no_map |
| XRPUSDT | IDLE | 0.91 | 1.88 | 0.54 | -0.04 | 60521353.13 | 2.08 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 31.72 | 7.93 | 0.17 | 14508.64 | 21.98 | tvl≈2,588,824,896 |
| CCUSDT | IDLE | 1.33 | 2.58 | 2.08 | -0.04 | 514289.11 | 9.25 | no_map |
| CHIPUSDT | IDLE | 1.63 | 4.71 | 1.58 | -0.03 | 378959.25 | 6.18 | no_map |
| WUSDT | IDLE | 1.57 | 3.09 | 0.67 | -0.03 | 288832.67 | 6.33 | tvl≈1,573,173,601 |
| EDELUSDT | IDLE | 0.9 | 12.62 | 10.36 | 0.03 | 159384.19 | 18.8 | no_map |
| REDUSDT | IDLE | 1.95 | 4.97 | 2.31 | 0.01 | 80012.24 | 9.51 | tvl≈2,063,363 |
| HBARUSDT | IDLE | 0.94 | 1.84 | 0.2 | -0.04 | 576696.65 | 1.27 | empty_tvl |
| ZBCNUSDT | IDLE | 1.53 | 2.99 | 0.45 | -0.02 | 160046.11 | 17.76 | n/a |
| KITEUSDT | IDLE | 1.89 | 3.76 | 0.1 | 0.0 | 59256.61 | 12.95 | no_map |
| BIOUSDT | IDLE | 1.16 | 2.04 | 1.83 | -0.04 | 95407.82 | 6.92 | n/a |
| QAITUSDT | IDLE | 0.93 | 2.61 | 0.0 | 0.05 | 13000.46 | 62.77 | no_map |
| RWAINCUSDT | IDLE | 0.93 | 1.62 | 1.55 | 0.01 | 1514.61 | 126.04 | no_map |
| RWAUSDT | IDLE | 1.19 | 2.09 | 1.88 | -0.05 | 55959.0 | 41.68 | no_map |
| QNTUSDT | IDLE | 0.54 | 1.05 | 0.2 | -0.04 | 131759.61 | 1.57 | n/a |
| TELUSDT | IDLE | 0.83 | 1.61 | 0.33 | -0.03 | 93616.89 | 43.88 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
