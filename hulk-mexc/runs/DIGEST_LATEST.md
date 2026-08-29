# Hulk DIGEST — 2026-08-29T08:08:57Z

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
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.74 | 12.93 | 7.41 | 0.03 | 1247525.57 | 2.43 | no_map |
| XRPUSDT | IDLE | 0.66 | 1.17 | 0.94 | -0.03 | 43066043.93 | 2.17 | n/a |
| PYTHUSDT | IDLE | 1.71 | 2.98 | 2.88 | -0.04 | 500827.07 | 2.15 | tvl≈107,084,942 |
| WUSDT | IDLE | 1.24 | 2.18 | 2.0 | -0.03 | 209646.45 | 13.17 | tvl≈1,517,533,932 |
| KITEUSDT | IDLE | 1.59 | 2.85 | 2.15 | -0.01 | 69165.16 | 11.84 | no_map |
| REDUSDT | IDLE | 1.44 | 2.82 | 0.62 | 0.01 | 60932.63 | 11.89 | tvl≈2,019,461 |
| CCUSDT | IDLE | 0.79 | 1.52 | 0.34 | -0.01 | 213277.65 | 11.67 | no_map |
| HBARUSDT | IDLE | 0.75 | 1.32 | 1.24 | -0.04 | 461301.87 | 1.34 | empty_tvl |
| EDELUSDT | IDLE | 1.0 | 3.69 | 3.19 | -0.11 | 90084.03 | 19.38 | no_map |
| ZBCNUSDT | IDLE | 0.53 | 1.4 | 0.53 | -0.06 | 180573.73 | 10.71 | n/a |
| RIZEUSDT | IDLE | 1.56 | 3.21 | 1.41 | -0.05 | 29584.13 | 58.36 | no_map |
| BIOUSDT | IDLE | 0.76 | 1.34 | 1.22 | -0.04 | 81818.53 | 3.63 | n/a |
| RWAINCUSDT | IDLE | 0.95 | 1.66 | 1.63 | 0.01 | 3548.47 | 88.35 | no_map |
| QAITUSDT | IDLE | 0.24 | 2.07 | 1.47 | -0.03 | 84066.77 | 66.99 | no_map |
| TELUSDT | IDLE | 0.8 | 1.44 | 1.08 | -0.05 | 79925.84 | 40.1 | no_map |
| QNTUSDT | IDLE | 0.62 | 1.08 | 1.07 | -0.03 | 40666.8 | 1.64 | n/a |
| RWAUSDT | IDLE | 0.61 | 1.16 | 0.41 | 0.01 | 55511.12 | 8.22 | no_map |
| FLUIDUSDT | IDLE | 0.25 | 0.44 | 0.44 | -0.05 | 3704.21 | 21.65 | tvl≈2,598,605,640 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
