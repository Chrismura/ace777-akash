# Hulk DIGEST — 2026-08-18T09:23:05Z

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
| XRPUSDT | IDLE | 0.57 | 1.07 | 0.49 | -0.0 | 11974203.53 | 1.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 28.38 | 11.37 | 0.21 | 82407.01 | 22.84 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 11.21 | 8.04 | -0.02 | 82039.02 | 39.09 | skipped_fast |
| CHIPUSDT | IDLE | 2.12 | 8.07 | 3.63 | -0.07 | 285841.19 | 3.52 | skipped_fast |
| KITEUSDT | IDLE | 2.84 | 5.03 | 4.3 | -0.01 | 61472.13 | 14.29 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.55 | 1.35 | -0.04 | 290944.99 | 5.45 | skipped_fast |
| QAITUSDT | IDLE | 1.64 | 10.79 | 8.2 | -0.05 | 11418.58 | 63.39 | skipped_fast |
| RWAINCUSDT | IDLE | 1.79 | 3.21 | 2.52 | -0.04 | 1909.09 | 24.13 | skipped_fast |
| PYTHUSDT | IDLE | 0.83 | 1.54 | 0.76 | -0.03 | 179098.0 | 5.27 | skipped_fast |
| ZBCNUSDT | IDLE | 0.7 | 1.32 | 0.53 | -0.01 | 214858.21 | 14.67 | skipped_fast |
| WUSDT | IDLE | 0.76 | 1.37 | 0.94 | -0.03 | 154600.36 | 1.23 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.29 | 0.7 | -0.02 | 75930.57 | 4.13 | skipped_fast |
| RIZEUSDT | IDLE | 0.39 | 2.72 | 0.94 | -0.09 | 65478.86 | 43.7 | skipped_fast |
| HBARUSDT | IDLE | 0.49 | 0.95 | 0.24 | 0.01 | 128571.25 | 1.52 | skipped_fast |
| TELUSDT | IDLE | 0.68 | 1.44 | 0.28 | -0.03 | 134434.24 | 35.55 | skipped_fast |
| QNTUSDT | IDLE | 0.52 | 0.93 | 0.69 | -0.0 | 36901.03 | 5.37 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.61 | 0.43 | -0.0 | 50132.74 | 8.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.21 | 0.38 | 0.23 | -0.04 | 202.93 | 5.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
