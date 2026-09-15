# Hulk DIGEST — 2026-09-15T03:44:10Z

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
| XRPUSDT | IDLE | 1.46 | 2.87 | 2.27 | 0.03 | 75028842.21 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 1.35 | 2.4 | 2.03 | -0.0 | 449183365.15 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 49.04 | 23.48 | 0.25 | 442521.33 | 35.07 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.46 | 1.34 | 0.0 | 504082169.44 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.95 | 40.02 | 20.59 | -0.07 | 58582.69 | 107.05 | skipped_fast |
| ZBCNUSDT | IDLE | 2.53 | 4.51 | 3.73 | 0.03 | 196007.34 | 20.04 | skipped_fast |
| REDUSDT | IDLE | 2.25 | 8.27 | 4.47 | 0.06 | 172488.36 | 17.99 | skipped_fast |
| PYTHUSDT | IDLE | 1.5 | 2.77 | 1.54 | -0.01 | 354289.89 | 1.78 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 2.98 | 1.77 | 0.0 | 306899.46 | 5.18 | skipped_fast |
| WUSDT | IDLE | 1.62 | 2.88 | 2.34 | -0.02 | 206878.05 | 14.19 | skipped_fast |
| KITEUSDT | IDLE | 1.78 | 3.16 | 2.68 | -0.03 | 65773.86 | 12.29 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.51 | 1.99 | -0.0 | 97747.25 | 11.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 2.8 | 1.48 | -0.02 | 73630.82 | 19.15 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.75 | 1.25 | 0.02 | 368637.5 | 1.29 | skipped_fast |
| RWAINCUSDT | IDLE | 0.74 | 1.39 | 0.6 | 0.0 | 5606.36 | 5.5 | skipped_fast |
| TELUSDT | IDLE | 1.33 | 3.03 | 2.34 | 0.03 | 103688.93 | 61.54 | skipped_fast |
| FLUIDUSDT | IDLE | 1.11 | 2.06 | 1.11 | 0.01 | 1692.54 | 21.66 | skipped_fast |
| QNTUSDT | IDLE | 0.46 | 0.9 | 0.14 | 0.02 | 40106.42 | 6.17 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.9 | 0.74 | -0.01 | 54734.98 | 22.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 0.97 | 0.77 | 0.01 | 33675.13 | 27.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
