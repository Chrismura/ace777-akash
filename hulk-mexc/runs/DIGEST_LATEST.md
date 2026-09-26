# Hulk DIGEST — 2026-09-26T23:04:17Z

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
| QNTUSDT | IDLE | 1.93 | 24.43 | 0.81 | 0.5 | 1696305.68 | 11.61 | n/a |
| XRPUSDT | IDLE | 1.25 | 2.38 | 0.77 | -0.03 | 40314172.08 | 0.66 | n/a |
| ETHUSDT | IDLE | 0.54 | 1.07 | 0.01 | -0.0 | 113588608.05 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.34 | 0.68 | 0.05 | 0.0 | 335660560.23 | 0.07 | no_map |
| PYTHUSDT | IDLE | 2.08 | 6.07 | 0.09 | 0.09 | 1069947.88 | 6.18 | tvl≈178,469,146 |
| CCUSDT | IDLE | 1.72 | 3.73 | 1.03 | 0.05 | 832476.06 | 6.63 | no_map |
| WUSDT | IDLE | 2.53 | 5.22 | 1.48 | 0.06 | 566821.32 | 10.75 | tvl≈1,851,860,679 |
| EDELUSDT | IDLE | 2.94 | 5.27 | 4.01 | 0.02 | 171937.91 | 10.04 | no_map |
| CHIPUSDT | IDLE | 2.56 | 6.17 | 2.88 | -0.03 | 103915.04 | 10.23 | no_map |
| KITEUSDT | IDLE | 1.99 | 7.67 | 1.7 | 0.14 | 126590.86 | 8.57 | no_map |
| BIOUSDT | IDLE | 2.14 | 3.95 | 2.17 | -0.03 | 112944.94 | 9.39 | n/a |
| HBARUSDT | IDLE | 1.35 | 2.57 | 0.86 | -0.02 | 544973.9 | 1.07 | empty_tvl |
| ZBCNUSDT | IDLE | 1.64 | 2.97 | 2.09 | -0.03 | 190924.28 | 17.24 | n/a |
| RIZEUSDT | IDLE | 2.35 | 6.03 | 0.52 | 0.1 | 49303.1 | 59.87 | no_map |
| REDUSDT | IDLE | 1.62 | 2.99 | 1.72 | -0.03 | 58782.42 | 14.29 | tvl≈3,065,259 |
| RWAINCUSDT | IDLE | 1.39 | 4.65 | 4.16 | 0.04 | 10058.44 | 63.37 | no_map |
| TELUSDT | IDLE | 1.53 | 3.0 | 0.36 | 0.0 | 120779.0 | 18.26 | no_map |
| FLUIDUSDT | IDLE | 1.24 | 2.29 | 1.32 | 0.0 | 633.15 | 19.42 | tvl≈2,582,844,082 |
| RWAUSDT | IDLE | 0.62 | 1.15 | 0.57 | 0.03 | 56502.58 | 7.16 | no_map |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.15 | -0.0 | 38484.45 | 22.95 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
