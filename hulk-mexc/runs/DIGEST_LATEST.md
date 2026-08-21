# Hulk DIGEST — 2026-08-21T23:50:37Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.86 | 0.1 | 6192387.58 | 6.17 | skipped_fast |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.31 | 0.15 | 141868150.85 | 1.37 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 11.25 | 2.21 | 0.13 | 514236.97 | 17.31 | skipped_fast |
| HBARUSDT | IDLE | 2.62 | 6.36 | 1.11 | 0.09 | 907138.0 | 1.25 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.87 | 0.13 | 644803.17 | 8.01 | skipped_fast |
| WUSDT | IDLE | 2.78 | 6.91 | 1.88 | 0.08 | 378262.85 | 13.39 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 3.56 | 1.55 | 0.03 | 545666.69 | 24.71 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.54 | 0.02 | 186667.66 | 9.37 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.41 | 0.0 | 80198.1 | 22.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.85 | 0.12 | 58848.39 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.36 | 0.07 | 190410.05 | 25.66 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.85 | 0.18 | 157875.6 | 11.31 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.04 | 0.08 | 151335.53 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3921.68 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10306.4 | 69.69 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.45 | 0.09 | 61335.25 | 13.96 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54582.92 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 22.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
