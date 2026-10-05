# Hulk DIGEST — 2026-10-05T03:00:50Z

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
| QNTUSDT | IDLE | 0.95 | 2.77 | 1.96 | -0.08 | 3083185.59 | 0.4 | skipped_fast |
| XRPUSDT | IDLE | 0.79 | 1.47 | 0.8 | 0.02 | 23693134.62 | 1.32 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.33 | 0.28 | 0.01 | 164393703.76 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.29 | 0.51 | 0.02 | 416585808.99 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.36 | 2.65 | 0.48 | 0.01 | 999505.77 | 9.59 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 6.33 | 5.03 | 0.03 | 244383.36 | 22.03 | skipped_fast |
| EDELUSDT | IDLE | 1.65 | 3.79 | 2.33 | 0.02 | 515938.89 | 20.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.27 | 2.43 | 0.69 | 0.01 | 438218.35 | 2.54 | skipped_fast |
| REDUSDT | IDLE | 2.37 | 4.58 | 1.11 | -0.0 | 83413.3 | 7.26 | skipped_fast |
| RIZEUSDT | IDLE | 1.9 | 18.57 | 3.57 | 0.3 | 42704.9 | 76.18 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.61 | 1.4 | 0.01 | 306907.08 | 6.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 4.89 | 2.89 | 0.11 | 79453.56 | 16.25 | skipped_fast |
| HBARUSDT | IDLE | 0.93 | 1.79 | 0.47 | 0.03 | 507731.48 | 3.83 | skipped_fast |
| TELUSDT | IDLE | 2.51 | 4.98 | 0.3 | 0.02 | 141615.43 | 30.03 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.31 | 0.19 | 0.0 | 70795.7 | 9.69 | skipped_fast |
| KITEUSDT | IDLE | 0.92 | 1.78 | 0.43 | -0.03 | 76021.36 | 10.2 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 2.19 | 0.87 | -0.05 | 5223.65 | 16.63 | skipped_fast |
| FLUIDUSDT | IDLE | 1.07 | 2.15 | 0.0 | 0.03 | 3154.84 | 22.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.84 | 1.57 | 0.69 | 0.01 | 45907.67 | 25.78 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.24 | 0.29 | 0.01 | 51687.59 | 14.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
