# Hulk DIGEST — 2026-08-19T11:57:33Z

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
| XRPUSDT | IDLE | 0.53 | 1.01 | 0.38 | 0.01 | 10284327.56 | 0.99 | skipped_fast |
| CHIPUSDT | IDLE | 2.05 | 5.74 | 0.22 | -0.04 | 165751.31 | 3.73 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.5 | 1.74 | 0.01 | 177589.47 | 2.61 | skipped_fast |
| KITEUSDT | IDLE | 1.66 | 3.21 | 0.67 | 0.0 | 56465.32 | 11.95 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.67 | 0.48 | -0.01 | 222111.94 | 9.92 | skipped_fast |
| ZBCNUSDT | IDLE | 0.83 | 1.64 | 0.19 | 0.01 | 161591.79 | 12.57 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 2.98 | 1.91 | -0.12 | 136704.12 | 23.89 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.31 | 1.86 | -0.03 | 59206.18 | 26.99 | skipped_fast |
| WUSDT | IDLE | 0.96 | 1.87 | 0.28 | -0.0 | 100698.92 | 11.07 | skipped_fast |
| BIOUSDT | IDLE | 1.1 | 2.05 | 1.02 | 0.03 | 64236.4 | 11.94 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 3.86 | 1.26 | -0.07 | 28405.22 | 51.27 | skipped_fast |
| QAITUSDT | IDLE | 1.18 | 6.87 | 2.32 | -0.14 | 13005.56 | 65.85 | skipped_fast |
| RWAINCUSDT | IDLE | 0.82 | 1.43 | 1.41 | 0.0 | 9520.83 | 53.56 | skipped_fast |
| HBARUSDT | IDLE | 0.39 | 0.74 | 0.25 | 0.03 | 150651.4 | 1.48 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 1.74 | 1.37 | 0.01 | 86773.68 | 41.49 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 1.42 | 0.86 | 0.01 | 37666.91 | 7.08 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.26 | -0.01 | 52278.79 | 8.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.86 | 1.72 | 0.0 | -0.01 | 1261.45 | 21.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
