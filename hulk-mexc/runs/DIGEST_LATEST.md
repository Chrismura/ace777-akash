# Hulk DIGEST — 2026-09-06T00:28:48Z

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
| XRPUSDT | IDLE | 0.75 | 1.41 | 0.59 | 0.01 | 23244978.85 | 2.83 | n/a |
| ETHUSDT | IDLE | 0.41 | 0.78 | 0.28 | 0.01 | 162407663.74 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.08 | 0.0 | 368860440.93 | 0.0 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 20.43 | 12.96 | -0.05 | 128726.99 | 61.54 | no_map |
| PYTHUSDT | IDLE | 1.9 | 3.73 | 0.41 | 0.03 | 358095.88 | 1.78 | tvl≈123,719,242 |
| CHIPUSDT | IDLE | 1.32 | 3.41 | 1.38 | 0.08 | 421676.22 | 5.07 | no_map |
| RWAINCUSDT | IDLE | 2.87 | 5.2 | 3.59 | 0.0 | 8280.39 | 26.96 | no_map |
| ZBCNUSDT | IDLE | 1.73 | 3.24 | 1.41 | -0.0 | 217136.78 | 10.8 | n/a |
| WUSDT | IDLE | 1.57 | 3.11 | 0.26 | 0.05 | 161237.55 | 7.87 | tvl≈1,652,671,794 |
| CCUSDT | IDLE | 0.77 | 1.39 | 1.06 | 0.02 | 271896.48 | 5.51 | no_map |
| BIOUSDT | IDLE | 0.81 | 1.51 | 0.71 | 0.03 | 82382.14 | 3.57 | n/a |
| REDUSDT | IDLE | 0.92 | 1.73 | 0.79 | 0.02 | 60451.63 | 8.7 | tvl≈2,314,601 |
| EDELUSDT | IDLE | 0.21 | 2.66 | 2.59 | -0.02 | 168129.25 | 9.5 | no_map |
| HBARUSDT | IDLE | 0.76 | 1.43 | 0.55 | 0.02 | 356538.32 | 1.24 | empty_tvl |
| KITEUSDT | IDLE | 0.55 | 1.21 | 0.83 | -0.08 | 64349.94 | 10.32 | no_map |
| TELUSDT | IDLE | 1.95 | 3.58 | 2.13 | -0.01 | 72060.13 | 47.0 | no_map |
| RWAUSDT | IDLE | 1.64 | 2.96 | 2.19 | 0.04 | 52959.44 | 13.99 | no_map |
| QNTUSDT | IDLE | 0.43 | 0.85 | 0.02 | 0.02 | 36660.98 | 3.07 | n/a |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.1 | 0.0 | 38860.69 | 6.82 | no_map |
| FLUIDUSDT | IDLE | 0.4 | 0.79 | 0.1 | 0.01 | 385.8 | 23.83 | tvl≈2,651,769,771 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
