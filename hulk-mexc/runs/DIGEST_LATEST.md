# Hulk DIGEST — 2026-08-22T03:31:05Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 11.15 | 0.69 | 0.17 | 7826455.85 | 1.87 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.53 | 0.21 | 164554297.85 | 8.26 | n/a |
| HBARUSDT | IDLE | 2.32 | 6.48 | 0.01 | 0.12 | 1020007.49 | 1.2 | empty_tvl |
| CCUSDT | IDLE | 2.0 | 8.96 | 2.35 | 0.16 | 682160.84 | 5.99 | no_map |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.37 | 0.08 | 198218.75 | 3.0 | n/a |
| CHIPUSDT | IDLE | 2.01 | 4.43 | 0.5 | -0.03 | 452614.19 | 2.97 | no_map |
| ZBCNUSDT | IDLE | 1.4 | 5.16 | 1.16 | 0.12 | 538027.58 | 19.98 | n/a |
| WUSDT | IDLE | 1.81 | 5.79 | 0.29 | 0.12 | 423623.53 | 7.88 | tvl≈1,672,612,247 |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.03 | 79975.5 | 22.47 | no_map |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.55 | 0.1 | 59535.95 | 39.11 | no_map |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.56 | 0.22 | 157691.64 | 8.73 | tvl≈2,314,909 |
| RWAINCUSDT | IDLE | 1.87 | 3.44 | 2.06 | 0.01 | 9365.21 | 21.61 | no_map |
| KITEUSDT | IDLE | 1.39 | 4.5 | 0.1 | 0.12 | 67720.51 | 13.36 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.76 | 4.29 | 0.01 | 0.09 | 174197.13 | 7.41 | n/a |
| RWAUSDT | IDLE | 1.37 | 2.72 | 0.16 | 0.05 | 56331.92 | 24.13 | no_map |
| TELUSDT | IDLE | 1.02 | 2.45 | 0.41 | 0.07 | 173543.19 | 50.97 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 47.17 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
