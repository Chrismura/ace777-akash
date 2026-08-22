# Hulk DIGEST — 2026-08-22T00:20:37Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.67 | 0.1 | 6331870.97 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.05 | 8.23 | 2.14 | 0.13 | 143652257.97 | 2.08 | skipped_fast |
| HBARUSDT | IDLE | 2.83 | 6.36 | 2.14 | 0.07 | 931652.25 | 1.27 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.37 | 0.1 | 519225.49 | 24.83 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 7.42 | 2.23 | 0.12 | 647963.81 | 10.8 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 0.95 | 0.08 | 384487.91 | 10.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.05 | 545193.77 | 6.13 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.62 | 0.02 | 186110.86 | 6.21 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.01 | 79838.09 | 33.24 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 9.82 | 3.09 | 0.14 | 59820.83 | 45.2 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.06 | 188936.17 | 41.24 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.63 | 0.06 | 171074.39 | 4.55 | skipped_fast |
| REDUSDT | IDLE | 0.56 | 4.91 | 1.65 | 0.2 | 157704.36 | 10.4 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 3.12 | 0.38 | 0.09 | 61299.06 | 11.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.03 | 9753.94 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54717.62 | 24.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
