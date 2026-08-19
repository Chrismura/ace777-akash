# Hulk DIGEST — 2026-08-19T19:17:45Z

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
| XRPUSDT | IDLE | 2.95 | 5.83 | 0.53 | 0.07 | 26409327.53 | 2.81 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 17.68 | 9.06 | 0.0 | 121163.32 | 14.93 | skipped_fast |
| CCUSDT | IDLE | 3.85 | 11.04 | 2.65 | 0.07 | 296247.3 | 9.25 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 19.8 | 7.26 | 0.09 | 167413.87 | 6.37 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.75 | 14.65 | 0.59 | 0.14 | 74978.08 | 23.56 | skipped_fast |
| RIZEUSDT | IDLE | 4.25 | 8.15 | 3.46 | -0.02 | 44856.64 | 24.84 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 13.4 | 5.27 | 0.14 | 135604.96 | 3.56 | skipped_fast |
| PYTHUSDT | IDLE | 2.83 | 5.55 | 0.72 | 0.02 | 251444.42 | 2.48 | skipped_fast |
| ZBCNUSDT | IDLE | 2.86 | 7.74 | 0.52 | 0.1 | 200193.03 | 20.4 | skipped_fast |
| WUSDT | IDLE | 2.62 | 5.07 | 1.19 | 0.04 | 173276.8 | 13.01 | skipped_fast |
| QAITUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.27 | 9.16 | 1.07 | 0.03 | 11397.81 | 62.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 5.02 | 2.67 | 0.05 | 172244.36 | 3.56 | skipped_fast |
| KITEUSDT | IDLE | 2.31 | 4.5 | 0.84 | 0.04 | 57324.27 | 12.53 | skipped_fast |
| FLUIDUSDT | IDLE | 3.45 | 7.57 | 3.64 | 0.03 | 2835.1 | 22.19 | skipped_fast |
| HBARUSDT | IDLE | 2.17 | 4.08 | 1.76 | 0.04 | 254957.15 | 1.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.11 | 3.17 | 2.46 | 0.03 | 17094.75 | 5.72 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 3.54 | 1.45 | 0.03 | 38058.1 | 8.67 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.49 | 1.04 | -0.0 | 53836.65 | 17.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
