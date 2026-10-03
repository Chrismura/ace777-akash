# Hulk DIGEST — 2026-10-03T03:47:13Z

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
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.39 | 12.89 | 1.65 | 0.02 | 4685841.95 | 5.91 | n/a |
| XRPUSDT | IDLE | 0.73 | 1.4 | 0.42 | -0.01 | 65009793.95 | 1.34 | n/a |
| ETHUSDT | IDLE | 0.44 | 0.86 | 0.13 | -0.01 | 520326739.96 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.17 | 0.32 | 0.07 | -0.01 | 864390349.12 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.8 | 6.34 | 4.2 | 0.04 | 696128.96 | 6.37 | tvl≈176,562,507 |
| EDELUSDT | IDLE | 0.61 | 4.96 | 4.0 | 0.3 | 704260.83 | 24.35 | no_map |
| HBARUSDT | IDLE | 1.0 | 2.38 | 1.97 | -0.03 | 954124.45 | 9.92 | empty_tvl |
| WUSDT | IDLE | 1.47 | 3.99 | 0.17 | 0.01 | 502670.64 | 8.13 | tvl≈1,903,324,117 |
| CCUSDT | IDLE | 0.78 | 1.69 | 1.05 | -0.01 | 523542.88 | 10.06 | no_map |
| BIOUSDT | IDLE | 2.42 | 6.23 | 0.09 | 0.05 | 100907.38 | 12.62 | n/a |
| CHIPUSDT | IDLE | 2.46 | 4.65 | 2.0 | 0.01 | 87000.17 | 16.04 | no_map |
| ZBCNUSDT | IDLE | 1.89 | 5.57 | 3.0 | -0.02 | 221104.91 | 39.33 | n/a |
| RWAINCUSDT | IDLE | 2.81 | 8.21 | 2.69 | 0.02 | 6751.24 | 68.98 | no_map |
| KITEUSDT | IDLE | 1.93 | 3.67 | 1.22 | 0.01 | 81896.0 | 8.66 | no_map |
| REDUSDT | IDLE | 1.11 | 5.21 | 2.62 | -0.05 | 119846.55 | 14.46 | tvl≈4,210,643 |
| RIZEUSDT | IDLE | 0.57 | 2.63 | 1.86 | 0.07 | 42589.56 | 52.19 | no_map |
| TELUSDT | IDLE | 0.95 | 2.82 | 1.6 | -0.07 | 153794.86 | 35.47 | no_map |
| MNSRYUSDT | IDLE | 1.01 | 1.81 | 1.36 | 0.0 | 42204.57 | 11.68 | no_map |
| FLUIDUSDT | IDLE | 1.09 | 2.06 | 1.27 | 0.05 | 6017.69 | 21.83 | tvl≈2,496,114,060 |
| RWAUSDT | IDLE | 0.32 | 0.58 | 0.36 | -0.01 | 55636.78 | 14.59 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
