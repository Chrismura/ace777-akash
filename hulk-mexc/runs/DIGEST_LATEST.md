# Hulk DIGEST — 2026-09-27T23:14:04Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 105.87 | 19.59 | 0.99 | 13041189.57 | 24.71 | n/a |
| PYTHUSDT | IDLE | 2.18 | 4.8 | 4.03 | 0.03 | 2310862.48 | 1.2 | tvl≈193,194,886 |
| WUSDT | IDLE | 1.37 | 7.72 | 4.38 | 0.19 | 5066218.73 | 13.54 | tvl≈1,897,992,344 |
| XRPUSDT | IDLE | 1.41 | 2.51 | 2.06 | -0.01 | 42135561.72 | 1.99 | n/a |
| ETHUSDT | IDLE | 0.62 | 1.1 | 0.91 | -0.01 | 208080990.89 | 0.49 | no_map |
| BTCUSDT | IDLE | 0.47 | 0.83 | 0.78 | -0.0 | 429465070.45 | 0.0 | no_map |
| CCUSDT | IDLE | 1.69 | 2.98 | 2.71 | -0.01 | 632842.03 | 9.61 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 24.16 | 18.24 | -0.24 | 53921.83 | 78.8 | no_map |
| ZBCNUSDT | IDLE | 2.88 | 5.08 | 4.52 | -0.03 | 216700.63 | 21.06 | n/a |
| EDELUSDT | IDLE | 2.17 | 8.73 | 8.03 | -0.15 | 141040.88 | 3.95 | no_map |
| HBARUSDT | IDLE | 1.1 | 2.03 | 1.16 | 0.01 | 782214.76 | 1.06 | empty_tvl |
| RWAINCUSDT | IDLE | 2.01 | 20.76 | 2.73 | 0.24 | 29038.97 | 102.77 | no_map |
| CHIPUSDT | IDLE | 1.97 | 3.74 | 3.04 | -0.06 | 99175.42 | 17.32 | no_map |
| REDUSDT | IDLE | 1.58 | 2.87 | 1.9 | 0.01 | 65253.7 | 13.51 | tvl≈3,109,907 |
| KITEUSDT | IDLE | 1.02 | 2.05 | 0.36 | 0.0 | 117007.03 | 9.13 | no_map |
| BIOUSDT | IDLE | 1.03 | 1.88 | 1.19 | -0.01 | 81704.39 | 3.16 | n/a |
| TELUSDT | IDLE | 0.84 | 2.96 | 0.53 | 0.13 | 178197.16 | 59.03 | no_map |
| FLUIDUSDT | IDLE | 1.14 | 2.07 | 1.35 | 0.03 | 2838.49 | 21.58 | tvl≈2,591,959,221 |
| RWAUSDT | IDLE | 0.08 | 0.14 | 0.14 | 0.01 | 58969.8 | 7.07 | no_map |
| MNSRYUSDT | IDLE | 0.22 | 0.41 | 0.16 | 0.01 | 39956.55 | 36.69 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
