# Hulk DIGEST — 2026-08-22T00:02:57Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.29 | 0.1 | 6243970.72 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 8.23 | 1.05 | 0.15 | 142326319.66 | 2.06 | skipped_fast |
| HBARUSDT | IDLE | 2.75 | 6.36 | 0.83 | 0.09 | 906637.55 | 6.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 11.25 | 2.68 | 0.12 | 515144.0 | 21.23 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 7.42 | 0.57 | 0.14 | 645098.36 | 7.97 | skipped_fast |
| WUSDT | IDLE | 2.76 | 6.91 | 1.38 | 0.08 | 379008.42 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.88 | 0.04 | 536546.95 | 9.21 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.89 | 0.03 | 187125.8 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.57 | 5.5 | 1.19 | -0.0 | 80046.86 | 10.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.27 | 9.82 | 4.21 | 0.13 | 58947.47 | 45.81 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.46 | 0.06 | 189816.27 | 25.66 | skipped_fast |
| QNTUSDT | IDLE | 2.48 | 5.42 | 0.31 | 0.07 | 166713.81 | 8.98 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 4.91 | 2.4 | 0.19 | 157868.58 | 12.07 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.69 | 0.09 | 61472.29 | 9.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54535.18 | 16.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 40.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
