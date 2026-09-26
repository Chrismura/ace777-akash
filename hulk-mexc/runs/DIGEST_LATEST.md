# Hulk DIGEST — 2026-09-26T12:59:19Z

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
| XRPUSDT | IDLE | 0.72 | 1.3 | 0.92 | -0.04 | 71297637.71 | 0.65 | skipped_fast |
| PYTHUSDT | IDLE | 2.57 | 7.91 | 2.3 | 0.07 | 1156412.81 | 2.59 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.66 | 0.35 | -0.01 | 205941669.62 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.49 | 0.31 | -0.01 | 469888287.57 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 4.36 | 1.66 | 0.13 | 997730.28 | 10.94 | skipped_fast |
| QNTUSDT | IDLE | 2.45 | 10.52 | 5.95 | 0.09 | 793589.02 | 5.8 | skipped_fast |
| WUSDT | IDLE | 1.89 | 4.86 | 2.25 | 0.05 | 478984.32 | 7.88 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 5.0 | 1.23 | 0.02 | 173358.57 | 3.28 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 5.93 | 5.17 | 0.02 | 6194.82 | 60.45 | skipped_fast |
| BIOUSDT | IDLE | 1.77 | 3.18 | 2.4 | 0.01 | 123990.07 | 6.14 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.5 | 1.14 | -0.01 | 601277.61 | 1.07 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.52 | 0.49 | -0.01 | 222135.09 | 16.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.55 | 2.82 | 1.82 | -0.0 | 133298.0 | 14.39 | skipped_fast |
| REDUSDT | IDLE | 1.41 | 2.49 | 2.2 | -0.02 | 57697.16 | 7.14 | skipped_fast |
| RIZEUSDT | IDLE | 1.36 | 8.55 | 3.84 | -0.14 | 49105.93 | 96.91 | skipped_fast |
| RWAUSDT | IDLE | 2.27 | 4.23 | 2.07 | 0.0 | 55824.32 | 14.56 | skipped_fast |
| KITEUSDT | IDLE | 0.85 | 2.03 | 0.0 | 0.05 | 73593.9 | 8.78 | skipped_fast |
| TELUSDT | IDLE | 1.5 | 2.71 | 1.97 | -0.04 | 121885.24 | 75.33 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | 0.01 | 3388.79 | 21.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.04 | 0.0 | 39072.74 | 6.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
