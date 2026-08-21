# Hulk DIGEST — 2026-08-21T20:46:23Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.6 | 0.08 | 5549862.09 | 4.21 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.47 | 0.1 | 128763077.67 | 2.19 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.35 | 0.18 | 153345.14 | 12.16 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.53 | 0.12 | 478662.36 | 15.99 | n/a |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.17 | 0.1 | 641043.92 | 6.43 | no_map |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.86 | 0.05 | 811117.98 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.22 | 0.08 | 514355.69 | 3.08 | no_map |
| WUSDT | IDLE | 2.06 | 3.92 | 1.39 | 0.06 | 367690.28 | 13.72 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.52 | 5.33 | 2.61 | 0.01 | 188366.11 | 3.15 | n/a |
| EDELUSDT | IDLE | 2.74 | 5.01 | 3.47 | -0.04 | 81427.48 | 33.69 | no_map |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.42 | 0.02 | 56265.83 | 45.14 | no_map |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 32.07 | no_map |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.53 | 0.11 | 61072.72 | 12.11 | no_map |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.16 | 0.01 | 181675.6 | 26.76 | no_map |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.75 | 0.03 | 59923.23 | 1.57 | n/a |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.03 | 53982.52 | 8.31 | no_map |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2795.49 | 289.74 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.53 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
