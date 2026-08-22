# Hulk DIGEST — 2026-08-22T12:48:26Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.03 | 0.09 | 216002913.1 | 1.98 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 7.83 | 1.28 | 0.05 | 51596386.47 | 1.97 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.26 | 0.01 | 1252626.58 | 3.86 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.1 | 0.13 | 774880.86 | 7.63 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.74 | -0.0 | 575120.19 | 11.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 5.77 | 3.73 | -0.0 | 335407.44 | 20.49 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 1.98 | -0.11 | 606374.02 | 6.74 | skipped_fast |
| KITEUSDT | IDLE | 2.69 | 6.37 | 0.94 | 0.04 | 84902.39 | 8.86 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.7 | -0.05 | 238170.25 | 3.23 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 3.89 | 2.65 | -0.03 | 78254.75 | 45.15 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2384.58 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.42 | 0.01 | 152818.89 | 11.57 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.73 | -0.03 | 163201.57 | 58.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.41 | -0.01 | 187556.24 | 4.66 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 2.03 | 0.27 | -0.0 | 46801.64 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.02 | 57565.99 | 16.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.04 | 5072.55 | 21.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
