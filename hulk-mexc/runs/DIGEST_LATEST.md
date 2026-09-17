# Hulk DIGEST — 2026-09-17T18:04:02Z

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
| XRPUSDT | IDLE | 1.26 | 2.29 | 1.49 | 0.04 | 53502197.25 | 3.08 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 2.02 | 0.84 | 0.04 | 395038795.18 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.38 | 0.52 | 0.02 | 510357260.58 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.29 | 6.31 | 0.77 | 0.1 | 622611.56 | 3.52 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 3.22 | 2.93 | 0.09 | 634800.23 | 7.99 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.81 | 8.92 | 6.74 | -0.08 | 186554.39 | 58.41 | skipped_fast |
| RIZEUSDT | IDLE | 2.77 | 19.9 | 3.66 | -0.07 | 46100.01 | 104.34 | skipped_fast |
| WUSDT | IDLE | 1.97 | 5.89 | 0.02 | 0.11 | 245714.49 | 13.27 | skipped_fast |
| CHIPUSDT | IDLE | 2.2 | 7.14 | 4.12 | 0.06 | 140738.56 | 15.65 | skipped_fast |
| HBARUSDT | IDLE | 1.84 | 3.5 | 1.24 | 0.05 | 566862.13 | 1.32 | skipped_fast |
| ZBCNUSDT | IDLE | 2.3 | 4.32 | 1.9 | 0.03 | 187111.99 | 18.7 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.79 | 2.05 | 0.03 | 65002.33 | 0.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 3.46 | 2.19 | 0.01 | 21911.57 | 23.6 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 3.14 | 0.38 | 0.05 | 61308.15 | 12.32 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.21 | 0.79 | 0.04 | 71101.4 | 11.87 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.41 | 1.35 | 0.04 | 89920.49 | 34.09 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 1.74 | 0.92 | 0.03 | 37180.31 | 4.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.04 | 235.05 | 21.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.55 | 1.02 | 0.54 | 0.02 | 41750.83 | 5.59 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.13 | 0.07 | 0.01 | 58284.17 | 29.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
