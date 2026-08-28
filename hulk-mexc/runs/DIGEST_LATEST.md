# Hulk DIGEST — 2026-08-28T23:09:11Z

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
| XRPUSDT | IDLE | 0.98 | 1.88 | 0.52 | -0.05 | 52226988.39 | 1.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 7.37 | 4.61 | 0.06 | 1101626.37 | 4.87 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 33.82 | 24.02 | -0.16 | 83216.99 | 61.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.33 | 3.02 | 0.02 | -0.03 | 688502.54 | 2.11 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 13.86 | 10.52 | -0.14 | 91442.01 | 107.47 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 5.63 | 4.36 | -0.08 | 174052.88 | 10.21 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.3 | 0.0 | -0.01 | 336669.78 | 5.38 | skipped_fast |
| REDUSDT | IDLE | 2.06 | 5.16 | 0.99 | -0.01 | 63844.11 | 12.09 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 3.61 | 1.54 | -0.02 | 78468.75 | 8.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.89 | 4.97 | 3.87 | -0.01 | 35873.7 | 55.56 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.82 | 1.2 | -0.04 | 469257.71 | 1.32 | skipped_fast |
| RWAINCUSDT | IDLE | 2.36 | 4.28 | 2.93 | -0.02 | 3438.2 | 98.25 | skipped_fast |
| WUSDT | IDLE | 0.62 | 1.47 | 0.05 | -0.05 | 207663.12 | 12.03 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 2.01 | 0.43 | -0.06 | 88946.56 | 3.59 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.82 | 2.24 | -0.08 | 96978.9 | 28.68 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.36 | 0.11 | -0.04 | 43084.88 | 4.91 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.58 | 0.17 | 0.0 | 54449.43 | 33.2 | skipped_fast |
| FLUIDUSDT | IDLE | 0.2 | 0.41 | 0.0 | -0.05 | 4563.02 | 29.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
