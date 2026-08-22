# Hulk DIGEST — 2026-08-22T12:51:17Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.05 | 0.09 | 216018125.25 | 1.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 7.83 | 1.3 | 0.05 | 51593392.39 | 1.97 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.27 | 0.01 | 1252458.86 | 6.43 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.02 | 0.13 | 775066.05 | 8.47 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.77 | -0.0 | 574614.44 | 10.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.59 | -0.0 | 335370.03 | 17.4 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.08 | -0.1 | 606355.32 | 3.37 | skipped_fast |
| KITEUSDT | IDLE | 2.69 | 6.37 | 0.99 | 0.04 | 84820.98 | 9.75 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.83 | -0.05 | 238198.6 | 3.24 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 3.89 | 2.54 | -0.02 | 78279.65 | 56.47 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2384.58 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.43 | 0.02 | 152750.36 | 20.48 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.99 | -0.03 | 162996.58 | 53.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.48 | -0.0 | 187602.92 | 4.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 2.03 | 0.34 | -0.01 | 46797.64 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57529.28 | 24.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.04 | 5072.55 | 20.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
