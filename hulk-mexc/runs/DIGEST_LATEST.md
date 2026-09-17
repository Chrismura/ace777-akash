# Hulk DIGEST — 2026-09-17T09:03:54Z

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
| ETHUSDT | IDLE | 0.63 | 1.2 | 0.35 | 0.02 | 371032584.17 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.53 | 1.03 | 0.17 | 0.01 | 55663668.73 | 2.3 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.64 | 0.06 | 0.01 | 483515160.24 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.07 | 3.9 | 1.54 | 0.03 | 534726.57 | 3.69 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 4.99 | 0.24 | 0.11 | 624597.47 | 9.85 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 9.16 | 5.72 | -0.06 | 211654.39 | 36.5 | skipped_fast |
| CHIPUSDT | IDLE | 2.73 | 7.61 | 0.64 | 0.06 | 142228.8 | 18.02 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 1.7 | 1.01 | 0.02 | 169522.57 | 14.96 | skipped_fast |
| WUSDT | IDLE | 0.58 | 1.15 | 0.09 | 0.05 | 226271.54 | 7.52 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 3.32 | 2.4 | 0.07 | 67562.96 | 11.24 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.21 | 0.28 | -0.0 | 431210.06 | 1.35 | skipped_fast |
| REDUSDT | IDLE | 0.84 | 1.68 | 0.05 | 0.01 | 61573.75 | 16.69 | skipped_fast |
| RIZEUSDT | IDLE | 0.82 | 8.9 | 3.77 | -0.12 | 61181.9 | 89.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.47 | 2.57 | 2.44 | -0.0 | 17643.94 | 87.34 | skipped_fast |
| BIOUSDT | IDLE | 0.59 | 1.16 | 0.12 | 0.03 | 69968.63 | 15.78 | skipped_fast |
| RWAUSDT | IDLE | 1.73 | 3.31 | 0.97 | 0.02 | 58756.22 | 52.45 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.45 | 0.1 | 0.04 | 34549.02 | 4.86 | skipped_fast |
| TELUSDT | IDLE | 0.64 | 1.19 | 0.55 | -0.02 | 113053.03 | 48.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.96 | 0.07 | 0.01 | 37560.44 | 2.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.0 | 1551.54 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
