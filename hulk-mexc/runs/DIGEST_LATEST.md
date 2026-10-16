# Hulk DIGEST — 2026-10-16T20:04:47Z

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
| PYTHUSDT | IDLE | 1.93 | 6.8 | 5.49 | -0.12 | 2039585.13 | 3.57 | skipped_fast |
| WUSDT | IDLE | 2.45 | 6.06 | 4.86 | -0.04 | 1739068.91 | 9.21 | skipped_fast |
| XRPUSDT | IDLE | 1.7 | 3.07 | 2.25 | -0.03 | 28484907.24 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 1.55 | 2.78 | 2.11 | -0.02 | 212518618.25 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.76 | 1.43 | 0.55 | -0.01 | 359879569.59 | 0.09 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 3.33 | 2.6 | -0.04 | 784927.71 | 1.99 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 5.45 | 5.0 | -0.0 | 189574.68 | 34.03 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 6.86 | 6.42 | -0.1 | 97061.43 | 16.9 | skipped_fast |
| ZBCNUSDT | IDLE | 2.37 | 4.27 | 3.19 | -0.04 | 202319.92 | 24.31 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.49 | 1.61 | -0.04 | 385174.6 | 6.8 | skipped_fast |
| RWAINCUSDT | IDLE | 1.98 | 9.03 | 8.28 | -0.13 | 25994.3 | 5.79 | skipped_fast |
| HBARUSDT | IDLE | 2.36 | 4.2 | 3.51 | -0.03 | 306532.67 | 6.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 5.31 | 4.71 | -0.03 | 152393.47 | 11.07 | skipped_fast |
| BIOUSDT | IDLE | 1.94 | 3.52 | 2.38 | -0.03 | 61985.03 | 8.0 | skipped_fast |
| KITEUSDT | IDLE | 1.44 | 2.52 | 2.37 | -0.04 | 56273.78 | 19.25 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 2.25 | 0.26 | -0.0 | 46281.58 | 24.39 | skipped_fast |
| RWAUSDT | IDLE | 2.08 | 3.9 | 1.8 | -0.01 | 53117.98 | 15.91 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 3.33 | 3.0 | -0.02 | 94372.92 | 40.1 | skipped_fast |
| FLUIDUSDT | IDLE | 1.77 | 3.4 | 0.93 | -0.01 | 6545.69 | 19.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.88 | 0.78 | -0.01 | 34721.86 | 61.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
