# Hulk DIGEST — 2026-10-14T10:16:18Z

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
| PYTHUSDT | IDLE | 2.57 | 5.23 | 2.37 | -0.02 | 1769825.4 | 1.22 | tvl≈181,249,525 |
| WUSDT | IDLE | 1.11 | 6.53 | 3.4 | -0.19 | 3722157.28 | 4.33 | tvl≈1,665,520,068 |
| ETHUSDT | IDLE | 1.07 | 1.94 | 1.3 | -0.01 | 127215369.6 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.01 | 1.8 | 1.46 | 0.0 | 29915180.91 | 1.46 | n/a |
| BTCUSDT | IDLE | 0.73 | 1.31 | 0.96 | -0.0 | 328595466.12 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.33 | 3.18 | 2.46 | -0.05 | 1701338.11 | 1.42 | n/a |
| CCUSDT | IDLE | 1.94 | 3.66 | 3.38 | 0.0 | 574524.87 | 9.08 | no_map |
| CHIPUSDT | IDLE | 2.55 | 4.54 | 3.76 | -0.05 | 80320.07 | 12.53 | no_map |
| KITEUSDT | IDLE | 2.22 | 6.92 | 4.28 | 0.07 | 76524.6 | 8.08 | no_map |
| EDELUSDT | IDLE | 1.33 | 2.49 | 1.07 | 0.05 | 216152.0 | 20.41 | no_map |
| REDUSDT | IDLE | 1.52 | 2.72 | 2.13 | -0.01 | 63813.07 | 16.09 | tvl≈3,962,736 |
| BIOUSDT | IDLE | 1.33 | 2.35 | 2.01 | -0.01 | 69193.78 | 3.67 | n/a |
| RIZEUSDT | IDLE | 1.62 | 5.66 | 0.34 | 0.05 | 49796.79 | 57.67 | no_map |
| ZBCNUSDT | IDLE | 0.65 | 1.19 | 0.72 | -0.01 | 200882.27 | 10.11 | n/a |
| FLUIDUSDT | IDLE | 2.29 | 6.63 | 5.05 | 0.04 | 18131.32 | 21.33 | tvl≈2,380,473,938 |
| HBARUSDT | IDLE | 1.15 | 2.06 | 1.54 | -0.01 | 311541.66 | 5.79 | empty_tvl |
| RWAINCUSDT | IDLE | 0.98 | 2.08 | 1.53 | -0.08 | 34254.22 | 5.17 | no_map |
| TELUSDT | IDLE | 0.92 | 1.74 | 0.72 | 0.03 | 115240.39 | 33.43 | no_map |
| RWAUSDT | IDLE | 0.35 | 0.7 | 0.23 | -0.01 | 56439.03 | 7.77 | no_map |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.1 | -0.01 | 38130.99 | 12.57 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
