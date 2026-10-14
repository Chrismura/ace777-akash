# Hulk DIGEST — 2026-10-14T14:19:27Z

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
| PYTHUSDT | IDLE | 2.58 | 6.19 | 2.88 | 0.01 | 2099139.08 | 3.61 | skipped_fast |
| WUSDT | IDLE | 1.85 | 7.99 | 6.61 | -0.17 | 3384104.39 | 9.14 | skipped_fast |
| ETHUSDT | IDLE | 2.03 | 3.56 | 3.28 | -0.03 | 160928961.41 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.02 | 3.56 | 3.19 | -0.03 | 36301914.25 | 1.49 | skipped_fast |
| BTCUSDT | IDLE | 1.31 | 2.3 | 2.19 | -0.02 | 381679971.98 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.91 | 4.44 | 3.83 | -0.02 | 1555630.76 | 2.94 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 18.92 | 15.67 | -0.01 | 50444.42 | 60.06 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 4.89 | 4.3 | -0.09 | 478789.31 | 5.96 | skipped_fast |
| ZBCNUSDT | IDLE | 2.74 | 4.8 | 4.48 | -0.03 | 190396.64 | 17.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.84 | 5.51 | 4.4 | -0.08 | 77389.18 | 10.97 | skipped_fast |
| EDELUSDT | IDLE | 2.05 | 3.65 | 3.06 | -0.04 | 144754.75 | 14.88 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 4.04 | 3.48 | -0.04 | 69061.99 | 11.28 | skipped_fast |
| KITEUSDT | IDLE | 1.97 | 5.55 | 3.93 | 0.03 | 83667.28 | 8.36 | skipped_fast |
| HBARUSDT | IDLE | 2.21 | 3.89 | 3.58 | -0.06 | 302766.75 | 3.57 | skipped_fast |
| REDUSDT | IDLE | 1.93 | 3.43 | 2.81 | -0.01 | 59710.92 | 8.54 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 5.62 | 3.63 | -0.07 | 32669.37 | 5.31 | skipped_fast |
| FLUIDUSDT | IDLE | 2.03 | 5.74 | 5.43 | 0.03 | 23124.04 | 19.32 | skipped_fast |
| TELUSDT | IDLE | 1.59 | 2.79 | 2.6 | 0.0 | 105383.44 | 22.74 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.74 | 1.55 | -0.02 | 56133.44 | 15.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.55 | 1.0 | 0.6 | -0.01 | 39881.75 | 26.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
