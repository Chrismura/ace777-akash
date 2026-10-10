# Hulk DIGEST — 2026-10-10T07:38:07Z

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
| WUSDT | IDLE | 1.73 | 4.55 | 2.36 | -0.02 | 1833484.61 | 7.59 | skipped_fast |
| PYTHUSDT | IDLE | 1.86 | 4.6 | 3.82 | -0.07 | 1405903.27 | 1.26 | skipped_fast |
| XRPUSDT | IDLE | 0.48 | 0.89 | 0.44 | 0.0 | 24360125.0 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.21 | 0.39 | 0.14 | 0.0 | 245073986.4 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.2 | 0.37 | 0.21 | -0.0 | 132992926.23 | 0.04 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 2.21 | 1.32 | 0.02 | 1158342.53 | 2.03 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.87 | 1.83 | 0.02 | 575969.91 | 5.8 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 2.62 | 0.33 | -0.07 | 264031.73 | 20.09 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 4.04 | 2.14 | 0.07 | 89327.88 | 11.33 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 2.32 | 1.7 | 0.13 | 207959.45 | 17.52 | skipped_fast |
| RIZEUSDT | IDLE | 1.06 | 5.68 | 5.05 | 0.05 | 65891.74 | 31.9 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 2.14 | 1.84 | 0.01 | 57212.68 | 16.13 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.21 | 0.13 | -0.02 | 75554.19 | 10.56 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.88 | 1.47 | 0.01 | 61261.36 | 6.94 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.9 | 0.93 | 0.0 | 296797.59 | 6.48 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.61 | -0.01 | 52799.18 | 23.61 | skipped_fast |
| TELUSDT | IDLE | 1.41 | 2.67 | 1.01 | -0.01 | 114028.32 | 32.19 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 2.29 | 0.1 | 0.05 | 8871.5 | 124.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.77 | 1.42 | 0.81 | 0.01 | 41621.69 | 27.02 | skipped_fast |
| FLUIDUSDT | IDLE | 0.3 | 1.99 | 0.0 | 0.02 | 17215.49 | 21.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
