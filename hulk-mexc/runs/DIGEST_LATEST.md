# Hulk DIGEST — 2026-08-30T03:12:47Z

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
| XRPUSDT | IDLE | 0.41 | 0.76 | 0.46 | 0.01 | 16643364.82 | 2.15 | n/a |
| CHIPUSDT | IDLE | 1.24 | 3.9 | 1.38 | -0.05 | 822103.65 | 2.49 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.06 | 12.31 | 5.73 | -0.06 | 44845.55 | 62.31 | no_map |
| CCUSDT | IDLE | 1.32 | 3.18 | 0.85 | 0.08 | 270885.98 | 5.83 | no_map |
| PYTHUSDT | IDLE | 0.85 | 1.51 | 1.28 | -0.0 | 315567.73 | 2.1 | tvl≈108,869,783 |
| ZBCNUSDT | IDLE | 1.38 | 2.56 | 1.37 | -0.03 | 201275.08 | 15.78 | n/a |
| WUSDT | IDLE | 0.61 | 1.15 | 0.46 | -0.0 | 185647.32 | 7.66 | tvl≈1,545,716,193 |
| BIOUSDT | IDLE | 0.93 | 1.76 | 0.68 | -0.01 | 67181.6 | 3.62 | n/a |
| REDUSDT | IDLE | 0.85 | 1.52 | 1.21 | 0.01 | 76963.5 | 11.93 | tvl≈2,028,643 |
| KITEUSDT | IDLE | 0.67 | 1.7 | 1.66 | -0.0 | 68301.59 | 12.48 | no_map |
| EDELUSDT | IDLE | 0.24 | 4.42 | 1.55 | 0.08 | 121542.12 | 26.26 | no_map |
| TELUSDT | IDLE | 1.81 | 3.37 | 1.69 | -0.04 | 72286.47 | 17.78 | no_map |
| RWAINCUSDT | IDLE | 0.84 | 1.47 | 1.45 | -0.04 | 1577.44 | 96.13 | no_map |
| HBARUSDT | IDLE | 0.4 | 0.7 | 0.63 | -0.01 | 133555.95 | 1.33 | empty_tvl |
| FLUIDUSDT | IDLE | 0.9 | 1.61 | 1.24 | 0.01 | 1482.06 | 21.63 | tvl≈2,617,285,524 |
| QNTUSDT | IDLE | 0.58 | 1.14 | 0.11 | 0.01 | 31324.68 | 1.62 | n/a |
| RWAUSDT | IDLE | 0.76 | 1.4 | 0.81 | 0.01 | 54558.75 | 40.97 | no_map |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
