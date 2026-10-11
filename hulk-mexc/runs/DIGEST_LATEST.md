# Hulk DIGEST — 2026-10-11T23:30:09Z

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
| WUSDT | IDLE | 2.49 | 22.27 | 6.37 | 0.24 | 4623345.96 | 5.04 | tvl≈1,692,180,884 |
| XRPUSDT | IDLE | 0.69 | 1.32 | 0.42 | 0.01 | 16016984.6 | 2.13 | n/a |
| ETHUSDT | IDLE | 0.54 | 1.04 | 0.22 | 0.01 | 208171003.51 | 0.08 | no_map |
| BTCUSDT | IDLE | 0.38 | 0.74 | 0.18 | 0.01 | 149994562.78 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.3 | 4.34 | 1.75 | 0.0 | 906924.78 | 5.08 | tvl≈174,086,355 |
| QNTUSDT | IDLE | 2.17 | 3.86 | 3.16 | -0.01 | 746792.19 | 1.26 | n/a |
| EDELUSDT | IDLE | 2.14 | 3.81 | 3.18 | -0.03 | 370418.78 | 26.86 | no_map |
| RIZEUSDT | IDLE | 2.49 | 14.72 | 12.64 | 0.01 | 40136.83 | 57.83 | no_map |
| CCUSDT | IDLE | 1.62 | 3.32 | 1.48 | 0.06 | 358486.76 | 5.56 | no_map |
| ZBCNUSDT | IDLE | 2.17 | 3.84 | 3.3 | -0.01 | 212313.22 | 7.43 | n/a |
| CHIPUSDT | IDLE | 1.02 | 4.07 | 2.14 | -0.01 | 261836.59 | 14.65 | no_map |
| TELUSDT | IDLE | 2.52 | 4.51 | 3.58 | -0.03 | 170592.01 | 5.89 | no_map |
| BIOUSDT | IDLE | 1.37 | 2.54 | 1.29 | 0.03 | 95808.46 | 3.34 | n/a |
| RWAINCUSDT | IDLE | 1.52 | 3.98 | 3.59 | -0.01 | 28832.2 | 34.75 | no_map |
| KITEUSDT | IDLE | 1.15 | 2.26 | 0.25 | 0.01 | 65431.44 | 11.66 | no_map |
| HBARUSDT | IDLE | 1.1 | 2.13 | 0.53 | 0.02 | 302244.51 | 5.31 | empty_tvl |
| REDUSDT | IDLE | 0.84 | 1.53 | 0.98 | 0.01 | 56335.37 | 14.52 | tvl≈3,802,172 |
| RWAUSDT | IDLE | 1.42 | 2.57 | 1.82 | 0.02 | 52874.3 | 7.73 | no_map |
| MNSRYUSDT | IDLE | 0.69 | 1.24 | 0.92 | 0.0 | 33352.87 | 17.79 | no_map |
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
