# Hulk DIGEST — 2026-08-22T00:08:43Z

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
| PYTHUSDT | IDLE | 1.8 | 6.39 | 2.4 | 0.09 | 6277302.62 | 10.33 | skipped_fast |
| XRPUSDT | IDLE | 2.08 | 8.23 | 3.09 | 0.13 | 143132616.23 | 1.4 | skipped_fast |
| HBARUSDT | IDLE | 2.83 | 6.36 | 2.15 | 0.07 | 911842.54 | 6.33 | skipped_fast |
| ZBCNUSDT | IDLE | 2.92 | 11.25 | 3.62 | 0.11 | 515323.51 | 44.3 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 7.42 | 0.89 | 0.13 | 642237.33 | 8.88 | skipped_fast |
| WUSDT | IDLE | 2.79 | 6.91 | 1.84 | 0.07 | 380147.93 | 14.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.43 | 0.04 | 544652.73 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 5.04 | 2.21 | 0.01 | 187273.58 | 15.74 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | -0.0 | 79887.07 | 22.03 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 9.82 | 3.53 | 0.14 | 59054.08 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.86 | 6.89 | 1.02 | 0.06 | 190245.0 | 36.26 | skipped_fast |
| QNTUSDT | IDLE | 2.53 | 5.42 | 0.99 | 0.07 | 166754.4 | 9.08 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 4.91 | 3.18 | 0.19 | 157680.86 | 24.4 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.44 | 0.08 | 61433.43 | 12.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54624.04 | 24.62 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 22.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
