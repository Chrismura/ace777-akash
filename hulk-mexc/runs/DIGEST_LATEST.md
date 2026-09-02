# Hulk DIGEST — 2026-09-02T15:48:17Z

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
| XRPUSDT | IDLE | 1.45 | 2.79 | 0.74 | -0.03 | 39657732.57 | 2.24 | n/a |
| ETHUSDT | IDLE | 1.41 | 2.63 | 1.22 | -0.02 | 412141724.93 | 0.63 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 11.79 | 9.82 | -0.07 | 1031379.6 | 2.45 | no_map |
| BTCUSDT | IDLE | 0.81 | 1.59 | 0.24 | -0.01 | 519641989.33 | 0.08 | no_map |
| PYTHUSDT | IDLE | 1.96 | 8.81 | 0.03 | 0.14 | 1184688.18 | 10.32 | tvl≈122,283,218 |
| CCUSDT | IDLE | 2.14 | 3.77 | 3.44 | -0.05 | 363739.91 | 9.09 | no_map |
| REDUSDT | IDLE | 2.74 | 5.41 | 0.48 | 0.02 | 159719.65 | 8.65 | tvl≈2,128,255 |
| WUSDT | IDLE | 1.45 | 2.78 | 0.78 | -0.03 | 388188.72 | 13.66 | tvl≈1,499,328,768 |
| KITEUSDT | IDLE | 1.65 | 6.19 | 2.09 | 0.12 | 94452.93 | 16.09 | no_map |
| RWAINCUSDT | IDLE | 1.93 | 5.69 | 2.85 | 0.08 | 10542.18 | 5.43 | no_map |
| RIZEUSDT | IDLE | 2.19 | 7.8 | 1.08 | -0.06 | 37298.68 | 77.43 | no_map |
| ZBCNUSDT | IDLE | 1.03 | 2.07 | 1.68 | -0.06 | 182884.8 | 11.11 | n/a |
| BIOUSDT | IDLE | 1.14 | 2.2 | 0.55 | -0.03 | 71138.02 | 3.94 | n/a |
| EDELUSDT | IDLE | 0.67 | 3.7 | 1.54 | 0.07 | 170266.48 | 24.72 | no_map |
| HBARUSDT | IDLE | 0.99 | 1.84 | 0.96 | -0.02 | 211698.13 | 1.36 | empty_tvl |
| FLUIDUSDT | IDLE | 2.0 | 3.74 | 2.33 | -0.06 | 1836.1 | 30.72 | tvl≈2,600,072,715 |
| TELUSDT | IDLE | 1.68 | 3.25 | 0.76 | -0.01 | 74432.1 | 29.4 | no_map |
| QNTUSDT | IDLE | 1.3 | 2.48 | 0.76 | 0.02 | 69834.39 | 9.33 | n/a |
| RWAUSDT | IDLE | 1.27 | 2.47 | 0.45 | 0.02 | 51691.07 | 7.57 | no_map |
| MNSRYUSDT | IDLE | 0.26 | 0.52 | 0.01 | -0.01 | 33753.6 | 39.89 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
