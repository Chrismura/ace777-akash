# Hulk DIGEST — 2026-10-14T19:23:35Z

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
| PYTHUSDT | IDLE | 2.53 | 6.23 | 0.78 | 0.04 | 2119659.83 | 1.21 | skipped_fast |
| WUSDT | IDLE | 1.05 | 4.46 | 2.91 | -0.08 | 2741250.04 | 10.55 | skipped_fast |
| XRPUSDT | IDLE | 1.29 | 2.34 | 1.66 | -0.03 | 44574335.01 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.91 | 1.64 | 1.22 | -0.02 | 430327389.24 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.64 | 0.91 | -0.03 | 198238562.96 | 0.04 | skipped_fast |
| QNTUSDT | IDLE | 1.97 | 4.17 | 2.65 | -0.06 | 1172635.49 | 6.83 | skipped_fast |
| ZBCNUSDT | IDLE | 2.93 | 5.26 | 3.97 | -0.04 | 183469.88 | 16.45 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 3.38 | 2.56 | -0.09 | 435912.88 | 8.58 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 13.1 | 7.09 | 0.07 | 18313.38 | 12.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.15 | 6.35 | 4.34 | -0.07 | 106781.92 | 15.06 | skipped_fast |
| REDUSDT | IDLE | 2.55 | 4.95 | 1.03 | 0.01 | 61899.81 | 16.0 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 3.61 | 2.43 | -0.03 | 167096.9 | 32.97 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 5.41 | 4.24 | -0.0 | 86025.21 | 8.64 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.18 | 1.68 | -0.04 | 526286.27 | 5.98 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 6.57 | 1.94 | -0.07 | 29894.97 | 31.19 | skipped_fast |
| TELUSDT | IDLE | 2.91 | 5.61 | 1.42 | 0.03 | 102733.91 | 33.31 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.71 | 2.04 | -0.05 | 64840.49 | 7.59 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 4.08 | 2.68 | -0.01 | 49222.83 | 61.51 | skipped_fast |
| RWAUSDT | IDLE | 0.86 | 1.51 | 1.41 | -0.03 | 56283.4 | 7.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.73 | 0.41 | -0.01 | 37015.06 | 29.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
