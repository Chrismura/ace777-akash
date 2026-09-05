# Hulk DIGEST — 2026-09-05T14:45:15Z

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
| XRPUSDT | IDLE | 0.66 | 1.28 | 0.25 | 0.02 | 24785063.99 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.48 | 0.22 | 0.01 | 193692025.78 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.26 | 0.03 | 0.01 | 382126215.32 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 6.25 | 0.34 | 0.11 | 455000.54 | 1.71 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 3.6 | 1.37 | 0.03 | 356768.93 | 1.83 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 6.21 | 5.15 | -0.04 | 63633.92 | 8.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 11.89 | 9.95 | 0.03 | 154683.12 | 75.17 | skipped_fast |
| REDUSDT | IDLE | 1.92 | 3.4 | 3.0 | 0.01 | 63400.37 | 12.03 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.73 | 0.25 | 0.02 | 300082.21 | 8.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 2.66 | 0.32 | -0.01 | 187371.34 | 19.33 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.86 | 0.61 | 0.04 | 82057.54 | 3.59 | skipped_fast |
| RWAINCUSDT | IDLE | 1.56 | 2.72 | 2.65 | -0.02 | 7377.09 | 21.81 | skipped_fast |
| WUSDT | IDLE | 0.55 | 1.03 | 0.48 | 0.07 | 162139.85 | 7.04 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 1.94 | 1.01 | 0.05 | 319396.22 | 1.24 | skipped_fast |
| EDELUSDT | IDLE | 0.13 | 2.29 | 1.59 | -0.02 | 191590.0 | 18.98 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 2.14 | 0.64 | -0.01 | 71733.95 | 23.39 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.02 | 52422.87 | 21.21 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.15 | 0.79 | -0.01 | 38799.13 | 3.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.3 | 0.04 | 0.0 | 38683.64 | 21.83 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 820.75 | 21.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
