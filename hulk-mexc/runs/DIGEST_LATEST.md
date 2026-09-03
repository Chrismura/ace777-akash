# Hulk DIGEST — 2026-09-03T01:04:07Z

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
| ETHUSDT | IDLE | 0.69 | 1.23 | 0.97 | -0.01 | 348383059.86 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.67 | 1.19 | 0.97 | 0.0 | 35803122.6 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.7 | 0.51 | -0.0 | 495742564.15 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.14 | 3.55 | 3.02 | 0.05 | 1346204.55 | 1.77 | skipped_fast |
| CHIPUSDT | IDLE | 1.06 | 3.89 | 2.68 | -0.04 | 923006.07 | 4.77 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.52 | 2.39 | -0.04 | 414443.0 | 8.29 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 25.63 | 13.78 | 0.16 | 56058.21 | 192.22 | skipped_fast |
| EDELUSDT | IDLE | 1.75 | 6.62 | 4.95 | -0.0 | 135017.97 | 26.35 | skipped_fast |
| WUSDT | IDLE | 1.57 | 2.83 | 2.08 | 0.02 | 222202.64 | 14.46 | skipped_fast |
| BIOUSDT | IDLE | 2.24 | 4.26 | 1.45 | 0.01 | 70862.81 | 15.5 | skipped_fast |
| REDUSDT | IDLE | 1.91 | 3.65 | 1.09 | 0.02 | 113301.71 | 19.71 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 4.69 | 3.77 | 0.11 | 141446.4 | 9.4 | skipped_fast |
| ZBCNUSDT | IDLE | 1.09 | 2.34 | 2.12 | -0.02 | 180483.72 | 23.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 5.45 | 0.0 | 0.13 | 12319.52 | 52.03 | skipped_fast |
| HBARUSDT | IDLE | 0.68 | 1.31 | 0.37 | 0.01 | 192804.74 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 1.7 | 0.43 | 0.01 | 60714.18 | 10.88 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.77 | 1.14 | 0.0 | 51477.49 | 22.98 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 1.6 | 0.47 | 0.04 | 74007.45 | 29.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.09 | 0.18 | 0.0 | -0.02 | 2252.11 | 20.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.0 | 18804.92 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
