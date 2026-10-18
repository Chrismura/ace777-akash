# Hulk DIGEST — 2026-10-18T02:25:32Z

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
| ETHUSDT | IDLE | 1.43 | 2.79 | 0.53 | -0.0 | 93609879.43 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.42 | 2.74 | 0.67 | -0.01 | 17604805.29 | 1.54 | n/a |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 9.68 | 6.78 | -0.09 | 1070728.53 | 1.27 | tvl≈176,051,498 |
| BTCUSDT | IDLE | 0.67 | 1.3 | 0.21 | 0.0 | 178579223.84 | 0.0 | no_map |
| WUSDT | IDLE | 1.47 | 4.48 | 1.89 | -0.04 | 1085941.63 | 18.07 | tvl≈1,590,323,785 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 9.38 | 7.38 | -0.11 | 162797.62 | 11.38 | no_map |
| QNTUSDT | IDLE | 2.65 | 5.0 | 1.94 | -0.02 | 585182.13 | 1.02 | n/a |
| ZBCNUSDT | IDLE | 2.29 | 4.09 | 3.25 | -0.04 | 179417.08 | 16.13 | n/a |
| BIOUSDT | IDLE | 2.34 | 4.41 | 1.79 | -0.04 | 71730.76 | 8.27 | n/a |
| CHIPUSDT | IDLE | 2.04 | 5.54 | 3.42 | -0.08 | 81757.25 | 11.71 | no_map |
| HBARUSDT | IDLE | 2.56 | 5.02 | 0.66 | 0.03 | 267652.01 | 6.95 | empty_tvl |
| CCUSDT | IDLE | 1.29 | 2.32 | 1.76 | -0.0 | 251362.23 | 6.8 | no_map |
| REDUSDT | IDLE | 1.83 | 3.34 | 2.18 | -0.04 | 61099.68 | 17.36 | tvl≈3,485,270 |
| KITEUSDT | IDLE | 1.5 | 3.79 | 2.08 | -0.04 | 70967.79 | 12.08 | no_map |
| RWAINCUSDT | IDLE | 1.15 | 3.53 | 2.12 | 0.06 | 20488.77 | 5.28 | no_map |
| TELUSDT | IDLE | 1.85 | 3.36 | 2.23 | -0.06 | 103640.11 | 36.97 | no_map |
| RIZEUSDT | IDLE | 0.89 | 1.74 | 0.21 | 0.01 | 45919.96 | 60.78 | no_map |
| FLUIDUSDT | IDLE | 1.42 | 2.69 | 0.97 | -0.01 | 1680.94 | 21.32 | tvl≈2,231,560,488 |
| RWAUSDT | IDLE | 1.21 | 2.35 | 0.4 | 0.0 | 52217.09 | 23.91 | no_map |
| MNSRYUSDT | IDLE | 0.42 | 0.75 | 0.65 | -0.0 | 30300.1 | 12.73 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
