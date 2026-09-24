# Hulk DIGEST — 2026-09-24T22:40:35Z

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
| XRPUSDT | IDLE | 1.14 | 2.12 | 1.1 | 0.02 | 68647490.79 | 1.31 | n/a |
| ETHUSDT | IDLE | 0.81 | 1.52 | 0.73 | -0.0 | 352414127.02 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.5 | 0.9 | 0.61 | -0.0 | 721481490.39 | 0.0 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 42.58 | 25.64 | 0.04 | 198981.94 | 30.72 | no_map |
| PYTHUSDT | IDLE | 1.02 | 3.52 | 2.8 | 0.06 | 1165626.99 | 1.49 | tvl≈153,315,721 |
| CCUSDT | IDLE | 2.12 | 3.91 | 2.16 | 0.03 | 496056.97 | 5.33 | no_map |
| RIZEUSDT | IDLE | 2.92 | 35.82 | 4.65 | 0.4 | 69180.15 | 126.32 | no_map |
| HBARUSDT | IDLE | 1.54 | 2.88 | 1.31 | 0.03 | 818210.95 | 1.08 | empty_tvl |
| CHIPUSDT | IDLE | 2.37 | 12.95 | 4.3 | 0.15 | 95171.52 | 14.57 | no_map |
| QNTUSDT | IDLE | 1.96 | 17.26 | 5.64 | 0.27 | 290228.63 | 33.65 | n/a |
| ZBCNUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.0 | 203735.77 | 20.07 | n/a |
| WUSDT | IDLE | 1.23 | 2.24 | 1.49 | 0.05 | 247032.7 | 6.83 | tvl≈1,790,698,646 |
| KITEUSDT | IDLE | 1.68 | 2.93 | 2.85 | -0.01 | 65395.52 | 9.96 | no_map |
| RWAINCUSDT | IDLE | 1.4 | 7.19 | 2.53 | 0.19 | 11669.03 | 13.69 | no_map |
| BIOUSDT | IDLE | 1.08 | 3.14 | 2.79 | 0.09 | 87141.76 | 13.04 | n/a |
| REDUSDT | IDLE | 0.82 | 2.07 | 1.93 | 0.06 | 100600.53 | 13.77 | tvl≈2,918,395 |
| TELUSDT | IDLE | 1.58 | 2.9 | 1.68 | -0.06 | 110402.42 | 48.93 | no_map |
| RWAUSDT | IDLE | 0.95 | 1.77 | 0.8 | 0.01 | 57062.38 | 7.31 | no_map |
| FLUIDUSDT | IDLE | 0.46 | 0.91 | 0.0 | 0.05 | 1871.74 | 21.48 | tvl≈2,596,288,512 |
| MNSRYUSDT | IDLE | 0.39 | 0.76 | 0.19 | 0.0 | 37985.79 | 58.46 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
