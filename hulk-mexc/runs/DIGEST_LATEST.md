# Hulk DIGEST — 2026-08-22T10:37:12Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.22 | 0.01 | 51647999.27 | 2.06 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.39 | 0.08 | 217549432.9 | 1.34 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.29 | 0.01 | 1251022.26 | 6.49 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.77 | -0.1 | 661924.14 | 3.38 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.78 | 0.01 | 598542.12 | 13.81 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.04 | -0.06 | 239050.83 | 3.28 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.5 | 0.13 | 812256.43 | 8.64 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.37 | 0.03 | 154579.97 | 21.68 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 9.72 | 7.6 | -0.02 | 425778.55 | 31.69 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 9.28 | 5.07 | 0.03 | 73238.37 | 9.22 | skipped_fast |
| EDELUSDT | IDLE | 3.35 | 5.96 | 4.97 | -0.04 | 78918.91 | 45.35 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 9.12 | 8.16 | -0.05 | 168456.1 | 32.31 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 9.75 | 6.85 | -0.01 | 189449.05 | 12.55 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 21.63 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3241.83 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11275.22 | 43.43 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.48 | -0.0 | 49245.34 | 25.9 | skipped_fast |
| RWAUSDT | IDLE | 1.8 | 3.29 | 2.07 | 0.02 | 57451.19 | 16.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
