# Hulk DIGEST — 2026-09-15T14:45:26Z

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
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 5.66 | 5.02 | -0.01 | 81491023.3 | 2.88 | skipped_fast |
| ETHUSDT | IDLE | 1.71 | 3.15 | 2.83 | -0.03 | 480553294.17 | 2.28 | skipped_fast |
| BTCUSDT | IDLE | 1.12 | 2.0 | 1.65 | -0.03 | 563250902.93 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 10.01 | 8.64 | -0.08 | 88742.43 | 15.77 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 5.93 | 5.33 | -0.02 | 208615.82 | 27.23 | skipped_fast |
| EDELUSDT | IDLE | 1.71 | 24.22 | 2.28 | 0.51 | 459223.5 | 109.79 | skipped_fast |
| RWAINCUSDT | IDLE | 3.12 | 5.5 | 4.94 | -0.04 | 9432.51 | 22.88 | skipped_fast |
| CCUSDT | IDLE | 1.55 | 2.74 | 2.4 | -0.03 | 344820.71 | 9.64 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 20.86 | 8.88 | -0.04 | 55549.29 | 104.46 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 3.88 | 3.29 | 0.01 | 424493.88 | 1.3 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.48 | 2.09 | -0.03 | 281452.09 | 1.87 | skipped_fast |
| WUSDT | IDLE | 1.49 | 2.81 | 2.4 | -0.04 | 142902.09 | 13.72 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.3 | 1.82 | -0.02 | 84607.94 | 8.05 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.44 | 2.26 | -0.0 | 61150.06 | 10.49 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 4.25 | 3.7 | -0.07 | 109310.58 | 19.16 | skipped_fast |
| QNTUSDT | IDLE | 1.24 | 2.19 | 1.96 | -0.03 | 46963.23 | 4.82 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 3.53 | 2.27 | -0.04 | 98329.81 | 38.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.33 | 2.34 | 2.08 | -0.04 | 2088.93 | 22.03 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.98 | 0.37 | -0.01 | 52364.77 | 14.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.59 | 1.04 | 0.91 | 0.0 | 33475.39 | 66.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
