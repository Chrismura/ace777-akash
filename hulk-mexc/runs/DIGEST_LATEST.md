# Hulk DIGEST — 2026-09-06T03:29:39Z

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
| XRPUSDT | IDLE | 0.73 | 1.41 | 0.29 | 0.01 | 23712070.06 | 1.41 | n/a |
| ETHUSDT | IDLE | 0.67 | 1.29 | 0.35 | 0.02 | 197336201.22 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.23 | 0.43 | 0.2 | 0.0 | 371954644.43 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.18 | 4.0 | 2.39 | 0.02 | 414632.79 | 1.81 | tvl≈123,271,808 |
| CHIPUSDT | IDLE | 1.93 | 4.3 | 2.67 | 0.08 | 417859.45 | 1.69 | no_map |
| RWAINCUSDT | IDLE | 2.82 | 5.2 | 2.97 | 0.01 | 8659.32 | 43.01 | no_map |
| CCUSDT | IDLE | 1.34 | 2.52 | 1.02 | 0.02 | 291431.19 | 11.8 | no_map |
| WUSDT | IDLE | 1.78 | 3.22 | 2.24 | 0.03 | 169407.46 | 9.96 | tvl≈1,671,676,413 |
| ZBCNUSDT | IDLE | 1.36 | 2.5 | 1.52 | -0.01 | 216115.58 | 15.68 | n/a |
| KITEUSDT | IDLE | 1.87 | 3.55 | 1.33 | -0.05 | 64581.95 | 11.68 | no_map |
| RIZEUSDT | IDLE | 1.28 | 8.56 | 1.58 | -0.02 | 122489.85 | 52.39 | no_map |
| REDUSDT | IDLE | 1.48 | 2.67 | 1.97 | -0.01 | 58251.02 | 8.7 | tvl≈2,331,573 |
| HBARUSDT | IDLE | 1.02 | 1.98 | 0.34 | 0.03 | 382517.98 | 1.23 | empty_tvl |
| RWAUSDT | IDLE | 2.22 | 3.91 | 3.49 | 0.03 | 53729.83 | 14.17 | no_map |
| BIOUSDT | IDLE | 0.67 | 1.22 | 0.82 | 0.02 | 94278.44 | 3.59 | n/a |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.39 | 0.02 | 114737.78 | 28.1 | no_map |
| TELUSDT | IDLE | 1.68 | 3.22 | 0.87 | 0.0 | 72142.91 | 40.78 | no_map |
| QNTUSDT | IDLE | 1.34 | 2.5 | 1.19 | 0.03 | 37039.73 | 1.53 | n/a |
| FLUIDUSDT | IDLE | 0.91 | 1.82 | 0.0 | 0.03 | 390.92 | 22.04 | tvl≈2,659,762,913 |
| MNSRYUSDT | IDLE | 0.53 | 1.01 | 0.28 | 0.01 | 38949.38 | 25.77 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
