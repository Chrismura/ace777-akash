# Hulk DIGEST — 2026-09-10T16:15:32Z

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
| XRPUSDT | IDLE | 1.43 | 2.52 | 2.21 | -0.05 | 44569280.35 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 1.43 | 2.67 | 1.26 | -0.02 | 425991483.56 | 0.21 | skipped_fast |
| BTCUSDT | IDLE | 0.97 | 1.74 | 1.36 | -0.02 | 550925000.65 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.22 | 67.14 | 15.93 | -0.5 | 124766.79 | 120.97 | skipped_fast |
| PYTHUSDT | IDLE | 1.48 | 4.14 | 2.76 | -0.08 | 906574.99 | 1.94 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.83 | 15.83 | 11.59 | 0.04 | 262792.91 | 54.1 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 2.68 | 2.33 | -0.04 | 639120.4 | 7.99 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 4.54 | 2.75 | 0.02 | 190089.95 | 20.03 | skipped_fast |
| WUSDT | IDLE | 1.04 | 2.81 | 1.56 | -0.06 | 232644.65 | 2.1 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.96 | 1.98 | -0.06 | 79769.3 | 3.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.81 | 4.38 | 4.2 | -0.18 | 91507.49 | 10.74 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.93 | 1.83 | -0.08 | 66677.32 | 19.8 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 2.62 | 0.34 | -0.04 | 56714.54 | 22.75 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 2.27 | 1.75 | -0.04 | 275775.35 | 1.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.31 | 0.62 | -0.02 | 4894.7 | 33.98 | skipped_fast |
| FLUIDUSDT | IDLE | 1.75 | 3.36 | 2.33 | -0.07 | 2242.43 | 21.86 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 3.48 | 1.76 | -0.02 | 80668.5 | 84.2 | skipped_fast |
| RWAUSDT | IDLE | 1.32 | 2.37 | 1.79 | -0.04 | 53917.07 | 7.6 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.44 | 1.45 | -0.02 | 36262.7 | 7.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.99 | 1.76 | 1.44 | -0.03 | 27595.83 | 54.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
