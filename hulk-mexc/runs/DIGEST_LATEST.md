# Hulk DIGEST — 2026-08-22T11:48:54Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.88 | 0.01 | 51615773.56 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.47 | 0.08 | 216481516.83 | 2.69 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.58 | 0.14 | 786697.99 | 5.99 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.35 | 0.02 | 1253869.84 | 2.59 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.6 | 0.02 | 582615.55 | 13.75 | skipped_fast |
| ZBCNUSDT | IDLE | 2.25 | 5.93 | 3.59 | -0.03 | 387789.0 | 51.75 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.25 | -0.1 | 617662.72 | 3.34 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.15 | -0.03 | 79258.72 | 34.11 | skipped_fast |
| KITEUSDT | IDLE | 2.55 | 6.17 | 0.0 | 0.05 | 80507.8 | 10.57 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.08 | -0.03 | 240390.89 | 3.21 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.46 | -0.03 | 167305.71 | 42.8 | skipped_fast |
| QAITUSDT | IDLE | 2.15 | 4.16 | 0.97 | 0.01 | 2466.7 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.53 | 0.04 | 154571.76 | 13.37 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.73 | 0.01 | 188335.49 | 10.91 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.89 | -0.03 | 48674.89 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 20.82 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57724.06 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
