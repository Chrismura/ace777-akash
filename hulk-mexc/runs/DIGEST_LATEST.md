# Hulk DIGEST — 2026-08-31T01:15:25Z

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
| XRPUSDT | IDLE | 3.26 | 5.88 | 4.25 | -0.03 | 32280882.26 | 2.95 | skipped_fast |
| ETHUSDT | IDLE | 2.78 | 5.03 | 3.59 | -0.02 | 366618032.27 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.38 | 2.51 | 1.6 | -0.01 | 369012674.56 | 0.2 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 7.16 | 5.39 | -0.02 | 488780.96 | 2.13 | skipped_fast |
| WUSDT | IDLE | 3.67 | 6.81 | 4.5 | -0.01 | 236835.96 | 12.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.05 | 6.38 | 3.06 | -0.04 | 521537.47 | 2.59 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.94 | 7.16 | 5.05 | -0.05 | 88445.55 | 3.82 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.03 | 8.23 | 5.54 | -0.08 | 91132.59 | 11.77 | skipped_fast |
| CCUSDT | IDLE | 2.35 | 4.26 | 2.94 | -0.02 | 232357.73 | 10.38 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 6.32 | 5.3 | 0.04 | 78635.83 | 25.41 | skipped_fast |
| ZBCNUSDT | IDLE | 1.67 | 3.74 | 2.39 | -0.04 | 218171.17 | 18.67 | skipped_fast |
| REDUSDT | IDLE | 2.32 | 4.49 | 0.95 | 0.0 | 62984.37 | 21.9 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.5 | 6.19 | 5.38 | -0.03 | 3917.97 | 18.73 | skipped_fast |
| HBARUSDT | IDLE | 2.3 | 4.14 | 3.09 | -0.02 | 215310.18 | 1.36 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 5.01 | 2.41 | -0.05 | 42907.58 | 57.7 | skipped_fast |
| TELUSDT | IDLE | 3.32 | 5.92 | 4.8 | 0.01 | 86804.84 | 65.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.65 | 3.05 | 1.64 | 0.02 | 1751.1 | 95.0 | skipped_fast |
| QNTUSDT | IDLE | 1.94 | 3.53 | 2.34 | -0.02 | 38351.68 | 8.3 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.39 | 1.05 | 0.0 | 52852.91 | 16.25 | skipped_fast |
| MNSRYUSDT | IDLE | 1.04 | 1.87 | 1.39 | -0.01 | 32434.64 | 48.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
