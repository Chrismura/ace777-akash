# Hulk DIGEST — 2026-09-02T19:55:16Z

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
| XRPUSDT | IDLE | 0.9 | 1.76 | 0.32 | -0.01 | 36522590.27 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.58 | 0.97 | -0.01 | 363298189.94 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.06 | 0.49 | -0.0 | 507996003.93 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.75 | 7.5 | 2.68 | 0.14 | 1319691.63 | 1.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 6.15 | 0.14 | -0.04 | 1052450.04 | 11.76 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 16.69 | 5.19 | 0.01 | 40607.03 | 72.93 | skipped_fast |
| ZBCNUSDT | IDLE | 3.03 | 8.19 | 3.11 | -0.05 | 181651.03 | 42.73 | skipped_fast |
| WUSDT | IDLE | 2.32 | 4.59 | 0.34 | -0.0 | 338171.29 | 21.6 | skipped_fast |
| KITEUSDT | IDLE | 2.0 | 9.23 | 6.58 | 0.12 | 131351.54 | 11.67 | skipped_fast |
| CCUSDT | IDLE | 1.4 | 2.52 | 1.84 | -0.04 | 382374.2 | 4.56 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.39 | 1.28 | -0.01 | 68221.96 | 3.94 | skipped_fast |
| EDELUSDT | IDLE | 0.83 | 4.33 | 3.58 | 0.09 | 167327.98 | 42.11 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 1.97 | 1.04 | 0.01 | 119138.94 | 11.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.65 | 4.48 | 2.52 | 0.06 | 9894.79 | 65.97 | skipped_fast |
| QNTUSDT | IDLE | 1.74 | 3.14 | 2.2 | 0.02 | 60770.08 | 3.11 | skipped_fast |
| FLUIDUSDT | IDLE | 1.85 | 3.5 | 1.38 | -0.01 | 2397.59 | 21.6 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.44 | 0.36 | -0.01 | 186347.0 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.66 | 3.03 | 1.9 | 0.02 | 75405.31 | 64.8 | skipped_fast |
| RWAUSDT | IDLE | 1.21 | 2.23 | 1.2 | 0.01 | 51758.74 | 7.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.12 | -0.0 | 28342.05 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
