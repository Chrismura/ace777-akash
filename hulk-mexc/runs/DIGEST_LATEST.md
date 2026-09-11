# Hulk DIGEST — 2026-09-11T12:19:27Z

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
| XRPUSDT | IDLE | 1.66 | 2.98 | 2.24 | -0.03 | 39779195.71 | 0.75 | n/a |
| ETHUSDT | IDLE | 0.75 | 1.34 | 1.05 | -0.0 | 463451231.38 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.52 | 0.94 | 0.6 | -0.01 | 511827907.66 | 0.0 | no_map |
| CCUSDT | IDLE | 2.8 | 5.15 | 3.0 | -0.04 | 438700.05 | 8.28 | no_map |
| PYTHUSDT | IDLE | 2.21 | 4.04 | 2.6 | -0.02 | 365712.26 | 1.98 | tvl≈114,862,105 |
| RIZEUSDT | IDLE | 1.21 | 24.77 | 8.03 | 0.11 | 126889.19 | 100.7 | no_map |
| WUSDT | IDLE | 1.86 | 3.32 | 2.64 | -0.02 | 128377.07 | 14.92 | tvl≈1,479,891,419 |
| BIOUSDT | IDLE | 1.75 | 3.16 | 2.23 | -0.04 | 79932.87 | 4.07 | n/a |
| ZBCNUSDT | IDLE | 1.55 | 2.95 | 0.99 | -0.02 | 189337.77 | 37.61 | n/a |
| QNTUSDT | IDLE | 2.91 | 5.13 | 4.64 | -0.03 | 41699.14 | 7.82 | n/a |
| REDUSDT | IDLE | 1.69 | 3.09 | 2.0 | -0.03 | 59558.65 | 20.03 | tvl≈2,196,779 |
| CHIPUSDT | IDLE | 1.13 | 3.47 | 1.49 | -0.06 | 129380.6 | 10.97 | no_map |
| RWAINCUSDT | IDLE | 1.69 | 3.14 | 1.58 | 0.02 | 4306.18 | 5.53 | no_map |
| KITEUSDT | IDLE | 1.36 | 2.48 | 1.55 | -0.02 | 57790.04 | 10.22 | no_map |
| EDELUSDT | IDLE | 0.64 | 2.87 | 1.86 | -0.07 | 197786.65 | 28.42 | no_map |
| HBARUSDT | IDLE | 1.4 | 2.55 | 1.73 | -0.03 | 195448.37 | 1.35 | empty_tvl |
| TELUSDT | IDLE | 1.2 | 2.17 | 1.49 | -0.04 | 100061.39 | 52.43 | no_map |
| FLUIDUSDT | IDLE | 1.14 | 1.98 | 1.94 | -0.04 | 2304.28 | 22.09 | tvl≈2,658,749,875 |
| MNSRYUSDT | IDLE | 0.33 | 0.59 | 0.46 | -0.01 | 38004.78 | 5.59 | no_map |
| RWAUSDT | IDLE | 0.24 | 0.46 | 0.15 | -0.01 | 49537.18 | 15.19 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
