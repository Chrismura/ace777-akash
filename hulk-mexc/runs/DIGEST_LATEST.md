# Hulk DIGEST — 2026-08-22T03:01:07Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 9.55 | 1.13 | 0.14 | 7410164.49 | 5.73 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 11.15 | 0.51 | 0.2 | 159595480.5 | 4.52 | n/a |
| HBARUSDT | IDLE | 2.14 | 5.29 | 0.11 | 0.1 | 993338.52 | 3.65 | empty_tvl |
| CCUSDT | IDLE | 1.88 | 8.53 | 0.0 | 0.19 | 665961.51 | 10.91 | no_map |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.49 | 0.08 | 194406.33 | 12.03 | n/a |
| CHIPUSDT | IDLE | 1.91 | 4.28 | 0.06 | -0.0 | 451657.0 | 5.95 | no_map |
| ZBCNUSDT | IDLE | 1.44 | 5.16 | 2.17 | 0.11 | 540810.47 | 23.55 | n/a |
| WUSDT | IDLE | 1.69 | 5.21 | 0.0 | 0.12 | 416666.46 | 12.84 | tvl≈1,646,654,250 |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.41 | 0.09 | 61381.79 | 44.22 | no_map |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.47 | 0.2 | 158006.21 | 10.32 | tvl≈2,314,909 |
| EDELUSDT | IDLE | 1.9 | 3.83 | 2.39 | -0.03 | 79943.62 | 33.39 | no_map |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 38.01 | no_map |
| KITEUSDT | IDLE | 1.31 | 4.03 | 0.2 | 0.12 | 62486.78 | 9.85 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.22 | 0.0 | 3930.15 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.69 | 3.97 | 0.18 | 0.09 | 172694.74 | 1.49 | n/a |
| RWAUSDT | IDLE | 1.17 | 2.31 | 0.24 | 0.05 | 56169.6 | 16.18 | no_map |
| TELUSDT | IDLE | 0.81 | 1.88 | 0.82 | 0.06 | 173120.18 | 51.65 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.31 | tvl≈2,599,456,799 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
