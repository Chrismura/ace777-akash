# Hulk DIGEST — 2026-08-21T22:34:25Z

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
| PYTHUSDT | IDLE | 1.38 | 5.17 | 0.69 | 0.11 | 5814919.25 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.57 | 5.84 | 0.27 | 0.14 | 134514892.02 | 2.08 | n/a |
| CCUSDT | IDLE | 1.75 | 6.49 | 0.0 | 0.13 | 658163.27 | 10.67 | no_map |
| HBARUSDT | IDLE | 2.24 | 4.71 | 1.11 | 0.07 | 868929.38 | 8.91 | empty_tvl |
| WUSDT | IDLE | 2.5 | 5.3 | 0.78 | 0.08 | 370631.78 | 14.46 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.42 | 0.06 | 533901.79 | 6.11 | no_map |
| ZBCNUSDT | IDLE | 1.59 | 6.77 | 0.65 | 0.11 | 502691.0 | 19.73 | n/a |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.48 | 0.02 | 188319.8 | 6.24 | n/a |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.99 | 0.18 | 155982.69 | 12.92 | tvl≈2,226,572 |
| RWAINCUSDT | IDLE | 2.22 | 4.07 | 2.43 | 0.02 | 10212.45 | 16.17 | no_map |
| EDELUSDT | IDLE | 2.36 | 5.04 | 1.2 | -0.04 | 82619.34 | 76.97 | no_map |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.82 | 0.05 | 187141.58 | 15.54 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | no_map |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.27 | 0.11 | 61542.06 | 12.0 | no_map |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.72 | 0.06 | 56355.9 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.92 | 3.84 | 0.0 | 0.06 | 72297.93 | 6.08 | n/a |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.0 | 0.04 | 54126.56 | 24.6 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.78 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
