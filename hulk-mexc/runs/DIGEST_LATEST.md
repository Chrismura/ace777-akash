# Hulk DIGEST — 2026-10-07T22:11:22Z

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
| XRPUSDT | IDLE | 1.1 | 2.0 | 1.3 | -0.06 | 48916601.23 | 2.12 | n/a |
| QNTUSDT | IDLE | 0.86 | 2.87 | 1.56 | -0.04 | 3350659.38 | 2.38 | n/a |
| ETHUSDT | IDLE | 0.79 | 1.51 | 0.4 | -0.05 | 530665713.44 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.36 | 0.65 | 0.45 | -0.03 | 798563202.55 | 0.0 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 8.99 | 0.06 | 0.04 | 585910.1 | 20.25 | tvl≈1,878,877,156 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.33 | 26.55 | 14.85 | -0.14 | 60460.01 | 29.5 | no_map |
| PYTHUSDT | IDLE | 1.34 | 2.88 | 0.54 | -0.06 | 742907.29 | 5.52 | tvl≈161,676,700 |
| EDELUSDT | IDLE | 1.38 | 7.2 | 5.26 | -0.16 | 506170.15 | 2.48 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.74 | 12.38 | 9.73 | -0.15 | 54509.14 | 71.03 | no_map |
| HBARUSDT | IDLE | 0.84 | 1.77 | 0.92 | -0.07 | 726651.7 | 3.24 | empty_tvl |
| ZBCNUSDT | IDLE | 1.8 | 4.18 | 4.01 | -0.09 | 287258.13 | 64.64 | n/a |
| CCUSDT | IDLE | 0.7 | 1.37 | 0.93 | -0.06 | 438269.2 | 10.02 | no_map |
| CHIPUSDT | IDLE | 1.33 | 3.87 | 2.71 | -0.06 | 140596.39 | 11.82 | no_map |
| KITEUSDT | IDLE | 1.04 | 2.01 | 0.41 | -0.05 | 63836.6 | 9.68 | no_map |
| REDUSDT | IDLE | 0.93 | 2.03 | 1.15 | -0.07 | 56677.85 | 15.29 | tvl≈3,786,570 |
| FLUIDUSDT | IDLE | 2.18 | 7.2 | 0.86 | 0.08 | 15717.29 | 19.7 | tvl≈2,472,534,633 |
| BIOUSDT | IDLE | 0.55 | 2.1 | 0.1 | -0.07 | 83019.65 | 10.16 | n/a |
| TELUSDT | IDLE | 0.99 | 3.33 | 2.98 | 0.06 | 216828.97 | 44.57 | no_map |
| RWAUSDT | IDLE | 0.29 | 0.53 | 0.37 | -0.02 | 51873.99 | 15.03 | no_map |
| MNSRYUSDT | IDLE | 0.63 | 1.17 | 0.63 | -0.02 | 39239.0 | 49.69 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
