# Hulk DIGEST — 2026-09-26T15:00:20Z

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
| XRPUSDT | IDLE | 0.55 | 1.03 | 0.44 | -0.03 | 50938798.11 | 1.94 | n/a |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.13 | -0.0 | 157092472.86 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.23 | 0.42 | 0.24 | 0.0 | 386852749.81 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.17 | 6.02 | 2.13 | 0.08 | 1183359.83 | 2.57 | tvl≈176,197,476 |
| CCUSDT | IDLE | 1.57 | 5.28 | 2.83 | 0.1 | 966411.2 | 7.31 | no_map |
| QNTUSDT | IDLE | 1.78 | 7.41 | 0.46 | 0.16 | 935029.74 | 0.91 | n/a |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 13.4 | 10.2 | -0.04 | 7696.44 | 74.07 | no_map |
| WUSDT | IDLE | 1.74 | 3.94 | 1.77 | 0.07 | 452543.25 | 5.48 | tvl≈1,858,100,460 |
| EDELUSDT | IDLE | 2.64 | 4.93 | 2.3 | 0.03 | 162705.36 | 3.27 | no_map |
| ZBCNUSDT | IDLE | 1.86 | 3.67 | 0.37 | -0.0 | 232730.02 | 11.58 | n/a |
| BIOUSDT | IDLE | 2.05 | 3.66 | 2.96 | -0.0 | 105137.63 | 3.09 | n/a |
| HBARUSDT | IDLE | 0.94 | 1.78 | 0.63 | 0.0 | 589576.19 | 1.06 | empty_tvl |
| CHIPUSDT | IDLE | 1.37 | 2.7 | 0.22 | 0.01 | 125887.05 | 22.28 | no_map |
| KITEUSDT | IDLE | 1.23 | 2.53 | 0.0 | 0.05 | 75483.59 | 23.19 | no_map |
| RIZEUSDT | IDLE | 1.45 | 7.38 | 3.51 | -0.1 | 46614.12 | 89.0 | no_map |
| REDUSDT | IDLE | 1.04 | 1.96 | 0.77 | -0.01 | 58431.21 | 7.68 | tvl≈3,085,363 |
| RWAUSDT | IDLE | 2.17 | 4.23 | 0.78 | 0.02 | 55670.38 | 14.35 | no_map |
| TELUSDT | IDLE | 1.54 | 2.78 | 2.03 | -0.04 | 122519.0 | 69.2 | no_map |
| FLUIDUSDT | IDLE | 0.61 | 1.22 | 0.0 | 0.03 | 628.63 | 22.02 | tvl≈2,584,477,393 |
| MNSRYUSDT | IDLE | 0.21 | 0.42 | 0.03 | 0.0 | 39457.13 | 48.49 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
