# Hulk DIGEST — 2026-08-22T08:08:23Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.21 | 0.0 | 25690890.78 | 5.92 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 23.87 | 9.38 | 0.16 | 224929942.08 | 5.2 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 9.82 | 0.04 | 1355564.23 | 6.39 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.0 | -0.09 | 683496.46 | 6.69 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.26 | 0.04 | 609326.84 | 19.73 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.47 | -0.05 | 247229.45 | 12.76 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.39 | 0.06 | 156178.42 | 19.28 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 2.38 | 0.2 | 815595.27 | 9.82 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 8.47 | 6.66 | 0.03 | 537130.8 | 19.62 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.6 | 0.03 | 194155.91 | 9.27 | skipped_fast |
| KITEUSDT | IDLE | 3.83 | 9.68 | 4.4 | 0.06 | 72901.58 | 10.03 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.15 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 4.52 | 3.68 | -0.04 | 87024.88 | 122.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 112.75 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 4.7 | 4.15 | -0.01 | 173951.75 | 51.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.86 | 0.0 | 52287.58 | 44.42 | skipped_fast |
| RWAUSDT | IDLE | 1.71 | 3.29 | 0.88 | 0.05 | 58319.86 | 16.09 | skipped_fast |
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
