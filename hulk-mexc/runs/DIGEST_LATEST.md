# Hulk DIGEST — 2026-08-22T10:12:12Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.31 | 0.01 | 51590893.01 | 6.18 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 23.87 | 13.54 | 0.05 | 214881973.38 | 8.18 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.45 | 0.01 | 1247348.4 | 7.8 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 22.93 | 12.78 | -0.11 | 663718.76 | 3.42 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 16.84 | 10.07 | 0.01 | 592265.67 | 14.92 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 11.29 | -0.04 | 236926.23 | 6.52 | skipped_fast |
| CCUSDT | IDLE | 2.27 | 11.25 | 9.2 | 0.11 | 813652.57 | 13.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 10.99 | 0.04 | 155748.83 | 28.76 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 8.06 | 7.46 | -0.02 | 429560.7 | 4.08 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 9.28 | 5.61 | 0.03 | 73160.81 | 9.29 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 9.75 | 6.79 | -0.0 | 189444.41 | 7.85 | skipped_fast |
| EDELUSDT | IDLE | 2.7 | 4.76 | 4.32 | -0.04 | 79163.8 | 22.57 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 7.9 | 6.68 | -0.03 | 170043.97 | 47.91 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 20.07 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.0 | 3167.54 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 3.18 | 1.91 | -0.01 | 49274.55 | 45.14 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | -0.0 | 11436.39 | 81.15 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.29 | 1.75 | 0.02 | 57460.44 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
