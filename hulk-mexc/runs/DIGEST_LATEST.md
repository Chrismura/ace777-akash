# Hulk DIGEST — 2026-08-21T22:03:19Z

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
| PYTHUSDT | IDLE | 1.25 | 4.74 | 0.29 | 0.1 | 5695139.92 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.63 | 0.11 | 129702206.36 | 2.14 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.72 | 0.08 | 840736.97 | 1.27 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 3.95 | 0.08 | 0.11 | 636389.88 | 6.38 | skipped_fast |
| CHIPUSDT | IDLE | 1.54 | 4.54 | 2.47 | 0.05 | 527387.16 | 3.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 6.19 | 0.04 | 0.12 | 494525.17 | 22.18 | skipped_fast |
| WUSDT | IDLE | 2.1 | 4.19 | 0.06 | 0.07 | 367573.23 | 11.4 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.01 | 1.2 | 0.03 | 185367.08 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.87 | 0.17 | 153838.3 | 10.61 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 4.12 | 1.1 | -0.05 | 82693.25 | 33.17 | skipped_fast |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.18 | 0.05 | 189087.07 | 31.19 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 4.07 | 0.9 | 0.02 | 10204.87 | 58.74 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.82 | 0.11 | 61275.08 | 9.19 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.76 | 0.06 | 56403.48 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 2.49 | 0.18 | 0.04 | 62413.28 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.33 | 0.33 | 0.04 | 54119.19 | 24.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 40.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
