# Hulk DIGEST — 2026-08-22T12:05:25Z

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
| PYTHUSDT | IDLE | 1.73 | 7.83 | 5.05 | 0.01 | 51609012.15 | 4.09 | tvl≈110,752,782 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 14.26 | 7.99 | 0.11 | 215561630.46 | 1.34 | n/a |
| HBARUSDT | IDLE | 1.28 | 4.63 | 2.73 | 0.03 | 1254423.32 | 1.29 | empty_tvl |
| CCUSDT | IDLE | 1.64 | 8.38 | 5.02 | 0.13 | 775456.98 | 6.85 | no_map |
| WUSDT | IDLE | 1.56 | 6.27 | 3.75 | 0.02 | 579697.34 | 10.59 | tvl≈1,560,017,487 |
| ZBCNUSDT | IDLE | 2.27 | 5.77 | 4.96 | -0.04 | 380935.67 | 33.25 | n/a |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 1.12 | -0.09 | 618970.27 | 3.34 | no_map |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.39 | 0.04 | 82605.08 | 10.55 | no_map |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.2 | -0.04 | 78185.81 | 22.78 | no_map |
| BIOUSDT | IDLE | 0.79 | 5.65 | 1.95 | -0.02 | 240724.32 | 6.42 | n/a |
| TELUSDT | IDLE | 2.19 | 5.61 | 4.45 | -0.03 | 165074.67 | 16.04 | no_map |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2386.65 | 63.29 | no_map |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.7 | 0.03 | 153540.17 | 20.35 | tvl≈2,031,082 |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | no_map |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.55 | 0.01 | 188369.54 | 7.78 | n/a |
| RIZEUSDT | IDLE | 0.48 | 1.91 | 0.75 | -0.05 | 48057.16 | 46.44 | no_map |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57851.92 | 24.46 | no_map |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 22.3 | tvl≈2,551,694,186 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
