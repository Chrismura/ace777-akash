# Hulk DIGEST — 2026-08-17T13:11:38Z

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
| XRPUSDT | IDLE | 0.38 | 0.69 | 0.49 | -0.0 | 11102817.68 | 1.0 | n/a |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 11.83 | 7.99 | 0.05 | 354916.17 | 16.56 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 25.22 | 13.3 | 0.23 | 75282.49 | 31.25 | no_map |
| CCUSDT | IDLE | 1.64 | 2.87 | 2.75 | -0.03 | 262717.57 | 9.65 | no_map |
| REDUSDT | IDLE | 2.32 | 4.16 | 3.16 | -0.05 | 56006.99 | 16.86 | tvl≈1,529,041 |
| EDELUSDT | IDLE | 2.37 | 4.66 | 0.49 | 0.07 | 60326.12 | 24.81 | no_map |
| PYTHUSDT | IDLE | 0.91 | 1.64 | 1.21 | -0.01 | 149967.72 | 2.56 | tvl≈88,917,837 |
| ZBCNUSDT | IDLE | 1.35 | 2.39 | 2.06 | 0.01 | 158775.51 | 64.9 | n/a |
| WUSDT | IDLE | 0.69 | 1.21 | 1.1 | -0.03 | 174411.48 | 8.37 | tvl≈1,361,115,442 |
| BIOUSDT | IDLE | 0.94 | 1.67 | 1.4 | -0.01 | 69877.85 | 4.06 | n/a |
| KITEUSDT | IDLE | 0.92 | 1.73 | 0.74 | -0.02 | 53543.12 | 13.99 | no_map |
| RWAINCUSDT | IDLE | 1.44 | 2.56 | 2.15 | -0.04 | 2000.6 | 58.17 | no_map |
| TELUSDT | IDLE | 1.94 | 3.6 | 1.84 | -0.01 | 92986.68 | 41.64 | no_map |
| QAITUSDT | IDLE | 1.18 | 2.1 | 1.68 | -0.0 | 1694.23 | 61.12 | no_map |
| HBARUSDT | IDLE | 0.86 | 1.62 | 0.72 | 0.01 | 119529.54 | 1.52 | empty_tvl |
| QNTUSDT | IDLE | 1.25 | 2.5 | 0.0 | -0.01 | 33256.22 | 35.09 | n/a |
| FLUIDUSDT | IDLE | 1.01 | 1.85 | 1.14 | -0.02 | 882.14 | 20.39 | tvl≈2,317,055,720 |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.26 | 0.01 | 49482.84 | 17.36 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
