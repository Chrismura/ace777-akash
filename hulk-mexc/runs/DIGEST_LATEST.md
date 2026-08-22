# Hulk DIGEST — 2026-08-22T02:01:54Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.06 | 0.14 | 6885826.94 | 1.95 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 10.03 | 1.87 | 0.14 | 154099198.04 | 3.38 | n/a |
| HBARUSDT | IDLE | 2.35 | 4.9 | 0.95 | 0.07 | 950726.79 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.83 | 0.08 | 548672.97 | 24.21 | n/a |
| CCUSDT | IDLE | 1.67 | 6.06 | 0.3 | 0.16 | 662638.75 | 11.35 | no_map |
| CHIPUSDT | IDLE | 1.58 | 3.65 | 0.0 | 0.02 | 510725.71 | 3.04 | no_map |
| WUSDT | IDLE | 1.7 | 4.31 | 0.1 | 0.09 | 399843.71 | 15.14 | tvl≈1,638,353,418 |
| BIOUSDT | IDLE | 2.33 | 4.66 | 0.0 | 0.06 | 184647.95 | 21.14 | n/a |
| EDELUSDT | IDLE | 2.4 | 5.02 | 1.95 | -0.02 | 79541.28 | 22.15 | no_map |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.89 | 0.11 | 61039.25 | 23.68 | no_map |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.13 | 0.16 | 156920.22 | 18.61 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.3 | 4.89 | 1.08 | 0.07 | 171342.98 | 9.06 | n/a |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.19 | 0.13 | 61280.91 | 8.96 | no_map |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | no_map |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.07 | 0.05 | 180977.39 | 36.2 | no_map |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9241.73 | 64.41 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 17.72 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54531.94 | 8.2 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
