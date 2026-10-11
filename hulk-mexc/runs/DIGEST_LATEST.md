# Hulk DIGEST — 2026-10-11T17:20:51Z

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
| XRPUSDT | IDLE | 1.21 | 2.38 | 0.31 | 0.01 | 13517845.89 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 1.09 | 2.14 | 0.31 | 0.02 | 212434728.72 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.21 | 0.09 | 0.01 | 148632059.48 | 0.0 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.37 | 8.15 | 0.93 | 0.05 | 924481.45 | 11.9 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 11.9 | 8.01 | -0.0 | 28167.1 | 14.75 | skipped_fast |
| PYTHUSDT | IDLE | 1.33 | 2.51 | 1.01 | -0.03 | 769386.65 | 3.89 | skipped_fast |
| CCUSDT | IDLE | 2.75 | 5.44 | 0.74 | 0.06 | 329737.57 | 8.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.67 | 9.0 | 3.58 | 0.23 | 410636.48 | 13.21 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 2.06 | 0.78 | 0.0 | 857415.57 | 0.41 | skipped_fast |
| EDELUSDT | IDLE | 1.77 | 3.17 | 2.47 | -0.0 | 404333.54 | 18.23 | skipped_fast |
| ZBCNUSDT | IDLE | 2.64 | 5.23 | 0.36 | 0.04 | 175978.25 | 19.77 | skipped_fast |
| TELUSDT | IDLE | 3.85 | 7.16 | 3.65 | -0.02 | 143112.2 | 34.46 | skipped_fast |
| RIZEUSDT | IDLE | 2.01 | 5.52 | 1.02 | -0.03 | 31888.48 | 12.33 | skipped_fast |
| REDUSDT | IDLE | 1.89 | 3.69 | 0.65 | 0.01 | 57884.33 | 8.52 | skipped_fast |
| BIOUSDT | IDLE | 1.66 | 3.24 | 0.59 | 0.04 | 85378.82 | 6.65 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 2.09 | 0.13 | -0.0 | 70507.69 | 2.34 | skipped_fast |
| HBARUSDT | IDLE | 1.43 | 2.79 | 0.5 | 0.01 | 248866.4 | 4.27 | skipped_fast |
| RWAUSDT | IDLE | 1.3 | 2.54 | 0.46 | 0.01 | 50874.58 | 15.53 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 5.76 | 0.25 | 0.09 | 55691.0 | 17.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.86 | 1.66 | 0.41 | -0.01 | 30545.63 | 17.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
