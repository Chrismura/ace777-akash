# Hulk DIGEST — 2026-08-26T06:44:42Z

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
| PYTHUSDT | IDLE | 2.51 | 5.36 | 0.24 | 0.04 | 2889788.0 | 1.88 | tvl≈117,898,207 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 73.61 | 38.9 | 0.09 | 62881.97 | 63.94 | no_map |
| XRPUSDT | IDLE | 0.94 | 1.75 | 0.88 | -0.05 | 59000167.16 | 2.09 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.93 | 31.72 | 12.13 | 0.12 | 16231.29 | 21.11 | tvl≈2,590,725,714 |
| WUSDT | IDLE | 2.39 | 4.58 | 1.35 | -0.01 | 295953.37 | 16.6 | tvl≈1,560,036,122 |
| CHIPUSDT | IDLE | 2.09 | 4.31 | 2.55 | -0.04 | 326192.19 | 6.24 | no_map |
| CCUSDT | IDLE | 1.07 | 2.08 | 1.66 | -0.05 | 501758.1 | 10.13 | no_map |
| BIOUSDT | IDLE | 2.33 | 4.1 | 3.7 | -0.05 | 97315.53 | 10.58 | n/a |
| EDELUSDT | IDLE | 0.91 | 12.46 | 9.63 | 0.02 | 159061.58 | 28.24 | no_map |
| REDUSDT | IDLE | 1.64 | 3.94 | 3.64 | -0.01 | 75993.37 | 11.41 | tvl≈2,111,212 |
| KITEUSDT | IDLE | 1.82 | 3.41 | 1.49 | -0.01 | 60934.29 | 11.37 | no_map |
| ZBCNUSDT | IDLE | 1.44 | 2.78 | 0.73 | -0.02 | 156885.83 | 13.64 | n/a |
| HBARUSDT | IDLE | 0.59 | 1.08 | 0.65 | -0.05 | 536609.18 | 1.28 | empty_tvl |
| QAITUSDT | IDLE | 1.64 | 3.03 | 1.69 | 0.04 | 9314.68 | 169.08 | no_map |
| TELUSDT | IDLE | 1.19 | 2.33 | 0.27 | -0.02 | 93744.95 | 10.88 | no_map |
| QNTUSDT | IDLE | 0.63 | 1.19 | 0.53 | -0.04 | 130538.69 | 4.73 | n/a |
| RWAUSDT | IDLE | 1.04 | 1.84 | 1.56 | -0.05 | 56752.57 | 33.42 | no_map |
| RWAINCUSDT | IDLE | 0.78 | 1.37 | 1.3 | -0.01 | 1277.4 | 131.05 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
