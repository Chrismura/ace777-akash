# Hulk DIGEST — 2026-08-22T05:38:56Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.22 | 0.08 | 16837044.58 | 3.95 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 10.88 | 0.16 | 202909609.18 | 3.96 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.61 | 0.05 | 1360581.94 | 10.19 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.0 | -0.09 | 707465.13 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.59 | 0.06 | 598949.16 | 14.44 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.94 | 0.11 | 164293.68 | 13.16 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.38 | -0.04 | 219772.89 | 16.52 | skipped_fast |
| CCUSDT | IDLE | 2.2 | 11.56 | 3.34 | 0.18 | 761157.23 | 7.54 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 8.47 | 5.55 | 0.06 | 547231.31 | 15.9 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 13.91 | 9.1 | 0.04 | 196968.74 | 12.39 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 9.68 | 5.59 | 0.08 | 73328.5 | 12.04 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 4.52 | 1.19 | -0.02 | 88467.01 | 32.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.3 | 0.06 | 58933.37 | 28.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 70.06 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5410.56 | 45.86 | skipped_fast |
| TELUSDT | IDLE | 2.1 | 5.52 | 3.26 | 0.07 | 195522.18 | 35.72 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.91 | 0.05 | 57991.65 | 8.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
