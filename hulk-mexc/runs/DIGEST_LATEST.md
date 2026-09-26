# Hulk DIGEST — 2026-09-26T05:28:45Z

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
| XRPUSDT | IDLE | 1.14 | 2.01 | 1.84 | 0.01 | 109810299.25 | 1.29 | n/a |
| ETHUSDT | IDLE | 0.29 | 0.54 | 0.29 | 0.0 | 299698314.67 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.22 | 0.41 | 0.22 | -0.0 | 648790136.8 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.31 | 3.33 | 1.95 | 0.08 | 1194990.83 | 2.72 | tvl≈165,199,262 |
| CCUSDT | IDLE | 1.23 | 5.0 | 2.55 | 0.15 | 926562.76 | 6.82 | no_map |
| HBARUSDT | IDLE | 1.28 | 2.24 | 2.08 | 0.02 | 883137.72 | 1.07 | empty_tvl |
| QNTUSDT | IDLE | 2.4 | 7.25 | 5.15 | 0.03 | 537221.64 | 9.03 | n/a |
| WUSDT | IDLE | 1.46 | 2.68 | 2.0 | 0.06 | 462611.83 | 10.61 | tvl≈1,829,494,075 |
| ZBCNUSDT | IDLE | 1.52 | 3.39 | 2.67 | 0.02 | 226028.55 | 8.56 | n/a |
| CHIPUSDT | IDLE | 1.82 | 4.65 | 3.87 | 0.05 | 148368.26 | 18.49 | no_map |
| KITEUSDT | IDLE | 1.9 | 5.34 | 1.76 | 0.09 | 78596.71 | 8.01 | no_map |
| REDUSDT | IDLE | 1.76 | 3.38 | 2.28 | 0.06 | 74781.09 | 13.43 | tvl≈3,162,950 |
| BIOUSDT | IDLE | 1.04 | 2.69 | 2.44 | 0.06 | 111630.02 | 3.08 | n/a |
| EDELUSDT | IDLE | 0.93 | 1.64 | 1.48 | -0.01 | 169996.73 | 40.79 | no_map |
| RIZEUSDT | IDLE | 0.17 | 2.21 | 0.8 | -0.16 | 77348.37 | 38.89 | no_map |
| TELUSDT | IDLE | 0.77 | 1.35 | 1.21 | 0.01 | 116694.0 | 12.27 | no_map |
| RWAINCUSDT | IDLE | 0.32 | 0.71 | 0.71 | -0.1 | 12751.69 | 60.88 | no_map |
| FLUIDUSDT | IDLE | 1.05 | 1.83 | 1.79 | 0.0 | 3437.87 | 21.76 | tvl≈2,581,723,607 |
| RWAUSDT | IDLE | 0.49 | 0.89 | 0.59 | -0.01 | 53104.89 | 14.78 | no_map |
| MNSRYUSDT | IDLE | 0.47 | 0.91 | 0.15 | 0.01 | 40971.03 | 8.92 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
