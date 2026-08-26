# Hulk DIGEST — 2026-08-26T01:44:33Z

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
| PYTHUSDT | IDLE | 1.82 | 3.88 | 0.16 | -0.01 | 2158065.87 | 3.92 | skipped_fast |
| XRPUSDT | IDLE | 2.0 | 4.78 | 2.09 | -0.04 | 71822054.58 | 2.08 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.39 | 0.74 | -0.02 | 533587.5 | 6.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.84 | 5.18 | 2.62 | -0.01 | 407337.78 | 6.33 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 2.22 | 1.13 | -0.03 | 761150.88 | 2.56 | skipped_fast |
| WUSDT | IDLE | 1.52 | 3.03 | 0.38 | -0.03 | 311570.44 | 14.85 | skipped_fast |
| BIOUSDT | IDLE | 2.17 | 4.18 | 1.02 | -0.01 | 104301.71 | 6.86 | skipped_fast |
| RIZEUSDT | IDLE | 2.64 | 5.51 | 2.27 | 0.02 | 50217.12 | 51.83 | skipped_fast |
| REDUSDT | IDLE | 2.1 | 5.54 | 1.34 | 0.03 | 81719.28 | 20.55 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 2.8 | 1.13 | 0.0 | 164737.85 | 13.71 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 9.23 | 6.36 | -0.0 | 165561.02 | 8.59 | skipped_fast |
| KITEUSDT | IDLE | 1.74 | 3.51 | 0.33 | -0.04 | 61129.77 | 9.75 | skipped_fast |
| QAITUSDT | IDLE | 2.02 | 5.43 | 1.48 | 0.03 | 12851.48 | 37.64 | skipped_fast |
| RWAINCUSDT | IDLE | 1.28 | 2.23 | 2.18 | -0.02 | 2540.19 | 35.47 | skipped_fast |
| FLUIDUSDT | IDLE | 2.13 | 3.96 | 2.03 | -0.03 | 390.01 | 20.64 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.59 | 0.47 | -0.02 | 135717.66 | 1.57 | skipped_fast |
| RWAUSDT | IDLE | 1.13 | 1.98 | 1.86 | -0.04 | 55988.9 | 8.25 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.18 | 0.55 | -0.03 | 98148.32 | 27.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
