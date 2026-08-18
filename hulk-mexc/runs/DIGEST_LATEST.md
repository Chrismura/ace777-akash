# Hulk DIGEST — 2026-08-18T01:18:31Z

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
| XRPUSDT | IDLE | 0.3 | 0.54 | 0.43 | 0.0 | 11826340.98 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.2 | 5.74 | 3.24 | 0.0 | 335977.76 | 7.2 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.78 | 0.81 | -0.05 | 274250.17 | 9.96 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 2.77 | 1.41 | 0.0 | 65910.88 | 13.01 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 5.85 | 2.59 | -0.05 | 131389.12 | 50.31 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 1.56 | 1.33 | -0.01 | 144331.02 | 2.6 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 7.23 | 5.72 | 0.02 | 87097.45 | 47.1 | skipped_fast |
| WUSDT | IDLE | 0.9 | 1.62 | 1.24 | -0.05 | 133902.56 | 8.52 | skipped_fast |
| QAITUSDT | IDLE | 1.89 | 3.62 | 1.08 | -0.04 | 4076.43 | 60.02 | skipped_fast |
| ZBCNUSDT | IDLE | 0.53 | 1.01 | 0.36 | 0.0 | 227943.08 | 13.3 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 2.17 | 0.05 | 0.01 | 57305.99 | 26.19 | skipped_fast |
| BIOUSDT | IDLE | 0.63 | 1.1 | 1.05 | 0.02 | 81500.36 | 4.07 | skipped_fast |
| KITEUSDT | IDLE | 0.73 | 1.28 | 1.25 | -0.02 | 59970.45 | 14.14 | skipped_fast |
| RWAINCUSDT | IDLE | 0.41 | 0.76 | 0.41 | -0.03 | 1057.17 | 58.58 | skipped_fast |
| HBARUSDT | IDLE | 0.33 | 0.62 | 0.21 | 0.02 | 121835.15 | 1.52 | skipped_fast |
| QNTUSDT | IDLE | 0.59 | 1.06 | 0.75 | 0.01 | 35074.12 | 7.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.24 | 1.12 | -0.03 | 751.16 | 37.38 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.61 | 0.43 | 0.01 | 49294.23 | 25.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
