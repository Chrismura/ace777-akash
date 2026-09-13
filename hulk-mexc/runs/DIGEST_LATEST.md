# Hulk DIGEST — 2026-09-13T18:41:03Z

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
| ETHUSDT | IDLE | 1.04 | 2.05 | 0.16 | -0.01 | 253439100.84 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.96 | 1.92 | 0.04 | -0.01 | 14511331.73 | 2.95 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.07 | 0.04 | 0.0 | 290757767.03 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.47 | 35.81 | 21.35 | -0.1 | 74741.52 | 12.32 | skipped_fast |
| PYTHUSDT | IDLE | 2.72 | 5.33 | 0.7 | 0.04 | 458596.54 | 1.75 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 9.26 | 0.98 | 0.11 | 201674.77 | 15.16 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.69 | 0.11 | 0.02 | 264375.99 | 10.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.16 | 6.14 | 5.11 | -0.11 | 85035.47 | 16.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 2.96 | 0.54 | -0.0 | 200551.64 | 23.98 | skipped_fast |
| CCUSDT | IDLE | 0.61 | 1.21 | 0.02 | -0.02 | 296064.72 | 8.34 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.79 | 1.95 | -0.0 | 61223.57 | 17.56 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.22 | 1.79 | 0.01 | 63497.94 | 12.13 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.3 | 0.39 | 0.0 | 68564.86 | 7.8 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.42 | 1.23 | -0.02 | 6540.87 | 5.66 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 2.14 | 0.13 | 0.03 | 204355.14 | 1.31 | skipped_fast |
| QNTUSDT | IDLE | 1.4 | 2.77 | 0.23 | 0.02 | 35863.66 | 4.59 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.27 | 0.0 | 0.0 | 55094.58 | 14.81 | skipped_fast |
| TELUSDT | IDLE | 0.75 | 1.46 | 0.31 | -0.04 | 80217.36 | 43.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.63 | 1.11 | 1.05 | -0.01 | 1479.56 | 21.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.25 | 0.08 | -0.0 | 32128.42 | 13.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
