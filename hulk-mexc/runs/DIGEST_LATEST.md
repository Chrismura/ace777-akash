# Hulk DIGEST — 2026-08-21T23:58:25Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.49 | 0.1 | 6227474.5 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.97 | 8.23 | 1.34 | 0.15 | 142063879.47 | 2.75 | n/a |
| HBARUSDT | IDLE | 2.62 | 6.36 | 1.16 | 0.09 | 909347.38 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 3.08 | 0.12 | 515108.04 | 35.9 | n/a |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.06 | 0.13 | 645070.97 | 8.01 | no_map |
| WUSDT | IDLE | 2.77 | 6.91 | 1.77 | 0.08 | 379002.85 | 19.54 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 1.0 | 0.04 | 545729.4 | 12.3 | no_map |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.92 | 0.02 | 187255.5 | 3.11 | n/a |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | -0.01 | 80067.22 | 21.98 | no_map |
| RIZEUSDT | IDLE | 2.19 | 9.82 | 4.18 | 0.13 | 58897.39 | 45.71 | no_map |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.41 | 0.06 | 189922.27 | 10.27 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.82 | 0.18 | 157758.05 | 12.96 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.07 | 155185.96 | 1.49 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10291.37 | 69.69 | no_map |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.84 | 0.09 | 61546.48 | 13.86 | no_map |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54478.97 | 16.37 | no_map |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.97 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
