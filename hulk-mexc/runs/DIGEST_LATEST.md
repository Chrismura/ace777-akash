# Hulk DIGEST — 2026-09-26T08:54:00Z

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
| XRPUSDT | IDLE | 0.71 | 1.29 | 0.9 | 0.01 | 109165764.01 | 1.29 | n/a |
| ETHUSDT | IDLE | 0.28 | 0.53 | 0.22 | 0.0 | 277168317.56 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.28 | 0.54 | 0.11 | -0.0 | 584424998.51 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.04 | 3.99 | 0.56 | 0.07 | 1170836.37 | 1.33 | tvl≈167,416,854 |
| CCUSDT | IDLE | 1.63 | 7.25 | 2.37 | 0.14 | 1059605.3 | 6.61 | no_map |
| QNTUSDT | IDLE | 2.42 | 9.16 | 3.98 | 0.04 | 770952.9 | 23.26 | n/a |
| WUSDT | IDLE | 2.11 | 4.78 | 0.11 | 0.08 | 476106.58 | 7.06 | tvl≈1,848,318,253 |
| HBARUSDT | IDLE | 0.74 | 1.42 | 0.34 | 0.02 | 836626.07 | 1.06 | empty_tvl |
| KITEUSDT | IDLE | 1.98 | 4.32 | 2.81 | 0.05 | 77402.14 | 11.03 | no_map |
| RWAINCUSDT | IDLE | 2.31 | 4.42 | 1.27 | 0.02 | 8385.98 | 4.93 | no_map |
| EDELUSDT | IDLE | 1.58 | 3.04 | 0.83 | 0.02 | 175858.13 | 6.68 | no_map |
| ZBCNUSDT | IDLE | 1.27 | 2.82 | 1.33 | 0.04 | 246390.19 | 12.73 | n/a |
| CHIPUSDT | IDLE | 1.51 | 2.89 | 0.99 | 0.04 | 146297.73 | 16.3 | no_map |
| REDUSDT | IDLE | 0.84 | 1.53 | 1.04 | 0.03 | 59549.25 | 6.45 | tvl≈3,123,109 |
| BIOUSDT | IDLE | 0.53 | 1.3 | 0.52 | 0.04 | 122233.55 | 3.07 | n/a |
| RIZEUSDT | IDLE | 0.25 | 3.43 | 1.06 | -0.25 | 62198.88 | 25.57 | no_map |
| TELUSDT | IDLE | 0.89 | 1.61 | 1.16 | -0.01 | 117603.73 | 30.84 | no_map |
| RWAUSDT | IDLE | 0.63 | 1.19 | 0.44 | -0.01 | 53160.07 | 7.38 | no_map |
| FLUIDUSDT | IDLE | 0.96 | 1.83 | 0.62 | 0.0 | 3382.73 | 22.25 | tvl≈2,580,811,423 |
| MNSRYUSDT | IDLE | 0.32 | 0.63 | 0.11 | 0.01 | 40781.52 | 10.19 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
