# Hulk DIGEST — 2026-10-17T13:18:43Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 8.35 | 7.62 | -0.03 | 1314351.4 | 17.06 | skipped_fast |
| XRPUSDT | IDLE | 0.77 | 1.35 | 1.28 | -0.03 | 21183649.0 | 2.32 | skipped_fast |
| ETHUSDT | IDLE | 0.44 | 0.77 | 0.73 | -0.02 | 119340458.36 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.34 | 0.33 | -0.01 | 245907932.69 | 0.31 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 1.58 | 1.37 | -0.04 | 1209472.31 | 1.19 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 12.81 | 7.08 | -0.04 | 25426.04 | 5.3 | skipped_fast |
| ZBCNUSDT | IDLE | 2.14 | 4.76 | 1.47 | -0.05 | 225494.07 | 3.27 | skipped_fast |
| CHIPUSDT | IDLE | 2.6 | 4.56 | 4.22 | -0.08 | 97822.87 | 6.7 | skipped_fast |
| KITEUSDT | IDLE | 2.37 | 4.18 | 3.69 | -0.02 | 61210.3 | 10.86 | skipped_fast |
| QNTUSDT | IDLE | 1.01 | 1.77 | 1.63 | -0.03 | 592514.61 | 3.97 | skipped_fast |
| CCUSDT | IDLE | 0.61 | 1.1 | 0.85 | -0.01 | 286946.03 | 8.72 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 2.99 | 2.65 | -0.08 | 70043.1 | 7.88 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.46 | 2.24 | -0.05 | 65926.36 | 8.18 | skipped_fast |
| EDELUSDT | IDLE | 0.83 | 1.45 | 1.43 | -0.05 | 155298.62 | 13.83 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.8 | 1.63 | -0.04 | 163214.62 | 6.04 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 1.19 | 0.4 | 0.0 | 44742.29 | 52.89 | skipped_fast |
| FLUIDUSDT | IDLE | 1.62 | 2.84 | 2.76 | 0.04 | 3720.86 | 21.39 | skipped_fast |
| RWAUSDT | IDLE | 1.21 | 2.35 | 0.4 | -0.01 | 52764.42 | 15.92 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.61 | 1.46 | -0.06 | 84060.72 | 17.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.23 | 0.07 | -0.0 | 27284.31 | 4.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
