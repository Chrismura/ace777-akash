# Hulk DIGEST — 2026-08-19T20:18:48Z

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
| XRPUSDT | IDLE | 2.22 | 4.4 | 0.25 | 0.07 | 27536146.93 | 0.93 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 15.44 | 7.83 | 0.01 | 120514.66 | 11.6 | tvl≈1,739,280 |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.29 | 9.71 | 0.67 | 0.1 | 302904.5 | 11.08 | no_map |
| EDELUSDT | IDLE | 3.49 | 15.36 | 3.33 | 0.12 | 76896.22 | 23.81 | no_map |
| PYTHUSDT | IDLE | 2.98 | 7.47 | 0.5 | 0.08 | 268856.11 | 4.8 | tvl≈90,381,317 |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.94 | 18.38 | 7.62 | 0.09 | 169654.27 | 19.16 | no_map |
| RIZEUSDT | IDLE | 4.19 | 8.15 | 2.65 | -0.02 | 45755.6 | 49.24 | no_map |
| BIOUSDT | IDLE | 2.19 | 10.57 | 6.92 | 0.12 | 140090.13 | 3.63 | n/a |
| ZBCNUSDT | IDLE | 2.24 | 6.31 | 0.36 | 0.1 | 200195.29 | 3.48 | n/a |
| CHIPUSDT | IDLE | 1.64 | 5.02 | 3.39 | 0.05 | 181254.17 | 3.58 | no_map |
| WUSDT | IDLE | 1.85 | 3.55 | 0.99 | 0.05 | 183197.4 | 14.16 | tvl≈1,418,339,777 |
| QAITUSDT | IDLE | 2.53 | 7.05 | 1.07 | 0.03 | 11289.64 | 62.16 | no_map |
| KITEUSDT | IDLE | 1.89 | 3.6 | 1.19 | 0.04 | 57236.33 | 16.76 | no_map |
| HBARUSDT | IDLE | 1.73 | 3.3 | 1.06 | 0.05 | 255279.19 | 1.43 | empty_tvl |
| RWAINCUSDT | IDLE | 1.16 | 3.23 | 3.13 | 0.04 | 17042.7 | 22.96 | no_map |
| FLUIDUSDT | IDLE | 2.26 | 4.81 | 3.39 | 0.03 | 2850.08 | 22.09 | tvl≈2,416,918,092 |
| QNTUSDT | IDLE | 1.16 | 2.29 | 0.22 | 0.04 | 40016.36 | 1.71 | n/a |
| RWAUSDT | IDLE | 0.77 | 1.4 | 0.95 | -0.0 | 54258.72 | 8.72 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
