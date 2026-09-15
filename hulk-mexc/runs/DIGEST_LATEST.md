# Hulk DIGEST — 2026-09-15T01:44:11Z

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
| ETHUSDT | IDLE | 2.41 | 4.25 | 3.74 | 0.01 | 452228800.54 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.31 | 5.41 | 4.46 | 0.06 | 75270993.68 | 2.81 | skipped_fast |
| BTCUSDT | IDLE | 1.32 | 2.34 | 1.99 | 0.01 | 566815776.19 | 0.0 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 49.04 | 1.92 | 0.67 | 381297.77 | 40.83 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.74 | 30.46 | 22.5 | -0.07 | 62400.41 | 54.62 | skipped_fast |
| CCUSDT | IDLE | 2.5 | 4.46 | 3.63 | 0.0 | 316882.0 | 3.12 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 1.69 | 0.41 | -0.01 | 386628.12 | 1.77 | skipped_fast |
| WUSDT | IDLE | 1.62 | 2.92 | 2.14 | 0.01 | 206190.83 | 13.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.69 | 2.96 | 2.86 | 0.02 | 198501.33 | 25.4 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 4.85 | 0.26 | 0.09 | 166049.06 | 16.53 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 2.92 | 2.54 | 0.02 | 96598.73 | 15.55 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 3.03 | 2.75 | -0.0 | 64998.15 | 11.27 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 2.48 | 1.73 | 0.03 | 374793.01 | 1.28 | skipped_fast |
| TELUSDT | IDLE | 2.35 | 5.57 | 4.18 | 0.06 | 104485.26 | 36.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.12 | 2.25 | 0.47 | 0.01 | 75184.97 | 21.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.79 | 1.44 | 0.98 | -0.01 | 5778.16 | 5.53 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.37 | 1.28 | 0.03 | 1526.34 | 21.54 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.54 | 0.12 | 0.03 | 43733.52 | 7.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.73 | 1.33 | 0.92 | 0.01 | 32030.56 | 12.42 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.05 | 0.74 | -0.0 | 55165.86 | 22.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
