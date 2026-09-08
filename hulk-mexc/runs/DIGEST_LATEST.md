# Hulk DIGEST — 2026-09-08T04:38:49Z

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
| XRPUSDT | IDLE | 0.74 | 1.34 | 0.9 | -0.01 | 32543076.76 | 1.43 | n/a |
| ETHUSDT | IDLE | 0.65 | 1.15 | 1.0 | -0.0 | 296286242.11 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.53 | 0.94 | 0.84 | -0.01 | 439785821.95 | 0.54 | no_map |
| EDELUSDT | IDLE | 3.22 | 9.19 | 2.01 | -0.04 | 91069.71 | 38.99 | no_map |
| CHIPUSDT | IDLE | 2.48 | 6.96 | 6.03 | -0.11 | 187966.75 | 19.49 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 9.59 | 6.87 | -0.02 | 52274.73 | 65.87 | no_map |
| CCUSDT | IDLE | 1.45 | 2.78 | 0.85 | -0.03 | 449979.1 | 5.62 | no_map |
| PYTHUSDT | IDLE | 1.18 | 2.19 | 1.17 | -0.02 | 404052.03 | 1.86 | tvl≈121,856,448 |
| WUSDT | IDLE | 1.9 | 3.43 | 2.52 | -0.01 | 236772.6 | 12.68 | tvl≈1,578,385,025 |
| KITEUSDT | IDLE | 2.2 | 3.89 | 3.42 | -0.05 | 63445.19 | 10.95 | no_map |
| HBARUSDT | IDLE | 1.24 | 2.18 | 2.04 | 0.01 | 503577.22 | 1.23 | empty_tvl |
| ZBCNUSDT | IDLE | 0.81 | 2.33 | 0.19 | -0.03 | 252235.42 | 18.37 | n/a |
| BIOUSDT | IDLE | 1.32 | 2.41 | 1.59 | -0.0 | 63137.64 | 3.68 | n/a |
| REDUSDT | IDLE | 1.12 | 1.98 | 1.79 | 0.03 | 57844.3 | 9.96 | tvl≈2,429,960 |
| RWAINCUSDT | IDLE | 0.7 | 1.83 | 0.82 | -0.07 | 3408.13 | 67.51 | no_map |
| TELUSDT | IDLE | 1.08 | 1.95 | 1.34 | -0.01 | 79684.88 | 29.42 | no_map |
| QNTUSDT | IDLE | 0.84 | 1.52 | 1.06 | -0.01 | 60043.79 | 6.04 | n/a |
| RWAUSDT | IDLE | 0.43 | 0.8 | 0.43 | -0.01 | 54051.81 | 21.78 | no_map |
| MNSRYUSDT | IDLE | 0.38 | 0.71 | 0.35 | -0.01 | 37192.4 | 46.27 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.01 | 818.78 | 21.76 | tvl≈2,648,726,591 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
