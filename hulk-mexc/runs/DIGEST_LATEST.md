# Hulk DIGEST — 2026-09-15T05:44:54Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 49.04 | 21.03 | 0.26 | 450846.99 | 5.65 | skipped_fast |
| XRPUSDT | IDLE | 1.16 | 2.19 | 1.72 | 0.02 | 76110768.24 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.66 | 1.16 | -0.01 | 468866047.76 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.67 | 1.2 | 0.98 | -0.0 | 519254565.09 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.96 | 40.02 | 21.08 | -0.13 | 54143.16 | 67.13 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 17.54 | 14.11 | 0.06 | 167666.49 | 17.23 | skipped_fast |
| PYTHUSDT | IDLE | 2.43 | 4.32 | 3.55 | -0.05 | 313538.19 | 1.81 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 3.98 | 3.0 | 0.01 | 194203.84 | 18.34 | skipped_fast |
| WUSDT | IDLE | 2.0 | 3.54 | 3.05 | -0.04 | 201894.81 | 12.25 | skipped_fast |
| CHIPUSDT | IDLE | 2.52 | 4.47 | 3.83 | -0.05 | 67776.56 | 19.56 | skipped_fast |
| CCUSDT | IDLE | 0.83 | 1.48 | 1.23 | -0.01 | 318415.75 | 4.19 | skipped_fast |
| HBARUSDT | IDLE | 1.55 | 2.74 | 2.34 | 0.0 | 387290.14 | 1.3 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.13 | 1.39 | -0.0 | 97385.96 | 11.75 | skipped_fast |
| TELUSDT | IDLE | 2.05 | 4.65 | 3.78 | 0.01 | 102333.71 | 31.2 | skipped_fast |
| KITEUSDT | IDLE | 0.9 | 1.65 | 0.97 | -0.02 | 64956.08 | 12.27 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.39 | 1.37 | -0.0 | 5095.31 | 22.16 | skipped_fast |
| QNTUSDT | IDLE | 1.15 | 2.04 | 1.71 | 0.0 | 46414.99 | 6.25 | skipped_fast |
| FLUIDUSDT | IDLE | 1.19 | 2.08 | 2.04 | 0.0 | 1864.24 | 21.92 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.45 | -0.01 | 54132.3 | 22.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.64 | 0.55 | 0.01 | 34584.17 | 29.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
