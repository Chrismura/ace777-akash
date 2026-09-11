# Hulk DIGEST — 2026-09-11T21:20:49Z

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
| RIZEUSDT | IDLE | 2.16 | 149.56 | 44.33 | 0.93 | 225106.67 | 101.09 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 2.81 | 1.34 | 0.01 | 54847240.22 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 1.1 | 2.37 | 1.7 | 0.03 | 639622942.26 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.5 | 0.84 | 0.0 | 562875372.33 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.65 | 10.48 | 2.91 | 0.04 | 166674.9 | 26.4 | skipped_fast |
| PYTHUSDT | IDLE | 2.47 | 4.61 | 3.5 | -0.02 | 414278.16 | 1.95 | skipped_fast |
| WUSDT | IDLE | 2.19 | 4.23 | 2.79 | 0.01 | 201989.33 | 13.38 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 6.1 | 4.41 | -0.05 | 141457.68 | 14.88 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 1.74 | 1.32 | -0.01 | 445123.82 | 8.19 | skipped_fast |
| RWAINCUSDT | IDLE | 2.53 | 5.21 | 1.16 | 0.05 | 13171.13 | 5.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 2.9 | 2.27 | -0.01 | 190803.02 | 10.44 | skipped_fast |
| BIOUSDT | IDLE | 1.73 | 3.19 | 1.84 | 0.0 | 83280.28 | 11.95 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.31 | 0.27 | 0.05 | 62876.96 | 17.2 | skipped_fast |
| HBARUSDT | IDLE | 1.44 | 2.65 | 1.54 | -0.01 | 241027.88 | 1.34 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 1.55 | 0.72 | -0.01 | 59293.6 | 10.13 | skipped_fast |
| TELUSDT | IDLE | 1.6 | 3.23 | 1.9 | -0.02 | 103357.56 | 39.92 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 2.1 | 2.05 | -0.02 | 41461.19 | 3.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 2.66 | 2.19 | 0.02 | 1301.43 | 21.67 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.05 | 0.22 | 0.02 | 52545.42 | 22.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.55 | 0.99 | 0.69 | 0.0 | 36269.27 | 44.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
