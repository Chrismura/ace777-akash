# Hulk DIGEST — 2026-09-28T23:32:27Z

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
| HBARUSDT | IDLE | 1.63 | 14.78 | 7.15 | 0.28 | 11721854.58 | 9.05 | empty_tvl |
| QNTUSDT | IDLE | 0.88 | 12.95 | 7.39 | -0.16 | 15464192.03 | 9.29 | n/a |
| XRPUSDT | IDLE | 1.42 | 2.65 | 1.28 | -0.01 | 66146704.48 | 2.67 | n/a |
| WUSDT | IDLE | 0.69 | 3.21 | 0.47 | -0.13 | 1794168.64 | 8.04 | tvl≈1,804,294,669 |
| ETHUSDT | IDLE | 0.67 | 1.29 | 0.34 | 0.0 | 399028028.51 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.61 | 1.14 | 0.52 | -0.01 | 830531831.81 | 0.0 | no_map |
| CCUSDT | IDLE | 1.41 | 5.38 | 2.59 | -0.04 | 1359153.03 | 7.67 | no_map |
| PYTHUSDT | IDLE | 1.82 | 4.0 | 0.63 | -0.03 | 1186160.5 | 1.23 | tvl≈177,971,605 |
| TELUSDT | IDLE | 2.82 | 28.41 | 4.99 | 0.26 | 360935.28 | 8.47 | no_map |
| EDELUSDT | IDLE | 1.87 | 11.4 | 9.11 | 0.05 | 159443.99 | 7.5 | no_map |
| ZBCNUSDT | IDLE | 1.6 | 3.05 | 1.0 | -0.02 | 219282.36 | 9.39 | n/a |
| RWAINCUSDT | IDLE | 2.65 | 5.88 | 4.65 | -0.03 | 17232.41 | 114.71 | no_map |
| RIZEUSDT | IDLE | 1.58 | 5.52 | 3.41 | 0.09 | 46121.05 | 37.6 | no_map |
| CHIPUSDT | IDLE | 1.31 | 3.17 | 1.27 | -0.06 | 75454.68 | 18.31 | no_map |
| KITEUSDT | IDLE | 0.94 | 3.49 | 1.67 | -0.1 | 100306.8 | 9.48 | no_map |
| BIOUSDT | IDLE | 0.84 | 2.59 | 0.54 | -0.07 | 115688.32 | 10.14 | n/a |
| REDUSDT | IDLE | 1.03 | 2.12 | 0.29 | -0.05 | 58919.26 | 14.87 | tvl≈2,919,893 |
| FLUIDUSDT | IDLE | 0.95 | 2.23 | 1.6 | -0.05 | 4433.25 | 21.98 | tvl≈2,599,980,478 |
| RWAUSDT | IDLE | 0.41 | 0.72 | 0.64 | -0.01 | 57723.66 | 7.2 | no_map |
| MNSRYUSDT | IDLE | 0.24 | 0.45 | 0.26 | -0.02 | 33930.84 | 15.48 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
