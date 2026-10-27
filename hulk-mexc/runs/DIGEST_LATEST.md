# Hulk DIGEST — 2026-10-27T01:52:25Z

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
| XRPUSDT | IDLE | 1.14 | 2.19 | 0.65 | 0.02 | 24612548.84 | 1.53 | n/a |
| ETHUSDT | IDLE | 0.71 | 1.35 | 0.42 | 0.01 | 129030504.46 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.44 | 0.83 | 0.3 | 0.01 | 355491332.12 | 0.0 | no_map |
| QNTUSDT | IDLE | 0.46 | 1.99 | 1.16 | 0.07 | 1410180.27 | 1.98 | n/a |
| PYTHUSDT | IDLE | 1.73 | 3.12 | 2.27 | -0.01 | 680423.63 | 5.43 | tvl≈164,006,083 |
| WUSDT | IDLE | 1.5 | 2.99 | 1.34 | 0.05 | 639803.66 | 25.85 | tvl≈1,516,296,021 |
| CHIPUSDT | IDLE | 0.72 | 5.48 | 3.65 | 0.2 | 328013.95 | 17.6 | no_map |
| RWAINCUSDT | IDLE | 1.55 | 5.5 | 4.72 | -0.12 | 58865.08 | 19.27 | no_map |
| EDELUSDT | IDLE | 1.16 | 2.16 | 1.1 | 0.02 | 175731.46 | 6.19 | no_map |
| CCUSDT | IDLE | 1.07 | 1.96 | 1.18 | -0.02 | 186266.94 | 6.07 | no_map |
| REDUSDT | IDLE | 1.62 | 2.95 | 1.95 | 0.03 | 61670.58 | 16.41 | tvl≈3,642,722 |
| ZBCNUSDT | IDLE | 0.96 | 1.85 | 0.51 | -0.02 | 219248.36 | 28.33 | n/a |
| BIOUSDT | IDLE | 1.12 | 2.19 | 0.36 | 0.01 | 57299.28 | 8.97 | n/a |
| KITEUSDT | IDLE | 0.75 | 1.31 | 1.25 | 0.01 | 53857.16 | 11.47 | no_map |
| RIZEUSDT | IDLE | 0.88 | 1.66 | 0.6 | -0.01 | 43918.84 | 64.89 | no_map |
| HBARUSDT | IDLE | 0.87 | 1.66 | 0.54 | 0.01 | 210708.56 | 6.48 | empty_tvl |
| FLUIDUSDT | IDLE | 1.35 | 2.68 | 0.18 | 0.05 | 2179.39 | 21.76 | tvl≈2,187,847,033 |
| RWAUSDT | IDLE | 0.64 | 1.21 | 0.48 | -0.0 | 53601.23 | 15.96 | no_map |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.07 | 0.0 | 41568.98 | 76.46 | no_map |
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
