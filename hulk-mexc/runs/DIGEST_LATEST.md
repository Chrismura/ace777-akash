# Hulk DIGEST — 2026-10-11T00:02:22Z

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
| ETHUSDT | IDLE | 0.32 | 0.56 | 0.48 | 0.01 | 122386699.87 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.32 | 0.58 | 0.43 | 0.0 | 13129663.28 | 2.14 | n/a |
| BTCUSDT | IDLE | 0.1 | 0.18 | 0.13 | 0.0 | 156680754.08 | 0.0 | no_map |
| WUSDT | IDLE | 1.06 | 3.34 | 2.46 | 0.03 | 1253660.14 | 6.23 | tvl≈1,657,793,187 |
| QNTUSDT | IDLE | 1.17 | 2.11 | 1.47 | -0.03 | 1229448.18 | 0.83 | n/a |
| PYTHUSDT | IDLE | 0.9 | 1.64 | 1.06 | -0.02 | 760647.82 | 3.81 | tvl≈176,975,805 |
| EDELUSDT | IDLE | 2.49 | 4.54 | 2.91 | -0.05 | 250452.54 | 38.98 | no_map |
| CHIPUSDT | IDLE | 1.34 | 11.6 | 3.05 | 0.31 | 265011.83 | 13.26 | no_map |
| TELUSDT | IDLE | 2.58 | 4.89 | 4.06 | -0.07 | 145651.8 | 34.31 | no_map |
| BIOUSDT | IDLE | 1.27 | 2.23 | 2.12 | 0.02 | 87821.95 | 3.44 | n/a |
| CCUSDT | IDLE | 0.57 | 1.07 | 0.52 | -0.03 | 260917.26 | 5.89 | no_map |
| RIZEUSDT | IDLE | 1.78 | 3.45 | 2.16 | -0.06 | 33474.1 | 56.82 | no_map |
| ZBCNUSDT | IDLE | 0.71 | 1.34 | 0.49 | 0.02 | 187238.8 | 18.65 | n/a |
| KITEUSDT | IDLE | 0.94 | 2.0 | 1.65 | 0.06 | 72799.15 | 8.62 | no_map |
| REDUSDT | IDLE | 0.6 | 1.07 | 0.89 | 0.02 | 56326.86 | 14.64 | tvl≈3,770,923 |
| HBARUSDT | IDLE | 0.43 | 0.79 | 0.4 | 0.0 | 302697.24 | 5.41 | empty_tvl |
| RWAINCUSDT | IDLE | 0.57 | 1.04 | 0.73 | -0.02 | 9639.33 | 83.81 | no_map |
| MNSRYUSDT | IDLE | 1.01 | 1.82 | 1.31 | -0.01 | 36826.69 | 28.8 | no_map |
| FLUIDUSDT | IDLE | 0.77 | 1.41 | 0.87 | 0.0 | 8172.97 | 18.98 | tvl≈2,427,351,722 |
| RWAUSDT | IDLE | 0.45 | 0.79 | 0.7 | 0.0 | 53613.99 | 15.75 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
