# Hulk DIGEST — 2026-08-22T11:26:51Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.74 | -0.0 | 51635133.17 | 2.07 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.8 | 0.07 | 217270557.35 | 1.35 | n/a |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.76 | 0.11 | 809397.1 | 5.2 | no_map |
| HBARUSDT | IDLE | 1.48 | 5.26 | 3.87 | 0.0 | 1258926.6 | 5.19 | empty_tvl |
| WUSDT | IDLE | 1.57 | 6.27 | 4.28 | 0.01 | 582712.58 | 14.9 | tvl≈1,560,017,487 |
| ZBCNUSDT | IDLE | 2.32 | 5.93 | 4.92 | -0.04 | 396021.1 | 19.67 | n/a |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.51 | -0.11 | 640624.46 | 3.39 | no_map |
| EDELUSDT | IDLE | 2.77 | 4.93 | 4.04 | -0.05 | 78932.52 | 22.78 | no_map |
| BIOUSDT | IDLE | 0.95 | 6.64 | 3.43 | -0.05 | 239111.1 | 3.26 | n/a |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.75 | 5.92 | -0.04 | 168417.92 | 10.75 | no_map |
| KITEUSDT | IDLE | 1.83 | 4.3 | 0.91 | 0.03 | 73665.0 | 11.74 | no_map |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | no_map |
| REDUSDT | IDLE | 0.49 | 6.02 | 5.01 | 0.02 | 154745.13 | 12.69 | tvl≈2,031,082 |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | 0.0 | 11178.17 | 38.12 | no_map |
| QNTUSDT | IDLE | 1.11 | 3.47 | 2.63 | -0.01 | 188607.0 | 7.86 | n/a |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.85 | -0.02 | 48817.18 | 46.44 | no_map |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.66 | tvl≈2,551,694,186 |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57505.67 | 16.33 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
