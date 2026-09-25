# Hulk DIGEST — 2026-09-25T22:47:03Z

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
| XRPUSDT | IDLE | 1.01 | 1.94 | 0.49 | 0.03 | 115824429.5 | 1.27 | n/a |
| ETHUSDT | IDLE | 0.42 | 0.81 | 0.22 | 0.0 | 324628649.6 | 0.22 | no_map |
| BTCUSDT | IDLE | 0.33 | 0.65 | 0.13 | -0.0 | 685157472.21 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.01 | 5.87 | 0.12 | 0.12 | 1236516.79 | 1.33 | tvl≈162,005,824 |
| CCUSDT | IDLE | 1.61 | 6.68 | 2.37 | 0.15 | 847821.18 | 7.72 | no_map |
| HBARUSDT | IDLE | 1.77 | 3.46 | 0.53 | 0.03 | 902301.03 | 3.15 | empty_tvl |
| EDELUSDT | IDLE | 2.61 | 4.68 | 3.66 | 0.0 | 180532.99 | 6.78 | no_map |
| WUSDT | IDLE | 1.72 | 3.35 | 0.62 | 0.05 | 410354.61 | 9.78 | tvl≈1,824,493,843 |
| RIZEUSDT | IDLE | 1.28 | 18.86 | 14.08 | -0.0 | 111066.8 | 47.34 | no_map |
| ZBCNUSDT | IDLE | 1.84 | 4.18 | 2.94 | 0.06 | 253044.97 | 18.46 | n/a |
| CHIPUSDT | IDLE | 1.99 | 5.09 | 0.38 | 0.04 | 160590.23 | 14.05 | no_map |
| KITEUSDT | IDLE | 1.8 | 3.49 | 0.69 | 0.02 | 80309.29 | 9.79 | no_map |
| QNTUSDT | IDLE | 0.58 | 2.42 | 1.23 | 0.1 | 558326.06 | 6.14 | n/a |
| BIOUSDT | IDLE | 1.1 | 3.35 | 0.63 | 0.08 | 113368.93 | 6.04 | n/a |
| REDUSDT | IDLE | 0.78 | 1.87 | 1.16 | 0.09 | 137377.84 | 14.95 | tvl≈3,156,241 |
| RWAINCUSDT | IDLE | 0.83 | 2.63 | 0.75 | -0.09 | 14313.6 | 20.11 | no_map |
| TELUSDT | IDLE | 1.17 | 2.15 | 1.32 | 0.0 | 116211.89 | 48.72 | no_map |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
