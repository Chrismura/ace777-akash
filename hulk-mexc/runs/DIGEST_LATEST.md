# Hulk DIGEST — 2026-08-21T22:20:25Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.18 | 0.11 | 5746914.05 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.54 | 5.67 | 0.11 | 0.14 | 132373830.21 | 2.09 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 6.48 | 0.64 | 0.13 | 647010.36 | 10.72 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.71 | 0.41 | 0.09 | 854865.34 | 1.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.18 | 0.06 | 534137.77 | 3.05 | skipped_fast |
| WUSDT | IDLE | 2.44 | 5.3 | 0.03 | 0.08 | 369790.67 | 17.44 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 6.5 | 0.17 | 0.11 | 500459.66 | 36.44 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.55 | 0.03 | 187927.14 | 3.09 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.95 | 0.18 | 156272.91 | 12.92 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 4.24 | 0.33 | -0.03 | 82362.14 | 22.03 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.5 | 6.45 | 0.31 | 0.06 | 186846.7 | 46.4 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.74 | 0.11 | 61270.33 | 11.96 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 86.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.57 | 0.06 | 56380.86 | 19.07 | skipped_fast |
| QNTUSDT | IDLE | 1.79 | 3.58 | 0.0 | 0.05 | 65426.65 | 12.2 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.25 | 0.04 | 54126.15 | 8.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 0.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
