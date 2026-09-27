# Hulk DIGEST — 2026-09-27T08:33:45Z

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
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 13.56 | 1.95 | 0.2 | 2035419.49 | 11.18 | tvl≈1,884,286,634 |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.17 | 9.68 | 1.86 | 0.16 | 1889456.4 | 13.79 | tvl≈188,329,996 |
| QNTUSDT | IDLE | 0.77 | 15.83 | 8.73 | 0.69 | 5028548.39 | 11.28 | n/a |
| XRPUSDT | IDLE | 1.22 | 2.43 | 0.08 | -0.01 | 41741046.93 | 1.3 | n/a |
| ETHUSDT | IDLE | 0.52 | 1.04 | 0.03 | 0.01 | 146765927.1 | 0.37 | no_map |
| BTCUSDT | IDLE | 0.32 | 0.64 | 0.0 | 0.01 | 364080178.74 | 0.0 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 16.11 | 11.43 | -0.01 | 50650.18 | 51.59 | no_map |
| CCUSDT | IDLE | 1.67 | 3.18 | 1.12 | -0.0 | 644835.9 | 5.86 | no_map |
| HBARUSDT | IDLE | 1.84 | 3.64 | 0.24 | 0.01 | 616082.42 | 2.09 | empty_tvl |
| EDELUSDT | IDLE | 2.17 | 5.38 | 2.92 | -0.03 | 146164.54 | 10.34 | no_map |
| REDUSDT | IDLE | 2.59 | 5.15 | 0.2 | 0.04 | 61513.25 | 12.42 | tvl≈3,103,022 |
| ZBCNUSDT | IDLE | 1.52 | 2.96 | 0.56 | -0.0 | 207224.31 | 20.65 | n/a |
| KITEUSDT | IDLE | 1.2 | 5.25 | 1.68 | 0.14 | 167370.01 | 7.76 | no_map |
| BIOUSDT | IDLE | 1.57 | 3.14 | 0.03 | -0.01 | 102294.99 | 9.31 | n/a |
| CHIPUSDT | IDLE | 1.13 | 2.88 | 0.16 | -0.0 | 115176.69 | 16.22 | no_map |
| TELUSDT | IDLE | 1.52 | 4.93 | 3.81 | 0.07 | 126824.73 | 40.22 | no_map |
| RWAINCUSDT | IDLE | 0.88 | 3.31 | 0.14 | 0.05 | 8378.63 | 89.35 | no_map |
| MNSRYUSDT | IDLE | 1.06 | 2.07 | 0.29 | 0.01 | 39469.87 | 3.79 | no_map |
| RWAUSDT | IDLE | 0.87 | 1.72 | 0.07 | 0.04 | 58002.68 | 7.04 | no_map |
| FLUIDUSDT | IDLE | 1.02 | 2.05 | 0.0 | 0.03 | 909.03 | 21.66 | tvl≈2,592,598,586 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
