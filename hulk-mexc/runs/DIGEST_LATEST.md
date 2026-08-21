# Hulk DIGEST — 2026-08-21T19:51:02Z

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
| PYTHUSDT | IDLE | 1.37 | 4.99 | 4.14 | 0.07 | 5429044.35 | 6.39 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 4.21 | 3.53 | 0.11 | 129080503.77 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.76 | 0.17 | 152967.42 | 19.74 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 11.37 | 9.47 | 0.06 | 482680.75 | 19.21 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 5.44 | 2.03 | 0.07 | 631388.23 | 5.62 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 3.08 | 2.96 | 0.05 | 791524.56 | 6.57 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.09 | 0.09 | 514494.5 | 3.11 | skipped_fast |
| WUSDT | IDLE | 2.16 | 3.92 | 2.92 | 0.05 | 360491.82 | 12.85 | skipped_fast |
| BIOUSDT | IDLE | 2.64 | 5.33 | 4.48 | -0.0 | 190331.9 | 3.22 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.05 | 79601.41 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 11.27 | 2.94 | 0.02 | 56475.55 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.41 | 0.09 | 61122.12 | 11.26 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 80.49 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 4.46 | 2.21 | 0.02 | 183355.45 | 32.31 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2917.53 | 63.29 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.01 | 2.12 | 0.04 | 59876.9 | 6.28 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.16 | 1.07 | 0.04 | 54324.21 | 24.91 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4276.39 | 21.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
