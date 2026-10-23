# Hulk DIGEST — 2026-10-23T09:44:55Z

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
| XRPUSDT | IDLE | 0.59 | 1.06 | 0.83 | -0.01 | 25699451.65 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.49 | 0.89 | 0.55 | -0.0 | 231898014.57 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.28 | 0.51 | 0.36 | -0.0 | 346591510.76 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.41 | 4.27 | 3.62 | -0.01 | 687491.51 | 18.62 | skipped_fast |
| PYTHUSDT | IDLE | 1.95 | 3.51 | 2.66 | -0.03 | 652688.34 | 1.39 | skipped_fast |
| ZBCNUSDT | IDLE | 3.63 | 8.19 | 4.01 | -0.01 | 172976.99 | 4.95 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 11.91 | 8.94 | -0.1 | 45217.03 | 53.63 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 2.99 | 2.5 | -0.06 | 403362.86 | 22.14 | skipped_fast |
| QNTUSDT | IDLE | 1.97 | 3.52 | 2.8 | -0.05 | 535200.73 | 0.54 | skipped_fast |
| CHIPUSDT | IDLE | 2.15 | 4.25 | 2.05 | 0.05 | 130484.77 | 22.05 | skipped_fast |
| HBARUSDT | IDLE | 1.83 | 3.25 | 2.77 | -0.02 | 309370.4 | 15.12 | skipped_fast |
| CCUSDT | IDLE | 0.83 | 1.46 | 1.36 | -0.02 | 211310.16 | 8.78 | skipped_fast |
| RWAINCUSDT | IDLE | 1.27 | 2.3 | 1.59 | 0.02 | 50011.15 | 5.58 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 1.73 | 1.56 | -0.01 | 82532.64 | 15.7 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.22 | 0.87 | 0.01 | 59190.76 | 8.37 | skipped_fast |
| KITEUSDT | IDLE | 0.54 | 1.05 | 0.25 | 0.0 | 57401.26 | 10.82 | skipped_fast |
| WAXLUSDT | IDLE | 1.78 | 3.13 | 2.85 | -0.03 | 56946.28 | 61.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.04 | 1.95 | 1.91 | -0.05 | 9555.94 | 21.13 | skipped_fast |
| LAUSDT | IDLE | 0.89 | 1.7 | 0.47 | -0.0 | 53868.19 | 23.48 | skipped_fast |
| IOTAUSDT | IDLE | 0.72 | 1.3 | 0.91 | -0.0 | 64753.1 | 22.3 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.51 | 1.02 | -0.0 | 52503.85 | 31.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.34 | 0.63 | 0.4 | -0.01 | 38030.84 | 65.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
