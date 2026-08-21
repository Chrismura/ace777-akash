# Hulk DIGEST — 2026-08-21T21:47:33Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.62 | 0.09 | 5664563.09 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.82 | 0.11 | 129755966.14 | 1.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.67 | 0.05 | 527443.11 | 9.29 | skipped_fast |
| HBARUSDT | IDLE | 1.93 | 4.08 | 0.03 | 0.08 | 821301.4 | 1.27 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 3.75 | 0.08 | 0.11 | 650707.56 | 9.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 8.19 | 3.76 | 0.1 | 492370.06 | 54.9 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.83 | 0.05 | 0.07 | 368980.77 | 7.29 | skipped_fast |
| BIOUSDT | IDLE | 2.39 | 5.2 | 1.44 | 0.03 | 187726.6 | 6.23 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.29 | 0.17 | 154190.1 | 18.02 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 0.99 | 0.04 | 55811.2 | 22.81 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 4.12 | 1.65 | -0.04 | 83584.03 | 33.28 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.3 | 0.11 | 61175.78 | 13.81 | skipped_fast |
| TELUSDT | IDLE | 1.94 | 4.81 | 1.56 | 0.02 | 183704.43 | 37.16 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.65 | 0.57 | 0.04 | 62632.17 | 7.73 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.41 | 0.03 | 53879.82 | 24.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
