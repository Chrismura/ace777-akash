# Hulk DIGEST — 2026-09-14T03:41:29Z

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
| XRPUSDT | IDLE | 1.77 | 3.48 | 0.42 | 0.01 | 22696138.42 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 1.13 | 2.2 | 0.44 | -0.0 | 305929610.77 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.0 | 1.94 | 0.36 | 0.0 | 365524030.96 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 49.46 | 24.0 | 0.22 | 71354.3 | 103.11 | skipped_fast |
| REDUSDT | IDLE | 4.15 | 10.0 | 2.55 | 0.03 | 90136.44 | 9.46 | skipped_fast |
| PYTHUSDT | IDLE | 2.31 | 4.62 | 2.29 | 0.03 | 475208.33 | 1.76 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 7.94 | 1.93 | 0.11 | 223624.67 | 7.29 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 3.0 | 0.36 | -0.01 | 331748.81 | 7.23 | skipped_fast |
| WUSDT | IDLE | 2.07 | 4.09 | 0.35 | 0.0 | 185093.44 | 4.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.96 | 3.47 | 3.0 | -0.02 | 206420.04 | 25.18 | skipped_fast |
| KITEUSDT | IDLE | 2.18 | 4.27 | 0.56 | 0.02 | 59277.17 | 11.93 | skipped_fast |
| BIOUSDT | IDLE | 2.09 | 4.12 | 0.35 | 0.0 | 68269.26 | 7.79 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 5.35 | 0.58 | -0.1 | 96711.64 | 18.68 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.31 | 0.44 | 0.02 | 266226.0 | 1.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.4 | 0.72 | 0.6 | -0.01 | 8964.06 | 27.51 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.75 | 0.85 | -0.02 | 1413.38 | 21.89 | skipped_fast |
| QNTUSDT | IDLE | 1.12 | 2.18 | 0.38 | -0.01 | 35688.1 | 9.46 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 1.86 | 0.25 | -0.03 | 83455.88 | 50.66 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.6 | 0.0 | 0.0 | 53081.18 | 14.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.18 | -0.0 | 30296.19 | 6.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
