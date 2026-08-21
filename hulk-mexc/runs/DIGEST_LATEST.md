# Hulk DIGEST — 2026-08-21T23:40:01Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.45 | 0.1 | 6138332.25 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.95 | 8.23 | 1.02 | 0.15 | 140985353.0 | 4.11 | skipped_fast |
| HBARUSDT | IDLE | 2.61 | 6.36 | 0.92 | 0.09 | 909123.67 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.86 | 0.12 | 513874.95 | 41.69 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 0.99 | 0.13 | 644449.06 | 8.0 | skipped_fast |
| WUSDT | IDLE | 2.77 | 6.91 | 1.74 | 0.08 | 379870.86 | 10.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.28 | 0.03 | 547828.46 | 6.16 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.14 | 0.02 | 186423.11 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82442.06 | 21.81 | skipped_fast |
| RIZEUSDT | IDLE | 2.2 | 9.82 | 4.6 | 0.12 | 59379.92 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.46 | 0.07 | 189893.6 | 30.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10344.85 | 21.39 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.68 | 0.19 | 157720.47 | 11.31 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.07 | 0.08 | 143895.66 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.9 | 0.09 | 61421.56 | 9.25 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.08 | 0.04 | 54592.83 | 8.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 39.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
