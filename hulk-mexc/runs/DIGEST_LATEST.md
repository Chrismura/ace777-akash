# Hulk DIGEST — 2026-08-22T17:23:05Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.77 | 8.48 | 1.72 | 0.1 | 49143541.61 | 3.85 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.46 | 0.06 | 213803609.04 | 1.35 | n/a |
| CCUSDT | IDLE | 0.94 | 4.25 | 0.38 | 0.12 | 766962.05 | 7.52 | no_map |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.92 | 0.01 | 1096536.14 | 6.45 | empty_tvl |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.73 | -0.1 | 631339.86 | 6.69 | no_map |
| WUSDT | IDLE | 0.59 | 2.58 | 0.02 | 0.0 | 533561.82 | 9.45 | tvl≈1,557,321,639 |
| BIOUSDT | IDLE | 1.19 | 7.96 | 6.65 | -0.08 | 227295.21 | 3.37 | n/a |
| ZBCNUSDT | IDLE | 1.26 | 3.45 | 1.19 | -0.01 | 306363.22 | 16.34 | n/a |
| EDELUSDT | IDLE | 1.76 | 3.11 | 2.68 | -0.02 | 74907.79 | 22.99 | no_map |
| KITEUSDT | IDLE | 1.39 | 3.22 | 0.9 | 0.05 | 89684.17 | 7.08 | no_map |
| REDUSDT | IDLE | 0.54 | 5.67 | 2.5 | -0.14 | 121718.74 | 13.46 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.12 | 2.63 | 0.82 | 0.04 | 46109.57 | 45.71 | no_map |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.88 | -0.01 | 181219.62 | 4.72 | n/a |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.73 | 0.01 | 135141.79 | 32.1 | no_map |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 107.7 | no_map |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.6 | tvl≈2,548,281,440 |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
