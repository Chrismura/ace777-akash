# Hulk DIGEST — 2026-10-08T01:11:56Z

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
| WUSDT | IDLE | 3.18 | 22.82 | 2.61 | 0.18 | 1277404.16 | 18.65 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 2.34 | 1.69 | -0.06 | 3123230.39 | 0.4 | skipped_fast |
| XRPUSDT | IDLE | 0.79 | 1.57 | 0.12 | -0.05 | 49186493.64 | 2.1 | skipped_fast |
| ETHUSDT | IDLE | 0.44 | 0.86 | 0.19 | -0.04 | 550774530.81 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 0.29 | 0.56 | 0.19 | -0.02 | 820346163.32 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.72 | 3.33 | 0.69 | -0.02 | 703099.69 | 8.12 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 14.18 | 9.01 | -0.22 | 530826.98 | 56.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.09 | 4.63 | 2.67 | -0.07 | 281963.57 | 24.5 | skipped_fast |
| CCUSDT | IDLE | 0.84 | 1.5 | 1.24 | -0.06 | 434374.53 | 9.23 | skipped_fast |
| BIOUSDT | IDLE | 2.19 | 5.47 | 0.65 | -0.03 | 83338.65 | 3.28 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.66 | 0.21 | -0.06 | 707506.2 | 3.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.84 | 3.95 | 0.38 | -0.03 | 139701.55 | 9.63 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.81 | 5.57 | 5.18 | -0.1 | 184614.94 | 30.6 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 11.01 | 0.49 | -0.11 | 60791.67 | 62.03 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 1.72 | 0.48 | -0.06 | 56809.23 | 8.61 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 1.64 | 0.32 | -0.04 | 65595.0 | 11.84 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 3.36 | 1.03 | -0.13 | 52663.05 | 10.0 | skipped_fast |
| FLUIDUSDT | IDLE | 0.72 | 2.58 | 0.02 | 0.09 | 15601.47 | 21.49 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.83 | 0.22 | -0.01 | 50243.09 | 14.97 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.79 | 0.2 | -0.01 | 37498.55 | 23.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
