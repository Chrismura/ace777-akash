# Hulk DIGEST — 2026-08-22T05:25:19Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.07 | 0.08 | 16215508.58 | 15.93 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 23.87 | 12.37 | 0.14 | 197455428.41 | 8.06 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.47 | 0.05 | 1342793.17 | 12.7 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.74 | -0.09 | 682103.42 | 19.93 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.6 | 0.06 | 582102.73 | 11.47 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.15 | -0.03 | 213981.47 | 9.87 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 45.06 | 12.0 | 0.12 | 164026.77 | 29.38 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.56 | 3.81 | 0.17 | 757510.43 | 8.41 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 8.47 | 6.49 | 0.05 | 544203.12 | 31.12 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 13.91 | 9.7 | 0.03 | 195303.47 | 39.02 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 9.68 | 6.43 | 0.08 | 73305.87 | 14.89 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.73 | -0.02 | 88495.76 | 32.91 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.34 | 0.05 | 5420.59 | 38.57 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.03 | 11443.8 | 69.46 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.05 | 5.52 | 2.32 | 0.08 | 192480.25 | 35.4 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 4.01 | 0.09 | 58713.72 | 42.81 | skipped_fast |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.15 | 0.05 | 57531.12 | 40.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
