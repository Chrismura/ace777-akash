# Hulk DIGEST — 2026-10-21T00:04:49Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.09 | 2.08 | 0.71 | 0.02 | 24810109.9 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.6 | 0.73 | 0.02 | 175625405.48 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.94 | 0.26 | 0.01 | 333848865.29 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 4.97 | 1.27 | 0.09 | 1194031.04 | 2.5 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.76 | 1.09 | 0.03 | 657760.6 | 17.8 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 3.39 | 1.9 | 0.0 | 807735.02 | 1.54 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 9.64 | 8.69 | -0.04 | 77246.57 | 16.12 | skipped_fast |
| CHIPUSDT | IDLE | 0.98 | 3.53 | 1.23 | 0.06 | 444748.42 | 13.37 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 13.83 | 10.48 | 0.06 | 17190.17 | 21.16 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.76 | 1.09 | 0.0 | 392575.44 | 8.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 2.89 | 0.94 | 0.02 | 192807.04 | 14.49 | skipped_fast |
| EDELUSDT | IDLE | 0.41 | 3.73 | 1.22 | 0.33 | 363432.32 | 16.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.83 | 4.56 | 0.07 | 75184.02 | 63.44 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.17 | 1.0 | 0.05 | 61836.46 | 4.05 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.76 | 0.32 | 0.02 | 353209.44 | 3.56 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 1.88 | 0.08 | 0.02 | 58154.94 | 15.59 | skipped_fast |
| KITEUSDT | IDLE | 0.76 | 1.33 | 1.23 | -0.01 | 73726.12 | 9.07 | skipped_fast |
| LAUSDT | IDLE | 1.32 | 2.56 | 0.55 | 0.03 | 54591.0 | 20.31 | skipped_fast |
| IOTAUSDT | IDLE | 1.11 | 2.06 | 1.02 | 0.03 | 73123.88 | 30.01 | skipped_fast |
| WAXLUSDT | IDLE | 1.0 | 1.89 | 0.67 | -0.04 | 55948.26 | 59.87 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.16 | 0.0 | 52036.44 | 23.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.43 | 0.27 | -0.0 | 39593.55 | 34.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
