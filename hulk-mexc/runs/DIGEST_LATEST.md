# Hulk DIGEST — 2026-08-18T02:19:08Z

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
| XRPUSDT | IDLE | 0.57 | 1.0 | 0.98 | -0.0 | 11970778.97 | 1.01 | n/a |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 28.73 | 18.68 | -0.02 | 8218.44 | 61.66 | no_map |
| CHIPUSDT | IDLE | 1.18 | 5.74 | 2.65 | -0.01 | 335282.67 | 3.58 | no_map |
| PYTHUSDT | IDLE | 1.41 | 2.5 | 2.13 | -0.01 | 147269.17 | 2.62 | tvl≈87,844,149 |
| CCUSDT | IDLE | 0.95 | 1.89 | 0.08 | -0.05 | 279208.52 | 9.88 | no_map |
| REDUSDT | IDLE | 1.85 | 3.65 | 0.75 | 0.03 | 56168.11 | 11.3 | tvl≈1,581,082 |
| RIZEUSDT | IDLE | 1.07 | 8.14 | 7.26 | 0.04 | 82313.28 | 27.66 | no_map |
| EDELUSDT | IDLE | 1.8 | 3.17 | 2.82 | -0.02 | 65969.93 | 52.56 | no_map |
| WUSDT | IDLE | 1.18 | 2.1 | 1.77 | -0.05 | 134153.59 | 14.68 | tvl≈1,370,709,687 |
| TELUSDT | IDLE | 2.57 | 5.85 | 1.89 | -0.04 | 132774.77 | 42.8 | no_map |
| BIOUSDT | IDLE | 1.15 | 2.02 | 1.9 | 0.0 | 82342.07 | 4.12 | n/a |
| ZBCNUSDT | IDLE | 0.57 | 1.01 | 0.87 | -0.0 | 225578.81 | 11.44 | n/a |
| KITEUSDT | IDLE | 1.11 | 1.93 | 1.88 | -0.02 | 60065.81 | 15.33 | no_map |
| RWAINCUSDT | IDLE | 0.41 | 0.76 | 0.41 | -0.03 | 1057.17 | 58.58 | no_map |
| HBARUSDT | IDLE | 0.41 | 0.72 | 0.7 | 0.01 | 122770.18 | 1.52 | empty_tvl |
| QNTUSDT | IDLE | 0.71 | 1.24 | 1.17 | 0.01 | 35125.26 | 8.83 | n/a |
| FLUIDUSDT | IDLE | 0.7 | 1.24 | 1.12 | -0.03 | 632.41 | 22.69 | tvl≈2,321,887,885 |
| RWAUSDT | IDLE | 0.32 | 0.61 | 0.17 | 0.01 | 49284.83 | 17.24 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
