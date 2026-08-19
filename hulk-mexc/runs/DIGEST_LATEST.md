# Hulk DIGEST — 2026-08-19T17:17:06Z

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
| XRPUSDT | IDLE | 3.54 | 6.85 | 1.5 | 0.06 | 23956031.66 | 1.89 | skipped_fast |
| REDUSDT | IDLE | 3.87 | 17.91 | 2.95 | 0.09 | 121984.96 | 44.99 | skipped_fast |
| BIOUSDT | IDLE | 3.31 | 16.9 | 4.09 | 0.15 | 120588.53 | 3.52 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.98 | 13.8 | 1.78 | 0.1 | 71432.94 | 24.18 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.1 | 12.24 | 6.6 | 0.04 | 20520.64 | 34.11 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 19.8 | 8.32 | 0.07 | 163641.82 | 57.9 | skipped_fast |
| CCUSDT | IDLE | 3.1 | 6.19 | 0.03 | 0.05 | 265671.78 | 8.38 | skipped_fast |
| QAITUSDT | IDLE | 4.22 | 11.42 | 3.98 | 0.02 | 11844.92 | 62.35 | skipped_fast |
| PYTHUSDT | IDLE | 3.07 | 6.05 | 0.64 | 0.04 | 226073.37 | 2.48 | skipped_fast |
| ZBCNUSDT | IDLE | 3.02 | 7.07 | 0.45 | 0.08 | 198979.12 | 35.51 | skipped_fast |
| CHIPUSDT | IDLE | 2.51 | 8.0 | 3.25 | 0.01 | 157002.56 | 3.59 | skipped_fast |
| WUSDT | IDLE | 2.85 | 5.56 | 0.95 | 0.05 | 159163.17 | 10.62 | skipped_fast |
| RIZEUSDT | IDLE | 3.19 | 7.12 | 2.47 | -0.04 | 31734.03 | 51.01 | skipped_fast |
| KITEUSDT | IDLE | 2.64 | 5.16 | 0.82 | 0.04 | 57100.57 | 12.53 | skipped_fast |
| FLUIDUSDT | IDLE | 3.4 | 7.57 | 2.77 | 0.02 | 2336.32 | 21.91 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.2 | 1.18 | 0.06 | 238715.37 | 1.44 | skipped_fast |
| QNTUSDT | IDLE | 1.97 | 3.71 | 1.52 | 0.03 | 38147.07 | 10.43 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.49 | 0.61 | 0.0 | 53917.63 | 17.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
