# Hulk DIGEST — 2026-08-22T00:05:06Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.39 | 0.1 | 6255482.48 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 8.23 | 1.91 | 0.15 | 142418163.38 | 6.22 | skipped_fast |
| HBARUSDT | IDLE | 2.78 | 6.36 | 1.28 | 0.09 | 910669.0 | 5.02 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.78 | 0.12 | 515122.92 | 33.86 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 7.42 | 0.56 | 0.13 | 645151.68 | 7.97 | skipped_fast |
| WUSDT | IDLE | 2.77 | 6.91 | 1.52 | 0.08 | 379266.22 | 12.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.09 | 0.04 | 542168.24 | 6.15 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.48 | 0.03 | 187327.43 | 12.5 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | -0.01 | 80046.8 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.29 | 9.82 | 5.02 | 0.12 | 59051.17 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.41 | 0.06 | 189887.2 | 10.27 | skipped_fast |
| QNTUSDT | IDLE | 2.49 | 5.42 | 0.46 | 0.07 | 166725.5 | 1.5 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 4.91 | 2.49 | 0.19 | 157749.9 | 20.26 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.09 | 61531.0 | 12.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.08 | 0.04 | 54540.62 | 8.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 22.0 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
