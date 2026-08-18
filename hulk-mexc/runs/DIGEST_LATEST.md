# Hulk DIGEST — 2026-08-18T11:27:52Z

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
| XRPUSDT | IDLE | 0.5 | 0.97 | 0.15 | -0.0 | 11792706.89 | 2.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.44 | 11.21 | 8.16 | -0.04 | 80050.73 | 39.19 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.47 | 8.85 | 6.79 | -0.04 | 3436.58 | 5.98 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 5.9 | 2.82 | -0.05 | 267199.64 | 6.98 | skipped_fast |
| REDUSDT | IDLE | 1.5 | 13.13 | 6.97 | 0.22 | 90122.14 | 22.84 | skipped_fast |
| CCUSDT | IDLE | 1.4 | 2.53 | 1.86 | -0.04 | 284987.95 | 5.48 | skipped_fast |
| QAITUSDT | IDLE | 1.64 | 10.79 | 8.2 | -0.04 | 11442.24 | 43.44 | skipped_fast |
| KITEUSDT | IDLE | 1.78 | 3.27 | 1.93 | -0.02 | 70959.03 | 14.2 | skipped_fast |
| PYTHUSDT | IDLE | 0.79 | 1.51 | 0.44 | -0.02 | 200505.81 | 2.63 | skipped_fast |
| ZBCNUSDT | IDLE | 0.86 | 1.66 | 0.34 | -0.0 | 210244.66 | 17.12 | skipped_fast |
| WUSDT | IDLE | 0.64 | 1.19 | 0.54 | -0.03 | 153130.17 | 14.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.94 | 5.11 | 0.33 | -0.17 | 50647.67 | 40.6 | skipped_fast |
| BIOUSDT | IDLE | 0.6 | 1.2 | 0.04 | -0.01 | 75986.65 | 4.1 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.23 | 0.07 | -0.03 | 136447.59 | 49.31 | skipped_fast |
| HBARUSDT | IDLE | 0.46 | 0.92 | 0.0 | -0.0 | 122774.33 | 1.51 | skipped_fast |
| QNTUSDT | IDLE | 0.32 | 0.61 | 0.2 | 0.0 | 38023.52 | 3.57 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.61 | 0.17 | -0.0 | 50546.15 | 17.36 | skipped_fast |
| FLUIDUSDT | IDLE | 0.2 | 0.41 | 0.0 | -0.03 | 238.93 | 20.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
