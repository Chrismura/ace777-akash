# Hulk DIGEST — 2026-10-11T23:57:14Z

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
| WUSDT | IDLE | 2.48 | 22.27 | 6.04 | 0.24 | 4701163.25 | 10.95 | tvl≈1,692,180,884 |
| XRPUSDT | IDLE | 0.7 | 1.32 | 0.49 | 0.01 | 15884263.16 | 0.71 | n/a |
| ETHUSDT | IDLE | 0.53 | 1.04 | 0.19 | 0.01 | 204136478.73 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.38 | 0.74 | 0.14 | 0.01 | 148315502.75 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.31 | 4.34 | 1.84 | -0.0 | 913654.0 | 3.82 | tvl≈174,086,355 |
| QNTUSDT | IDLE | 2.16 | 3.86 | 3.08 | -0.01 | 756096.36 | 1.68 | n/a |
| EDELUSDT | IDLE | 2.12 | 3.81 | 2.89 | -0.03 | 371062.8 | 21.47 | no_map |
| RIZEUSDT | IDLE | 2.48 | 14.72 | 12.08 | 0.02 | 39570.04 | 57.67 | no_map |
| CCUSDT | IDLE | 1.63 | 3.32 | 1.51 | 0.06 | 359292.78 | 8.74 | no_map |
| ZBCNUSDT | IDLE | 2.17 | 3.84 | 3.34 | -0.01 | 213937.5 | 17.03 | n/a |
| CHIPUSDT | IDLE | 1.02 | 4.07 | 2.01 | 0.0 | 254289.78 | 14.64 | no_map |
| RWAINCUSDT | IDLE | 1.69 | 4.39 | 4.21 | -0.02 | 28957.69 | 9.94 | no_map |
| BIOUSDT | IDLE | 1.34 | 2.54 | 0.89 | 0.03 | 96257.55 | 3.33 | n/a |
| TELUSDT | IDLE | 2.51 | 4.51 | 3.46 | -0.03 | 171707.59 | 35.27 | no_map |
| KITEUSDT | IDLE | 1.15 | 2.26 | 0.23 | 0.01 | 65451.85 | 10.1 | no_map |
| HBARUSDT | IDLE | 1.1 | 2.13 | 0.48 | 0.02 | 301538.04 | 4.25 | empty_tvl |
| REDUSDT | IDLE | 0.84 | 1.53 | 0.96 | 0.01 | 56437.14 | 14.52 | tvl≈3,802,172 |
| RWAUSDT | IDLE | 1.42 | 2.57 | 1.82 | 0.02 | 52742.34 | 30.91 | no_map |
| MNSRYUSDT | IDLE | 0.69 | 1.24 | 0.92 | 0.0 | 33624.45 | 12.31 | no_map |
| FLUIDUSDT | IDLE | 0.32 | 2.51 | 0.28 | 0.07 | 61805.39 | 21.59 | tvl≈2,419,742,096 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
