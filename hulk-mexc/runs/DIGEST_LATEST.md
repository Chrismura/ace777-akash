# Hulk DIGEST — 2026-08-22T12:04:10Z

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
| PYTHUSDT | IDLE | 1.73 | 7.83 | 5.01 | 0.01 | 51609106.79 | 2.04 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 14.26 | 7.64 | 0.11 | 215571396.32 | 3.33 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 4.63 | 2.45 | 0.03 | 1254565.35 | 5.16 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 8.38 | 4.94 | 0.13 | 774596.56 | 9.4 | skipped_fast |
| WUSDT | IDLE | 1.54 | 6.27 | 3.38 | 0.02 | 581000.59 | 12.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.27 | 5.77 | 5.0 | -0.04 | 380932.43 | 43.65 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 1.02 | -0.09 | 618974.72 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.29 | 0.04 | 82574.58 | 13.22 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.2 | -0.04 | 78160.85 | 22.78 | skipped_fast |
| BIOUSDT | IDLE | 0.79 | 5.65 | 1.76 | -0.02 | 240543.2 | 6.41 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2386.65 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 2.19 | 5.61 | 4.39 | -0.03 | 165102.44 | 21.38 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.65 | 0.04 | 154078.18 | 18.57 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10327.23 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.59 | 0.01 | 188376.53 | 6.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 1.91 | 0.95 | -0.04 | 48184.29 | 46.44 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57838.54 | 8.15 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 22.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
