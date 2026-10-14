# Hulk DIGEST — 2026-10-14T14:18:42Z

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
| PYTHUSDT | IDLE | 2.58 | 6.19 | 2.87 | 0.0 | 2098907.59 | 2.41 | skipped_fast |
| WUSDT | IDLE | 1.85 | 7.99 | 6.68 | -0.17 | 3382553.77 | 7.84 | skipped_fast |
| ETHUSDT | IDLE | 2.02 | 3.56 | 3.26 | -0.03 | 161023845.0 | 0.82 | skipped_fast |
| XRPUSDT | IDLE | 2.01 | 3.56 | 3.06 | -0.03 | 36356471.98 | 2.24 | skipped_fast |
| BTCUSDT | IDLE | 1.31 | 2.3 | 2.15 | -0.02 | 379785566.49 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.91 | 4.44 | 3.9 | -0.02 | 1557466.28 | 4.91 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 18.92 | 15.63 | -0.01 | 50446.45 | 31.02 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 4.89 | 4.46 | -0.09 | 478784.89 | 7.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.74 | 4.8 | 4.52 | -0.03 | 190131.85 | 15.27 | skipped_fast |
| CHIPUSDT | IDLE | 2.83 | 5.51 | 4.16 | -0.07 | 77329.47 | 16.41 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 3.65 | 3.09 | -0.03 | 144704.88 | 17.85 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 4.04 | 3.37 | -0.04 | 69054.13 | 7.51 | skipped_fast |
| KITEUSDT | IDLE | 1.98 | 5.55 | 4.12 | 0.03 | 83577.64 | 10.62 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 3.84 | 3.5 | -0.05 | 302678.56 | 5.95 | skipped_fast |
| REDUSDT | IDLE | 1.93 | 3.43 | 2.87 | -0.01 | 59676.12 | 15.11 | skipped_fast |
| RWAINCUSDT | IDLE | 1.79 | 5.62 | 4.2 | -0.08 | 32649.89 | 10.68 | skipped_fast |
| FLUIDUSDT | IDLE | 2.03 | 5.74 | 5.43 | 0.03 | 23124.04 | 16.71 | skipped_fast |
| TELUSDT | IDLE | 1.59 | 2.79 | 2.6 | 0.0 | 105308.37 | 22.74 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.74 | 1.55 | -0.02 | 56165.41 | 15.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.56 | 1.0 | 0.78 | -0.01 | 39874.17 | 40.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
