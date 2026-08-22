# Hulk DIGEST — 2026-08-22T11:59:34Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 6.86 | 0.01 | 51607371.5 | 4.1 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.6 | 0.09 | 216113560.36 | 2.02 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.7 | 0.13 | 780586.22 | 9.42 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.41 | 0.02 | 1257962.55 | 6.46 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.57 | 0.01 | 580766.16 | 14.79 | skipped_fast |
| ZBCNUSDT | IDLE | 2.3 | 5.93 | 4.38 | -0.03 | 382179.49 | 25.27 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 0.96 | -0.1 | 617347.08 | 3.33 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.26 | -0.04 | 79048.94 | 22.78 | skipped_fast |
| KITEUSDT | IDLE | 2.61 | 6.24 | 0.5 | 0.04 | 81845.01 | 8.83 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.17 | -0.03 | 241255.43 | 3.21 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 6.75 | 5.31 | -0.03 | 167523.71 | 32.03 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | 0.0 | 2438.68 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.53 | 0.02 | 154231.56 | 14.25 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 76.09 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 2.89 | 0.97 | -0.04 | 48596.46 | 29.22 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.62 | 0.0 | 188327.96 | 6.22 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.29 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57870.85 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
