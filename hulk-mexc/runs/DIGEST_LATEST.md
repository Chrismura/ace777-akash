# Hulk DIGEST — 2026-09-11T23:20:52Z

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
| RIZEUSDT | IDLE | 1.59 | 108.76 | 44.71 | 0.67 | 218910.33 | 122.83 | no_map |
| ETHUSDT | IDLE | 1.19 | 2.5 | 2.09 | 0.03 | 656035490.09 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.82 | 1.67 | 0.99 | 0.01 | 54808773.86 | 2.95 | n/a |
| BTCUSDT | IDLE | 0.45 | 0.83 | 0.52 | 0.01 | 596258911.05 | 0.0 | no_map |
| EDELUSDT | IDLE | 3.14 | 8.94 | 3.08 | 0.04 | 166255.07 | 26.49 | no_map |
| PYTHUSDT | IDLE | 1.97 | 3.73 | 2.4 | -0.02 | 408725.85 | 1.97 | tvl≈114,765,176 |
| CCUSDT | IDLE | 1.25 | 2.28 | 1.51 | -0.0 | 435019.84 | 8.22 | no_map |
| ZBCNUSDT | IDLE | 2.1 | 3.81 | 2.63 | 0.01 | 196469.38 | 23.9 | n/a |
| WUSDT | IDLE | 1.7 | 3.24 | 2.39 | 0.01 | 200274.71 | 7.31 | tvl≈1,495,834,373 |
| CHIPUSDT | IDLE | 1.74 | 4.93 | 3.06 | -0.0 | 139887.79 | 12.81 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.05 | 3.9 | 0.02 | 14426.63 | 5.5 | no_map |
| BIOUSDT | IDLE | 1.07 | 1.94 | 1.31 | 0.01 | 78877.81 | 4.01 | n/a |
| REDUSDT | IDLE | 1.15 | 2.27 | 0.65 | 0.05 | 63782.02 | 18.05 | tvl≈2,299,900 |
| TELUSDT | IDLE | 2.15 | 4.27 | 3.03 | -0.02 | 103879.81 | 40.45 | no_map |
| KITEUSDT | IDLE | 0.74 | 1.35 | 0.93 | -0.0 | 59322.52 | 10.18 | no_map |
| HBARUSDT | IDLE | 0.66 | 1.2 | 0.74 | -0.01 | 257210.34 | 1.35 | empty_tvl |
| QNTUSDT | IDLE | 1.56 | 2.77 | 2.34 | -0.03 | 46639.47 | 6.34 | n/a |
| FLUIDUSDT | IDLE | 1.49 | 2.66 | 2.19 | 0.04 | 1265.76 | 21.67 | tvl≈2,665,499,160 |
| RWAUSDT | IDLE | 0.47 | 0.9 | 0.22 | 0.03 | 53178.02 | 7.44 | no_map |
| MNSRYUSDT | IDLE | 0.47 | 0.85 | 0.64 | 0.01 | 35665.09 | 26.37 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
