# Hulk DIGEST — 2026-08-22T11:39:04Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.9 | 0.01 | 51618346.76 | 4.1 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.33 | 0.08 | 216899254.6 | 2.68 | n/a |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.47 | 0.13 | 793605.59 | 8.54 | no_map |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.31 | 0.01 | 1258591.75 | 6.45 | empty_tvl |
| WUSDT | IDLE | 1.55 | 6.27 | 3.66 | 0.02 | 585214.33 | 11.65 | tvl≈1,560,017,487 |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.32 | -0.03 | 388951.43 | 24.19 | n/a |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.82 | -0.11 | 636754.79 | 3.36 | no_map |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.45 | -0.04 | 243020.69 | 3.22 | n/a |
| EDELUSDT | IDLE | 2.77 | 4.93 | 4.04 | -0.04 | 79063.96 | 101.87 | no_map |
| KITEUSDT | IDLE | 1.92 | 4.64 | 0.0 | 0.04 | 73419.31 | 13.37 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.61 | -0.03 | 167275.43 | 37.5 | no_map |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2491.52 | 67.45 | no_map |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.05 | 0.04 | 155240.47 | 9.85 | tvl≈2,031,082 |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10923.76 | 32.68 | no_map |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.92 | -0.03 | 48690.21 | 22.39 | no_map |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.97 | -0.0 | 188527.17 | 4.68 | n/a |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.33 | tvl≈2,551,694,186 |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57704.98 | 24.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
