# Hulk DIGEST — 2026-10-20T02:08:54Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 1.03 | 1.9 | 1.04 | -0.01 | 20635757.37 | 1.54 | n/a |
| ETHUSDT | IDLE | 1.01 | 1.85 | 1.16 | -0.02 | 125509536.68 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.72 | 1.31 | 0.85 | -0.01 | 312971997.73 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.08 | 3.71 | 3.0 | -0.04 | 1032236.04 | 1.39 | tvl≈162,110,455 |
| WUSDT | IDLE | 3.08 | 5.57 | 3.93 | -0.01 | 725823.12 | 16.18 | tvl≈1,560,881,489 |
| QNTUSDT | IDLE | 1.7 | 3.09 | 2.01 | -0.0 | 708926.71 | 2.59 | n/a |
| CCUSDT | IDLE | 1.15 | 2.26 | 0.25 | 0.03 | 386101.81 | 8.51 | no_map |
| EDELUSDT | IDLE | 1.9 | 3.61 | 1.28 | 0.01 | 177550.56 | 14.86 | no_map |
| CHIPUSDT | IDLE | 1.85 | 3.33 | 2.42 | -0.03 | 76030.77 | 12.04 | no_map |
| REDUSDT | IDLE | 1.65 | 3.0 | 1.99 | -0.02 | 57289.56 | 11.01 | tvl≈3,411,415 |
| ZBCNUSDT | IDLE | 0.98 | 2.56 | 1.58 | -0.0 | 197609.26 | 17.8 | n/a |
| KITEUSDT | IDLE | 1.49 | 2.86 | 2.21 | 0.05 | 77087.03 | 20.59 | no_map |
| BIOUSDT | IDLE | 1.34 | 2.46 | 1.43 | -0.02 | 66711.55 | 8.56 | n/a |
| RWAINCUSDT | IDLE | 1.3 | 2.61 | 2.24 | 0.03 | 67864.15 | 25.94 | no_map |
| HBARUSDT | IDLE | 0.8 | 1.5 | 0.73 | -0.02 | 428092.65 | 6.05 | empty_tvl |
| RIZEUSDT | IDLE | 0.56 | 1.92 | 0.76 | -0.05 | 52449.85 | 43.95 | no_map |
| FLUIDUSDT | IDLE | 0.83 | 1.67 | 0.0 | 0.02 | 4706.89 | 21.71 | tvl≈2,225,198,365 |
| RWAUSDT | IDLE | 0.33 | 0.63 | 0.23 | 0.0 | 52778.37 | 23.54 | no_map |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
