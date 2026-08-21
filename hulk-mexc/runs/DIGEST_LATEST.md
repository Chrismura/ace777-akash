# Hulk DIGEST — 2026-08-21T23:22:04Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.5 | 0.12 | 6044459.43 | 2.03 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.81 | 7.3 | 0.05 | 0.15 | 139117424.19 | 4.79 | n/a |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 11.25 | 0.39 | 0.16 | 512603.1 | 21.72 | n/a |
| HBARUSDT | IDLE | 2.55 | 6.29 | 0.01 | 0.1 | 895624.04 | 6.2 | empty_tvl |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.2 | 0.13 | 644677.08 | 6.24 | no_map |
| WUSDT | IDLE | 2.75 | 6.91 | 1.43 | 0.08 | 377672.04 | 8.2 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.34 | 0.05 | 548003.49 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.2 | 0.02 | 187841.15 | 9.34 | n/a |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82500.69 | 21.83 | no_map |
| RIZEUSDT | IDLE | 2.16 | 9.82 | 3.28 | 0.1 | 59642.01 | 43.62 | no_map |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 26.99 | no_map |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.15 | 0.07 | 185057.72 | 30.83 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.55 | 0.19 | 157461.08 | 17.73 | tvl≈2,226,572 |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| QNTUSDT | IDLE | 2.53 | 5.3 | 0.04 | 0.07 | 119007.58 | 1.5 | n/a |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.38 | 0.09 | 61538.3 | 9.29 | no_map |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54476.43 | 8.19 | no_map |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.12 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
