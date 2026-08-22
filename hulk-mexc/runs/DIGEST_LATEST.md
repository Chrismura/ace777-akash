# Hulk DIGEST — 2026-08-22T01:04:21Z

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
| PYTHUSDT | IDLE | 2.32 | 7.67 | 0.0 | 0.13 | 6564698.54 | 3.98 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.21 | 8.4 | 1.28 | 0.15 | 148549147.98 | 3.42 | skipped_fast |
| HBARUSDT | IDLE | 3.04 | 6.36 | 1.11 | 0.08 | 953149.95 | 2.51 | skipped_fast |
| ZBCNUSDT | IDLE | 2.62 | 10.08 | 3.26 | 0.11 | 543277.95 | 27.67 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 6.71 | 0.0 | 0.16 | 650772.89 | 8.77 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.52 | 0.1 | 391996.56 | 8.13 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.73 | 0.02 | 539400.21 | 6.12 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 5.37 | 0.0 | 0.05 | 186631.01 | 3.05 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79745.07 | 22.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.95 | 0.12 | 60326.79 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 8.27 | 2.61 | 0.21 | 159855.36 | 17.17 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.9 | 0.07 | 170460.04 | 4.52 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.82 | 0.06 | 183825.01 | 46.4 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 4.01 | 0.03 | 0.12 | 60730.78 | 10.85 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 0.7 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 55053.97 | 16.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
