# Hulk DIGEST — 2026-10-02T12:42:49Z

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
| QNTUSDT | IDLE | 1.9 | 11.66 | 1.18 | -0.11 | 5892372.14 | 9.31 | n/a |
| XRPUSDT | IDLE | 1.16 | 2.21 | 0.79 | 0.03 | 51458327.35 | 0.65 | n/a |
| ETHUSDT | IDLE | 1.01 | 1.88 | 0.9 | 0.02 | 439260564.26 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.86 | 1.63 | 0.61 | 0.03 | 795816386.64 | 0.0 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 10.92 | 7.51 | -0.04 | 5502.84 | 4.2 | no_map |
| CCUSDT | IDLE | 2.76 | 5.43 | 0.65 | 0.02 | 472431.08 | 10.44 | no_map |
| REDUSDT | IDLE | 4.24 | 8.2 | 3.33 | -0.02 | 76883.71 | 0.56 | tvl≈4,322,484 |
| PYTHUSDT | IDLE | 2.19 | 4.32 | 0.35 | 0.03 | 442726.89 | 58.31 | tvl≈172,998,930 |
| HBARUSDT | IDLE | 1.76 | 3.49 | 0.26 | 0.02 | 662540.57 | 8.44 | empty_tvl |
| EDELUSDT | IDLE | 1.66 | 7.11 | 4.51 | 0.03 | 292420.9 | 27.07 | no_map |
| WUSDT | IDLE | 1.13 | 2.1 | 1.01 | 0.02 | 401495.74 | 16.82 | tvl≈1,927,609,579 |
| KITEUSDT | IDLE | 2.9 | 5.47 | 2.19 | -0.01 | 94371.16 | 103.01 | no_map |
| ZBCNUSDT | IDLE | 1.58 | 3.41 | 3.03 | -0.04 | 286252.23 | 92.25 | n/a |
| CHIPUSDT | IDLE | 1.68 | 3.98 | 1.04 | 0.06 | 90447.09 | 22.36 | no_map |
| TELUSDT | IDLE | 2.04 | 3.68 | 2.68 | -0.02 | 142639.38 | 32.73 | no_map |
| BIOUSDT | IDLE | 1.13 | 2.2 | 0.44 | 0.03 | 90371.7 | 54.01 | n/a |
| RIZEUSDT | IDLE | 1.05 | 4.48 | 3.64 | -0.0 | 40560.02 | 61.66 | no_map |
| FLUIDUSDT | IDLE | 1.64 | 5.68 | 1.16 | 0.11 | 7353.46 | 21.57 | tvl≈2,496,656,571 |
| MNSRYUSDT | IDLE | 0.34 | 0.66 | 0.17 | 0.02 | 37550.71 | 8.98 | no_map |
| RWAUSDT | IDLE | 0.28 | 0.51 | 0.36 | 0.01 | 54113.59 | 36.04 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
