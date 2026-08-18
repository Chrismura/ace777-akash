# Hulk DIGEST — 2026-08-18T22:10:17Z

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
| XRPUSDT | IDLE | 0.23 | 0.43 | 0.24 | -0.0 | 10619229.38 | 1.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 7.03 | 5.5 | -0.02 | 10023.43 | 23.72 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 6.74 | 5.6 | -0.08 | 209347.7 | 3.82 | skipped_fast |
| RIZEUSDT | IDLE | 2.48 | 4.65 | 4.23 | -0.06 | 33112.31 | 45.1 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 2.69 | 2.16 | -0.01 | 173460.55 | 2.6 | skipped_fast |
| CCUSDT | IDLE | 0.7 | 1.3 | 0.65 | -0.0 | 236526.84 | 7.73 | skipped_fast |
| REDUSDT | IDLE | 0.71 | 5.38 | 2.79 | 0.09 | 151565.99 | 25.53 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 2.57 | 1.45 | -0.04 | 74357.75 | 13.4 | skipped_fast |
| ZBCNUSDT | IDLE | 0.5 | 0.96 | 0.32 | -0.01 | 171954.08 | 23.64 | skipped_fast |
| WUSDT | IDLE | 0.49 | 0.87 | 0.74 | -0.03 | 132731.75 | 14.9 | skipped_fast |
| BIOUSDT | IDLE | 0.52 | 0.94 | 0.73 | -0.0 | 64187.36 | 8.15 | skipped_fast |
| KITEUSDT | IDLE | 0.21 | 0.37 | 0.27 | -0.01 | 63739.34 | 14.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.72 | 3.05 | 2.58 | -0.02 | 212.15 | 21.91 | skipped_fast |
| QAITUSDT | IDLE | 0.22 | 3.0 | 1.73 | -0.18 | 18652.2 | 51.93 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.81 | 0.01 | 0.02 | 106739.01 | 1.49 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 1.89 | 0.21 | 0.04 | 90433.06 | 41.27 | skipped_fast |
| QNTUSDT | IDLE | 0.53 | 0.95 | 0.73 | -0.02 | 34439.97 | 3.58 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.35 | -0.01 | 50612.47 | 17.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
