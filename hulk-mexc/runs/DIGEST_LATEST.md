# Hulk DIGEST — 2026-09-25T14:44:29Z

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
| XRPUSDT | IDLE | 2.66 | 5.7 | 2.8 | 0.04 | 113620207.73 | 1.89 | n/a |
| ETHUSDT | IDLE | 1.46 | 2.63 | 1.95 | 0.0 | 389344391.3 | 0.33 | no_map |
| BTCUSDT | IDLE | 1.36 | 2.46 | 1.69 | -0.01 | 751631420.95 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.75 | 4.19 | 1.45 | 0.07 | 1211904.29 | 9.75 | tvl≈160,370,764 |
| HBARUSDT | IDLE | 2.46 | 4.48 | 2.99 | -0.01 | 1009119.71 | 1.07 | empty_tvl |
| CCUSDT | IDLE | 1.94 | 7.48 | 2.19 | 0.12 | 788701.8 | 12.16 | no_map |
| ZBCNUSDT | IDLE | 4.01 | 9.17 | 3.61 | 0.05 | 194191.25 | 24.68 | n/a |
| RIZEUSDT | IDLE | 1.44 | 32.62 | 23.12 | 0.54 | 127581.24 | 53.7 | no_map |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 10.33 | 5.4 | 0.06 | 117043.22 | 9.32 | n/a |
| WUSDT | IDLE | 2.15 | 3.97 | 2.21 | 0.01 | 358575.69 | 7.57 | tvl≈1,825,056,864 |
| QNTUSDT | IDLE | 1.22 | 8.52 | 5.92 | 0.17 | 574980.41 | 8.45 | n/a |
| REDUSDT | IDLE | 2.07 | 5.16 | 1.74 | 0.07 | 135723.94 | 19.39 | tvl≈3,104,735 |
| KITEUSDT | IDLE | 2.0 | 3.8 | 1.4 | -0.02 | 72875.98 | 9.96 | no_map |
| CHIPUSDT | IDLE | 1.57 | 6.93 | 1.83 | 0.15 | 127419.63 | 22.35 | no_map |
| EDELUSDT | IDLE | 0.49 | 5.36 | 2.18 | 0.09 | 219778.09 | 57.4 | no_map |
| TELUSDT | IDLE | 1.69 | 3.11 | 1.78 | -0.02 | 124115.37 | 42.21 | no_map |
| RWAINCUSDT | IDLE | 0.81 | 3.53 | 2.22 | 0.05 | 23636.95 | 106.52 | no_map |
| MNSRYUSDT | IDLE | 1.28 | 2.42 | 0.92 | 0.02 | 42826.25 | 20.44 | no_map |
| FLUIDUSDT | IDLE | 1.39 | 2.49 | 1.97 | 0.03 | 915.96 | 21.71 | tvl≈2,583,580,857 |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.73 | -0.0 | 57915.81 | 7.31 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
