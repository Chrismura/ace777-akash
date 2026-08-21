# Hulk DIGEST — 2026-08-21T22:12:30Z

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
| PYTHUSDT | IDLE | 1.34 | 5.11 | 0.04 | 0.11 | 5710477.97 | 4.08 | skipped_fast |
| XRPUSDT | IDLE | 1.53 | 5.44 | 0.71 | 0.13 | 131524712.26 | 3.51 | skipped_fast |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.59 | 0.08 | 846763.22 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 6.0 | 0.0 | 0.13 | 643859.37 | 10.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 4.54 | 0.93 | 0.06 | 534426.92 | 3.04 | skipped_fast |
| WUSDT | IDLE | 2.4 | 5.04 | 0.0 | 0.08 | 368172.24 | 23.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 6.5 | 0.25 | 0.12 | 497637.2 | 21.19 | skipped_fast |
| BIOUSDT | IDLE | 2.25 | 5.04 | 0.49 | 0.02 | 187797.59 | 6.17 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.5 | 0.18 | 155184.28 | 18.69 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.62 | 0.06 | 186816.41 | 5.17 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.17 | 4.07 | 1.8 | 0.02 | 10212.63 | 42.76 | skipped_fast |
| EDELUSDT | IDLE | 1.88 | 4.12 | 0.22 | -0.04 | 82362.97 | 66.3 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 3.58 | 0.54 | 0.12 | 61371.92 | 11.91 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.71 | 0.07 | 56410.68 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.5 | 3.0 | 0.06 | 0.05 | 65307.65 | 12.26 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.16 | 0.04 | 54322.15 | 16.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 16.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
