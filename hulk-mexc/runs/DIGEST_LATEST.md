# Hulk DIGEST — 2026-08-13T00:27:17Z

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
| XRPUSDT | IDLE | 0.53 | 0.99 | 0.45 | -0.01 | 14410672.08 | 0.99 | skipped_fast |
| RIZEUSDT | IDLE | 2.02 | 16.86 | 5.29 | 0.2 | 53224.09 | 45.04 | skipped_fast |
| RWAINCUSDT | IDLE | 3.05 | 5.46 | 4.24 | -0.03 | 2064.97 | 32.82 | skipped_fast |
| EDELUSDT | IDLE | 2.33 | 8.33 | 5.81 | 0.07 | 71522.16 | 49.88 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 2.01 | 0.15 | -0.03 | 335424.76 | 2.47 | skipped_fast |
| QNTUSDT | IDLE | 3.1 | 5.57 | 4.18 | 0.01 | 60423.52 | 6.85 | skipped_fast |
| WUSDT | IDLE | 1.43 | 2.73 | 0.88 | -0.04 | 175135.82 | 12.37 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.26 | 1.23 | -0.04 | 62097.2 | 4.15 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 2.13 | 0.52 | -0.01 | 213006.18 | 10.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 2.15 | 0.6 | -0.03 | 167987.08 | 15.19 | skipped_fast |
| KITEUSDT | IDLE | 1.48 | 2.85 | 0.79 | -0.04 | 55167.71 | 12.78 | skipped_fast |
| CHIPUSDT | IDLE | 1.01 | 2.23 | 1.71 | 0.03 | 104070.31 | 8.69 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 2.1 | 0.56 | -0.01 | 60632.54 | 16.45 | skipped_fast |
| QAITUSDT | IDLE | 0.77 | 2.51 | 1.67 | -0.04 | 4081.32 | 60.51 | skipped_fast |
| HBARUSDT | IDLE | 0.35 | 0.69 | 0.05 | -0.01 | 83583.31 | 1.51 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.75 | 0.58 | 0.01 | 52207.08 | 16.64 | skipped_fast |
| TELUSDT | IDLE | 0.51 | 0.96 | 0.44 | -0.0 | 95968.54 | 57.02 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 0.64 | 0.23 | -0.02 | 547.16 | 17.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
