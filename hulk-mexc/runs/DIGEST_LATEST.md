# Hulk DIGEST — 2026-08-22T12:27:37Z

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.61 | 0.12 | 215793158.47 | 5.27 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 7.83 | 2.2 | 0.05 | 51603708.98 | 1.99 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 4.63 | 1.93 | 0.03 | 1260356.28 | 6.41 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 8.38 | 3.28 | 0.14 | 773744.82 | 10.05 | skipped_fast |
| WUSDT | IDLE | 1.54 | 6.27 | 3.23 | 0.02 | 576038.31 | 14.74 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.55 | -0.02 | 371154.82 | 20.98 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.16 | -0.09 | 606302.32 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.32 | 0.05 | 83544.56 | 20.22 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 3.89 | 2.54 | -0.02 | 78104.18 | 22.57 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 5.65 | 0.79 | -0.01 | 241947.34 | 6.34 | skipped_fast |
| QAITUSDT | IDLE | 2.25 | 4.16 | 2.33 | -0.01 | 2396.75 | 43.59 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.99 | -0.03 | 163897.7 | 42.58 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.43 | 0.02 | 153219.6 | 13.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 3.47 | 1.06 | 0.01 | 187993.48 | 9.29 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.27 | -0.03 | 47958.01 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.99 | 1.8 | 1.2 | 0.02 | 57757.12 | 8.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 21.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
