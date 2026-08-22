# Hulk DIGEST — 2026-08-22T08:26:41Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.65 | 0.03 | 27896701.95 | 9.92 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 23.87 | 10.03 | 0.14 | 222802404.06 | 6.55 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 9.97 | 0.03 | 1343686.63 | 8.95 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.29 | -0.1 | 684780.97 | 6.71 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.24 | 0.04 | 599642.13 | 14.54 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.18 | -0.04 | 250567.1 | 6.37 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.42 | 0.08 | 155615.42 | 14.05 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.13 | 0.19 | 823213.33 | 8.16 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.1 | 0.02 | 537234.5 | 2.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.74 | 0.03 | 194020.92 | 7.74 | skipped_fast |
| KITEUSDT | IDLE | 3.8 | 9.68 | 3.87 | 0.06 | 73187.94 | 11.8 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 4.52 | 3.78 | -0.03 | 86816.67 | 33.58 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6716.59 | 44.37 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11182.34 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | 0.0 | 173485.83 | 10.28 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.78 | 0.0 | 52277.06 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 1.04 | 0.04 | 58160.6 | 16.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
