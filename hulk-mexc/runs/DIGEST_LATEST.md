# Hulk DIGEST — 2026-08-22T11:29:22Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.72 | -0.0 | 51633652.23 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.52 | 0.07 | 217369819.13 | 4.03 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.61 | 0.11 | 808844.82 | 9.5 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.67 | 0.0 | 1258044.67 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.58 | 6.27 | 4.42 | 0.01 | 587982.66 | 9.6 | skipped_fast |
| ZBCNUSDT | IDLE | 2.31 | 5.93 | 4.69 | -0.03 | 396125.14 | 29.98 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.31 | -0.11 | 637869.11 | 3.37 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.26 | -0.05 | 79007.54 | 22.78 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.64 | 3.18 | -0.06 | 237227.32 | 3.25 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.81 | -0.04 | 168361.55 | 21.47 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 4.3 | 1.08 | 0.03 | 73677.96 | 11.76 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 4.89 | 0.03 | 155203.18 | 14.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | 0.0 | 11178.17 | 38.12 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 3.47 | 2.45 | -0.01 | 188574.48 | 6.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.78 | -0.03 | 48751.97 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.66 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57509.04 | 16.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
