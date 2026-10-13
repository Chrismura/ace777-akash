# Hulk DIGEST — 2026-10-13T11:13:39Z

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
| PYTHUSDT | IDLE | 1.56 | 5.48 | 4.85 | -0.07 | 3141937.08 | 10.88 | skipped_fast |
| WUSDT | IDLE | 0.71 | 7.23 | 5.08 | -0.28 | 7079377.11 | 10.95 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 2.37 | 2.06 | -0.03 | 37647199.9 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 1.05 | 1.84 | 1.72 | -0.02 | 240101725.36 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.46 | 1.08 | -0.0 | 387761015.8 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 15.02 | 11.02 | -0.13 | 998871.06 | 9.25 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 3.75 | 2.31 | -0.02 | 443771.78 | 9.82 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 5.45 | 5.1 | -0.07 | 225254.4 | 7.27 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 3.08 | 2.98 | -0.07 | 523295.42 | 4.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 5.14 | 4.72 | -0.09 | 139444.7 | 12.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 2.4 | 1.98 | -0.04 | 216782.07 | 21.7 | skipped_fast |
| EDELUSDT | IDLE | 0.89 | 2.94 | 2.18 | -0.11 | 273347.46 | 15.24 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 4.12 | 3.95 | -0.07 | 72880.91 | 3.67 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 3.43 | 2.89 | -0.04 | 66405.52 | 10.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.57 | 2.78 | 2.42 | -0.04 | 34713.5 | 4.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 7.45 | 4.97 | -0.1 | 63916.13 | 87.9 | skipped_fast |
| TELUSDT | IDLE | 1.74 | 3.07 | 2.7 | -0.03 | 102169.05 | 46.11 | skipped_fast |
| FLUIDUSDT | IDLE | 1.56 | 3.08 | 2.99 | 0.03 | 14710.62 | 21.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.45 | 0.79 | 0.7 | -0.02 | 38762.39 | 40.21 | skipped_fast |
| RWAUSDT | IDLE | 0.16 | 0.31 | 0.08 | 0.0 | 53225.67 | 15.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
