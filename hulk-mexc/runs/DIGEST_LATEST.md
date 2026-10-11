# Hulk DIGEST — 2026-10-11T14:21:30Z

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
| XRPUSDT | IDLE | 0.34 | 0.66 | 0.15 | -0.01 | 10064769.84 | 0.72 | n/a |
| ETHUSDT | IDLE | 0.25 | 0.46 | 0.28 | 0.0 | 172952613.94 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.19 | 0.34 | 0.22 | 0.0 | 124968967.59 | 0.0 | no_map |
| WUSDT | IDLE | 0.87 | 2.42 | 0.56 | -0.01 | 1101721.33 | 6.28 | tvl≈1,647,600,291 |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 31.62 | 16.61 | 0.04 | 59494.23 | 20.17 | tvl≈2,414,250,512 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 11.9 | 7.33 | -0.0 | 28327.34 | 4.89 | no_map |
| QNTUSDT | IDLE | 1.59 | 3.03 | 0.95 | -0.02 | 1022819.39 | 2.46 | n/a |
| PYTHUSDT | IDLE | 1.42 | 2.56 | 1.88 | -0.02 | 724681.99 | 5.22 | tvl≈171,505,575 |
| CCUSDT | IDLE | 1.93 | 3.8 | 0.43 | 0.03 | 305698.78 | 8.09 | no_map |
| CHIPUSDT | IDLE | 0.92 | 9.04 | 0.72 | 0.33 | 394008.38 | 17.29 | no_map |
| EDELUSDT | IDLE | 1.25 | 2.3 | 1.28 | 0.01 | 383213.98 | 10.34 | no_map |
| RIZEUSDT | IDLE | 2.35 | 6.54 | 2.59 | -0.06 | 35566.55 | 31.87 | no_map |
| ZBCNUSDT | IDLE | 1.33 | 2.54 | 0.74 | 0.0 | 161021.51 | 21.85 | n/a |
| BIOUSDT | IDLE | 1.39 | 2.71 | 0.47 | 0.03 | 76197.22 | 6.72 | n/a |
| TELUSDT | IDLE | 2.16 | 3.85 | 3.25 | -0.06 | 147845.1 | 29.49 | no_map |
| REDUSDT | IDLE | 0.85 | 1.58 | 0.81 | -0.01 | 57960.09 | 17.48 | tvl≈3,718,072 |
| KITEUSDT | IDLE | 0.67 | 1.24 | 0.73 | -0.03 | 74385.36 | 11.92 | no_map |
| HBARUSDT | IDLE | 0.84 | 1.65 | 0.24 | -0.01 | 243687.3 | 4.35 | empty_tvl |
| RWAUSDT | IDLE | 0.77 | 1.51 | 0.16 | 0.0 | 52162.58 | 7.83 | no_map |
| MNSRYUSDT | IDLE | 0.39 | 0.74 | 0.29 | -0.01 | 31621.38 | 28.73 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
