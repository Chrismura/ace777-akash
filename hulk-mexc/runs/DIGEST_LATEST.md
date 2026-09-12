# Hulk DIGEST — 2026-09-12T01:22:09Z

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
| RIZEUSDT | IDLE | 1.28 | 85.83 | 44.8 | 0.54 | 212855.02 | 144.42 | no_map |
| ETHUSDT | IDLE | 0.78 | 1.66 | 1.27 | 0.02 | 653003069.83 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.78 | 1.63 | 0.56 | 0.01 | 53683958.96 | 1.47 | n/a |
| BTCUSDT | IDLE | 0.36 | 0.68 | 0.2 | 0.01 | 581491107.47 | 0.0 | no_map |
| ZBCNUSDT | IDLE | 2.08 | 3.64 | 3.52 | -0.01 | 194609.08 | 8.46 | n/a |
| EDELUSDT | IDLE | 2.2 | 5.98 | 3.93 | 0.04 | 167627.91 | 26.7 | no_map |
| PYTHUSDT | IDLE | 1.2 | 2.47 | 0.14 | -0.01 | 407214.95 | 1.95 | tvl≈114,190,097 |
| CCUSDT | IDLE | 1.27 | 2.52 | 0.11 | 0.01 | 405086.18 | 11.13 | no_map |
| RWAINCUSDT | IDLE | 2.67 | 4.99 | 4.7 | 0.01 | 14885.0 | 5.55 | no_map |
| CHIPUSDT | IDLE | 1.62 | 4.93 | 0.5 | 0.02 | 121150.35 | 16.64 | no_map |
| WUSDT | IDLE | 1.18 | 2.45 | 0.34 | 0.02 | 199199.43 | 10.3 | tvl≈1,484,283,448 |
| REDUSDT | IDLE | 1.44 | 3.72 | 0.0 | 0.08 | 65069.79 | 9.96 | tvl≈2,295,785 |
| BIOUSDT | IDLE | 1.24 | 2.46 | 0.12 | 0.02 | 81957.75 | 7.88 | n/a |
| TELUSDT | IDLE | 2.13 | 4.3 | 4.06 | -0.04 | 103178.27 | 47.03 | no_map |
| KITEUSDT | IDLE | 0.72 | 1.35 | 0.59 | -0.0 | 58854.51 | 10.14 | no_map |
| HBARUSDT | IDLE | 0.59 | 1.15 | 0.24 | -0.01 | 258569.09 | 1.34 | empty_tvl |
| QNTUSDT | IDLE | 1.18 | 2.26 | 0.68 | -0.02 | 45719.58 | 9.4 | n/a |
| FLUIDUSDT | IDLE | 1.14 | 2.27 | 0.0 | 0.02 | 1933.19 | 22.12 | tvl≈2,656,991,234 |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
