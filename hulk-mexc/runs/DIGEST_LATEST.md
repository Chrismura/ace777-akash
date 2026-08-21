# Hulk DIGEST — 2026-08-21T22:25:45Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.2 | 0.11 | 5769880.89 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.57 | 5.68 | 0.84 | 0.14 | 133825597.26 | 1.4 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 6.48 | 0.49 | 0.13 | 650043.45 | 9.8 | skipped_fast |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.63 | 0.08 | 855986.9 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.47 | 5.3 | 0.34 | 0.08 | 370833.28 | 12.35 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.24 | 0.06 | 534127.6 | 6.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 6.5 | 0.42 | 0.11 | 502591.8 | 23.19 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.11 | 0.03 | 187898.98 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.98 | 0.19 | 156178.13 | 11.31 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 4.47 | 0.11 | -0.03 | 82580.28 | 10.97 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.05 | 186948.33 | 41.49 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.28 | 0.1 | 61308.28 | 13.86 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 86.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.77 | 0.06 | 56370.07 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 3.68 | 0.0 | 0.05 | 65345.38 | 3.04 | skipped_fast |
| RWAUSDT | IDLE | 0.9 | 1.75 | 0.33 | 0.04 | 54116.91 | 8.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 17.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
