# Hulk DIGEST — 2026-08-22T12:35:44Z

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.66 | 0.11 | 216010245.9 | 0.66 | n/a |
| PYTHUSDT | IDLE | 1.64 | 7.83 | 2.02 | 0.05 | 51605171.23 | 1.98 | tvl≈110,752,782 |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.19 | 0.03 | 1260549.6 | 3.86 | empty_tvl |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.8 | 0.14 | 778352.41 | 5.85 | no_map |
| WUSDT | IDLE | 1.55 | 6.27 | 3.7 | 0.01 | 577935.4 | 11.65 | tvl≈1,571,378,489 |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.67 | -0.01 | 335379.1 | 37.97 | n/a |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.78 | -0.1 | 605353.54 | 3.36 | no_map |
| KITEUSDT | IDLE | 2.68 | 6.37 | 0.7 | 0.03 | 84328.51 | 0.88 | no_map |
| EDELUSDT | IDLE | 2.13 | 3.89 | 2.43 | -0.02 | 78129.71 | 11.28 | no_map |
| BIOUSDT | IDLE | 0.79 | 5.65 | 1.92 | -0.02 | 238293.0 | 12.86 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.16 | 2.56 | -0.01 | 2404.2 | 67.45 | no_map |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.3 | 0.01 | 153095.34 | 9.78 | tvl≈2,031,082 |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.88 | -0.03 | 163531.21 | 37.22 | no_map |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 70.63 | no_map |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.61 | 0.0 | 188104.92 | 6.23 | n/a |
| RIZEUSDT | IDLE | 0.47 | 1.91 | 0.44 | -0.0 | 46777.46 | 29.07 | no_map |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.12 | 0.02 | 57845.4 | 8.11 | no_map |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.02 | 5711.25 | 21.52 | tvl≈2,552,552,396 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
