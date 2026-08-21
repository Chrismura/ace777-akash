# Hulk DIGEST — 2026-08-21T20:08:14Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 3.09 | 0.08 | 5469835.07 | 4.23 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.58 | 0.11 | 129012547.64 | 2.92 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.93 | 0.17 | 154225.31 | 10.59 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.53 | 10.86 | 7.48 | 0.1 | 477838.95 | 19.89 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.71 | 0.07 | 633519.28 | 6.53 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.23 | 2.65 | 0.05 | 794154.92 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.64 | 0.08 | 513670.92 | 6.19 | skipped_fast |
| WUSDT | IDLE | 2.15 | 3.92 | 2.54 | 0.05 | 366430.73 | 13.85 | skipped_fast |
| BIOUSDT | IDLE | 2.59 | 5.33 | 3.62 | 0.0 | 189860.3 | 3.18 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.41 | 4.23 | -0.05 | 80160.17 | 11.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.63 | 0.02 | 56217.9 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 2.96 | 0.1 | 61174.76 | 11.22 | skipped_fast |
| RWAINCUSDT | IDLE | 2.31 | 4.3 | 2.17 | 0.04 | 11069.14 | 112.93 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2857.0 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.59 | 0.01 | 183400.46 | 43.41 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 59884.26 | 6.25 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.03 | 54365.52 | 16.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
