# Hulk DIGEST — 2026-08-22T08:31:49Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 19.14 | 10.66 | 0.02 | 29057469.63 | 38.1 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 23.87 | 11.24 | 0.11 | 224343998.13 | 6.64 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.26 | 0.02 | 1340778.16 | 3.85 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 12.74 | -0.1 | 684269.42 | 6.74 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 9.08 | 0.03 | 600809.64 | 16.78 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 9.9 | -0.05 | 253216.86 | 12.86 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 12.05 | 0.07 | 155750.2 | 11.47 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 11.25 | 3.32 | 0.18 | 819956.81 | 8.27 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 8.47 | 6.39 | 0.01 | 535723.14 | 27.6 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.39 | 0.02 | 193986.46 | 9.34 | skipped_fast |
| KITEUSDT | IDLE | 3.83 | 9.68 | 4.41 | 0.06 | 73409.52 | 11.85 | skipped_fast |
| EDELUSDT | IDLE | 2.29 | 4.52 | 3.57 | -0.03 | 86908.57 | 33.61 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6716.59 | 21.17 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11110.27 | 118.03 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 4.7 | 4.05 | 0.0 | 173471.46 | 36.02 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.9 | 0.01 | 52272.69 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.73 | 3.29 | 1.12 | 0.04 | 58352.48 | 24.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
