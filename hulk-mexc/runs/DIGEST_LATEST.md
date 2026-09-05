# Hulk DIGEST — 2026-09-05T17:27:18Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.72 | 1.4 | 0.25 | 0.02 | 21662291.31 | 2.11 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.28 | 0.11 | 0.01 | 174555152.9 | 0.32 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.81 | 0.19 | 0.01 | 341005938.36 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.57 | 8.91 | 4.43 | 0.07 | 480274.39 | 29.61 | skipped_fast |
| KITEUSDT | IDLE | 2.3 | 5.35 | 4.12 | -0.06 | 61287.45 | 8.72 | skipped_fast |
| RWAINCUSDT | IDLE | 2.87 | 5.2 | 3.64 | -0.01 | 7555.5 | 37.71 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 2.8 | 1.23 | 0.03 | 282984.99 | 8.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.25 | 2.38 | 0.81 | 0.02 | 325115.25 | 1.82 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 2.67 | 2.24 | -0.01 | 170739.26 | 13.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 11.89 | 1.75 | 0.23 | 144010.79 | 60.74 | skipped_fast |
| WUSDT | IDLE | 1.44 | 2.65 | 1.6 | 0.02 | 152077.23 | 12.08 | skipped_fast |
| BIOUSDT | IDLE | 1.55 | 3.0 | 0.68 | 0.04 | 78334.34 | 7.16 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 1.65 | 1.01 | 0.02 | 61033.4 | 10.39 | skipped_fast |
| EDELUSDT | IDLE | 0.26 | 4.79 | 1.59 | -0.01 | 175989.3 | 38.02 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.52 | 1.24 | 0.04 | 314276.94 | 1.24 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.02 | 0.35 | 0.03 | 52012.78 | 14.0 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.2 | 0.17 | -0.0 | 69288.51 | 46.59 | skipped_fast |
| QNTUSDT | IDLE | 0.61 | 1.21 | 0.12 | 0.0 | 40134.74 | 4.66 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.43 | 0.62 | 0.01 | 897.41 | 21.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.3 | 0.05 | 0.0 | 38355.58 | 12.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
