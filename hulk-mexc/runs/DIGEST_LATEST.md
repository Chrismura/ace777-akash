# Hulk DIGEST — 2026-09-08T06:38:14Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.02 | 1.79 | 1.67 | -0.02 | 33154151.45 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 1.01 | 1.77 | 1.67 | -0.01 | 302702076.69 | 0.41 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.4 | 1.37 | -0.02 | 475060400.92 | 0.2 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.63 | 10.33 | 8.56 | -0.07 | 50366.63 | 72.16 | skipped_fast |
| CCUSDT | IDLE | 1.65 | 2.92 | 2.56 | -0.05 | 460064.45 | 12.41 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.73 | 7.31 | 6.53 | -0.1 | 132927.39 | 11.82 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.19 | 1.27 | -0.03 | 395299.68 | 1.86 | skipped_fast |
| WUSDT | IDLE | 1.76 | 3.1 | 2.75 | -0.03 | 237062.74 | 13.69 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 2.86 | 2.59 | -0.0 | 507484.45 | 1.24 | skipped_fast |
| KITEUSDT | IDLE | 2.21 | 3.87 | 3.62 | -0.06 | 64644.59 | 10.99 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 5.98 | 1.53 | -0.04 | 89320.19 | 48.66 | skipped_fast |
| ZBCNUSDT | IDLE | 0.91 | 2.29 | 2.24 | -0.05 | 241348.0 | 13.09 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.68 | 2.61 | 0.02 | 57974.01 | 9.28 | skipped_fast |
| RWAINCUSDT | IDLE | 2.0 | 7.39 | 6.88 | -0.11 | 3173.24 | 99.5 | skipped_fast |
| BIOUSDT | IDLE | 1.33 | 2.33 | 2.14 | -0.01 | 62786.69 | 7.4 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 1.87 | 1.79 | -0.01 | 60213.29 | 6.09 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 1.66 | 1.46 | -0.02 | 78508.15 | 17.75 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.53 | 0.65 | 0.0 | 54088.45 | 14.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.22 | -0.01 | 36657.75 | 35.37 | skipped_fast |
| FLUIDUSDT | IDLE | 0.17 | 0.3 | 0.29 | 0.02 | 789.42 | 14.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
