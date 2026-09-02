# Hulk DIGEST — 2026-09-02T09:37:17Z

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
| ETHUSDT | IDLE | 1.43 | 2.51 | 2.32 | -0.03 | 380424780.03 | 0.3 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 2.29 | 2.2 | -0.03 | 38052917.68 | 2.27 | skipped_fast |
| BTCUSDT | IDLE | 0.86 | 1.51 | 1.45 | -0.02 | 498685458.84 | 0.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 8.6 | 1.61 | 0.17 | 976764.98 | 13.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.36 | 4.34 | 3.29 | 0.1 | 826407.23 | 1.84 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.95 | 16.28 | 7.38 | 0.02 | 173346.12 | 49.67 | skipped_fast |
| WUSDT | IDLE | 2.13 | 3.84 | 2.86 | 0.0 | 398374.71 | 14.65 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 3.28 | 2.27 | -0.06 | 338374.65 | 6.21 | skipped_fast |
| KITEUSDT | IDLE | 2.36 | 9.81 | 2.06 | 0.15 | 77917.53 | 9.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.74 | 8.35 | 2.22 | 0.09 | 10579.17 | 80.62 | skipped_fast |
| RIZEUSDT | IDLE | 2.07 | 7.95 | 5.77 | -0.12 | 40539.25 | 81.52 | skipped_fast |
| ZBCNUSDT | IDLE | 1.05 | 2.07 | 1.99 | -0.02 | 226210.95 | 12.14 | skipped_fast |
| QNTUSDT | IDLE | 2.81 | 6.12 | 4.32 | 0.05 | 69554.87 | 6.23 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.1 | 1.67 | -0.03 | 75091.1 | 3.95 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.94 | 1.21 | 0.01 | 154732.45 | 19.8 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.54 | 1.17 | -0.01 | 233493.63 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 1.41 | 2.52 | 2.05 | -0.02 | 86482.85 | 5.99 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.52 | 1.49 | -0.04 | 328.21 | 22.02 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.62 | 0.38 | 0.0 | 50725.61 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.34 | 0.66 | 0.15 | -0.02 | 36684.98 | 2.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
