# Hulk DIGEST — 2026-09-07T10:34:58Z

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
| XRPUSDT | IDLE | 1.05 | 1.92 | 1.24 | -0.01 | 32695750.18 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.52 | 0.96 | -0.0 | 314206478.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.16 | 0.65 | -0.01 | 404056829.55 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 7.43 | 5.73 | -0.11 | 374104.83 | 14.81 | skipped_fast |
| PYTHUSDT | IDLE | 1.6 | 3.07 | 0.89 | 0.01 | 600866.99 | 1.8 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 3.63 | 3.2 | -0.03 | 428888.9 | 8.39 | skipped_fast |
| WUSDT | IDLE | 1.74 | 3.3 | 1.16 | 0.03 | 464187.49 | 13.49 | skipped_fast |
| EDELUSDT | IDLE | 2.81 | 7.53 | 4.3 | -0.04 | 74486.73 | 29.23 | skipped_fast |
| KITEUSDT | IDLE | 2.57 | 4.56 | 3.91 | -0.05 | 56953.86 | 10.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.56 | 8.07 | 6.91 | -0.16 | 72475.37 | 64.98 | skipped_fast |
| REDUSDT | IDLE | 1.76 | 3.52 | 0.0 | 0.02 | 63651.77 | 14.5 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 2.03 | 0.19 | -0.02 | 163713.26 | 2.66 | skipped_fast |
| BIOUSDT | IDLE | 1.27 | 2.39 | 0.95 | -0.02 | 71535.71 | 3.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 4.21 | 2.19 | 0.06 | 6557.34 | 4.91 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.81 | 1.24 | -0.01 | 361343.75 | 1.24 | skipped_fast |
| TELUSDT | IDLE | 1.7 | 3.11 | 1.99 | 0.01 | 103776.71 | 23.23 | skipped_fast |
| QNTUSDT | IDLE | 1.32 | 2.33 | 2.11 | -0.01 | 39425.59 | 9.18 | skipped_fast |
| FLUIDUSDT | IDLE | 0.81 | 1.58 | 0.25 | -0.01 | 1152.45 | 23.66 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.58 | 0.5 | -0.01 | 53263.32 | 14.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.13 | -0.0 | 38647.11 | 18.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
