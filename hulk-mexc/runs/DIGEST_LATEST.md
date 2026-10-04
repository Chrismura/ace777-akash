# Hulk DIGEST — 2026-10-04T05:59:47Z

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
| QNTUSDT | IDLE | 3.05 | 9.2 | 4.8 | 0.03 | 3553298.39 | 7.54 | n/a |
| XRPUSDT | IDLE | 0.26 | 0.5 | 0.09 | 0.0 | 16501587.76 | 1.34 | n/a |
| ETHUSDT | IDLE | 0.2 | 0.38 | 0.09 | 0.01 | 94409563.9 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.12 | 0.23 | 0.02 | 0.0 | 302370980.88 | 0.0 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.55 | 8.39 | 0.98 | 0.09 | 571758.78 | 14.22 | tvl≈1,875,753,218 |
| EDELUSDT | IDLE | 1.09 | 7.23 | 2.72 | 0.17 | 502512.28 | 41.06 | no_map |
| CCUSDT | IDLE | 1.6 | 2.8 | 2.64 | 0.04 | 352762.35 | 10.52 | no_map |
| KITEUSDT | IDLE | 2.71 | 5.26 | 3.46 | 0.04 | 80992.32 | 8.51 | no_map |
| PYTHUSDT | IDLE | 1.61 | 3.23 | 0.0 | 0.01 | 264603.13 | 3.75 | tvl≈174,809,538 |
| RWAINCUSDT | IDLE | 2.76 | 5.33 | 1.25 | 0.03 | 4827.71 | 54.97 | no_map |
| RIZEUSDT | IDLE | 1.88 | 10.49 | 8.71 | -0.18 | 53070.19 | 77.12 | no_map |
| CHIPUSDT | IDLE | 2.11 | 4.2 | 0.11 | 0.05 | 59114.77 | 15.37 | no_map |
| ZBCNUSDT | IDLE | 1.36 | 2.62 | 0.73 | -0.0 | 231457.59 | 36.18 | n/a |
| FLUIDUSDT | IDLE | 2.26 | 6.12 | 4.1 | 0.07 | 2500.44 | 21.57 | tvl≈2,498,561,582 |
| REDUSDT | IDLE | 0.77 | 2.11 | 1.55 | 0.08 | 62717.16 | 13.48 | tvl≈4,499,398 |
| BIOUSDT | IDLE | 0.72 | 1.39 | 0.32 | -0.01 | 69757.93 | 9.6 | n/a |
| HBARUSDT | IDLE | 0.72 | 1.35 | 0.56 | 0.0 | 329214.29 | 3.94 | empty_tvl |
| TELUSDT | IDLE | 1.4 | 2.58 | 2.01 | -0.01 | 131338.18 | 15.36 | no_map |
| RWAUSDT | IDLE | 0.36 | 0.66 | 0.44 | -0.0 | 55304.64 | 29.24 | no_map |
| MNSRYUSDT | IDLE | 0.33 | 0.62 | 0.25 | 0.0 | 36416.68 | 22.02 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
