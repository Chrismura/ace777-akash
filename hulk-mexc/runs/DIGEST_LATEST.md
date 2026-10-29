# Hulk DIGEST — 2026-10-29T02:38:37Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 2.01 | 3.53 | 3.31 | -0.03 | 23381999.9 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 1.92 | 3.36 | 3.14 | -0.03 | 225189677.92 | 1.7 | skipped_fast |
| BTCUSDT | IDLE | 1.18 | 2.06 | 1.97 | -0.01 | 327627417.54 | 0.01 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 6.5 | 6.0 | -0.04 | 454158.46 | 7.12 | skipped_fast |
| WUSDT | IDLE | 2.97 | 5.32 | 4.19 | -0.04 | 454015.45 | 16.28 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 5.7 | 5.24 | -0.03 | 445032.56 | 9.37 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.67 | 6.45 | 5.95 | -0.04 | 449904.29 | 6.82 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 6.86 | 6.29 | -0.05 | 90844.03 | 9.19 | skipped_fast |
| HBARUSDT | IDLE | 2.42 | 4.27 | 3.75 | -0.04 | 591802.81 | 8.18 | skipped_fast |
| KITEUSDT | IDLE | 2.63 | 4.61 | 4.29 | -0.05 | 60493.82 | 9.82 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 3.68 | 3.55 | -0.05 | 176330.63 | 25.58 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 6.69 | 6.27 | -0.05 | 53384.95 | 28.06 | skipped_fast |
| IOTAUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 6.0 | 5.64 | -0.06 | 94719.57 | 2.5 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 2.56 | 2.46 | -0.01 | 274057.51 | 20.9 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 5.14 | 4.69 | -0.13 | 233828.32 | 12.57 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 5.55 | 5.09 | -0.05 | 6069.28 | 19.76 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 2.26 | 1.72 | -0.03 | 63150.1 | 16.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.4 | 5.51 | 2.68 | -0.05 | 32914.8 | 49.28 | skipped_fast |
| LAUSDT | IDLE | 2.34 | 4.11 | 3.85 | -0.05 | 54920.16 | 24.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 2.13 | 1.34 | -0.03 | 39293.84 | 64.29 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.13 | 0.87 | 0.0 | 54358.79 | 8.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.22 | 1.12 | -0.0 | 36823.49 | 67.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
