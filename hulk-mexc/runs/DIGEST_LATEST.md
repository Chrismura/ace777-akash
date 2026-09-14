# Hulk DIGEST — 2026-09-14T04:42:02Z

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
| XRPUSDT | IDLE | 1.72 | 3.39 | 0.38 | 0.01 | 23812383.72 | 2.18 | skipped_fast |
| ETHUSDT | IDLE | 1.11 | 2.2 | 0.16 | -0.0 | 310006109.82 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.99 | 1.94 | 0.33 | 0.0 | 372216304.57 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.54 | 49.46 | 23.37 | 0.2 | 70388.87 | 53.18 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 9.93 | 7.6 | -0.02 | 113871.14 | 19.95 | skipped_fast |
| PYTHUSDT | IDLE | 1.87 | 3.91 | 1.0 | 0.05 | 495467.75 | 1.74 | skipped_fast |
| WUSDT | IDLE | 2.31 | 4.55 | 0.45 | 0.01 | 191754.41 | 10.86 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 7.94 | 0.71 | 0.13 | 226695.9 | 21.54 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.71 | 1.08 | -0.02 | 328361.02 | 9.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.9 | 3.47 | 2.15 | -0.02 | 206864.11 | 12.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.8 | 7.62 | 1.16 | -0.08 | 102947.0 | 13.77 | skipped_fast |
| KITEUSDT | IDLE | 1.96 | 3.71 | 1.36 | -0.01 | 59275.93 | 10.18 | skipped_fast |
| BIOUSDT | IDLE | 1.85 | 3.66 | 0.31 | 0.0 | 68493.16 | 3.89 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.19 | 0.22 | 0.02 | 270362.74 | 1.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.07 | 2.07 | 0.44 | -0.01 | 9452.93 | 27.46 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 2.34 | 0.05 | -0.0 | 35864.36 | 1.57 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.75 | 0.85 | -0.02 | 1413.38 | 21.87 | skipped_fast |
| TELUSDT | IDLE | 1.07 | 2.12 | 0.13 | -0.03 | 83566.09 | 25.22 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.6 | 0.07 | -0.0 | 52566.85 | 7.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.22 | 0.19 | -0.0 | 30284.03 | 5.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
