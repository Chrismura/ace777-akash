# Hulk DIGEST — 2026-09-16T08:12:34Z

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
| XRPUSDT | IDLE | 0.74 | 2.52 | 2.24 | -0.08 | 96167653.61 | 2.34 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.26 | 1.03 | -0.03 | 483729506.9 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.8 | 0.7 | -0.02 | 606316508.42 | 0.06 | skipped_fast |
| PYTHUSDT | IDLE | 2.01 | 3.54 | 3.21 | -0.04 | 665961.36 | 3.81 | skipped_fast |
| EDELUSDT | IDLE | 1.31 | 19.68 | 12.15 | 0.41 | 428602.59 | 19.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.33 | 27.54 | 2.93 | 0.42 | 43045.53 | 61.31 | skipped_fast |
| CCUSDT | IDLE | 1.02 | 1.81 | 1.48 | -0.04 | 387448.83 | 5.49 | skipped_fast |
| REDUSDT | IDLE | 2.08 | 4.36 | 3.82 | -0.03 | 69172.51 | 16.81 | skipped_fast |
| WUSDT | IDLE | 1.41 | 3.0 | 2.82 | -0.08 | 205170.29 | 10.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 4.49 | 4.3 | -0.11 | 117655.08 | 16.42 | skipped_fast |
| KITEUSDT | IDLE | 1.74 | 3.09 | 2.74 | -0.06 | 61192.61 | 16.07 | skipped_fast |
| ZBCNUSDT | IDLE | 0.76 | 2.49 | 1.99 | -0.05 | 221990.68 | 39.01 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.07 | 1.95 | -0.02 | 80026.43 | 16.25 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.19 | 0.88 | -0.03 | 465172.26 | 1.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 1.68 | 1.31 | -0.04 | 13395.41 | 17.32 | skipped_fast |
| TELUSDT | IDLE | 1.22 | 2.54 | 1.07 | -0.07 | 107650.06 | 27.1 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 2.18 | 2.13 | -0.06 | 44814.22 | 1.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.44 | 1.42 | -0.06 | 1312.08 | 22.12 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.53 | 0.3 | -0.01 | 52615.59 | 15.17 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.48 | 0.25 | -0.02 | 29719.69 | 8.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
