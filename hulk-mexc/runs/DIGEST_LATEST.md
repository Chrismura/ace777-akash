# Hulk DIGEST — 2026-09-10T15:15:25Z

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
| ETHUSDT | IDLE | 1.47 | 2.77 | 1.19 | -0.02 | 425074959.86 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.39 | 2.51 | 1.74 | -0.04 | 45001846.46 | 2.21 | n/a |
| BTCUSDT | IDLE | 0.94 | 1.74 | 0.92 | -0.01 | 553765177.81 | 0.0 | no_map |
| RIZEUSDT | IDLE | 1.24 | 68.27 | 16.5 | -0.51 | 124834.57 | 100.81 | no_map |
| PYTHUSDT | IDLE | 1.41 | 4.14 | 1.31 | -0.05 | 976695.75 | 1.92 | tvl≈116,320,814 |
| CCUSDT | IDLE | 1.45 | 2.68 | 1.41 | -0.03 | 676615.16 | 10.89 | no_map |
| ZBCNUSDT | IDLE | 2.5 | 4.54 | 3.11 | 0.03 | 184449.53 | 31.01 | n/a |
| EDELUSDT | IDLE | 1.71 | 6.28 | 4.09 | 0.03 | 227326.63 | 18.13 | no_map |
| WUSDT | IDLE | 0.87 | 2.5 | 0.25 | -0.04 | 240309.74 | 2.08 | tvl≈1,477,046,091 |
| BIOUSDT | IDLE | 1.5 | 2.96 | 1.98 | -0.06 | 78230.95 | 3.97 | n/a |
| KITEUSDT | IDLE | 1.22 | 2.62 | 1.02 | -0.05 | 56144.15 | 13.75 | no_map |
| HBARUSDT | IDLE | 1.22 | 2.27 | 1.13 | -0.03 | 318341.58 | 1.32 | empty_tvl |
| REDUSDT | IDLE | 1.03 | 2.57 | 1.12 | -0.06 | 66589.15 | 17.99 | tvl≈2,266,018 |
| CHIPUSDT | IDLE | 0.67 | 3.6 | 2.59 | -0.18 | 92002.94 | 14.78 | no_map |
| RWAINCUSDT | IDLE | 1.09 | 1.93 | 1.61 | -0.02 | 4976.79 | 39.58 | no_map |
| TELUSDT | IDLE | 1.86 | 3.48 | 1.65 | -0.03 | 82282.73 | 61.71 | no_map |
| FLUIDUSDT | IDLE | 1.75 | 3.36 | 2.33 | -0.08 | 2246.54 | 20.01 | tvl≈2,627,661,643 |
| RWAUSDT | IDLE | 1.32 | 2.37 | 1.79 | -0.04 | 53901.34 | 7.6 | no_map |
| QNTUSDT | IDLE | 1.36 | 2.53 | 1.31 | -0.02 | 39727.95 | 6.1 | n/a |
| MNSRYUSDT | IDLE | 0.98 | 1.76 | 1.37 | -0.03 | 26569.06 | 54.5 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
