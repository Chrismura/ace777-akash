# Hulk DIGEST — 2026-08-22T12:41:22Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.0 | 0.1 | 216412194.45 | 1.32 | n/a |
| PYTHUSDT | IDLE | 1.62 | 7.83 | 1.24 | 0.05 | 51601769.39 | 1.97 | tvl≈110,752,782 |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.2 | 0.02 | 1259727.41 | 3.85 | empty_tvl |
| CCUSDT | IDLE | 1.59 | 8.38 | 3.05 | 0.15 | 776597.41 | 5.87 | no_map |
| WUSDT | IDLE | 1.56 | 6.27 | 3.74 | 0.0 | 576687.49 | 10.59 | tvl≈1,571,378,489 |
| ZBCNUSDT | IDLE | 2.22 | 5.77 | 3.94 | -0.01 | 335562.98 | 21.05 | n/a |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.65 | -0.1 | 603608.11 | 3.36 | no_map |
| KITEUSDT | IDLE | 2.69 | 6.37 | 0.92 | 0.03 | 84938.77 | 10.62 | no_map |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.02 | 78204.71 | 33.84 | no_map |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.83 | -0.04 | 239279.27 | 3.23 | n/a |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2408.77 | 67.45 | no_map |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.72 | 0.0 | 153262.93 | 10.71 | tvl≈2,031,082 |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.83 | -0.03 | 163538.59 | 42.51 | no_map |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | no_map |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.68 | -0.0 | 187678.46 | 6.22 | n/a |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.24 | -0.0 | 46780.16 | 46.13 | no_map |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.02 | 57803.0 | 24.4 | no_map |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.03 | 5705.21 | 23.73 | tvl≈2,552,552,396 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
