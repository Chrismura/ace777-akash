# Hulk DIGEST — 2026-10-12T07:51:57Z

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
| WUSDT | IDLE | 1.82 | 35.96 | 2.41 | 0.72 | 11787985.51 | 20.53 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.51 | 0.49 | 0.03 | 234918760.97 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.35 | 0.53 | 0.01 | 22045371.31 | 2.12 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.98 | 0.35 | 0.01 | 190698015.71 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.83 | 6.39 | 1.55 | 0.05 | 1097227.75 | 4.88 | skipped_fast |
| QNTUSDT | IDLE | 2.05 | 3.95 | 1.06 | 0.02 | 775564.22 | 2.91 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 7.92 | 5.17 | -0.01 | 221486.74 | 14.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.64 | 5.36 | 1.61 | 0.07 | 279693.57 | 12.51 | skipped_fast |
| REDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.47 | 8.57 | 0.52 | 0.07 | 55986.31 | 14.87 | skipped_fast |
| CCUSDT | IDLE | 1.24 | 2.28 | 1.34 | 0.05 | 428158.46 | 7.97 | skipped_fast |
| RIZEUSDT | IDLE | 2.5 | 16.43 | 4.99 | 0.14 | 46782.84 | 74.76 | skipped_fast |
| EDELUSDT | IDLE | 1.7 | 3.12 | 1.82 | -0.04 | 280258.17 | 18.6 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 1.96 | 0.95 | 0.02 | 422712.58 | 4.24 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 2.14 | 1.33 | 0.02 | 62267.87 | 12.47 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.69 | 1.2 | -0.0 | 99856.87 | 3.36 | skipped_fast |
| RWAINCUSDT | IDLE | 1.04 | 2.95 | 1.93 | -0.01 | 21352.22 | 5.03 | skipped_fast |
| TELUSDT | IDLE | 1.48 | 2.75 | 1.37 | -0.03 | 174990.36 | 5.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.78 | 1.37 | 1.24 | 0.01 | 36068.44 | 5.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.43 | 3.22 | 1.03 | 0.06 | 66450.85 | 19.59 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.46 | 0.08 | 0.03 | 52485.79 | 15.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
