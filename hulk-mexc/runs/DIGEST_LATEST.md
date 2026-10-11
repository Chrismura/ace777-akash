# Hulk DIGEST — 2026-10-11T00:06:44Z

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
| ETHUSDT | IDLE | 0.32 | 0.56 | 0.47 | 0.01 | 122681915.2 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.33 | 0.58 | 0.49 | 0.0 | 13055752.61 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.1 | 0.18 | 0.13 | 0.0 | 155622150.19 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.07 | 3.34 | 2.63 | 0.02 | 1252355.55 | 13.64 | skipped_fast |
| QNTUSDT | IDLE | 1.19 | 2.11 | 1.75 | -0.03 | 1262040.24 | 0.83 | skipped_fast |
| PYTHUSDT | IDLE | 0.91 | 1.64 | 1.14 | -0.02 | 758457.47 | 3.82 | skipped_fast |
| EDELUSDT | IDLE | 2.51 | 4.54 | 3.21 | -0.06 | 250519.2 | 13.04 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 11.6 | 3.22 | 0.31 | 266548.3 | 16.21 | skipped_fast |
| RIZEUSDT | IDLE | 2.4 | 5.84 | 5.02 | -0.08 | 34220.95 | 29.21 | skipped_fast |
| TELUSDT | IDLE | 2.58 | 4.89 | 4.01 | -0.07 | 145916.15 | 17.17 | skipped_fast |
| CCUSDT | IDLE | 0.6 | 1.07 | 0.91 | -0.03 | 260272.69 | 1.69 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.23 | 2.15 | 0.03 | 88040.1 | 3.44 | skipped_fast |
| ZBCNUSDT | IDLE | 0.71 | 1.34 | 0.57 | 0.02 | 186005.54 | 14.33 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 2.0 | 1.64 | 0.06 | 72790.75 | 8.62 | skipped_fast |
| REDUSDT | IDLE | 0.61 | 1.07 | 0.94 | 0.02 | 56061.92 | 15.98 | skipped_fast |
| HBARUSDT | IDLE | 0.44 | 0.79 | 0.54 | 0.0 | 310702.44 | 4.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.59 | 1.04 | 0.98 | -0.03 | 9763.62 | 24.53 | skipped_fast |
| MNSRYUSDT | IDLE | 1.02 | 1.82 | 1.42 | -0.01 | 36877.68 | 28.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.77 | 1.41 | 0.87 | 0.0 | 8172.97 | 13.26 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.79 | 0.7 | 0.0 | 53670.24 | 15.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
