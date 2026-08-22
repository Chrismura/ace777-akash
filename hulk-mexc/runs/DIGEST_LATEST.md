# Hulk DIGEST — 2026-08-22T11:25:38Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.89 | -0.0 | 51639939.29 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.66 | 0.07 | 217291370.39 | 3.37 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.79 | 0.11 | 810133.16 | 5.2 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 5.26 | 3.8 | 0.0 | 1260604.63 | 5.19 | skipped_fast |
| WUSDT | IDLE | 1.57 | 6.27 | 4.04 | 0.01 | 582782.49 | 2.13 | skipped_fast |
| ZBCNUSDT | IDLE | 2.33 | 5.93 | 5.03 | -0.04 | 395965.52 | 15.59 | skipped_fast |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.67 | -0.11 | 641110.63 | 10.17 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.26 | -0.05 | 78957.53 | 34.19 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.64 | 3.46 | -0.05 | 239068.87 | 6.52 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.75 | 5.92 | -0.04 | 168461.53 | 16.12 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 4.3 | 0.93 | 0.04 | 73670.65 | 12.65 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 5.01 | 0.02 | 154727.83 | 9.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | 0.0 | 11178.17 | 38.12 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.97 | -0.02 | 48799.03 | 29.22 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 3.47 | 2.65 | -0.01 | 188618.12 | 11.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.68 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57491.9 | 8.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
