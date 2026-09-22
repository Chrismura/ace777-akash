# Hulk DIGEST — 2026-09-22T15:13:00Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 20.05 | 11.45 | 0.0 | 1472847.04 | 10.71 | skipped_fast |
| XRPUSDT | IDLE | 2.56 | 4.93 | 1.27 | 0.05 | 115053420.97 | 3.18 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.73 | 0.78 | -0.0 | 526609376.31 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.14 | 0.31 | 0.0 | 928880125.63 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.56 | 5.39 | 0.27 | 0.06 | 1212127.14 | 3.07 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 3.99 | 3.35 | -0.01 | 497629.67 | 9.52 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 9.22 | 4.29 | 0.09 | 259610.7 | 11.95 | skipped_fast |
| QNTUSDT | IDLE | 3.34 | 10.62 | 3.24 | 0.07 | 184086.56 | 8.3 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.89 | 0.47 | 0.01 | 382007.21 | 5.85 | skipped_fast |
| CHIPUSDT | IDLE | 2.4 | 4.48 | 2.17 | -0.03 | 146826.86 | 17.39 | skipped_fast |
| RIZEUSDT | IDLE | 2.06 | 24.12 | 8.29 | -0.21 | 41677.65 | 119.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 2.28 | 1.77 | -0.02 | 261973.74 | 23.87 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 2.78 | 0.75 | -0.01 | 115014.23 | 3.45 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 5.59 | 0.0 | 0.14 | 114576.7 | 29.85 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 2.45 | 0.53 | 0.01 | 66056.62 | 14.09 | skipped_fast |
| TELUSDT | IDLE | 2.28 | 4.52 | 0.3 | 0.05 | 104673.62 | 41.65 | skipped_fast |
| RWAINCUSDT | IDLE | 0.88 | 1.61 | 1.04 | 0.03 | 26762.05 | 5.51 | skipped_fast |
| FLUIDUSDT | IDLE | 1.14 | 2.07 | 1.37 | 0.01 | 8990.81 | 19.85 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.95 | 0.22 | -0.0 | 54508.95 | 29.15 | skipped_fast |
| MNSRYUSDT | IDLE | 0.11 | 0.21 | 0.05 | -0.0 | 40082.25 | 6.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
