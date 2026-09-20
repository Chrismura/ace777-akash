# Hulk DIGEST — 2026-09-20T17:45:59Z

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
| XRPUSDT | IDLE | 1.65 | 3.2 | 0.68 | -0.01 | 42553166.81 | 1.42 | n/a |
| ETHUSDT | IDLE | 1.56 | 3.03 | 0.54 | -0.0 | 265789610.88 | 0.38 | no_map |
| BTCUSDT | IDLE | 0.73 | 1.45 | 0.13 | -0.0 | 471076639.58 | 0.0 | no_map |
| HBARUSDT | IDLE | 3.45 | 10.79 | 3.53 | 0.06 | 1259738.21 | 5.76 | empty_tvl |
| PYTHUSDT | IDLE | 3.23 | 6.57 | 0.57 | 0.01 | 670129.45 | 3.27 | tvl≈135,868,455 |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.02 | 8.91 | 0.32 | 0.02 | 91573.46 | 18.15 | no_map |
| WUSDT | IDLE | 2.67 | 5.31 | 0.25 | 0.02 | 392437.67 | 7.99 | tvl≈1,612,333,322 |
| CCUSDT | IDLE | 1.97 | 4.25 | 0.86 | -0.04 | 439451.22 | 8.35 | no_map |
| ZBCNUSDT | IDLE | 3.05 | 5.91 | 4.27 | -0.03 | 185298.82 | 46.04 | n/a |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.73 | 11.84 | 0.58 | 0.07 | 74411.39 | 26.99 | no_map |
| BIOUSDT | IDLE | 2.45 | 4.85 | 0.39 | -0.02 | 80472.13 | 7.2 | n/a |
| KITEUSDT | IDLE | 1.53 | 3.0 | 0.45 | -0.01 | 66991.4 | 11.37 | no_map |
| TELUSDT | IDLE | 2.92 | 5.66 | 1.16 | 0.0 | 97381.32 | 39.22 | no_map |
| REDUSDT | IDLE | 1.45 | 2.89 | 0.1 | 0.03 | 74920.76 | 13.81 | tvl≈2,724,843 |
| RWAINCUSDT | IDLE | 1.23 | 2.46 | 0.0 | 0.02 | 9290.08 | 46.98 | no_map |
| QNTUSDT | IDLE | 1.47 | 2.87 | 0.49 | -0.0 | 85028.65 | 4.61 | n/a |
| FLUIDUSDT | IDLE | 1.69 | 3.37 | 0.0 | -0.02 | 3886.79 | 22.25 | tvl≈2,623,351,768 |
| RIZEUSDT | IDLE | 0.87 | 2.18 | 0.92 | -0.03 | 26092.43 | 100.39 | no_map |
| RWAUSDT | IDLE | 0.81 | 1.57 | 0.37 | -0.01 | 53926.6 | 14.74 | no_map |
| MNSRYUSDT | IDLE | 0.42 | 0.79 | 0.37 | 0.0 | 35279.19 | 54.45 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
