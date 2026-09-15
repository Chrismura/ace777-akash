# Hulk DIGEST — 2026-09-15T09:36:26Z

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
| XRPUSDT | IDLE | 1.26 | 2.36 | 1.12 | 0.01 | 74775186.91 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.41 | 0.95 | -0.02 | 456545935.83 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.35 | 0.98 | -0.01 | 546109080.01 | 0.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 22.32 | 14.31 | 0.01 | 145909.18 | 16.58 | skipped_fast |
| EDELUSDT | IDLE | 1.24 | 16.9 | 8.82 | 0.32 | 449587.25 | 76.59 | skipped_fast |
| PYTHUSDT | IDLE | 2.22 | 3.93 | 3.39 | -0.03 | 294627.5 | 1.84 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 21.94 | 1.78 | -0.04 | 51382.4 | 7.71 | skipped_fast |
| CCUSDT | IDLE | 1.09 | 2.01 | 1.19 | 0.0 | 365987.56 | 1.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 3.62 | 0.07 | 0.04 | 221371.96 | 41.74 | skipped_fast |
| WUSDT | IDLE | 1.75 | 3.12 | 2.48 | -0.04 | 161494.02 | 22.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.63 | 2.85 | 2.77 | -0.02 | 7380.28 | 5.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 2.7 | 0.69 | 0.01 | 66779.84 | 21.68 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.03 | 1.56 | -0.01 | 91897.09 | 7.93 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 2.13 | 0.47 | 0.01 | 63452.12 | 10.29 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.76 | 0.21 | 0.02 | 365180.03 | 1.29 | skipped_fast |
| FLUIDUSDT | IDLE | 2.23 | 3.9 | 3.75 | -0.03 | 2076.5 | 21.51 | skipped_fast |
| QNTUSDT | IDLE | 1.77 | 3.12 | 2.74 | -0.01 | 44267.26 | 3.16 | skipped_fast |
| TELUSDT | IDLE | 1.61 | 3.63 | 3.44 | -0.01 | 97799.82 | 25.49 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.37 | -0.01 | 53928.69 | 14.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.9 | 0.57 | 0.01 | 33599.04 | 29.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
