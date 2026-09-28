# Hulk DIGEST — 2026-09-28T08:19:15Z

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
| WUSDT | IDLE | 2.34 | 8.07 | 6.35 | -0.07 | 4497086.25 | 9.85 | tvl≈1,842,827,780 |
| PYTHUSDT | IDLE | 2.16 | 5.78 | 3.87 | -0.08 | 1817756.22 | 3.74 | tvl≈186,631,590 |
| QNTUSDT | IDLE | 0.55 | 17.68 | 8.43 | 0.53 | 17071159.99 | 11.71 | n/a |
| XRPUSDT | IDLE | 1.22 | 2.22 | 1.44 | -0.04 | 50289851.85 | 2.7 | n/a |
| HBARUSDT | IDLE | 2.9 | 5.8 | 0.03 | 0.04 | 1566862.29 | 2.01 | empty_tvl |
| CCUSDT | IDLE | 3.87 | 9.05 | 4.72 | 0.02 | 938510.57 | 7.22 | no_map |
| BTCUSDT | IDLE | 0.57 | 1.04 | 0.6 | -0.02 | 607160135.71 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.48 | 0.91 | 0.32 | -0.02 | 295335920.46 | 0.04 | no_map |
| KITEUSDT | IDLE | 2.15 | 5.23 | 4.12 | -0.09 | 106089.69 | 9.96 | no_map |
| BIOUSDT | IDLE | 2.14 | 4.78 | 3.4 | -0.07 | 102587.57 | 6.7 | n/a |
| TELUSDT | IDLE | 2.87 | 5.74 | 4.08 | 0.02 | 177350.21 | 33.54 | no_map |
| REDUSDT | IDLE | 1.85 | 3.57 | 2.42 | -0.09 | 64262.95 | 15.41 | tvl≈2,995,392 |
| EDELUSDT | IDLE | 1.07 | 5.76 | 3.25 | -0.14 | 185029.13 | 23.95 | no_map |
| CHIPUSDT | IDLE | 1.25 | 3.73 | 2.89 | -0.1 | 89925.43 | 15.79 | no_map |
| ZBCNUSDT | IDLE | 0.85 | 1.52 | 1.18 | -0.06 | 219891.39 | 29.72 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 5.39 | 5.11 | -0.05 | 3627.16 | 21.49 | tvl≈2,581,061,018 |
| RWAINCUSDT | IDLE | 0.66 | 6.09 | 5.74 | 0.14 | 32169.32 | 65.6 | no_map |
| RIZEUSDT | IDLE | 0.32 | 1.99 | 0.69 | -0.15 | 59349.7 | 60.5 | no_map |
| RWAUSDT | IDLE | 0.72 | 1.3 | 1.0 | -0.02 | 59411.81 | 43.1 | no_map |
| MNSRYUSDT | IDLE | 0.38 | 0.75 | 0.13 | -0.01 | 36851.7 | 25.65 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
