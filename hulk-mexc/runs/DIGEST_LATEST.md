# Hulk DIGEST — 2026-09-19T02:56:19Z

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
| XRPUSDT | IDLE | 1.14 | 2.51 | 0.99 | 0.08 | 69957319.63 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.41 | 0.76 | 0.06 | 655024433.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.09 | 0.54 | 0.06 | 776907178.04 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.96 | 3.21 | 1.86 | 0.1 | 947357.53 | 11.89 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 19.02 | 13.97 | 0.08 | 95540.07 | 17.84 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.4 | 0.15 | 0.07 | 768935.34 | 16.22 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.5 | 0.27 | 0.05 | 637176.28 | 7.97 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 11.9 | 6.66 | -0.04 | 177513.39 | 27.46 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 2.02 | 0.45 | 0.04 | 690674.11 | 1.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 5.69 | 1.8 | 0.09 | 154874.82 | 17.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.33 | 1.47 | 0.03 | 233058.15 | 19.84 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 11.02 | 6.52 | 0.11 | 127247.3 | 44.01 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.83 | 0.16 | 0.06 | 77784.2 | 11.43 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 1.85 | 0.36 | 0.07 | 87696.37 | 10.93 | skipped_fast |
| RWAINCUSDT | IDLE | 0.13 | 0.23 | 0.23 | 0.05 | 6452.55 | 28.76 | skipped_fast |
| RIZEUSDT | IDLE | 0.12 | 2.14 | 0.0 | -0.07 | 52926.9 | 87.86 | skipped_fast |
| QNTUSDT | IDLE | 0.57 | 1.12 | 0.17 | 0.03 | 75078.08 | 4.7 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.04 | 0.81 | -0.01 | 55041.77 | 14.87 | skipped_fast |
| FLUIDUSDT | IDLE | 0.67 | 2.87 | 0.87 | 0.17 | 3962.38 | 21.58 | skipped_fast |
| MNSRYUSDT | IDLE | 0.1 | 0.18 | 0.16 | 0.06 | 42061.62 | 2.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
