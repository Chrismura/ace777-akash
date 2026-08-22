# Hulk DIGEST — 2026-08-22T11:58:09Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.91 | 0.01 | 51608956.18 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.55 | 0.09 | 216185505.97 | 2.69 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.66 | 0.13 | 780350.58 | 6.84 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.36 | 0.02 | 1257988.46 | 5.17 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.67 | 0.01 | 580728.59 | 9.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.3 | 5.93 | 4.4 | -0.03 | 382776.72 | 24.75 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.19 | -0.1 | 618272.62 | 3.34 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.15 | -0.03 | 79333.67 | 22.78 | skipped_fast |
| KITEUSDT | IDLE | 2.61 | 6.24 | 0.58 | 0.04 | 81881.94 | 9.71 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.42 | -0.03 | 241274.77 | 3.22 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 6.75 | 5.31 | -0.03 | 167459.04 | 32.03 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.01 | 2438.68 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.55 | 0.02 | 154185.72 | 22.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.65 | 0.0 | 188385.02 | 9.34 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.92 | -0.04 | 48590.52 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.55 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 1.8 | 1.61 | 0.01 | 57870.54 | 16.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
