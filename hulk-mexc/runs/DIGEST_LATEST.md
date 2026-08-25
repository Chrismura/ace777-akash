# Hulk DIGEST — 2026-08-25T23:45:01Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 6.92 | 5.7 | 0.0 | 2225222.36 | 2.01 | tvl≈116,225,421 |
| XRPUSDT | IDLE | 2.3 | 5.37 | 3.26 | -0.03 | 74961704.72 | 1.39 | n/a |
| HBARUSDT | IDLE | 2.11 | 4.2 | 3.3 | -0.02 | 799088.07 | 1.28 | empty_tvl |
| CCUSDT | IDLE | 1.8 | 3.74 | 1.26 | -0.03 | 531086.35 | 5.82 | no_map |
| CHIPUSDT | IDLE | 1.76 | 5.18 | 1.08 | -0.01 | 452360.29 | 6.23 | no_map |
| WUSDT | IDLE | 2.29 | 4.36 | 2.72 | -0.02 | 344563.64 | 8.59 | tvl≈1,568,751,203 |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.04 | 7.38 | 6.07 | -0.02 | 80848.42 | 11.51 | tvl≈2,151,186 |
| BIOUSDT | IDLE | 3.12 | 5.87 | 2.47 | -0.0 | 113526.92 | 10.29 | n/a |
| RIZEUSDT | IDLE | 3.48 | 7.26 | 3.12 | 0.03 | 50408.33 | 34.83 | no_map |
| ZBCNUSDT | IDLE | 2.19 | 3.85 | 3.55 | -0.01 | 184619.5 | 18.66 | n/a |
| EDELUSDT | IDLE | 1.09 | 15.51 | 13.13 | -0.03 | 164417.59 | 60.95 | no_map |
| KITEUSDT | IDLE | 2.4 | 4.57 | 2.24 | -0.02 | 61893.52 | 14.3 | no_map |
| QAITUSDT | IDLE | 2.07 | 5.67 | 0.85 | 0.04 | 12771.48 | 55.86 | no_map |
| FLUIDUSDT | IDLE | 2.13 | 3.96 | 2.03 | -0.02 | 2037.2 | 21.59 | tvl≈2,580,954,688 |
| QNTUSDT | IDLE | 1.17 | 2.13 | 1.46 | -0.02 | 133061.18 | 1.58 | n/a |
| RWAINCUSDT | IDLE | 0.34 | 0.6 | 0.6 | -0.01 | 2546.77 | 25.08 | no_map |
| RWAUSDT | IDLE | 0.92 | 1.65 | 1.3 | -0.03 | 56761.74 | 8.21 | no_map |
| TELUSDT | IDLE | 1.28 | 2.46 | 0.66 | -0.04 | 93946.95 | 66.08 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
