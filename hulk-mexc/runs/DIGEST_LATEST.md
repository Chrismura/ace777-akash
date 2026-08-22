# Hulk DIGEST — 2026-08-22T11:14:26Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.97 | 0.0 | 51653154.03 | 2.08 | tvl≈113,478,518 |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.58 | 0.07 | 217914808.94 | 2.69 | n/a |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.72 | 0.11 | 811824.97 | 7.8 | no_map |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.75 | 0.0 | 1254110.13 | 3.89 | empty_tvl |
| WUSDT | IDLE | 1.56 | 6.27 | 3.74 | 0.02 | 584727.31 | 11.65 | tvl≈1,583,490,295 |
| ZBCNUSDT | IDLE | 2.33 | 5.93 | 5.05 | -0.04 | 400080.48 | 28.56 | n/a |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.15 | -0.1 | 644837.71 | 6.75 | no_map |
| EDELUSDT | IDLE | 2.8 | 4.93 | 4.48 | -0.05 | 78848.25 | 22.78 | no_map |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.74 | -0.04 | 238109.88 | 3.27 | n/a |
| KITEUSDT | IDLE | 1.88 | 4.3 | 1.66 | 0.04 | 73650.18 | 25.55 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.61 | -0.04 | 169391.39 | 42.87 | no_map |
| QAITUSDT | IDLE | 2.25 | 4.16 | 2.21 | 0.0 | 2497.35 | 63.67 | no_map |
| REDUSDT | IDLE | 0.49 | 6.02 | 5.14 | 0.03 | 154574.67 | 13.59 | tvl≈2,031,082 |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | -0.01 | 11311.88 | 59.83 | no_map |
| QNTUSDT | IDLE | 1.09 | 3.47 | 2.08 | -0.0 | 188712.61 | 9.38 | n/a |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.92 | 0.0 | 49263.56 | 46.44 | no_map |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.61 | tvl≈2,553,890,177 |
| RWAUSDT | IDLE | 1.03 | 1.8 | 1.69 | 0.01 | 57450.77 | 8.17 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
