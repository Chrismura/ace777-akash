# Hulk DIGEST — 2026-10-27T23:28:27Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.56 | 1.03 | 0.63 | 0.01 | 236640975.94 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.55 | 1.03 | 0.5 | 0.01 | 324441682.95 | 0.0 | no_map |
| XRPUSDT | IDLE | 0.54 | 1.06 | 0.18 | 0.03 | 20314262.45 | 0.75 | n/a |
| EDELUSDT | IDLE | 2.06 | 3.95 | 1.17 | 0.03 | 465691.63 | 30.17 | no_map |
| WUSDT | IDLE | 0.94 | 2.09 | 1.35 | 0.03 | 684139.18 | 19.56 | tvl≈1,525,225,540 |
| ZBCNUSDT | IDLE | 2.44 | 8.33 | 7.02 | -0.03 | 239069.96 | 35.23 | n/a |
| PYTHUSDT | IDLE | 1.34 | 2.43 | 1.67 | -0.02 | 392472.96 | 2.75 | tvl≈163,049,914 |
| QNTUSDT | IDLE | 1.32 | 2.39 | 1.67 | -0.01 | 685475.88 | 3.01 | n/a |
| RWAINCUSDT | IDLE | 1.68 | 3.57 | 2.86 | -0.05 | 60305.51 | 6.7 | no_map |
| CHIPUSDT | IDLE | 1.47 | 3.57 | 1.71 | 0.05 | 131717.47 | 18.43 | no_map |
| CCUSDT | IDLE | 0.76 | 1.44 | 0.48 | -0.0 | 225782.74 | 8.09 | no_map |
| RIZEUSDT | IDLE | 1.86 | 3.68 | 0.25 | 0.01 | 33238.83 | 60.07 | no_map |
| BIOUSDT | IDLE | 0.98 | 1.83 | 0.83 | 0.02 | 58800.51 | 8.84 | n/a |
| REDUSDT | IDLE | 0.89 | 1.87 | 0.81 | 0.05 | 60069.37 | 15.43 | tvl≈3,851,756 |
| KITEUSDT | IDLE | 0.73 | 1.47 | 0.18 | 0.05 | 57563.89 | 13.44 | no_map |
| HBARUSDT | IDLE | 0.72 | 1.31 | 0.83 | -0.01 | 302571.38 | 9.21 | empty_tvl |
| LAUSDT | IDLE | 0.9 | 1.78 | 1.15 | 0.03 | 60553.83 | 38.08 | no_map |
| IOTAUSDT | IDLE | 0.69 | 1.36 | 0.19 | -0.0 | 78876.19 | 26.0 | no_map |
| WAXLUSDT | IDLE | 0.78 | 1.46 | 0.65 | 0.04 | 56958.54 | 44.84 | no_map |
| RWAUSDT | IDLE | 0.41 | 0.72 | 0.64 | -0.0 | 57800.58 | 16.03 | no_map |
| FLUIDUSDT | IDLE | 0.32 | 0.63 | 0.12 | 0.02 | 2583.56 | 21.83 | tvl≈2,211,700,338 |
| MNSRYUSDT | IDLE | 0.45 | 0.81 | 0.63 | 0.0 | 37599.42 | 79.41 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
