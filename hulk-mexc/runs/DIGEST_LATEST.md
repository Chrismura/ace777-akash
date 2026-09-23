# Hulk DIGEST — 2026-09-23T15:20:41Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 10.92 | 7.36 | -0.03 | 1423269.77 | 1.58 | skipped_fast |
| XRPUSDT | IDLE | 2.71 | 6.11 | 4.45 | -0.03 | 120621341.75 | 1.31 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.03 | 9.2 | 6.03 | -0.05 | 1732578.12 | 1.09 | skipped_fast |
| ETHUSDT | IDLE | 1.92 | 3.51 | 2.22 | -0.02 | 489158456.78 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.35 | 2.47 | 1.58 | -0.02 | 859648088.97 | 0.0 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.0 | 9.65 | 6.42 | -0.03 | 411863.57 | 8.64 | skipped_fast |
| CCUSDT | IDLE | 2.94 | 6.23 | 4.15 | -0.06 | 468205.63 | 10.13 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 8.67 | 5.53 | -0.05 | 222505.88 | 13.81 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 7.52 | 5.34 | -0.01 | 126863.09 | 10.45 | skipped_fast |
| REDUSDT | IDLE | 3.42 | 6.33 | 3.38 | 0.0 | 59889.62 | 7.01 | skipped_fast |
| ZBCNUSDT | IDLE | 2.44 | 5.81 | 3.55 | 0.02 | 247448.2 | 14.7 | skipped_fast |
| QNTUSDT | IDLE | 3.76 | 8.9 | 4.54 | -0.0 | 200681.46 | 4.16 | skipped_fast |
| KITEUSDT | IDLE | 2.81 | 5.2 | 2.82 | -0.02 | 165867.05 | 10.4 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 6.04 | 5.27 | -0.13 | 209520.49 | 24.03 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 8.15 | 6.56 | 0.03 | 158685.91 | 46.38 | skipped_fast |
| FLUIDUSDT | IDLE | 3.44 | 6.26 | 4.12 | -0.02 | 4131.68 | 21.97 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 14.55 | 9.49 | 0.44 | 63464.48 | 52.11 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.69 | 0.43 | 0.03 | 20960.13 | 21.52 | skipped_fast |
| RWAUSDT | IDLE | 1.65 | 2.89 | 2.67 | -0.02 | 55313.1 | 14.79 | skipped_fast |
| MNSRYUSDT | IDLE | 1.08 | 1.97 | 1.32 | -0.01 | 40972.51 | 32.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
