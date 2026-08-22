# Hulk DIGEST — 2026-08-22T00:57:27Z

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
| PYTHUSDT | IDLE | 2.0 | 7.38 | 0.62 | 0.13 | 6529549.49 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 8.72 | 2.11 | 0.15 | 147803802.0 | 2.76 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.6 | 0.08 | 942721.71 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.89 | 0.11 | 543419.39 | 35.85 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.74 | 0.14 | 650135.22 | 8.87 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.7 | 0.1 | 391271.5 | 15.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.46 | 0.02 | 544876.89 | 3.05 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.62 | 0.46 | 0.05 | 186642.57 | 6.15 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.02 | 79766.08 | 22.17 | skipped_fast |
| TELUSDT | IDLE | 2.85 | 6.89 | 0.77 | 0.06 | 183889.18 | 30.9 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.58 | 3.12 | 0.19 | 159321.82 | 18.84 | skipped_fast |
| QNTUSDT | IDLE | 2.54 | 5.42 | 1.18 | 0.07 | 170552.81 | 1.51 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 4.3 | 0.26 | 0.11 | 60976.02 | 11.8 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.22 | 1.21 | 0.01 | 3850.39 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.02 | 9620.44 | 53.97 | skipped_fast |
| RIZEUSDT | IDLE | 2.27 | 9.82 | 4.18 | 0.11 | 60252.84 | 301.83 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54976.24 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 4.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
