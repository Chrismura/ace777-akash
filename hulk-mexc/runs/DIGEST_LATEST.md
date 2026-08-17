# Hulk DIGEST — 2026-08-17T18:13:17Z

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
| XRPUSDT | IDLE | 0.62 | 1.13 | 0.72 | 0.0 | 13120900.39 | 1.0 | n/a |
| CHIPUSDT | IDLE | 1.73 | 7.43 | 6.92 | -0.01 | 336857.84 | 3.49 | no_map |
| EDELUSDT | IDLE | 3.14 | 5.59 | 4.56 | 0.02 | 64960.74 | 25.84 | no_map |
| ZBCNUSDT | IDLE | 2.34 | 4.67 | 0.02 | 0.02 | 188686.15 | 14.99 | n/a |
| REDUSDT | IDLE | 2.82 | 5.45 | 1.27 | -0.02 | 57896.11 | 18.55 | tvl≈1,540,264 |
| CCUSDT | IDLE | 1.69 | 2.99 | 2.65 | -0.04 | 245124.98 | 5.49 | no_map |
| RIZEUSDT | IDLE | 1.25 | 11.77 | 6.98 | 0.15 | 87322.89 | 46.99 | no_map |
| PYTHUSDT | IDLE | 1.11 | 2.05 | 1.17 | -0.01 | 160226.03 | 2.57 | tvl≈88,507,149 |
| WUSDT | IDLE | 0.73 | 1.28 | 1.26 | -0.03 | 147945.79 | 13.25 | tvl≈1,361,956,382 |
| QAITUSDT | IDLE | 1.57 | 2.87 | 1.8 | -0.01 | 806.65 | 62.04 | no_map |
| BIOUSDT | IDLE | 0.57 | 1.1 | 0.24 | 0.01 | 72955.49 | 8.1 | n/a |
| TELUSDT | IDLE | 2.07 | 3.8 | 2.28 | -0.03 | 119569.92 | 63.67 | no_map |
| FLUIDUSDT | IDLE | 2.07 | 3.61 | 3.49 | -0.03 | 751.15 | 22.46 | tvl≈2,317,815,153 |
| KITEUSDT | IDLE | 0.55 | 1.05 | 0.38 | -0.02 | 59595.45 | 17.25 | no_map |
| QNTUSDT | IDLE | 1.4 | 2.67 | 0.88 | 0.0 | 37233.29 | 5.24 | n/a |
| HBARUSDT | IDLE | 0.76 | 1.44 | 0.56 | 0.01 | 141378.44 | 1.52 | empty_tvl |
| RWAINCUSDT | IDLE | 0.3 | 0.52 | 0.52 | -0.03 | 1225.45 | 81.35 | no_map |
| RWAUSDT | IDLE | 0.5 | 0.96 | 0.26 | 0.01 | 49895.31 | 17.26 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
