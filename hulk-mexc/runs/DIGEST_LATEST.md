# Hulk DIGEST — 2026-08-28T20:09:06Z

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
| XRPUSDT | IDLE | 3.03 | 5.46 | 4.0 | -0.05 | 53187679.62 | 0.72 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 17.52 | 11.39 | 0.05 | 1033938.47 | 11.94 | skipped_fast |
| PYTHUSDT | IDLE | 2.79 | 5.81 | 3.42 | -0.05 | 842769.9 | 8.55 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 7.82 | 7.1 | -0.06 | 194119.94 | 36.21 | skipped_fast |
| CCUSDT | IDLE | 2.34 | 4.24 | 2.96 | -0.02 | 360048.63 | 10.9 | skipped_fast |
| WUSDT | IDLE | 2.51 | 5.41 | 3.89 | -0.06 | 205556.17 | 15.37 | skipped_fast |
| HBARUSDT | IDLE | 2.76 | 5.29 | 1.53 | -0.02 | 441546.8 | 1.31 | skipped_fast |
| BIOUSDT | IDLE | 2.65 | 5.85 | 4.13 | -0.05 | 94673.31 | 3.62 | skipped_fast |
| KITEUSDT | IDLE | 2.55 | 5.04 | 0.44 | 0.01 | 80061.41 | 19.62 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 4.01 | 2.49 | -0.05 | 72300.19 | 8.78 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 4.63 | 1.03 | -0.01 | 67554.72 | 13.22 | skipped_fast |
| QAITUSDT | IDLE | 1.06 | 13.93 | 10.98 | -0.19 | 73425.07 | 67.41 | skipped_fast |
| RWAINCUSDT | IDLE | 1.78 | 3.87 | 0.0 | 0.02 | 19225.31 | 48.09 | skipped_fast |
| RIZEUSDT | IDLE | 1.57 | 4.58 | 0.85 | -0.03 | 40195.88 | 48.16 | skipped_fast |
| RWAUSDT | IDLE | 2.46 | 4.33 | 3.91 | 0.0 | 54630.62 | 16.63 | skipped_fast |
| QNTUSDT | IDLE | 2.03 | 3.71 | 2.32 | -0.03 | 42822.02 | 6.55 | skipped_fast |
| FLUIDUSDT | IDLE | 2.3 | 4.19 | 2.79 | -0.05 | 4475.04 | 21.47 | skipped_fast |
| TELUSDT | IDLE | 1.5 | 3.42 | 3.2 | -0.1 | 102717.54 | 28.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
