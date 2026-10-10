# Hulk DIGEST — 2026-10-10T19:01:23Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 8.42 | 6.19 | 0.03 | 1220862.14 | 7.31 | tvl≈1,653,273,745 |
| ETHUSDT | IDLE | 0.41 | 0.8 | 0.18 | 0.01 | 92261637.23 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.39 | 0.7 | 0.52 | 0.01 | 14397648.55 | 2.14 | n/a |
| BTCUSDT | IDLE | 0.24 | 0.46 | 0.15 | 0.01 | 175833056.92 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.83 | 5.17 | 3.28 | -0.0 | 1135812.68 | 4.94 | n/a |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.37 | 24.51 | 1.9 | 0.26 | 157847.34 | 20.46 | no_map |
| PYTHUSDT | IDLE | 1.24 | 2.34 | 0.94 | -0.02 | 831695.61 | 1.27 | tvl≈177,352,946 |
| CCUSDT | IDLE | 1.49 | 2.64 | 2.24 | -0.05 | 332517.3 | 9.3 | no_map |
| EDELUSDT | IDLE | 1.66 | 3.39 | 2.23 | -0.05 | 224187.21 | 7.85 | no_map |
| BIOUSDT | IDLE | 1.57 | 2.95 | 1.25 | 0.05 | 88283.32 | 6.84 | n/a |
| RWAINCUSDT | IDLE | 2.23 | 4.24 | 1.45 | -0.03 | 9591.46 | 63.87 | no_map |
| ZBCNUSDT | IDLE | 1.06 | 1.96 | 1.01 | 0.0 | 201468.23 | 25.76 | n/a |
| KITEUSDT | IDLE | 1.19 | 3.16 | 1.84 | 0.09 | 71786.52 | 8.48 | no_map |
| HBARUSDT | IDLE | 0.88 | 1.55 | 1.44 | 0.02 | 341238.65 | 5.42 | empty_tvl |
| TELUSDT | IDLE | 2.0 | 3.63 | 2.52 | -0.03 | 131711.59 | 44.87 | no_map |
| REDUSDT | IDLE | 0.66 | 1.21 | 0.79 | 0.03 | 54556.81 | 8.63 | tvl≈3,764,014 |
| RIZEUSDT | IDLE | 0.5 | 1.1 | 1.07 | -0.01 | 43476.83 | 27.92 | no_map |
| FLUIDUSDT | IDLE | 1.43 | 2.85 | 0.02 | 0.03 | 14842.99 | 20.92 | tvl≈2,429,031,451 |
| RWAUSDT | IDLE | 0.4 | 0.71 | 0.63 | 0.0 | 54333.73 | 15.75 | no_map |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.14 | 0.0 | 38439.71 | 10.82 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
