# Hulk DIGEST — 2026-09-05T10:41:11Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 57.48 | 33.06 | -0.04 | 223560.67 | 18.67 | skipped_fast |
| XRPUSDT | IDLE | 0.6 | 1.13 | 0.44 | -0.03 | 38613750.14 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.33 | 0.63 | 0.22 | -0.03 | 368929756.83 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.21 | 0.4 | 0.17 | -0.02 | 502663399.99 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 5.8 | 5.48 | -0.03 | 451907.77 | 12.4 | skipped_fast |
| RIZEUSDT | IDLE | 1.13 | 25.72 | 16.47 | -0.42 | 175203.81 | 103.99 | skipped_fast |
| PYTHUSDT | IDLE | 0.71 | 1.41 | 0.09 | -0.02 | 425311.86 | 1.85 | skipped_fast |
| WUSDT | IDLE | 1.43 | 2.78 | 0.56 | 0.01 | 203545.87 | 17.11 | skipped_fast |
| KITEUSDT | IDLE | 1.81 | 3.17 | 2.97 | -0.03 | 62899.28 | 8.41 | skipped_fast |
| CCUSDT | IDLE | 0.68 | 1.3 | 0.35 | -0.03 | 337465.24 | 7.37 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.44 | 1.01 | -0.0 | 86832.5 | 3.65 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.32 | 1.1 | 0.05 | 65874.13 | 10.23 | skipped_fast |
| ZBCNUSDT | IDLE | 0.61 | 1.35 | 0.59 | -0.05 | 186136.96 | 9.05 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.31 | 0.58 | 0.02 | 279723.13 | 1.25 | skipped_fast |
| RWAUSDT | IDLE | 1.5 | 2.94 | 0.36 | 0.0 | 52861.64 | 14.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.19 | 0.64 | -0.01 | 3348.91 | 43.2 | skipped_fast |
| TELUSDT | IDLE | 0.72 | 1.3 | 0.87 | -0.03 | 74163.05 | 23.54 | skipped_fast |
| QNTUSDT | IDLE | 0.68 | 1.28 | 0.5 | -0.04 | 45290.41 | 3.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.92 | 0.0 | 0.01 | 1150.69 | 21.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.31 | 0.12 | -0.01 | 36023.4 | 30.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
