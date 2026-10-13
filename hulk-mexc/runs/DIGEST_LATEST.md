# Hulk DIGEST — 2026-10-13T19:07:55Z

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
| WUSDT | IDLE | 1.99 | 15.66 | 11.81 | -0.23 | 4863894.92 | 8.59 | tvl≈1,672,758,553 |
| PYTHUSDT | IDLE | 2.51 | 7.99 | 4.86 | -0.02 | 2021215.97 | 3.77 | tvl≈175,284,878 |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.53 | 9.65 | 0.84 | -0.03 | 1561031.69 | 7.77 | n/a |
| XRPUSDT | IDLE | 0.74 | 1.4 | 0.49 | 0.01 | 37519368.79 | 2.18 | n/a |
| ETHUSDT | IDLE | 0.7 | 1.3 | 0.73 | -0.0 | 238395052.76 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.57 | 1.03 | 0.75 | 0.01 | 397326348.64 | 0.0 | no_map |
| CCUSDT | IDLE | 1.42 | 4.35 | 1.99 | 0.05 | 611569.89 | 9.39 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 10.22 | 6.91 | -0.08 | 64005.71 | 60.31 | no_map |
| EDELUSDT | IDLE | 1.89 | 3.94 | 1.85 | 0.02 | 274399.24 | 17.4 | no_map |
| CHIPUSDT | IDLE | 2.2 | 4.82 | 3.1 | -0.02 | 110536.36 | 15.66 | no_map |
| RWAINCUSDT | IDLE | 2.5 | 4.82 | 1.14 | 0.03 | 29939.35 | 4.8 | no_map |
| REDUSDT | IDLE | 2.0 | 4.28 | 0.47 | 0.01 | 145956.79 | 7.73 | tvl≈3,808,596 |
| ZBCNUSDT | IDLE | 1.62 | 2.89 | 2.32 | -0.01 | 225721.2 | 10.54 | n/a |
| HBARUSDT | IDLE | 1.53 | 2.86 | 1.34 | -0.02 | 327918.81 | 4.56 | empty_tvl |
| BIOUSDT | IDLE | 1.28 | 2.92 | 0.39 | -0.02 | 75006.88 | 10.8 | n/a |
| TELUSDT | IDLE | 2.05 | 3.74 | 2.38 | 0.01 | 118913.97 | 28.37 | no_map |
| KITEUSDT | IDLE | 0.88 | 1.9 | 0.34 | 0.0 | 60567.04 | 10.18 | no_map |
| FLUIDUSDT | IDLE | 0.93 | 2.02 | 0.6 | 0.03 | 26318.55 | 21.16 | tvl≈2,376,650,574 |
| RWAUSDT | IDLE | 0.44 | 0.78 | 0.62 | -0.0 | 53015.78 | 15.48 | no_map |
| MNSRYUSDT | IDLE | 0.32 | 0.59 | 0.29 | -0.02 | 38408.86 | 22.33 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
