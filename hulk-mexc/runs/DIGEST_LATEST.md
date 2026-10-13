# Hulk DIGEST — 2026-10-13T17:06:45Z

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
| WUSDT | IDLE | 2.12 | 16.19 | 12.97 | -0.23 | 5323337.66 | 18.86 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 8.61 | 5.16 | -0.07 | 2140850.61 | 11.27 | skipped_fast |
| XRPUSDT | IDLE | 1.06 | 1.96 | 1.05 | 0.0 | 37298641.79 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.74 | 1.36 | 0.78 | -0.0 | 237068819.78 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.85 | 0.68 | 0.01 | 385579537.66 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 4.18 | 2.92 | -0.11 | 1297884.18 | 4.89 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 14.13 | 10.78 | -0.1 | 77086.08 | 60.67 | skipped_fast |
| CCUSDT | IDLE | 2.31 | 7.41 | 1.04 | 0.07 | 589149.95 | 10.0 | skipped_fast |
| EDELUSDT | IDLE | 2.46 | 5.03 | 2.99 | 0.04 | 306443.12 | 20.58 | skipped_fast |
| ZBCNUSDT | IDLE | 1.75 | 3.31 | 1.21 | -0.01 | 236392.42 | 13.89 | skipped_fast |
| CHIPUSDT | IDLE | 2.02 | 4.31 | 3.54 | -0.02 | 108854.64 | 12.25 | skipped_fast |
| REDUSDT | IDLE | 1.51 | 3.24 | 0.34 | -0.01 | 151228.72 | 8.46 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 3.37 | 1.68 | -0.02 | 344022.33 | 5.72 | skipped_fast |
| RWAINCUSDT | IDLE | 1.88 | 3.75 | 0.0 | 0.02 | 30261.51 | 24.06 | skipped_fast |
| BIOUSDT | IDLE | 1.36 | 3.0 | 1.19 | -0.03 | 72028.82 | 7.28 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.33 | 1.19 | 0.01 | 60537.42 | 10.27 | skipped_fast |
| TELUSDT | IDLE | 1.58 | 2.89 | 1.74 | -0.0 | 106736.51 | 22.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.38 | 2.93 | 1.19 | 0.04 | 26423.78 | 21.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.58 | 1.04 | 0.78 | -0.02 | 38318.96 | 16.74 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.46 | 0.38 | -0.0 | 52450.66 | 7.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
