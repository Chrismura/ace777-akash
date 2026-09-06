# Hulk DIGEST — 2026-09-06T10:30:11Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| ETHUSDT | IDLE | 0.88 | 1.61 | 0.96 | 0.02 | 230253583.67 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.76 | 1.41 | 0.69 | 0.01 | 25465805.31 | 1.41 | n/a |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.15 | 0.0 | 404205265.11 | 0.0 | no_map |
| CHIPUSDT | IDLE | 2.69 | 7.32 | 1.35 | 0.07 | 400284.69 | 3.29 | no_map |
| PYTHUSDT | IDLE | 1.47 | 2.7 | 1.64 | 0.02 | 431599.74 | 1.82 | tvl≈123,301,040 |
| RIZEUSDT | IDLE | 2.23 | 12.15 | 10.68 | 0.01 | 90011.47 | 63.3 | no_map |
| CCUSDT | IDLE | 1.02 | 1.93 | 0.67 | 0.02 | 304792.35 | 7.24 | no_map |
| ZBCNUSDT | IDLE | 1.45 | 2.76 | 0.88 | 0.01 | 224875.11 | 18.92 | n/a |
| RWAINCUSDT | IDLE | 2.33 | 4.65 | 0.05 | 0.04 | 9400.36 | 31.32 | no_map |
| WUSDT | IDLE | 1.14 | 2.13 | 1.0 | 0.01 | 174246.24 | 10.91 | tvl≈1,669,244,695 |
| EDELUSDT | IDLE | 1.58 | 2.83 | 2.2 | 0.0 | 68734.6 | 18.74 | no_map |
| BIOUSDT | IDLE | 1.25 | 2.29 | 1.42 | 0.01 | 93743.47 | 3.61 | n/a |
| REDUSDT | IDLE | 1.39 | 2.75 | 0.25 | 0.01 | 61788.34 | 12.48 | tvl≈2,329,432 |
| HBARUSDT | IDLE | 0.86 | 1.61 | 0.67 | 0.01 | 422668.82 | 1.23 | empty_tvl |
| KITEUSDT | IDLE | 1.13 | 1.99 | 1.78 | -0.03 | 65420.94 | 8.64 | no_map |
| QNTUSDT | IDLE | 1.55 | 2.79 | 2.03 | 0.03 | 39941.61 | 1.52 | n/a |
| TELUSDT | IDLE | 0.82 | 1.47 | 1.16 | 0.0 | 71217.04 | 41.02 | no_map |
| RWAUSDT | IDLE | 0.6 | 1.07 | 0.92 | 0.0 | 53039.98 | 14.3 | no_map |
| FLUIDUSDT | IDLE | 0.47 | 0.91 | 0.14 | 0.02 | 353.17 | 21.3 | tvl≈2,659,762,913 |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
