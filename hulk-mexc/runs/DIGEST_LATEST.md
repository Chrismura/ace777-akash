# Hulk DIGEST — 2026-10-26T23:33:40Z

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
| XRPUSDT | IDLE | 0.79 | 1.48 | 0.73 | 0.0 | 24123190.61 | 2.32 | n/a |
| ETHUSDT | IDLE | 0.64 | 1.19 | 0.54 | -0.0 | 140713592.84 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.46 | 0.86 | 0.45 | 0.0 | 361128808.58 | 0.0 | no_map |
| QNTUSDT | IDLE | 0.68 | 2.85 | 2.38 | 0.06 | 1414933.7 | 2.97 | n/a |
| PYTHUSDT | IDLE | 1.43 | 2.75 | 0.71 | -0.0 | 754708.54 | 5.36 | tvl≈164,006,083 |
| WUSDT | IDLE | 1.37 | 2.72 | 1.31 | 0.05 | 642608.5 | 25.12 | tvl≈1,512,511,511 |
| CHIPUSDT | IDLE | 1.38 | 10.29 | 9.08 | 0.16 | 322469.02 | 19.64 | no_map |
| RWAINCUSDT | IDLE | 2.46 | 8.72 | 7.42 | -0.11 | 58681.19 | 6.41 | no_map |
| CCUSDT | IDLE | 1.1 | 2.05 | 1.0 | -0.01 | 185184.41 | 7.06 | no_map |
| EDELUSDT | IDLE | 1.32 | 2.38 | 1.8 | 0.01 | 125729.33 | 27.99 | no_map |
| ZBCNUSDT | IDLE | 0.91 | 1.65 | 1.07 | -0.05 | 222747.36 | 30.47 | n/a |
| BIOUSDT | IDLE | 1.17 | 2.19 | 1.03 | 0.0 | 57605.06 | 9.03 | n/a |
| REDUSDT | IDLE | 1.05 | 2.06 | 0.22 | 0.03 | 62360.95 | 15.6 | tvl≈3,670,321 |
| KITEUSDT | IDLE | 0.67 | 1.24 | 0.63 | 0.02 | 54279.44 | 14.05 | no_map |
| RIZEUSDT | IDLE | 1.05 | 1.95 | 0.99 | -0.0 | 44502.01 | 62.8 | no_map |
| HBARUSDT | IDLE | 0.53 | 1.04 | 0.14 | -0.0 | 242598.49 | 9.09 | empty_tvl |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
