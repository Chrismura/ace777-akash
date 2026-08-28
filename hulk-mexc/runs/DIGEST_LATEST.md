# Hulk DIGEST — 2026-08-28T18:09:02Z

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
| XRPUSDT | IDLE | 2.64 | 4.69 | 3.88 | -0.05 | 53882364.87 | 2.17 | skipped_fast |
| CHIPUSDT | IDLE | 2.33 | 14.34 | 9.29 | 0.09 | 963104.34 | 2.33 | skipped_fast |
| PYTHUSDT | IDLE | 2.8 | 5.81 | 3.59 | -0.07 | 908725.49 | 2.14 | skipped_fast |
| QAITUSDT | IDLE | 2.43 | 32.58 | 19.84 | -0.15 | 72823.04 | 60.91 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 5.51 | 5.18 | -0.06 | 198928.63 | 16.77 | skipped_fast |
| CCUSDT | IDLE | 2.41 | 4.39 | 2.91 | -0.03 | 357424.8 | 6.36 | skipped_fast |
| HBARUSDT | IDLE | 3.09 | 5.77 | 2.76 | -0.04 | 454816.46 | 1.32 | skipped_fast |
| WUSDT | IDLE | 2.74 | 5.91 | 4.24 | -0.06 | 210353.83 | 14.29 | skipped_fast |
| BIOUSDT | IDLE | 2.67 | 5.99 | 3.54 | -0.06 | 96253.45 | 7.19 | skipped_fast |
| REDUSDT | IDLE | 2.68 | 6.25 | 4.36 | -0.05 | 67944.03 | 14.5 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.25 | 4.07 | -0.1 | 67851.27 | 17.68 | skipped_fast |
| KITEUSDT | IDLE | 2.34 | 4.27 | 2.75 | -0.03 | 80484.69 | 12.92 | skipped_fast |
| RWAUSDT | IDLE | 3.26 | 5.9 | 4.14 | 0.0 | 55057.87 | 16.61 | skipped_fast |
| RIZEUSDT | IDLE | 1.64 | 4.58 | 2.76 | 0.05 | 56178.47 | 57.86 | skipped_fast |
| FLUIDUSDT | IDLE | 2.31 | 4.19 | 2.88 | -0.06 | 4807.84 | 21.53 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 3.33 | 2.73 | -0.04 | 42497.59 | 4.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 3.82 | 0.69 | 0.01 | 18028.29 | 64.27 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 4.07 | 3.37 | -0.08 | 112822.94 | 39.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
