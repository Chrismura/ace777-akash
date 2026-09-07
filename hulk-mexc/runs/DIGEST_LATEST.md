# Hulk DIGEST — 2026-09-07T19:36:49Z

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
| XRPUSDT | IDLE | 0.96 | 1.89 | 0.23 | -0.01 | 36186700.15 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.33 | 0.09 | 0.0 | 342173010.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.89 | 0.0 | -0.01 | 458299772.96 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.86 | 10.48 | 4.84 | -0.04 | 214263.05 | 11.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.85 | 3.42 | 1.93 | 0.01 | 551548.57 | 1.82 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 3.43 | 2.62 | -0.04 | 451773.95 | 10.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 7.85 | 1.09 | -0.05 | 237740.27 | 20.16 | skipped_fast |
| HBARUSDT | IDLE | 1.6 | 3.14 | 0.35 | 0.03 | 590601.82 | 1.21 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.77 | 8.31 | 7.67 | -0.0 | 4890.86 | 51.98 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 7.6 | 5.32 | -0.07 | 94920.73 | 40.94 | skipped_fast |
| RIZEUSDT | IDLE | 2.49 | 7.16 | 4.37 | -0.06 | 59093.42 | 60.21 | skipped_fast |
| WUSDT | IDLE | 1.37 | 2.6 | 0.99 | -0.02 | 280850.98 | 9.76 | skipped_fast |
| REDUSDT | IDLE | 1.97 | 3.77 | 1.19 | 0.04 | 59883.32 | 9.0 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 3.37 | 2.38 | -0.05 | 60736.94 | 11.71 | skipped_fast |
| BIOUSDT | IDLE | 1.68 | 3.17 | 1.26 | -0.01 | 68665.14 | 3.66 | skipped_fast |
| MNSRYUSDT | IDLE | 2.77 | 5.29 | 1.67 | -0.02 | 37106.52 | 38.22 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.89 | 1.16 | -0.02 | 112669.34 | 11.74 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 2.11 | 0.21 | 0.01 | 47002.67 | 3.0 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.72 | -0.01 | 53881.94 | 21.83 | skipped_fast |
| FLUIDUSDT | IDLE | 0.07 | 0.14 | 0.0 | 0.0 | 1172.4 | 21.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
