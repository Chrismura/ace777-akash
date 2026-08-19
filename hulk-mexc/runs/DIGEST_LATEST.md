# Hulk DIGEST — 2026-08-19T13:11:52Z

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
| XRPUSDT | IDLE | 0.51 | 1.02 | 0.05 | 0.02 | 11075341.44 | 0.99 | skipped_fast |
| CHIPUSDT | IDLE | 3.19 | 7.04 | 0.29 | -0.02 | 159318.84 | 7.37 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 12.24 | 9.15 | 0.0 | 13934.14 | 128.81 | skipped_fast |
| QAITUSDT | IDLE | 3.61 | 8.03 | 2.74 | 0.03 | 10764.89 | 62.35 | skipped_fast |
| BIOUSDT | IDLE | 2.87 | 5.55 | 1.3 | 0.06 | 71321.78 | 3.86 | skipped_fast |
| PYTHUSDT | IDLE | 1.37 | 2.5 | 1.62 | 0.0 | 176375.15 | 2.6 | skipped_fast |
| RIZEUSDT | IDLE | 1.89 | 5.21 | 3.41 | -0.1 | 33528.29 | 31.12 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.67 | 0.64 | -0.02 | 221978.6 | 9.94 | skipped_fast |
| KITEUSDT | IDLE | 1.52 | 2.89 | 0.94 | -0.0 | 56492.12 | 14.14 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.71 | 0.66 | -0.01 | 59176.98 | 13.27 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 2.88 | 1.59 | -0.1 | 133674.25 | 12.49 | skipped_fast |
| ZBCNUSDT | IDLE | 0.71 | 1.36 | 0.45 | 0.01 | 160333.01 | 15.07 | skipped_fast |
| WUSDT | IDLE | 0.72 | 1.38 | 0.37 | 0.0 | 102185.37 | 12.29 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 3.1 | 2.39 | 0.01 | 86483.47 | 55.98 | skipped_fast |
| HBARUSDT | IDLE | 0.47 | 0.93 | 0.1 | 0.03 | 153272.25 | 2.94 | skipped_fast |
| QNTUSDT | IDLE | 0.68 | 1.28 | 0.58 | 0.01 | 37335.1 | 5.29 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.24 | 0.26 | -0.01 | 52919.51 | 26.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.49 | 0.99 | 0.0 | -0.01 | 1234.14 | 21.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
