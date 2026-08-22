# Hulk DIGEST — 2026-08-22T11:30:44Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.72 | -0.0 | 51633768.34 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.65 | 0.07 | 217435645.35 | 1.35 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 10.24 | 7.38 | 0.11 | 808360.41 | 7.77 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.75 | 0.0 | 1259602.63 | 3.89 | skipped_fast |
| WUSDT | IDLE | 1.58 | 6.27 | 4.36 | 0.01 | 588788.7 | 12.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.31 | 5.93 | 4.61 | -0.03 | 395883.8 | 23.26 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 1.98 | -0.1 | 637818.73 | 6.73 | skipped_fast |
| EDELUSDT | IDLE | 2.77 | 4.93 | 4.04 | -0.05 | 78957.57 | 22.81 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.64 | 3.18 | -0.06 | 237404.94 | 3.25 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.75 | 5.86 | -0.04 | 168283.38 | 21.47 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 4.3 | 0.68 | 0.03 | 73675.7 | 11.72 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 4.82 | 0.03 | 155167.52 | 13.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | 0.0 | 11178.17 | 38.12 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 3.47 | 2.31 | -0.01 | 188582.64 | 10.97 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.99 | -0.03 | 48764.01 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 23.14 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57656.74 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
