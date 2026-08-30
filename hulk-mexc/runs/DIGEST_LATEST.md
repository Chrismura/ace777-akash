# Hulk DIGEST — 2026-08-30T20:14:35Z

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
| XRPUSDT | IDLE | 1.46 | 2.71 | 1.44 | 0.01 | 22289689.86 | 2.83 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.51 | 1.1 | 0.02 | 220329518.9 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 0.97 | 0.63 | 0.01 | 281803159.07 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.76 | 5.97 | 4.73 | -0.04 | 489946.34 | 2.56 | skipped_fast |
| ZBCNUSDT | IDLE | 2.82 | 5.98 | 3.71 | -0.04 | 196209.53 | 12.48 | skipped_fast |
| PYTHUSDT | IDLE | 1.94 | 3.62 | 1.79 | 0.03 | 397104.01 | 4.05 | skipped_fast |
| KITEUSDT | IDLE | 2.03 | 3.6 | 3.01 | -0.02 | 60648.59 | 10.36 | skipped_fast |
| WUSDT | IDLE | 1.15 | 2.08 | 1.48 | 0.03 | 226654.76 | 13.74 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.74 | 2.35 | 0.01 | 63638.21 | 4.58 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 4.54 | 1.39 | 0.08 | 74044.34 | 24.93 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 5.3 | 2.4 | -0.01 | 42698.78 | 59.09 | skipped_fast |
| CCUSDT | IDLE | 0.56 | 1.05 | 0.5 | -0.0 | 242107.46 | 5.07 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.94 | 0.83 | -0.0 | 80471.54 | 3.63 | skipped_fast |
| TELUSDT | IDLE | 1.9 | 3.61 | 1.31 | -0.01 | 85678.94 | 28.94 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.6 | 0.16 | 0.01 | 167906.17 | 1.32 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 2.24 | 0.0 | 0.02 | 1480.3 | 120.81 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 1.57 | 0.88 | 0.01 | 38406.36 | 1.62 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.3 | 0.08 | 0.02 | 53071.71 | 16.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.89 | 1.73 | 0.37 | 0.03 | 3286.72 | 21.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.47 | 0.19 | 0.01 | 31960.54 | 4.0 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
