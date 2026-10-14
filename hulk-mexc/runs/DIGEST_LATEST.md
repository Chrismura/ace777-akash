# Hulk DIGEST — 2026-10-14T00:10:45Z

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
| WUSDT | IDLE | 1.55 | 10.24 | 4.89 | -0.11 | 4458668.1 | 8.3 | tvl≈1,675,554,082 |
| PYTHUSDT | IDLE | 1.11 | 3.48 | 2.55 | -0.02 | 2086275.68 | 2.55 | tvl≈174,714,842 |
| QNTUSDT | IDLE | 1.86 | 6.22 | 5.46 | -0.06 | 1744404.5 | 1.9 | n/a |
| XRPUSDT | IDLE | 0.5 | 0.91 | 0.59 | 0.03 | 33456180.7 | 2.19 | n/a |
| ETHUSDT | IDLE | 0.38 | 0.7 | 0.46 | 0.03 | 195115228.59 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.26 | 0.48 | 0.3 | 0.02 | 369396947.9 | 0.0 | no_map |
| CCUSDT | IDLE | 1.27 | 3.41 | 2.71 | 0.05 | 617569.85 | 2.4 | no_map |
| RWAINCUSDT | IDLE | 2.16 | 3.89 | 2.88 | 0.0 | 32106.8 | 19.77 | no_map |
| EDELUSDT | IDLE | 1.03 | 2.05 | 1.67 | 0.03 | 215862.71 | 8.77 | no_map |
| ZBCNUSDT | IDLE | 1.03 | 1.88 | 1.26 | -0.0 | 223445.62 | 17.27 | n/a |
| RIZEUSDT | IDLE | 1.57 | 5.26 | 1.8 | 0.0 | 50576.31 | 56.75 | no_map |
| CHIPUSDT | IDLE | 1.1 | 2.31 | 0.4 | -0.01 | 103599.48 | 19.04 | no_map |
| TELUSDT | IDLE | 2.28 | 4.31 | 1.71 | 0.04 | 117229.92 | 33.61 | no_map |
| REDUSDT | IDLE | 0.82 | 1.64 | 0.0 | 0.04 | 124310.19 | 14.0 | tvl≈3,913,224 |
| KITEUSDT | IDLE | 0.9 | 1.77 | 0.25 | 0.05 | 58608.45 | 10.02 | no_map |
| BIOUSDT | IDLE | 0.6 | 1.16 | 0.22 | 0.03 | 73886.5 | 7.2 | n/a |
| HBARUSDT | IDLE | 0.8 | 1.43 | 1.1 | 0.01 | 286430.12 | 3.44 | empty_tvl |
| FLUIDUSDT | IDLE | 1.39 | 2.98 | 0.0 | 0.07 | 22534.01 | 19.87 | tvl≈2,376,837,942 |
| MNSRYUSDT | IDLE | 0.22 | 0.42 | 0.15 | 0.0 | 37530.45 | 11.17 | no_map |
| RWAUSDT | IDLE | 0.17 | 0.31 | 0.15 | 0.01 | 52014.78 | 15.48 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
