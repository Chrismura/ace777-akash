# Hulk DIGEST — 2026-10-22T12:29:30Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 0.81 | 3.64 | 3.12 | -0.05 | 3252368.75 | 14.84 | tvl≈1,578,515,866 |
| ETHUSDT | IDLE | 0.9 | 1.62 | 1.17 | -0.03 | 223827503.64 | 0.25 | no_map |
| XRPUSDT | IDLE | 0.87 | 1.58 | 1.08 | -0.02 | 32813058.96 | 1.51 | n/a |
| BTCUSDT | IDLE | 0.59 | 1.06 | 0.82 | -0.02 | 530574589.92 | 0.0 | no_map |
| HBARUSDT | IDLE | 1.07 | 1.94 | 1.34 | -0.05 | 1374041.37 | 6.19 | empty_tvl |
| QNTUSDT | IDLE | 0.92 | 2.17 | 1.93 | -0.03 | 1286402.14 | 1.03 | n/a |
| EDELUSDT | IDLE | 2.57 | 4.52 | 4.15 | -0.05 | 564773.35 | 12.18 | no_map |
| PYTHUSDT | IDLE | 1.03 | 2.84 | 1.6 | -0.07 | 628802.44 | 2.68 | tvl≈166,252,005 |
| ZBCNUSDT | IDLE | 2.23 | 6.18 | 1.99 | -0.05 | 223636.3 | 17.82 | n/a |
| CHIPUSDT | IDLE | 1.14 | 4.83 | 2.21 | -0.03 | 338273.06 | 13.58 | no_map |
| CCUSDT | IDLE | 0.81 | 2.43 | 1.92 | -0.03 | 396690.75 | 8.73 | no_map |
| RWAINCUSDT | IDLE | 1.89 | 3.51 | 1.84 | -0.0 | 64681.98 | 28.32 | no_map |
| REDUSDT | IDLE | 1.02 | 1.96 | 1.53 | -0.03 | 85521.95 | 16.93 | tvl≈3,561,575 |
| RIZEUSDT | IDLE | 1.34 | 3.0 | 0.89 | 0.03 | 43721.09 | 35.58 | no_map |
| BIOUSDT | IDLE | 0.84 | 1.81 | 0.83 | -0.04 | 77493.72 | 8.35 | n/a |
| KITEUSDT | IDLE | 0.95 | 1.83 | 0.46 | -0.02 | 60102.11 | 10.8 | no_map |
| IOTAUSDT | IDLE | 0.95 | 1.85 | 1.23 | -0.04 | 77973.97 | 22.16 | no_map |
| FLUIDUSDT | IDLE | 0.7 | 3.67 | 3.26 | -0.03 | 19562.57 | 21.32 | tvl≈2,216,960,780 |
| LAUSDT | IDLE | 0.71 | 1.91 | 0.81 | -0.03 | 58259.46 | 27.05 | no_map |
| WAXLUSDT | IDLE | 0.9 | 3.18 | 1.59 | -0.09 | 58503.05 | 63.53 | no_map |
| RWAUSDT | IDLE | 0.52 | 0.95 | 0.55 | -0.01 | 52685.26 | 15.79 | no_map |
| MNSRYUSDT | IDLE | 0.31 | 0.57 | 0.34 | 0.0 | 40223.87 | 55.51 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
