# Hulk DIGEST — 2026-08-22T15:55:06Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.4 | 0.04 | 51487852.37 | 1.97 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.32 | 0.02 | 216028845.98 | 2.09 | n/a |
| CCUSDT | IDLE | 1.3 | 5.65 | 2.28 | 0.09 | 758714.42 | 9.39 | no_map |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.56 | -0.02 | 1152906.87 | 2.63 | empty_tvl |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 2.06 | -0.1 | 603603.24 | 6.78 | no_map |
| WUSDT | IDLE | 0.79 | 3.17 | 2.11 | -0.02 | 553217.71 | 12.85 | tvl≈1,556,368,553 |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.8 | 0.03 | 85539.0 | 11.61 | no_map |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.88 | -0.05 | 320458.96 | 20.04 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.26 | -0.07 | 218988.64 | 6.64 | n/a |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.02 | 75087.84 | 22.81 | no_map |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.67 | -0.16 | 134316.62 | 10.11 | tvl≈2,005,037 |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.13 | 0.03 | 56494.74 | 45.5 | no_map |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.56 | -0.03 | 184248.12 | 6.33 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | -0.01 | 9586.61 | 75.23 | no_map |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.0 | 139076.08 | 42.71 | no_map |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 22.49 | tvl≈2,554,315,465 |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 56526.16 | 24.36 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
