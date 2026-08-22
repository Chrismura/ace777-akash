# Hulk DIGEST — 2026-08-22T02:32:13Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 10.52 | 1.16 | 0.15 | 7071742.56 | 1.92 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.37 | 11.1 | 0.06 | 0.17 | 155118193.79 | 0.66 | n/a |
| HBARUSDT | IDLE | 2.37 | 5.4 | 0.05 | 0.09 | 968212.7 | 1.23 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 9.63 | 1.75 | 0.1 | 545063.34 | 32.11 | n/a |
| CCUSDT | IDLE | 1.72 | 6.49 | 0.07 | 0.15 | 652819.25 | 3.47 | no_map |
| CHIPUSDT | IDLE | 2.21 | 5.1 | 0.0 | -0.01 | 469977.84 | 3.0 | no_map |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.12 | 8.18 | 0.53 | 0.1 | 193209.36 | 5.88 | n/a |
| WUSDT | IDLE | 1.94 | 5.62 | 0.08 | 0.1 | 406117.05 | 12.96 | tvl≈1,646,654,250 |
| EDELUSDT | IDLE | 2.49 | 5.02 | 3.15 | -0.04 | 79698.01 | 33.58 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.03 | 0.1 | 61419.22 | 45.71 | no_map |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.41 | 0.17 | 157850.25 | 8.92 | tvl≈2,314,909 |
| QNTUSDT | IDLE | 2.28 | 5.2 | 0.0 | 0.08 | 171067.34 | 4.47 | n/a |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.01 | 9358.7 | 37.95 | no_map |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.14 | 0.12 | 61865.42 | 9.85 | no_map |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | no_map |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.07 | 0.05 | 178482.92 | 51.76 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 22.41 | tvl≈2,599,456,799 |
| RWAUSDT | IDLE | 1.08 | 2.17 | 0.0 | 0.04 | 55087.03 | 32.65 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
