# Hulk DIGEST — 2026-09-29T14:46:22Z

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
| HBARUSDT | IDLE | 1.73 | 6.39 | 4.37 | -0.04 | 6927599.88 | 0.87 | skipped_fast |
| XRPUSDT | IDLE | 2.09 | 4.15 | 0.26 | 0.05 | 62110600.84 | 1.93 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 9.42 | 6.82 | 0.05 | 9313252.42 | 5.26 | skipped_fast |
| ETHUSDT | IDLE | 0.91 | 1.65 | 1.14 | 0.02 | 435791240.36 | 0.22 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.88 | 0.63 | 0.01 | 593713426.08 | 0.0 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 7.69 | 5.85 | 0.03 | 992684.16 | 8.56 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 3.0 | 1.4 | -0.0 | 905274.88 | 11.49 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 3.01 | 0.72 | 0.01 | 901274.67 | 3.76 | skipped_fast |
| ZBCNUSDT | IDLE | 2.44 | 19.46 | 2.0 | 0.29 | 340443.08 | 32.21 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 16.48 | 9.6 | 0.07 | 48156.26 | 75.92 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 18.06 | 9.99 | 0.07 | 24103.49 | 19.97 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 10.42 | 5.92 | -0.06 | 62899.39 | 42.43 | skipped_fast |
| BIOUSDT | IDLE | 2.08 | 7.14 | 0.0 | 0.12 | 111068.98 | 3.06 | skipped_fast |
| KITEUSDT | IDLE | 2.12 | 3.87 | 2.41 | 0.02 | 67418.83 | 7.9 | skipped_fast |
| TELUSDT | IDLE | 1.05 | 8.93 | 5.01 | 0.25 | 467698.92 | 48.0 | skipped_fast |
| REDUSDT | IDLE | 1.63 | 3.25 | 0.1 | 0.04 | 70461.16 | 12.67 | skipped_fast |
| CHIPUSDT | IDLE | 1.44 | 3.09 | 0.0 | 0.04 | 72808.67 | 17.52 | skipped_fast |
| EDELUSDT | IDLE | 0.43 | 1.5 | 0.76 | -0.11 | 94059.95 | 22.88 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.46 | 1.22 | -0.01 | 55570.03 | 36.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.6 | 0.24 | -0.0 | 36265.54 | 9.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
