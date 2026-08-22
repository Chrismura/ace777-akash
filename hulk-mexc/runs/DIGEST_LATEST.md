# Hulk DIGEST — 2026-08-22T12:26:36Z

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
| XRPUSDT | IDLE | 2.47 | 14.26 | 6.44 | 0.12 | 215868755.6 | 4.6 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 7.83 | 2.21 | 0.05 | 51603180.21 | 3.97 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 4.63 | 1.87 | 0.03 | 1260238.08 | 5.12 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 8.38 | 3.08 | 0.14 | 775048.3 | 10.91 | skipped_fast |
| WUSDT | IDLE | 1.53 | 6.27 | 2.96 | 0.02 | 575870.68 | 7.35 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.54 | -0.02 | 371083.0 | 10.23 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.16 | -0.09 | 606238.22 | 6.68 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.32 | 0.05 | 83488.34 | 4.41 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.02 | 78129.13 | 22.57 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 5.65 | 0.38 | -0.01 | 241891.72 | 3.16 | skipped_fast |
| QAITUSDT | IDLE | 2.25 | 4.16 | 2.33 | -0.01 | 2396.75 | 43.59 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.25 | 0.02 | 153186.6 | 9.68 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.83 | -0.03 | 164423.51 | 47.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 3.47 | 0.8 | 0.01 | 187973.97 | 7.73 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.27 | -0.04 | 47977.21 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57757.11 | 8.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 18.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
