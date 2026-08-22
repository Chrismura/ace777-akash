# Hulk DIGEST — 2026-08-22T09:36:02Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.48 | 0.03 | 42910971.82 | 6.0 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 23.87 | 10.49 | 0.1 | 218728209.72 | 2.63 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 15.8 | 9.75 | 0.04 | 1292880.71 | 5.1 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 23.96 | 12.12 | -0.09 | 665207.95 | 6.72 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.55 | 0.04 | 594565.72 | 15.63 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.51 | -0.03 | 237674.86 | 6.45 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 41.27 | 11.03 | 0.06 | 154560.59 | 7.89 | skipped_fast |
| CCUSDT | IDLE | 2.21 | 11.25 | 7.1 | 0.14 | 797628.19 | 6.03 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.56 | -0.01 | 440218.12 | 14.63 | skipped_fast |
| KITEUSDT | IDLE | 4.29 | 9.68 | 4.67 | 0.04 | 73147.87 | 10.97 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.93 | 0.01 | 193165.2 | 6.19 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.02 | 79319.19 | 22.4 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.69 | 5.87 | -0.01 | 171249.75 | 5.25 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.01 | 11436.39 | 91.42 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.84 | -0.02 | 49412.54 | 46.77 | skipped_fast |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
