# Hulk DIGEST — 2026-09-01T20:26:53Z

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
| XRPUSDT | IDLE | 1.78 | 3.21 | 2.27 | -0.03 | 33495445.47 | 1.48 | n/a |
| ETHUSDT | IDLE | 1.6 | 2.98 | 1.43 | -0.02 | 326497227.59 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.22 | 2.29 | 0.99 | -0.02 | 535601419.14 | 0.0 | no_map |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 10.09 | 0.22 | 0.17 | 578428.49 | 4.41 | no_map |
| PYTHUSDT | IDLE | 2.06 | 3.94 | 1.25 | 0.03 | 647198.83 | 1.98 | tvl≈113,597,849 |
| ZBCNUSDT | IDLE | 3.45 | 6.37 | 3.48 | 0.02 | 201497.94 | 2.13 | n/a |
| CCUSDT | IDLE | 1.72 | 3.62 | 3.1 | -0.09 | 350079.32 | 11.42 | no_map |
| WUSDT | IDLE | 1.7 | 3.61 | 0.26 | 0.08 | 360228.3 | 15.2 | tvl≈1,518,936,260 |
| REDUSDT | IDLE | 2.08 | 6.24 | 4.94 | 0.06 | 109740.23 | 13.34 | tvl≈2,090,812 |
| RIZEUSDT | IDLE | 2.6 | 4.92 | 2.85 | -0.05 | 44359.93 | 71.98 | no_map |
| BIOUSDT | IDLE | 1.81 | 3.31 | 2.1 | -0.03 | 70736.21 | 3.89 | n/a |
| KITEUSDT | IDLE | 1.55 | 3.03 | 0.51 | 0.04 | 69030.28 | 20.19 | no_map |
| EDELUSDT | IDLE | 0.94 | 7.1 | 4.91 | -0.04 | 171940.38 | 63.61 | no_map |
| TELUSDT | IDLE | 2.83 | 5.08 | 3.9 | -0.06 | 94693.01 | 60.72 | no_map |
| RWAINCUSDT | IDLE | 1.4 | 2.8 | 0.0 | -0.0 | 6712.65 | 11.59 | no_map |
| FLUIDUSDT | IDLE | 2.52 | 4.41 | 4.22 | -0.03 | 129.84 | 21.04 | tvl≈2,574,734,472 |
| HBARUSDT | IDLE | 0.89 | 1.74 | 0.2 | 0.01 | 249165.33 | 1.34 | empty_tvl |
| QNTUSDT | IDLE | 1.32 | 2.4 | 1.61 | 0.03 | 47904.8 | 3.16 | n/a |
| MNSRYUSDT | IDLE | 0.94 | 1.71 | 1.07 | -0.02 | 34003.37 | 19.2 | no_map |
| RWAUSDT | IDLE | 0.43 | 1.01 | 0.61 | -0.02 | 59612.96 | 23.14 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
