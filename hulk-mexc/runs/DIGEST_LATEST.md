# Hulk DIGEST — 2026-08-21T23:14:19Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.46 | 0.12 | 6008848.45 | 2.03 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.75 | 6.77 | 0.36 | 0.14 | 138599826.46 | 1.38 | n/a |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.17 | 0.13 | 666888.74 | 10.7 | no_map |
| HBARUSDT | IDLE | 2.38 | 5.24 | 0.03 | 0.09 | 890664.31 | 1.25 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 10.14 | 0.16 | 0.15 | 511417.99 | 19.51 | n/a |
| WUSDT | IDLE | 2.74 | 6.91 | 1.26 | 0.08 | 375504.07 | 11.25 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 0.91 | 0.05 | 547411.12 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.51 | 0.02 | 187551.06 | 3.12 | n/a |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82539.65 | 32.73 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10186.51 | 16.16 | no_map |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.34 | 0.18 | 157506.62 | 19.48 | tvl≈2,226,572 |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | no_map |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.31 | 0.07 | 184985.14 | 41.19 | no_map |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.07 | 0.07 | 117887.09 | 1.5 | n/a |
| RIZEUSDT | IDLE | 1.53 | 7.18 | 0.75 | 0.1 | 58704.54 | 43.62 | no_map |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.26 | 0.09 | 61587.02 | 12.98 | no_map |
| RWAUSDT | IDLE | 1.01 | 2.0 | 0.16 | 0.04 | 54459.98 | 24.58 | no_map |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.22 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
