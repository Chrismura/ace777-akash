# Hulk DIGEST — 2026-08-18T13:36:42Z

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
| XRPUSDT | IDLE | 0.52 | 0.97 | 0.5 | -0.0 | 11435696.73 | 1.0 | n/a |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 8.85 | 5.29 | -0.02 | 3405.64 | 11.79 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.76 | 8.07 | 7.37 | -0.11 | 251678.48 | 14.71 | no_map |
| QAITUSDT | IDLE | 2.06 | 27.25 | 18.66 | -0.2 | 15706.21 | 60.62 | no_map |
| CCUSDT | IDLE | 0.97 | 1.77 | 1.1 | -0.02 | 260479.22 | 9.85 | no_map |
| REDUSDT | IDLE | 1.01 | 8.44 | 7.05 | 0.17 | 100712.8 | 25.8 | tvl≈1,773,646 |
| ZBCNUSDT | IDLE | 1.0 | 1.88 | 0.8 | 0.0 | 212296.49 | 21.64 | n/a |
| RIZEUSDT | IDLE | 1.59 | 5.26 | 3.0 | -0.02 | 45955.2 | 48.33 | no_map |
| PYTHUSDT | IDLE | 0.47 | 0.9 | 0.31 | -0.03 | 202135.21 | 2.63 | tvl≈85,819,507 |
| KITEUSDT | IDLE | 1.1 | 2.17 | 0.15 | -0.01 | 70825.35 | 14.11 | no_map |
| BIOUSDT | IDLE | 1.0 | 1.95 | 0.37 | -0.0 | 76508.9 | 8.16 | n/a |
| WUSDT | IDLE | 0.43 | 0.78 | 0.6 | -0.03 | 152637.97 | 8.62 | tvl≈1,359,325,111 |
| EDELUSDT | IDLE | 0.9 | 2.25 | 1.81 | -0.06 | 78683.26 | 39.6 | no_map |
| TELUSDT | IDLE | 1.51 | 2.8 | 1.47 | -0.03 | 124682.43 | 49.7 | no_map |
| HBARUSDT | IDLE | 0.51 | 0.95 | 0.45 | -0.0 | 117604.19 | 1.52 | empty_tvl |
| QNTUSDT | IDLE | 0.39 | 0.72 | 0.34 | -0.03 | 36617.26 | 5.36 | n/a |
| RWAUSDT | IDLE | 0.42 | 0.78 | 0.43 | -0.0 | 50302.41 | 17.38 | no_map |
| FLUIDUSDT | IDLE | 0.23 | 0.41 | 0.31 | -0.04 | 135.04 | 21.05 | tvl≈2,319,812,915 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
