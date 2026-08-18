# Hulk DIGEST — 2026-08-18T21:44:31Z

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
| XRPUSDT | IDLE | 0.28 | 0.52 | 0.33 | -0.0 | 10653868.35 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.26 | 6.74 | 6.03 | -0.09 | 217329.85 | 3.84 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.6 | 7.03 | 6.23 | -0.02 | 9806.23 | 41.8 | skipped_fast |
| PYTHUSDT | IDLE | 1.49 | 2.69 | 1.93 | -0.0 | 173402.34 | 5.18 | skipped_fast |
| RIZEUSDT | IDLE | 2.01 | 4.44 | 4.25 | -0.06 | 33496.93 | 50.62 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.47 | 1.14 | -0.0 | 236517.97 | 8.86 | skipped_fast |
| REDUSDT | IDLE | 0.8 | 6.03 | 3.04 | 0.08 | 149250.62 | 23.48 | skipped_fast |
| WUSDT | IDLE | 0.77 | 1.34 | 1.32 | -0.03 | 134806.56 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 0.65 | 1.22 | 0.5 | -0.01 | 173337.04 | 20.44 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 1.76 | 1.4 | -0.0 | 63877.75 | 12.22 | skipped_fast |
| EDELUSDT | IDLE | 0.88 | 2.57 | 1.85 | -0.04 | 74234.46 | 40.3 | skipped_fast |
| KITEUSDT | IDLE | 0.32 | 0.56 | 0.51 | -0.01 | 63999.08 | 12.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.72 | 3.05 | 2.58 | -0.01 | 222.14 | 21.97 | skipped_fast |
| QAITUSDT | IDLE | 0.25 | 3.28 | 2.28 | -0.18 | 18558.75 | 60.06 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.61 | 0.18 | 0.01 | 106133.06 | 1.5 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.96 | 0.48 | 0.04 | 90653.92 | 27.57 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 1.27 | 1.01 | -0.02 | 34574.25 | 3.58 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.7 | 0.52 | -0.01 | 50882.48 | 17.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
