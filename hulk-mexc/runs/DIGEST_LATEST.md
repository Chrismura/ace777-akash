# Hulk DIGEST — 2026-08-12T23:28:35Z

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
| XRPUSDT | IDLE | 0.66 | 1.16 | 1.02 | -0.02 | 14582692.34 | 2.0 | n/a |
| RIZEUSDT | IDLE | 2.06 | 17.24 | 5.93 | 0.18 | 52494.54 | 39.16 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 5.46 | 5.18 | -0.04 | 2019.97 | 44.1 | no_map |
| PYTHUSDT | IDLE | 1.34 | 2.42 | 1.79 | -0.05 | 329910.56 | 2.5 | tvl≈91,244,786 |
| EDELUSDT | IDLE | 2.27 | 8.33 | 4.24 | 0.08 | 71754.88 | 32.84 | no_map |
| BIOUSDT | IDLE | 2.17 | 3.94 | 2.69 | -0.04 | 62546.98 | 4.18 | n/a |
| WUSDT | IDLE | 1.76 | 3.2 | 2.16 | -0.05 | 175862.47 | 13.72 | tvl≈1,358,843,517 |
| ZBCNUSDT | IDLE | 1.52 | 2.73 | 2.07 | -0.04 | 180535.65 | 14.68 | n/a |
| QNTUSDT | IDLE | 3.1 | 5.57 | 4.21 | 0.01 | 60261.1 | 20.54 | n/a |
| KITEUSDT | IDLE | 1.53 | 2.85 | 1.38 | -0.03 | 59913.96 | 10.86 | no_map |
| REDUSDT | IDLE | 1.32 | 2.39 | 1.62 | -0.02 | 60556.3 | 13.02 | tvl≈1,565,896 |
| CHIPUSDT | IDLE | 1.02 | 2.4 | 0.73 | 0.04 | 103997.31 | 4.3 | no_map |
| CCUSDT | IDLE | 0.48 | 0.86 | 0.64 | -0.02 | 211829.59 | 6.08 | no_map |
| QAITUSDT | IDLE | 0.77 | 2.51 | 1.67 | -0.04 | 4101.28 | 60.51 | no_map |
| HBARUSDT | IDLE | 0.41 | 0.75 | 0.51 | -0.01 | 80646.33 | 1.52 | empty_tvl |
| RWAUSDT | IDLE | 0.54 | 1.0 | 0.58 | 0.02 | 52191.76 | 8.31 | no_map |
| TELUSDT | IDLE | 0.58 | 1.08 | 0.57 | 0.01 | 96396.68 | 44.4 | no_map |
| FLUIDUSDT | IDLE | 0.34 | 0.64 | 0.23 | -0.02 | 547.16 | 20.89 | tvl≈2,326,050,730 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
