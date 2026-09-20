# Hulk DIGEST — 2026-09-20T05:02:41Z

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
| XRPUSDT | IDLE | 1.73 | 3.13 | 2.16 | -0.02 | 57695594.5 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 1.49 | 2.67 | 2.07 | -0.02 | 249305506.65 | 0.16 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.49 | 1.11 | -0.01 | 471259312.47 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 6.71 | 5.63 | -0.03 | 725861.26 | 3.41 | skipped_fast |
| WUSDT | IDLE | 2.7 | 4.91 | 3.33 | 0.02 | 507928.35 | 4.54 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 5.43 | 3.83 | 0.02 | 689463.58 | 2.48 | skipped_fast |
| CCUSDT | IDLE | 2.52 | 5.16 | 3.79 | -0.06 | 327040.85 | 7.59 | skipped_fast |
| CHIPUSDT | IDLE | 2.47 | 6.39 | 5.15 | -0.08 | 110593.31 | 16.74 | skipped_fast |
| BIOUSDT | IDLE | 2.63 | 4.75 | 3.44 | 0.01 | 88490.47 | 11.02 | skipped_fast |
| ZBCNUSDT | IDLE | 1.68 | 6.3 | 4.1 | 0.06 | 217370.27 | 24.48 | skipped_fast |
| REDUSDT | IDLE | 1.94 | 3.81 | 0.53 | 0.04 | 100119.12 | 14.58 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 8.99 | 3.51 | -0.02 | 39327.69 | 103.41 | skipped_fast |
| KITEUSDT | IDLE | 1.54 | 2.81 | 1.79 | 0.0 | 76303.52 | 11.49 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 5.56 | 4.27 | -0.13 | 102205.03 | 62.24 | skipped_fast |
| QNTUSDT | IDLE | 1.75 | 3.12 | 2.51 | 0.01 | 55455.47 | 6.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.94 | 3.45 | 2.85 | -0.02 | 6692.04 | 21.61 | skipped_fast |
| RWAINCUSDT | IDLE | 0.3 | 0.66 | 0.59 | -0.03 | 7299.21 | 5.96 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 2.06 | 1.21 | -0.07 | 105488.57 | 47.64 | skipped_fast |
| RWAUSDT | IDLE | 0.95 | 1.72 | 1.25 | -0.0 | 52688.95 | 22.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.75 | 0.03 | -0.01 | 34249.3 | 72.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
