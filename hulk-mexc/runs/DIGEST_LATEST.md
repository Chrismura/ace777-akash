# Hulk DIGEST — 2026-08-21T23:06:09Z

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
| PYTHUSDT | IDLE | 1.67 | 6.26 | 0.02 | 0.12 | 5963687.88 | 2.02 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.72 | 6.54 | 0.2 | 0.15 | 138028069.96 | 4.14 | n/a |
| CCUSDT | IDLE | 1.89 | 7.42 | 0.65 | 0.14 | 665216.5 | 5.32 | no_map |
| HBARUSDT | IDLE | 2.36 | 5.03 | 0.15 | 0.09 | 888647.07 | 1.26 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 10.07 | 0.65 | 0.14 | 510162.97 | 24.39 | n/a |
| WUSDT | IDLE | 2.74 | 6.91 | 1.29 | 0.08 | 376375.18 | 4.1 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.09 | 0.05 | 544865.61 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.11 | 0.02 | 187364.48 | 3.11 | n/a |
| EDELUSDT | IDLE | 2.52 | 5.5 | 0.43 | -0.02 | 82517.99 | 32.77 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10205.68 | 16.16 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.01 | 0.18 | 157275.11 | 18.63 | tvl≈2,226,572 |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.41 | 0.07 | 185118.52 | 46.36 | no_map |
| QNTUSDT | IDLE | 2.49 | 5.13 | 0.02 | 0.07 | 96262.79 | 1.5 | n/a |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.23 | 0.09 | 61443.04 | 12.98 | no_map |
| RIZEUSDT | IDLE | 1.05 | 4.7 | 2.05 | 0.06 | 56402.36 | 29.56 | no_map |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.33 | 0.04 | 54371.6 | 24.58 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.83 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
