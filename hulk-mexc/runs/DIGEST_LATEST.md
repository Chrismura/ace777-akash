# Hulk DIGEST — 2026-09-16T21:14:10Z

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
| XRPUSDT | IDLE | 2.87 | 5.48 | 1.71 | 0.0 | 59962644.5 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.56 | 0.85 | 0.0 | 371803177.08 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.02 | 1.96 | 0.6 | 0.0 | 513059447.62 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.35 | 6.96 | 0.5 | 0.04 | 481175.73 | 9.39 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.6 | 12.11 | 9.18 | -0.0 | 66154.25 | 12.8 | skipped_fast |
| PYTHUSDT | IDLE | 2.12 | 4.01 | 1.47 | -0.01 | 413060.82 | 1.91 | skipped_fast |
| CHIPUSDT | IDLE | 2.45 | 5.22 | 2.99 | -0.03 | 79991.72 | 13.92 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.81 | 0.17 | -0.03 | 210363.25 | 13.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.86 | 3.58 | 0.96 | 0.03 | 199510.7 | 16.11 | skipped_fast |
| BIOUSDT | IDLE | 2.11 | 4.17 | 0.32 | -0.01 | 78603.61 | 8.04 | skipped_fast |
| REDUSDT | IDLE | 1.72 | 3.64 | 0.49 | -0.03 | 65253.16 | 17.04 | skipped_fast |
| EDELUSDT | IDLE | 0.5 | 4.31 | 1.49 | 0.03 | 326268.9 | 37.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.62 | 2.84 | 2.65 | -0.05 | 12125.98 | 18.11 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 4.87 | 1.5 | -0.05 | 114523.85 | 20.8 | skipped_fast |
| HBARUSDT | IDLE | 1.51 | 2.88 | 0.93 | -0.03 | 262479.59 | 1.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.55 | 8.6 | 2.02 | 0.3 | 58822.25 | 73.63 | skipped_fast |
| RWAUSDT | IDLE | 1.99 | 3.87 | 0.67 | 0.01 | 53785.01 | 30.03 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 2.94 | 0.15 | -0.01 | 37538.47 | 6.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | -0.02 | 1573.23 | 21.27 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.73 | 0.31 | -0.01 | 30867.83 | 2.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
