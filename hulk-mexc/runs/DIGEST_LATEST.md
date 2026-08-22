# Hulk DIGEST — 2026-08-22T11:21:55Z

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
| PYTHUSDT | IDLE | 2.18 | 9.66 | 7.62 | 0.0 | 51642734.83 | 12.41 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.72 | 0.08 | 217494434.28 | 2.69 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.69 | 0.11 | 812648.62 | 6.05 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 5.26 | 3.8 | 0.01 | 1260691.38 | 5.19 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.94 | 0.02 | 583081.01 | 14.85 | skipped_fast |
| ZBCNUSDT | IDLE | 2.33 | 5.93 | 5.05 | -0.04 | 395862.69 | 2.08 | skipped_fast |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.41 | -0.11 | 641104.57 | 3.38 | skipped_fast |
| EDELUSDT | IDLE | 2.76 | 4.93 | 3.93 | -0.05 | 78871.03 | 45.56 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.64 | 3.02 | -0.05 | 238474.98 | 6.5 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.75 | 5.92 | -0.04 | 168402.98 | 21.48 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 4.3 | 1.18 | 0.04 | 73687.49 | 9.96 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 5.09 | 0.02 | 154584.0 | 9.96 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | 0.0 | 11178.17 | 38.12 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 3.47 | 2.34 | -0.0 | 188670.26 | 7.84 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.77 | -0.01 | 48813.13 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.36 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57502.37 | 24.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
