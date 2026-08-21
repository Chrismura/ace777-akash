# Hulk DIGEST — 2026-08-21T22:36:14Z

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
| PYTHUSDT | IDLE | 1.37 | 5.17 | 0.63 | 0.11 | 5825610.59 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.59 | 5.91 | 0.28 | 0.14 | 134714006.18 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 6.75 | 0.05 | 0.14 | 659657.03 | 12.42 | skipped_fast |
| HBARUSDT | IDLE | 2.23 | 4.71 | 1.02 | 0.08 | 869081.18 | 5.08 | skipped_fast |
| WUSDT | IDLE | 2.47 | 5.3 | 0.42 | 0.08 | 370972.57 | 14.43 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 6.77 | 0.53 | 0.11 | 503382.0 | 4.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.63 | 0.06 | 533807.32 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.31 | 5.04 | 1.41 | 0.03 | 188350.86 | 6.24 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.08 | 0.18 | 155985.93 | 11.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.07 | 2.43 | 0.02 | 10212.45 | 16.17 | skipped_fast |
| EDELUSDT | IDLE | 2.34 | 5.04 | 0.87 | -0.03 | 82594.42 | 65.93 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.06 | 187104.64 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3825.97 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.2 | 0.11 | 61546.24 | 12.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.79 | 0.06 | 56362.81 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 2.03 | 4.06 | 0.05 | 0.06 | 75019.22 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.0 | 0.04 | 54143.5 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
