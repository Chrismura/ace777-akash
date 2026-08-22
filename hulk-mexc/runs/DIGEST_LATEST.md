# Hulk DIGEST — 2026-08-22T12:41:59Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.01 | 0.1 | 216307711.37 | 3.97 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 7.83 | 1.88 | 0.05 | 51601289.6 | 27.69 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 4.63 | 2.15 | 0.02 | 1251418.99 | 3.85 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 8.38 | 3.17 | 0.14 | 777428.49 | 8.4 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.61 | 0.0 | 576670.08 | 11.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 5.77 | 3.76 | -0.01 | 335510.96 | 22.55 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.62 | -0.1 | 603604.39 | 3.36 | skipped_fast |
| KITEUSDT | IDLE | 2.69 | 6.37 | 1.0 | 0.03 | 84907.59 | 19.52 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.02 | 78229.75 | 22.57 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.67 | -0.04 | 238870.05 | 3.23 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2406.15 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.66 | 0.01 | 152951.08 | 9.82 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.83 | -0.02 | 163530.27 | 58.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.58 | -0.0 | 187674.52 | 4.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.19 | -0.0 | 46775.9 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.12 | 0.02 | 57817.47 | 32.55 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.04 | 5094.24 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
