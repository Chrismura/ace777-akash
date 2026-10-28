# Hulk DIGEST — 2026-10-28T10:30:47Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| ETHUSDT | IDLE | 0.84 | 1.57 | 0.75 | 0.03 | 247719201.07 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.68 | 1.24 | 0.75 | 0.03 | 20232509.03 | 1.5 | n/a |
| BTCUSDT | IDLE | 0.6 | 1.15 | 0.35 | 0.02 | 309342020.38 | 0.0 | no_map |
| CCUSDT | IDLE | 2.98 | 6.2 | 1.24 | 0.08 | 286800.11 | 6.78 | no_map |
| WUSDT | IDLE | 0.7 | 1.36 | 0.87 | 0.04 | 623845.43 | 21.07 | tvl≈1,521,225,941 |
| RWAINCUSDT | IDLE | 2.81 | 5.62 | 0.0 | 0.03 | 54642.6 | 6.49 | no_map |
| ZBCNUSDT | IDLE | 1.61 | 3.17 | 1.25 | -0.03 | 213586.4 | 4.79 | n/a |
| PYTHUSDT | IDLE | 0.82 | 1.57 | 0.49 | 0.0 | 395918.08 | 2.75 | tvl≈160,234,737 |
| EDELUSDT | IDLE | 1.19 | 2.1 | 1.91 | 0.01 | 306091.69 | 21.61 | no_map |
| QNTUSDT | IDLE | 1.44 | 2.75 | 0.84 | -0.0 | 514572.12 | 1.98 | n/a |
| RIZEUSDT | IDLE | 2.44 | 4.52 | 2.39 | 0.03 | 36279.24 | 61.37 | no_map |
| CHIPUSDT | IDLE | 1.3 | 2.33 | 1.75 | 0.07 | 123036.15 | 16.66 | no_map |
| REDUSDT | IDLE | 1.02 | 1.81 | 1.57 | 0.05 | 54993.82 | 8.52 | tvl≈3,812,721 |
| KITEUSDT | IDLE | 0.87 | 1.55 | 1.25 | 0.04 | 60231.18 | 12.01 | no_map |
| BIOUSDT | IDLE | 0.77 | 1.5 | 0.26 | 0.05 | 82899.95 | 8.74 | n/a |
| HBARUSDT | IDLE | 0.69 | 1.32 | 0.42 | 0.01 | 387776.0 | 6.53 | empty_tvl |
| RWAUSDT | IDLE | 0.72 | 1.29 | 1.03 | 0.0 | 55405.66 | 56.07 | no_map |
| FLUIDUSDT | IDLE | 0.46 | 1.42 | 0.46 | 0.01 | 6654.9 | 20.31 | tvl≈2,209,009,110 |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
