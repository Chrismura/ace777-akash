# Hulk DIGEST — 2026-08-19T00:46:14Z

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
| XRPUSDT | IDLE | 0.38 | 0.66 | 0.6 | -0.0 | 11084235.42 | 1.0 | n/a |
| PYTHUSDT | IDLE | 1.79 | 3.15 | 2.9 | -0.01 | 184639.47 | 7.85 | tvl≈87,124,382 |
| REDUSDT | IDLE | 1.1 | 7.66 | 6.55 | 0.05 | 163452.89 | 1.11 | tvl≈1,701,643 |
| CHIPUSDT | IDLE | 1.18 | 3.97 | 0.22 | -0.03 | 188669.77 | 11.16 | no_map |
| CCUSDT | IDLE | 1.05 | 1.99 | 0.75 | 0.0 | 217693.15 | 6.59 | no_map |
| ZBCNUSDT | IDLE | 0.6 | 1.17 | 0.23 | -0.0 | 146749.98 | 14.61 | n/a |
| WUSDT | IDLE | 0.6 | 1.11 | 0.65 | -0.02 | 130522.46 | 16.12 | tvl≈1,362,658,033 |
| RIZEUSDT | IDLE | 1.14 | 2.19 | 1.73 | -0.03 | 29860.98 | 48.87 | no_map |
| RWAINCUSDT | IDLE | 0.91 | 1.92 | 0.65 | -0.01 | 10586.78 | 11.85 | no_map |
| BIOUSDT | IDLE | 0.54 | 1.02 | 0.36 | 0.0 | 64528.93 | 4.06 | n/a |
| KITEUSDT | IDLE | 0.42 | 0.76 | 0.53 | -0.01 | 64772.96 | 16.4 | no_map |
| EDELUSDT | IDLE | 0.78 | 2.3 | 1.46 | -0.03 | 74075.76 | 93.65 | no_map |
| QAITUSDT | IDLE | 0.23 | 3.3 | 0.51 | -0.16 | 16068.87 | 31.31 | no_map |
| TELUSDT | IDLE | 1.23 | 2.31 | 0.96 | 0.04 | 88811.37 | 20.68 | no_map |
| HBARUSDT | IDLE | 0.94 | 1.83 | 0.3 | 0.02 | 118580.23 | 1.49 | empty_tvl |
| QNTUSDT | IDLE | 0.47 | 0.83 | 0.71 | -0.02 | 38360.4 | 5.37 | n/a |
| FLUIDUSDT | IDLE | 0.45 | 0.79 | 0.77 | -0.01 | 204.36 | 21.14 | tvl≈2,329,423,563 |
| RWAUSDT | IDLE | 0.14 | 0.26 | 0.17 | -0.01 | 51498.16 | 17.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
