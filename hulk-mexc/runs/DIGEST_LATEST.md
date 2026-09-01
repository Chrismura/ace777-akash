# Hulk DIGEST — 2026-09-01T07:23:18Z

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
| XRPUSDT | IDLE | 1.04 | 1.96 | 0.8 | 0.01 | 28727749.05 | 2.17 | n/a |
| BTCUSDT | IDLE | 0.68 | 1.28 | 0.55 | 0.01 | 550657481.09 | 0.02 | no_map |
| ETHUSDT | IDLE | 0.64 | 1.21 | 0.4 | 0.01 | 287335942.54 | 0.04 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 29.11 | 19.09 | -0.03 | 171401.65 | 17.06 | no_map |
| CHIPUSDT | IDLE | 2.56 | 6.47 | 0.17 | 0.01 | 332125.81 | 4.96 | no_map |
| PYTHUSDT | IDLE | 1.42 | 3.58 | 1.33 | 0.07 | 487520.93 | 39.42 | tvl≈113,741,883 |
| WUSDT | IDLE | 2.18 | 4.22 | 0.99 | 0.02 | 225758.5 | 14.58 | tvl≈1,542,460,139 |
| CCUSDT | IDLE | 1.12 | 2.01 | 1.48 | 0.02 | 384544.34 | 9.82 | no_map |
| ZBCNUSDT | IDLE | 1.39 | 2.49 | 1.87 | 0.04 | 193713.5 | 19.44 | n/a |
| RWAINCUSDT | IDLE | 1.81 | 3.21 | 2.77 | -0.03 | 4431.97 | 23.74 | no_map |
| RWAUSDT | IDLE | 2.09 | 6.63 | 6.15 | 0.07 | 63860.55 | 22.56 | no_map |
| REDUSDT | IDLE | 1.16 | 2.26 | 0.39 | -0.03 | 57472.86 | 19.53 | tvl≈1,986,510 |
| KITEUSDT | IDLE | 1.0 | 1.81 | 1.31 | -0.03 | 68510.64 | 10.99 | no_map |
| RIZEUSDT | IDLE | 1.29 | 4.55 | 0.39 | -0.05 | 36208.61 | 60.69 | no_map |
| BIOUSDT | IDLE | 0.73 | 1.33 | 0.86 | -0.01 | 62602.46 | 3.78 | n/a |
| HBARUSDT | IDLE | 1.06 | 2.02 | 0.62 | 0.0 | 235005.8 | 1.34 | empty_tvl |
| TELUSDT | IDLE | 1.58 | 3.07 | 0.63 | 0.0 | 82873.78 | 40.31 | no_map |
| QNTUSDT | IDLE | 0.47 | 0.83 | 0.73 | 0.0 | 49861.9 | 3.27 | n/a |
| FLUIDUSDT | IDLE | 0.46 | 0.85 | 0.53 | 0.01 | 1149.26 | 19.64 | tvl≈2,610,055,231 |
| MNSRYUSDT | IDLE | 0.48 | 0.86 | 0.65 | -0.0 | 28870.34 | 47.35 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
