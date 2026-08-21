# Hulk DIGEST — 2026-08-21T22:16:26Z

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
| PYTHUSDT | IDLE | 1.35 | 5.17 | 0.02 | 0.11 | 5728669.79 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.54 | 5.44 | 1.04 | 0.13 | 131619716.42 | 2.11 | skipped_fast |
| CCUSDT | IDLE | 1.75 | 6.45 | 0.02 | 0.14 | 644557.3 | 10.68 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.67 | 0.08 | 848356.46 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.46 | 5.3 | 0.21 | 0.08 | 369158.46 | 10.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.11 | 0.06 | 534644.23 | 6.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 6.5 | 0.18 | 0.11 | 498921.3 | 15.26 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.55 | 0.02 | 187715.81 | 6.19 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.14 | 0.18 | 155845.14 | 12.12 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 4.24 | 0.33 | -0.03 | 82362.18 | 33.02 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.51 | 6.45 | 0.56 | 0.06 | 186821.68 | 36.15 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 75.27 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.74 | 0.11 | 61394.86 | 11.93 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.83 | 0.06 | 56366.46 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.61 | 3.22 | 0.0 | 0.05 | 65374.07 | 13.75 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.41 | 0.04 | 54122.69 | 32.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
