# Hulk DIGEST — 2026-08-22T02:09:45Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 8.42 | 1.26 | 0.13 | 6897147.71 | 1.96 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 10.03 | 0.42 | 0.16 | 154160772.75 | 2.0 | n/a |
| HBARUSDT | IDLE | 2.31 | 4.9 | 0.41 | 0.07 | 952798.99 | 1.24 | empty_tvl |
| ZBCNUSDT | IDLE | 2.51 | 9.63 | 3.33 | 0.08 | 546580.65 | 34.54 | n/a |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.19 | 0.14 | 654172.25 | 11.34 | no_map |
| CHIPUSDT | IDLE | 1.71 | 3.91 | 0.24 | 0.01 | 515480.99 | 3.04 | no_map |
| BIOUSDT | IDLE | 2.97 | 6.88 | 0.0 | 0.09 | 190558.12 | 14.84 | n/a |
| WUSDT | IDLE | 1.74 | 4.41 | 0.58 | 0.08 | 399868.52 | 15.2 | tvl≈1,638,353,418 |
| EDELUSDT | IDLE | 2.37 | 5.02 | 1.41 | -0.01 | 79596.23 | 22.03 | no_map |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.8 | 0.11 | 61137.28 | 45.71 | no_map |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.15 | 0.17 | 156817.36 | 12.96 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.31 | 4.89 | 1.28 | 0.07 | 171281.69 | 4.54 | n/a |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.69 | 0.12 | 61353.22 | 10.8 | no_map |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | no_map |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.43 | 0.04 | 179013.39 | 57.07 | no_map |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.02 | 9241.73 | 69.8 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.2 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54711.38 | 16.41 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
