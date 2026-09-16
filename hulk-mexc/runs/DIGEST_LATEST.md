# Hulk DIGEST — 2026-09-16T21:03:02Z

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
| XRPUSDT | IDLE | 2.84 | 5.48 | 1.3 | 0.01 | 60114681.83 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.56 | 0.79 | 0.0 | 372846793.21 | 0.66 | skipped_fast |
| BTCUSDT | IDLE | 1.02 | 1.96 | 0.52 | 0.0 | 513526819.83 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.32 | 6.96 | 0.07 | 0.05 | 479664.23 | 8.31 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.59 | 12.11 | 9.13 | 0.0 | 66027.06 | 10.82 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 4.01 | 1.22 | -0.0 | 414400.6 | 1.9 | skipped_fast |
| CHIPUSDT | IDLE | 2.45 | 5.22 | 2.91 | -0.01 | 80082.85 | 11.12 | skipped_fast |
| WUSDT | IDLE | 1.8 | 3.59 | 0.03 | -0.02 | 210268.67 | 12.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.88 | 3.58 | 1.23 | 0.03 | 200528.81 | 27.1 | skipped_fast |
| BIOUSDT | IDLE | 2.07 | 4.13 | 0.08 | -0.0 | 78489.54 | 8.03 | skipped_fast |
| EDELUSDT | IDLE | 0.49 | 4.31 | 0.89 | 0.05 | 329064.35 | 22.54 | skipped_fast |
| REDUSDT | IDLE | 1.74 | 3.64 | 0.77 | -0.03 | 65454.26 | 17.86 | skipped_fast |
| RWAINCUSDT | IDLE | 1.61 | 2.84 | 2.47 | -0.04 | 12105.92 | 18.11 | skipped_fast |
| TELUSDT | IDLE | 2.49 | 4.87 | 0.89 | -0.05 | 114160.58 | 41.35 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 2.88 | 0.54 | -0.02 | 262600.28 | 1.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.55 | 8.6 | 2.19 | 0.32 | 58871.21 | 41.15 | skipped_fast |
| RWAUSDT | IDLE | 2.0 | 3.87 | 0.82 | 0.01 | 53619.29 | 45.01 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.94 | 0.05 | -0.01 | 37614.69 | 4.96 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | -0.02 | 1573.23 | 21.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.73 | 0.35 | -0.01 | 30901.73 | 14.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
