# Hulk DIGEST — 2026-09-22T01:08:07Z

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
| XRPUSDT | IDLE | 1.75 | 4.71 | 3.63 | 0.06 | 111628415.79 | 2.64 | skipped_fast |
| ETHUSDT | IDLE | 1.41 | 2.52 | 2.03 | 0.02 | 712853909.42 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.16 | 2.05 | 1.77 | 0.05 | 1086058811.76 | 0.14 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 18.24 | 13.65 | 0.04 | 239038.56 | 3.32 | skipped_fast |
| PYTHUSDT | IDLE | 2.02 | 5.01 | 1.6 | 0.02 | 758774.24 | 10.94 | skipped_fast |
| CCUSDT | IDLE | 2.17 | 4.43 | 1.88 | 0.06 | 668111.44 | 9.36 | skipped_fast |
| HBARUSDT | IDLE | 1.16 | 2.86 | 1.28 | 0.08 | 1101787.3 | 1.08 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.69 | 19.83 | 14.57 | -0.25 | 53858.29 | 55.63 | skipped_fast |
| WUSDT | IDLE | 1.1 | 2.45 | 1.43 | 0.02 | 550832.16 | 8.47 | skipped_fast |
| RWAINCUSDT | IDLE | 2.78 | 7.23 | 1.13 | 0.09 | 19800.39 | 10.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.53 | 3.61 | 3.42 | 0.02 | 265160.76 | 23.85 | skipped_fast |
| REDUSDT | IDLE | 2.14 | 4.12 | 1.04 | 0.02 | 105211.08 | 14.26 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.17 | 1.61 | 0.03 | 81303.88 | 10.88 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 4.98 | 2.07 | 0.07 | 153759.11 | 10.75 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 2.73 | 1.16 | 0.04 | 100190.26 | 20.68 | skipped_fast |
| QNTUSDT | IDLE | 1.57 | 2.77 | 2.5 | 0.02 | 111557.9 | 9.06 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 3.49 | 2.9 | 0.07 | 116240.13 | 42.7 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.09 | 1.01 | 0.0 | 57883.72 | 21.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.79 | 1.5 | 0.51 | 0.03 | 41758.86 | 39.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.09 | 0.74 | 0.07 | 12038.86 | 42.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
