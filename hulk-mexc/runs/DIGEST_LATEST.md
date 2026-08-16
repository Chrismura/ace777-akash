# Hulk DIGEST — 2026-08-16T17:06:13Z

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
| XRPUSDT | IDLE | 0.23 | 0.44 | 0.12 | -0.0 | 4946307.48 | 1.0 | n/a |
| CHIPUSDT | IDLE | 2.22 | 13.28 | 7.93 | 0.14 | 274501.47 | 7.0 | no_map |
| CCUSDT | IDLE | 1.23 | 2.29 | 1.91 | -0.03 | 350486.8 | 6.28 | no_map |
| ZBCNUSDT | IDLE | 1.47 | 2.92 | 0.16 | 0.02 | 194057.3 | 17.54 | n/a |
| QAITUSDT | IDLE | 2.08 | 6.52 | 1.55 | -0.02 | 2685.9 | 61.3 | no_map |
| RIZEUSDT | IDLE | 1.7 | 3.43 | 1.11 | -0.03 | 49782.15 | 21.96 | no_map |
| WUSDT | IDLE | 1.0 | 1.84 | 1.07 | 0.02 | 161595.7 | 12.77 | tvl≈1,361,680,705 |
| EDELUSDT | IDLE | 1.39 | 2.54 | 1.56 | -0.03 | 60454.35 | 39.6 | no_map |
| PYTHUSDT | IDLE | 0.68 | 1.33 | 0.2 | -0.01 | 123308.44 | 2.52 | tvl≈88,941,988 |
| RWAINCUSDT | IDLE | 1.55 | 4.0 | 3.85 | 0.05 | 9330.51 | 98.12 | no_map |
| BIOUSDT | IDLE | 0.52 | 0.93 | 0.68 | -0.03 | 63491.34 | 4.04 | n/a |
| KITEUSDT | IDLE | 0.47 | 0.9 | 0.25 | -0.03 | 57096.45 | 15.85 | no_map |
| REDUSDT | IDLE | 0.14 | 1.12 | 1.05 | -0.03 | 88673.76 | 25.2 | tvl≈1,593,982 |
| TELUSDT | IDLE | 1.17 | 2.31 | 0.21 | -0.02 | 97649.32 | 27.49 | no_map |
| HBARUSDT | IDLE | 0.33 | 0.62 | 0.28 | -0.01 | 75456.84 | 1.53 | empty_tvl |
| RWAUSDT | IDLE | 0.43 | 0.79 | 0.52 | -0.01 | 51699.58 | 17.5 | no_map |
| QNTUSDT | IDLE | 0.32 | 0.56 | 0.49 | -0.01 | 32807.7 | 5.24 | n/a |
| FLUIDUSDT | IDLE | 0.5 | 0.92 | 0.48 | 0.02 | 154.76 | 21.73 | tvl≈2,305,667,636 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
