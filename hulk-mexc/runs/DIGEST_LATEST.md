# Hulk DIGEST — 2026-08-21T23:59:42Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.49 | 0.1 | 6231851.13 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.28 | 0.15 | 142096167.49 | 2.06 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.88 | 0.12 | 515141.56 | 14.99 | skipped_fast |
| HBARUSDT | IDLE | 2.62 | 6.36 | 1.13 | 0.09 | 909397.93 | 1.25 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.42 | 0.67 | 0.13 | 646348.18 | 6.2 | skipped_fast |
| WUSDT | IDLE | 2.77 | 6.91 | 1.82 | 0.08 | 379052.11 | 10.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.13 | 0.05 | 545621.96 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.05 | 0.03 | 187203.38 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | -0.01 | 80067.22 | 11.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 9.82 | 4.18 | 0.13 | 58946.22 | 22.08 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.41 | 0.06 | 189805.6 | 10.27 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.98 | 0.18 | 157640.87 | 10.52 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.07 | 0.07 | 162768.57 | 1.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10291.37 | 42.83 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.74 | 0.1 | 61515.24 | 12.93 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54481.67 | 16.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
