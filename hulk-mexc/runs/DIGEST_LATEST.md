# Hulk DIGEST — 2026-10-17T21:22:15Z

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
| XRPUSDT | IDLE | 0.76 | 1.46 | 0.34 | -0.0 | 13192264.53 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.53 | 1.05 | 0.12 | 0.0 | 77253574.88 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.31 | 0.61 | 0.08 | -0.0 | 168259347.34 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.12 | 5.54 | 0.76 | -0.03 | 955695.73 | 4.79 | tvl≈185,824,620 |
| WUSDT | IDLE | 1.81 | 5.3 | 2.41 | -0.06 | 996160.84 | 17.25 | tvl≈1,599,020,313 |
| QNTUSDT | IDLE | 1.51 | 2.79 | 1.47 | -0.03 | 519494.23 | 2.53 | n/a |
| ZBCNUSDT | IDLE | 1.75 | 3.49 | 0.1 | -0.01 | 193092.31 | 21.12 | n/a |
| CCUSDT | IDLE | 1.09 | 2.02 | 1.02 | 0.01 | 261000.39 | 10.56 | no_map |
| EDELUSDT | IDLE | 1.24 | 2.19 | 1.94 | -0.04 | 150750.64 | 7.06 | no_map |
| HBARUSDT | IDLE | 2.24 | 4.47 | 0.02 | 0.03 | 197709.59 | 1.17 | empty_tvl |
| BIOUSDT | IDLE | 1.38 | 2.67 | 0.61 | -0.03 | 71717.78 | 4.08 | n/a |
| RIZEUSDT | IDLE | 1.51 | 2.8 | 1.5 | -0.03 | 50396.19 | 61.33 | no_map |
| CHIPUSDT | IDLE | 0.92 | 1.67 | 1.15 | -0.05 | 81305.73 | 13.7 | no_map |
| KITEUSDT | IDLE | 0.91 | 1.68 | 1.4 | -0.03 | 68564.48 | 12.81 | no_map |
| REDUSDT | IDLE | 0.97 | 1.91 | 0.23 | -0.03 | 59331.68 | 10.63 | tvl≈3,487,263 |
| RWAINCUSDT | IDLE | 0.88 | 3.31 | 0.0 | 0.08 | 20125.25 | 5.17 | no_map |
| TELUSDT | IDLE | 1.28 | 2.32 | 1.61 | -0.06 | 98614.11 | 18.19 | no_map |
| RWAUSDT | IDLE | 0.52 | 0.96 | 0.55 | 0.0 | 51066.86 | 15.87 | no_map |
| FLUIDUSDT | IDLE | 0.76 | 1.51 | 0.0 | 0.0 | 1570.34 | 20.99 | tvl≈2,234,993,388 |
| MNSRYUSDT | IDLE | 0.34 | 0.68 | 0.06 | 0.01 | 31406.31 | 8.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
