# Hulk DIGEST — 2026-08-21T20:24:55Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 2.91 | 0.08 | 5507833.97 | 4.22 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 4.21 | 2.77 | 0.12 | 129095508.33 | 2.17 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.65 | 0.17 | 153477.41 | 8.92 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.53 | 0.11 | 478298.9 | 25.47 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 3.91 | 1.14 | 0.08 | 632772.33 | 6.5 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.9 | 0.06 | 801897.49 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.55 | 0.08 | 509793.45 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.1 | 3.92 | 1.84 | 0.06 | 366622.91 | 17.98 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.82 | 0.02 | 189588.89 | 3.16 | skipped_fast |
| EDELUSDT | IDLE | 2.71 | 4.77 | 4.33 | -0.05 | 80341.33 | 22.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.68 | 0.01 | 56217.64 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.47 | 0.11 | 61041.54 | 13.96 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2801.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.42 | 3.39 | 2.01 | 0.01 | 183624.53 | 26.93 | skipped_fast |
| QNTUSDT | IDLE | 1.42 | 2.65 | 1.32 | 0.04 | 59947.96 | 81.31 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.15 | 0.03 | 54313.07 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
