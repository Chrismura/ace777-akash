# Hulk DIGEST — 2026-08-30T23:08:43Z

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
| XRPUSDT | IDLE | 2.1 | 3.68 | 3.5 | -0.01 | 25925670.28 | 1.45 | n/a |
| ETHUSDT | IDLE | 1.29 | 2.27 | 2.06 | 0.0 | 260157056.77 | 1.01 | no_map |
| BTCUSDT | IDLE | 0.68 | 1.2 | 1.05 | 0.0 | 303821532.68 | 0.0 | no_map |
| CHIPUSDT | IDLE | 2.2 | 5.82 | 4.83 | -0.05 | 566016.06 | 2.61 | no_map |
| PYTHUSDT | IDLE | 2.63 | 4.7 | 3.77 | 0.0 | 419664.75 | 2.06 | tvl≈109,675,290 |
| WUSDT | IDLE | 2.0 | 3.55 | 3.0 | 0.02 | 237447.47 | 11.85 | tvl≈1,531,052,661 |
| ZBCNUSDT | IDLE | 1.66 | 3.74 | 2.15 | -0.05 | 208389.42 | 3.84 | n/a |
| BIOUSDT | IDLE | 2.07 | 3.66 | 3.17 | -0.02 | 85784.19 | 3.72 | n/a |
| EDELUSDT | IDLE | 2.17 | 6.23 | 2.97 | 0.07 | 76133.55 | 33.03 | no_map |
| KITEUSDT | IDLE | 1.91 | 3.4 | 2.85 | -0.05 | 62326.11 | 11.35 | no_map |
| CCUSDT | IDLE | 0.92 | 1.78 | 0.37 | 0.01 | 231472.53 | 5.89 | no_map |
| REDUSDT | IDLE | 1.3 | 2.49 | 0.75 | -0.0 | 62874.85 | 10.07 | tvl≈2,002,827 |
| RIZEUSDT | IDLE | 1.66 | 4.72 | 2.7 | -0.06 | 42144.41 | 62.7 | no_map |
| RWAINCUSDT | IDLE | 1.65 | 3.05 | 1.64 | 0.02 | 1676.0 | 83.87 | no_map |
| HBARUSDT | IDLE | 1.35 | 2.38 | 2.15 | -0.01 | 172091.52 | 2.69 | empty_tvl |
| TELUSDT | IDLE | 2.16 | 3.81 | 3.39 | 0.02 | 88148.49 | 58.38 | no_map |
| QNTUSDT | IDLE | 1.25 | 2.21 | 1.97 | -0.01 | 37175.19 | 3.29 | n/a |
| FLUIDUSDT | IDLE | 1.29 | 2.25 | 2.2 | 0.01 | 3330.5 | 19.63 | tvl≈2,635,474,435 |
| RWAUSDT | IDLE | 0.42 | 0.81 | 0.16 | 0.02 | 51564.6 | 16.1 | no_map |
| MNSRYUSDT | IDLE | 0.49 | 0.87 | 0.72 | 0.0 | 31864.14 | 52.31 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
