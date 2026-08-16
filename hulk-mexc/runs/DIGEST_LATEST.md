# Hulk DIGEST — 2026-08-16T16:05:35Z

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
| XRPUSDT | IDLE | 0.17 | 0.32 | 0.07 | -0.0 | 4885403.9 | 1.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.54 | 15.73 | 8.04 | 0.16 | 264657.53 | 20.58 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.56 | 1.52 | -0.01 | 333265.85 | 7.3 | skipped_fast |
| RIZEUSDT | IDLE | 2.29 | 4.27 | 3.78 | -0.06 | 49300.0 | 32.36 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.77 | 0.99 | 0.02 | 157607.88 | 8.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 2.13 | 0.71 | 0.0 | 199166.14 | 12.07 | skipped_fast |
| QAITUSDT | IDLE | 2.09 | 6.52 | 1.74 | -0.02 | 2652.64 | 61.48 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 3.51 | 0.13 | -0.02 | 60067.7 | 39.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.55 | 4.0 | 3.85 | 0.05 | 9331.88 | 98.12 | skipped_fast |
| PYTHUSDT | IDLE | 0.46 | 0.92 | 0.05 | -0.01 | 119070.7 | 2.53 | skipped_fast |
| BIOUSDT | IDLE | 0.48 | 0.93 | 0.16 | -0.01 | 65663.27 | 8.05 | skipped_fast |
| KITEUSDT | IDLE | 0.47 | 0.9 | 0.25 | -0.03 | 57429.17 | 15.85 | skipped_fast |
| REDUSDT | IDLE | 0.15 | 1.26 | 0.79 | -0.03 | 89253.02 | 15.99 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.31 | 0.48 | -0.02 | 99832.31 | 48.23 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.79 | 0.09 | -0.01 | 51422.39 | 8.73 | skipped_fast |
| HBARUSDT | IDLE | 0.2 | 0.38 | 0.09 | -0.01 | 78950.66 | 1.53 | skipped_fast |
| QNTUSDT | IDLE | 0.32 | 0.59 | 0.36 | -0.01 | 32830.66 | 5.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 0.92 | 0.91 | 0.01 | 118.38 | 21.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
