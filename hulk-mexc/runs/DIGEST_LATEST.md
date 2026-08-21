# Hulk DIGEST — 2026-08-21T20:55:57Z

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
| PYTHUSDT | IDLE | 1.29 | 4.78 | 2.05 | 0.09 | 5565835.37 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.44 | 0.1 | 128368113.32 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.32 | 0.18 | 152961.21 | 24.35 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 10.86 | 6.46 | 0.1 | 479273.5 | 80.05 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.35 | 0.1 | 642503.11 | 6.44 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.23 | 1.71 | 0.06 | 808827.98 | 2.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.73 | 0.08 | 514917.28 | 6.2 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.92 | 0.89 | 0.07 | 368051.11 | 13.63 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.33 | 2.64 | 0.01 | 188031.96 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.93 | 5.73 | 4.98 | -0.06 | 82458.17 | 34.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.71 | 0.36 | 0.03 | 56234.21 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 69.76 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 4.0 | 2.21 | 0.11 | 61328.46 | 9.29 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 181223.19 | 32.19 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60211.86 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 190.78 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 53895.11 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
