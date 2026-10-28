# Hulk DIGEST — 2026-10-28T04:26:02Z

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
| XRPUSDT | IDLE | 0.78 | 1.4 | 1.09 | 0.02 | 19607198.61 | 2.26 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.21 | 0.66 | 0.02 | 247907250.95 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.74 | 0.34 | 0.01 | 314326158.8 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.77 | 5.49 | 2.72 | -0.07 | 215858.1 | 23.02 | skipped_fast |
| WUSDT | IDLE | 0.76 | 1.73 | 0.41 | 0.05 | 656425.06 | 23.31 | skipped_fast |
| EDELUSDT | IDLE | 1.84 | 3.4 | 1.88 | 0.02 | 387960.51 | 21.36 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 11.23 | 9.7 | -0.0 | 7487.54 | 21.3 | skipped_fast |
| RWAINCUSDT | IDLE | 2.51 | 5.25 | 4.85 | -0.05 | 58540.76 | 13.55 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 1.89 | 1.45 | -0.01 | 667800.96 | 1.52 | skipped_fast |
| PYTHUSDT | IDLE | 0.97 | 1.75 | 1.22 | 0.0 | 373524.51 | 5.48 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 2.02 | 0.36 | 0.03 | 226298.32 | 7.02 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 3.29 | 1.62 | 0.07 | 127128.7 | 16.49 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 1.82 | 1.31 | 0.03 | 59020.59 | 8.83 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 2.07 | 1.27 | 0.0 | 328429.84 | 10.48 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.83 | 1.35 | 0.05 | 59729.26 | 11.02 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 1.84 | 1.3 | 0.06 | 59127.57 | 15.6 | skipped_fast |
| LAUSDT | IDLE | 1.3 | 2.5 | 2.18 | 0.03 | 58749.28 | 20.29 | skipped_fast |
| RIZEUSDT | IDLE | 0.34 | 0.65 | 0.25 | 0.02 | 34804.38 | 64.68 | skipped_fast |
| IOTAUSDT | IDLE | 1.03 | 1.85 | 1.4 | 0.01 | 75172.5 | 28.38 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.81 | 0.4 | -0.01 | 56078.4 | 16.05 | skipped_fast |
| WAXLUSDT | IDLE | 0.71 | 1.25 | 1.2 | 0.03 | 56951.68 | 63.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.77 | 0.57 | 0.0 | 36091.13 | 66.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
