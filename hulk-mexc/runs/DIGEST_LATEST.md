# Hulk DIGEST — 2026-09-05T13:14:45Z

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
| XRPUSDT | IDLE | 0.6 | 1.19 | 0.06 | 0.01 | 27866839.94 | 2.12 | n/a |
| ETHUSDT | IDLE | 0.19 | 0.36 | 0.12 | 0.0 | 236680813.46 | 0.16 | no_map |
| BTCUSDT | IDLE | 0.14 | 0.27 | 0.1 | 0.0 | 438284962.71 | 0.15 | no_map |
| CHIPUSDT | IDLE | 1.88 | 6.78 | 5.23 | 0.01 | 445127.21 | 5.36 | no_map |
| PYTHUSDT | IDLE | 2.06 | 3.95 | 1.12 | 0.03 | 368659.32 | 3.64 | tvl≈120,618,249 |
| KITEUSDT | IDLE | 2.4 | 4.51 | 4.32 | -0.05 | 64850.98 | 18.88 | no_map |
| ZBCNUSDT | IDLE | 1.43 | 2.66 | 1.35 | -0.04 | 194473.91 | 9.5 | n/a |
| CCUSDT | IDLE | 0.93 | 1.82 | 0.2 | 0.01 | 283249.07 | 8.21 | no_map |
| REDUSDT | IDLE | 1.57 | 2.75 | 2.55 | 0.04 | 65456.31 | 8.78 | tvl≈2,335,697 |
| BIOUSDT | IDLE | 1.01 | 1.94 | 0.5 | 0.03 | 81062.56 | 3.62 | n/a |
| RIZEUSDT | IDLE | 1.2 | 11.89 | 1.95 | -0.09 | 160826.27 | 157.1 | no_map |
| HBARUSDT | IDLE | 1.33 | 2.66 | 0.01 | 0.05 | 276310.29 | 1.23 | empty_tvl |
| WUSDT | IDLE | 0.53 | 1.03 | 0.15 | 0.06 | 177507.08 | 11.03 | tvl≈1,654,750,876 |
| EDELUSDT | IDLE | 0.13 | 2.29 | 1.21 | -0.04 | 204663.71 | 28.29 | no_map |
| RWAINCUSDT | IDLE | 0.82 | 1.52 | 0.75 | 0.01 | 7104.03 | 69.61 | no_map |
| RWAUSDT | IDLE | 1.46 | 2.83 | 0.56 | 0.02 | 53608.58 | 21.25 | no_map |
| TELUSDT | IDLE | 0.84 | 1.6 | 0.58 | -0.01 | 74944.09 | 29.4 | no_map |
| QNTUSDT | IDLE | 0.58 | 1.11 | 0.39 | -0.01 | 40745.82 | 1.56 | n/a |
| FLUIDUSDT | IDLE | 0.45 | 0.9 | 0.0 | 0.02 | 820.75 | 22.25 | tvl≈2,635,155,670 |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.18 | -0.0 | 37146.16 | 27.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
