# Hulk DIGEST — 2026-10-05T07:34:13Z

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
| QNTUSDT | IDLE | 2.18 | 5.23 | 0.67 | -0.04 | 2995194.63 | 1.95 | n/a |
| XRPUSDT | IDLE | 1.02 | 1.97 | 0.47 | 0.02 | 28569985.05 | 1.31 | n/a |
| ETHUSDT | IDLE | 0.82 | 1.58 | 0.46 | 0.01 | 211664020.67 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.79 | 1.51 | 0.48 | 0.02 | 499062096.49 | 0.0 | no_map |
| WUSDT | IDLE | 1.87 | 3.56 | 1.26 | -0.0 | 810451.03 | 10.97 | tvl≈1,899,392,202 |
| PYTHUSDT | IDLE | 2.21 | 4.4 | 0.15 | -0.0 | 456598.32 | 2.51 | tvl≈172,707,211 |
| REDUSDT | IDLE | 3.11 | 5.5 | 4.77 | -0.03 | 83862.36 | 13.9 | tvl≈4,480,214 |
| EDELUSDT | IDLE | 1.32 | 3.0 | 2.07 | 0.04 | 444093.88 | 24.41 | no_map |
| CCUSDT | IDLE | 1.29 | 2.37 | 1.45 | 0.02 | 282628.26 | 10.25 | no_map |
| HBARUSDT | IDLE | 1.2 | 2.29 | 0.69 | 0.02 | 540112.07 | 3.84 | empty_tvl |
| KITEUSDT | IDLE | 1.76 | 3.8 | 2.31 | -0.07 | 72333.98 | 10.4 | no_map |
| ZBCNUSDT | IDLE | 1.11 | 2.46 | 0.28 | 0.03 | 215858.47 | 2.32 | n/a |
| BIOUSDT | IDLE | 1.72 | 3.42 | 0.1 | 0.0 | 81722.99 | 9.65 | n/a |
| CHIPUSDT | IDLE | 1.35 | 4.52 | 1.36 | 0.09 | 99972.92 | 10.1 | no_map |
| RIZEUSDT | IDLE | 1.23 | 10.74 | 9.38 | 0.25 | 41530.78 | 82.68 | no_map |
| RWAINCUSDT | IDLE | 2.06 | 5.28 | 1.55 | -0.05 | 4534.37 | 98.85 | no_map |
| TELUSDT | IDLE | 2.34 | 4.26 | 2.8 | 0.02 | 138900.15 | 50.66 | no_map |
| FLUIDUSDT | IDLE | 1.25 | 2.47 | 0.25 | 0.04 | 5289.56 | 21.61 | tvl≈2,533,694,313 |
| RWAUSDT | IDLE | 0.7 | 1.24 | 1.08 | -0.0 | 51926.08 | 7.31 | no_map |
| MNSRYUSDT | IDLE | 0.23 | 0.44 | 0.14 | 0.0 | 44821.29 | 5.15 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
