# Hulk DIGEST — 2026-09-01T22:27:50Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.47 | 2.62 | 2.08 | -0.03 | 34773948.03 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 1.26 | 2.34 | 1.15 | -0.02 | 335523709.19 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.7 | 0.7 | -0.02 | 530220978.85 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.92 | 5.74 | 0.71 | 0.06 | 675730.49 | 1.93 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 11.2 | 3.26 | 0.15 | 680196.57 | 2.25 | skipped_fast |
| WUSDT | IDLE | 2.21 | 4.18 | 3.64 | 0.05 | 407325.28 | 14.61 | skipped_fast |
| ZBCNUSDT | IDLE | 2.8 | 4.94 | 4.43 | -0.01 | 203283.89 | 30.17 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 5.85 | 2.89 | 0.09 | 115740.58 | 13.04 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 2.16 | 1.55 | -0.07 | 332715.13 | 7.04 | skipped_fast |
| RIZEUSDT | IDLE | 2.03 | 4.22 | 2.74 | -0.06 | 40566.3 | 57.25 | skipped_fast |
| EDELUSDT | IDLE | 0.8 | 6.02 | 5.07 | -0.08 | 138247.61 | 9.2 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.78 | 0.97 | 0.04 | 68287.32 | 12.23 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.29 | 1.85 | -0.04 | 69998.82 | 3.93 | skipped_fast |
| TELUSDT | IDLE | 2.66 | 4.83 | 3.27 | -0.04 | 94591.37 | 36.17 | skipped_fast |
| RWAINCUSDT | IDLE | 1.52 | 2.8 | 1.56 | -0.02 | 6196.92 | 5.88 | skipped_fast |
| FLUIDUSDT | IDLE | 2.56 | 4.47 | 4.28 | -0.03 | 229.45 | 18.13 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.66 | 0.91 | 0.0 | 249227.31 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.52 | 2.91 | 0.88 | 0.05 | 46794.75 | 6.27 | skipped_fast |
| MNSRYUSDT | IDLE | 0.9 | 1.64 | 1.11 | -0.02 | 34539.92 | 6.87 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.93 | 0.69 | -0.03 | 59227.15 | 7.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
