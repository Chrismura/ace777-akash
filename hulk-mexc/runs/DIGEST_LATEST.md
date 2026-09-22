# Hulk DIGEST — 2026-09-22T18:15:20Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 17.48 | 8.92 | 0.05 | 1599760.8 | 2.98 | tvl≈142,720,178 |
| XRPUSDT | IDLE | 2.1 | 3.98 | 1.52 | 0.04 | 116547927.76 | 0.64 | n/a |
| ETHUSDT | IDLE | 0.89 | 1.73 | 0.37 | 0.0 | 466599009.56 | 0.51 | no_map |
| BTCUSDT | IDLE | 0.72 | 1.42 | 0.09 | 0.01 | 929337649.08 | 0.0 | no_map |
| HBARUSDT | IDLE | 2.03 | 4.42 | 2.87 | 0.05 | 1447023.6 | 2.08 | empty_tvl |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 18.96 | 10.39 | 0.01 | 289117.65 | 50.97 | no_map |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 6.3 | 5.66 | -0.03 | 483818.56 | 7.11 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.97 | 35.18 | 9.14 | -0.16 | 44149.27 | 110.39 | no_map |
| WUSDT | IDLE | 2.01 | 3.87 | 0.99 | 0.02 | 367586.73 | 8.3 | tvl≈1,783,009,545 |
| ZBCNUSDT | IDLE | 2.47 | 4.6 | 2.21 | -0.03 | 243088.97 | 26.04 | n/a |
| CHIPUSDT | IDLE | 2.41 | 4.48 | 2.29 | 0.01 | 140574.71 | 13.06 | no_map |
| BIOUSDT | IDLE | 2.36 | 4.57 | 1.04 | 0.02 | 136553.97 | 10.2 | n/a |
| REDUSDT | IDLE | 1.8 | 3.56 | 0.25 | 0.05 | 66038.35 | 7.58 | tvl≈2,837,450 |
| KITEUSDT | IDLE | 1.35 | 6.06 | 0.43 | 0.17 | 116278.03 | 10.85 | no_map |
| TELUSDT | IDLE | 2.68 | 7.85 | 0.0 | 0.07 | 105023.55 | 28.22 | no_map |
| QNTUSDT | IDLE | 1.65 | 5.05 | 2.97 | 0.09 | 178701.12 | 1.38 | n/a |
| RWAINCUSDT | IDLE | 0.5 | 1.0 | 0.0 | 0.05 | 20718.84 | 5.51 | no_map |
| RWAUSDT | IDLE | 0.67 | 1.32 | 0.14 | 0.0 | 54957.48 | 7.22 | no_map |
| FLUIDUSDT | IDLE | 0.67 | 1.25 | 0.63 | 0.02 | 7749.3 | 21.83 | tvl≈2,650,991,800 |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.03 | -0.0 | 40415.06 | 9.02 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
