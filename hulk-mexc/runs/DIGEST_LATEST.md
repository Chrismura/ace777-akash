# Hulk DIGEST — 2026-08-22T08:10:10Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.81 | 0.01 | 25916590.54 | 13.76 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 23.87 | 9.07 | 0.16 | 225002044.59 | 1.94 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.51 | 0.04 | 1357216.84 | 7.63 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.62 | -0.09 | 683234.09 | 3.33 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.24 | 0.04 | 609317.31 | 14.49 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.24 | -0.04 | 247433.72 | 12.7 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.44 | 0.06 | 154761.73 | 11.39 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.01 | 0.2 | 816313.48 | 11.43 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 8.47 | 6.2 | 0.03 | 537123.17 | 25.04 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.46 | 0.03 | 194145.96 | 10.78 | skipped_fast |
| KITEUSDT | IDLE | 3.82 | 9.68 | 4.3 | 0.06 | 72931.6 | 10.0 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.85 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 4.52 | 2.49 | -0.02 | 86999.09 | 100.17 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 4.7 | 3.8 | -0.0 | 173768.93 | 51.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.81 | 0.0 | 52287.63 | 44.42 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 0.96 | 0.05 | 58331.25 | 16.09 | skipped_fast |
| QAITUSDT | IDLE | 0.99 | 1.92 | 0.35 | 0.01 | 3170.95 | 67.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
