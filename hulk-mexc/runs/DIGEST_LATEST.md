# Hulk DIGEST — 2026-08-21T21:48:54Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.57 | 0.09 | 5666027.8 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.62 | 0.11 | 129964636.91 | 2.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.64 | 0.04 | 527406.51 | 3.09 | skipped_fast |
| HBARUSDT | IDLE | 1.95 | 4.08 | 0.29 | 0.08 | 821367.57 | 2.54 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 3.82 | 0.0 | 0.11 | 645870.65 | 6.38 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.81 | 0.11 | 493279.35 | 55.8 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.86 | 0.0 | 0.07 | 368804.73 | 10.4 | skipped_fast |
| BIOUSDT | IDLE | 2.39 | 5.2 | 1.47 | 0.03 | 187334.34 | 6.23 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.21 | 0.17 | 154162.71 | 11.48 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 0.87 | 0.04 | 55828.44 | 47.31 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 4.12 | 0.99 | -0.04 | 83609.06 | 44.44 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.29 | 0.11 | 61207.73 | 11.96 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 4.81 | 1.04 | 0.03 | 184155.83 | 52.94 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.65 | 0.49 | 0.04 | 62604.94 | 4.63 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.17 | 0.33 | 0.03 | 53906.91 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
