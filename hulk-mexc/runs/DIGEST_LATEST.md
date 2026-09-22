# Hulk DIGEST — 2026-09-22T17:15:10Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.06 | 18.79 | 10.29 | 0.02 | 1559620.99 | 6.04 | skipped_fast |
| XRPUSDT | IDLE | 2.25 | 4.27 | 1.51 | 0.05 | 116425897.55 | 2.55 | skipped_fast |
| ETHUSDT | IDLE | 0.91 | 1.73 | 0.57 | -0.0 | 473737624.09 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.42 | 0.31 | 0.01 | 909794195.68 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.57 | 5.76 | 2.52 | 0.05 | 1363693.98 | 1.04 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 6.91 | 5.6 | -0.02 | 484158.11 | 7.08 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 14.26 | 11.62 | -0.01 | 263409.54 | 29.22 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.87 | 0.58 | 0.03 | 364861.51 | 8.26 | skipped_fast |
| CHIPUSDT | IDLE | 2.44 | 4.48 | 2.61 | -0.0 | 142739.79 | 17.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.99 | 3.64 | 2.3 | -0.02 | 238450.0 | 49.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.95 | 23.47 | 3.91 | -0.18 | 42641.05 | 114.23 | skipped_fast |
| BIOUSDT | IDLE | 2.06 | 4.12 | 0.0 | 0.02 | 127315.52 | 6.78 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.2 | 8.52 | 0.4 | 0.06 | 102895.18 | 17.17 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 6.05 | 1.07 | 0.16 | 110542.21 | 9.46 | skipped_fast |
| REDUSDT | IDLE | 1.82 | 3.53 | 0.71 | 0.03 | 66342.08 | 15.85 | skipped_fast |
| QNTUSDT | IDLE | 1.9 | 6.04 | 1.97 | 0.1 | 188791.23 | 9.57 | skipped_fast |
| RWAINCUSDT | IDLE | 0.84 | 1.61 | 0.49 | 0.04 | 23249.21 | 5.51 | skipped_fast |
| FLUIDUSDT | IDLE | 0.67 | 1.25 | 0.63 | 0.0 | 7959.28 | 44.58 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.95 | 0.51 | -0.0 | 53971.31 | 51.0 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.05 | -0.0 | 40299.3 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
