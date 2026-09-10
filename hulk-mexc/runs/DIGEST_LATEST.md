# Hulk DIGEST — 2026-09-10T13:14:35Z

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
| ETHUSDT | IDLE | 1.68 | 2.95 | 2.68 | -0.04 | 369263608.87 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.49 | 2.65 | 2.21 | -0.06 | 45520780.99 | 2.95 | n/a |
| BTCUSDT | IDLE | 1.11 | 1.96 | 1.77 | -0.03 | 544067293.09 | 0.0 | no_map |
| RIZEUSDT | IDLE | 1.26 | 68.27 | 23.65 | -0.55 | 114204.32 | 21.93 | no_map |
| CCUSDT | IDLE | 2.64 | 4.72 | 3.71 | -0.05 | 675013.78 | 9.94 | no_map |
| PYTHUSDT | IDLE | 0.97 | 2.72 | 1.67 | -0.08 | 1019398.01 | 1.95 | tvl≈116,320,814 |
| KITEUSDT | IDLE | 3.1 | 6.55 | 4.9 | -0.06 | 55838.26 | 20.48 | no_map |
| ZBCNUSDT | IDLE | 2.71 | 4.79 | 4.17 | -0.02 | 178699.31 | 30.23 | n/a |
| EDELUSDT | IDLE | 1.67 | 6.26 | 3.2 | 0.05 | 229536.68 | 35.68 | no_map |
| WUSDT | IDLE | 1.11 | 2.96 | 1.79 | -0.07 | 251356.61 | 11.56 | tvl≈1,493,119,047 |
| BIOUSDT | IDLE | 1.46 | 2.96 | 2.64 | -0.08 | 82618.45 | 3.99 | n/a |
| HBARUSDT | IDLE | 1.35 | 2.4 | 2.05 | -0.05 | 341090.12 | 1.33 | empty_tvl |
| REDUSDT | IDLE | 1.04 | 2.57 | 1.38 | -0.09 | 66198.55 | 18.87 | tvl≈2,266,018 |
| CHIPUSDT | IDLE | 0.65 | 3.34 | 3.23 | -0.19 | 93473.26 | 14.79 | no_map |
| RWAINCUSDT | IDLE | 1.28 | 2.27 | 1.89 | -0.01 | 5981.8 | 22.59 | no_map |
| TELUSDT | IDLE | 2.08 | 3.64 | 3.4 | -0.02 | 90991.53 | 17.05 | no_map |
| QNTUSDT | IDLE | 1.68 | 2.95 | 2.68 | -0.04 | 39225.82 | 9.23 | n/a |
| FLUIDUSDT | IDLE | 1.49 | 3.96 | 3.81 | -0.1 | 2472.1 | 21.87 | tvl≈2,649,181,092 |
| RWAUSDT | IDLE | 1.35 | 2.37 | 2.24 | -0.05 | 54086.12 | 30.51 | no_map |
| MNSRYUSDT | IDLE | 0.91 | 1.64 | 1.14 | -0.03 | 25173.01 | 47.41 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
