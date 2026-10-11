# Hulk DIGEST — 2026-10-11T19:22:10Z

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
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.59 | 22.13 | 1.02 | 0.18 | 2105671.34 | 18.59 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 2.36 | 1.14 | 0.0 | 14826565.84 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 1.13 | 2.14 | 0.75 | 0.01 | 212590510.93 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.38 | 0.54 | 0.01 | 153875129.78 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 2.97 | 0.49 | -0.01 | 825312.69 | 1.28 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 22.33 | 11.79 | 0.01 | 40612.39 | 53.4 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.96 | 3.97 | -0.01 | 408818.65 | 21.14 | skipped_fast |
| ZBCNUSDT | IDLE | 2.97 | 5.42 | 3.53 | 0.01 | 204385.51 | 5.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 6.53 | 3.16 | 0.07 | 353671.52 | 14.62 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 4.18 | 0.38 | 0.08 | 327348.33 | 5.5 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 2.0 | 0.79 | 0.0 | 825474.55 | 4.1 | skipped_fast |
| TELUSDT | IDLE | 3.96 | 7.35 | 4.31 | -0.03 | 161311.18 | 34.74 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 3.58 | 0.83 | 0.01 | 57480.82 | 15.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.73 | 4.86 | 2.01 | 0.01 | 28368.72 | 4.88 | skipped_fast |
| BIOUSDT | IDLE | 1.2 | 2.26 | 0.89 | 0.02 | 88001.34 | 6.67 | skipped_fast |
| HBARUSDT | IDLE | 1.42 | 2.69 | 0.97 | 0.01 | 285964.82 | 8.59 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.13 | 0.05 | -0.01 | 73547.96 | 12.47 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.21 | 1.82 | 0.02 | 52330.65 | 23.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 5.76 | 0.59 | 0.06 | 57624.49 | 21.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.92 | 1.75 | 0.58 | -0.01 | 30694.79 | 12.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
