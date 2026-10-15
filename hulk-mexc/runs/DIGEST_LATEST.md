# Hulk DIGEST — 2026-10-15T01:31:44Z

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
| PYTHUSDT | IDLE | 2.12 | 5.34 | 3.21 | 0.06 | 2122653.97 | 2.37 | skipped_fast |
| WUSDT | IDLE | 1.29 | 3.78 | 1.73 | -0.09 | 2477386.4 | 2.58 | skipped_fast |
| XRPUSDT | IDLE | 0.7 | 1.28 | 0.85 | -0.03 | 47213001.64 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.24 | 0.75 | -0.04 | 252030549.11 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.7 | 0.37 | -0.02 | 466817065.91 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 3.31 | 2.41 | -0.04 | 1044950.54 | 4.41 | skipped_fast |
| CCUSDT | IDLE | 1.54 | 3.71 | 3.54 | -0.1 | 404227.04 | 6.19 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.26 | 4.0 | -0.05 | 181393.0 | 24.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 7.08 | 6.18 | -0.13 | 110885.24 | 16.02 | skipped_fast |
| RWAINCUSDT | IDLE | 2.55 | 5.72 | 1.59 | 0.01 | 25140.51 | 35.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 2.77 | 2.41 | -0.06 | 189962.13 | 26.53 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.41 | 1.26 | -0.04 | 527057.75 | 9.53 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 2.11 | 1.77 | -0.06 | 68129.12 | 7.65 | skipped_fast |
| REDUSDT | IDLE | 1.13 | 2.04 | 1.49 | 0.01 | 63559.94 | 14.0 | skipped_fast |
| KITEUSDT | IDLE | 0.82 | 2.6 | 2.11 | -0.05 | 87211.2 | 11.99 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 3.35 | 3.08 | -0.05 | 95132.67 | 23.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 3.6 | 3.18 | -0.03 | 54123.08 | 41.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 2.15 | 1.74 | 0.03 | 20512.54 | 21.2 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.88 | 0.79 | -0.03 | 57087.6 | 8.0 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.61 | 0.22 | -0.01 | 33955.54 | 28.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
