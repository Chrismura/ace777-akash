# Hulk DIGEST — 2026-08-20T13:12:59Z

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
| XRPUSDT | IDLE | 1.75 | 7.76 | 0.47 | 0.18 | 63366128.12 | 1.68 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.82 | 12.13 | 1.8 | 0.13 | 286242.39 | 3.28 | skipped_fast |
| PYTHUSDT | IDLE | 1.33 | 5.32 | 2.49 | 0.14 | 727470.14 | 4.56 | skipped_fast |
| BIOUSDT | IDLE | 1.8 | 11.75 | 9.33 | 0.18 | 278697.6 | 6.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.68 | 7.43 | 5.96 | 0.13 | 255618.98 | 17.19 | skipped_fast |
| CCUSDT | IDLE | 0.73 | 2.89 | 0.84 | 0.15 | 479034.8 | 5.76 | skipped_fast |
| WUSDT | IDLE | 1.32 | 2.65 | 1.02 | 0.07 | 326182.55 | 6.87 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.63 | 7.03 | 0.23 | 199043.06 | 12.04 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 3.2 | 1.09 | 0.07 | 441107.0 | 1.37 | skipped_fast |
| QAITUSDT | IDLE | 2.12 | 6.03 | 4.35 | -0.01 | 8372.58 | 61.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.2 | 8.15 | 3.67 | 0.1 | 65493.62 | 28.21 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.94 | 0.57 | 0.05 | 59791.96 | 14.49 | skipped_fast |
| TELUSDT | IDLE | 1.17 | 5.94 | 1.23 | 0.18 | 207946.19 | 29.59 | skipped_fast |
| QNTUSDT | IDLE | 1.8 | 4.44 | 0.35 | 0.09 | 59213.55 | 8.08 | skipped_fast |
| EDELUSDT | IDLE | 0.39 | 3.05 | 1.1 | 0.2 | 103275.59 | 33.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 1.82 | 1.4 | 0.04 | 13621.05 | 152.16 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.3 | 0.51 | 0.01 | 52356.21 | 8.6 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 3.3 | 0.16 | 0.11 | 3400.7 | 48.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
