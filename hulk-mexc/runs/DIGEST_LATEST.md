# Hulk DIGEST — 2026-10-15T02:32:42Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 9.22 | 7.51 | -0.12 | 2738780.98 | 13.72 | skipped_fast |
| PYTHUSDT | IDLE | 2.37 | 6.23 | 5.27 | 0.05 | 2305722.58 | 21.62 | skipped_fast |
| ETHUSDT | IDLE | 2.33 | 4.66 | 3.51 | -0.06 | 274719826.09 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.27 | 4.06 | 3.25 | -0.05 | 51495875.93 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 1.16 | 2.07 | 1.62 | -0.03 | 486837766.22 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.95 | 9.5 | 6.18 | -0.08 | 1083333.83 | 9.19 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 5.9 | 4.66 | -0.07 | 595231.62 | 6.17 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 6.63 | 5.51 | -0.11 | 427849.14 | 5.47 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.95 | 9.96 | 8.53 | -0.12 | 73088.55 | 20.5 | skipped_fast |
| CHIPUSDT | IDLE | 2.27 | 13.43 | 11.12 | -0.19 | 113960.08 | 21.33 | skipped_fast |
| EDELUSDT | IDLE | 2.82 | 4.94 | 4.71 | -0.06 | 185051.15 | 30.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.9 | 4.56 | 4.09 | -0.07 | 198032.49 | 18.99 | skipped_fast |
| REDUSDT | IDLE | 2.18 | 4.09 | 1.78 | -0.01 | 63582.23 | 14.68 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 6.03 | 4.68 | -0.06 | 88417.52 | 9.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.93 | 4.25 | 1.84 | 0.0 | 25586.69 | 15.19 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 7.12 | 4.24 | -0.04 | 55098.13 | 61.63 | skipped_fast |
| TELUSDT | IDLE | 2.38 | 4.24 | 3.45 | -0.06 | 100313.33 | 41.04 | skipped_fast |
| FLUIDUSDT | IDLE | 1.71 | 5.03 | 3.92 | 0.0 | 20748.25 | 21.47 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.62 | 0.95 | -0.04 | 57535.21 | 16.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.14 | 1.03 | -0.02 | 33203.66 | 65.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
