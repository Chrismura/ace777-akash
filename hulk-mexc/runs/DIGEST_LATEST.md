# Hulk DIGEST — 2026-09-01T12:24:38Z

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
| XRPUSDT | IDLE | 0.98 | 1.88 | 0.53 | 0.0 | 29869676.46 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.51 | 0.86 | -0.0 | 290994964.08 | 0.53 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.32 | 1.01 | -0.0 | 558589352.79 | 0.13 | skipped_fast |
| PYTHUSDT | IDLE | 2.31 | 5.52 | 1.31 | 0.07 | 583236.88 | 3.97 | skipped_fast |
| CCUSDT | IDLE | 2.59 | 4.56 | 4.12 | -0.01 | 394670.17 | 7.67 | skipped_fast |
| CHIPUSDT | IDLE | 2.58 | 4.67 | 3.25 | -0.01 | 342113.79 | 5.1 | skipped_fast |
| REDUSDT | IDLE | 3.23 | 6.02 | 2.87 | 0.01 | 62289.67 | 0.92 | skipped_fast |
| ZBCNUSDT | IDLE | 2.13 | 3.87 | 2.6 | 0.03 | 188238.62 | 12.48 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.7 | 1.69 | 0.02 | 234538.23 | 11.6 | skipped_fast |
| KITEUSDT | IDLE | 2.06 | 3.97 | 0.97 | -0.0 | 61730.41 | 12.47 | skipped_fast |
| RWAUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 6.85 | 5.25 | 0.03 | 63617.54 | 7.69 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 5.0 | 3.59 | -0.04 | 178021.84 | 17.3 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.59 | 1.51 | -0.01 | 62404.19 | 7.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.66 | 5.14 | 4.07 | -0.1 | 37787.56 | 73.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.4 | 2.62 | 1.22 | -0.02 | 4681.96 | 5.87 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 2.22 | 0.21 | 0.01 | 251397.0 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.0 | 1.15 | 0.0 | 85690.55 | 29.1 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 2.19 | 0.16 | 0.01 | 39229.66 | 4.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.57 | 0.43 | 0.0 | 31301.87 | 10.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1143.37 | 22.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
