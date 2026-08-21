# Hulk DIGEST — 2026-08-21T20:31:21Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.78 | 0.08 | 5522910.34 | 2.11 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.22 | 0.11 | 129092776.52 | 2.18 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.99 | 25.8 | 11.8 | 0.18 | 153701.9 | 19.27 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.38 | 0.12 | 478075.44 | 18.97 | n/a |
| CCUSDT | IDLE | 1.47 | 3.91 | 1.38 | 0.07 | 633074.0 | 4.65 | no_map |
| HBARUSDT | IDLE | 1.73 | 3.23 | 1.94 | 0.06 | 801469.46 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.37 | 0.08 | 510020.33 | 3.09 | no_map |
| WUSDT | IDLE | 2.1 | 3.92 | 1.83 | 0.06 | 365478.53 | 10.57 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.39 | 0.02 | 189813.69 | 3.14 | n/a |
| EDELUSDT | IDLE | 2.77 | 4.89 | 4.33 | -0.05 | 80341.3 | 22.68 | no_map |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.66 | 0.01 | 56203.14 | 45.77 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10934.71 | 32.14 | no_map |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.52 | 0.1 | 60995.44 | 12.11 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | no_map |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.69 | 0.02 | 183820.85 | 16.13 | no_map |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.78 | 0.04 | 59961.24 | 7.83 | n/a |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 54169.37 | 8.31 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.5 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
