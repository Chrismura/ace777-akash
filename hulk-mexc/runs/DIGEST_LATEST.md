# Hulk DIGEST — 2026-09-11T01:16:38Z

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
| XRPUSDT | IDLE | 1.14 | 2.12 | 1.08 | -0.03 | 42042758.17 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.43 | 0.53 | -0.01 | 423749992.57 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.11 | 0.63 | -0.02 | 529177061.1 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 10.01 | 6.73 | -0.07 | 100352.57 | 17.05 | skipped_fast |
| PYTHUSDT | IDLE | 1.59 | 2.94 | 1.62 | -0.01 | 425167.06 | 1.94 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 2.01 | 0.76 | -0.05 | 484318.5 | 5.06 | skipped_fast |
| ZBCNUSDT | IDLE | 2.07 | 3.79 | 2.28 | -0.01 | 204516.22 | 17.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 36.95 | 2.49 | -0.39 | 138514.33 | 120.34 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 5.04 | 4.36 | -0.05 | 221573.37 | 18.6 | skipped_fast |
| WUSDT | IDLE | 1.18 | 2.17 | 1.25 | -0.04 | 168252.74 | 16.76 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.49 | 1.52 | -0.04 | 57436.4 | 13.81 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.23 | 0.56 | -0.02 | 77574.35 | 4.0 | skipped_fast |
| REDUSDT | IDLE | 0.72 | 1.32 | 0.81 | -0.06 | 65581.22 | 18.99 | skipped_fast |
| RWAINCUSDT | IDLE | 0.66 | 1.24 | 0.56 | 0.01 | 4331.46 | 28.05 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.67 | 0.84 | -0.02 | 190468.21 | 1.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.69 | 3.38 | 0.0 | -0.03 | 2345.82 | 17.51 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 2.5 | 1.94 | -0.01 | 87292.66 | 45.22 | skipped_fast |
| QNTUSDT | IDLE | 1.27 | 2.37 | 1.17 | -0.03 | 36842.69 | 7.71 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.07 | 0.76 | -0.02 | 50722.44 | 15.27 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.56 | 0.43 | -0.01 | 36092.5 | 48.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
