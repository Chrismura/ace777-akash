# Hulk DIGEST — 2026-09-28T14:24:17Z

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
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 14.75 | 9.97 | -0.01 | 1298227.8 | 2.27 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 30.69 | 9.91 | 0.38 | 20614990.37 | 3.92 | skipped_fast |
| WUSDT | IDLE | 1.47 | 6.03 | 4.26 | -0.03 | 3132539.26 | 8.61 | skipped_fast |
| HBARUSDT | IDLE | 1.98 | 16.48 | 3.68 | 0.29 | 7086506.15 | 0.83 | skipped_fast |
| XRPUSDT | IDLE | 2.23 | 4.22 | 1.62 | -0.01 | 60685720.43 | 1.99 | skipped_fast |
| ETHUSDT | IDLE | 1.18 | 2.3 | 0.45 | -0.01 | 338177111.43 | 0.89 | skipped_fast |
| PYTHUSDT | IDLE | 2.02 | 4.53 | 2.45 | -0.04 | 1476858.94 | 2.48 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.45 | 0.3 | -0.02 | 724960045.02 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.53 | 23.45 | 4.25 | 0.03 | 194492.9 | 23.66 | skipped_fast |
| CHIPUSDT | IDLE | 2.49 | 5.22 | 2.68 | -0.06 | 81876.87 | 15.67 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.38 | 1.99 | -0.04 | 62184.32 | 12.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 2.31 | 0.87 | -0.04 | 232863.75 | 38.59 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 3.84 | 1.72 | -0.06 | 103066.92 | 9.41 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 3.04 | 1.66 | -0.06 | 96441.65 | 6.76 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 5.0 | 0.27 | -0.0 | 160172.22 | 48.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.57 | 5.69 | 2.22 | 0.06 | 31540.53 | 55.82 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 2.89 | 0.75 | -0.14 | 60037.48 | 108.6 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.99 | 1.44 | -0.05 | 3185.47 | 21.95 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.94 | 0.36 | -0.02 | 60210.33 | 28.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 0.96 | 0.77 | -0.02 | 34529.97 | 59.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
