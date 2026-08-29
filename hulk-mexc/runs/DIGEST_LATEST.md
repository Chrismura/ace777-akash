# Hulk DIGEST — 2026-08-29T09:09:53Z

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
| CHIPUSDT | IDLE | 2.13 | 9.96 | 6.6 | 0.02 | 1304994.28 | 2.41 | skipped_fast |
| XRPUSDT | IDLE | 0.64 | 1.17 | 0.72 | -0.02 | 42304878.09 | 1.45 | skipped_fast |
| PYTHUSDT | IDLE | 1.3 | 2.32 | 1.91 | -0.04 | 485794.81 | 2.14 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 3.33 | 0.42 | 0.02 | 212520.11 | 8.82 | skipped_fast |
| WUSDT | IDLE | 1.42 | 2.5 | 2.22 | -0.03 | 211160.94 | 13.19 | skipped_fast |
| ZBCNUSDT | IDLE | 0.72 | 1.92 | 0.64 | -0.05 | 188041.36 | 11.68 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.29 | 1.26 | -0.04 | 425449.3 | 1.34 | skipped_fast |
| RIZEUSDT | IDLE | 1.54 | 3.21 | 1.15 | -0.01 | 29434.08 | 56.03 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.92 | 0.69 | -0.0 | 67046.73 | 10.21 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 2.02 | 0.49 | 0.03 | 62433.57 | 10.92 | skipped_fast |
| BIOUSDT | IDLE | 0.79 | 1.38 | 1.29 | -0.04 | 85657.53 | 3.63 | skipped_fast |
| EDELUSDT | IDLE | 1.14 | 4.2 | 3.75 | -0.11 | 90148.14 | 77.59 | skipped_fast |
| QAITUSDT | IDLE | 0.39 | 3.4 | 2.18 | -0.03 | 84131.97 | 57.07 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 1.66 | 1.63 | 0.01 | 3548.47 | 105.0 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 1.28 | 0.97 | -0.02 | 40561.99 | 1.64 | skipped_fast |
| TELUSDT | IDLE | 0.72 | 1.27 | 1.14 | -0.05 | 79382.04 | 28.76 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.16 | 0.57 | 0.01 | 55955.75 | 16.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.25 | 0.44 | 0.44 | -0.05 | 3704.21 | 22.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
