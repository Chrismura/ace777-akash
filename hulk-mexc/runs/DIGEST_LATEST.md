# Hulk DIGEST — 2026-09-10T01:14:17Z

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
| XRPUSDT | IDLE | 1.07 | 1.97 | 1.07 | -0.02 | 43328574.99 | 2.16 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.43 | 0.34 | -0.01 | 385544860.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.93 | 0.21 | -0.01 | 555388660.92 | 0.02 | skipped_fast |
| PYTHUSDT | IDLE | 2.53 | 6.65 | 4.2 | -0.03 | 1043280.07 | 1.92 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.05 | 14.07 | 1.14 | 0.08 | 219282.27 | 26.51 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 2.75 | 1.37 | -0.04 | 629148.03 | 8.65 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 8.04 | 5.67 | -0.09 | 103435.95 | 7.85 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 13.98 | 9.84 | -0.07 | 124253.12 | 15.97 | skipped_fast |
| WUSDT | IDLE | 2.6 | 5.08 | 2.56 | -0.03 | 211227.68 | 15.12 | skipped_fast |
| REDUSDT | IDLE | 2.79 | 5.33 | 1.69 | 0.01 | 64168.58 | 7.76 | skipped_fast |
| RWAINCUSDT | IDLE | 2.15 | 3.88 | 2.74 | -0.01 | 6032.32 | 5.67 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.45 | 1.17 | -0.03 | 471770.92 | 1.3 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 3.5 | 1.67 | -0.01 | 57119.61 | 13.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 2.1 | 1.26 | 0.02 | 184371.91 | 12.63 | skipped_fast |
| RIZEUSDT | IDLE | 0.82 | 10.0 | 0.48 | 0.03 | 75216.34 | 107.06 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.62 | -0.03 | 55327.79 | 14.95 | skipped_fast |
| MNSRYUSDT | IDLE | 1.25 | 2.18 | 2.12 | -0.01 | 26126.59 | 5.54 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.16 | 1.03 | -0.0 | 45269.79 | 5.97 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 1.84 | 1.54 | 0.01 | 97440.92 | 50.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.75 | 1.72 | -0.08 | 997.13 | 21.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
