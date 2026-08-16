# Hulk DIGEST — 2026-08-16T23:09:12Z

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
| XRPUSDT | IDLE | 0.67 | 1.2 | 0.87 | -0.01 | 6608220.82 | 1.01 | skipped_fast |
| RIZEUSDT | IDLE | 3.66 | 7.8 | 1.92 | 0.01 | 37372.45 | 59.59 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 7.25 | 4.9 | 0.02 | 296888.25 | 3.56 | skipped_fast |
| PYTHUSDT | IDLE | 1.87 | 3.38 | 2.46 | -0.02 | 147582.76 | 5.19 | skipped_fast |
| CCUSDT | IDLE | 0.57 | 1.25 | 0.0 | -0.04 | 334227.32 | 5.22 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 2.75 | 1.95 | -0.02 | 67974.98 | 4.14 | skipped_fast |
| EDELUSDT | IDLE | 1.97 | 3.74 | 1.29 | 0.03 | 60636.68 | 52.36 | skipped_fast |
| WUSDT | IDLE | 1.11 | 2.14 | 0.48 | 0.01 | 182812.12 | 14.06 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 1.57 | 0.73 | -0.02 | 191623.63 | 18.49 | skipped_fast |
| REDUSDT | IDLE | 0.69 | 1.25 | 0.93 | -0.07 | 65911.15 | 12.71 | skipped_fast |
| KITEUSDT | IDLE | 0.75 | 1.34 | 1.07 | -0.03 | 55803.38 | 17.12 | skipped_fast |
| QAITUSDT | IDLE | 1.25 | 3.83 | 0.0 | -0.01 | 2289.9 | 61.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.78 | 1.37 | 1.29 | 0.05 | 8958.85 | 45.27 | skipped_fast |
| HBARUSDT | IDLE | 0.67 | 1.21 | 0.93 | -0.01 | 100415.35 | 1.55 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 1.74 | 0.89 | -0.02 | 95151.67 | 34.59 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 1.61 | 0.82 | -0.02 | 33880.66 | 1.76 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.7 | 0.61 | -0.0 | 50645.54 | 8.75 | skipped_fast |
| FLUIDUSDT | IDLE | 0.67 | 1.16 | 1.15 | 0.01 | 220.62 | 20.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
