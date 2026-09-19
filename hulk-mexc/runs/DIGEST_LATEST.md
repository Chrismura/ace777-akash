# Hulk DIGEST — 2026-09-19T05:57:12Z

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
| XRPUSDT | IDLE | 1.45 | 3.26 | 0.7 | 0.09 | 71026960.54 | 0.7 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.09 | 0.81 | 0.05 | 723920919.77 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.15 | 0.07 | 0.06 | 614597772.76 | 0.68 | skipped_fast |
| WUSDT | IDLE | 1.5 | 4.45 | 3.54 | 0.07 | 966056.76 | 6.51 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.53 | 19.02 | 13.13 | 0.07 | 105698.98 | 18.33 | skipped_fast |
| PYTHUSDT | IDLE | 2.14 | 3.89 | 2.65 | 0.01 | 679947.33 | 4.97 | skipped_fast |
| CCUSDT | IDLE | 2.0 | 3.52 | 3.21 | 0.01 | 531417.42 | 7.27 | skipped_fast |
| RIZEUSDT | IDLE | 2.13 | 17.7 | 9.62 | -0.07 | 42467.44 | 43.66 | skipped_fast |
| CHIPUSDT | IDLE | 2.29 | 7.81 | 3.82 | 0.07 | 144845.22 | 19.6 | skipped_fast |
| EDELUSDT | IDLE | 1.78 | 8.41 | 1.98 | -0.03 | 179715.43 | 4.5 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.89 | 0.79 | 0.04 | 646136.17 | 2.52 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 3.11 | 0.98 | 0.04 | 70211.4 | 13.22 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.34 | 2.25 | 0.03 | 84422.68 | 11.15 | skipped_fast |
| ZBCNUSDT | IDLE | 0.81 | 1.47 | 0.95 | 0.01 | 208536.04 | 19.94 | skipped_fast |
| RWAINCUSDT | IDLE | 0.67 | 1.21 | 0.8 | 0.06 | 6008.29 | 5.72 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 4.23 | 3.13 | 0.1 | 127799.44 | 57.05 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.27 | 1.14 | 0.01 | 73752.97 | 6.34 | skipped_fast |
| FLUIDUSDT | IDLE | 0.79 | 3.4 | 1.71 | 0.16 | 5381.68 | 21.7 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.19 | 0.0 | 0.0 | 55472.3 | 36.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.01 | 0.01 | 0.01 | 0.05 | 40449.57 | 2.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
