# Hulk DIGEST — 2026-08-22T09:55:36Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 19.14 | 11.19 | 0.02 | 49386050.6 | 12.1 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 11.85 | 0.06 | 216388438.32 | 4.01 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 15.8 | 10.61 | 0.02 | 1261800.39 | 3.86 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 23.96 | 12.85 | -0.11 | 665271.68 | 3.39 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 17.58 | 9.48 | 0.02 | 592577.39 | 13.69 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.22 | -0.03 | 237703.16 | 3.22 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 12.32 | 0.05 | 153975.95 | 11.57 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 11.25 | 8.04 | 0.12 | 804857.84 | 7.82 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 8.0 | 6.9 | -0.01 | 438567.74 | 17.22 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 9.68 | 5.09 | 0.04 | 73276.55 | 9.19 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.19 | 0.01 | 191922.04 | 9.32 | skipped_fast |
| EDELUSDT | IDLE | 2.65 | 4.64 | 4.43 | -0.03 | 79215.57 | 11.25 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 19.19 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 7.2 | 6.52 | -0.02 | 171102.74 | 36.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.45 | 4.36 | 3.61 | 0.01 | 11477.95 | 64.86 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.79 | -0.01 | 49323.32 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.02 | 57554.74 | 8.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
