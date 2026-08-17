# Hulk DIGEST — 2026-08-17T22:08:17Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.31 | 0.56 | 0.34 | 0.01 | 12471503.65 | 2.0 | n/a |
| CHIPUSDT | IDLE | 0.97 | 4.24 | 3.28 | -0.02 | 333177.57 | 7.06 | no_map |
| EDELUSDT | IDLE | 1.94 | 3.69 | 1.27 | 0.01 | 66533.26 | 25.71 | no_map |
| CCUSDT | IDLE | 0.96 | 1.74 | 1.21 | -0.05 | 248738.84 | 6.62 | no_map |
| ZBCNUSDT | IDLE | 1.13 | 2.04 | 1.45 | 0.01 | 202965.15 | 14.54 | n/a |
| BIOUSDT | IDLE | 1.39 | 2.49 | 1.95 | 0.02 | 80037.46 | 4.06 | n/a |
| TELUSDT | IDLE | 2.63 | 5.93 | 2.45 | -0.03 | 136952.38 | 35.83 | no_map |
| PYTHUSDT | IDLE | 0.96 | 1.74 | 1.15 | 0.01 | 146877.18 | 5.17 | tvl≈88,507,149 |
| QAITUSDT | IDLE | 1.88 | 3.61 | 0.94 | -0.03 | 1000.03 | 46.08 | no_map |
| REDUSDT | IDLE | 1.16 | 2.11 | 1.37 | -0.01 | 58529.35 | 25.5 | tvl≈1,561,905 |
| WUSDT | IDLE | 0.73 | 1.31 | 0.96 | -0.03 | 135435.55 | 13.29 | tvl≈1,367,180,133 |
| RIZEUSDT | IDLE | 0.56 | 4.72 | 2.45 | 0.09 | 85444.62 | 47.76 | no_map |
| KITEUSDT | IDLE | 0.56 | 1.03 | 0.57 | -0.01 | 60541.7 | 14.05 | no_map |
| RWAINCUSDT | IDLE | 0.41 | 0.76 | 0.41 | -0.04 | 1098.95 | 58.58 | no_map |
| QNTUSDT | IDLE | 0.77 | 1.35 | 1.25 | 0.01 | 35418.74 | 3.52 | n/a |
| HBARUSDT | IDLE | 0.34 | 0.62 | 0.42 | 0.01 | 112750.92 | 1.52 | empty_tvl |
| FLUIDUSDT | IDLE | 0.62 | 1.24 | 0.0 | -0.02 | 772.33 | 22.39 | tvl≈2,318,816,392 |
| RWAUSDT | IDLE | 0.32 | 0.61 | 0.26 | 0.01 | 49630.97 | 17.26 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
