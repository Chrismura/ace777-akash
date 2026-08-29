# Hulk DIGEST — 2026-08-29T07:09:55Z

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
| CHIPUSDT | IDLE | 2.61 | 12.93 | 3.2 | 0.07 | 1205307.45 | 11.64 | skipped_fast |
| XRPUSDT | IDLE | 0.64 | 1.17 | 0.73 | -0.03 | 43727006.29 | 2.17 | skipped_fast |
| QAITUSDT | IDLE | 2.36 | 20.42 | 15.35 | -0.03 | 84056.79 | 56.66 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 2.7 | 2.08 | -0.04 | 506615.13 | 2.13 | skipped_fast |
| WUSDT | IDLE | 1.19 | 2.18 | 1.29 | -0.03 | 210136.31 | 11.99 | skipped_fast |
| RIZEUSDT | IDLE | 2.15 | 5.15 | 0.98 | -0.05 | 29531.23 | 58.02 | skipped_fast |
| KITEUSDT | IDLE | 1.54 | 2.85 | 1.56 | -0.02 | 72113.05 | 10.23 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 3.2 | 0.36 | 0.0 | 61110.29 | 10.03 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 1.52 | 0.22 | -0.02 | 217753.16 | 3.59 | skipped_fast |
| HBARUSDT | IDLE | 0.71 | 1.32 | 0.73 | -0.04 | 466515.91 | 1.33 | skipped_fast |
| EDELUSDT | IDLE | 0.93 | 3.47 | 2.79 | -0.1 | 89863.35 | 19.14 | skipped_fast |
| ZBCNUSDT | IDLE | 0.61 | 1.56 | 1.08 | -0.06 | 177810.42 | 18.45 | skipped_fast |
| BIOUSDT | IDLE | 0.74 | 1.34 | 1.0 | -0.03 | 81890.82 | 3.62 | skipped_fast |
| TELUSDT | IDLE | 1.27 | 2.24 | 1.97 | -0.05 | 91588.97 | 40.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.38 | 0.66 | 0.65 | 0.02 | 3515.73 | 71.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.61 | 1.22 | -0.05 | 3721.3 | 21.64 | skipped_fast |
| QNTUSDT | IDLE | 0.5 | 0.95 | 0.29 | -0.01 | 40442.66 | 4.88 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.16 | 0.33 | 0.0 | 55461.63 | 24.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
