# Hulk DIGEST — 2026-09-10T00:14:38Z

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
| XRPUSDT | IDLE | 1.62 | 2.98 | 1.8 | -0.02 | 42892052.71 | 2.15 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 9.06 | 6.65 | -0.03 | 1035206.14 | 1.92 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.68 | 0.65 | -0.01 | 380778495.08 | 0.73 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.03 | 0.38 | -0.01 | 535709746.23 | 0.1 | skipped_fast |
| WUSDT | IDLE | 4.33 | 8.4 | 4.56 | -0.02 | 211173.11 | 13.95 | skipped_fast |
| EDELUSDT | IDLE | 4.12 | 12.28 | 2.4 | 0.05 | 204969.57 | 36.33 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.75 | 0.89 | -0.04 | 634228.63 | 7.65 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 14.41 | 8.87 | -0.06 | 124233.89 | 19.65 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 8.28 | 4.69 | -0.08 | 102719.25 | 3.88 | skipped_fast |
| REDUSDT | IDLE | 2.73 | 5.33 | 0.92 | 0.01 | 62555.73 | 10.78 | skipped_fast |
| HBARUSDT | IDLE | 1.79 | 3.26 | 2.18 | -0.03 | 488934.44 | 1.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.16 | 3.88 | 2.96 | -0.02 | 6299.12 | 11.31 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 3.68 | 1.08 | -0.01 | 57767.27 | 9.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.1 | 2.1 | 0.72 | 0.02 | 182949.14 | 23.5 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 9.95 | 2.32 | 0.04 | 74412.02 | 108.8 | skipped_fast |
| RWAUSDT | IDLE | 1.7 | 2.99 | 2.69 | -0.03 | 55390.15 | 22.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 2.51 | 2.44 | -0.08 | 951.16 | 21.2 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.16 | 1.11 | -0.01 | 44863.04 | 8.96 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.84 | 1.43 | 0.01 | 97613.86 | 50.1 | skipped_fast |
| MNSRYUSDT | IDLE | 1.2 | 2.12 | 1.83 | -0.01 | 25807.89 | 38.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
