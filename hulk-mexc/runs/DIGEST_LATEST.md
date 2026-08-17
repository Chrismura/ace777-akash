# Hulk DIGEST — 2026-08-17T20:14:18Z

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
| XRPUSDT | IDLE | 0.5 | 0.88 | 0.75 | -0.0 | 12874778.01 | 2.0 | skipped_fast |
| EDELUSDT | IDLE | 3.77 | 6.84 | 4.68 | 0.02 | 66132.4 | 12.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 8.15 | 6.19 | -0.02 | 349849.55 | 7.02 | skipped_fast |
| REDUSDT | IDLE | 2.78 | 5.49 | 0.46 | 0.0 | 58683.16 | 16.08 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 3.06 | 2.83 | -0.05 | 241480.15 | 5.53 | skipped_fast |
| RIZEUSDT | IDLE | 1.38 | 11.55 | 7.74 | 0.14 | 86421.85 | 47.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.19 | 2.12 | 1.73 | 0.0 | 200159.44 | 22.83 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.15 | 1.97 | -0.02 | 1071.95 | 62.41 | skipped_fast |
| PYTHUSDT | IDLE | 1.05 | 1.92 | 1.2 | -0.01 | 159328.16 | 5.16 | skipped_fast |
| WUSDT | IDLE | 0.99 | 1.74 | 1.59 | -0.03 | 149538.97 | 15.71 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.49 | 2.03 | 0.01 | 81696.23 | 97.52 | skipped_fast |
| FLUIDUSDT | IDLE | 2.04 | 3.61 | 3.17 | -0.03 | 761.15 | 12.17 | skipped_fast |
| KITEUSDT | IDLE | 0.54 | 1.02 | 0.38 | -0.01 | 60314.58 | 17.25 | skipped_fast |
| TELUSDT | IDLE | 1.5 | 2.66 | 2.31 | -0.04 | 121075.91 | 35.8 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 0.96 | 0.95 | 0.01 | 145150.96 | 1.52 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.27 | 1.16 | -0.0 | 36684.88 | 7.02 | skipped_fast |
| RWAINCUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1218.85 | 63.97 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.69 | 0.43 | 0.01 | 48972.63 | 17.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
