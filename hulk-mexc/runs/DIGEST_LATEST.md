# Hulk DIGEST — 2026-08-22T03:47:35Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 11.77 | 1.61 | 0.17 | 8470472.88 | 16.93 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.48 | 0.2 | 165471302.88 | 4.45 | n/a |
| HBARUSDT | IDLE | 2.43 | 6.93 | 0.98 | 0.1 | 1033387.86 | 2.42 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 10.39 | 0.52 | 0.2 | 696882.61 | 15.68 | no_map |
| CHIPUSDT | IDLE | 2.49 | 5.36 | 1.41 | -0.03 | 453901.74 | 5.96 | no_map |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.05 | 0.08 | 199262.21 | 2.99 | n/a |
| ZBCNUSDT | IDLE | 1.39 | 5.16 | 0.79 | 0.14 | 537132.15 | 22.26 | n/a |
| WUSDT | IDLE | 1.81 | 5.83 | 0.25 | 0.12 | 424184.14 | 9.84 | tvl≈1,672,612,247 |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.08 | 0.11 | 59481.04 | 45.81 | no_map |
| REDUSDT | IDLE | 0.91 | 7.96 | 3.1 | 0.22 | 157993.84 | 18.81 | tvl≈2,314,909 |
| EDELUSDT | IDLE | 1.98 | 3.95 | 2.82 | -0.03 | 80476.83 | 55.59 | no_map |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 38.1 | no_map |
| KITEUSDT | IDLE | 1.47 | 4.86 | 0.24 | 0.12 | 67657.23 | 9.78 | no_map |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.47 | 0.09 | 174994.9 | 4.44 | n/a |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.08 | 0.06 | 56191.05 | 8.02 | no_map |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.56 | 0.07 | 173774.25 | 51.15 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.21 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
