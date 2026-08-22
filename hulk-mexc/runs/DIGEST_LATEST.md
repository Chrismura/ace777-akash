# Hulk DIGEST — 2026-08-22T11:09:58Z

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
| PYTHUSDT | IDLE | 2.2 | 9.66 | 8.14 | -0.0 | 51658544.88 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.27 | 0.07 | 218240881.09 | 4.02 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.56 | 0.11 | 813326.94 | 6.05 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.65 | 0.0 | 1255014.4 | 6.48 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.84 | 0.01 | 595695.6 | 13.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.18 | 5.47 | 5.19 | -0.04 | 410902.39 | 25.5 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.34 | -0.11 | 645900.5 | 6.76 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.26 | -0.05 | 78823.38 | 56.92 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.93 | -0.05 | 240767.31 | 3.28 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 4.3 | 1.65 | 0.04 | 73635.45 | 11.83 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.16 | 2.48 | -0.0 | 2500.36 | 35.86 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.61 | -0.04 | 169258.12 | 53.5 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.71 | 0.03 | 154281.56 | 11.74 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | -0.01 | 11311.88 | 59.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 2.89 | 1.82 | -0.01 | 49238.9 | 22.54 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 3.47 | 2.11 | -0.01 | 189146.7 | 9.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 63.53 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57511.75 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
