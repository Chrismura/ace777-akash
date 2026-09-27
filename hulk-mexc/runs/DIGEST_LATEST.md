# Hulk DIGEST — 2026-09-27T17:11:47Z

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
| WUSDT | IDLE | 1.67 | 11.02 | 0.03 | 0.19 | 4101229.71 | 7.64 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 6.98 | 2.41 | 0.13 | 2171473.32 | 15.09 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 20.99 | 1.79 | 0.52 | 6139623.22 | 8.6 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 2.43 | 1.69 | -0.01 | 44675668.68 | 1.32 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.28 | 1.05 | 0.0 | 192661741.1 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.95 | 0.87 | 0.0 | 453228291.84 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 42.2 | 24.78 | 0.07 | 25155.47 | 13.95 | skipped_fast |
| CCUSDT | IDLE | 2.7 | 5.02 | 2.52 | -0.02 | 538191.55 | 8.86 | skipped_fast |
| CHIPUSDT | IDLE | 3.29 | 5.98 | 4.5 | -0.06 | 100049.76 | 19.13 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.07 | 2.34 | -0.01 | 691615.48 | 1.07 | skipped_fast |
| EDELUSDT | IDLE | 2.32 | 8.31 | 6.33 | -0.11 | 137323.06 | 33.14 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 1.95 | 1.89 | -0.02 | 211300.79 | 7.65 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 3.05 | 1.28 | -0.04 | 93916.13 | 12.64 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 3.18 | 0.97 | 0.04 | 172786.93 | 9.98 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.76 | 0.49 | 0.01 | 64684.95 | 14.1 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 6.49 | 2.49 | 0.15 | 148724.04 | 32.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.52 | 1.94 | 1.03 | -0.05 | 46262.27 | 41.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.79 | 0.15 | 0.02 | 1556.07 | 21.51 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.85 | 0.35 | 0.01 | 56386.63 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.52 | 0.52 | 0.01 | 39548.12 | 37.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
