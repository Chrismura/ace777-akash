# Hulk DIGEST — 2026-08-19T05:48:30Z

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
| XRPUSDT | IDLE | 0.26 | 0.5 | 0.14 | 0.01 | 9864899.32 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.67 | 5.77 | 5.19 | -0.09 | 185526.89 | 7.83 | skipped_fast |
| PYTHUSDT | IDLE | 1.76 | 3.25 | 1.8 | 0.02 | 169927.21 | 2.58 | skipped_fast |
| REDUSDT | IDLE | 1.27 | 7.34 | 5.36 | -0.18 | 162710.2 | 9.1 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.33 | 1.63 | -0.02 | 214435.49 | 10.0 | skipped_fast |
| ZBCNUSDT | IDLE | 0.82 | 1.58 | 0.37 | 0.01 | 166891.16 | 13.35 | skipped_fast |
| WUSDT | IDLE | 0.9 | 1.58 | 1.44 | -0.01 | 121841.17 | 11.26 | skipped_fast |
| EDELUSDT | IDLE | 0.95 | 2.71 | 2.37 | -0.03 | 73548.44 | 26.99 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.84 | 0.16 | 0.03 | 62754.1 | 4.02 | skipped_fast |
| KITEUSDT | IDLE | 0.85 | 1.49 | 1.45 | -0.04 | 65412.82 | 14.36 | skipped_fast |
| QAITUSDT | IDLE | 0.48 | 3.72 | 3.58 | -0.18 | 12274.68 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.43 | 0.82 | 0.0 | 10698.05 | 71.34 | skipped_fast |
| HBARUSDT | IDLE | 0.72 | 1.36 | 0.59 | 0.03 | 116437.86 | 1.48 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.36 | 0.48 | 0.0 | 37948.59 | 3.56 | skipped_fast |
| RWAUSDT | IDLE | 0.75 | 1.32 | 1.22 | -0.02 | 51415.19 | 17.61 | skipped_fast |
| TELUSDT | IDLE | 0.68 | 1.25 | 0.75 | 0.04 | 87641.42 | 41.44 | skipped_fast |
| RIZEUSDT | IDLE | 1.31 | 3.36 | 2.41 | -0.04 | 27496.03 | 258.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.47 | 0.47 | -0.01 | 175.53 | 23.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
