# Hulk DIGEST — 2026-10-09T01:23:19Z

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
| PYTHUSDT | IDLE | 1.61 | 7.07 | 5.64 | 0.08 | 2858908.54 | 5.02 | skipped_fast |
| WUSDT | IDLE | 0.56 | 3.56 | 0.0 | -0.07 | 4449255.88 | 7.7 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 4.14 | 0.83 | -0.04 | 1977205.88 | 5.8 | skipped_fast |
| XRPUSDT | IDLE | 0.65 | 1.3 | 0.27 | -0.03 | 53093103.66 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.44 | 0.81 | 0.51 | -0.04 | 532249700.54 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.4 | 0.33 | -0.02 | 467473020.03 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.85 | 1.91 | -0.03 | 967435.76 | 2.2 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 3.15 | 1.24 | -0.01 | 562797.05 | 9.29 | skipped_fast |
| EDELUSDT | IDLE | 1.28 | 7.62 | 1.46 | -0.09 | 425451.3 | 31.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.72 | 5.13 | 1.36 | -0.01 | 266665.18 | 7.66 | skipped_fast |
| KITEUSDT | IDLE | 1.16 | 2.68 | 2.29 | -0.07 | 67277.24 | 9.61 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 2.73 | 2.02 | -0.08 | 81602.7 | 7.22 | skipped_fast |
| CHIPUSDT | IDLE | 0.52 | 2.66 | 0.83 | -0.06 | 163924.73 | 14.25 | skipped_fast |
| REDUSDT | IDLE | 0.64 | 1.64 | 0.49 | -0.03 | 62562.12 | 7.57 | skipped_fast |
| RWAINCUSDT | IDLE | 0.84 | 3.07 | 2.7 | 0.04 | 24753.66 | 38.2 | skipped_fast |
| FLUIDUSDT | IDLE | 2.01 | 7.77 | 0.0 | -0.04 | 13816.39 | 21.44 | skipped_fast |
| TELUSDT | IDLE | 1.05 | 2.76 | 1.29 | -0.07 | 184352.06 | 43.62 | skipped_fast |
| RWAUSDT | IDLE | 0.92 | 1.75 | 0.55 | -0.05 | 54634.19 | 23.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.82 | 5.4 | 1.83 | 0.03 | 67098.5 | 212.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.75 | 0.22 | -0.03 | 32250.85 | 33.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
