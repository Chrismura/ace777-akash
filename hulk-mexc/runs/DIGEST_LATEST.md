# Hulk DIGEST — 2026-08-12T20:28:08Z

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
| XRPUSDT | IDLE | 0.34 | 0.64 | 0.32 | -0.01 | 15004393.57 | 0.99 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.34 | 27.36 | 16.69 | 0.12 | 46719.65 | 47.95 | skipped_fast |
| CHIPUSDT | IDLE | 2.85 | 6.56 | 3.63 | 0.06 | 105384.08 | 4.29 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 2.99 | 1.97 | -0.04 | 321702.12 | 2.48 | skipped_fast |
| CCUSDT | IDLE | 1.2 | 2.15 | 1.63 | -0.02 | 223903.65 | 5.06 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 8.52 | 2.51 | 0.08 | 71328.07 | 97.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 2.03 | 1.75 | -0.02 | 196046.77 | 19.01 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 2.9 | 1.97 | -0.01 | 60510.08 | 17.55 | skipped_fast |
| RWAINCUSDT | IDLE | 2.12 | 4.03 | 1.36 | -0.01 | 1707.38 | 52.88 | skipped_fast |
| WUSDT | IDLE | 0.8 | 1.49 | 0.72 | -0.02 | 176502.38 | 14.75 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 1.9 | 1.78 | -0.03 | 63495.52 | 4.12 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.26 | 0.02 | -0.04 | 60266.39 | 12.8 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 2.77 | 2.06 | 0.01 | 58165.63 | 8.56 | skipped_fast |
| QAITUSDT | IDLE | 0.71 | 2.54 | 2.48 | -0.04 | 4591.18 | 60.7 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 1.8 | 0.32 | 0.03 | 100490.45 | 38.05 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.25 | 0.66 | 0.02 | 51965.93 | 16.61 | skipped_fast |
| HBARUSDT | IDLE | 0.41 | 0.76 | 0.35 | -0.01 | 71679.22 | 1.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.21 | 0.37 | 0.29 | -0.02 | 542.31 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
