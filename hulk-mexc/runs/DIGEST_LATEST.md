# Hulk DIGEST — 2026-08-22T12:34:01Z

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.73 | 0.11 | 215971620.71 | 3.96 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 7.83 | 2.16 | 0.05 | 51604589.29 | 3.97 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.24 | 0.02 | 1260599.88 | 5.14 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.8 | 0.14 | 777792.19 | 5.01 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.71 | 0.01 | 578056.46 | 10.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 5.77 | 3.9 | -0.02 | 336164.24 | 27.73 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.32 | -0.1 | 605537.02 | 3.35 | skipped_fast |
| KITEUSDT | IDLE | 2.66 | 6.37 | 0.41 | 0.04 | 83644.63 | 6.17 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 3.89 | 2.43 | -0.02 | 78129.6 | 33.88 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 5.65 | 1.54 | -0.02 | 238210.13 | 12.77 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.16 | 2.56 | -0.01 | 2404.2 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.19 | 0.01 | 153185.21 | 11.55 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.99 | -0.03 | 163532.43 | 47.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.62 | -0.0 | 188068.91 | 6.21 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.91 | 0.44 | 0.0 | 46779.09 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57779.07 | 24.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 22.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
