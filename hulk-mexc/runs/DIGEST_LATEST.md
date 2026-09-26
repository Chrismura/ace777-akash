# Hulk DIGEST — 2026-09-26T15:01:42Z

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
| XRPUSDT | IDLE | 0.53 | 1.0 | 0.44 | -0.03 | 50853504.2 | 3.23 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.4 | 0.21 | 0.0 | 386239901.51 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.2 | 0.38 | 0.11 | -0.0 | 157101856.73 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.14 | 5.91 | 2.28 | 0.06 | 1175615.97 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 5.28 | 2.65 | 0.1 | 966380.64 | 7.31 | skipped_fast |
| QNTUSDT | IDLE | 1.78 | 7.41 | 0.46 | 0.16 | 938887.03 | 0.91 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 13.4 | 10.2 | -0.04 | 7696.44 | 74.07 | skipped_fast |
| WUSDT | IDLE | 1.65 | 3.37 | 1.67 | 0.07 | 451592.89 | 5.48 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 4.93 | 2.37 | 0.03 | 162729.22 | 3.28 | skipped_fast |
| BIOUSDT | IDLE | 2.06 | 3.66 | 3.02 | -0.01 | 105064.43 | 3.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.69 | 0.51 | -0.0 | 233083.93 | 6.02 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.78 | 0.63 | 0.0 | 589574.5 | 1.06 | skipped_fast |
| CHIPUSDT | IDLE | 1.38 | 2.7 | 0.34 | 0.01 | 125835.47 | 18.28 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 2.53 | 0.25 | 0.05 | 75333.11 | 10.91 | skipped_fast |
| RIZEUSDT | IDLE | 1.47 | 7.27 | 3.53 | -0.1 | 46616.43 | 89.0 | skipped_fast |
| RWAUSDT | IDLE | 2.17 | 4.23 | 0.78 | 0.02 | 55658.01 | 14.35 | skipped_fast |
| REDUSDT | IDLE | 0.81 | 1.56 | 0.41 | -0.01 | 58426.77 | 14.17 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.15 | 1.36 | -0.04 | 122475.89 | 62.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.61 | 1.22 | 0.0 | 0.03 | 628.63 | 21.33 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.42 | 0.41 | 0.0 | 39525.82 | 45.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
