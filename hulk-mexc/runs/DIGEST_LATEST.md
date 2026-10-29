# Hulk DIGEST — 2026-10-29T09:19:31Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.74 | 1.35 | 0.87 | -0.03 | 24001421.56 | 1.55 | n/a |
| ETHUSDT | IDLE | 0.7 | 1.31 | 0.54 | -0.02 | 237019369.14 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.48 | 0.91 | 0.34 | -0.02 | 347616494.93 | 0.0 | no_map |
| WUSDT | IDLE | 1.89 | 3.52 | 1.7 | -0.03 | 502332.28 | 17.75 | tvl≈1,474,800,531 |
| PYTHUSDT | IDLE | 1.6 | 2.97 | 1.51 | -0.03 | 456369.11 | 4.26 | tvl≈156,290,508 |
| CCUSDT | IDLE | 0.6 | 1.41 | 0.31 | -0.04 | 427762.14 | 10.31 | no_map |
| QNTUSDT | IDLE | 1.61 | 2.91 | 2.07 | -0.04 | 431867.98 | 3.65 | n/a |
| HBARUSDT | IDLE | 1.01 | 1.89 | 0.93 | -0.03 | 559207.25 | 5.42 | empty_tvl |
| LAUSDT | IDLE | 3.2 | 5.76 | 4.29 | -0.04 | 56908.61 | 24.58 | no_map |
| EDELUSDT | IDLE | 1.39 | 2.57 | 1.35 | -0.04 | 178299.34 | 19.09 | no_map |
| CHIPUSDT | IDLE | 0.67 | 3.55 | 1.3 | -0.12 | 242624.65 | 10.46 | no_map |
| REDUSDT | IDLE | 1.56 | 2.85 | 1.85 | -0.04 | 64128.81 | 14.93 | tvl≈3,658,611 |
| ZBCNUSDT | IDLE | 0.77 | 1.43 | 0.78 | -0.01 | 256413.48 | 17.04 | n/a |
| BIOUSDT | IDLE | 1.5 | 2.85 | 1.03 | -0.03 | 67834.92 | 9.03 | n/a |
| RWAINCUSDT | IDLE | 1.13 | 4.82 | 1.32 | -0.06 | 28740.71 | 7.09 | no_map |
| RIZEUSDT | IDLE | 1.08 | 2.12 | 0.33 | -0.03 | 37671.07 | 11.71 | no_map |
| KITEUSDT | IDLE | 0.81 | 1.51 | 0.72 | -0.04 | 60637.98 | 14.25 | no_map |
| FLUIDUSDT | IDLE | 2.3 | 4.39 | 3.06 | -0.06 | 6071.6 | 20.3 | tvl≈2,217,439,636 |
| WAXLUSDT | IDLE | 1.7 | 4.01 | 1.98 | -0.06 | 54062.51 | 39.15 | no_map |
| IOTAUSDT | IDLE | 1.1 | 2.11 | 0.91 | -0.05 | 101714.05 | 19.89 | no_map |
| RWAUSDT | IDLE | 1.1 | 2.01 | 1.26 | 0.0 | 56253.48 | 8.0 | no_map |
| MNSRYUSDT | IDLE | 0.3 | 0.53 | 0.5 | -0.01 | 37215.15 | 56.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
