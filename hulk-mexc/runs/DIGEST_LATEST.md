# Hulk DIGEST — 2026-09-17T06:15:00Z

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
| XRPUSDT | IDLE | 0.82 | 1.49 | 1.02 | 0.0 | 55172078.85 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.33 | 0.18 | 0.02 | 386885892.96 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.89 | 0.38 | 0.01 | 508404359.51 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.39 | 4.56 | 1.45 | 0.02 | 531862.19 | 1.84 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.71 | 10.83 | 7.37 | -0.06 | 217561.4 | 28.48 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 4.07 | 1.75 | 0.08 | 575282.13 | 6.11 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 4.35 | 1.53 | 0.03 | 172552.26 | 13.81 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 16.51 | 11.58 | -0.03 | 61300.53 | 69.09 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.06 | 1.48 | 0.03 | 222646.17 | 14.11 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 4.33 | 2.77 | -0.02 | 79298.25 | 19.19 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.93 | 1.7 | -0.01 | 60513.32 | 0.76 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.65 | 0.86 | 0.07 | 67312.06 | 12.92 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.59 | 1.18 | 0.02 | 77990.6 | 7.94 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.38 | 1.05 | -0.01 | 317865.92 | 2.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.89 | 1.7 | 0.52 | -0.01 | 16388.57 | 63.6 | skipped_fast |
| TELUSDT | IDLE | 0.88 | 1.53 | 1.51 | -0.03 | 115832.92 | 41.81 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.42 | 0.98 | 0.01 | 37730.78 | 1.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.95 | 0.07 | 0.01 | 36277.68 | 1.41 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.98 | 0.22 | 0.02 | 55668.66 | 44.88 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1571.52 | 21.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
