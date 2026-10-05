# Hulk DIGEST — 2026-10-05T10:35:06Z

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
| QNTUSDT | IDLE | 1.83 | 3.89 | 0.91 | -0.01 | 3125209.02 | 7.04 | skipped_fast |
| XRPUSDT | IDLE | 0.96 | 1.83 | 0.6 | 0.01 | 30000467.17 | 1.98 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.44 | 0.61 | 0.0 | 235200265.26 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.25 | 0.43 | 0.01 | 546037448.83 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.86 | 5.57 | 0.95 | 0.03 | 501182.55 | 2.49 | skipped_fast |
| WUSDT | IDLE | 1.3 | 2.48 | 0.82 | 0.01 | 552787.78 | 15.06 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.4 | 3.0 | 0.04 | 425953.85 | 20.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 3.86 | 3.14 | 0.02 | 218453.07 | 13.79 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 4.86 | 1.32 | 0.02 | 84396.23 | 9.6 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.42 | 2.17 | 0.02 | 303397.28 | 7.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.95 | 1.87 | 0.11 | 141664.75 | 18.11 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.62 | 1.49 | 0.01 | 520852.18 | 5.83 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 1.66 | 1.0 | -0.02 | 87485.88 | 13.95 | skipped_fast |
| RWAINCUSDT | IDLE | 1.71 | 4.08 | 3.2 | -0.05 | 4133.15 | 99.01 | skipped_fast |
| RIZEUSDT | IDLE | 0.89 | 7.24 | 5.47 | 0.23 | 39890.63 | 82.66 | skipped_fast |
| KITEUSDT | IDLE | 0.65 | 1.17 | 0.89 | -0.05 | 73755.58 | 7.66 | skipped_fast |
| TELUSDT | IDLE | 1.83 | 3.29 | 2.43 | 0.01 | 139766.21 | 36.22 | skipped_fast |
| FLUIDUSDT | IDLE | 2.37 | 5.0 | 0.0 | 0.08 | 6257.17 | 45.27 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.59 | 0.29 | -0.0 | 52187.11 | 21.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.37 | 0.08 | 0.0 | 44131.76 | 24.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
