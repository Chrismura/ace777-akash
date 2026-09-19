# Hulk DIGEST — 2026-09-19T17:59:13Z

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
| XRPUSDT | IDLE | 1.22 | 2.17 | 1.79 | 0.03 | 60695385.54 | 2.1 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.53 | 0.81 | 0.02 | 357349848.57 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.91 | 0.55 | 0.01 | 503994092.35 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.62 | 14.49 | 4.25 | 0.11 | 224366.63 | 19.88 | skipped_fast |
| WUSDT | IDLE | 2.43 | 4.42 | 2.93 | 0.02 | 604285.93 | 10.82 | skipped_fast |
| PYTHUSDT | IDLE | 1.37 | 2.54 | 1.32 | 0.02 | 680430.33 | 4.96 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 9.89 | 5.49 | -0.03 | 5508.6 | 95.29 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.69 | 1.55 | 0.02 | 363637.26 | 6.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 4.45 | 3.57 | 0.0 | 126705.96 | 22.98 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.18 | 0.73 | 0.04 | 559897.61 | 1.23 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 7.36 | 3.71 | -0.13 | 170533.68 | 48.05 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 3.09 | 1.39 | 0.04 | 82412.65 | 14.14 | skipped_fast |
| RIZEUSDT | IDLE | 2.03 | 8.74 | 7.52 | 0.02 | 38446.49 | 104.71 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.05 | 1.65 | 0.04 | 71072.53 | 6.08 | skipped_fast |
| REDUSDT | IDLE | 0.64 | 2.7 | 2.23 | 0.02 | 133842.86 | 8.16 | skipped_fast |
| TELUSDT | IDLE | 1.23 | 3.73 | 2.31 | -0.01 | 128175.28 | 26.28 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.11 | 1.51 | 0.08 | 9845.44 | 23.79 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.26 | 1.23 | 0.02 | 48403.31 | 3.07 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.48 | 0.66 | 0.0 | 54062.51 | 14.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.82 | 1.52 | 0.79 | 0.0 | 36226.34 | 62.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
