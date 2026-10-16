# Hulk DIGEST — 2026-10-16T23:06:16Z

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
| PYTHUSDT | IDLE | 1.75 | 6.23 | 0.95 | -0.06 | 1950178.27 | 3.43 | skipped_fast |
| WUSDT | IDLE | 2.36 | 6.24 | 3.0 | -0.01 | 1559375.98 | 16.7 | skipped_fast |
| XRPUSDT | IDLE | 0.91 | 1.82 | 0.03 | -0.02 | 28925193.41 | 2.29 | skipped_fast |
| ETHUSDT | IDLE | 0.61 | 1.22 | 0.05 | -0.01 | 208669606.1 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.08 | 0.0 | -0.01 | 344015249.92 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.81 | 3.24 | 2.51 | -0.01 | 773545.72 | 1.0 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.08 | 2.83 | 0.01 | 188899.71 | 13.54 | skipped_fast |
| CCUSDT | IDLE | 1.21 | 2.36 | 0.46 | -0.02 | 360648.64 | 7.69 | skipped_fast |
| RWAINCUSDT | IDLE | 1.79 | 8.45 | 5.44 | -0.12 | 28153.26 | 11.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.27 | 1.24 | -0.02 | 190194.32 | 9.63 | skipped_fast |
| REDUSDT | IDLE | 1.66 | 3.7 | 0.85 | -0.07 | 96988.74 | 15.1 | skipped_fast |
| CHIPUSDT | IDLE | 0.74 | 2.91 | 0.39 | -0.03 | 154313.72 | 15.15 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.15 | 0.15 | -0.01 | 57334.49 | 9.04 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 2.02 | 0.08 | -0.02 | 61978.18 | 7.93 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 2.16 | 0.12 | -0.02 | 324975.88 | 5.97 | skipped_fast |
| RIZEUSDT | IDLE | 1.03 | 2.17 | 1.96 | -0.0 | 45934.79 | 30.92 | skipped_fast |
| FLUIDUSDT | IDLE | 2.34 | 4.65 | 0.2 | 0.0 | 5463.12 | 21.21 | skipped_fast |
| TELUSDT | IDLE | 1.68 | 3.0 | 2.41 | -0.03 | 92272.26 | 40.24 | skipped_fast |
| MNSRYUSDT | IDLE | 0.68 | 1.31 | 0.27 | -0.0 | 34317.65 | 19.73 | skipped_fast |
| RWAUSDT | IDLE | 0.18 | 0.32 | 0.24 | -0.0 | 53738.51 | 15.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
