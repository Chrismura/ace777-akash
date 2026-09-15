# Hulk DIGEST — 2026-09-15T15:46:03Z

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
| XRPUSDT | IDLE | 3.27 | 6.39 | 4.66 | -0.01 | 83486396.14 | 2.15 | n/a |
| ETHUSDT | IDLE | 1.9 | 4.09 | 2.42 | -0.03 | 506057375.43 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.15 | 2.15 | 1.02 | -0.03 | 576988181.41 | 0.0 | no_map |
| EDELUSDT | IDLE | 1.83 | 24.22 | 13.6 | 0.33 | 467985.53 | 41.56 | no_map |
| ZBCNUSDT | IDLE | 4.25 | 8.73 | 4.76 | -0.01 | 207745.42 | 25.93 | n/a |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.48 | 10.61 | 9.25 | -0.1 | 90118.41 | 15.95 | no_map |
| CCUSDT | IDLE | 1.85 | 3.41 | 1.89 | -0.02 | 344980.97 | 9.6 | no_map |
| HBARUSDT | IDLE | 2.21 | 4.08 | 2.3 | 0.02 | 458841.78 | 1.28 | empty_tvl |
| PYTHUSDT | IDLE | 1.65 | 3.22 | 1.36 | -0.03 | 293673.99 | 1.86 | tvl≈120,975,427 |
| KITEUSDT | IDLE | 2.41 | 4.4 | 2.8 | -0.0 | 62460.37 | 14.39 | no_map |
| RWAINCUSDT | IDLE | 2.45 | 4.29 | 4.06 | -0.05 | 8127.06 | 11.59 | no_map |
| WUSDT | IDLE | 1.6 | 3.44 | 1.6 | -0.04 | 155034.28 | 13.61 | tvl≈1,438,422,916 |
| REDUSDT | IDLE | 1.19 | 6.22 | 3.98 | -0.02 | 108289.81 | 8.91 | tvl≈2,494,935 |
| RIZEUSDT | IDLE | 1.24 | 10.95 | 9.43 | 0.02 | 53630.75 | 64.41 | no_map |
| BIOUSDT | IDLE | 1.49 | 2.84 | 0.99 | -0.02 | 82499.23 | 7.98 | n/a |
| FLUIDUSDT | IDLE | 1.79 | 3.21 | 2.57 | -0.04 | 2071.8 | 21.97 | tvl≈2,641,869,823 |
| TELUSDT | IDLE | 1.33 | 4.37 | 2.79 | -0.05 | 99621.44 | 52.19 | no_map |
| QNTUSDT | IDLE | 1.19 | 2.31 | 0.47 | -0.03 | 50639.92 | 4.77 | n/a |
| RWAUSDT | IDLE | 0.53 | 0.98 | 0.52 | -0.01 | 52013.61 | 14.98 | no_map |
| MNSRYUSDT | IDLE | 0.57 | 1.04 | 0.65 | 0.0 | 33473.11 | 32.05 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
