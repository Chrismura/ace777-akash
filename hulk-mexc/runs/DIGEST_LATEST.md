# Hulk DIGEST — 2026-09-22T23:06:50Z

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
| XRPUSDT | IDLE | 1.88 | 3.48 | 1.83 | 0.01 | 107024014.8 | 3.16 | skipped_fast |
| HBARUSDT | IDLE | 2.05 | 5.15 | 1.12 | 0.07 | 1681279.24 | 9.04 | skipped_fast |
| PYTHUSDT | IDLE | 0.69 | 3.37 | 0.49 | 0.05 | 1660559.78 | 10.44 | skipped_fast |
| ETHUSDT | IDLE | 0.52 | 1.02 | 0.08 | -0.01 | 416027075.3 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.76 | 0.4 | -0.0 | 903911251.03 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 42.49 | 11.42 | 0.1 | 50357.7 | 106.57 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.65 | 9.03 | 5.96 | 0.01 | 20205.35 | 32.17 | skipped_fast |
| CCUSDT | IDLE | 1.25 | 2.5 | 0.01 | -0.03 | 486335.97 | 9.57 | skipped_fast |
| WUSDT | IDLE | 1.61 | 3.22 | 0.06 | 0.03 | 325812.67 | 5.71 | skipped_fast |
| CHIPUSDT | IDLE | 1.82 | 3.79 | 0.3 | -0.01 | 136260.01 | 12.94 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 7.91 | 4.86 | -0.01 | 241436.01 | 135.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.28 | 1.88 | -0.03 | 214532.61 | 18.95 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.57 | 0.07 | 0.03 | 135963.35 | 13.38 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 4.82 | 1.71 | 0.1 | 211204.57 | 6.78 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.97 | 0.23 | 0.05 | 63422.96 | 13.77 | skipped_fast |
| KITEUSDT | IDLE | 0.61 | 2.75 | 0.39 | 0.17 | 113205.98 | 12.16 | skipped_fast |
| TELUSDT | IDLE | 1.32 | 5.51 | 0.7 | 0.11 | 101657.49 | 65.08 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.51 | 0.43 | -0.01 | 52978.35 | 14.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.86 | 0.13 | 0.02 | 5956.82 | 21.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.03 | -0.01 | 39917.76 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
