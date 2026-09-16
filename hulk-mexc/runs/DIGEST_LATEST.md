# Hulk DIGEST — 2026-09-16T15:02:38Z

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
| XRPUSDT | IDLE | 1.09 | 2.96 | 2.25 | -0.08 | 82097704.08 | 1.58 | skipped_fast |
| ETHUSDT | IDLE | 1.14 | 2.06 | 1.44 | -0.0 | 427722603.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.13 | 0.72 | -0.0 | 569357039.29 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.81 | 3.21 | 2.69 | -0.02 | 674338.3 | 1.92 | skipped_fast |
| CCUSDT | IDLE | 2.0 | 3.55 | 3.03 | -0.04 | 440489.45 | 8.97 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 5.94 | 5.4 | -0.05 | 65154.89 | 18.21 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.95 | 7.82 | 6.5 | -0.04 | 99809.59 | 13.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 22.31 | 17.1 | 0.39 | 57872.11 | 94.73 | skipped_fast |
| EDELUSDT | IDLE | 0.58 | 8.12 | 7.29 | 0.33 | 412837.4 | 45.56 | skipped_fast |
| HBARUSDT | IDLE | 1.65 | 3.34 | 2.56 | -0.06 | 354108.58 | 1.38 | skipped_fast |
| WUSDT | IDLE | 1.07 | 2.33 | 1.54 | -0.07 | 222346.68 | 15.86 | skipped_fast |
| BIOUSDT | IDLE | 1.58 | 2.84 | 2.2 | -0.02 | 80598.61 | 8.19 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 2.92 | 2.42 | -0.06 | 59639.55 | 10.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.0 | 2.59 | 1.59 | -0.01 | 194271.49 | 19.34 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 5.6 | 3.74 | -0.07 | 121600.91 | 21.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.27 | 2.31 | 1.51 | -0.03 | 13229.5 | 41.53 | skipped_fast |
| FLUIDUSDT | IDLE | 1.74 | 3.17 | 2.13 | -0.05 | 2521.8 | 21.64 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 2.02 | 0.98 | -0.04 | 43103.07 | 8.41 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.76 | 0.08 | -0.01 | 52920.61 | 7.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.08 | -0.01 | 33019.82 | 7.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
