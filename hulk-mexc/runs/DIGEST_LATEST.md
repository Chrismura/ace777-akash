# Hulk DIGEST — 2026-08-30T23:15:04Z

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
| XRPUSDT | IDLE | 2.12 | 3.72 | 3.45 | -0.01 | 25845942.61 | 2.89 | n/a |
| ETHUSDT | IDLE | 1.29 | 2.27 | 2.09 | 0.0 | 260551402.11 | 0.41 | no_map |
| BTCUSDT | IDLE | 0.68 | 1.2 | 1.03 | 0.0 | 308907126.24 | 0.0 | no_map |
| CHIPUSDT | IDLE | 2.2 | 5.82 | 4.81 | -0.06 | 565502.24 | 5.23 | no_map |
| PYTHUSDT | IDLE | 2.87 | 5.09 | 4.31 | 0.0 | 429208.87 | 2.08 | tvl≈109,675,290 |
| WUSDT | IDLE | 2.0 | 3.55 | 2.95 | 0.02 | 236374.87 | 10.77 | tvl≈1,531,052,661 |
| ZBCNUSDT | IDLE | 1.66 | 3.74 | 2.19 | -0.05 | 208261.75 | 15.35 | n/a |
| BIOUSDT | IDLE | 2.06 | 3.66 | 3.02 | -0.02 | 85771.07 | 3.71 | n/a |
| EDELUSDT | IDLE | 2.18 | 6.23 | 3.13 | 0.07 | 76133.56 | 49.67 | no_map |
| KITEUSDT | IDLE | 1.92 | 3.4 | 2.91 | -0.05 | 62443.69 | 8.92 | no_map |
| RIZEUSDT | IDLE | 1.79 | 5.01 | 3.38 | -0.06 | 42533.57 | 39.55 | no_map |
| CCUSDT | IDLE | 0.92 | 1.78 | 0.39 | 0.01 | 229318.19 | 7.57 | no_map |
| REDUSDT | IDLE | 1.29 | 2.49 | 0.57 | 0.0 | 62659.82 | 14.62 | tvl≈2,002,827 |
| TELUSDT | IDLE | 2.17 | 3.81 | 3.56 | 0.01 | 88296.05 | 35.15 | no_map |
| RWAINCUSDT | IDLE | 1.65 | 3.05 | 1.64 | 0.02 | 1676.0 | 83.87 | no_map |
| HBARUSDT | IDLE | 1.35 | 2.38 | 2.18 | -0.01 | 172000.83 | 1.34 | empty_tvl |
| QNTUSDT | IDLE | 1.26 | 2.21 | 2.05 | -0.01 | 37086.64 | 3.29 | n/a |
| FLUIDUSDT | IDLE | 1.29 | 2.25 | 2.2 | 0.01 | 3330.5 | 22.63 | tvl≈2,635,474,435 |
| RWAUSDT | IDLE | 0.42 | 0.81 | 0.16 | 0.02 | 51655.71 | 16.1 | no_map |
| MNSRYUSDT | IDLE | 0.49 | 0.87 | 0.77 | 0.0 | 31897.31 | 30.88 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
