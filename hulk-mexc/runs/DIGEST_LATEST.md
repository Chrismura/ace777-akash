# Hulk DIGEST — 2026-08-22T08:28:15Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.08 | 0.03 | 28182411.59 | 15.94 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 23.87 | 10.55 | 0.13 | 223778303.93 | 2.64 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 10.01 | 0.03 | 1342953.97 | 3.84 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 12.82 | -0.1 | 684823.59 | 10.11 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.6 | 0.03 | 598269.51 | 15.65 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.47 | -0.04 | 250628.59 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.6 | 0.07 | 155638.6 | 9.68 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 11.25 | 2.64 | 0.18 | 822722.07 | 5.74 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.02 | 0.02 | 538036.2 | 7.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.17 | 0.02 | 194020.84 | 13.98 | skipped_fast |
| KITEUSDT | IDLE | 3.82 | 9.68 | 4.25 | 0.06 | 73250.19 | 9.12 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6716.59 | 21.14 | skipped_fast |
| EDELUSDT | IDLE | 2.26 | 4.52 | 3.14 | -0.03 | 86841.64 | 44.74 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11182.34 | 128.82 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | 0.01 | 173461.63 | 20.57 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.78 | 0.01 | 52274.28 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 0.96 | 0.05 | 58274.09 | 8.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
