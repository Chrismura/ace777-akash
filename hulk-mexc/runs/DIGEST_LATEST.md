# Hulk DIGEST — 2026-08-22T11:05:16Z

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
| PYTHUSDT | IDLE | 2.2 | 9.66 | 8.33 | -0.01 | 51655883.27 | 12.51 | skipped_fast |
| XRPUSDT | IDLE | 2.35 | 14.26 | 9.12 | 0.07 | 218335839.14 | 3.38 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.77 | 0.11 | 816703.01 | 5.2 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 5.26 | 3.83 | 0.0 | 1252005.17 | 6.5 | skipped_fast |
| WUSDT | IDLE | 1.57 | 6.27 | 4.08 | 0.01 | 595098.61 | 3.19 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 5.08 | 4.48 | -0.03 | 425040.45 | 31.48 | skipped_fast |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.41 | -0.11 | 646355.86 | 3.38 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 4.93 | 3.82 | -0.04 | 78917.29 | 34.03 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.64 | 3.99 | -0.06 | 240710.49 | 3.27 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 4.3 | 2.11 | 0.03 | 73284.28 | 5.48 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 6.75 | 5.41 | -0.04 | 169165.88 | 48.19 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.34 | 0.03 | 154370.22 | 21.58 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.01 | 2418.23 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | 0.0 | 11326.93 | 59.83 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 3.47 | 2.42 | -0.01 | 189169.33 | 7.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 1.24 | -0.0 | 49227.26 | 46.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 68.48 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57434.8 | 32.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
