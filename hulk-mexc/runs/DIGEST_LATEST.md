# Hulk DIGEST — 2026-08-22T11:24:16Z

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
| PYTHUSDT | IDLE | 2.18 | 9.66 | 7.55 | 0.0 | 51640754.64 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.64 | 0.07 | 217274157.99 | 2.69 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.68 | 0.11 | 809373.49 | 9.52 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 5.26 | 3.87 | 0.0 | 1260600.75 | 5.2 | skipped_fast |
| WUSDT | IDLE | 1.57 | 6.27 | 4.1 | 0.01 | 582842.54 | 3.19 | skipped_fast |
| ZBCNUSDT | IDLE | 2.33 | 5.93 | 5.13 | -0.04 | 395959.76 | 16.62 | skipped_fast |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.67 | -0.11 | 641102.26 | 3.39 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.26 | -0.05 | 78932.5 | 22.81 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.58 | -0.06 | 239034.35 | 3.26 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.75 | 5.92 | -0.04 | 168435.56 | 21.48 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 4.3 | 1.1 | 0.04 | 73719.94 | 5.43 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 5.04 | 0.02 | 154644.84 | 12.69 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | 0.0 | 11178.17 | 38.12 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 3.47 | 2.53 | -0.01 | 188629.79 | 6.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.97 | -0.01 | 48837.79 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.65 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57514.78 | 16.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
