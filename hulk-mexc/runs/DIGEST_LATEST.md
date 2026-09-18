# Hulk DIGEST — 2026-09-18T22:55:19Z

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
| XRPUSDT | IDLE | 1.31 | 2.92 | 1.31 | 0.08 | 64273252.82 | 2.87 | skipped_fast |
| ETHUSDT | IDLE | 1.16 | 2.33 | 1.0 | 0.07 | 630037321.73 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 1.0 | 0.34 | 0.06 | 754671413.12 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.24 | 4.34 | 2.01 | 0.1 | 890475.31 | 9.14 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 12.26 | 10.76 | 0.02 | 176183.57 | 13.43 | skipped_fast |
| PYTHUSDT | IDLE | 1.31 | 2.89 | 1.46 | 0.08 | 759635.71 | 3.33 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 2.98 | 0.13 | 0.11 | 665217.9 | 8.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 8.61 | 4.18 | 0.2 | 190384.39 | 11.17 | skipped_fast |
| HBARUSDT | IDLE | 1.3 | 2.46 | 0.95 | 0.06 | 617093.18 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.33 | 1.49 | 0.04 | 224531.14 | 12.13 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 2.7 | 0.57 | 0.04 | 7342.35 | 5.75 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 2.16 | 0.32 | 0.05 | 77447.97 | 14.36 | skipped_fast |
| TELUSDT | IDLE | 2.33 | 11.9 | 4.17 | 0.15 | 119748.19 | 104.39 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 2.19 | 1.12 | 0.09 | 88092.32 | 11.0 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 1.7 | 0.57 | 0.12 | 63338.35 | 16.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.62 | 6.66 | 1.51 | 0.15 | 2477.57 | 21.82 | skipped_fast |
| RIZEUSDT | IDLE | 0.15 | 2.53 | 0.85 | -0.1 | 57830.21 | 70.85 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.28 | 1.06 | 0.04 | 72836.63 | 4.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.47 | 0.14 | 0.07 | 43128.71 | 3.93 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.41 | 1.17 | 0.01 | 58445.45 | 44.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
