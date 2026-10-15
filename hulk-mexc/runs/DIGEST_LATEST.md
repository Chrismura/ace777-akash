# Hulk DIGEST — 2026-10-15T05:25:20Z

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
| PYTHUSDT | IDLE | 3.06 | 9.59 | 2.53 | 0.07 | 2551987.47 | 9.25 | skipped_fast |
| WUSDT | IDLE | 2.42 | 8.91 | 4.44 | -0.08 | 2648546.82 | 18.65 | skipped_fast |
| ETHUSDT | IDLE | 2.25 | 4.62 | 2.66 | -0.06 | 318468571.59 | 0.08 | skipped_fast |
| XRPUSDT | IDLE | 2.13 | 3.93 | 2.19 | -0.05 | 57500067.94 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 1.07 | 2.01 | 0.93 | -0.03 | 526312926.1 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 8.39 | 5.96 | -0.09 | 1187411.91 | 2.06 | skipped_fast |
| CCUSDT | IDLE | 2.01 | 6.72 | 5.93 | -0.13 | 454680.71 | 9.2 | skipped_fast |
| HBARUSDT | IDLE | 2.77 | 5.9 | 3.99 | -0.06 | 620557.62 | 4.91 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 9.55 | 6.45 | -0.1 | 78607.33 | 12.09 | skipped_fast |
| CHIPUSDT | IDLE | 2.06 | 12.49 | 10.91 | -0.19 | 118245.7 | 10.95 | skipped_fast |
| EDELUSDT | IDLE | 2.36 | 5.09 | 3.85 | -0.06 | 198215.12 | 6.26 | skipped_fast |
| RIZEUSDT | IDLE | 2.33 | 16.47 | 4.11 | 0.02 | 62243.27 | 48.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.84 | 4.67 | 3.53 | -0.07 | 218735.51 | 4.26 | skipped_fast |
| REDUSDT | IDLE | 2.22 | 4.29 | 1.06 | 0.0 | 66546.86 | 15.8 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 5.84 | 4.76 | -0.1 | 87454.72 | 11.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.55 | 3.3 | 2.25 | 0.0 | 27201.42 | 10.22 | skipped_fast |
| FLUIDUSDT | IDLE | 2.22 | 6.39 | 6.01 | -0.03 | 22363.86 | 21.57 | skipped_fast |
| TELUSDT | IDLE | 2.12 | 3.83 | 2.67 | -0.05 | 98844.21 | 40.83 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.62 | 0.95 | -0.03 | 54339.57 | 16.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.9 | 1.64 | 1.08 | -0.02 | 31881.44 | 36.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
