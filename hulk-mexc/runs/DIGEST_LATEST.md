# Hulk DIGEST — 2026-08-22T17:11:33Z

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
| PYTHUSDT | IDLE | 1.72 | 8.48 | 0.11 | 0.1 | 49184429.52 | 5.68 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.34 | 7.64 | 3.92 | 0.04 | 214082775.74 | 2.04 | n/a |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.07 | -0.01 | 1108863.85 | 3.88 | empty_tvl |
| CCUSDT | IDLE | 0.93 | 4.25 | 0.06 | 0.11 | 771934.87 | 6.67 | no_map |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.06 | -0.1 | 631121.93 | 3.36 | no_map |
| WUSDT | IDLE | 0.61 | 2.58 | 0.51 | -0.01 | 534778.14 | 11.61 | tvl≈1,556,368,553 |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.67 | -0.08 | 226299.4 | 3.34 | n/a |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.24 | -0.01 | 310361.55 | 23.45 | n/a |
| EDELUSDT | IDLE | 1.72 | 3.0 | 2.91 | -0.03 | 74857.67 | 34.5 | no_map |
| KITEUSDT | IDLE | 1.36 | 3.22 | 0.46 | 0.04 | 87591.13 | 11.47 | no_map |
| REDUSDT | IDLE | 0.54 | 5.67 | 3.09 | -0.13 | 122352.32 | 10.82 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.44 | 0.05 | 46190.38 | 45.5 | no_map |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.13 | -0.02 | 181159.69 | 1.58 | n/a |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 86.25 | no_map |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.05 | -0.0 | 136251.98 | 37.52 | no_map |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.16 | 0.02 | 56146.75 | 8.09 | no_map |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 20.14 | tvl≈2,551,700,555 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
