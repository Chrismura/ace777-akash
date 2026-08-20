# Hulk DIGEST — 2026-08-20T18:26:27Z

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
| XRPUSDT | IDLE | 2.1 | 13.07 | 5.02 | 0.21 | 97353525.83 | 3.13 | n/a |
| PYTHUSDT | IDLE | 1.08 | 3.0 | 1.73 | 0.1 | 1253901.64 | 2.28 | tvl≈100,469,598 |
| ZBCNUSDT | IDLE | 4.08 | 12.78 | 2.17 | 0.1 | 279157.94 | 26.16 | n/a |
| CCUSDT | IDLE | 2.02 | 3.54 | 3.3 | 0.03 | 501799.44 | 7.88 | no_map |
| CHIPUSDT | IDLE | 2.4 | 6.68 | 5.97 | 0.04 | 305200.13 | 6.83 | no_map |
| WUSDT | IDLE | 2.31 | 4.39 | 1.52 | 0.06 | 317407.25 | 6.73 | tvl≈1,515,037,702 |
| HBARUSDT | IDLE | 1.62 | 2.85 | 2.55 | 0.05 | 483650.6 | 1.38 | empty_tvl |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.57 | 16.68 | 1.38 | 0.24 | 175814.18 | 51.71 | no_map |
| KITEUSDT | IDLE | 2.06 | 3.89 | 1.51 | 0.03 | 64428.85 | 14.26 | no_map |
| RWAINCUSDT | IDLE | 2.19 | 4.37 | 0.05 | 0.06 | 6771.46 | 33.06 | no_map |
| REDUSDT | IDLE | 0.75 | 5.12 | 4.14 | 0.09 | 185580.49 | 12.51 | tvl≈1,907,253 |
| BIOUSDT | IDLE | 0.53 | 3.08 | 0.06 | 0.09 | 238828.75 | 6.44 | n/a |
| EDELUSDT | IDLE | 1.09 | 5.1 | 0.22 | 0.12 | 97046.79 | 21.6 | no_map |
| RIZEUSDT | IDLE | 1.01 | 5.87 | 5.28 | 0.05 | 59339.82 | 49.03 | no_map |
| QAITUSDT | IDLE | 1.73 | 3.24 | 1.49 | -0.01 | 5250.42 | 62.35 | no_map |
| QNTUSDT | IDLE | 1.66 | 4.02 | 3.68 | 0.07 | 64701.25 | 3.25 | n/a |
| RWAUSDT | IDLE | 0.98 | 1.83 | 0.85 | 0.01 | 53808.59 | 8.62 | no_map |
| FLUIDUSDT | IDLE | 1.09 | 2.55 | 0.0 | 0.08 | 2310.91 | 21.13 | tvl≈2,536,367,120 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
