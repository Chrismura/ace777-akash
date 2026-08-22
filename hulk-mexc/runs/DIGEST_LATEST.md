# Hulk DIGEST — 2026-08-22T04:57:24Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 0.99 | 0.2 | 12914510.23 | 3.62 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 17.46 | 0.57 | 0.26 | 180130766.47 | 5.41 | n/a |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 9.65 | 0.0 | 0.15 | 1080538.4 | 2.32 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.28 | 0.2 | 741463.17 | 8.2 | no_map |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.62 | 0.02 | 453972.75 | 2.99 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 8.62 | 0.79 | 0.15 | 447762.22 | 11.52 | tvl≈1,672,612,247 |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 8.28 | 0.29 | 0.08 | 201718.23 | 2.91 | n/a |
| ZBCNUSDT | IDLE | 1.4 | 4.29 | 0.67 | 0.11 | 538018.27 | 16.06 | n/a |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10338.25 | 21.57 | no_map |
| EDELUSDT | IDLE | 2.0 | 4.07 | 2.39 | -0.02 | 80270.01 | 33.31 | no_map |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.39 | 0.1 | 58622.95 | 46.02 | no_map |
| KITEUSDT | IDLE | 1.73 | 6.54 | 0.02 | 0.15 | 68310.7 | 10.46 | no_map |
| QNTUSDT | IDLE | 2.6 | 9.16 | 4.51 | 0.1 | 186791.11 | 51.28 | n/a |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.3 | 0.21 | 157975.53 | 10.34 | tvl≈2,314,909 |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.44 | 0.1 | 183333.2 | 14.88 | no_map |
| RWAUSDT | IDLE | 1.58 | 3.13 | 0.16 | 0.06 | 56544.95 | 15.99 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3692.42 | 20.74 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
