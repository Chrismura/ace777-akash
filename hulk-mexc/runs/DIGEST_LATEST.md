# Hulk DIGEST — 2026-08-22T10:22:31Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.6 | -0.0 | 51614949.79 | 12.38 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 23.87 | 13.97 | 0.05 | 216407410.23 | 6.16 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 15.8 | 11.75 | 0.0 | 1250309.17 | 5.22 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 22.93 | 12.96 | -0.12 | 664841.45 | 17.12 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 16.84 | 10.68 | -0.0 | 595447.14 | 8.59 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.33 | -0.06 | 236631.55 | 16.43 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.45 | 0.11 | 816354.03 | 9.58 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 11.77 | 0.03 | 155580.12 | 28.09 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.48 | 8.8 | 7.93 | -0.03 | 428190.49 | 19.49 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 9.28 | 5.74 | 0.03 | 73062.75 | 12.98 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 9.75 | 7.27 | -0.01 | 189334.64 | 1.58 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 8.01 | 7.27 | -0.04 | 168599.57 | 26.69 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5825.49 | 17.22 | skipped_fast |
| EDELUSDT | IDLE | 2.67 | 4.76 | 3.89 | -0.03 | 78525.4 | 67.34 | skipped_fast |
| QAITUSDT | IDLE | 1.6 | 2.91 | 1.98 | -0.01 | 3205.44 | 63.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11368.82 | 38.01 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.23 | -0.0 | 49217.8 | 46.66 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.31 | 0.02 | 57503.1 | 16.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
