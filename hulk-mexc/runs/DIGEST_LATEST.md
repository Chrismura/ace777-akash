# Hulk DIGEST — 2026-08-22T16:19:05Z

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
| PYTHUSDT | IDLE | 1.5 | 7.24 | 1.15 | 0.05 | 51442844.65 | 3.94 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.36 | 7.64 | 5.08 | 0.04 | 215441428.44 | 0.69 | n/a |
| HBARUSDT | IDLE | 0.83 | 3.03 | 1.64 | -0.01 | 1139808.19 | 5.2 | empty_tvl |
| CCUSDT | IDLE | 0.99 | 4.14 | 2.71 | 0.09 | 767816.4 | 5.99 | no_map |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.93 | -0.1 | 625946.33 | 3.35 | no_map |
| WUSDT | IDLE | 0.64 | 2.58 | 1.44 | -0.02 | 545674.56 | 13.85 | tvl≈1,556,368,553 |
| ZBCNUSDT | IDLE | 1.34 | 3.49 | 2.44 | -0.05 | 316091.79 | 14.99 | n/a |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.7 | -0.07 | 219740.59 | 3.31 | n/a |
| KITEUSDT | IDLE | 1.87 | 4.35 | 1.2 | 0.04 | 85417.53 | 12.42 | no_map |
| EDELUSDT | IDLE | 1.44 | 2.52 | 2.35 | -0.03 | 74788.13 | 22.88 | no_map |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.08 | -0.11 | 133871.53 | 11.87 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.12 | 0.03 | 56554.57 | 45.5 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.36 | -0.02 | 184115.81 | 1.58 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 8654.22 | 64.45 | no_map |
| TELUSDT | IDLE | 0.96 | 2.37 | 1.42 | 0.0 | 137440.91 | 48.01 | no_map |
| RWAUSDT | IDLE | 0.56 | 1.06 | 0.4 | 0.02 | 56290.99 | 32.49 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 21.67 | tvl≈2,554,315,465 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
