# Hulk DIGEST — 2026-08-22T12:29:41Z

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
| XRPUSDT | IDLE | 2.47 | 14.26 | 6.52 | 0.11 | 215813390.31 | 3.95 | n/a |
| PYTHUSDT | IDLE | 1.64 | 7.83 | 1.86 | 0.05 | 51604953.04 | 1.98 | tvl≈110,752,782 |
| HBARUSDT | IDLE | 1.25 | 4.63 | 2.02 | 0.03 | 1260394.18 | 5.13 | empty_tvl |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.87 | 0.14 | 773733.97 | 10.05 | no_map |
| WUSDT | IDLE | 1.54 | 6.27 | 3.16 | 0.02 | 577601.24 | 13.69 | tvl≈1,571,378,489 |
| ZBCNUSDT | IDLE | 2.19 | 5.77 | 3.41 | -0.02 | 370929.1 | 24.52 | n/a |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.16 | -0.09 | 606295.43 | 3.34 | no_map |
| KITEUSDT | IDLE | 2.62 | 6.33 | 0.0 | 0.06 | 83440.88 | 11.41 | no_map |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.02 | 78104.51 | 22.57 | no_map |
| BIOUSDT | IDLE | 0.77 | 5.65 | 1.01 | -0.01 | 241988.94 | 3.17 | n/a |
| QAITUSDT | IDLE | 2.25 | 4.16 | 2.33 | -0.01 | 2396.75 | 43.59 | no_map |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.57 | 0.02 | 153286.04 | 11.49 | tvl≈2,031,082 |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.93 | -0.03 | 163657.08 | 47.89 | no_map |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 76.09 | no_map |
| QNTUSDT | IDLE | 1.05 | 3.47 | 1.3 | 0.0 | 188089.34 | 7.76 | n/a |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.27 | -0.03 | 47961.88 | 46.13 | no_map |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57780.43 | 32.49 | no_map |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 22.15 | tvl≈2,552,552,396 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
