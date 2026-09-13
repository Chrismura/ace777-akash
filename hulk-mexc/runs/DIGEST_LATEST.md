# Hulk DIGEST — 2026-09-13T03:39:01Z

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
| XRPUSDT | IDLE | 0.34 | 0.6 | 0.47 | -0.0 | 14051921.17 | 2.2 | n/a |
| ETHUSDT | IDLE | 0.18 | 0.32 | 0.27 | 0.0 | 195048629.21 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.12 | 0.22 | 0.16 | -0.0 | 311666429.23 | 0.0 | no_map |
| RIZEUSDT | IDLE | 2.42 | 41.76 | 25.07 | 0.05 | 94245.54 | 69.83 | no_map |
| PYTHUSDT | IDLE | 1.32 | 2.49 | 1.02 | 0.06 | 433103.77 | 1.82 | tvl≈123,388,794 |
| WUSDT | IDLE | 2.2 | 4.05 | 2.29 | 0.03 | 215607.04 | 19.88 | tvl≈1,469,962,923 |
| ZBCNUSDT | IDLE | 1.76 | 5.23 | 2.12 | -0.01 | 225254.08 | 12.36 | n/a |
| RWAINCUSDT | IDLE | 2.46 | 4.7 | 3.28 | 0.03 | 9906.13 | 5.44 | no_map |
| QNTUSDT | IDLE | 3.32 | 5.95 | 4.63 | 0.0 | 41099.78 | 4.67 | n/a |
| REDUSDT | IDLE | 2.03 | 3.97 | 0.64 | 0.02 | 56173.11 | 11.21 | tvl≈2,385,775 |
| EDELUSDT | IDLE | 1.42 | 3.77 | 0.73 | 0.08 | 171759.78 | 16.26 | no_map |
| CCUSDT | IDLE | 0.85 | 1.59 | 0.77 | -0.01 | 187678.91 | 10.23 | no_map |
| RWAUSDT | IDLE | 2.68 | 4.77 | 3.98 | 0.0 | 54835.24 | 37.05 | no_map |
| BIOUSDT | IDLE | 0.93 | 1.74 | 0.78 | 0.0 | 70601.66 | 3.91 | n/a |
| CHIPUSDT | IDLE | 0.91 | 1.75 | 1.39 | 0.0 | 77281.03 | 14.72 | no_map |
| KITEUSDT | IDLE | 0.87 | 1.65 | 0.56 | -0.0 | 63067.27 | 10.26 | no_map |
| FLUIDUSDT | IDLE | 2.07 | 4.13 | 0.08 | 0.03 | 536.22 | 21.58 | tvl≈2,679,802,215 |
| HBARUSDT | IDLE | 0.51 | 0.97 | 0.35 | 0.0 | 132645.77 | 1.34 | empty_tvl |
| TELUSDT | IDLE | 0.86 | 1.53 | 1.27 | -0.04 | 90883.08 | 24.42 | no_map |
| MNSRYUSDT | IDLE | 0.08 | 0.14 | 0.08 | -0.0 | 29270.59 | 15.28 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
