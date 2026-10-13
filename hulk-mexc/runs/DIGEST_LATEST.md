# Hulk DIGEST — 2026-10-13T20:16:07Z

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
| WUSDT | IDLE | 2.04 | 13.52 | 6.09 | -0.19 | 4903386.82 | 14.07 | skipped_fast |
| PYTHUSDT | IDLE | 2.24 | 7.01 | 5.27 | -0.04 | 2145746.32 | 11.45 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.81 | 10.52 | 0.99 | -0.04 | 1655254.52 | 1.82 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.1 | 0.52 | -0.01 | 235941573.73 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.6 | 1.15 | 0.36 | 0.0 | 37156721.39 | 1.46 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.9 | 0.54 | 0.0 | 393011344.88 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.33 | 2.88 | 0.04 | 630864.44 | 7.11 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 10.22 | 5.01 | -0.07 | 66038.1 | 59.03 | skipped_fast |
| RWAINCUSDT | IDLE | 2.54 | 4.82 | 1.76 | 0.02 | 31451.18 | 19.31 | skipped_fast |
| ZBCNUSDT | IDLE | 1.6 | 2.89 | 2.06 | -0.01 | 220568.33 | 7.45 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 4.28 | 0.33 | -0.01 | 136360.44 | 7.09 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.81 | 0.46 | 0.02 | 256698.52 | 11.6 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.92 | 0.25 | -0.02 | 75793.75 | 7.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 2.65 | 0.45 | -0.02 | 106155.4 | 13.84 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 3.74 | 2.66 | 0.01 | 116120.45 | 28.47 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.77 | 0.03 | -0.02 | 327420.91 | 5.69 | skipped_fast |
| KITEUSDT | IDLE | 0.74 | 1.63 | 0.02 | -0.0 | 60212.32 | 11.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 2.02 | 0.6 | 0.02 | 25885.88 | 21.4 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.62 | 0.54 | -0.0 | 52492.79 | 7.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.49 | 0.17 | -0.02 | 38702.25 | 11.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
