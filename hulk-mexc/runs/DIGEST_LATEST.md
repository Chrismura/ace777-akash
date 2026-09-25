# Hulk DIGEST — 2026-09-25T21:46:09Z

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
| XRPUSDT | IDLE | 1.26 | 2.22 | 1.94 | 0.01 | 116796679.03 | 1.29 | n/a |
| ETHUSDT | IDLE | 0.45 | 0.81 | 0.62 | -0.0 | 333709566.88 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.36 | 0.65 | 0.44 | -0.01 | 694185624.59 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.62 | 4.42 | 1.09 | 0.08 | 1223411.85 | 6.81 | tvl≈162,005,824 |
| CCUSDT | IDLE | 1.74 | 7.48 | 3.67 | 0.13 | 827883.2 | 7.05 | no_map |
| HBARUSDT | IDLE | 1.84 | 3.46 | 1.47 | 0.0 | 925633.57 | 1.06 | empty_tvl |
| WUSDT | IDLE | 1.85 | 3.47 | 1.6 | 0.03 | 404378.96 | 10.7 | tvl≈1,840,714,311 |
| RIZEUSDT | IDLE | 1.43 | 21.14 | 15.81 | 0.02 | 113122.8 | 31.62 | no_map |
| EDELUSDT | IDLE | 2.63 | 4.68 | 3.82 | 0.02 | 183159.9 | 6.79 | no_map |
| ZBCNUSDT | IDLE | 1.76 | 3.9 | 3.47 | 0.05 | 255404.37 | 25.97 | n/a |
| QNTUSDT | IDLE | 1.03 | 4.28 | 2.42 | 0.09 | 572140.28 | 2.07 | n/a |
| CHIPUSDT | IDLE | 1.74 | 4.27 | 1.51 | -0.02 | 159014.19 | 18.47 | no_map |
| KITEUSDT | IDLE | 1.83 | 3.49 | 1.09 | 0.0 | 81317.5 | 12.1 | no_map |
| BIOUSDT | IDLE | 1.29 | 3.67 | 2.46 | 0.05 | 111514.67 | 6.15 | n/a |
| REDUSDT | IDLE | 0.98 | 2.35 | 1.47 | 0.08 | 136850.65 | 13.86 | tvl≈3,166,960 |
| RWAINCUSDT | IDLE | 0.72 | 2.63 | 0.7 | -0.11 | 15385.21 | 60.42 | no_map |
| TELUSDT | IDLE | 1.11 | 2.02 | 1.32 | -0.0 | 119019.51 | 24.36 | no_map |
| FLUIDUSDT | IDLE | 1.27 | 2.46 | 0.52 | 0.02 | 3356.58 | 21.65 | tvl≈2,582,407,344 |
| MNSRYUSDT | IDLE | 0.75 | 1.37 | 0.85 | 0.02 | 40914.78 | 7.63 | no_map |
| RWAUSDT | IDLE | 0.71 | 1.26 | 1.02 | -0.01 | 54762.63 | 44.25 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
